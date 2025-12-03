---
title: "DOME Registry"
description: "A repository supporting standardised machine learning method disclosures to supplement publication text in the life sciences."
contributors: ["Gavin Farrell","Omar Attafi"] 
page_id: dome_registry
type: research_software_story
---

## The Problem 
### Addressing the reproducibility crisis in life science machine learning caused by inconsistent and opaque reporting practices

In the life sciences, the reuse of supervised machine learning (ML) research outputs is hampered by inconsistent, opaque, and non-reproducible methods driven by poor reporting practices. Despite the wide availability of high-quality, FAIR data and advanced algorithms to build these ML methods, individual researchers document their ML outputs—covering areas such as data, optimisation, models, and evaluation—in ad hoc, free-text formats. These often omit critical biological context and technical details.

This fragmentation in reporting methods makes it nearly impossible to reliably validate, compare, or build upon published ML models, creating a fundamental reproducibility crisis. The lack of a standardised, domain-aware reporting framework meant that, even with the best intentions, life science ML studies remained isolated, difficult to trust, and slow to translate into cumulative scientific progress. The DOME Registry was established as a service to support the creation of standardised ML method disclosures to supplement publication text, providing an operational solution for researchers and journal publishers to produce high-quality, transparent ML methods.

## The Community 
### A collaborative ecosystem connecting biological researchers, ML practitioners, and infrastructure providers to foster transparency

The intended user community of the DOME Registry is multifaceted, primarily composed of three interconnected groups. **Biological Researchers & Data Producers** use the registry to discover validated ML approaches and report their work transparently to increase credibility. **ML Practitioners & Bioinformaticians** rely on the registry to structure their reporting, benchmark against community standards, and share pipelines in a findable way. Finally, **Consumers & Integrators** (including journal editors and funders) use the registry as a validation aid to assess reproducibility and integrate high-quality models into larger biological workflows.

