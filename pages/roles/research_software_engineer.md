---
title: Research Software Engineer (RSE)
page_id: research_software_engineer
description: Software development and quality guidance for Research Software Engineers (RSEs)
contributors: ["Aleksandra Nenadic"]
---


## Introduction

A Research Software Engineer (RSE) plays a crucial role in bridging the gap between research and software development.
The tasks and responsibilities in this role can vary significantly depending on the research domain, but they generally focus on ensuring that software they develop to support research is robust, sustainable, reliable, reusable, and efficient.

RSEs have a deeper understanding of engineering practices, performance, software quality and tooling and work alongside researchers to translate scientific problems into robust software solutions and are often required to work across multiple projects or domains.

What sets RSEs apart from software engineers is not just that they work within research, but that they are part of the research process. Some RSEs are, in fact, active researchers themselves, e.g. as expert innovators in their own digital domains. Many RSEs have a research background, e.g. as PhDs or postdocs. Their knowledge and experience from both the research and software worlds is what makes them especially well suited as bridge builders between the two fields.

RSEs may work day-to-day in a number of different ways, which will often depend on how they are employed within the institution they work for. RSEs may be embedded within a particular research group in an academic field they are interested in, or they may work in a centralised team associated with their institution's Professional Services, or even a mixture of the two. A centralised team offers the benefit of drawing on the expertise of other RSEs working in the same institution, allowing for a organisational structure that means those with more experience of research and software engineering can manage projects, individuals working on those projects, and services which cut across multiple projects the centralised team as a whole is working on.

## Software development & quality responsibilities, challenges & tasks

Main responsibilities and common challenges of this role in relation to research software development and Research Software Quality include:

- Collaboration with researchers: translating research problems into technical requirements and help implement solutions
- Software architecting: designing software systems that satisfy functional and non-functional requirements
- Software development: writing and maintaining code for research projects (prototyping, optimisation, refactoring)
- Code quality and best practices: applying best practices like version control, testing, documentation, and continuous integration
- Reproducibility & sustainability: ensuring research outputs are reproducible and software is maintainable
- Data management: handling data wrangling, storage, format conversions, and pipeline automation
- Performance optimisation: improving performance of simulations, analyses, or computational workflows
- Tool integration: helping integrate existing tools and frameworks into research environments
- Training: educating researchers and early career RSEs on coding practices and tools

Some example domain-specific tasks of RSEs are listed below.

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


## Software development & quality guidance

- [Software project structure](./software_project_structure) - a well-structured project directory facilitates collaboration, maintenance and reproducibility
- [Adopting FAIR principles](./fair_rs) promotes transparency and facilitates wider adoption of research software
- Code quality best practices - [version control](./using_version_control), [testing](./testing_software), [documentation](./documenting_software) and [licensing](./licensing_software)
- [Software testing practices](./testing_software) and automating tests using [Continuous Integration](./ci_cd) (CI)
- Engaging in [code reviews](./code_review) - regular code reviews contribute to code quality and facilitate knowledge sharing among team members
