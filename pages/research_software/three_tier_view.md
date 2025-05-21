---
title: Three-Tier Model of Research Software
---

The **three-tier model of research software** provides a framework for understanding the diverse landscape of software 
in research - from scripts, code, notebooks, to computational workflows, libraries, modules, frameworks, utilities and applications. 
This model distinguishes three tiers of research software, focussing on what they get built for:

- **Analysis code** - research software that captures computational research processes and methodology, often used in simulation, 
data generation, preparation, analysis and visualisation. It typically represents software created for personal use with a small scope, such as analysis scripts. 
- **Prototype tools** - research software that demonstrates a new idea, method or model for use beyond the project in which it originated,
  often as a substantive intellectual contribution or a proof of concept.
  These software tools are designed to answer multiple research questions and are typically developed and used by more than one person.
- **Research software infrastructure** - software that captures broadly accepted ideas, methods and models for use in research,
  warranting close researcher involvement in their development.
  This tier represents a broadly applicable research software, often with a large and possibly distributed development team.

<img src="../../images/3-tier-model.svg" width="1200" alt-text="Three-tier model of research software" />

*Diagram adapted from ["EVERSE Paving the way towards a European Virtual Institute for Research Software Excellence" presentation](https://indico.cern.ch/event/1501988/contributions/6323204/attachments/3016679/5320601/EVERSE_Overview_Slides.pdf) by F. Psomopoulos, February 2025*

For example, [Nipype](https://nipype.readthedocs.io/en/latest/), a Python tool for neuroimaging data processing, began as a collection of analysis scripts before evolving into a more comprehensive tool.
[GROMACS](https://www.gromacs.org/), a software suite for high-performance molecular dynamics and output analysis, is another good example of a prototype tool
that has become widely used in its field.
[NumPy](https://doi.org/10.1038/s41586-020-2649-2), a fundamental package for scientific computing in Python, exemplifies the research software infrastructure tier,
providing essential numerical computing capabilities used across many scientific domains, and is uses as a basis for more new and up-and-coming 
analysis code and prototype tools build by [researchers who code](/researcher_who_codes) and [Research Software Engineers](/research_software_engineer).

The three-tier model acknowledges a relationship between the tiers: software at higher tiers builds on the existence and stability of software in lower tiers,
while the existence of higher-tier software reinforces the value of lower-tier software.
This interconnectedness highlights the importance of supporting all levels of research software development.

## Context and History

The three-tier model originated from the Australian Research Data Commons (ARDC) as part of their ["National Agenda for Research Software"](https://doi.org/10.5281/zenodo.6378082) 
and was also inspired by discussions around ["Dealing With Software Collapse"](https://ieeexplore.ieee.org/document/8701540). 
It emerged from the need to better categorise and support different types of research software, recognising that a 
one-size-fits-all approach is inadequate for the varied purposes and stakeholders involved in research software - “best practice” in the production of
analysis code, prototype tools and research software infrastructure could mean quite different things.

Since its introduction, the model has gained international recognition. 
It has been referenced in various contexts, including the ["FAIR Principles for Research Software (FAIR4RS Principles)"](https://doi.org/10.1038/s41597-022-01710-x). 
Similar tiered approaches have been adopted by other organisations, such as the German Aerospace Center (DLR) in their ["Software Engineering Guidelines"](https://doi.org/10.5281/zenodo.1344612).

The three-tier model aligns with a broader vision of recognising research software as a first-class output of research. 
It provides a framework for addressing specific challenges at each tier, from increasing transparency in analysis code 
to enabling broad impact through quality prototype tools and ensuring sustained support for research software infrastructure.

For initiatives like [EVERSE](https://everse.software/), the three-tier model offers a valuable lens through which to view research software quality 
and excellence. It suggests that practices, tools, and assessment criteria may need to be adjusted based on the tier of 
software being considered, contributing to a more comprehensive framework for research software quality that can be applied across diverse research contexts.
The essence of the three-tier model is that software in different tiers has distinct purposes, stakeholders, and needs.
This nuanced approach allows for more appropriate development, management, and assessment strategies tailored to each tier.

The three-tier of research software aligns closely with practical Software Management Plan (SMP) frameworks. 
As outlined in the ["Practical Guide to Software Management Plans"](https://doi.org/10.5281/zenodo.7248877), SMPs can be tailored to low, medium, and high 
management levels, corresponding to analysis code, prototype tools, and research software infrastructure respectively. 
This alignment demonstrates how the three-tier model can guide the development of appropriate management practices for 
different types of research software, ensuring that software management efforts are appropriately scaled to the nature 
and intended use of the software. By mapping specific SMP requirements to each tier, researchers and institutions can 
enhance the quality and sustainability of research software across all levels of complexity and scope.