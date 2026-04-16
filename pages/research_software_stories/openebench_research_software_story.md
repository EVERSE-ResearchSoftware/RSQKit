---
title: "Research Software Story - OpenEBench"
description: "OpenEBench is an open, community-driven platform for benchmarking and monitoring bioinformatics software, enabling transparent performance evaluation and improved research software quality."
contributors: [Laura Portell-Silva, José María Fernández, Eva Martín del Pico]
page_id: openebench_research_software_story
---

## The Problem 
### Researchers struggle to compare and evaluate bioinformatics tools reliably and improve their quality

Life sciences research depends heavily on bioinformatics software: tools, workflows and web services that analyse complex biological data.
As the number of available methods grows, researchers and developers face persistent challenges:
- Lack of objective comparison between tools performing similar tasks
- Difficulty assessing software quality beyond published claims
- Limited reproducibility of performance evaluations
- Fragmented benchmarking efforts, often confined to individual projects or short-lived challenges

Without shared, transparent benchmarking events, users struggle to choose appropriate tools, developers lack systematic feedback, and communities miss opportunities for collective improvement.
**{% tool "openebench" %}** addresses these challenges by providing an open, community-driven benchmarking and monitoring platform for bioinformatics software.
OpenEBench brings together scientific benchmarking and technical monitoring to help users compare and improve software.

It enables scientific communities to:
- Define reference datasets and evaluation metrics.
- Run standardised, reproducible benchmarking events.
- Compare tools fairly and transparently.
- Track software performance and quality over time.

Beyond performance benchmarking, {% tool "openebench" %} also contributes to improve research software quality through its {% tool "openebench-observatory" %}.
The observatory aggregates metadata from multiple sources and evaluates software against FAIR principles (Findable, Accessible, Interoperable, Reusable), providing:
- FAIRness indicators and scores.
- Visibility into software maturity and maintenance practices.
- Actionable insights for developers to improve their software.

This dual focus on performance and quality distinguishes OpenEBench from traditional benchmarking efforts.

## User Community 
### Developers and researchers collaborate to improve bioinformatics tools

{% tool "openebench" %} serves a diverse and interconnected user base:

- *Bioinformatic tools developers*, who want objective feedback on performance and visibility for their tools.
- *Scientific communities*, who define domain-specific benchmarking events aligned with real research needs.
- *Researchers and end-users*, who need trustworthy information to select appropriate tools.
- *Infrastructure providers and funders*, who seek insight into software quality, sustainability and impact.

The platform is designed to be community-led: benchmarking events are defined and governed by the communities that use them.

## Technical Aspects  
{% tool "openebench" %} is built as a modular, service-oriented platform designed to support reproducible benchmarking and software observatory.

### Languages and Codebase

The {% tool "openebench" %} codebase is primarily developed using:
- {% tool "java" %} and {% tool "python" %} for data processing and benchmarking workflows infrastructure.
- Observatory backend: {% tool "python" %} (FastAPI as REST API paradigm) and {% tool "javascript" %} (Node/Express.js).
- {% tool "java" %} for REST and graphQL services of the [scientific benchmarking][OPENEBENCH_SCI], and {% tool "python" %} for accessory REST services.
- {% tool "php" %} for {% tool "openebench-vre" %}, which uses bash and Nextflow for orchestrating benchmarking pipelines.
- Most of the frontends are written in Javascript based on Nuxt framework.

The platform is organised into independent but interoperable components, enabling reuse across different benchmarking communities and facilitating long-term maintenance and extension.
All core components are open source and developed following collaborative good practices.

### Architecture and Deplopyment

{% tool "openebench" %} follows a cloud-ready, container-based architecture:

- OpenEBench provides RESTful APIs for data access and integration.
- Most of services and tools are packaged using Docker containers to ensure reproducibility and portability.
- Benchmarking workflows are executed within a Virtual Research Environment (VRE).
- {% tool "mongodb" %} is deployed as a core backend service supporting scalable data storage and querying.

### Interoperabiltiy and Integration
The platform integrates with external registries, repositories and monitoring services to harvest software metadata and usage signals. 

