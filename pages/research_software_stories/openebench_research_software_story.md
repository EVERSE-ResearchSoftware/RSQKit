---
title: "Research Software Story - OpenEBench"
description: "OpenEBench is an open, community-driven platform for benchmarking and monitoring bioinformatics software, enabling transparent performance evaluation and improved research software quality."
contributors: [Laura Portell-Silva, José María Fernández, Eva Martín del Pico]
page_id: openebench_research_software_story
type: research_software_story # leave this as is
---

## The Problem 
### Researchers struggle to compare and evaluate bioinformatics tools reliably and improve their quality

Life sciences research depends heavily on bioinformatics software: tools, workflows and web services that analyse complex biological data. As the number of available methods grows, researchers and developers face persistent challenges:
- Lack of objective comparison between tools performing similar tasks
- Difficulty assessing software quality beyond published claims
- Limited reproducibility of performance evaluations
- Fragmented benchmarking efforts, often confined to individual projects or short-lived challenges

Without shared, transparent benchmarking events, users struggle to choose appropriate tools, developers lack systematic feedback, and communities miss opportunities for collective improvement. **[OpenEBench](https://openebench.bsc.es/dashboard/)** addresses these challenges by providing an open, community-driven benchmarking and monitoring platform for bioinformatics software. OpenEBench brings together scientific benchmarking and technical monitoring to help users compare and improve software.

It enables scientific communities to:
- Define reference datasets and evaluation metrics.
- Run standardised, reproducible benchmarking events.
- Compare tools fairly and transparently.
- Track software performance and quality over time.

Beyond performance benchmarking, OpenEBench also contributes to improve research software quality through its [Software Observatory](https://openebench.bsc.es/observatory/Trends). The observatory aggregates metadata from multiple sources and evaluates software against FAIR principles (Findable, Accessible, Interoperable, Reusable), providing:
- FAIRness indicators and scores.
- Visibility into software maturity and maintenance practices.
- Actionable insights for developers to improve their software.

This dual focus on performance and quality distinguishes OpenEBench from traditional benchmarking efforts.

## User Community 
### Developers and researchers collaborate to improve bioinformatics tools

OpenEBench serves a diverse and interconnected user base:

- *Bioinformatic tools developers*, who want objective feedback on performance and visibility for their tools.
- *Scientific communities*, who define domain-specific benchmarking events aligned with real research needs.
- *Researchers and end-users*, who need trustworthy information to select appropriate tools.
- *Infrastructure providers and funders*, who seek insight into software quality, sustainability and impact.

The platform is designed to be community-led: benchmarking events are defined and governed by the communities that use them.

## Technical Aspects  
OpenEBench is built as a modular, service-oriented platform designed to support reproducible benchmarking and software observatory.

### Languages and Codebase

The OpenEBench codebase is primarily developed using:
- Java and Python for data processing and benchmarking workflows infrastructure.
- Observatory backend: Python (FastAPI as REST API paradigm) and javascript (Node/Express.js).
- Java for REST and graphQL services of the scientific benchmarking, and Python for accessory REST services.
- PHP for OpenEBench VRE, which uses bash and Nextflow for orchestrating benchmarking pipelines.
- Most of the frontends are written in Javascript based on Nuxt framework.

The platform is organised into independent but interoperable components, enabling reuse across different benchmarking communities and facilitating long-term maintenance and extension. All core components are open source and developed following collaborative good practices.

### Architecture and Deplopyment

OpenEBench follows a cloud-ready, container-based architecture:

- OpenEBench provides RESTful APIs for data access and integration.
- Most of services and tools are packaged using Docker containers to ensure reproducibility and portability.
- Benchmarking workflows are executed within a Virtual Research Environment (VRE).
- MongoDB is deployed as a core backend service supporting scalable data storage and querying.

### Interoperabiltiy and Integration
The platform integrates with external registries, repositories and monitoring services to harvest software metadata and usage signals. 

## Software Practices 
### OpenEBench follows open-source and FAIR-aligned practices

OpenEBench is developed as an open‑source platform with code repositories hosted on GitHub. Contributors follow community standards for version control, code review, and integration.

- *Version control*: Both BSC Gitlab and GitHub‑based repositories with clear topic tagging for discoverability.
- *Code review*: Pull requests are used to ensure changes align with project objectives and maintain quality standards.
- *Testing and validation*: Benchmarking workflows, maintained by the different scientific communities (usually in GitHub), are encouraged to include validation and verification of results.
- *Community feedback*: Issues and discussions capture user feedback, drive prioritisation, and support continuous improvement across releases.

## Developer Community 
### Add a short one-two liner subtitle about how the software is being adopted for usage and how a community is being built around it

OpenEBench is developed and maintained at the Technologies for Biomedical Research Laboratory
 (TechBioLab) at the [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) as part of the [ELIXIR Tools Platform](https://elixir-europe.org/platforms/tools). New contributors can get started by exploring the different git repositories (https://github.com/inab/openebench-hub) and participating in community discussions (https://openebench.bsc.es/benchmarking). The platform encourages collaborative development and feedback to continuously improve benchmarking events.

## Tools 
### OpenEBench uses tools to be FAIR-compliant

OpenEBench relies on a combination of development and deployment tools that streamline scientific benchmarking workflow creation, testing, and containerisation. These tools ensure the software remains stable and reproducible across environments. Key tools include:
- *Git/GitHub*: version control and code collaboration.
- *Docker*: containerizing workflows for reproducibility.
- *Workflow languages*: Nextflow for standardised benchmarking pipelines from the different scientific communities.

## FAIR & Open 
### OpenEBench is fully aligned with FAIR and open science principles

OpenEBench promotes openness and FAIR compliance across its code, workflows, and benchmarking results:
- The different git repositories holding both the code and the data model are publicly hosted both on GitHub
  and BSC's Gitlab under open-source licenses ([Apache-2.0](https://spdx.org/licenses/Apache-2.0.html),
  [CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html),
  [LGPLv2](https://spdx.org/licenses/LGPL-2.1-or-later.html), etc...).
- APIs and workflows use either standard or documented formats to support interoperability. Some examples:
  * Metrics workflows provided by the communities must be written in Nextflow. The steps must depend on 
    docker images, which should be public and distributable. Their docker recipes and build process should be public.
    When the docker images are not distributable, the docker recipes must be public.
    All the metrics workflows from the different communities have to support
    the very same minimal named parameters, and produce their main outputs listing the metrics
    assigned to the assessed participants, following a minimal dataset data model
    ([model](https://github.com/inab/OEB_level2_data_migration/blob/master/oeb_level2/schemas/minimal_bdm_oeb_level2.yaml)
    and [sample](https://github.com/inab/OEB_level2_data_migration/tree/master/minimal_dataset_examples)).
  * REST API both returns and accepts documents following the OEB benchmarking data model,
    described in JSON Schema with several relational extensions ([link to the 1.0 model](https://github.com/inab/benchmarking-data-model/tree/master/json-schemas/1.0.x), [examples of 1.0 model](https://github.com/inab/benchmarking-data-model/tree/master/prototype-data/1.0.x) and [graphical representation of the 1.0 model](https://github.com/inab/benchmarking-data-model/blob/master/json-schemas/openebench-bdm-1.0.x.dot.pdf)).
- Users can access software, documentation, and benchmark data freely, and contribute via GitHub or BSC's Gitlab.
- The development process is transparent, with scientific and technical benchmarking
  communities involvement in decisions and feature development.

## Documentation 
### Comprehensive documentation ensures the community can effectively use of OpenEBench

OpenEBench provides multiple documentation resources to help users navigate the platform and contribute to development:
- Main entry point: [OpenEBench ReadTheDocs](https://openebench.readthedocs.io/en/latest/)
- README files for each repository explaining setup and usage [https://github.com/inab/openebench-hub]
- Templates and examples for workflow examples and benchmarking pipelines [https://github.com/inab/TCGA_benchmarking_workflow]
- Step-by-step guides for developers and administrators [https://openebench.readthedocs.io/en/latest/how_to/3_participate.html]

## Sustainability 
### Add a short one-two liner subtitle about how is the research software being made sustainable

As mentioned above, OpenEBench is maintained by the TechBioLab at BSC and supported by the ELIXIR Tools Platform. Governance combines core team oversight with community input. Funding from ELIXIR and institutional support ensures ongoing development, maintenance, and future-proofing. The project emphasises modular design, open standards, and containerization to reduce risks and facilitate long-term sustainability.

## References 

- OpenEBench main entry point: https://openebench.bsc.es/
- OpenEBench technical monitoring: https://openebench.bsc.es/tool
- OpenEBench scientific benchmarking: https://openebench.bsc.es/benchmarking
- OpenEBench Software Observatory: https://openebench.bsc.es/observatory/Trends
- OpenEBench ReadTheDocs: https://openebench.readthedocs.io/en/latest/
- OpenEBEnch Scientific benchmarking data model: https://github.com/inab/benchmarking-data-model/
- OpenEBEnch Scientific benchmarking REST and graphQL code: https://gitlab.bsc.es/inb/elixir/openebench/openebench-backend-legacy
- Quest for Orthologs benchmarking metrics computation workflow: https://github.com/qfo/benchmark-webservice 
- OpenEBench Scientific benchmarking tools: https://gitlab.bsc.es/inb/elixir/openebench/oeb-sci-admin-tools
- OpenEBench Scientific level2 ingestion tools: https://github.com/inab/OEB_level2_data_migration
- OpenEBench Scientific frontend code: https://github.com/inab/openEBench-nuxt
- OpenEBench Technical monitoring repository metadata enricher: https://github.com/inab/opeb-repo-enricher
