---
title: Documenting code
description: How to write technical documentation to explain to other developers how your code works internally?
contributors: ["Azza Gamgami", "Aleksandra Nenadic", "Laura Portell-Silva"]
page_id: documenting_code
related_pages:
  tasks: [documenting_software_project, writing_readable_code, creating_good_readme]
child_pages: [documenting_software_readthedocs]
quality_indicators: [software_has_documentation]
keywords: ["documentation", "code documentation"]

---

## How to document your code?

### Description

Code documentation explains how the code works internally.
It supports developers who maintain or wish to extend the code by making its logic and structure easier to understand and follow.
When compared to [software project documentation][documenting_software_project], which helps people use and adopt your software, code documentation helps people develop and sustain it.

Check ["How to Write Software Documentation in 7 Simple Steps"](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/) and [Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561) for more reading on the topic.

### Considerations

* Software documentation should be accessible, clear, consistent, regularly updated, cover all key software aspects and encourage feedback.
  For example, it can include: source code documentation, requirements specifications, software architecture, installation and usage, command line interface (CLI), API specification, deployment guide, tutorials and how-to guides, troubleshooting guides and FAQs.
* It should be automatically generated where possible, and use standard documentation formats such as (R)Markdown, reStructuredText, HTML, PDF, or wikis.
* Each piece of code documentation serves a distinct purpose and is aimed at different technical audience:
  * *Administrators* – who are responsible for installing, configuring, managing, and maintaining software systems.
  * *Developers* – who create, modify, debug, and maintain software applications.
  * *Testers* – who test the code according to its specification.
* Code documentation can vary depending on the aspect of the code it addresses:
  * *Product documentation* provides comprehensive information about the software’s features, functionality, usage, and maintenance. Examples include requirements documents, high-level descriptions (e.g., README files), source code documentation, user guides, and API references. It targets multiple audiences, ensuring they can understand, operate, and troubleshoot the software.
  * *Process documentation* is primarily intended for the development team and may include plans, progress reports, working papers, and notes that capture development ideas and decisions.

It should be noted that *end users* - individuals who use the software for personal or work-related tasks - are not the target audience of code documentation (but rather [software project documentation][documenting_software_project]).

It should also be noted that code and software project documentation are sometimes mixed together - for example installation and usage documentation may be targeted at end-users and developers/administrators alike.

### Solutions

#### Understand purpose and audience

* Create and maintain different types of software documentation based on its **purpose** and **intended audience**.
* Think about who will be using the documentation and tailor content accordingly:
  * *User documentation* (for end-users) – explains clearly what the software does and how to use it; focuses on usability, clarity, and step-by-step instructions (e.g., end user guides).
  * *Developer documentation* (for developers and testers) – covers in-depth technical details such as specifications, docstrings, inline comments, error messages, contribution guidance, testing, and software governance.
  * *Deployment documentation* (for developers and administrators) – provides installation, configuration, dependency, platform, and testing instructions.
* Creating personas can help target content effectively for different audiences.

#### Document as you code

Code comments are documentation embedded in your source code and include:

* Inline comments – short explanations for specific lines/blocks
* Block comments – detailed explanations for complex logic
* Documentation strings – structured descriptions of functions/classes/modules

A documentation string is a string literal specified in source code that is used, like a comment, to document a specific segment of code. 
The difference is that the documentation string is visible to the outside world, while comments are not. 
Documentations strings are for helping people use the code, while comments are meant for people modifying the code - yourself and other developers.

Some general advice when writing comments:

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

#### Include a quickstart guide and a more detailed tutorial

* Quickstart guide offers a fast path from setup to experimentation 
* Tutorials include more details step-by-step information on installing, running and experimenting with your software.
* The [TPOT tool](http://epistasislab.github.io/tpot/) includes an effective quickstart with code snippets and visuals.

#### Provide a README
README overlaps slightly with the [software project documentation][documenting_software_project], but can be used as part of code documentation to explain or point to technical details.

* README file explains basic functionality, installation steps, and usage (e.g., a quick start).
* It acts as a project homepage on platforms like {% tool "github" %} and {% tool "gitlab" %}.
* Include links to full project and code documentation.
* See more details on [how to create a good README file][creating_good_readme].

#### Document Command Line Interface (CLI) or the Application Programming Interface (API)

If your software provides a CLI or API:

* Describe usage, subcommands, options, arguments, and environment variables.
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

#### Version control your documentation

* Store documentation in the project repository and track it using version control.
* Treat documentation like code to keep it updated through familiar workflows. Read more on [how to use *Read the Docs* for your software project](documenting_software_readthedocs.md).
* {% tool "readthedocs" %} integrates with Git workflows and can automatically publish documentation. See more in the [Documenting Software Readthedocs page](./documenting_software_readthedocs).
* {% tool "zenodo" %} can archive documentation automatically with each software release.

Examples:
* The bioinformatics library [khmer](https://github.com/dib-lab/khmer/) uses version control for its documentation, includes a comprehensive changelog, lists contributors, and tracks user- vs developer-facing issues.
* *RSQKit* uses GitHub Actions to automate documentation tasks.

#### Use automated documentation tools

While no software can completely write software documentation for you, several tools can significantly ease the process.

* {% tool "sphinx" %} (for Python and other languages), {% tool "doxygen" %} (for C++ and other languages), {% tool "roxygen" %} (for R) and {% tool "jsdoc" %} (for JavaScript) can generate documentation in multiple formats (HTML, PDF) and automatically extract comments from annotated code in your codebase.
* {% tool "mkdocs" %} enables the creation of professional-looking documentation websites using Markdown.
* {% tool "swagger" %} can automate the generation of client libraries, server stubs, and API documentation efficiently based on API definitions. 
* {% tool "documenter-jl" %} is a Julia package for building documentation from docstrings in code and Markdown files.
* Leverage CI/DC tools, offered by platforms such as {% tool "github" %} and {% tool "gitlab" %} to automate quality assurance and release of your updated documentation to the public. For example, take a look at the [GitHub actions in the RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit/actions) 
for some automated tasks.

## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% assign child_pages = page.child_pages | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}

[documenting_software_project]: ./documenting_software_project
[creating_good_readme]: ./creating_good_readme