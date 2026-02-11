---
title: "Packaging software" 
search_exclude: false 
description: "How to package and release your software for distribution and reuse?" 
contributors: ["Eva Martín del Pico", "Aleksandra Nenadic"] 
page_id: packaging_software
related_pages:
  tasks: [releasing_software, publishing_software] 
quality_indicators: [has_published_package, has_releases]
keywords: ["package software", "packaging software", "releasing software", "release software", "pypi"]

---

## How to package and release your software?

### Description

Making your code publicly available is a key step toward open, reusable, and citable research software.

[Publishing][publishing_software] means sharing your software in a way that others can find, use, and cite it - it is often achieved by putting your code in a shared code repository such as GitHub or in a dedicated package repository.

Packaging is the process of preparing your software in a neat "package" so that others can install and use it easily (e.g. using a simple command or download).

[Releasing][releasing_software] refers to packaging a particular stable version of your code for others to download and run.

### Considerations

Packaging is the process of preparing your software so that others can install and use it easily.
It may involve: 
* organising your code and files in a standard structure and providing package configuration files (e.g., `package.json`, `pyproject.toml`)
* including metadata such as version number, authors, dependencies, and license,
* adding configuration or build files,
* ensuring users can install the software using a simple command or download.

### Solutions

Here are some common ways to package and release your software:

* **Code hosting platforms** – like {% tool "github" %}, {% tool "gitlab" %}, and {% tool "bitbucket" %} - provide a place to share and publish your project’s source code. 
They are often the first step toward an open release and packaging too - they allow storing and distributing packages across multiple programming languages and formats.
* **Software registries and package repositories** – once your code is ready to be installed or reused, you can package and publish it to discipline- or language-specific registries (for example, PyPI for Python, CRAN for R, npm for JavaScript, Maven Central for Java). 
These make it easy for users to install your software directly from their environment.
* **Container registries and workflow hubs** – for more complex or reproducible environments, you can publish your software as a {% tool "docker" %}/{% tool "singularity" %} container or share it on workflow repositories (e.g. {% tool "workflowhub" %}, {% tool "dockstore" %}) to support reproducible execution.

#### Code Hosting Platforms

Code hosting platforms are the most common way to share and collaborate on software projects. 
They provide online repositories that store your code and its history using version control (usually Git).

These platforms support:
* publishing and visibility – your repository can be public and easily shared through a web link.
* releases – you can tag a version (e.g. v1.0.0) and publish it as a release with release notes and downloadable archives.
* automation – continuous integration and testing pipelines can automatically check that your code works as intended before each release.

Code hosting platforms form the hub of most modern software projects.
Even if your users ultimately install your software from a package registry, the source code and development history usually live here.
However, it is possible to create and host packages directly code hosting platforms - e.g. check this guide on [how to create a Python package and publish it on GitHub][python-package-github].

#### Software Package Registries

Once software is stable and ready for others to install, you can distribute it through a package registry. 
These systems make software easy to install directly from the command line or within programming environments.
Examples include PyPI (Python), CRAN (R), npm (JavaScript), conda-forge (multi-language), CPAN (Perl).

Registries provide:
* simple installation – users can install your package with a single command (e.g. `pip install`, `conda install`, `install.packages`, etc.).
* versioned distribution – each release is recorded with its version number, so users can reproduce work with specific versions.
* metadata and discoverability – registries include information such as author, license, dependencies, and description, making your software findable by others.

Even though package registries are language-specific, the general principle is the same - they make your code accessible and reusable by a wide audience of users and developers.

#### Container and Workflow Registries

For complex research software that depends on multiple tools or specific environments, distributing containers or workflows ensures reproducibility.
Containers package your software together with its runtime environment (libraries, operating system dependencies, etc.) so others can run it reliably anywhere.
Workflows describe how multiple tools or scripts connect to form a complete computational process.
Examples include Docker Hub, GitHub Container Registry, Singularity Library, WorkflowHub, Dockstore.

Container and workflow registries allow you to:
* package and share ready-to-run code and environments – users can pull and run a container with no manual setup.
* versioned distribution – each container or workflow can have tagged versions, just like source code releases.

[publishing_software]: ./publishing_software
[releasing_software]: ./releasing_software
[python-package-github]: https://medium.com/@thomas.vidori/how-to-create-a-python-package-and-publish-it-on-github-eebc78b2a12d