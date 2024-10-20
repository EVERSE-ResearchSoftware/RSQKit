---
title: Research Software lifecycle
---

## The Research Software Lifecycle

![The Research Software Lifecycle](/images/lifecycle.png)

The research software lifecycle, shown in the figure above, provides a model for understanding the different phases encountered duing the development of research software. 
This lifecycle was developed as part of The EOSC Task Force [Infrastructure for quality research software](https://eosc.eu/advisory-groups/infrastructures-quality-research-software/) and described in detail in [this](https://doi.org/10.5281/zenodo.8324828) document. 

There is a close link between the this software lifecycle and the [Three tiers model](http://everse.software/RSQKit/three_tier_view). Depending on the tier of software,  the length of the lifecycle, or number of iterations through the lifecycle may vary. 

**Analysis Code (Tier 1 software)** typically represent software created for personal use and with a small scope, such as analysis scripts. The development of such software is directly driven 
by a research question, and requires only little planning and software engineering effort as well as limited documentation and testing. Once the software is finished, and the research question 
answered, it is important to publish the software together with the related research outputs, such as papers, datasets, workflows, etc. After this publication, the cycle ends and the software 
is not developed further nor maintained.

**Prototype tools (Tier 2 software)** represent tools designed to answer multiple research questions, often developed and used by more than one person. The developers and users of the 
software are typically part of the same research team or organisation, although the size and composition of the team may vary over time. There is a close connection between the research and software 
development cycles. Due to the broader scope and longer lifetime of the software, more extensive planning of development is needed to ensure the software cycle matches the research cycle.
In addition, the application of more advanced software engineering practices (e.g., issue tracking, semantic versioning, test coverage, code style and quality checkers, code reviews, etc.) is needed
to enable the software to be efficiently developed by a (potentially changing) team and to allow user feedback to be recorded. To ensure reproducibility of results, versioned releases should 
be archived, and properly cited in papers. After publication, the development cycle continues to answer further research questions and apply improvements to the existing code.

**Research Software Infrastructure (Tier 3 software)** represents broadly applicable research software. For this software Tier, the software and research cycles are no longer directly connected. The 
development team may be large and possibly distributed over multiple organisations. Different team members may have have different objectives and represent different communities. There may be a large 
group of external users who depend on the software without directly contributing to the development. Proper development planning and community management should be used to organise the team members, 
collect user feedback, and ensure a regular release cycle. This Tier requires the most advance software engineering techniques to ensure a smooth development process, quality, and long term 
maintainability. For online services or mission critical software that require continuous operation, special software engineering method such as DevOps and CI/CD are needed. To ensure the long term 
sustainability of the software, governance model and funding or business model are required.

## Context and History

The research software lifecycle description shown above was originally developed in the context of the EOSC Task Force [Infrastructure for quality research software](https://eosc.eu/advisory-groups/infrastructures-quality-research-software/). 
As part of the EOSC Task Force, it was important to achieve a common understanding on the processes in research software engineering to asses the infrastructure needs. 
Therefore, the Task Force split into various subgroups investigating different aspects of research software engineering. 
SubGroup 1 of this task force took al closer look at the research software lifecycle, and reported its findings in the deliverable [Research Software Lifecycle](https://doi.org/10.5281/zenodo.8324828). 
The aim of this document was to illustrate the lifecycle of research software and how its instantiations for particular software projects are influenced by varying developer groups and their intentions. 

## References

- [Research Software Lifecycle](https://doi.org/10.5281/zenodo.8324828)
- [Infrastructure for quality research software](https://eosc.eu/advisory-groups/infrastructures-quality-research-software/)
