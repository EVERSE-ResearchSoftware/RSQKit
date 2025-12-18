---
title: "Research Software Story - OpenEBench"
description: "OpenEBench is an open, community-driven platform for benchmarking and monitoring bioinformatics software, enabling transparent performance evaluation and improved research software quality."
contributors: [Laura Portell-Silva]
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
- Define reference datasets and evaluation metrics
- Run standardised, reproducible benchmarking events
- Compare tools fairly and transparently
- Track software performance and quality over time

Beyond performance benchmarking, OpenEBench also contributes to improving research software quality through its [Software Observatory](https://openebench.bsc.es/observatory/Trends). The observatory aggregates metadata from multiple sources and evaluates software against FAIR principles (Findable, Accessible, Interoperable, Reusable), providing:
- FAIRness indicators and scores
- Visibility into software maturity and maintenance practices
- Actionable insights for developers to improve their software

This dual focus on performance and quality distinguishes OpenEBench from traditional benchmarking efforts.

## User Community 
### Developers and researchers collaborate to improve bioinfromatics tools

OpenEBench serves a diverse and interconnected user base:
- *Bioinformatic tools developers*, who want objective feedback on performance and visibility for their tools
- *Scientific communities*, who define domain-specific benchmarking events aligned with real research needs
- *Researchers and end-users*, who need trustworthy information to select appropriate tools
- *Infrastructure providers and funders*, who seek insight into software quality, sustainability and impact

The platform is designed to be community-led: benchmarking events are defined and governed by the communities that use them.

## Technical Aspects  
OpenEBench is built as a modular, service-oriented platform designed to support reproducible benchmarking and software observaotry.

### Languages and Codebase

The OpenEBench codebase is primarily developed using:
- Python for backend services, data processing, benchmarking workflows and APIs
- Bash and Nextflow for orchestrating benchmarking pipelines

The platform is organised into independent but interoperable components, enabling reuse across different benchmarking communities and facilitating long-term maintenance and extension. All core components are open source and developed following collaborative good practices.

### Architecture and Deplopyment
OpenEBench follows a cloud-ready, container-based architecture:
- Services and tools are packaged using Docker containers to ensure reproducibility and portability
- Benchmarking workflows are executed within a Virtual Research Environment (VRE)
- MongoDB is deployed as a core backend service supporting scalable data storage and querying
- OpenEBench provides RESTful APIs for data access and integration

### Interoperabiltiy and Integration
The platform integrates with external registries, repositories and monitoring services to harvest software metadata and usage signals. 

## Software Practices 
### OpenEBench follows open-source and FAIR-aligned practices

OpenEBench is developed as an open‑source platform with code repositories hosted on GitHub. Contributors follow community standards for version control, code review, and integration.
- *Version control*: Git/GitHub‑based repositories with clear topic tagging for discoverability.
- *Code review*: Pull requests are used to ensure changes align with project objectives and maintain quality standards.
- *Testing and validation*: Benchmarking workflows include validation and verification of results.
- *Community feedback*: Issues and discussions capture user feedback, drive prioritisation, and support continuous improvement across releases.

## Developer Community 
### Add a short one-two liner subtitle about how the software is being adopted for usage and how a community is being built around it

OpenEBench is developed and maintained at the TechBioLab at the [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/es) as part of the [ELIXIR Tools Platform](https://elixir-europe.org/platforms/tools). New contributors can get started by exploring the GitHub repositories, following tutorials, and participating in community discussions. The platform encourages collaborative development and feedback to continuously improve benchmarking events.

## Tools 
### OpenEBench uses tools to be FAIR-compliant

OpenEBench relies on a combination of development and deployment tools that streamline workflow creation, testing, and containerisation. These tools ensure the software remains stable and reproducible across environments. Key tools include:
- *Git/GitHub*: version control and code collaboration
- *Docker*: containerizing workflows for reproducibility
- *Workflow languages*: Nextflow for standardised benchmarking pipelines

## FAIR & Open 
### OpenEBench is fully aligned with FAIR and open science principles

OpenEBench promotes openness and FAIR compliance across its code, workflows, and benchmarking results:
- The code is publicly hosted on GitHub under an open-source license.
- APIs and workflows use standard formats to support interoperability.
- Users can access software, documentation, and benchmark data freely, and contribute via GitHub.
- The development process is transparent, with community involvement in decisions and feature development.

## Documentation 
### Comprehensive documentation ensures the community can effectively use of OpenEBench

OpenEBench provides multiple documentation resources to help users navigate the platform and contribute to development:
- Main entry point: [OpenEBench ReadTheDocs](https://openebench.readthedocs.io/en/latest/)
- README files for each repository explaining setup and usage
- Templates and examples for workflow examples and benchmarking pipelines
- Step-by-step guides for developers and administrators

## Sustainability 
### Add a short one-two liner subtitle about how is the research software being made sustainable

As mentioned above, OpenEBench is maintained by the TechBioLab at BSC and supported by the ELIXIR Tools Platform. Governance combines core team oversight with community input. Funding from ELIXIR and institutional support ensures ongoing development, maintenance, and future-proofing. The project emphasises modular design, open standards, and containerization to reduce risks and facilitate long-term sustainability.

## References 

- OpenEBench main entry point: https://openebench.bsc.es/
- OpenEBench technical monitoring: https://openebench.bsc.es/tool
- OpenEBench scientific benchmarking: https://openebench.bsc.es/benchmarking
- OpenEBench Software Observatory: https://openebench.bsc.es/observatory/Trends
- OpenEBench ReadTheDocs: https://openebench.readthedocs.io/en/latest/
  
