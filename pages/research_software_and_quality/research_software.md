---
title: What is Research Software?
description: Research software and how it distinguishes from general software used in research
contributors: ["Shoaib Sufi", "Daniel Garijo", "Aleksandra Nenadic", "Laura Portell-Silva"]
coordinators: ["Shoaib Sufi"]
---

There are various definitions of research software.
The following two definitions are borrowed from [*"Defining Research Software: a controversial discussion"*][defining-rs] - the most recent and expansive discussion on what research software is, which was done under the auspices of the [FAIR4RS RDA working group][fair4rs-wg].

### Inclusive definition of research software

- *All code and software artefacts that are used, produced, or might be related to the research process in one or more stages of the research lifecycle and regardless of the layer of the software stack.*
- *Software that was not necessarily developed with the intention of being part of research, for example, a library for interfacing with a sensor, or software that ceased to be exclusive to the research domain, for example, certain programming languages developed in research projects, e.g., Python, Scala, R.*

### Exclusive definition of research software

- *Well identified software that is part of the research discovery process, which might require specialised domain knowledge and is by itself a contribution to science and research.*
- *Software that was developed with the intention of being part of research.*

The above two definitions offer two ends of a spectrum of what research software is.
For some, the inclusive definition would be more correctly termed **software in research** whereas the exclusive definition would be termed **research software**.

Following this line of thought - not all software that is used in research is **research software**.
Research software is software or code that is used to generate, process or analyse results of a research for publication.
For example, software used to guide a telescope that is used to conduct scientific research is not considered research software.
On the other hand, formulas or macros in spreadsheets used to analyse data are considered **research code** as they are a form of computer programming that allow one to create, calculate, and change data sets in a number of different ways.

This spectrum is only one way of viewing research software, and it is not the view the RSQKit leans on most heavily.
In practice the RSQKit organises its guidance around several complementary views: the [three-tier model](three_tier_view) of analysis code, prototype tools and research software infrastructure; the [software lifecycle](life_cycle); the [research clusters and infrastructures](../research_clusters_or_infrastructures) in which software is developed; the [roles](../roles) of the people who build and use it; and the [quality dimensions](quality_dimensions) and [indicators](../all_indicators) against which quality is assessed.
The inclusive and exclusive definitions above orient the reader in the debate; these views are how the RSQKit approaches research software quality in practice.

The RSQKit does not mandate the definition of what research software is, however its authors and the [Editorial Board](./editorial_board) may be opinionated on what they believe the definition is and this may vary over time and be reflected in the RSQKit pages.
Since the focus of the RSQKit is to highlight quality practice, most of the advice (especially around [computational tasks](../tasks)) could be applied to software in research.
However, many of the best practices are found in research software and we hope the RSQKit helps promote the practices to other areas of research and allows cross-pollination of ideas and practice.


[defining-rs]: https://doi.org/10.5281/zenodo.5504016

[fair4rs-wg]: https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg/
