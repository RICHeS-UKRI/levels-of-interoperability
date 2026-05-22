#!/usr/bin/env python3
"""Validate the framework data files against their JSON schemas and check cross-references.

Run from the repository root: python scripts/check_consistency.py

Exits with status 0 if all checks pass, 1 otherwise.
"""

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:
    print("Required packages missing. Install with:")
    print("  pip install jsonschema referencing")
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = REPO_ROOT / "schemas"

DATA_FILES = [
    ("treatment-levels", "treatment-levels.json", "treatment-levels.schema.json"),
    ("resources", "resources.json", "resources.schema.json"),
    ("tools-and-services", "tools-and-services.json", "tools-and-services.schema.json"),
    ("transitions", "transitions.json", "transitions.schema.json"),
    ("vocabularies", "vocabularies.json", "vocabularies.schema.json"),
]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_registry():
    """Build a referencing registry including all schemas so $refs resolve locally."""
    registry = Registry()
    for schema_path in SCHEMA_DIR.glob("*.schema.json"):
        schema = load_json(schema_path)
        resource = Resource(contents=schema, specification=DRAFT202012)
        # Register under the canonical $id and the filename for local relative refs.
        if "$id" in schema:
            registry = registry.with_resource(uri=schema["$id"], resource=resource)
        registry = registry.with_resource(uri=schema_path.name, resource=resource)
    return registry


def validate_schemas(registry):
    """Validate each data file against its schema."""
    errors = []
    for name, data_filename, schema_filename in DATA_FILES:
        data_path = DATA_DIR / data_filename
        schema_path = SCHEMA_DIR / schema_filename
        if not data_path.exists():
            errors.append(f"[{name}] data file missing: {data_path}")
            continue
        if not schema_path.exists():
            errors.append(f"[{name}] schema file missing: {schema_path}")
            continue
        schema = load_json(schema_path)
        data = load_json(data_path)
        validator = Draft202012Validator(schema, registry=registry)
        for err in validator.iter_errors(data):
            path = "/".join(str(p) for p in err.absolute_path)
            errors.append(f"[{name}] schema error at {path}: {err.message}")
    return errors


def collect_ids(data, key="entries", id_field="id"):
    """Return the set of ids in a data file's entries list."""
    if key not in data:
        return set()
    return {entry[id_field] for entry in data[key] if id_field in entry}


def check_cross_references():
    """Check that every cross-reference resolves to an existing identifier."""
    errors = []

    levels = load_json(DATA_DIR / "treatment-levels.json")
    resources = load_json(DATA_DIR / "resources.json")
    tools = load_json(DATA_DIR / "tools-and-services.json")
    transitions = load_json(DATA_DIR / "transitions.json")

    level_ids = collect_ids(levels)
    resource_ids = collect_ids(resources)
    tool_ids = collect_ids(tools)
    transition_ids = collect_ids(transitions)

    def check_refs(entries, source_name, field, target_ids, target_name):
        for entry in entries:
            for ref in entry.get(field, []) or []:
                if ref not in target_ids:
                    errors.append(
                        f"[{source_name}:{entry['id']}] {field} references "
                        f"{target_name} '{ref}' which does not exist"
                    )

    # Treatment levels: typicallyRequires references levels
    check_refs(levels["entries"], "treatment-levels", "typicallyRequires", level_ids, "level")

    # Resources: realisticCeilingLevels references levels
    check_refs(resources["entries"], "resources", "realisticCeilingLevels", level_ids, "level")

    # Tools: handlesResources references resources, supportsLevels references levels,
    # enablesTransitions references transitions, dependsOn references tools
    check_refs(tools["entries"], "tools-and-services", "handlesResources", resource_ids, "resource")
    check_refs(tools["entries"], "tools-and-services", "supportsLevels", level_ids, "level")
    check_refs(tools["entries"], "tools-and-services", "enablesTransitions", transition_ids, "transition")
    check_refs(tools["entries"], "tools-and-services", "dependsOn", tool_ids, "tool")

    # Transitions: from/to reference levels, resourcesAffected references resources,
    # toolsAndServicesInvolved references tools
    check_refs(transitions["entries"], "transitions", "from", level_ids, "level")
    check_refs(transitions["entries"], "transitions", "to", level_ids, "level")
    check_refs(transitions["entries"], "transitions", "resourcesAffected", resource_ids, "resource")
    check_refs(transitions["entries"], "transitions", "toolsAndServicesInvolved", tool_ids, "tool")

    return errors


