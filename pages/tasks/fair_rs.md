---
title: Adopting FAIR software practices
description: What practices and tools can help improve FAIRness of software?
contributors: ["Aleksandra Nenadic", "Daniel Garijo"]
page_id: fair_rs
indicators: []
related_pages: 
  tasks: [software_metadata, citing_software, licensing_software, software_documentation, documenting_code, archiving_software, organising_software_projects]
keywords: ["fair software", "fair"]
---

## What is FAIR Research Software?

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to increase the visibility and usefulness of your research to others.
The [FAIR data principles][fair-data], first published in 2016, are widely known and applied today to other areas, including [software][fair-rs], [scientific workflows][fair-workflows], or [machine learning projects][fair4ml].

The FAIR software principles for software mean that it should be:

- **Findable** - software and its associated metadata must be easy to discover by humans and machines.
- **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols, free and legally usable.
- **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through standardised protocols and application programming interfaces (APIs).
- **Reusable** - software should be usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software).

Let's have a quick look into what each of the above principle means in practice.
[Five Recommendations for FAIR Software](https://fair-software.eu/) also gives a quick overview of what is making software more FAIR entails.

### How can we Make our Software Findable?

- [Create a description of your software][software_metadata] to make it discoverable by search engines and other search tools
- Use standards (such as [CodeMeta][codemeta]) to describe interoperable metadata for your software (see [Research Software Metadata Guidelines][rsmd-g1])
- Place your software in a public software repository (and ideally register it in a [general-purpose or domain-specific software registry][software-registries])
- Use a unique and persistent identifiers for your software, such as **Digital Object Identifiers** (DOIs) provided by [Zenodo][zenodo], [FigShare][figshare], or **SoftWare Heritage persistent IDentifiers** ([SWHID](swhid)) provided by [Software Heritage][software-heritage]. 
In addition to findability of your software, identifiers can help you get credit for your work by providing citable references.
- More broadly, use software sharing and collaborative platforms, as they facilitate code publication, sharing and findability:
  - general-purpose software repositories - [GitHub][github] and [GitLab][gitlab]
  - programming language-specific software repositories - [PyPi][pypi] (for Python) and [CRAN][cran] (for R)
  - software registries - [BioTools][biotools] (for biosciences) and [Awesome Research Software Registries][awesome-rs-registries], providing a list of research software registries (by country, organisation, domain and programming language) where research software can be registered to help promote its discovery

### How can we Make our Software Accessible?

- Make sure people can obtain get a copy your software using standard communication protocols (e.g. HTTP, FTP, etc.)
- The code and its description (metadata) should be available even when the software is no longer actively developed (this includes earlier versions of the software) - see [software archiving][archiving_software]

### How can we Make our Software Interoperable?

- Use community-agreed standard formats for inputs and outputs of [your software and its metadata][software_metadata] (e.g. [CodeMeta][codemeta])
- Communicate with other software and tools via standard protocols and APIs
- Using standard data exchange, input and output formats and communication protocols helps create interoperable software that can more readily integrate with other tools into more complex pipelines 
- More broadly - explain the [functionality of your software and protocols (e.g command line interface) for interaction with it][documenting_code]

### How can we Make our Software Reusable?

- [Document your software][software_documentation] (including its functionality, how to install and run it) to make it more understandable by others who may wish to reuse or extend it
- [Give a licence to your software][licensing_software] clearly stating how it can be reused (check the [open source licence guide][opensource-licence-guide] or [choosealicense.com][choosealicense] on choosing the licence most appropriate for your needs)
- State how to [cite your software][citing_software], so people can give you credit when they reuse it
- More broadly, follow best practices for software development, e.g. [structure your software][organising_software_projects] using common patterns and use coding conventions to make your code readable and understandable by people

## FAIR and Quality

FAIR software sits squarely within the broader umbrella of **quality research software**.
[Quality software][rs-quality] is defined by multiple aspects - e.g. correctness, performance, maintainability, usability, robustness, and reproducibility, among others.
Reproducibility (the “openness & reusability” slice of software quality) often hinges on the FAIR principles: if your code and metadata are not findable or accessible, no one can rerun it; if it is not interoperable or reusable, others cannot adapt or extend or use it to verify your results.

So, FAIR is a crucial subset of quality, primarily ensuring that your software can actually be discovered, understood, and exercised by others (or by you, months down the line).
A truly high-quality, reproducible research software package will typically satisfy both classical software-engineering criteria (tests, style, documentation, performance) and the FAIR principles.

## Tools and Practices for FAIR

There are various tools and practices that support the development of FAIR research software - some of them listed above.
These tools and practices work together, as no single tool or practice will fully address one principle, but can contribute to multiple principles simultaneously.

It is important to note that while FAIR can improve software quality in several aspects - it does not say anything about its functionality.
This mean that software may be FAIR, but still not very good in terms of what it does - other practices need to be employed (e.g. [testing software][testing_software]) to make sure it works on different platforms/operating systems and that it is correct and does what it is set out to do.

Tools and frameworks exist for assessing software FAIRness:

- [FAIRsoft evaluator][fair-rs-evaluator]
- [FAIR software test][fair-rs-test]
- [FAIR Software Checklist][fair-rs-checklist] - a self-assessment tool developed by the Australian Research Data Commons (ARDC) and the Netherlands eScience Center
- ["How FAIR is your software"][howfairis] - a command line tool to evaluate a software repository's compliance with the FAIR principles
- [CODECHECK][codecheck] - an approach for independent execution of computations underlying research articles
- [Common metrics for Research Software][fair-metrics] that may used to assess each of the FAIR4RS principles

They not meant to criticise or discredit software or its authors. 
Their role is to make quality aspects visible, help researchers identify strengths and areas for improvement, and support the evolution of good practices. 
In the context of research software, such assessments are diagnostic rather than evaluative — they guide reflection, transparency, and learning, not scoring or ranking. 
By using them, researchers can better understand how their software performs across different aspects of FAIRness and make informed decisions about how to improve it.

[awesome-rs-registries]: https://github.com/NLeSC/awesome-research-software-registries
[biotools]: https://bio.tools
[cff]: https://citation-file-format.github.io/
[choosealicense]: https://choosealicense.com/
[codecheck]: https://codecheck.org.uk/project/
[codemeta]: (https://codemeta.github.io/)
[cran]: https://cran.r-project.org/web/packages/
[fair-cookbook]: https://faircookbook.elixir-europe.org/content/home.html
[fair-rs-evaluator]: https://openebench.bsc.es/observatory/Evaluation
[fair-rs-test]: https://github.com/marioa/fair-test?tab=readme-ov-file
[fair-rs-checklist]: https://fairsoftwarechecklist.net
[fair4ml]: https://www.rd-alliance.org/groups/fair-machine-learning-fair4ml-ig/activity/
[figshare]: https://figshare.com/
[github]: https://github.com
[gitlab]: https://about.gitlab.com/
[howfairis]: https://github.com/fair-software/howfairis/
[opensource-licence-guide]: https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project
[rsmd-g1]: https://fair-impact.github.io/RSMD-guidelines/1.General/
[swhid]: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html
[pypi]: https://pypi.org/
[software-heritage]: https://www.softwareheritage.org/
[software-registries]: https://github.com/NLeSC/awesome-research-software-registries
[zenodo]: https://zenodo.org/
[fair-data]: https://doi.org/10.1038/sdata.2016.18
[fair-workflows]: https://doi.org/10.1038/s41597-025-04451-9
[fair-rs]: https://doi.org/10.15497/RDA00068
[rs-quality]: ./rs-quality
[fair-metrics]: https://doi.org/10.5281/zenodo.15535629
[software_metadata]: ./software_metadata
[software_documentation]: ./software_documentation
[licensing_software]: ./licensing_software
[documenting_code]: ./documenting_code
[archiving_software.md]: ./archiving_software
[testing_software]: ./testing_software
[citing_software]: ./citing_software
[organising_software_projects]: ./organising_software_projects