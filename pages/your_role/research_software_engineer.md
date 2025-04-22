---
title: Research Software Engineer
page_id: research_software_engineer
---


## Introduction

A Research Software Engineer (RSE) plays a crucial role in bridging the gap between research and software development. 
Your tasks and responsibilities in this role can vary significantly depending on the research domain, but they generally focus on ensuring that software you develop 
to support research is robust, sustainable, reliable, reusable, and efficient.

You have an understanding of engineering practices, performance, software quality and tooling	and works alongside researchers to translate scientific problems 
into robust software solutions and are often required to work across multiple projects or domains.

## Responsibilities, tasks & challenges

Main responsibilities and common challenges of your role in relation to research software development and Research Software Quality include:

- Collaboration with researchers: translating research problems into technical requirements and help implement solutions
- Software development: writing and maintaining code for research projects (prototyping, optimization, refactoring)
- Code quality and best practices: applying best practices like version control, testing, documentation, and continuous integration
- Reproducibility & sustainability: ensuring research outputs are reproducible and software is maintainable
- Training: educating researchers and early career RSEs on coding practices and tools
- Data management: handling data wrangling, storage, format conversions, and pipeline automation
- Performance optimisation: improving performance of simulations, analyses, or computational workflows
- Tool integration: helping integrate existing tools and frameworks into research environments

### Domain-specific tasks

Soma example domain specific tasks of RSEs are listed below.

Life & health sciences:

- process and analyse genomic or proteomic data
- develop tools for sequence alignment, gene expression analysis, or CRISPR design
- optimise bioinformatics pipelines using tools like Snakemake or Nextflow
- build machine learning pipelines for medical imaging or patient data
- support integration with electronic health record systems

Physics & astronomy:

- implement or optimise simulations (e.g., quantum mechanics)
- parallelise code for HPC (using MPI/OpenMP)
- analyse big data (massive datasets) produced by modern telescopes
- visualise simulation results

Social sciences & digital humanities:

- build web applications for interactive data visualisations
- process and analyse textual or multimedia data using NLP techniques
- design databases for archival and metadata handling

Environmental sciences:

- develop and maintain climate models or Earth system models
- automate data assimilation pipelines
- visualise geospatial data using GIS tools


## Guidance

- Code quality best practices: version control, testing, documentation, and continuous integration



Organising Software Projects

A well-structured project directory facilitates collaboration, maintenance, and reproducibility. RSQKit recommends:

    Creating a top-level directory with a meaningful name.

    Including essential files such as:

        README: Describes the project and provides instructions for installation and usage.

        LICENSE: Specifies the terms under which the software can be used and redistributed.

        CITATION.cff: Provides citation information for the software.

    Organising subdirectories by content type, for example:

        data/: Raw and processed datasets.

        src/: Source code.

        tests/: Testing scripts.

        docs/: Documentation files.

This structure enhances clarity and facilitates easier navigation and collaboration.

Implementing Testing Practices

Incorporating testing into the development workflow ensures software reliability. RSQKit advocates for:

    Developing unit tests to verify individual components.

    Creating integration tests to assess combined parts of the application.

    Automating tests using continuous integration (CI) tools to detect issues early.​
    GitHub+1GitHub+1
    GitHub

These practices help maintain code quality and facilitate easier debugging and maintenance.

Adhering to FAIR Principles

Ensuring that software is Findable, Accessible, Interoperable, and Reusable (FAIR) enhances its utility and longevity. RSQKit suggests:

    Using persistent identifiers (e.g., DOIs) for software releases.

    Providing clear licensing information.

    Including comprehensive metadata and documentation.​

Adopting FAIR principles promotes transparency and facilitates wider adoption of research software.

Engaging in Code Reviews

Regular code reviews contribute to code quality by:

    Identifying bugs and potential issues.

    Ensuring adherence to coding standards.

    Facilitating knowledge sharing among team members.​

RSQKit encourages establishing a culture of constructive code reviews to enhance software robustness.
