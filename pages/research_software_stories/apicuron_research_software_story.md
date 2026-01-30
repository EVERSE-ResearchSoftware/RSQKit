---
title: "APICURON - The platform to credit and acknowledge scientific contributions beyond traditional publications" 
search_exclude: false
description: "APICURON aims to provide a recognition model for contributions beyond traditional publications, including research software, data sources, and training material" 
contributors: ["Mehdi Zoubiri", "Federica Quaglia", "Kamel Eddine Adel Bouhraoua"]
page_id: apicuron
type: research_software_story # leave this as is
---


## The Problem 
APICURON fundamentally addresses a critical flaw in scientific credit: the profound lack of formal, granular recognition for essential scientific labor, particularly biocuration. This work is vital for data integrity and utility but remains undervalued by traditional, publication-centric credit systems.

Before APICURON, assigning credit to data curators was fragmented, slow, and difficult due to the absence of a reliable, automated method for tracking ongoing, non-publication- based contributions. Credit defaulted to initial database publications, which quickly become outdated.

This reliance on peer-reviewed papers as the sole metric fails to capture scholarly impact in the modern data-driven landscape, specifically neglecting dynamic, continually evolving data resources. The traditional system overlooks the scholarly value in curated data and fails to integrate the sustained effort of curatorial work into academic profiles with the precision required for fair career evaluation. APICURON is designed to bridge this gap, ensuring biocuration is recognized as a vital, continuous, and measurable scholarly contribution.
## User Community 
The platform serves projects that require structured and transparent recognition of contributions to research software, data resources, and other non-traditional research outputs. Originally adopted by biocuration databases, it now supports broader communities seeking credit mechanisms that extend beyond publication-centric metrics. Development is handled by maintainers who are familiar with both the resource codebase and the domain models. Users, primarily including curators and contributors, rely on the service to track coding, maintenance, curation, and workflow activities, an arrangement that simplifies governance but concentrates responsibility on a limited set of core developers.

**Who uses the platform?**

* Resource managers integrating contribution tracking into community databases and services  
* Research software engineers seeking formal recognition for development, maintenance, and infrastructure work  
* Software maintainers and tool developers aiming for transparent contributor histories  
* Projects in the STEERS and EVERSE ecosystems requiring attribution for software and other non-traditional research outputs

## Technical Aspects  

The platform serves as a Tier 3 research software infrastructure service, designed for real-time, event-driven contribution tracking. It uses a modern TypeScript-based stack, containerised for consistent deployment, and optimised for stable, low-latency processing of granular lifecycle events.

**Core technologies**

* {% tool "typescript" %} across client and server, {% tool "nestjs" %} (backend application layer), {% tool "angular" %} (frontend interface), {% tool "mongodb" %} \+ {% tool "mongoose" %} (document-oriented datastore)

The codebase has been under continuous development since 2019 and has gradually expanded in modularity and functionality as new contribution types and community requirements were incorporated. The service has been shaped to respond to various operational requirements, including:

* Real-time ingestion of well-defined events  
* Low-latency processing under sustained load  
* Stable server environment (no HPC needed since changes are propagated on a more granular level)  
* Scalable database backend to support growing data sources  
* Robust handling of concurrent event submissions

### Libraries and Systems 
* {% tool "nodejs" %}/{% tool "nestjs" %}: Used to implement the web server and processing of the data, leveraging the event-loop to propagate and aggregate the processed data  
* {% tool "mongoose" %}:  
* {% tool "orcid" %}: used for authentication, linking user contributions back to their ORCIDs, and displaying those contributions on a CV-style page.  
* {% tool "bip-scholar" %} used to enrich users' profiles with additional metadata and relevant scientific indicators from the OpenAIRE Graph

## Software Practices 

Development follows a disciplined {% tool "github" %} {% tool "git" %}-centric workflow: feature branches, mandatory pull requests, and peer review for every change. Core functionality is validated through unit tests, while broader behavioural checks occur on a dedicated staging deployment at [dev.apicuron][dev-apicuron] before release. Decisions are informed by community feedback, and automated Slack notifications provide continuous awareness of ongoing changes.

These practices deliver tangible benefits: improved reliability, smoother coordination, predictable releases, and a codebase that remains maintainable as the platform evolves.

## Developer Community 
The platform is steadily gaining adoption as more research resources integrate contribution tracking, and the community is expanding through active engagement with both developers and data providers. The project focuses on lowering barriers to entry, allowing new contributors, whether technical or otherwise, to join and be productive quickly.

New developers are granted access to the repository, where documentation outlines the architecture and workflows. They typically begin with small, well-scoped tasks under the guidance of an experienced developer, gradually progressing to more complex work and eventually using the database and testing instance to validate their changes. New users, primarily resource managers, begin by visiting the documentation site and may request onboarding sessions to design recognition models tailored to their platforms. They rely on technical guidance, examples, and communication channels such as email and Slack to integrate the service effectively and resolve operational questions.

## Tools 
A set of development, quality-assurance, and deployment tools support the stability and maintainability of the platform. These tools streamline daily development, enforce coding standards, and ensure consistent deployments across environments.

**Development quality and automation**

* {% tool "eslint" %} – enforces coding standards and catches common errors.  
* {% tool "prettier-code-formatter" %} – provides consistent code formatting across the project.  
* {% tool "jest" %} – runs unit tests to validate core functionality.  
* {% tool "swagger" %} – supports accurate and maintainable API documentation.

**Deployment and packaging**