## Software Practices 
### OpenEBench follows open-source and FAIR-aligned practices

{% tool "openebench" %} is developed as an open‑source platform with code repositories hosted on {% tool "github" %}. Contributors follow community standards for version control, code review, and integration.

- *Version control*: Both BSC {% tool "gitlab" %} and GitHub‑based repositories with clear topic tagging for discoverability.
- *Code review*: Pull requests are used to ensure changes align with project objectives and maintain quality standards.
- *Testing and validation*: Benchmarking workflows, maintained by the different scientific communities (usually in {% tool "github" %}), are encouraged to include validation and verification of results.
- *Community feedback*: Issues and discussions capture user feedback, drive prioritisation, and support continuous improvement across releases.

## Developer Community 

{% tool "openebench" %} is developed and maintained at the Technologies for Biomedical Research Laboratory
 (TechBioLab) at the [Barcelona Supercomputing Center (BSC)][BSC] as part of the [ELIXIR Tools Platform][TOOLS_PLATFORM].
 New contributors can get started by exploring the different [git repositories][OPENEBENCH_GITHUB] and participating in [community discussions][OPENEBENCH_SCI].
 The platform encourages collaborative development and feedback to continuously improve benchmarking events.

## Tools 
### OpenEBench uses tools to be FAIR-compliant

{% tool "openebench" %} relies on a combination of development and deployment tools that streamline scientific benchmarking workflow creation, testing, and containerisation.
These tools ensure the software remains stable and reproducible across environments. Key tools include:
- *{% tool "git" %} / {% tool "github" %}*: version control and code collaboration.
- *{% tool "docker" %}*: containerizing workflows for reproducibility.
- *Workflow languages*: {% tool "nextflow" %} for standardised benchmarking pipelines from the different scientific communities.

## FAIR & Open 
### OpenEBench is fully aligned with FAIR and open science principles

{% tool "openebench" %} promotes openness and FAIR compliance across its code, workflows, and benchmarking results:

**Findable**:
- OpenEBench codebases and data models are publicly available through multiple repositories hosted on {% tool "github" %} and BSC’s {% tool "gitlab" %}.
- OpenEBench uses persistent identifiers (PIDs) to uniquely identify benchmarking related digital objects (e.g. challenges, datasets, metrics, and results), supporting finability.

**Accessible**:
- Users can access software, documentation, and benchmark data freely, and contribute via {% tool "github" %} or BSC's {% tool "gitlab" %}.
- The different git repositories holding both the code and the data model are publicly hosted both on {% tool "github" %} and BSC's {% tool "gitlab" %} under open-source licenses.

**Interoperable**:
- APIs and workflows use either standard or documented formats to support interoperability. Some examples:
  * Metrics workflows provided by the communities must be written in Nextflow. The steps must depend on 
    docker images, which should be public and distributable. Their docker recipes and build process should be public.
    When the docker images are not distributable, the docker recipes must be public.
    All the metrics workflows from the different communities have to support
    the very same minimal named parameters, and produce their main outputs listing the metrics
    assigned to the assessed participants, following a [minimal dataset data model][MODEL]. An example of a dataset following the model [here][MODEL_EXAMPLE].
  * REST API both returns and accepts documents following the OEB benchmarking data model,
    described in JSON Schema with several relational extensions ([link to the 1.0 model][JSON_MODEL], [examples of 1.0 model][JSON_EXAMPLE] and [graphical representation of the 1.0 model][MODEL_GRAF]).
    
**Reusable**:
- The different git repositories holding both the code and the data model are publicly hosted both on {% tool "github" %}
  and BSC's Gitlab under open-source licenses ({% tool "apache-license" %}), {% tool "cc-by-license" %}, {% tool "lgplv2 %}, etc...).
- Metrics workflows provided by the communities must be written in Nextflow and depend on Docker images, enabling reuse.
- The development process is transparent, with scientific and technical benchmarking communities involvement in decisions and feature development.

## Documentation 

