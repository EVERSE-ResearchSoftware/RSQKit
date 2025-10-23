---
title: Documenting software
description: How to document your software project?
contributors: ["Azza Gamgami", "Aleksandra Nenadic", "Laura Portell Silva"]
page_id: documenting_software
related_pages:
  tasks: [writing_readable_code, documenting_software_readthedocs, creating_good_readme]
quality_indicators: [software_has_documentation]
keywords: ["documentation", "software documentation", "readme", "sphynx", "readthedocs"]

---

## How to create good software documentation?

### Description

Software documentation is an essential part of the software development process, designed to provide clear communication between various stakeholders including developers, administrators, testers, users and project managers. It ensures that the software is easy to understand, maintain and use, and that its functionality can be effectively extended or reused by others.

Documentation provides the foundation for software sustainability and reusability. It facilitates collaboration, reduces dependency on individual contributors, and improves transparency, reproducibility, and quality assurance. Proper documentation also enhances user experience and supports onboarding for new contributors.

### Considerations

* Software documentation should be accessible, clear, consistent, regularly updated, cover all key software aspects (e.g., source code, software structure, APIs, usage), encourage feedback, and be automatically generated where possible. It should use standard formats such as (R)Markdown, reStructuredText, HTML, PDF, or wikis.
* Each piece of documentation serves a distinct purpose, with a specific audience, tone, and level of detail. Different users of software can be broadly categorised as:
  * *End users* – individuals who use the software for personal or work-related tasks.
  * *Administrators* – responsible for installing, configuring, managing, and maintaining software systems.
  * *Developers* – who create, modify, debug, and maintain software applications.
  * *Testers* and *project managers* – who engage with documentation based on their roles and needs.
* Documentation can vary depending on the aspect of the software it addresses:
  * *Product documentation* provides comprehensive information about the software’s features, functionality, usage, and maintenance. Examples include requirements documents, high-level descriptions (e.g., README files), source code documentation, user guides, and API references. It targets multiple audiences, ensuring they can understand, operate, and troubleshoot the software.
  * *Process documentation* is primarily intended for the development team and may include plans, progress reports, working papers, and notes that capture development ideas and decisions.

### Solutions

#### Understand purpose and audience

* Create and maintain different types of software documentation based on its **purpose** and **intended audience**.
* Think about who will be using the documentation and tailor content accordingly:
  * *User documentation* – explains clearly what the software does and how to use it; focuses on usability, clarity, and step-by-step instructions (e.g., end user guides).
  * *Developer documentation* – covers in-depth technical details such as specifications, docstrings, inline comments, error messages, contribution guidance, testing, and software governance.
  * *Deployment documentation* – provides installation, configuration, dependency, platform, and testing instructions.
* Creating personas can help target content effectively for different audiences.

#### Document as you code

A documentation string is a string literal specified in source code that is used, like a comment, to document a specific segment of code. The difference is that the documentation string is visible to the outside world, while comments are not. Documentations strings are for helping people use the code, while comments are meant for people modifying the code - yourself and other developers.

* Write comments and documentation strings while coding to keep information up to date.
* Balance the amount of commenting; focus on *why* and *how* instead of restating *what* the code does.
* Rewrite overly complex code rather than explaining it with excessive comments.
* Use integrated development environments (IDEs), such as {% tool "vscode" %}, {% tool "pycharm" %}, {% tool "eclipse" %} and extensions (e.g., {% tool "jsdoc" %}, {% tool "python-docstring-generator" %}) to assist in generating docstrings.

#### Write meaningful error messages

To help your users troubleshoot issues when using your software, error messages returned by your code should clearly state:

* When and where the error happened.
* What went wrong.
* The state of the software at that time.
* How to fix it or where to find help in your documentation.

#### Include usage examples

* Provide usage examples to help users understand, experiment with, and explore features.
* If documentation becomes cluttered, move examples to a dedicated section.
* {% tool "keras" %} is a good example of including code usage examples.

#### Include a quickstart guide

