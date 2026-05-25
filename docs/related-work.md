# Related work

This document records the projects, initiatives, and bodies of work
that the Levels of Interoperability framework relates to. The
relationships vary in kind, and the entries are grouped accordingly:

- **Foundational work** that the framework builds on directly
- **Active engagements** where conversation and collaboration are
  current
- **Intended connections** where alignment is planned but not yet
  actively developed
- **Underlying infrastructure and standards** that the framework
  depends on as a precondition for its existence
- **Adjacent and related work** in nearby domains that may or may
  not connect directly but is clearly relevant

Entries may move between categories as the framework develops. The
groupings record the relationship as it currently stands.

## Foundational work

These are the projects and outputs that the framework builds on
directly and continues. The Zenodo metadata records the formal
"Continues" relationships for the citable items.

- **IPERION HS levels of interoperability work**, including
  Padfield, J., Fremont, W., Schmidle, W., & Sotiropoulou, S. (2022).
  Interim report on documentation of instrument parameters and
  analysis protocols across access platforms, and metadata
  requirements (1.2). Zenodo.
  [https://doi.org/10.5281/zenodo.7101169](https://doi.org/10.5281/zenodo.7101169)
- **IPERION HS final report on innovation, exploitation and
  interoperability**, Gibson, A., Castillejo, M., Carmona, P., Anglos, D.,
  Ropret, P., Radvan, R., Padfield, J., Fremout, W., Schmidle, W., &
  Sotiropoulou, S. (2023). IPERION HS D6.3 Final report on innovation,
  exploitation and interoperability (1.0). Zenodo.
  [https://doi.org/10.5281/zenodo.7849169](https://doi.org/10.5281/zenodo.7849169)
- **HPSWG-Models**, the Heritage Painting Semantic Web Group's
  ongoing work on CIDOC CRM-based semantic models, which provided
  several of the concepts now formalised as recommended
  implementations and entity definitions in this framework.
  [https://github.com/RICHeS-UKRI/HPSWG-Models](https://github.com/RICHeS-UKRI/HPSWG-Models)

## Active engagements

These are projects and initiatives the framework is currently in
conversation with and where development is mutually shaped.

- **E-RIHS DIGILAB**, particularly the conversation on semantic
  artefacts, recommended implementations, and a federated registry
  that prompted the current articulation of the framework.
  [https://www.e-rihs.eu/](https://www.e-rihs.eu/)
- **HSPortal**, a related E-RIHS DIGILAB infrastructure that hosts a
  growing range of heritage science ontologies and other semantic artefacts.
  [https://hsportal.espadon.net/](https://hsportal.espadon.net/)
- **RICHeS Heritage Science Data Service (HSDS)**, the UK Research
  Infrastructure for Conservation and Heritage Science data service.
  Specifically, the Heritage Paint Samples Working Group within HSDS
  has been developing lists of required entities and metadata schemas
  as a practical implementation of various aspects of the framework.
  [https://hsds.ac.uk/](https://hsds.ac.uk/)
- **ECHOES**, the European Cloud for Heritage
  Open Science cluster currently shaping much of what will become
  the European Collaborative Cloud for Cultural Heritage. Several
  of the framework's transitions and tools and services have natural
  homes in the ECHOES architectural conversation. Work within ECHOES
  is also developing the scope and form of Heritage Science Digital Twins
  which has directly informed aspects of the framework.

## Intended or possible connections

These are initiatives the framework is designed to connect to, and
where active engagement is anticipated but not yet established.

- **ECCCH (European Collaborative Cloud for Cultural Heritage)**,
  the emerging European infrastructure that will inherit the
  architectural patterns developed in ECHOES and its sister projects.
  The framework is positioned to provide a common reference for
  participating organisations regardless of their current treatment
  level.
- **Linked.art**, the community profile of CIDOC CRM for art
  museum cataloguing. Alignment between this framework's
  recommended implementations and the Linked.art profile is an
  explicit design objective where the two domains overlap.
  [https://linked.art/](https://linked.art/)
- **CIDOC CRM Special Interest Group (CRM-SIG)**, the maintainers
  of the CIDOC CRM standard. Coordination with the CRM-SIG process
  is intended for the formal validation of recommended
  implementations within the framework.
  [https://www.cidoc-crm.org/](https://www.cidoc-crm.org/)
- **Heritage Samples Registry**, which is being developed in parallel
  and is expected to provide concrete worked examples of resources
  reaching T06 and above through IGSN-based persistent identification.
  [https://heritagesamples.org/](https://heritagesamples.org/)

## Underlying infrastructure and standards

These are the standards, vocabularies, identifier infrastructures,
and aggregator services that the framework depends on as preconditions
for the treatment levels and transitions it documents. The framework
does not actively develop these but cannot function without them.

- **FAIR principles**, Wilkinson et al. (2016), with the GO FAIR
  initiative providing the current reference.
  [https://www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)
- **CIDOC CRM** and its accepted extensions including CRMsci,
  CRMdig, and CRMarchaeo, providing the formal ontology underpinning
  the semantic levels of the framework.
  [https://cidoc-crm.org/](https://cidoc-crm.org/)
- **Persistent identifier infrastructures**, including DOI (via
  DataCite and Crossref), ORCID, IGSN (via SESAR and similar
  services), ROR, ARK, and Handle. These provide the identifier
  layer required for treatment level T06 and above.
  [UK - Towards a National Collection PIDResources](https://tanc-ahrc.github.io/PIDResources/)
- **Reference vocabularies**, including the Getty Art and
  Architecture Thesaurus (AAT), Wikidata, and domain-specific
  thesauri. These provide the vocabulary alignment required for
  treatment level T05. [Getty AAT](https://www.getty.edu/research/tools/vocabularies/aat/) -
  [Wikidata](https://www.wikidata.org/)  
- **Metadata standards**, including Spectrum (Collections Trust),
  LIDO, and the schemas used by national and international
  aggregators. These provide the shared schemas required for
  treatment level T04b. [Spectrum](https://collectionstrust.org.uk/spectrum/) - [LIDO](https://lido-schema.org/documents/primer/latest/lido-primer.html)  
- **Aggregators and federation services**, including ArtUK, the
  Museum Data Service (MDS), and Europeana, which provide the federation
  infrastructure that could support treatment level T08a and inform
  the schema work at T04b.
  [ArtUK](https://artuk.org/) - [MDS](https://museumdata.uk/) - [Europeana](https://www.europeana.eu/)

## Adjacent and related work

These are bodies of work in nearby domains that the framework does
not currently connect to formally but which are clearly relevant.
They are listed here for context and as candidates for future
investigation or connection.

- **Heritage Science Digital Twin initiatives**, including specific
  projects exploring what Digital Twins mean for heritage objects,
  sites, and collections. The framework's T09 level is positioned
  in this space but the specifications themselves remain under
  active development across multiple communities.
- **FAIR Digital Objects (FDO) initiative**, which articulates a
  vision of FAIR-compliant digital objects with rich metadata and
  type-bound operations. The relationship between FDOs and the
  framework's treatment levels is potentially deep but has not
  yet been worked out in detail.
  [https://fairdo.org/](https://fairdo.org/)
- **EOSC (European Open Science Cloud)**, the European federated
  infrastructure for research data. EOSC's adoption patterns
  influence what is realistic at higher treatment levels for
  European heritage science. [https://eosc.eu/](https://eosc.eu/)
- **Research data management initiatives** at institutional and
  national level, which provide much of the practical context in
  which researchers move from T01 to T03 in their daily work. The
  framework's transitions X01 and X02 in particular depend on the
  patterns and tooling these initiatives develop.
- **Access frameworks** including E-RIHS ARCHLAB and similar transnational
  access programmes, which deliver findability and accessibility
  for resources at lower treatment levels through human and
  infrastructural means. The framework currently treats these as
  outside its boundary (see the FAIR discussion in the main README),
  but they are central to how heritage science actually operates.

## Notes on the categorisation

The five categories above are working distinctions rather than
fixed taxonomies. Some entries could plausibly sit in more than one
category. The Heritage Samples Registry, for example, could be
treated as an active engagement once specific datasets are linked
into the framework as examples, rather than an intended connection.

The categorisation also reflects the position of the framework at
a specific moment. As the framework develops, entries are expected
to move toward more active relationships, and new categories may
emerge (notably around supported FAIR through access frameworks,
which currently sits in adjacent work but may become a substantive
extension of the framework itself).

Suggestions for additions, corrections, or recategorisation are
welcome through the repository's contribution process.
