---
title: Documenting software project
description: How to write clear and useful software project documentation for end-users and collaborators?
contributors: ["Azza Gamgami", "Aleksandra Nenadic", "Laura Portell-Silva"]
page_id: documenting_software_project
related_pages:
  tasks: [software_documentation, documenting_code, documenting_software_readthedocs, creating_good_readme]
quality_indicators: [software_has_documentation]
keywords: ["software documentation", "documentation", "code documentation"]

---

## How to document your software project?

### Description

Software project documentation describes the software as a whole: its purpose, audience, installation instructions, usage examples, licensing, and contribution guidelines.
This information typically appears in files such as a README, INSTALL, or CONTRIBUTING, and helps users and collaborators understand how to work with the project (rather than the code itself).

When compared to [technical code documentation][documenting_code], which explains how the code works internally to other developers, project documentation is mainly intended for end-users to help them use and adopt your software for their work scenarios.

### Considerations

* Audience - identify who will read the documentation (e.g., end users, collaborators, contributors) and write at the right level of detail and technical depth.
Typically, software project documentation does not cover in-depth [technical documentation][documenting_code] apart from how to install and run the software, but may point to it.
* Purpose - clarify what the documentation is meant to achieve — e.g., helping users install and run the software, explaining research context, or enabling contributions.
* Structure - organise information logically. For example, consider including a clear description (README), installation guide, usage examples, contribution guidelines, and license information.
* Keep it up to date - update documentation whenever functionality or dependencies change; outdated documentation can be less helpful than none.
* Accessibility - ensure the documentation is easy to find, read, and navigate (e.g., hosted on GitHub Pages, with clear headings and links to different parts of documentation held in various files).
* Reproducibility - include enough information for others to reproduce results — such as environment setup, data requirements, and example workflows.

### Solutions

Documenting a research software project is much like documenting any open project.
Project documentation details key external-facing elements of a software project, focusing on managing and tracking its development, usage, contributions and community.

An excellent overview of what documentation each software project should provide can be found in the [Turing Way's "Guide for Reproducible Research"](https://book.the-turing-way.org/reproducible-research/reproducible-research) - section on [project documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-project).
Also check ["How to Write Software Documentation in 7 Simple Steps"](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/) and [Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561).

Project documentation should include the following:

- README - a text or Markdown file in the project root that introduces and explains a project and explains the basic functionality, dependencies and usage of your software. README
  also acts as a homepage for your project on code sharing platforms such as {% tool "github" %} and {% tool "gitlab" %}.
  See more on [how to create a good README document for your software project][creating_good_readme].
- Installation instructions (INSTALL) - a text or Markdown file in the project root that provides steps on how to download and/or run software. This information can also be a section in the README.
- Licensing (LICENSE) - a text or Markdown file in the project root that lets users know under what legal conditions they are allowed to use the software. 
See more on [how to license your software project][licensing_software].
- Software citation (CITATION) - a CFF, text or Markdown file in the project root that lets people know how to cite or credit your software. 
See more on [how to cite your software project][citing_software].
- Contributing guidelines (CONTRIBUTING) - a text or Markdown file in the project root that describes how people can contribute to the development of software and get involved in the project.
- Code of Conduct (CODE_OF_CONDUCT) - a text or Markdown file in the project root that helps create and maintain a collaboration environment that promotes participation, collaboration and exchange of ideas, while fostering respect among developers.
- List of all authors and contributors to the software - e.g. listed under a section in README or in a separate file AUTHORS/CONTRIBUTORS in the project root, or a pointer to a list of project collaborators.
- Pointers to various other technical documentation about your software (installation guide, source code/API documentation, deployment documentation, etc.).
- Roadmap - an overview of the current and future development plans and milestones (this can also be a pointer to your issue tracker, e.g. in GitHub).
- Changelog and release notes - a text file that contains a record of what notable changes are made between versions of software.

[open-api]: https://swagger.io/specification/
[click]: https://click.palletsprojects.com/en/stable/
[magicblast]: https://ncbi.github.io/magicblast/
[documenting_code]: ./documenting_code
[citing_software]: ./citing_software
[creating_good_readme]: ./creating_good_readme
[licensing_software]: ./licensing_software