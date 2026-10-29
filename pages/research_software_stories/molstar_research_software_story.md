---
title: "Mol* Viewer - web-native 3D visualization and analysis tool not only for large biomolecular structures" # short title
search_exclude: false # set to false if you want this page to show up in search results (it's 'true for the template as we don't want that in search results)
description: "Mol* Viewer is an open-source, web-native 3D visualization and analysis tool for large biomolecular structures, molecular dynamics trajectories, experimental density data, and structural biology annotations." # a description of the page - A brief description of the exemplar or use case and which problem it solves and which domains (or if its cross domain) it applies to. 
contributors:  ["Radka Svobodová", "Karel Berka", "David Sehnal"] # a comma separated list of contributors' names, as found in _data/CONTRIBUTORS.yml (add yourself to the files if you do not have an entry)
page_id: molstar_viewer # unique page id, ideally lowercase words separated by underscore(s) - for example page_id of 'Galaxy' could be galaxy
affiliations: ["LS-RI", "ELIXIR"] # a comma separated list of affiliation names, as found in _data/affiliations.yml
---

<!-- 
Please keep all sections and fill them in.
If this is not possible for any reason - you may remove sections (you will need to explain to the Editorial Board in your pull request why certain sections are not present).
The text describing what is needed in the sections can be removed.
Once you have completed your research community entry - please add it to _data/sidebars/main.yml under the Research Software Stories entry in alphabetical order.
All markdown and page metadata comment sections can be removed before you submit a pull request.
-->

## The Problem
### Scalable browser-based access to complex biomolecular structures

<!--
**What scientific or practical problem does the software solve?**
**Questions:**
- What was difficult, fragile, slow, or unreliable before this software existed?
- What scientific question or workflow needed improvement?
- Why was existing tooling not enough?
- What assumptions sit behind the problem?
- What boundaries or limitations define the scope?
*Write 2-3 full sentences first, then add bullets if helpful.*
-->
Modern structural biology generates massive, complex datasets—from atomic models to mesoscale cell structures—that traditional web tools struggled to visualize efficiently. Mol Viewer* solves this by delivering fast, extensible, browser-based 3D visualization without requiring local software installation.

Key Capabilities
- High-Performance Rendering: Smoothly visualizes very large structures and multi-protein assemblies in the browser.
- Efficient Streaming: Streams coordinate and experimental data quickly over limited bandwidth.
- Integrated Annotations: Displays structural, functional, validation, and biological-context data simultaneously.
- Multi-Scale Support: Handles static structures, dynamic trajectories, density maps, and mesoscale models.
- Ecosystem Integration: Powers public data resources and third-party web services seamlessly.

## User Community
### Structural biology, bioinformatics, education, and molecular design users