{% tool "openebench" %} provides multiple documentation resources to help users navigate the platform and contribute to development:
- Main entry point: [OpenEBench ReadTheDocs][OPENEBENCH_DOC]
- [README files][OPENEBENCH_README] for each repository explaining setup and usage
- [Templates and examples][OPENEBENCH_TEMPLATES] for workflow examples and benchmarking pipelines
- [Step-by-step guides][OPENEBENCH_GUIDE] for developers and administrators

## Sustainability 

As mentioned above, {% tool "openebench" %} is maintained by the TechBioLab at BSC and supported by the ELIXIR Tools Platform.
Governance combines core team oversight with community input. Funding from ELIXIR and institutional support ensures ongoing development, maintenance, and future-proofing.
The project emphasises modular design, open standards, and containerization to reduce risks and facilitate long-term sustainability.

## References 

- [OpenEBench main entry point][OPENEBENCH]
- [OpenEBench technical monitoring][[OPENEBENCH_TECH]
- [OpenEBench scientific benchmarking][OPENEBENCH_SCI]
- [OpenEBench Software Observatory][OPENEBENCH_OB]
- [OpenEBench ReadTheDocs][OPENEBENCH_DOC]
- [OpenEBEnch Scientific benchmarking data model][OPENEBENCH_MODEL]
- [OpenEBEnch Scientific benchmarking REST and graphQL code][OPENEBENCH_API]
- [Quest for Orthologs benchmarking metrics computation workflow][OPENEBENCH_BENCH]
- [OpenEBench Scientific benchmarking tools][OPENEBENCH_TOOLS]
- [OpenEBench Scientific level2 ingestion tools][OPENEBENCH_ING_TOOLS]
- [OpenEBench Scientific frontend code][OPENEBENCH_FRONTEND]
- [OpenEBench Technical monitoring repository metadata enricher][OPENEBENCH_TECH_METADATA]

<!-- External References embedded as links -->

- [OPENBENCH_GITHUB]: https://github.com/inab/openebench-hub
- [OPENEBENCH_TECH]: https://openebench.bsc.es/tool
- [OPENEBENCH_SCI]: https://openebench.bsc.es/benchmarking
- [OPENEBENCH_DOC]: https://openebench.readthedocs.io/en/latest/
- [OPENEBENCH_MODEL]: https://github.com/inab/benchmarking-data-model/
- [OPENEBENCH_API]: https://gitlab.bsc.es/inb/elixir/openebench/openebench-backend-legacy
- [OPENEBENCH_BENCH]: https://github.com/qfo/benchmark-webservice
- [OPENEBENCH_TOOLS]: https://gitlab.bsc.es/inb/elixir/openebench/oeb-sci-admin-tools
- [OPENEBENCH_ING_TOOLS]: https://github.com/inab/OEB_level2_data_migration
- [OPENEBENCH_FRONTEND]: https://github.com/inab/openEBench-nuxt
- [OPENEBENCH_TECH_METADATA]: https://github.com/inab/opeb-repo-enricher
- [OPENEBENCH_README]: https://github.com/inab/openebench-hub
- [OPENEBENCH_TEMPLATES]: https://github.com/inab/TCGA_benchmarking_workflow
- [OPENEBENCH_GUIDE]: https://openebench.readthedocs.io/en/latest/how_to/3_participate.html
- [BSC]: https://www.bsc.es/
- [TOOLS_PLATFORM]: https://elixir-europe.org/platforms/tools
- [MODEL]: https://github.com/inab/OEB_level2_data_migration/blob/master/oeb_level2/schemas/minimal_bdm_oeb_level2.yaml
- [MODEL_EXAMPLE]: https://github.com/inab/OEB_level2_data_migration/tree/master/minimal_dataset_examples
- [JSON_MODEL]: https://github.com/inab/benchmarking-data-model/tree/master/json-schemas/1.0.x
- [JSON_EXAMPLE]: https://github.com/inab/benchmarking-data-model/tree/master/prototype-data/1.0.x
- [MODEL_GRAF]: https://github.com/inab/benchmarking-data-model/blob/master/json-schemas/openebench-bdm-1.0.x.dot.pdf
