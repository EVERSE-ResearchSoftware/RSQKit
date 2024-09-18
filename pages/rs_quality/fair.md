---
title: FAIR Research Software
---


## FAIR Research Software

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to
increase the visibility and usefulness of your research to others.
The FAIR data principles, first published [in 2016][fair-data-principles], are widely known and applied today.
Similar [FAIR principles for software][fair-principles-research-software] have now been defined too. In general, they mean:

* **Findable** - software and its associated metadata must be easy to discover by humans and machines.
* **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols, free and legally usable.
* **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through
  standardised protocols and application programming interfaces (APIs).
* **Reusable** - software should be usable (can be executed) and reusable
  (can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below.
This is not an exact science, and by all means the list below is not exhaustive,
but any of the practices that you employ in your research software workflow will bring you
closer to the gold standard of a fully reproducible research.

* Findable
  * Create a description of your software
  * Place your software in a public software repository (and ideally register it in a [software registry](https://github.com/NLeSC/awesome-research-software-registries))
  * Use a unique and persistent identifier (DOI) for your software (e.g. by depositing your code on Zenodo), 
  which is also useful for citations - note that depositing your data/code on GitHub and similar software repositories 
  may not be enough as they may change their open access model or disappear completely in the future
* Accessible
  * Make sure people can freely, legally and easily get a copy your software
  * Structure your code using common patterns and use coding conventions to make your code readable and understandable by people (once they obtain a copy of it)
* Interoperable
  * Explain the functionality of your software
  * Use standard formats for inputs and outputs
  * Communicate with other software via standard protocols and APIs
* Reusable
  * Document your software (including its functionality, and how to install and run it)
  * Follow best practices for software development (including coding conventions, code readability and verifying its correctness)
  * Test your software and make sure it works on different platforms/operating systems
  * Give a licence to your software clearly stating how it can be reused
  * State how to cite your software
 
  
## Tools 

There are various tools and practices that support the development of FAIR research software, contributing to each of the four FAIR principles. 
These tools and practices work together, as no single tool or practice addresses only one principle. 
In fact, a single tool or practice can often contribute to multiple principles simultaneously. 
The table below provides a summary of how different tools and practices align with the FAIR software principles.

| Tools and practices                                                                               | Findable | Accessible | Interoperable | Reusable |
|---------------------------------------------------------------------------------------------------|----------|------------|---------------|----------|
| Virtual development environments, programming language and dependencies - run, test, debug, share |          | x          |               | x        |
| Integrated development environments/IDEs (e.g. VS Code, PyCharm) - run, test, debug               |          |            |               | x        |
| Command line terminal (e.g. Bash, GitBash) - reproducible workflows/pipelines                     |          |            | x             | x        |
| Version control tools                                                                             | x        |            |               |          |
| Testing - code correctness and reproducibility                                                    |          | x          |               | x        |
| Coding conventions and documentation                                                              |          | x          | x             | x        |
| Explaining functionality/installation/running - README, inline comments and documentation         |          | x          | x             | x        |
| Standard formats - e.g. for data exchange (CSV, YAML)                                             |          | x          | x             | x        |
| Communication protocols - Command Line Interface (CLI) or Application Programming Interface (API) |          | x          | x             | x        |
| License                                                                                           |          | x          |               | x        |
| Citation                                                                                          | x        |            |               | x        |
| Software repositories (e.g. GitHub, PyPi) or registries (e.g. BioTools)                           | x        | x          |               |          |
| Unique persistent identifier (e.g. DOIs, commits/tags/releases) - Zenodo, FigShare GitHub         | x        | x          |               |          |





[fair-principles-research-software]: https://www.nature.com/articles/s41597-022-01710-x
[fair-data-principles]: https://www.nature.com/articles/sdata201618
