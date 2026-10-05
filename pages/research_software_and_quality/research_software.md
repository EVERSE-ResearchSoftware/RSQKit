---
title: What is Research Software?
description: Research software and how it distinguishes from general software used in research
contributors: ["Shoaib Sufi", "Daniel Garijo", "Aleksandra Nenadic", "Laura Portell-Silva"]
coordinators: ["Shoaib Sufi"]
---

There are various definitions of research software, and the field has not settled on one.
The two definitions below are borrowed from [*"Defining Research Software: a controversial discussion"*][defining-rs] - the most expansive discussion of the question, carried out under the auspices of the [FAIR4RS RDA working group][fair4rs-wg].
That report set out to agree a single concise definition and deliberately stopped short of one, offering a spectrum with two ends instead.

### Inclusive definition of research software

- *All code and software artefacts that are used, produced, or might be related to the research process in one or more stages of the research lifecycle and regardless of the layer of the software stack.*
- *Software that was not necessarily developed with the intention of being part of research, for example, a library for interfacing with a sensor, or software that ceased to be exclusive to the research domain, for example, certain programming languages developed in research projects, e.g., Python, Scala, R.*

### Exclusive definition of research software

- *Well identified software that is part of the research discovery process, which might require specialised domain knowledge and is by itself a contribution to science and research.*
- *Software that was developed with the intention of being part of research.*

The two definitions mark the ends of a spectrum rather than rival answers.
The inclusive definition sits closer to a *usage* point of view and the exclusive one closer to a *creation* point of view, and the report leaves each discipline to decide where along that spectrum its own threshold falls.
For some, the inclusive definition would be more correctly termed **software in research** whereas the exclusive definition would be termed **research software**.

### Where the layer of the software stack comes in

The inclusive definition's phrase *"regardless of the layer of the software stack"* refers to [Hinsen's six-layer stack][hinsen], which runs from software written by scientists for a specific project (scripts, notebooks, workflows), through domain-specific research software, scientific computing infrastructure and general-purpose infrastructure such as compilers and editors, down to the operating system and the hardware.
Hinsen devised it to explain how research results become irreproducible when the layers beneath them shift - what he calls software collapse.
It is useful here because it reframes the question: rather than asking whether a given piece of software is research software, it asks at which layer of the stack a community draws its threshold.

### Research software and software in research

The distinction between these two terms is codified by the [FAIR4RS principles][fair4rs-principles], which treat research software as *"source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose"*, and classify software components used for research but not created with a clear research intent - operating systems, libraries, dependencies, packages - as software in research instead.
On that reading, not all software used in research is research software.

Boundary cases remain genuinely contested rather than settled.
Software that guides a telescope used for scientific research is read by some as instrument control and so outside the definition, while [van Nieuwpoort and Katz's account of the roles of research software][roles-of-rs] treats exactly this case as research software in its own right, under the role *component of instruments*.
Formulas or macros in spreadsheets used to analyse data are generally considered **research code**, as they are a form of computer programming that allows one to create, calculate, and change data sets in a number of different ways.

### What the different views agree on

The views above disagree less than their variety suggests.
The artefacts in scope are stable across all of them: source code, scripts, notebooks, computational workflows, libraries and executables, together with the documentation and parameters needed to use them.
What makes software *research* software is its relationship to research, not any technical property of the software itself.
They divide on a single axis - whether that relationship is established by the intent with which the software was created, or by the use to which it is put.

The inclusive/exclusive spectrum is only one way of viewing research software, and it is not the view the RSQKit leans on most heavily.
In practice the RSQKit organises its guidance around several complementary views: the [three-tier model](three_tier_view) of analysis code, prototype tools and research software infrastructure; the [software lifecycle](life_cycle); the [research clusters and infrastructures](../research_clusters_or_infrastructures) in which software is developed; the [roles](../roles) of the people who build and use it; and the [quality dimensions](quality_dimensions) and [indicators](../all_indicators) against which quality is assessed.
The inclusive and exclusive definitions above orient the reader in the debate; these views are how the RSQKit approaches research software quality in practice.

The RSQKit does not mandate the definition of what research software is, however its authors and the [Editorial Board](./editorial_board) may be opinionated on what they believe the definition is and this may vary over time and be reflected in the RSQKit pages.
Since the focus of the RSQKit is to highlight quality practice, most of the advice (especially around [computational tasks](../tasks)) could be applied to software in research.
However, many of the best practices are found in research software and we hope the RSQKit helps promote the practices to other areas of research and allows cross-pollination of ideas and practice.


[defining-rs]: https://doi.org/10.5281/zenodo.5504016

[fair4rs-wg]: https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg/

[fair4rs-principles]: https://doi.org/10.1038/s41597-022-01710-x

[hinsen]: https://doi.org/10.1109/MCSE.2019.2900945

[roles-of-rs]: https://upstream.force11.org/defining-the-roles-of-research-software-2/
