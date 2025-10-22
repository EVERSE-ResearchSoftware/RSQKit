---
title: Writing FAIRer Research Software
description: How can you develop FAIRer software?
contributors: ["Aleksandra Nenadic"]
page_id: fair_rs
indicators: []
related_pages:
keywords: ["fair software", "fair"]
---

## What is FAIR Research Software?

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to increase the visibility and usefulness of your research to others.
The FAIR data principles, first published in 2016[^1], are widely known and applied today, including scientific workflows[^2], or [machine learning projects][fair4ml].
Similar FAIR principles for software[^3][^4] have now been defined too.

In general, they mean:

- **Findable** - software and its associated metadata must be easy to discover by humans and machines.
- **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols, free and legally usable.
- **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through standardised protocols and application programming interfaces (APIs).
- **Reusable** - software should be usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below.
This is not an exact science, and by all means the list below is not exhaustive, but any of the practices that you employ in your research software workflow will bring you closer to the gold standard of fully reproducible research.

[Five Recommendations for FAIR Software](https://fair-software.eu/) is a quick overview of what is making software more FAIR entails.


[FAIR software][fair-rs-nature] — i.e. software that is Findable, Accessible, Interoperable, and Reusable — sits squarely within the broader umbrella of **quality research software**.
Quality software is defined by multiple dimensions - e.g. correctness, performance, maintainability, usability, robustness, and reproducibility, among others.
Reproducibility often hinges on the FAIR principles: if your code and metadata are not findable or accessible, no one can rerun it; if it is not interoperable or reusable, others cannot adapt or extend or use it to verify your results.

FAIR is not a completely separate concern — it is a crucial subset of quality, primarily ensuring that your software can actually be discovered, understood, and exercised by others (or by you, months down the line).
A truly high-quality, reproducible research software package will typically satisfy both classical software-engineering criteria (tests, style, documentation, performance) and the FAIR principles.

So, FAIR - the “openness & reusability” slice of software quality - is essential for reproducibility, but most impactful when combined with all the other [quality practices](rs_quality) like [testing][testing_software], [version control][using_version_control], and [robust software design][robust_software_design].

### Findable
- Create a description of your software to make it discoverable by search engines and other search tools
- Use standards (such as [CodeMeta][codemeta]) to describe interoperable metadata for your software (see [Research Software Metadata Guidelines][rsmd-g1])
- Place your software in a public software repository (and ideally register it in a [general-purpose or domain-specific software registry][software-registries])
- Use a unique and persistent identifier (DOI) for your software (e.g. by depositing your code on [Zenodo][zenodo]),
which is also useful for citations - note that depositing your data/code on GitHub and similar software repositories may not be enough as they may change their open access model or disappear completely in the future, so archiving your code means it stands a better chance at being preserved

### Accessible
- Make sure people can obtain get a copy your software using standard communication protocols (e.g. HTTP, FTP, etc.)
- The code and its description (metadata) has to be available even when the software is no longer actively developed (this includes earlier versions of the software)

### Interoperable
- Explain the functionality of your software and protocols for interaction with it
- Use community-agreed standard formats for inputs and outputs of your software and its metadata (e.g. [CodeMeta][codemeta])
- Communicate with other software and tools via standard protocols and APIs

### Reusable
- Document your software (including its functionality, how to install and run it) to make it more understandable by others who may wish to reuse or extend it
- Follow best practices for software development, e.g. structure your code using common patterns and use coding conventions to make your code readable and understandable by people
- Test your software and make sure it works on different platforms/operating systems
- Give a licence to your software clearly stating how it can be reused
- State how to cite your software, so people can give you credit when they reuse it

## Tools and practices to help you make software FAIRer

There are various tools and practices that support the development of FAIR research software.
These tools and practices work together, as no single tool or practice will fully address one principle, but can contribute to multiple principles simultaneously.

It is important to note that simply using these tools, without following good practice and guidance on how best to align their usage with the FAIR principles, is not enough to produce FAIR software.
In addition, FAIR is not a [software quality metric](https://everse.software/RSQKit/rs_quality) even though it can improve software quality in several aspects - software may be FAIR, but still not very good in terms of its functionality.

### Development environments

Virtual and integrated development environments (IDEs), such as VS Code or PyCharm, help with reading, running, testing, and debugging code.
Virtual environments further enable us to share our working environments with others, making it easier to reuse and extend our code.
IDEs often provide integrations with other tools, e.g. version control and command line terminals, enabling you to do many tasks from a single environment, saving time in switching between different tools.

### Command line terminals

Command line terminals (e.g. Bash, GitBash) enable us to run and test our code without graphical user interfaces (GUI) afforded to us by IDEs - this is sometimes needed for running our code remotely on servers and high-performance systems without a GUI provision, where time, memory and processing power are expensive or in high demand.

Version control systems are typically provided as command line tools, making them often only accessible from command line terminals to enter commands and access remote version control servers to backing up and sharing our work.

Finally, command line tools are interoperable software that use standard protocols for passing parameters, inputs and outputs via the command line terminal.
This makes it easier to integrate with other tools, allowing us to chain command line tools and build up complex and reproducible workflows and analysis pipelines using several programs in different steps.
If we write our software in a way which provides such an interoperable command line interface - we will be able to integrate it with other command line tools to automate and speed up our work.

### Standard input/output formats and communication protocols

Using standard data exchange, input and output formats and communication protocols helps create interoperable software that can more readily integrate with other tools into more complex pipelines - increasing its interoperability and reusability.

### Version control tools

Version control means knowing what changes were made to your code, when and by whom - promoting code ownership, responsibility and credit.
When combined with software sharing and collaborative platforms such as GitHub or GitLab, it facilitates code publication, sharing and findability, teamwork and discussions about software and design decisions, provides backup facilities for your code and speeds up collaboration on shared code by allowing edits by more than one person at a time.

### Code testing

Testing ensures that your code is correct and does what it is set out to do.
When you write code you often feel very confident that it is perfect, but when writing bigger codes or code that is meant to do complex operations it is very hard to consider all possible edge cases or notice every single typing mistake.
Testing also gives other people confidence in your code as they can see an example of how it is meant to run and be assured that it does work correctly on their machine - helping with code understanding and reusability.

### Coding conventions

Following coding conventions and guides for your programming language that is agreed upon by the community and other programmers are important practices to ensure that others find it easy to read your code, reuse or extend it in their own examples and applications.

### Code licensing

A licence is a legal document which sets down the terms under which the creator of work (such as written text, photographs, films, music, software code) is releasing what they have created for others to use, modify, extend or exploit.

It is important to state the terms under which software can be reused - the lack of a licence for your software implies that no one can reuse the software at all.
A common way to declare your copyright of a piece of software and the license you are distributing it under is to include a file called LICENSE in the root directory of your code repository.

Some good resources to check out for choosing a licence for your code:

- [The open source guide][opensource-licence-guide] on applying, changing and editing licenses.
- [choosealicense.com][choosealicense] has some great resources to help you choose a license that is appropriate for your needs, and can even automate adding the LICENSE file to your GitHub code repository.

### Code citation

We should add a citation file to our repository to provide instructions on how and when to cite our code.
A citation file can be a plain text (CITATION.txt) or a Markdown file (CITATION.md), but there are certain benefits to using use a special file format called the [Citation File Format (CFF)][cff], which provides a way to include richer metadata about code (or datasets) we want to cite, making it easy for both humans and machines to use this information.

### Code- and project-level documentation

Documentation comes in many forms - from **code-level documentation** to **project-level documentation**.
Code-level documentation may docstrings and additional inline comments that explain lines of your code.
Project-level documentation typically include README, LICENCE, CITATION, CONTRIBUTING, etc. files that help to describe and discover your project, explain the legal terms of reusing it, describe its functionality and how to install, run and contribute to it.
It can include separate technical documentation websites for your project with full documentation including function definitions, APIs, usage examples, tutorials and guides.
You many not need as much documentation as a large commercial software product, but making your code reusable relies on other people being able to understand what your code does and how to use it.

### Software repositories and registries

Having somewhere to share your code is fundamental to making it findable and accessible.
Your institution might have a code repository, your research field may have a practice of sharing code via a specific website, archive or journal, or your version control system might include an online component that makes sharing different versions of your code easy.
You should check the rules or guidelines of your institution, grant or domain on publishing code, as well as any licenses of the code your software depends on or reuses.

Some examples of commonly used software repositories and registries include:

- general-purpose software repositories - [GitHub][github] and [GitLab][gitlab]
- programming language-specific software repositories - [PyPi][pypi] (for Python) and [CRAN][cran] (for R)
- software registries - [BioTools][biotools] (for biosciences) and [Awesome Research Software Registries][awesome-rs-registries], providing a list of research software registries (by country, organisation, domain and programming language) where research software can be registered to help promote its discovery

### Persistent identifiers

Unique persistent identifiers, such as **Digital Object Identifiers** (DOIs) provided by [Zenodo][zenodo], [FigShare][figshare], etc., or **SoftWare Heritage persistent IDentifiers** ([SWHID](swhid)) provided by [Software Heritage][software-heritage], and similar digital archiving services, and commits/tags/releases used by GitHub and similar code sharing platforms, help with findability and accessibility of your software, and can help you get credit for your work by providing citable references.

### Tools for assessing FAIRness of software

Here are some tools that can check your software and provide an assessment of its FAIRness:

- [FAIRsoft evaluator][fair-rs-evaluator]
- [FAIR software test][fair-rs-test]
- [FAIR Software Checklist][fair-rs-checklist] - self-assessment tool developed by the Australian Research Data Commons (ARDC) and the Netherlands eScience Center
- [`How FAIR is your software` - command line tool to evaluate a software repository's compliance with the FAIR principles][howfairis]
- [CODECHECK][codecheck] - An approach for independent execution of computations underlying research articles.

### Summary

The table below provides a summary of how different tools and practices help with the FAIR software principles.

| Tools and practices                                                                                  | Findable | Accessible | Interoperable | Reusable |
|------------------------------------------------------------------------------------------------------|----------|------------|---------------| -------- |
| Virtual development environments                                                                     |          |            |               | x        |
| Integrated development environments (IDEs)                                                           |          |            |               | x        |
| Command line terminals - automated and reproducible pipelines                                        |          |            | x             | x        |
| Standard data exchange formats - e.g. for data exchange (CSV, YAML)                                  |          |            | x             | x        |
| Communication protocols - Command Line Interface (CLI) or Application Programming Interface (API)    |          |            | x             | x        |
| Version control tools                                                                                | x        |            |               |          |
| Code testing & correctness                                                                           |          |            |               | x        |
| Coding conventions                                                                                   |          |            |               | x        |
| Code-level documentation (comments and docstrings, explaining functionality)                         |          |            |               | x        |
| Project-level documentation & metadata (README, explaining functionality/installation/running, etc.) |          |            | x             | x        |
| License - code sharing & reuse                                                                       |          |            |               | x        |
| Citation - code reuse & credit                                                                       |          |            |               | x        |
| Software repositories & registries                                                                   | x        | x          |               |          |
| Unique persistent identifiers                                                                        | x        | x          |               |          |

## Training materials
- The [FAIR Cookbook][fair-cookbook] contains general reusable recipes for FAIR assessment.
- [10 easy things to make your research software FAIR](https://doi.org/10.5281/zenodo.3409968)
- Common metrics for Research Software[^5] that may used to assess each of the FAIR4RS principles.
- [A cookie software project template with FAIR metadata](https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter)
- [Carpentries course on tools and practices for FAIR Research Software](https://carpentries-incubator.github.io/fair-research-software/)

## References
[^1]: Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, Blomberg N, Boiten JW, da Silva Santos LB, Bourne PE, Bouwman J. The FAIR Guiding Principles for scientific data management and stewardship. Scientific data. 2016 Mar 15;3(1):1-9. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)
[^2]: Wilkinson SR, Aloqalaa M, Belhajjame K, Crusoe MR, de Paula Kinoshita B, Gadelha L, Garijo D, Gustafsson OJ, Juty N, Kanwal S, Khan FZ. Applying the FAIR principles to Computational Workflows. Scientific Data. 2025 Feb 24;12(1):328. [https://doi.org/10.1038/s41597-025-04451-9](https://doi.org/10.1038/s41597-025-04451-9)
[^3]: Barker M, Chue Hong NP, Katz DS, Lamprecht AL, Martinez-Ortiz C, Psomopoulos F, Harrow J, Castro LJ, Gruenpeter M, Martinez PA, Honeyman T. Introducing the FAIR Principles for research software. Scientific Data. 2022 Oct 14;9(1):622. [https://doi.org/10.1038/s41597-022-01710-x](https://doi.org/10.1038/s41597-022-01710-x)
[^4]: Chue Hong, N. P., Katz, D. S., Barker, M., Lamprecht, A.-L., Martinez, C., Psomopoulos, F. E., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., Honeyman, T., Struck, A., Lee, A., Loewe, A., van Werkhoven, B., Jones, C., Garijo, D., Plomp, E., Genova, F., … RDA FAIR4RS WG. (2022). FAIR Principles for Research Software (FAIR4RS Principles) (1.0). Zenodo. [https://doi.org/10.15497/RDA00068](https://doi.org/10.15497/RDA00068)
[^5]: Chue Hong, N., Breitmoser, E., Antonioletti, M., Davidson, J., Garijo, D., Gonzalez-Beltran, A., Gruenpeter, M., Huber, R., Jonquet, C., Priddy, M., Shepeherdson, J., Verburg, M., & Wood, C. (2025). D5.2 - Metrics for automated FAIR software assessment in a disciplinary context (1.1). Zenodo. [https://doi.org/10.5281/zenodo.15535629](https://doi.org/10.5281/zenodo.15535629)

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