---
title: FAIR Research Software
---


## FAIR Research Software

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to
increase the visibility and usefulness of your research to others.
The FAIR data principles, first published [in 2016][fair-data-principles], are widely known and applied today.
Similar [FAIR principles for software][fair-principles-research-software] have now been defined too. In general, they mean:

- **Findable** - software and its associated metadata must be easy to discover by humans and machines.
- **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols, free and legally usable.
- **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through
  standardised protocols and application programming interfaces (APIs).
- **Reusable** - software should be usable (can be executed) and reusable
  (can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below.
This is not an exact science, and by all means the list below is not exhaustive,
but any of the practices that you employ in your research software workflow will bring you
closer to the gold standard of a fully reproducible research.

### Findable
- Create a description of your software to make it discoverable by search engines and other search tools
- Place your software in a public software repository (and ideally register it in a [general-purpose or domain-specific software registry][software-registries])
- Use a unique and persistent identifier (DOI) for your software (e.g. by depositing your code on [Zenodo][zenodo]), 
which is also useful for citations - note that depositing your data/code on GitHub and similar software repositories 
may not be enough as they may change their open access model or disappear completely in the future, so archiving your code means it stands a better chance at being preserved 

### Accessible
- Make sure people can freely, legally and easily get a copy your software
- Structure your code using common patterns and use coding conventions to make your code readable and understandable by people (once they obtain a copy of it), and thereby more accessible 

### Interoperable
- Explain the functionality of your software and protocols for interaction with it
- Use standard formats for inputs and outputs
- Communicate with other software and tools via standard protocols and APIs

### Reusable
- Document your software (including its functionality, and how to install and run it) to make it more understainable by others who may wish to reuse or extend it
- Follow best practices for software development (including structuring your code in reusable functions with a single functionality
that can be built on top of, coding conventions, code readability and verifying its correctness)
- Test your software and make sure it works on different platforms/operating systems to make it more reusable
- Give a licence to your software clearly stating how it can be reused
- State how to cite your software so people can give you credit when they reuse it
   
## Tools and practices for FAIR research software development 

There are various tools and practices that support the development of FAIR research software, contributing to each of the four FAIR principles. 
These tools and practices work together, as no single tool or practice will fully addresses one principle but can 
contribute to multiple principles simultaneously. 

It is important to note that simply using these tools, without following good practice and guidance on how best to align 
their usage with the FAIR principles, is not enough to produce FAIR software. 
In addition, FAIR is not a [software quality metric](https://everse.software/RSQKit/rs_quality) even though it can improve software quality in several aspects - 
software may be FAIR but still not very good in terms of its functionality.

### Development environments

Virtual and integrated development environments (IDEs), such as VS Code or PyCharm, help with running, testing, and debuging code. 
Virtual environments further enable us to share our working environments with others, making it easier to access, reuse and extend our code.
IDEs often provide integrations with other tools, e.g. version control and command line terminals, enabling you to do many tasks from a single environment, 
saving time in switching between different tools.

### Command line terminals

Command line terminals (e.g. Bash, GitBash) enable us to run and test our code without graphical user interfaces (GUI) afforded to us by IDEs - 
this is sometimes needed for accessing and running our code remotely on servers and high-performance systems without a GUI provision, where time, 
memory and processing power are expensive or in high demand.

Version control systems are typically provided as command line tools making them often only accessible from command line terminals to enter commands and access 
remote version control servers to backing up and sharing our work.

Finally, command line tools are interoperable software that use standard protocols for passing parameters, inputs and outputs via the command line terminal. 
This makes it easier to integrate with other tools, allowing us to chain command line tools and build up complex and reproducible workflows and analysis pipelines 
using several programs in different steps. 
If we write our software in a way which provides such an interoperable command line interface - we will be able to integrate it with other command line tools to 
automate and speed up our work.

### Standard input/output formats and communication protocols

Using standard data exchange, input and output formats and communication protocols helps create interoperable software that can more readily integrate 
with other tools into more complex pipelines - increasing its interoprability and reusability. 

### Version control tools

Version control means knowing what changes were made to your code, when and by who - promoting code ownership, responsibility and credit. 
When combined with software sharing and collaborative platforms such as GitHub or GitLab, it facilitates code publication, sharing and findability, 
teamwork and discussions around software and design decisions, provides backup facilities for your code and speeds up 
collabortion on shared code by allowing edits by more than one person at a time.

### Code testing

Testing ensures that your code is correct and does what it is set out to do. 
When you write code you often feel very confident that it is perfect, but when writing bigger codes or code that is meant to do complex operations 
it is very hard to consider all possible edge cases or notice every single typing mistake. 
Testing also gives other people confidence in your code as they can see an example of how it is meant to run and be assured that it does work 
correctly on their machine - helping with code understading and reusability.

### Coding conventions

Following coding conventions and guides for your programming language that is agreed upon by the community and other programmers
are important practices to ensure that others find easy to read your code, reuse or extend it in their own examples and applications.

### Software- and project- level documentation

Documentation comes in many forms - from **software-level documentation** including decriptive names of variables and functions and 
additional comments that explain lines of your code, to **project-level documentation** (including README, LICENCE, CITATION, CONTRIBUTING, etc. files) 
that help to discover it, explain the legal terms of reusing it, describe its functionalty and how to install, run and contribute to it, 
to whole websites full of documentation with function definitions, usage examples, tutorials and guides. 
You many not need as much documentation as a large commercial software product, but making your code reusable relies on other people being able to understand 
what your code does and how to use it.

### Software repositories and registries

Having somewhere to share your code is fundamental to making it findable and accessible. 
Your institution might have a code repository, your research field may have a practice of sharing code via a specific website, archive or journal,
or your version control system might include an online component that makes sharing different versions of your code easy. 
You should check the rules or guidelines of your institution, grant or domain on publishing code, as well as any licenses of the code your software depends on or reuses.

Some examples of commonly used software repositoris and registries include:

- general-purporse software repositories - [GitHub][github] and [GitLab][gitlab]
- programming language-specific software repositories - [PyPi][pypi] (for Python) and [CRAN][cran] (for R)
- software registries  - [BioTools][biotools] (for biosciences) and [Awesome Research Software Registries][awesome-rs-registries], providing a list of research software registries (by country, organisation, domain and programming language) where research software can be registered to help promote its discovery

### Persistent identifiers

Unique persistent identifiers, such as Digital Object Identifiers (DOIs) provided by Zenodo, FigShare and similar digital archiving services, and commits/tags/releases used by GitHub and similar code sharing platforms, 
help with findability and accessibility of your software, and can help you get credit for your work by providing citeable references.

The table below provides a summary of how different tools and practices help with the FAIR software principles.

| Tools and practices                                                                                  | Findable | Accessible | Interoperable | Reusable |
| ---------------------------------------------------------------------------------------------------- | -------- | ---------- | ------------- | -------- |
| Virtual development environments                                                                     |          | x          |               | x        |
| Integrated development environments/IDEs                                                             |          |            |               | x        |
| Command line terminals - automated and reproducible pipelines                                        |          |            | x             | x        |
| Standard formats - e.g. for data exchange (CSV, YAML)                                                |          | x          | x             | x        |
| Communication protocols - Command Line Interface (CLI) or Application Programming Interface (API)    |          | x          | x             | x        |
| Version control tools                                                                                | x        |            |               |          |
| Testing - code correctness and reproducibility                                                       |          | x          |               | x        |
| Coding conventions                                                                                   |          | x          | x             | x        |
| Software-level documentation (comments and docstrings, explaining functionality)                     |          | x          | x             | x        |
| Project-level documentation (READMEs, explaining functionality/installation/running)                 |          | x          | x             | x        |
| License - code sharing and reuse                                                                     |          | x          |               | x        |
| Citation - code reuse and credit                                                                     | x        |            |               | x        |
| Software repositories and registries                                                                 | x        | x          |               |          |
| Unique persistent identifiers                                                                        | x        | x          |               |          |



TODO: cross link with other pages talking about specific tools or practices, e.g. version control, code readability, documentation, etc.


[fair-principles-research-software]: https://www.nature.com/articles/s41597-022-01710-x
[fair-data-principles]: https://www.nature.com/articles/sdata201618
[zenodo]: https://zenodo.org/
[software-registries]: https://github.com/NLeSC/awesome-research-software-registries
[github]: https://github.com
[biotools]: https://biotools.us/
[pypi]: https://pypi.org/
[cran]: https://cran.r-project.org/web/packages/
[gitlab]: https://about.gitlab.com/
[awesome-rs-registries]: https://github.com/NLeSC/awesome-research-software-registries
