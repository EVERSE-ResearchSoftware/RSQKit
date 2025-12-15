---
title: "DOME Registry"
description: "A repository supporting standardised machine learning method disclosures in the life sciences."
contributors: ["Gavin Farrell", "Omar Attafi"]
page_id: dome_registry
type: research_software_story
---

## The Problem 
### Addressing the reproducibility crisis in life science machine learning caused by inconsistent and opaque reporting practices

In the life sciences, the reuse of supervised machine learning (ML) research outputs is hampered by inconsistent, opaque, and non-reproducible methods driven by poor reporting practices. Despite the wide availability of high quality, FAIR data and advanced algorithms to build these ML methods, individual researchers document their ML outputs—covering areas such as data, optimisation, models, and evaluation—in ad hoc, free-text formats, often omitting critical biological context and technical details. 

This fragmentation in reporting methods makes it nearly impossible to reliably validate, compare, or build upon published ML models, creating a fundamental reproducibility crisis. The lack of a standardised, domain-aware reporting framework meant that even with the best intentions, life science ML studies remained isolated, difficult to trust, and slow to translate into cumulative scientific progress. In response to the challenges, the DOME Registry was set up as a service to support the creation of standardised ML method disclosures to supplement publication text. The [DOME Registry](https://registry.dome-ml.org/intro) is now an operational solution to support both researchers and journal publishers in the production of high quality and transparent ML methods.

## The Community 
### A collaborative ecosystem connecting biological researchers, ML practitioners, and infrastructure providers

The intended user community of the DOME Registry is multifaceted. It is primarily composed of three interconnected groups with different DOME Registry usage needs:

* **Biological Researchers & Data Producers:** These are experimentalists and bench scientists who generate or work with complex biological datasets (e.g., genomic, imaging, clinical) and wish to apply ML. They use the registry to discover validated ML approaches relevant to their domain, report their own work transparently, and ensure their models are reusable, thereby increasing the impact and credibility of their computational findings.
* **ML Practitioners & Bioinformaticians:** This core user group includes data scientists, computational biologists, and ML engineers who develop and implement algorithms. They rely on the registry to structure and standardise their model reporting, benchmark their methods against community standards (DOME), and share their pipelines in a findable, citable way. For them, it is a tool for professional rigour and recognition.
* **Consumers & Integrators:** This group includes journal editors, reviewers, funders, and infrastructure providers (like public databases). They use the registry as a curated validation aid to assess the reusability and reproducibility of submitted ML studies, to encourage or mandate standards compliance, and to integrate high-quality ML models into larger biological data resources and workflows.

Ultimately, the DOME Registry serves the broader [ELIXIR](https://elixir-europe.org/) and global life science community by fostering a culture of transparency. Its success depends on engaging all user groups—from the biologist seeking a trustworthy model to the developer sharing one—in a collaborative ecosystem dedicated to improving the reliability of ML-driven discovery.

## Technical Aspects  

The DOME Registry is implemented as a full-stack web application, specifically designed as research software infrastructure. It is a production-grade, community-serving web platform, not a prototype or analysis tool based on the [EVERSE categorisation levels](https://everse.software/RSQKit/three_tier_view). 

Technically, it is built with {% tool "typescript" %} across the stack, utilising the [Angular](https://angular.io/) framework for its dynamic single-page frontend and [NestJS](https://nestjs.com/) for its modular, service-based backend, with data served via a flexible [MongoDB](https://www.mongodb.com/) database. The codebase is actively maintained by the ELIXIR community, specifically the core maintainers at the [University of Padua](https://biocomputingup.it/). Deployment is designed for standard web hosting, requiring a [Node.js](https://nodejs.org/) environment and MongoDB instance without dependence on high-performance computing; its primary infrastructural need is robust database storage for the growing corpus of curated ML metadata. In essence, the software is a FAIR-enabling metadata repository: a database-backed API service with a rich client interface that systematically ingests, validates, and disseminates structured descriptions of biological machine learning workflows.

### Libraries and Systems 

The software relies on a specific stack of modern web technologies and domain integrations.

* **Core Stack:** {% tool "typescript" %}, [Angular](https://angular.io/), [NestJS](https://nestjs.com/), [Node.js](https://nodejs.org/).
* **Data Storage:** [MongoDB](https://www.mongodb.com/).
* **Integrations:** It integrates key external tools like the [Data Stewardship Wizard (DSW)](https://ds-wizard.org/) (specifically the implementation referred to as the ‘DOME Wizard’) for guided user submissions.
* **Standards:** [BioSchemas](https://bioschemas.org/) for interoperable markup, [FAIRsharing](https://fairsharing.org/), and [Identifiers.org](https://identifiers.org/).

## Software Practices 
### Balancing established engineering standards with the challenges of rotational academic development

The DOME Registry is developed using established software engineering practices to ensure quality, transparency, and long-term maintainability. It uses a {% tool "git" %}-based version control system ({% tool "github" %}) with a clear contribution policy, adopts open-source licensing (CC-BY 4.0), and follows a structured workflow and semantic versioning for releases. 

* **Version Control:** All source code is managed in a {% tool "git" %} repository ({% tool "github" %}) ([BioComputingUP/dome-registry](https://github.com/BioComputingUP/dome-registry)), with feature development isolated in branches. The workflow is [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)-like, though deletion and deprecation of branches could use improvements. The main branch reflects stable, production-ready code, and changes are integrated via pull requests by team members, with integrations and deployment managed by the lead developer.
* **Code Review & Testing:** Code review is mandatory for all pull requests, ensuring adherence to standards and catching issues early. The lead developer ensures this step is completed and advises more junior developers on future contributions to build technical competencies across the team. There are currently no formalised testing practices, but this will be considered in the future as team bandwidth allows.
* **Decision Making:** Significant technical or directional decisions are made through discussion within the [ELIXIR AI Ecosystem Focus Group](https://elixir-europe.org/focus-groups/ai-ecosystem), often informed by user needs and community feedback. One major focus is breaking silos to interface the DOME Registry with new standards and other ELIXIR Europe services (e.g. [Europe PMC](https://europepmc.org/)). A Scientific Advisory Board (SAB) meets annually to review and inform the development plan, with an annual roadmap logged and output via {% tool "zenodo" %} (first release planned for December 2025).
* **Communication:** Formal changes could be better tracked through [GitHub Issues](https://github.com/features/issues) and pull requests; work is in progress to professionalise this aspect. Real-time coordination occurs via team chat tools ([Slack](https://slack.com/)) and regular development meetings ([Zoom](https://zoom.us/)).
* **Informal Practices:** Informal yet crucial practices include ad-hoc troubleshooting chats, shared documentation of “tribal knowledge” in [Google Drive](https://www.google.com/drive/) workflow files, and a culture of mentorship and cross-training to sustain the project through contributor turnover. Trust and open communication are key to maintaining momentum.

## Community 
### Streamlining the path for new developers and contributors through mentorship and guided tools

The DOME Registry is developed and maintained by a diverse, rotational team anchored at the [University of Padua (UNIPD)](https://www.unipd.it/en/). The core development team consists of academic staff at various career stages, including two PhD researchers who provide multi-year stability and IT/engineering focused interns who contribute targeted technical work. Because of this rotational nature, the project relies on a strong "handover" culture where knowledge is actively transferred to new contributors to maintain continuity. While UNIPD serves as the primary development hub, the infrastructure is supported by a mirror deployment at [CERTH (ELIXIR Greece)](https://www.certh.gr/), which provides operational resilience without requiring a separate development team. Beyond the core staff, the community expands through international collaborations via ELIXIR projects or collaborations in the EOSC frameworks such as with the [AI4EOSC project](https://ai4eosc.eu/).

**How DOME Registry onboards new developers:**
* **Workflow:** New developers, often interns or project partners, start by cloning the {% tool "github" %} repository. Work is commonly organised via GitHub Issues, and [GitHub Projects](https://github.com/features/issues) is being considered to bring code, strategy and management into one location.
* **Mentorship:** Due to the "handover" nature of the project, new staff typically pair with senior PhD researchers or the lab technician to learn the codebase and deployment nuances.
* **Obstacles:** The primary hurdle is the local environment setup. While documentation exists, the lack of full {% tool "docker" %} containerisation means initial configuration of Node.js and database connections can be time-consuming. Work is underway to ensure {% tool "docker" %} for both local use and full deployment to reduce this burden.

**How DOME Registry handles new content contributions:**
* **Submission Page:** New contributors start at the [Submission Page](https://registry.dome-ml.org/review), which guides them to the DOME Wizard content generation platform.
* **The DOME Wizard:** Users start with the integrated [DOME Data Stewardship Wizard (DSW)](https://dome.dsw.elixir-europe.org/wizard/dashboard) instance, which guides them through reporting ML methods in a step-by-step process.
* **Training:** Users rely on the [DOME Training Course](https://biodataanalysisgroup.github.io/DOME-Training-Course/) and specific video tutorials to understand the content generation and submission workflow.

## Tools 
### Utilising a modern web development toolchain while working to bridge gaps in automation

The project employs a well-integrated toolchain to ensure high software quality and streamlined development.

* **Linting & Formatting:** [ESLint](https://eslint.org/) is used for code quality and {% tool "prettier-code-formatter" %} for consistent code styling.
* **Version Control & Tracking:** {% tool "github" %} serves as the central hub for version control, issue tracking, and documentation.
* **Package Management:** Node Package Manager ([NPM](https://www.npmjs.com/)) handles dependencies.
* **Productivity:** {% tool "github-copilot" %} is used to assist with developer productivity and accelerate progress.
* **Containerisation:** Full containerisation with {% tool "docker" %} is planned but not yet implemented. Currently, the environment is managed via detailed setup instructions and version-locked dependencies (`package.json`) to ensure consistency across local setups.
* **Future Plans:** {% tool "github-actions" %}, automated dependency updates ({% tool "dependabot" %} to maintain security with minimal effort), and AI code generation are being considered to accelerate development progress, though risks regarding codebase stability and knowledge retention are acknowledged.

## FAIR & Open 
### Adhering to FAIR principles for research software to ensure findability, accessibility, interoperability, and reusability

The DOME Registry aspires to fully adhere to the FAIR principles for research software, ensuring it is a reliable component of the Open Science ecosystem.

* **Findable:** The software is indexed in major research meta-discovery platforms (e.g., [FAIRsharing](https://fairsharing.org/)) and utilises [BioSchemas](https://bioschemas.org/) markup to make entry metadata harvestable. The project is published in high-profile journals ([Nature Methods](https://doi.org/10.1038/s41592-021-01205-4), [GigaScience](https://doi.org/10.1093/gigascience/giae094)) with persistent DOIs. Cross-linking to {% tool "zenodo" %} is planned for archiving specific versions, and [Europe PMC](https://europepmc.org/) indexing is currently being worked on.
* **Accessible:** The registry is free to use via a web interface. All source code is available on {% tool "github" %} ([BioComputingUP/dome-registry]) under an open license (CC-BY 4.0), allowing inspection of the underlying logic. A public REST API allows programmatic access to all public registry data without authentication barriers. [Identifiers.org](https://identifiers.org/) is used to ensure accessible entry resolution.
* **Interoperable:** The platform uses standard data formats (JSON) and adheres to the DOME recommendations for ML reporting. It integrates seamlessly with the [Data Stewardship Wizard (DSW)](https://ds-wizard.org/). The separation of frontend (Angular) and backend (NestJS) allows for independent integration with other tools.
* **Reusable:** The "Mirror" deployment at CERTH proves the software is not tied to a single institution's infrastructure and can be redeployed. Documentation and permissive licensing ensure that the code and content can be reused, modified, and built upon by the wider scientific community.

## Documentation 
### Empowering users and developers with comprehensive guides, video tutorials, and API references

Documentation is distributed across GitHub and the web platform to support both technical contributors and end-users.

* **GitHub:** The README file covers basic deployment and setup (see {% tool "github" %}/BioComputingUP/dome-registry), though improvements are planned.
* **Training & Tutorials:** The [DOME Training Course](https://biodataanalysisgroup.github.io/DOME-Training-Course/) provides educational materials.
* **Submission Guides:** The [Submission Page](https://registry.dome-ml.org/review) and [Video Tutorials](https://youtu.be/fmVppa9ESw0) guide users through the process.
* **Integrations & API:** [Integration standards](https://registry.dome-ml.org/integrations) and [API documentation](https://registry.dome-ml.org/api/) are available online.

## Sustainability 
### Securing long-term viability through multi-institutional mirror deployments and dedicated core funding

The DOME Registry operates as a resilient multi-node service delivered jointly by UNIPD (ELIXIR Italy) and CERTH (ELIXIR Greece). This dual-institutional approach ensures operational redundancy, while a 10-year service guarantee provides long-term stability beyond typical grant cycles.

* **Financial Sustainability:** The project is supported by a mix of permanent core funding and competitive grants. A key pillar is the **[ELIXIR NextGenIT grant](https://elixir-italy.org/project/elixirxnextgenit/)** (Jan 2024 - Dec 2028), which includes a signed guarantee from the University of Padua to provision the DOME Registry for the next 10 years. Other funding sources include **[ELIXIR ML SIS](https://elixir-europe.org/focus-groups/machine-learning)** (Machine Learning Structural Implementation Study), **[EVERSE EC](https://everse.software/)**, and **[STEERS EC](https://elixir-europe.org/about-us/how-funded/eu-projects/steers)**.
* **Operational Maintenance:** The core infrastructure is maintained by the Biocomputing Lab at UNIPD with a dedicated full-time technician. Services are partially mirrored (front end) at CERTH to ensure high availability and fault tolerance.
* **Content Strategy:** Current curation is manual, but scaling plans involve implementing LLM-based triage models. Active integration with publishers (e.g., [GigaScience](https://academic.oup.com/gigascience), [Gigabyte](https://gigabytejournal.com/)) ensures a continuous stream of new content.
* **Risk Mitigation:** Technical failure is mitigated by the mirror setup and regular backups. Staffing gaps are addressed by permanent technician roles and overlapping PhD cycles. In the unlikely event both labs cease operations, the open {% tool "github" %} repository allows the community to fork and redeploy.

## References 

The project is shaped by community standards, key tools, and academic publications.

* **Code & Registry:** {% tool "github" %} Repository ([BioComputingUP/dome-registry])
* **Primary Publication:** Attafi, O. A., et al. (2024). *DOME Registry: implementing community-wide recommendations for reporting machine learning in biology*. GigaScience. DOI: [10.1093/gigascience/giae094](https://doi.org/10.1093/gigascience/giae094)
* **Community Standards:** Walsh, I., et al. (2021). *DOME: recommendations for machine learning validation in biology*. Nature Methods. DOI: [10.1038/s41592-021-01205-4](https://doi.org/10.1038/s41592-021-01205-4)
* **Integrated Tool:** Pergl, R., et al. (2019). *"Data Stewardship Wizard": A Tool Bringing Together Researchers, Data Stewards, and Data Experts around Data Management Planning*. Data Science Journal. DOI: [10.5334/dsj-2019-059](https://doi.org/10.5334/dsj-2019-059)