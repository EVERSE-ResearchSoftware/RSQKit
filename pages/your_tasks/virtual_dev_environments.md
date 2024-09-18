---
title: Reproducible virtual software development environments
description: Virtual software development environments for reproducible research 
contributors: ["Aleksandra Nenadic"]
page_id: virtual_environments
related_pages: []
---

## What are virtual software development environments?

A virtual software development environment helps us create an **isolated working copy** of a software project that uses a specific 
version of a programming language interpreter/compiler (e.g. Python 3.11) together with specific versions of a number of external 
libraries (dependencies) required by our software installed into that virtual environment. 
Virtual environments are typically implemented as directories with a particular structure (usually contained within software projects 
but can be outside too), containing links to specified dependencies allowing isolation from other software projects on your machine 
that may require different versions of the same programming language or external libraries.

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

* As more external libraries are added to your software project over time, you can add them to its specific virtual environment
and avoid a great deal of confusion by having separate (smaller) virtual environments for each project
rather than one huge global environment with potential package version clashes.
* You have an older project that only works under Python 2. You do not have the time to migrate the project to Python 3
or it may not even be possible as some of the third party dependencies are not available under Python 3.
You have to start another project under Python 3. The best way to do this on a single machine is
to set up two separate Python virtual environments.
* One of your Python 3 projects is locked to use a particular older version of a third party dependency.
You cannot use the latest version of the dependency as it breaks things in your project.
In a separate branch of your project, you want to try and fix problems introduced by the new version of the dependency
without affecting the working version of your project. You need to set up a separate virtual environment for your branch to
'isolate' your code while testing the new feature.
* You do not have to worry too much about specific versions of external libraries that your project depends on most of the time.
Virtual environments also enable you to always use the latest available version without specifying it explicitly.
They also enable you to use a specific older version of a package for your project, should you need to. 

### Solutions

* Make your research software reusable and your research that relies on that software reproducible by setting up and sharing its virtual development environment.

## How do you create virtual software development environments? 

### Description



### Considerations

* Are you reusing code which is already under an open source license? What obligations do you have under those licenses?
* Do you want to ensure that anybody modifying and redistributing your code will release the source code of their changes?
* Do you want to ensure the least number of restrictions and that your code will be used as widely as possible? Even if that means it might end up in commercial products that do not release their source code and do not compensate you.
* Is there a preferred license used in your research community?
* Do not be tempted to write your own license (or modify an existing one) unless you are a copyright lawyer.
* Remember that the rights granted in a license cannot be revoked once it has been applied.


### Solutions

* [Choose an open license](https://choosealicense.com/) website is a great tool to help you choose a license that is appropriate for your needs.


## Tools and resources

| Tool or resource                                                                                            | Description                                                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [Choose an open license tool](https://choosealicense.com/)                                                  | A guided tool to help you choose a license for your resource  |
| [license selector for software](https://ufal.github.io/public-license-selector)                             | A question-guided tool to help you choose a software license  |
| [Spdx](https://spdx.org/licenses/) list of licenses                                                         | A list of commonly recognized licenses used in software       |
| [OpenSource guide](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project) | Guidelines on changing and editing licenses                   |


## How to cite this page

To be added.


## Credit

The contents of this page have been inspired by the ["Tools and Practices for FAIR Research Software" course](https://carpentries-incubator.github.io/fair-research-software/05-code-environment.html) 
and the ["Intermediate Research Software Development" course](https://carpentries-incubator.github.io/python-intermediate-development/) developed by the Software Sustainability Institute.

      
## References

[^1]: [Aleksandra Nenadic, Steve Crouch, et al. (2024). carpentries-incubator/python-intermediate-development: beta-May2024 (beta-May2024). Zenodo. https://doi.org/10.5281/zenodo.11368608]
[^2]: [Gibson, S., Jaffa, S., Kopec-Harding, K., Nenadic, A., & Sauze, C. (2024). Tools and Practices for FAIR Research Software Course (alpha-July-2024). Zenodo. https://doi.org/10.5281/zenodo.12666089]

 