Developed by an international team—with backing from RCSB PDB and PDBe—Mol Viewer* serves thousands of daily users worldwide. It is the primary 3D visualization tool for major global databases, including the [PDBe](https://www.ebi.ac.uk/pdbe/), [RCSB PDB](https://www.rcsb.org/), [PDBe-KB](https://www.ebi.ac.uk/pdbe/pdbe-kb/), [PDB-IHM](https://pdb-ihm.org/), [EMDataResource](https://www.emdataresource.org/), [PED](https://proteinensemble.org/), [MobiDB](https://mobidb.org/), and [HARP](https://harp-leprosy.org/).

Key Community & Roles
- Core Developers & Maintainers: Contributors from PDBe, RCSB PDB, Masaryk University, UC San Diego, Rutgers, and partner institutions.
- Scientific Users: Structural biologists, bioinformaticians, and modelers analyzing structures, simulations, and maps.
- Database & Web Teams: Developers embedding Mol* into scientific portals and web services.
- Educators & Communicators: Teachers and outreach creators building interactive learning materials.
<!--

- Describe how the development is organised (e.g. is it one person, many, how are they organised and/or governed)
- Who are the users - how experienced are they in using your software?

**Who builds the software and who uses it?**

**Questions:**

- Who are the developers and contributors?
- Who relies on the software in their research?
- What roles or expertise are involved?
- How do these groups interact?
- Are there gaps, risks, or single points of failure?

*2-3 full sentences, then optional bullets.*

-->

## Technical Aspects
Mol* Viewer is a web-native molecular graphics application and part of the broader Mol* open-source project. It can be understood as research software infrastructure: it is not only a single viewer, but also a modular library and set of tools for data storage, in-memory molecular representation, query language support, UI state management, visualisation, and efficient data access.

The viewer is implemented with TypeScript, WebGL, React, and open web-platform standards. WebGL provides hardware-accelerated 3D rendering, while React is used for the user interface. The surrounding JavaScript ecosystem, including Node.js, NPM, TypeScript, and GitHub, supports modular development and reuse.

Mol* Viewer is designed around demanding structural-biology constraints: large coordinate files, volume data, density maps, multi-scale models, molecular dynamics trajectories, and the need for responsive interaction in a browser. Built-in BinaryCIF support, decompression, and model/volume streaming allow large structures to remain interactively renderable even over limited bandwidth. The paper demonstrates browser-based rendering of a cellPACK model of an enveloped HIV capsid in blood serum containing 67,870,140 atoms, and the visual examples on page 3 show how rendering modes improve perception of structural detail.

Technical capabilities include:
- Advanced Rendering: Supports cartoons, surfaces, volumes, electron-density/Cryo-EM maps, and glycan 3D-SNFG symbols.
- Analysis & Navigation: Features sequence navigation, structural alignment, superposition, and distance/angle measurements.
- Dynamic Data: Handles molecular dynamics trajectory playback, animation export, and multi-scale models.
- Integration & Export: Offers screenshot export, reloadable session states, and seamless embedding into third-party web applications.
<!--

**What is the software, technically?**

**Questions:**

- What type of software is it (e.g. analysis tool, prototype tools, workflow, service, registry …)?
- What tier of software is it (analysis code, prototype tools, research software infrastructure - see https://everse.software/RSQKit/three_tier_view)
- Which languages, frameworks, or technologies does it use?
- How large or complex is the codebase? (e.g. size, complexity, activity, when did development start)
- What constraints shape it? (data size, performance, domain-specific rules)

*Begin with full sentences.*

-->

### Libraries and Systems
Mol* Viewer depends on the modern web ecosystem and on structural-biology data systems. It integrates with RCSB PDB and PDBe data services, PDBe MX and 3DEM density servers, wwPDB validation reports, RCSB PDB assembly-symmetry annotations, and other databases that embed the viewer.

The software must understand both general web-development technologies and domain-specific molecular data formats. Contributors need familiarity with web graphics, TypeScript, state management, structural biology concepts, and the coordinate, volume, and trajectory formats used by molecular science communities.

Supported or referenced formats and systems include:
- Structure formats: PDBx/mmCIF, BinaryCIF, PDB, PDBQT, GRO, SDF, MOL, MOL2, CIF-core.
- Volume and density formats: CCP4, MRC, MAP, DSN6, BRIX, CUBE, DX, BinaryCIF.
- Trajectory and topology formats: XTC, DCD, PSF.
- Geometry formats: PLY for generic triangle geometries, such as coloured surfaces from external tools.
- Annotation and data systems: SCOP, Pfam, UniProt, wwPDB validation reports, RCSB PDB assembly symmetry, PDBe, RCSB PDB, PDB-Dev, EMDataResource, PDBe-KB, PED, MobiDB, and HARP.


<!--
**What major libraries, systems, or ecosystems does the software depend on?**

**Questions:**

- What scientific libraries, frameworks, or APIs does it rely on?
- Which external systems does it integrate with?
- What data formats or domain tools must it support?
- What does someone need to know before contributing?

*Write 2-3 clear sentences before listing items.*

-->

## Software Practices
### Open-source collaborative development for reusable molecular graphics
Mol* Viewer is developed as an open-source project hosted on GitHub. The article describes its development as an international collaboration, supported by PDBe and RCSB PDB, and as a continuation of expertise and code from LiteMol, NGL Viewer, PatternQuery, MMTF, and BinaryCIF.

The paper does not describe all day-to-day engineering practices, such as pull-request review rules, test coverage, release cadence, or continuous integration setup. However, it does identify several visible practices that support reuse and collaboration: public source code, permissive licensing, modular architecture, integration with production scientific services, and collaboration across institutional partners.

Benefits for the user community include:
- a shared web-based viewer across major structural biology resources;
- reusable components for third-party scientific applications;
- common infrastructure for data access, visualisation, annotations, and state management;
- easier adoption because the viewer runs in the browser and can be embedded in external services;
- stronger long-term prospects through collaboration between PDBe, RCSB PDB, and the wider structural-biology ecosystem.

<!--

**What practices guide development and collaboration?**

**Questions:**

- How do you use version control?
- Is there code review? Testing? Release processes?
- How are decisions made?
- How do people communicate about changes?
- What's informal but still important?
- What have the benefits been of using these practices?

*First: 2-3 sentences capturing reality as it is.*

-->

## Developer Community
### From web viewer usage to embedded scientific services
A typical user can start by opening structures at the Mol* web page or through integrated viewers in PDBe and RCSB PDB. Developers can adopt Mol* Viewer by embedding it into scientific web applications or by using the source code available through the Mol* GitHub organisation.

The on-ramp for new developers is shaped by both web engineering and structural biology. A contributor may begin by using examples on the Mol* website, exploring the interactive demonstrations described in the paper, reading the source code, or integrating the viewer into an existing web resource. New contributors benefit from knowledge of TypeScript, WebGL-based rendering, React UI development, and common macromolecular data formats.

Likely newcomer paths include:
- using Mol* Viewer as an end user through the public web interface;
- embedding Mol* Viewer in an institutional database or analysis service;
- extending support for additional file formats or annotations;
- improving rendering, interaction, UI, documentation, or data-loading workflows;
- building educational or analysis workflows that rely on Mol* scenes, screenshots, or animations.

Potential obstacles include the size and complexity of molecular data, the need to understand domain-specific formats, and the performance expectations of interactive 3D graphics in the browser.

<!--

**How do new users and developers start using or contributing to the software?**

**Questions:**

- What is a typical user (developer) journey?
- What do new contributors usually do first?
- What examples, notebooks, wikis, or tutorials exist?
- How do people learn the workflow?
- What obstacles do newcomers face?

*Write full sentences about the “on-ramp”, then add bullets.*

-->

## Tools
### Web, graphics, data-streaming, and molecular-format tooling
Mol* Viewer relies on tools and technologies from both web software engineering and structural biology. The paper specifically names TypeScript, WebGL, React, Node.js, NPM, GitHub, BinaryCIF, and CIFTools as important parts of the project’s implementation and ecosystem.

Tools and resources that support development and operation include:
- TypeScript: main implementation language for the web application.
- WebGL: hardware-accelerated 3D rendering in the browser.
- React: user-interface framework.
- Node.js and NPM: JavaScript runtime and package ecosystem for modular web development.
- GitHub: public hosting and collaboration platform for the open-source code.
- BinaryCIF and CIFTools: efficient macromolecular data management and transmission.
- RCSB PDB and PDBe data services: production data sources and embedding environments.
- Density servers and validation reports: data sources for volume rendering and structure-quality annotations.

The article does not specify particular linters, formatters, CI systems, or test runners. These should be checked in the current GitHub repository before adding operational details to a production story page.


<!--

**Questions:**

- What linters, formatters, CI systems, test runners, or similar are used?
- How do you containerise or package the environment?
- What workflow or documentation tools help keep things stable?
- Which of these tools make daily development easier?

*Begin with sentences; bullets optional.*

Note: if any tools mentioned don’t exist in https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/tool_and_resource_list.yml consider adding them

-->

## FAIR & Open
### Open-source software using standard structural biology formats
Mol* Viewer aligns strongly with open and FAIR research software practices. It is freely available at the Mol* website, its source code is public on GitHub, and it is released under the permissive MIT licence to support code sharing, reuse, and collaboration.

The software supports interoperability through widely used molecular and structural-biology formats, including PDBx/mmCIF, BinaryCIF, PDB, CCP4/MRC/MAP, XTC, DCD, and others. It is reusable as a standalone web application and as an embeddable component in third-party scientific services, which supports adoption across databases, analysis platforms, and educational resources.

FAIR and open aspects include:
- public project website and source-code repository;
- permissive MIT licence;
- support for standard molecular coordinate, volume, trajectory, and geometry formats;
- integration with public structural-biology archives and annotation resources;
- browser-based access without requiring local installation;
- reuse through embedding in other web applications.


<!--

**How does your software align with FAIR principles and open practices?** *2-3 sentences*

**Questions:**

- Is the code publicly findable? How?
- What licence do you use?
- How can others access the software and its documentation?
- What formats or standards promote interoperability?
- How can others reuse or build on your work?
- How open is the development process?

Note: to understand more about FAIR see - https://everse.software/RSQKit/fair_rs

-->

## Documentation
### Documentation and examples help users explore structures without installing software
The main entry point for users is the Mol* website, which provides access to the viewer and examples. The source code is available through the Mol* GitHub organisation, and the paper describes practical demonstrations available from the Mol* web page, including examples for cellPACK models, cytochrome P450 superposition, molecular dynamics trajectories, SARS-CoV-2 virion visualisation, nuclear pore complex models, Zika virus Cryo-EM density, molecular orbitals, and assembly-symmetry annotation.

The paper acknowledges the basis of user documentation and describes how documentation, examples, and interactive demonstrations support adoption. The most useful documentation for users is likely task-oriented material showing how to load structures, change representations and colouring, inspect annotations, save state, export images or animations, and embed the viewer in another service.

Useful documentation topics include:
- getting started through the Mol* web viewer;
- loading structures, volumes, trajectories, and external files;
- using representations, colouring, selection, focus, alignment, measurements, and labels;
- saving sessions and exporting screenshots or animations;
- embedding Mol* Viewer into another web application;
- extending Mol* with additional formats, annotations, or visual components.

Documentation gaps to verify against the current repository include contributor guidance, release-process documentation, testing practices, and examples for extending the plugin architecture.

<!--

**What documentation exists, and where is it?**

**Questions:**

- Where is the main entry point?
- What forms of documentation exist (README, wiki, notebooks…)?
- What is missing or incomplete?
- What do users find most useful right now?
- What do *you* wish existed?

*Write sentences first, then bullets for specifics.*

-->

## Sustainability
### Institutional support and production use strengthen long-term maintenance
Mol* Viewer’s sustainability is supported by its role as production infrastructure for major structural-biology resources. The project is supported by PDBe and RCSB PDB, developed by an international group of contributors, and embedded as the primary 3D viewer in PDBe and RCSB PDB.

The paper argues that collaborative development helps the project anticipate and keep up with changes in structural biology and related fields, which supports long-term sustainability. Funding and institutional support are reported from ELIXIR-CZ, EMBL-EBI, the Wellcome Trust, RCSB PDB funding from NSF, NIH, and DOE, and related support for software development in chemical discovery and education.

Sustainability strengths include:
- production use by major international data resources;
- open-source availability under the MIT licence;
- an international contributor base;
- integration into multiple scientific databases and services;
- modular architecture designed for reuse and extension;
- alignment with rapidly evolving structural-biology data needs.

Risks and uncertainties include the need to maintain performance as datasets grow, the need to track browser and WebGL technology changes, and dependence on continuing institutional support. The article does not define a formal governance model, so governance details should be verified from the current repository before publication.

<!--

**How is the software managed, maintained, and supported over time?**

**Questions:**

- Who maintains it?
- How active is the project?
- What governance (formal or informal) exists?
- What funding supports development or maintenance?
- What risks or future uncertainties matter?
- What plans exist beyond current grants?

*Begin with a few sentences. Clarity beats detail.*

-->

## References
This story is based primarily on the Mol* Viewer Nucleic Acids Research article and the software/project resources identified in that paper.
- Sehnal, D., Bittrich, S., Deshpande, M., Svobodová, R., Berka, K., Bazgier, V., Velankar, S., Burley, S. K., Koča, J., & Rose, A. S. (2021). Mol Viewer: modern web app for 3D visualization and analysis of large biomolecular structures*. Nucleic Acids Research, 49(W1), W431–W437. [https://doi.org/10.1093/nar/gkab314](https://doi.org/10.1093/nar/gkab314)
- Mol* project website: [https://molstar.org/](https://molstar.org/)
- Mol* GitHub organisation: [https://github.com/molstar](https://github.com/molstar)
- Sehnal, D., Rose, A. S., Koča, J., Burley, S. K., & Velankar, S. (2018). Mol: Towards a common library and tools for web molecular graphics, MolVA '18: Proceedings of the Workshop on Molecular Graphics and Visual Analysis of Molecular Data, 29 - 33. [https://doi.org/10.5555/3293503.3293509](https://dl.acm.org/doi/10.5555/3293503.3293509)
- LiteMol Suite, NGL Viewer, PatternQuery, MMTF, BinaryCIF, and CIFTools, which are cited in the paper as earlier tools and technologies informing Mol* development.
- Public structural-biology resources and standards referenced in the paper, including PDBe, RCSB PDB, wwPDB validation reports, PDBx/mmCIF, BinaryCIF, CCP4/MRC/MAP, and molecular dynamics trajectory formats.

<!--

**What external material shapes or supports the project?**

**Questions:**

- Documentation
- Tools
- Research papers
- External standards
- Anything the story builds upon

*Write 1-2 sentences, then list items.*

-->

