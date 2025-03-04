---
title: Software documentation
description: How to write clear and useful software documentation for developers and end-users
contributors: ["Azza Gamgami"]
page_id: software_documentation
related_pages:
  your_tasks: [creating_readthedocs, how_to_make_a_good_readme]
---

## How to create good software documentation?

### Description

Software documentation is an essential part of the software development process, designed to provide clear 
communication between various stakeholders including developers, testers, users, and project managers. 
It helps align the expectations and goals of all parties, while also ensuring the software is easy to understand and use.

### Considerations

* Software documentation should be clear, consistent, regularly updated, cover all key software aspects, encourage feedback, and ideally be auto-generated to a large extent.
* Each piece of documentation should have a distinct purpose, based on the intended users. Different users of software can largely be categorised into the following (often overlapping) groups, based on their roles, needs, and level of expertise:
  * *end users* (general users) - individuals who use software for personal or work-related tasks.
  * *administrators* - responsible for installing, configuring, managing, and maintaining software systems.
  * *developers* (programmers) - who create, modify, and debug software applications.
* Software documentation can vary in focus depending on the specific aspect of the software it addresses.
  * *product documentation* refers to a comprehensive set of documents that provide information about a software product, including its features, functionality, usage, and maintenance (e.g., requirements documents, high-level software description in README files; source code documentation, end user documentation such as user guides and API references). It targets all users - end users, administrators, and developers - and ensures that they can effectively understand, operate, and troubleshoot the software.
  * *process documentation* is primarily intended for the development team (e.g., plans; progress reports that track progress; working papers that capture ideas and notes from the team).

### Solutions

#### Understand the purpose and audience for your documentation

* Think about who will be using the documentation and what is its purpose. 
* Understanding the purpose allows you to tailor the content accordingly. For example:
  * *user documentation* (e.g. end user guides) -  should explain clearly what the software does and how it should be used, focussing on usability and clarity and offering step-by-step instructions. 
  * *developer documentation* (including software specification, docstrings, in-line comments, etc.) - covers in-depth techincal details about the software and should explain how the software can be modified, tested, and contributed to (governance, code of conduct, contributing guidelines, etc.).
  * *deployment documentation* (e.g. installation and administration guide) - should explain system requirements (e.g. dependencies) for installing/deploying and running the software on various platforms/infrastructures and instructions for installation and testing.
* Create personas to represent your audience for better-targeted technical content - it helps categorise your help documentation.

#### Write comments and docstrings as you code

* Ensure you strike a balance in the amount of commenting - you do not have to explain each line of your code
* Focus on the *why* and the *how* of your code - avoid using comments to explain what your code does. If your code is too 
complex for other programmers to understand, consider rewriting it for clarity rather than adding comments to explain it.
* Use integrated development environments (IDEs), such as {% tool "vscode" %}, {% tool "pycharm" %} or {% tool "eclipse" %}, 
that automatically generate documentation strings using extensions like {% tool "jsdoc" %} or {% tool "python-docstring-generator" %}.

#### Write meaningful explanations for error messages

To help your users troubleshoot issues when using your software, error messages returned by your code should clearly state:

* When and where the error occurred
* What went wrong
* The state of the software at that point
* How to fix it or where to find relevant information or solution in your documentation.

#### Include a quickstart guide

* A quickstart guide enables users to move quickly from idea to experimentation. This can take the form of an example, tutorial, or a video. 
For instance, [a quickstart guide for TPOT (Tree-Based Pipeline Optimization) tool](http://epistasislab.github.io/tpot/) includes an animated GIF and minimal code snippets.

#### Include a README file with basic software description

* The README file should explain the basic functionality of your code and how to install and use it (e.g. a quick start guide). 
It also acts as a homepage for your project on code sharing platforms such as {% tool "github" %} and {% tool "gitlab" %}. 
* README should include a link to the full software documentation. 
* See more details on [how to create a good README file](how_to_make_a_good_readme.md).

#### Include examples of code usages 

* Examples help users understand and experiment with the software and showcase different aspects of your software. 
* If your documentation becomes too cluttered, consider moving examples to a dedicated section. 
* For instance, [Keras](https://github.com/keras-team/keras/tree/master/examples)  provides example scripts to demonstrate its functionalities along with a README file that outlines.

#### Version control software documentation

* Since your documentation is a crucial component of your code, it should also be under version control. 
Store your documentation within your software's repository alongside code and other files. 
* Services like {% tool "readthedocs" %} and {% tool "zenodo" %} can help by automatically generating documentation from your code and archiving your software's documentation with each new release of your software.
* *Read the Docs* used the Git workflow you already use for code - treating documentation like code lets your team use tools they already know, and makes keeping your docs updated easier. 
Read more on [how to create a *Read the Docs* page](https://everse.software/RSQKit/creating_readthedocs). 

A good example of a bioinformatics library effectively managing version control for its documentation is [khmer](https://github.com/dib-lab/khmer/). 
This library features a comprehensive changelog that details new features, bug fixes (categorized based on relevance to users or developers), 
known issues, and a list of contributors for each release. 

#### Document the Command Line Interface (CLI) or the Application Programming Interface (API) of your software

If your software has a Command Line Interface (CLI) or an Application Programming Interface (API) - make sure you describe its usage, as it 
will serve as a reference for your users as well as developers.

An effective way to document the CLI is to implement a `help` command that provides instructions on how to use the software so that users do not have to search for documentation to complete basic tasks.

The `help` command should cover:

* Usage instructions (how to execute the command).
* Relevant subcommands
* Options and/or arguments
* Applicable environment variables
* And ideally, some examples.

Tools like [Click](https://click.palletsprojects.com/en/stable/) for Python can assist you not only in creating your help command but also in building your interface.
A great example of a good CLI is the one included with the [Magic-BLAST](https://ncbi.github.io/magicblast/) bioinformatics tool.

The [OpenAPI Specification][open-ai], previously known as the Swagger Specification, is a specification for a machine-readable API definition language for describing, producing, consuming and visualising web services.
{% tool "swagger" %} is a set of open-source tools built around the OpenAPI Specification that can help you design, build, document, and consume REST APIs. 

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

## References
1. [Lee B. D., Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561)
2. [Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P. Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)
3. [Perez-Riverol Y, Gatto L, Wang R, Sachsenberg T, Uszkoreit J, Leprevost FdV, et al. Ten Simple Rules for Taking Advantage of Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004947)
4. [How to Write Software Documentation in 7 Simple Steps](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/)


[open-ai]: https://swagger.io/specification/
