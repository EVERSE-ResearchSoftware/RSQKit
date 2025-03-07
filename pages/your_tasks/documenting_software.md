---
title: Documenting software
description: How to document your software project?
contributors: ["Azza Gamgami", "Aleksandra Nenadic"]
page_id: documenting_software
related_pages:
  your_tasks: [writing_readable_code, creating_readthedocs, creating_good_readme]
---

## How to document your software project?

### Description

Software documentation is an essential part of the software development process, designed to provide clear
communication between various stakeholders including developers, administrators, testers, users and project managers - 
ensuring the software is easy to understand and use.

### Considerations

* Software documentation should be accessible, clear, consistent, regularly updated, cover all key software aspects (source code, software structure, APIs, usage, etc.), 
encourage feedback, and ideally be auto-generated to a large extent.
* Software documentation should use standard formats – (R)Markdown, HTML, PDF, or wikis.
* Each piece of documentation has a distinct purpose, different audience 
(e.g. developers, administrators, testers, users and project managers), tone and level of detail (developer-facing documentation provides 
in-depth and complex technical details; an end-user guide focuses on usability and clarity, offering step-by-step instructions for usage).

### Solutions

* Create and maintain different types of software documentation - based on its purpose and intended audiences. 
* Include usage examples to help users understand and experiment with the software and showcase different aspects of your software.
* Automate generating of documentation from your code where possible and publishing it online by using specialised tools 
(e.g. using {% tool "readthedocs" %}).
* Store your documentation with your software project and track it using version control. 
  * {% tool "readthedocs" %} integrates with the version control workflow you likely already use for your code (such as Git and GitHub). 
  By treating documentation like code, your team can leverage familiar tools, making it easier to keep your documentation up-to-date. Read more on [how to create a *Read the Docs* page](https://everse.software/RSQKit/creating_readthedocs).
  * Publishing service {% tool "zenodo" %} integrates with GitHub and can archive your software's documentation automatically with 
  each new release of your software.

An example of a software project that has good documentation practices is bioinformatics library [khmer](https://github.com/dib-lab/khmer/). 
It is using version control for its documentation which features a comprehensive changelog that details new features, 
bug fixes (categorised based on relevance to users or developers), known issues, and a list of contributors for each release.

[Keras](https://github.com/keras-team/keras) is another software project documentation example that includes examples of code usages 
to demonstrate its functionalities.

## Types of software documentation

Documenting source code and software (as a product as well as a project) is essential for user experience, collaboration, and maintainability.

### Documenting source code

Source code documentation helps developers (and to some extent system administrators) understand the logic, structure, and functionality of the code. 
It ensures that the codebase remains readable, maintainable, and scalable. This may include the following documentation types.

#### Code comments

Code comments are about improving readability and understandability of your code and may include:

- inline comments – short explanations within the code for specific lines or blocks,
- block comments – detailed explanations for complex logic or algorithms,
- documentation strings – structured documentation (e.g., Python docstrings, Javadoc in Java) that describe functions, classes, and modules.

Some good practices when writing comments:

- write comments as you code,
- ensure you strike a balance in the amount of commenting - you do not have to explain each line of your code,
- focus on the *why* and the *how* of your code - avoid using comments to explain what your code does. If your code is too
  complex for other programmers to understand, consider rewriting it for clarity rather than adding comments to explain it,
- write meaningful explanations for error messages - to help troubleshoot issues when using your software.

Also see the [related page on writing readable code](./writing_readable_code).

#### Interface documentation

Software interface documentation describes how different software components or systems interact with each other, 
outlining various interfaces (including Application Programming Interface (API)) and communication protocols:

- describes how to use functions, classes, and modules,
- includes parameters, return values, exceptions, and usage examples for functions and classes.

**Automated documentation tools** can help automate generation of this type of documentation from [documentation strings](#code-comments) - 
while no software can completely write source code documentation for you, several tools can significantly ease the process.

* {% tool "sphinx" %} (for Python and other languages), {% tool "doxygen" %} (for C++ and other languages), {% tool "roxygen" %} (for R), 
{% tool "javadoc" %} (for Java) and {% tool "jsdoc" %} (for JavaScript) can generate documentation in multiple formats (HTML, PDF) and automatically extract comments from annotated code in your codebase.
* {% tool "mkdocs" %} enables the creation of professional-looking documentation websites using Markdown.
* {% tool "swagger" %} automatically generates API documentation, providing user-friendly interfaces for developers.
* {% tool "documenter-jl" %} is a Julia package for building documentation from docstrings in code and Markdown files.
* [Continuous Integration (CI) and Continuous Deployment (CD)](https://github.com/resources/articles/devops/ci-cd) tools offered by platforms such as {% tool "github" %} and {% tool "gitlab" %} 
can automate documentation generation and release. 

### Documenting software product

Software product documentation comprehensive information about the software, including its features, usage, installation, and troubleshooting.
It may include some of the following documentation types.

#### Technical documentation

- Software requirement specifications – functional and non-functional requirements of the software
- System architecture – high-level system design, how different modules and components interact and key technologies used
- API (Application Programming Interface) documentation – if the software provides an API, detailed API specs
- Deployment guide – instructions on installing, configuring, and deploying the software for administrators.

#### User documentation

- Installation guides – instructions for setting up the software.
- Quickstart guides - concise documents that helps users quickly set up and start using software with minimal effort. 
For example, [a quickstart guide for TPOT (Tree-Based Pipeline Optimization) tool](http://epistasislab.github.io/tpot/) includes an animated GIFs with examples and minimal code snippets.
- User manuals – detailed step-by-step instructions on how to use the software.
- CLI (Command Line Interface) documentation - if the software provides a CLI, usage instructions including relevant commands, 
parameters and arguments to run the software. Tools like [Click](https://click.palletsprojects.com/) for Python can assist you in creating your software's CLI. 
A great example of a CLI is the one included with the [Magic-BLAST](https://ncbi.github.io/magicblast/) bioinformatics tool.
- Tutorials & How-To Guides – walk-throughs for common tasks.
- Troubleshooting & FAQs – solutions to common issues.

### Documenting software project

Documenting a research software project is much like documenting any open project.
Project documentation details key external-facing elements of a software project, focusing on managing and tracking its 
development, usage, contributions and community.

An excellent overview of what documentation each software project should provide can be found in the [Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).

Project documentation should include the following:

- README - a text or Markdown file that introduces and explains a project and explains the basic functionality, dependencies and usage of your software. README 
also acts as a homepage for your project on code sharing platforms such as {% tool "github" %} and {% tool "gitlab" %}.
See more on [how to create a good README document for your software project][creating_good_readme].
- Contributing guidelines - describes how people can contribute to the development of software and get involved in the project
- Roadmap - an overview of the current and future development plans and milestones
- Changelog and release notes - a text file that contains a record of what notable changes are made between versions of software
- Licensing - lets users know under what legal conditions they are allowed to use the software.
- Code of Conduct - to create and maintain a collaboration environment that promotes participation, collaboration and exchange of ideas, 
while fostering respect among developers
- Software citation - let people know how to cite your software, see more on [how to cite your software project](./citing_software)
- List of all authors and contributors to the software 
- Pointers to various other documentation about your software.

## References
1. [Lee B. D., Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561)
2. [Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P.Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)
3. [Perez-Riverol Y, Gatto L, Wang R, Sachsenberg T, Uszkoreit J, Leprevost FdV, et al. Ten Simple Rules for Taking Advantage of Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004947)
4. [How to Write Software Documentation in 7 Simple Steps](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/)
5. [The Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).

[creating_good_readme]: /creating_good_readme
[licensing_software]: /licensing_software
[releasing_code]: /releasing_software
[software_documentation]: /documenting_software