The software is developed and maintained by a diverse, rotational team anchored at the University of Padua (UNIPD), consisting of academic staff, PhD researchers who provide multi-year stability, and IT/engineering-focused interns. While UNIPD serves as the primary development hub, the infrastructure is supported by a mirror deployment at CERTH (ELIXIR Greece), providing operational resilience. The community further expands through international collaborations via ELIXIR projects and EOSC frameworks, such as the [AI4EOSC](https://ai4eosc.eu/) project.

## Technical Aspects  

The DOME Registry is implemented as a full-stack web application, specifically designed as research software infrastructure. It is a production-grade, community-serving web platform—rather than a prototype or analysis tool—based on the EVERSE categorisation levels.

Technically, it is built with [TypeScript](https://www.typescriptlang.org/) across the stack, utilising the [Angular](https://angular.io/) framework for its dynamic single-page frontend and [NestJS](https://nestjs.com/) for its modular, service-based backend, with data served via a flexible [MongoDB](https://www.mongodb.com/) database. Deployment is designed for standard web hosting, requiring a [Node.js](https://nodejs.org/) environment and MongoDB instance without dependence on high-performance computing. Its primary infrastructural need is robust database storage for the growing corpus of curated ML metadata.

### Libraries and Systems 

The software operates as a FAIR-enabling metadata repository that relies on a specific ecosystem of standard web technologies and domain-specific integrations.

* **Core Libraries:** The stack relies heavily on the **Angular** framework for the frontend and **NestJS** for the backend, communicating via a REST API.
* **Data Management:** It utilises **MongoDB** for flexible document storage of metadata.
* **Integrations:** It integrates with the [Data Stewardship Wizard (DSW)](https://ds-wizard.org/) (specifically the implementation referred to as the ‘DOME Wizard’) to guide user submissions.
* **Standards:** The platform supports [BioSchemas](https://bioschemas.org/) for interoperable markup and interoperates with standard JSON data formats.

## Software Practices 
### Ensuring quality and maintainability through version control, open governance, and structured development workflows

The DOME Registry is developed using established software engineering practices to ensure quality, transparency, and long-term maintainability. The project utilises a Git-based version control system ([GitHub](https://github.com/)) with a clear contribution policy, adopts open-source licensing (CC BY 4.0), and follows a structured workflow with semantic versioning for releases.

* **Version Control:** All source code is managed in a Git repository. Feature development is isolated in branches, following a GitHub flow-like model where the main branch reflects stable, production-ready code.
* **Code Review:** Review is mandatory for all pull requests to ensure adherence to standards and to catch issues early. The lead developer oversees this process, using it as a mentorship opportunity for junior developers.
* **Decision Making:** Significant technical decisions are made within the ELIXIR AI Ecosystem Focus Group, informed by user needs and community feedback. A Scientific Advisory Board (SAB) meets annually to review the development plan.
* **Communication:** Day-to-day coordination happens via Slack and Zoom syncs. Major changes are discussed in open meetings and documented through GitHub issues, while a roadmap is published via [Zenodo](https://zenodo.org/).

## Community 
### Streamlining the path for new developers and contributors through mentorship, documentation, and guided submission tools

New users and developers engage with the DOME Registry through distinct, supported pathways designed to lower barriers to entry.

* **Developer Journey:** New developers (often interns or partners) start by cloning the GitHub repository. Due to the project's rotational nature, they typically pair with senior PhD researchers or lab technicians to learn the codebase. Work is organised via GitHub Issues, and changes are submitted via Pull Requests.
* **Content Contributors:** Researchers submitting data start at the [submission page](https://registry.dome-ml.org/review). They are guided to the "DOME Wizard" (based on DSW), which walks them through the reporting process step-by-step.
* **Onboarding Resources:** Users rely on the [DOME Training Course](https://biodataanalysisgroup.github.io/DOME-Training-Course/) and specific video tutorials (e.g., Submission Walkthroughs) to understand the workflow.
* **Obstacles:** The primary hurdle for new developers is local environment setup. Work is underway to improve Docker containerisation to reduce the configuration burden for Node.js and database connections.

## Tools 
### Utilising a modern web development toolchain to ensure code quality, consistency, and efficient collaboration

The project employs a well-integrated toolchain to ensure high software quality and streamlined development.

* **Linting & Formatting:** [ESLint](https://eslint.org/) is used for code quality and [Prettier](https://prettier.io/) for consistent code styling.
* **Version Control & Tracking:** [GitHub](https://github.com/) serves as the central hub for version control, issue tracking, and documentation.
* **Package Management:** Node Package Manager ([NPM](https://www.npmjs.com/)) handles dependencies.
* **Productivity:** GitHub Copilot is used to assist with developer productivity.
* **Planned Tools:** Work is in progress to implement [Docker](https://www.docker.com/) for full containerisation and to introduce GitHub Actions for CI/CD.

## FAIR & Open 
### Adhering to FAIR principles for research software to ensure findability, accessibility, interoperability, and reusability

The DOME Registry aspires to fully adhere to the FAIR principles for research software, ensuring it is a reliable component of the Open Science ecosystem.

* **Findable:** The software is indexed in [FAIRsharing](https://fairsharing.org/), uses [BioSchemas](https://bioschemas.org/) for harvestable metadata, and is published in high-profile journals with persistent DOIs.
* **Accessible:** The registry is free to use via a web interface, and all source code is available on [GitHub](https://github.com/BioComputingUP/dome-registry) under an open license (CC-BY 4.0). A public REST API allows programmatic access without barriers.
* **Interoperable:** The platform uses standard data formats (JSON), adheres to DOME recommendations, and integrates seamlessly with the Data Stewardship Wizard.
* **Reusable:** The software is "Mirror" deployable (proven by the deployment at CERTH) and features extensive documentation and permissive licensing to encourage modification and reuse.

## Documentation 
### Empowering users and developers with comprehensive guides, video tutorials, and API references

Documentation is distributed across GitHub and the web platform to support both technical contributors and end-users.

* **Main Entry Point:** The [GitHub Repository](https://github.com/BioComputingUP/dome-registry) contains the README with basic deployment and setup instructions.
* **User Guides:** The [DOME Training Course](https://biodataanalysisgroup.github.io/DOME-Training-Course/) provides educational materials, and the [Submission Page](https://registry.dome-ml.org/review) hosts specific video tutorials.
* **Technical Docs:** API documentation is available at [https://registry.dome-ml.org/api/](https://registry.dome-ml.org/api/) and integration standards are detailed online.
* **Status:** While documentation exists, work is in progress to formalise "tribal knowledge" currently held in internal files into structured documentation for better knowledge transfer.

## Sustainability 
### Securing long-term viability through multi-institutional mirror deployments and dedicated core funding

The DOME Registry operates as a resilient multi-node service delivered jointly by UNIPD (ELIXIR Italy) and CERTH (ELIXIR Greece), ensuring operational redundancy and a 10-year service guarantee.

* **Maintenance:** The core infrastructure is maintained by the Biocomputing Lab at UNIPD with a dedicated full-time technician. Services are partially mirrored at CERTH to ensure high availability and fault tolerance.
* **Funding:** The project is supported by a mix of permanent core funding and competitive grants, including the ELIXIR NextGenIT grant (Jan 2024 - Dec 2028) which underpins the service guarantee.
* **Risk Mitigation:** Technical failure is mitigated by the mirror setup and regular backups. Staffing gaps are addressed by permanent technician roles and overlapping PhD cycles.
* **Governance:** Significant decisions are co-informed by the ELIXIR AI Ecosystem Focus Group and the Scientific Advisory Board.

## References 

The project is shaped by community standards, key tools, and academic publications.

* **Code & Registry:** [GitHub Repository](https://github.com/BioComputingUP/dome-registry)
* **Primary Publication:** Attafi, O. A., et al. (2024). *DOME Registry: implementing community-wide recommendations for reporting machine learning in biology*. GigaScience. DOI: [10.1093/gigascience/giae094](https://doi.org/10.1093/gigascience/giae094)
* **Community Standards:** Walsh, I., et al. (2021). *DOME: recommendations for machine learning validation in biology*. Nature Methods. DOI: [10.1038/s41592-021-01205-4](https://doi.org/10.1038/s41592-021-01205-4)
* **Integrated Tool:** Pergl, R., et al. (2019). *"Data Stewardship Wizard": A Tool Bringing Together Researchers, Data Stewards, and Data Experts around Data Management Planning*. Data Science Journal. DOI: [10.5334/dsj-2019-059](https://doi.org/10.5334/dsj-2019-059)