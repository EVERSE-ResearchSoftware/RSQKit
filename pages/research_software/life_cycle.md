---
title: Research Software Lifecycle
---

![The Research Software Lifecycle](../../images/lifecycle.png)

The research software lifecycle as shown in the diagram above provides a model for understanding the different phases 
encountered during the development of research software. 

There is a close link between this software lifecycle and the [three-tier model of software](/three_tier_view). 
Depending on its tier, the software lifecycle length or the number of iterations through the lifecycle may vary. 

For example, the development of analysis code (tier 1 software) is directly driven
by a research question, and involves little planning and software engineering effort with limited documentation and testing. 
Once the software is finished and the research question answered, it is important to publish the software together with 
the related research outputs, such as papers, datasets, workflows, etc. After this publication, the cycle ends and the software
is not developed further nor maintained.

Prototype tools (tier 2 software) are typically designed to answer multiple research questions (so "Research Question" from the diagram 
becomes "Research Purpose"), and are often developed and used by more than one person. The developers and users of the
software are typically part of the same research team or organisation, although the size and composition of the team may vary over time. 
There is a close connection between the research and software development parts of the cycle. 
Due to the broader scope and longer lifetime of the software, more extensive planning of development is needed to ensure 
the software cycle matches the research cycle. In addition, the application of more advanced software engineering practices 
(e.g., issue tracking, semantic versioning, test coverage, code style and quality checkers, code reviews, etc.) is needed
to enable the software to be efficiently developed by a (potentially changing) team and to allow user feedback to be recorded. 
To ensure reproducibility of results, versioned releases should
be archived, and properly cited in papers. 
After publication, the development cycle continues to answer further research questions and apply improvements and bug fixes to the existing code.

Research software infrastructure (tier 3 software) represents broadly applicable research software. For such software,
the software and research lifecycles are no longer directly connected.
The development team may be large and possibly distributed over multiple organisations.
Different team members may have have different objectives and represent different communities.
There may be a large
group of external users who depend on the software without directly contributing to the development.
Proper development planning and community management should be used to organise the team members,
collect user feedback, and ensure a regular release cycle.
This tier requires the most advanced software engineering techniques to ensure a smooth development process, quality, and long term
maintainability. For online services or mission critical software that require continuous operation, special software engineering methods such as DevOps and CI/CD are needed. 
To ensure the long term sustainability of the software, governance model and funding or business model are required.

### Context and History

The research software lifecycle description used here was originally developed by the [Infrastructures for Quality Research Software](https://eosc.eu/advisory-groups/infrastructures-quality-research-software/)
EOSC Task Force. This Task Force tried to achieve a common understanding on the processes in research software engineering to asses the research infrastructure needs. 
For this reason, the Task Force split into various subgroups investigating different aspects of the research software engineering process. 
SubGroup 1 of the Task Force took a closer look at the research software lifecycle, and reported its findings in the deliverable [Research Software Lifecycle](https://doi.org/10.5281/zenodo.8324828). 
The aim of this document was to illustrate the lifecycle of research software and how its instantiations for particular software projects are influenced by varying developer groups and their intentions. 

## Lifecycle Stages

TODO

Add a bit of explanation about each stage and provide links to task pages.