def check_orphans():
    """Warn about identifiers that no other file references.

    These are not errors but they may indicate gaps in the analysis. Returned
    as warnings, not errors.
    """
    warnings = []

    levels = load_json(DATA_DIR / "treatment-levels.json")
    resources = load_json(DATA_DIR / "resources.json")
    tools = load_json(DATA_DIR / "tools-and-services.json")
    transitions = load_json(DATA_DIR / "transitions.json")

    # Collect all references made anywhere
    referenced_levels = set()
    referenced_resources = set()
    referenced_tools = set()
    referenced_transitions = set()

    for entry in levels["entries"]:
        for ref in entry.get("typicallyRequires", []) or []:
            referenced_levels.add(ref)

    for entry in resources["entries"]:
        for ref in entry.get("realisticCeilingLevels", []) or []:
            referenced_levels.add(ref)

    for entry in tools["entries"]:
        for ref in entry.get("handlesResources", []) or []:
            referenced_resources.add(ref)
        for ref in entry.get("supportsLevels", []) or []:
            referenced_levels.add(ref)
        for ref in entry.get("enablesTransitions", []) or []:
            referenced_transitions.add(ref)
        for ref in entry.get("dependsOn", []) or []:
            referenced_tools.add(ref)

    for entry in transitions["entries"]:
        for ref in (entry.get("from", []) or []) + (entry.get("to", []) or []):
            referenced_levels.add(ref)
        for ref in entry.get("resourcesAffected", []) or []:
            referenced_resources.add(ref)
        for ref in entry.get("toolsAndServicesInvolved", []) or []:
            referenced_tools.add(ref)

    # Find orphans
    for entry in resources["entries"]:
        rid = entry["id"]
        if rid not in referenced_resources:
            # Check whether any tool or transition uses 'all resources' flags
            if any(t.get("handlesAllResources") for t in tools["entries"]):
                continue
            if any(t.get("resourcesAffectedAllResources") for t in transitions["entries"]):
                continue
            warnings.append(f"orphan resource: {rid} ({entry['name']}) is not referenced anywhere")

    for entry in tools["entries"]:
        sid = entry["id"]
        if sid not in referenced_tools:
            # Check whether it is referenced in transitions through toolsAndServicesInvolved
            in_transitions = any(
                sid in (t.get("toolsAndServicesInvolved", []) or [])
                for t in transitions["entries"]
            )
            if not in_transitions:
                warnings.append(f"orphan tool: {sid} ({entry['name']}) is not referenced anywhere")

    return warnings


def main():
    print("Building schema registry...")
    registry = build_registry()

    print("Validating data files against schemas...")
    schema_errors = validate_schemas(registry)

    print("Checking cross-references...")
    ref_errors = check_cross_references()

    print("Checking for orphan identifiers...")
    orphan_warnings = check_orphans()

    if schema_errors:
        print(f"\nSchema validation errors ({len(schema_errors)}):")
        for err in schema_errors:
            print(f"  {err}")

    if ref_errors:
        print(f"\nCross-reference errors ({len(ref_errors)}):")
        for err in ref_errors:
            print(f"  {err}")

    if orphan_warnings:
        print(f"\nOrphan warnings ({len(orphan_warnings)}):")
        for warn in orphan_warnings:
            print(f"  {warn}")

    if schema_errors or ref_errors:
        print(f"\nFAILED: {len(schema_errors)} schema errors, {len(ref_errors)} reference errors")
        sys.exit(1)
    else:
        print(f"\nOK: all checks passed ({len(orphan_warnings)} warnings)")
        sys.exit(0)


if __name__ == "__main__":
    main()