* Offers a fast path from setup to experimentation (e.g., tutorials, animated GIFs, minimal examples).
* The [TPOT tool](http://epistasislab.github.io/tpot/) includes an effective quickstart with code snippets and visuals.

#### Provide a README file

* The README should explain basic functionality, installation steps, and usage (e.g., a quick start).
* It acts as a project homepage on platforms like {% tool "github" %} and {% tool "gitlab" %}.
* Include a link to full project documentation.
* See more details on [how to create a good README file](./creating_good_readme).

#### Version control your documentation

* Store documentation in the project repository and track it using version control.
* Treat documentation like code to keep it updated through familiar workflows. Read more on [how to use *Read the Docs* for your software project](documenting_software_readthedocs.md).
* {% tool "readthedocs" %} integrates with Git workflows and can automatically publish documentation. See more in the [Documenting Software Readthedocs page](./documenting_software_readthedocs).
* {% tool "zenodo" %} can archive documentation automatically with each software release.

Examples:
* The bioinformatics library [khmer](https://github.com/dib-lab/khmer/) uses version control for its documentation, includes a comprehensive changelog, lists contributors, and tracks user- vs developer-facing issues.
* *RSQKit* uses GitHub Actions to automate documentation tasks.

#### Document Command Line Interface (CLI) or the Application Programming Interface (API)

If your software provides a CLI or API:
* Describe usage, subcommands, options, arguments, and environment variables.ç
* Provide examples where possible.
* Implement a `help` command to assist users without external documentation.

The `help` command should cover:
* Usage instructions (how to execute the command).
* Relevant subcommands
* Options and/or arguments
* Applicable environment variables
* And ideally, some examples.

Tools and examples:
* [Click](https://click.palletsprojects.com/en/stable/) helps build and document Python CLI tools.
* The [OpenAPI Specification](https://swagger.io/specification/), previously known as the Swagger Specification, is a specification for a machine-readable API definition language for describing, producing, consuming and visualising web services.
* {% tool "swagger" %} (built around the OpenAPI Specification) helps design, build, document, and consume REST APIs.
* A great example of a CLI is the one included with the [Magic-BLAST](https://ncbi.github.io/magicblast/) bioinformatics tool.

#### Use automated documentation tools

While no software can completely write software documentation for you, several tools can significantly ease the process.

* {% tool "sphinx" %} (for Python and other languages), {% tool "doxygen" %} (for C++ and other languages), {% tool "roxygen" %} (for R) and {% tool "jsdoc" %} (for JavaScript) can generate documentation in multiple formats (HTML, PDF) and automatically extract comments from annotated code in your codebase.
* {% tool "mkdocs" %} enables the creation of professional-looking documentation websites using Markdown.
* {% tool "swagger" %} can automate the generation of client libraries, server stubs, and API documentation efficiently based on API definitions. 
* {% tool "documenter-jl" %} is a Julia package for building documentation from docstrings in code and Markdown files.
* Leverage CI/DC tools, offered by platforms such as {% tool "github" %} and {% tool "gitlab" %} to automate quality assurance and release of your updated documentation to the public. For example, take a look at the [GitHub actions in the RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit/actions) 
for some automated tasks.

#### State how to cite your software

* Ensure that your documentation includes clear instructions on how to cite your work.
* See more on [how to cite your code repository using Citation File Format (CFF)].

### Types of software documentation

Documenting source code and software—both as a *product* and as a *project*—is essential for user experience, collaboration, and long-term maintainability.

#### Documenting source code

Improves readability, maintainability, and scalability. Includes:

**Code comments**
* Inline comments – short explanations for specific lines/blocks
* Block comments – detailed explanations for complex logic
* Documentation strings – structured descriptions of functions/classes/modules

**Interface documentation**
* Describes how components interact (e.g., APIs), including parameters, return values, exceptions, and usage examples.

#### Documenting the software product

Provides comprehensive information on functionality, usage, installation, and troubleshooting. Includes:

**Technical documentation**
* Requirements specifications
* System architecture
* API specifications
* Deployment guides

**User documentation**
* Installation guides
* Quickstart guides
* User manuals
* CLI usage instructions
* Tutorials and how-to guides
* Troubleshooting and FAQs

#### Documenting the software project

Covers external-facing details about development, contribution, licensing, and community. Includes:
* README
* Contributing guidelines
* Roadmap
* Changelog and release notes (see more in the [Releasing software page](./releasing_software))
* Licensing information (see more in the [Licensing software page](./licensing_software))
* Code of Conduct
* Software citation instructions
* List of authors and contributors
* Pointers to further documentation

An excellent overview of what documentation each software project should provide can be found in the [Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).

## References

1. [Lee B. D., Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561)
2. [Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P. Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)
3. [Perez-Riverol Y, Gatto L, Wang R, Sachsenberg T, Uszkoreit J, Leprevost FdV, et al. Ten Simple Rules for Taking Advantage of Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004947)
4. [How to Write Software Documentation in 7 Simple Steps](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/)
5. [The Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).
