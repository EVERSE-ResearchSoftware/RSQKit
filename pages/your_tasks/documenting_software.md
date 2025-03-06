---
title: Documenting software
description: How to document your software project?
contributors: ["Azza Gamgami", "Aleksandra Nenadic"]
page_id: documenting_software
related_pages:
  your_tasks: [writing_readable_code, creating_readthedocs, creating_readme]
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

* There are two types of software documentation:
  * Product documentation targets both internal and external users (e.g., requirements documents, high-level software description in README files; source code documentation, end-user documentation such as user guides and API references).
  * Process documentation is primarily intended for the development team (e.g., plans; progress reports that track progress; working papers that capture ideas and notes from the team).

It can be categorized into internal documentation (for developers) and external documentation (for end-users and stakeholders).

   Automate where possible – Use tools like Javadoc, Sphinx, or Swagger for generating docs.
    Keep it concise and clear – avoid unnecessary complexity.

Would you like help with a specific aspect, such as tools or templates?

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

- write comments as you code
- ensure you strike a balance in the amount of commenting - you do not have to explain each line of your code
- focus on the *why* and the *how* of your code - avoid using comments to explain what your code does. If your code is too
  complex for other programmers to understand, consider rewriting it for clarity rather than adding comments to explain it
- use integrated development environments (IDEs), such as {% tool "vscode" %}, {% tool "pycharm" %} or {% tool "eclipse" %}
  that automatically generate documentation strings using extensions like {% tool "jsdoc" %} or {% tool "python-docstring-generator" %}
- write meaningful explanations for error messages - to help your users troubleshoot issues when using your software, 
error messages returned by your code should clearly state: when and where the error occurred, what went wrong, the state of the software at that point, 
how to fix it or where to find relevant information or solution in your documentation.

Also see the [related page on writing readable code](./writing_readable_code).

#### Interface documentation

Software interface documentation describes how different software components or systems interact with each other, 
outlining various interfaces (including API) and communication protocols:

- describes how to use functions, classes, and modules
- includes parameters, return values, exceptions, and usage examples for functions and classes
- tools like {% tool "javadoc" %}, {% tool "doxygen" %}, and {% tool "sphinx" %} can help automate generation of this 
documentation type from documentation strings (see [above](#code-comments)).

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
- User manuals – step-by-step instructions on how to use the software 
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

- README - a text file that introduces and explains a project. It contains information that is commonly required to understand what the project is about.
See more on [how to create a good README document for your software project](./creating_readme).
- Contributing guidelines - describes how people can contribute to the development of software and get involved in the project.
- Roadmap - an overview of the current and future development plans and milestones.
- Changelog and release notes - a text file that contains a record of what notable changes are made between versions of software.
- Licensing - lets users know under what legal conditions they are allowed to use the software.
- Code of Conduct - to create and maintain a collaboration environment that promotes participation, collaboration and exchange of ideas, 
while fostering respect among developers.
- Software citation - let people know how to cite your software, see more on [how to cite your software project](./citing_software).
- List of all authors and contributors to the software 
- Pointers to various other documentation about your software
 
#### README Files

- High-level overview of the project, including setup instructions, dependencies, usage, and contribution guidelines.
- Typically written in Markdown format for better readability.




-----------------

## Good practices for creating software documentation


#### Include examples of code usages 

* Examples help users understand and experiment with the software and showcase different aspects of your software. 
* If your documentation becomes too cluttered, consider moving examples to a dedicated section. 
* For instance, [Keras](https://github.com/keras-team/keras/tree/master/examples)  provides example scripts to demonstrate its functionalities along with a README file that outlines.

#### Include a quickstart guide

* A quickstart guide enables users to move quickly from idea to experimentation. This can take the form of an example, tutorial, or a video. 
For instance, [a quickstart guide for TPOT (Tree-Based Pipeline Optimization) tool](http://epistasislab.github.io/tpot/) includes an animated GIF and minimal code snippets.

#### Include a README file with basic software description

* The README file should explain the basic functionality of your code and how to install and use it (e.g. a quick start guide). 
It also acts as a homepage for your project on code sharing platforms such as {% tool "github" %} and {% tool "gitlab" %}. 
* README should include a link to the full software documentation. 
* See more details on [how to create a good README file](creating_readme).

#### Version control software documentation

* Since your documentation is a crucial component of your code, it should also be under version control. 
Store your documentation within your software's repository alongside code and other files. 
* Services like {% tool "readthedocs" %} and {% tool "zenodo" %} can help by automatically generating documentation from your code and archiving your software's documentation with each new release of your software.
* *Read the Docs* used the Git workflow you already use for code - treating documentation like code lets your team use tools they already know, and makes keeping your docs updated easier. 
Read more on [how to create a *Read the Docs* page](https://everse.software/RSQKit/creating_readthedocs). 

A good example of a bioinformatics library effectively managing version control for its documentation is [khmer](https://github.com/dib-lab/khmer/). 
This library features a comprehensive changelog that details new features, bug fixes (categorized based on relevance to users or developers), 
known issues, and a list of contributors for each release. 

#### Use automated documentation tools

While no software can completely write software documentation for you, several tools can significantly ease the process.

* {% tool "sphinx" %} (for Python and other languages), {% tool "doxygen" %} (for C++ and other languages), {% tool "roxygen" %} (for R) and {% tool "jsdoc" %} (for JavaScript) can generate documentation in multiple formats (HTML, PDF) and automatically extract comments from annotated code in your codebase.
* {% tool "mkdocs" %} enables the creation of professional-looking documentation websites using Markdown.
* {% tool "swagger" %} automatically generates API documentation, providing user-friendly interfaces for developers.
* {% tool "documenter-jl" %} is a Julia package for building documentation from docstrings in code and Markdown files.
* Leverage CI/DC tools, offered by platforms such as {% tool "github" %} and {% tool "gitlab" %} to automate quality assurance and release of your updated documentation to the public. For example, take a look at the [GitHub actions in the RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit/actions) 
for some automated tasks. 


## References
1. [Lee B. D., Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561)
2. [Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P.Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)
3. [Perez-Riverol Y, Gatto L, Wang R, Sachsenberg T, Uszkoreit J, Leprevost FdV, et al. Ten Simple Rules for Taking Advantage of Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004947)
4. [How to Write Software Documentation in 7 Simple Steps](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/)
5. [The Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).


