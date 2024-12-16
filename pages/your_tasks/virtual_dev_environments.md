---
title: Reproducible virtual software development environments
description: What are virtual software development environments for reproducible research and how to use them?
contributors: ["Aleksandra Nenadic"]
page_id: virtual_environments
related_pages: []
---

## What are virtual software development environments?

A virtual software development environment helps us create an **isolated working copy** of a software project that uses a specific 
version of a programming language interpreter/compiler (e.g. Python 3.10 or Python 3.12) together with specific versions of a number of external 
libraries (dependencies) required by our software installed into that virtual environment. 

Virtual environments are typically implemented as sub-directories within your software project with a particular structure (but note 
that some tools can place virtual environments outside your software project). 
They contain links to specified dependencies and allow for isolation from other software projects on your machine that may require 
different versions of the same programming language or external libraries.

## Why should you use virtual software development environments? 

### Description 

Software applications often rely on external libraries that you need to install and manage on your system as you develop your software. 
Software will sometimes need a specific version of an external library (e.g. because they were written to work with feature, class, or 
function that may have been updated in more recent versions), or a specific version of the program language interpreter/compiler 
(e.g. consider legacy software requiring Python 2 vs. new applications written in Python 3). 

This means that each software application you develop on your machine may require a different setup and a set of dependencies so it is useful to be 
able to keep these configurations separate to avoid confusion between projects. 
The solution for this problem is to create a self-contained virtual environment per project, which contains a particular version of your 
programming language interpreter/compiler plus a number of additional external libraries.

Another big motivator for using virtual environments is that they make **sharing your code with others** (users or developers) much easier.
By sharing a description of your virtual development environment you enable others to quickly replicate the same environment 
on their machines and run or further develop your software - making your work **portable**, **reusable** and more **reproducible**.

### Considerations

- As more external libraries are added to your software project over time, you can add them to its specific virtual environment
and avoid a great deal of confusion by having separate (smaller) virtual environments for each project
rather than one huge global environment on your machine with potential package version clashes.
- You have an older project that only works under, e.g., Python 2. You do not have the time to migrate the project to Python 3
or it may not even be possible as some of the third party dependencies are not available under Python 3.
You have to start another project under Python 3. The best way to do this on a single machine is
to set up two separate Python virtual environments.
- One of your Python 3 projects is locked to use a particular older version of a third party dependency.
You cannot use the latest version of the dependency as it breaks things in your project.
In a separate branch of your project, you want to try and fix problems introduced by the new version of the dependency
without affecting the working version of your project. You need to set up a separate virtual environment for your branch to
'isolate' your code while testing the new feature.
- You do not have to worry too much about specific versions of external libraries that your project depends on most of the time.
Virtual environments enable you to always use the latest available version without specifying it explicitly.
They also enable you to use a specific older version of a package for your project, should you need to. 

### Solutions

- Make your research software reusable and your research that relies on that software reproducible by setting up and sharing its virtual development environment.

## How do you create virtual software development environments? 

### Description

Most modern programming languages use some kind of virtual environments or a similar mechanism to isolate libraries or dependencies for a specific project, 
making it easier to develop, run, test and share code with others. 
Some examples include Bundler for Ruby, Conan for C++, or Maven with classpath for Java. 
This can also be achieved with more generic package (dependency) managers like Spack, which is used extensively in HPC settings to resolve complex dependencies. 

Part of managing a virtual software development environment involves installing, updating and removing external packages on your system. 
You would need a package manager tool for your programming language to be able to do that - this is typically a command line tool that you invoke from 
a command line terminal. 
In addition to a package manager, you will need another command line tool to create and manage virtual environments on your machine. 
Sometimes, a package manager combines both of these functionalities and you only need to install one extra tool on your system.

### Considerations

- There are often multiple package and environment management tools for a single programming language.
  - For example, commonly used tools for managing Python packages and virtual environments are `pip` (Python package manager tool which interacts and obtains the packages
  from the central repository called Python Package Index (PyPI)) and `venv` (Python virtual environment manager tool available by default from the standard Python distribution from Python 3.3).
  One alternative is to use `poetry` - a modern Python packaging tool which also installs Python packages from PyPI and handles virtual environments automatically.
  - If your Python code relies on non-Python packages, for instance when some C++ libraries must also be installed and you want to support multiple platforms, a better choice may be `conda` -
  a Python package and environment management system part of the Anaconda Python distribution (often used by the scientific community). `conda` has its own repository system separate from
  (but compatible with) PyPI that distributes non-Python packages packages as well and has its own non-`venv`-based virtual environment system.
- You need to decide what tools are best for you - based on your personal preferences, or what the software project and your team or community is
already using (so you can get help when you need it). Not using virtual environments at all and mixing different tools to manage them could lead to
a [bad example of a spaghetti setup][python-env-hell], not knowing which dependencies are being used and causing issues when running and debugging code.

### Solutions

* Decide on and start using a package manager tool and a virtual environment management tool for your programming language.


## Tools and resources

| Tool or resource                                                                 | Description                                                                        |
| ---------------------------------------------------------------------------------| ---------------------------------------------------------------------------------- |
| [Install Python packages in a virtual environment using pip and venv][pip-venv]  | A guide on creating and activating virtual environments using venv and pip         |
| [Reproducible environments for your R projects][renv]                            | A guide on using renv to make R projects more isolated, portable and reproducible. |


## How to cite this page

To be added.


## Credit

The contents of this page have been inspired by the ["Tools and Practices for FAIR Research Software" course][fair-rs][^1] 
and the ["Intermediate Research Software Development" course][intermediate-rs-dev][^2] developed by the [Software Sustainability Institute][ssi].

      
## References
[^1]: [Aleksandra Nenadic, Steve Crouch, et al. (2024). carpentries-incubator/python-intermediate-development: beta-May2024 (beta-May2024). Zenodo. https://doi.org/10.5281/zenodo.11368608]
[^2]: [Gibson, S., Jaffa, S., Kopec-Harding, K., Nenadic, A., & Sauze, C. (2024). Tools and Practices for FAIR Research Software Course (alpha-July-2024). Zenodo. https://doi.org/10.5281/zenodo.12666089]

[pip-venv]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
[fair-rs]: https://carpentries-incubator.github.io/fair-research-software
[intermediate-rs-dev]: https://carpentries-incubator.github.io/python-intermediate-development/
[renv]: https://rstudio.github.io/renv/index.html
[ssi]: https://www.software.ac.uk/
[python-env-hell]: https://xkcd.com/1987/
