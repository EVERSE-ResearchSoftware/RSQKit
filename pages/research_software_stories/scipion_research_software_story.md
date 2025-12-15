---
title: "Research Software Story - SCIPION"
description: "Scipion is an integrated platform that unifies cryo-EM image processing tools to manage, execute, and reproduce complete structural reconstruction workflows."
contributors: ["Carlos Oscar Sorzano", "Lola Sanchez", "Irene Sanchez"]
page_id: scipion_research_software_story
type: research_software_story
---
<!-- This heading is automatically inserted -- # Research Software Story – Scipion -->

## The Problem

Unifying complex cryo-EM workflows for reproducibility and efficiency

Cryo-electron microscopy (cryo-EM) and electron tomography generate large volumes of raw movies, micrographs, particles, and reconstructions that require multi-step processing with specialized tools.
Traditionally, researchers combined these tools manually, which often led to duplicated effort, fragmented workflows, and challenges with reproducibility.
Existing software solutions were not fully interoperable, required extensive manual configuration, and demanded significant expertise to produce consistent results.

Scipion addresses these challenges by providing a unified, modular framework that integrates multiple cryo-EM and tomography software packages into a single workflow.
It automates data format conversion, manages project metadata, and enables reproducible, end-to-end pipelines, reducing manual effort and increasing reliability and interoperability across tools.
More interestingly, it allows comparison of results from multiple algorithms using consensus methods, which help detect parameter misestimation and highlight the parameters whose estimated values are more reliable.

## User Community

Cryo-EM researchers and structural biology facilities

The primary users of Scipion include cryo-EM and tomography researchers, structural biologists, and staff at cryo-electron microscopy platforms.
Users range from early-career scientists to experienced facility operators, typically with strong domain expertise but varying levels of software engineering experience.

Development is coordinated by the core team at the **Spanish National Center for Biotechnology (CNB-CSIC)**, with contributions from the broader community through plugins and workflow extensions.
Users often become contributors as they adapt or extend workflows for their projects.

* Developers: Core CNB-CSIC team and external contributors creating plugins or protocol integrations.

* Users: Structural biology labs, national and international cryo-EM facilities, and researchers in academia.

* Interaction: Communication occurs through GitHub, mailing lists, workshops, and facility training sessions.

## Technical Aspects

Modular workflow engine for cryo-EM pipelines

Scipion is a **research software infrastructure** designed to unify cryo-EM workflows and, in general, algorithms for the analysis of biological structures.
It provides a framework for defining reproducible workflows that wrap multiple external tools and manage metadata consistently.

* Languages: Python (core, GUI, workflows), C/C++ (computation-intensive modules).

* Codebase: Actively maintained, modular, supports hundreds of plugins.

* Deployment: Runs locally, on HPC clusters, or in containerized environments (Apptainer).

* Constraints: Handles large datasets, GPU acceleration, and integrates multiple heterogeneous cryo-EM tools.

## Libraries and Systems

Integration with cryo-EM software ecosystem

Scipion depends on multiple domain-specific libraries and external systems:

* RELION, CryoSPARC, XMIPP, EMAN2, SPHIRE, CTFFIND, MotionCor2, Topaz, among others.

* MPI and CUDA for distributed computing.

* SQLite for project metadata.

* Standard cryo-EM file formats (STAR, MRC).

## Software Quality Practices

Open-source development with continuous validation

Scipion follows open-source best practices.
The code is hosted on **GitHub**, and contributions are managed through pull requests with peer review.
Continuous Integration (CI) ensures builds, automated tests, and plugin validation.

* Version control: Git/GitHub.

* Code review: Mandatory for all pull requests; SonarCloud performs a check.

* Testing: Automated CI tests plus validation through real-world cryo-EM workflows; checked by BuildBot.

* Decision making: Core team reviews significant changes; community feedback is incorporated via GitHub issues.

## Developer Community

Building a collaborative ecosystem for cryo-EM workflows

New developers typically begin as users who identify workflow gaps or plugin needs.
They then contribute plugins or workflow improvements via GitHub.
Scipion provides extensive training and documentation to facilitate onboarding.

* Onboarding: Workshops, tutorials, and facility-led training.

* User stories: Researchers run complete cryo-EM pipelines efficiently and reproducibly.

* Learning resources: example workflows, extensive documentation, GitHub documentation.

## Tools

Supporting development and quality with modern software tools

Scipion employs a range of tools to maintain quality and stability:

* **Git/GitHub**: Version control and collaboration.

* **CI/CD systems**: Automated testing of workflows and plugins.

* **Visualization and workflow GUI**: Monitoring and debugging complex pipelines.

These tools streamline development, ensure reproducible results, and lower barriers for new contributors.

## FAIR & Open

FAIR principles and open development practices

Scipion aligns with FAIR and open-source principles:

* **Findable**: Publicly hosted on GitHub; plugins cataloged; versioned releases.

* **Accessible**: Open-source license; installation via source or Apptainer.

* **Interoperable**: Standardized metadata and integrated format conversion for multiple tools.

* **Reusable**: Workflows are reproducible and portable; the plugin system enables extension.

## Documentation

Comprehensive guides for users and developers

Scipion documentation is maintained on ReadTheDocs, GitHub, and the project website:

* Installation guides for local, HPC, and containerized environments.

* Tutorials and examples for cryo-EM workflows.

* Developer guides for plugin creation and API reference.

* Training materials from workshops and EM facilities.

Documentation is continuously updated, and community contributions expand tutorials and practical examples.

## Sustainability

Maintaining Scipion for long-term cryo-EM research

Scipion is maintained by the core CNB-CSIC team, with contributions from external developers and research infrastructures.
Sustainability relies on:

* Active user base in cryo-EM facilities worldwide.

* Modular plugin system and open-source ecosystem.

* Funding from grants and European research infrastructures (Instruct-ERIC, ELIXIR-ES).

## References

Scipion builds upon and integrates with the following resources:

* Scipion GitHub Repository: <https://github.com/I2PC>

* Scipion webpage: <https://scipion.i2pc.es>

* Scipion documentation and tutorials: <https://scipion-em.github.io/docs/release-3.0.0/index.html>

<!-- External References embedded as links -->

[SCIPION_GITHUB]: https://github.com/I2PC
[SCIPION_WEBPAGE]: https://scipion.i2pc.es/
[SCIPION_DOCS]: https://scipion-em.github.io/docs/release-3.0.0/index.html

