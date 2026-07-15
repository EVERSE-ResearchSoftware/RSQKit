---
title: Creating a good README
description: How to create a good README document for your software project.
contributors: ["Esteban González", "Aleksandra Nenadic", "Daniel Garijo"]
page_id: creating_good_readme
related_pages:
  tasks: [software_documentation, documenting_software_project, documenting_code, licensing_software]
quality_indicators: [software_has_documentation, software_has_citation, software_has_license, requirements_specified]
keywords: ["readme", "documentation", "installation", "citation", "license", "contribution"]
---

## Why does your research software need a good README?

### Description

Your README file is a key document in a software project that provides an overview of the software to help developers and users understand the project and how to use it.
You typically write it in plain text or Markdown and place it in your project's root directory, so it is shared along with the code.
For software shared in a public software repository - the README file serves as the project's homepage and a central reference for documentation, aiding software's accessibility and promoting engagement for open source projects.

The README file is the entry point to the [documentation associated with a software project][documenting-project] and the [code within the project][documenting-code].
The main purpose of the README is to:

- Describe the software project and its purpose.
- Facilitate the installation and explain the use of the software - including installation instructions, dependencies and usage guidelines.
- Include contribution guidelines to help community understand how to contribute to the project and ensure smooth collaboration. This may cover coding standards, pull request procedures, issue reporting, and community rules.

For research software, additional aspects should be considered and README should also:

- Document the process for reproducing or replicating research method or experiments.
- Include citation information, either within the README or a pointer to a separate CITATION document.
- Describe connections to other research outputs, such as publications and datasets.

### Considerations

A [well-written README document][readme-practices]:

- promotes the [adoption of your software][adoption-paper].
- enhances the transparency of your research.
- supports software maintenance throughout its lifecycle.

Also check [guidelines for creating a good README][readme-guidelines].

## What sections should you include in your README?

### Description 

Your README is usually the first document a researcher reads when they are interested in using your software.
For this reason, it should contain all the relevant information to install and to execute it. 
It includes references to additional information such as API documentation, specifications, scientific publications related, tutorials, guidelines, etc.

A basic README emphasises these aspects:

- Understandability: a user can comprehend the structure and the purpose of the software.
- Usability: a user can understand how to use the software.
- Attribution: how a user should cite the software.

These aspects should be addressed in different sections of the README.

### Considerations

Your README document should:

* describe the purpose and features of the software.
* describe how to run and use the code and (optionally) reproduce the scientific experiment it implements. 
* acknowledge the funding bodies and contributors.
* indicate how the software should be cited or acknowledged.
* be held to the same accuracy and completeness expectations if you use AI assistance to draft or edit it — verify that commands, requirements, and citation details are correct before publishing.

### Solutions

The following sections can be included in the README to facilitate the use of the software and to allow its citation.

#### Description

In this section, you will have to describe the purpose and the features of your software.

#### Requirements

In this section, you can include the requirements needed to install and to execute the software.
These requirements can be software (e.g. operative system) or hardware (e.g. CPU, memory, etc.).
There is no need to include low level requirements like language library dependencies.
These requirements must be provided with the appropriate mechanism of each language.
For example, in {% tool "python" %} by using the requirements.txt file.

This is a non exhaustive list of requirements categories that you can consider:

- Operating system version
- Operating system libraries version 
- Version of the interpreter (e.g. {% tool "python" %} 3.9, {% tool "java" %} 7, etc.)
- Additional software needed to execute the software. For example, a database, a workflow engine, etc.
- Infrastructure requirements (e.g. number of CPUs, memory, disk, etc.)  

#### Installation process

In this section, you can describe the installation steps needed to install the software.
You have to assume that the user has no knowledge about operative systems or programming languages, so you need to be exhaustive.
It is important to reflect all the commands that must be executed by the user.

In case you need to install additional software, like a Java Virtual Machine or a database, you will have to add a link to additional information that describes how to install it.

If you have multiple options for installing the software (e.g. installing a library, {% tool "docker" %}, script) you should describe them.

#### Configuration

Sometimes, software needs to be configured to be executed.
Usually, this task is done by filling in a configuration file.
You will need to add this information to the README.
In case you have documentation that describes the fields of the configuration file, you can also add it to the README.

#### Usage

In this section, you should include all the steps needed to use the application.
For example, if it is a command line tool, you will need to describe all the parameters.
As we mentioned in the installation section, you have to assume no skills in the user, so you will need to be exhaustive.

It is recommended to add examples of the application usage in order to illustrate users in the software management.
This information can be complemented with links to tutorials in different formats (e.g. video, PDF, notebooks, etc.)

Research software can be developed to execute experiments whose results are shown in a scientific publication.
For this reason, and to add transparency to the research, it is important to show how the results can be achieved.
You can use this section to describe the process to get the results.

#### Contribution

Research software works best as a collaborative effort, so describe the mechanism you use to let others contribute.
For example, if you want to add a new feature, you can create a pull request to integrate this new feature.

#### Acknowledgements

All funders of the research software should be mentioned in the README - check the acknowledgement policy of each institution for how best to do it.

#### Citation

Citation is fundamental in a research context.
In this section, you can add how you want your software to be cited in publications.
It is a common practice to add this information in a `CITATION.cff` file but it is a recommended practice to add it to the README file too (e.g., in Bibtex format).

Remember that you can include badges in your README file to add visual information about your software project.
You can see a list of them used to make your project more fair in {% tool "howfairis" %}.

#### License

Software without a license cannot legally be reused in other applications.
While having a [license file][licensing-software] is a common practice in code repositories, you may also add this information explicitly as a section of your README file.
For more information, see [our guidelines][licensing-software] on how to select an appropriate license.

#### Automated extraction of metadata from README

{% tool "somef" %} is a [tool to automatically extract information (metadata) from README files][somef-paper].
It is not an assessment tool for README files, but can be used for detecting missing parts of a README file.

## Further Reading

- **[Guidelines for creating a README file][readme-guidelines]** A concise, practical checklist for structuring a README, written specifically with research data and software in mind. Use it as a quick reference once you already know what each section should contain.

- **[Record of a specific analysis][rsspdc-record]** This Research Software Sharing, Publication, & Distribution Checklists (RSSPDC) documentation checklist complements this page's narrative guidance with a graduated self-assessment tool — its Bronze-through-Platinum tiers let you check your README against concrete criteria, with particular emphasis on reproducibility and verifiability that is especially relevant for analysis code underpinning published results.

- **[README.md: History and Components][readme-history]** This article traces the origins of the README convention and systematically breaks down its key structural components, giving readers a concise mental model of both why READMEs exist and what belongs in them. That historical and structural grounding complements RSQKit's task-oriented guidance by helping readers understand the reasoning behind README best practices.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.

{% assign child_pages = page.child_pages | join: ', ' %}
{% if child_pages != null and child_pages != '' %}
## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}
{% endif %}

[adoption-paper]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4281782
[documenting-code]: ./documenting_code.md
[documenting-project]: ./documenting_software_project.md
[licensing-software]: https://everse.software/RSQKit/licensing_software
[readme-guidelines]: https://data.4tu.nl/s/documents/Guidelines_for_creating_a_README_file.pdf
[readme-history]: https://medium.com/@NSomar/readme-md-history-and-components-a365aff07f10
[readme-practices]: https://tilburgsciencehub.com/topics/collaborate-share/share-your-work/content-creation/readme-best-practices/
[rsspdc-record]: https://rsspdc.org/checklists/rsspdc-specific-record.html#documentation
[somef-paper]: https://ieeexplore.ieee.org/document/9006447/