* {% tool "docker" %} – containers for both client and server components, enabling predictable and reproducible deployments.  
* {% tool "nginx" %} \+ {% tool "apache-http-server" %} – act as reverse proxies to route and manage production traffic.

These tools have improved code consistency, reduced integration friction, and made the build-and-release process more reliable, ultimately supporting a stable and maintainable service.
## FAIR & Open 
APICURON adheres to the FAIR principles for research software and non-traditional research artefacts as follows:

**• Findable:**  APICURON is openly accessible at [*https://apicuron.org*][apicuron], with publicly documented API endpoints and activity schemas that make contribution records discoverable. Integration with ORCID ensures that contributor identities remain globally findable across systems, and within the ELIXIR-STEERS and EOSC EVERSE ecosystems, APICURON acts as a contribution-tracking service for research asset recognition.

**• Accessible:**  Contribution data is available through open APIs and human-readable contributor profiles. The platform is free to use, and resource partners can submit contribution events programmatically. It stores only minimal metadata (Agent–Activity–Time), ensuring accessibility while limiting exposure of personal information. GDPR-compliant consent workflows are used for partners submitting user-level contributions. Contributors can request the modification or removal of their records through the submitting resource, which remains the responsible data controller.

**• Interoperable:** The platform is designed to interoperate with the broader research-assessment ecosystem. It uses standard identifiers (e.g., ORCID) and aligns with contribution-role standards proposed in policy initiatives such as CoARA and CodeMeta. GitHub integration and adapters for diverse contribution types enhance interoperability across research software environments. All interoperability points are exposed through public interfaces rather than proprietary mechanisms.

**• Reusable:** A simple contribution model and flexible activity definitions enable reuse across various domains, from software development to workflow engineering and data curation. Communities can define their own activity types and reward schemes, allowing disciplinary adaptation without changing the core service. The open documentation, public APIs, and generality of the model support long-term reuse in assessment, reporting, and research software credit workflows.

## Documentation 
Clear documentation supports both users and resource developers in understanding the platform, integrating their resources, and effectively utilising contribution-tracking features. All core materials are maintained alongside the service and updated as the platform evolves.

The primary entry point is the **Docs** page on the platform ([*https://apicuron.org/docs*][apicuron-docs]), which provides a unified overview of the system. Documentation includes a user guide for navigating the website, an integration guide for resource developers, and an OpenAPI specification presented through Swagger. Users can also request assistance or onboarding calls when beginning an integration.

**Documentation available:**

* [Website user guide][apicuron-user-guide]  
* [Integration guide for resource partners][apicuron-integration]  
* [OpenAPI / Swagger documentation][apicuron-api]  
* [Support via email or onboarding sessions][apicuron-email]

## Sustainability 
APICURON is maintained by the [BioComputingUP][biocomp] Lab at the University of Padova, with development, infrastructure, QA, and user support handled by the core team, and scientific oversight provided through the Italian ELIXIR node’s SAB and associated biocuration networks. This structure ensures continuity, ethical compliance (GDPR, ELSI), and alignment with community standards even without a standalone internal advisory board.

The platform is demonstrably active and growing, supported through ongoing institutional funding and integrated into broader ELIXIR activities. Its sustainability is reinforced by active maintenance practices—regular QA cycles, SOP-driven audits, community communication channels, and an expanding user base of 17 partner resources, 207 contributors, and over 143k tracked events—ensuring the service remains stable, supported, and viable over time.

## References 

APICURON Platform. Available at: [https://apicuron.org/][apicuron]

Hatos, A., Quaglia, F., Piovesan, D., & Tosatto, S. C. E. (2021). *APICURON: a database to credit and acknowledge the work of biocurators*. **Database**, 2021, baab019. [https://doi.org/10.1093/database/baab019][hatos-2021]

Vergoulis, T., Makaronidou, M., Amodeo, S., Stavropoulos, T., Quaglia, F., Bouhraoua, K. E. A., Roiser, S., Garijo, D., Piovesan, D., Psomopoulos, F., Pechlivanis, N., Orfanou, A., & Bakoglidou, E. (2025). *D5.1 Landscape analysis of existing rewards and mechanisms for research software and training activities*. Zenodo. [https://doi.org/10.5281/zenodo.14978474][vergoulis-2025]

Bouhraoua, A., Vergoulis, T., Makaronidou, M., Quaglia, F., & Tosatto, S. (2024). *ELIXIR-STEERS Report M3.1 Strategy for inclusion of credit for research assets decided*. Zenodo. [https://doi.org/10.5281/zenodo.14017751][bouhraoua-2024]

<!-- Reference-style link definitions -->
[apicuron]: https://apicuron.org/
[apicuron-docs]: https://apicuron.org/docs
[apicuron-user-guide]: https://apicuron.org/docs/user-guide
[apicuron-integration]: https://apicuron.org/docs/developer-guide/integration
[apicuron-api]: https://apicuron.org/api/
[apicuron-email]: mailto:info@apicuron.org
[dev-apicuron]: https://dev.apicuron.org/
[orcid]: https://orcid.org/
[mongodb]: https://www.mongodb.com/
[mongoose]: https://mongoosejs.com/
[bip-scholar]: https://bip.imsi.athenarc.gr/scholar
[nginx]: https://nginx.org/
[apache-http-server]: https://httpd.apache.org/
[git]: https://git-scm.com/
[hatos-2021]: https://doi.org/10.1093/database/baab019
[vergoulis-2025]: https://doi.org/10.5281/zenodo.14978474
[bouhraoua-2024]: https://doi.org/10.5281/zenodo.14017751
[biocomp]: https://biocomputingup.it/

