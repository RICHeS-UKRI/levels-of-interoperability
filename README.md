# Levels of Interoperability for Heritage Science

A framework for describing and planning the development of data practice
in heritage science, from tacit personal records through to integrated
digital constructs.

This repository holds the working record of the framework. The framework
itself is the conceptual structure described here; the repository captures
that structure as versioned data alongside the tooling to validate it
and produce derived outputs.

## What the framework is

The framework recognises that researchers and institutions hold a wide
range of resources, that those resources can be organised and described
in many different ways, and that the long-term goal of interoperable,
FAIR, and reusable heritage science data depends on a clear path from
where any given person or institution stands now to where they could
be in the future.

It describes this path through four interconnected datasets:

- **Treatment Levels** describe how resources can be organised,
  documented, and made interoperable, from tacit and unstructured
  through to integrated digital constructs.

- **Resources** is the inventory of material types researchers and
  institutions may hold, independent of how those materials are
  treated.

- **Tools and Services** records the tools, services, infrastructure,
  and reference resources that support work in the framework.

- **Transitions** describes the work involved in moving between
  treatment levels, both upward through the ladder and across the
  framework, including cross-cutting movements like accessibility
  and licensing improvements.

These four datasets reference each other extensively, so that a
researcher or institution can trace from any resource type to the
levels at which it can realistically be treated, the transitions
involved in reaching higher treatment levels, and the tools and
services that support those transitions.

## Repository layout

```
.
├── README.md                       # this file
├── data/                           # JSON source of truth
│   ├── treatment-levels.json
│   ├── resources.json
│   ├── tools-and-services.json
│   ├── transitions.json
│   └── vocabularies.json
├── schemas/                        # JSON Schema definitions
│   ├── definitions.schema.json
│   ├── treatment-levels.schema.json
│   ├── resources.schema.json
│   ├── tools-and-services.schema.json
│   ├── transitions.schema.json
│   └── vocabularies.schema.json
├── scripts/
│   ├── check_consistency.py        # validation
│   └── build_combined.py           # generate xlsx
├── build/                          # generated outputs (not versioned)
└── docs/                           # future presentation layer
```

## Identifier conventions

Each entry across the four datasets has a stable identifier that does
not change once assigned:

- `R01`, `R02`, ... for resources
- `T01`, `T02`, ..., with sublevels like `T04a`, `T07b`, and a
  qualified `T06+`, for treatment levels
- `S01`, `S02`, ... for tools and services
- `X01`, `X02`, ... for transitions
- `V01`, `V02`, ... for vocabulary terms

Identifiers are tags, not positions. The presentation order is given
by the separate `order` field on each entry, which uses integer values
with gaps of ten to allow easy insertion. Renumbering identifiers is
not permitted because it would break cross-references.

## Working with the framework

### Make a change

Edit the relevant JSON file in `data/`. Each file is an array of entries
with cross-references to entries in other files using the identifier
conventions above.

### Validate

```
pip install jsonschema referencing
python scripts/check_consistency.py
```

This validates each data file against its JSON Schema and checks that
all cross-references resolve to existing identifiers.

### Build a combined spreadsheet

```
pip install openpyxl
python scripts/build_combined.py
```

This produces a single xlsx in `build/` with one tab per dataset, plus
a vocabularies tab and an overview. The spreadsheet is a read-only view
of the framework data and is rebuilt on every release. Edits should be
made to the JSON files, not to the spreadsheet.

## Cross-cutting attributes

Alongside the treatment ladder itself, the framework recognises several
attributes that apply across all levels:

- **Scope**: whether something operates at individual, project,
  institutional, or wider scale.
- **Accessibility**: whether and how a resource can be reached by
  those who would use it.
- **Licensing**: whether re-use terms for a resource are clear and
  machine-readable, addressing the R in FAIR.
- **Population completeness**: how fully a schema-bearing resource
  has been populated within its level.

These are recorded both at the level definitions (where they shape
expectations for each level) and on individual resources (where they
describe behaviour in practice).

## FAIR and the framework

The framework operationalises FAIR rather than restating it. Findability
emerges from documented description and persistent identifiers (T03
upward, T06 in particular). Accessibility is the cross-cutting attribute
of the same name. Interoperability is the trajectory through T04 to
T07b. Reusability emerges from T08 onward when documentation, vocabulary,
semantics, identifiers, and licensing all combine.

## Licence

To be confirmed. Data: likely CC BY 4.0. Scripts: likely MIT or Apache 2.0.

## Citation

To be confirmed once first release is deposited via Zenodo.

## Related work

The framework draws on and connects to:

- IPERION HS work on levels of interoperability, including
  https://doi.org/10.5281/zenodo.7101169 and
  https://doi.org/10.5281/zenodo.7849169
- HPSWG-Models semantic modelling work
- RICHeS Heritage Science Data Service architecture
- E-RIHS DIGILAB activities on semantic artefacts and registries
- Linked.art, CRM-SIG, and CIDOC CRM community work
- Heritage Samples Registry

## License
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
