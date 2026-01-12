---
title: "Software Management Planning"
description: How to prepare a software management plan?
contributors: ["Marek Suchánek", "Eva Martín del Pico", "Vassilios Ioannidis", "Carlos Martinez Ortiz"] 
page_id: software_management_planning
keywords: ["software management plan", "smp", "research software management", "best practices", "planning"]
---

### Description 

A **Software Management Plan (SMP)** is an essential document that supports the quality, sustainability, and long-term reuse of research software. It provides a structured framework for planning how software will be developed, maintained, shared, and preserved over time. By capturing key decisions early and updating them throughout the project, an SMP embeds good practices into the development process and helps ensure that software remains usable. 

An SMP formalizes the structures and goals needed to guide responsible software development. It addresses several core areas, including:

- **Reproducibility and Reusability**: Ensuring the software can be reliably reproduced, verified, and reused by others.
- **Funding and Milestones**: Allowing funding bodies to understand the development strategy and monitor progress.
- **Community Standards and Best Practices**: Promoting awareness and adoption of established best practices in research software engineering, such as code reviews, continuous integration, testing frameworks, documentation standards, or [FAIR4RS principles](https://doi.org/10.15497/RDA00068).
- **Accessibility**: Ensuring the software is discoverable, accessible, and usable by the wider research community.
- **Crediting and Impact**: Defining how contributors are acknowledged (e.g., citation files, ORCID links, authorship practices), how usage will be tracked, and how the software’s scientific and societal impact will be evaluated and communicated.

Therefore, an SMP ultimately strengthens the impact and longevity of research software by supporting transparent, sustainable, and community-aligned development.

### Considerations

- The SMP is a **living document** that provides **guidance** throughout all phases of the [software lifecycle](./life_cycle), and it shall be continuously updated and maintained as the project evolves. 
- The planning process should engage all relevant stakeholders involved in the software lifecycle (e.g., architects, developers, researchers, legal advisors, community managers) to ensure that the **plan is comprehensive**, that **responsibilities are shared and understood**, and that the **SMP is effectively adopted and followed** throughout the project. One could consider the role of **user support, documentation, community contributions**, onboarding pathways, and governance structures to foster community-aligned development.
- The plan must systematically **cover foundational project aspects**, including general information, collaboration and licensing, analysis, design, implementation, testing and quality assurance, deployment and delivery, and versioning / releases.
- The SMP should **reinforce engineering best practices**, including coding standards, automated testing, continuous integration, code review, secure development workflows, and documentation strategies. However, it should also specify **long-term maintenance** expectations, resource needs, governance models, and contingency plans (e.g., succession of maintainers, deprecation strategies).
- The SMP should be designed for **integration with core development platforms** (e.g., [GitHub](https://github.com), [GitLab](https://about.gitlab.com/)) as well as essential research software registries and repositories (e.g., [Software Heritage](https://www.softwareheritage.org/), [Zenodo](https://zenodo.org/), [bio.tools](https://bio.tools), [OpenEBench](https://openebench.bsc.es/)) to streamline putting the plan into practice.
- The plan should build upon **established community standards and resources**, such as the [ELIXIR SMP template](https://elixir-europe.org/sites/default/files/documents/software-management-plan.pdf) and guidance from organizations like the [Software Sustainability Institute (SSI)](https://www.software.ac.uk/) and [The Turing Way](https://book.the-turing-way.org/).
- The SMP should be **explicitly tailored to the type, scope, and intended longevity of the software** (“not all software is created equal”). Different classes of software (e.g. exploratory analysis code, reusable research software, long-lived research software infrastructure) require different levels of rigor, formality, and investment across engineering practices, governance, and sustainability, as reflected in models such as the [**EVERSE three-tier view**](./three_tier_view).
- While all SMPs should **promote good practices**, the primary quality goals may differ by software type; for example, prioritising reproducibility, transparency, and provenance for analysis code, versus robustness, scalability, security, and long-term maintenance for research software infrastructure. The SMP should **make these priorities explicit and guide teams** to focus effort where it delivers the most value.
- The SMP planning tool should be capable of generating outputs that are both **human-readable** (for relevant stakeholders and reviewers) and **machine-actionable** (for automated workflows, pipelines, metadata extraction, or compliance checks).

### Solutions 

Before choosing an SMP solution, it is important to recognise that **different projects and contexts call for different levels of detail and support**. The choice of resources may depend on the type of software, the research domain, the project’s maturity, and the expectations set by **institutions, national guidelines, or funder requirements**. Available tools range from lightweight checklists to comprehensive templates and machine-actionable frameworks, allowing teams to select an approach that best aligns with their goals and obligations.

- [ELIXIR SMP](https://elixir-europe.github.io/software-management-plans/): ELIXIR has developed a low-barrier SMP, specifically tailored for life science researchers, aligned to the FAIR Research Software principles.
- {% tool "software-management-wizard" %}: Data Stewardship Wizard instance managed within ELIXIR for software management planning, offering guided question flows, true living document experience, collaborative editing, and various export options.
- [maSMP](https://zbmed-semtec.github.io/maSMPs/): A machine-actionable representation of SMPs following the work on maDMP application profile in order to cover the case of ELIXIR Software Management Plans (SMPs).
- [Software Sustainability Institute (SSI) guideline “Writing and using a software management plan”](https://www.software.ac.uk/guide/writing-and-using-software-management-plan): A high-level guide introducing the purpose, structure, and benefits of SMPs, aimed at researchers and project managers.
- [Software Sustainability Institute (SSI) SMP Checklist](https://doi.org/10.5281/zenodo.2159713): A practical checklist to help evaluate whether an SMP covers essential elements of sustainable research software development.
- [Wageningen University & Research (WUR) SMP Template and Guidance](https://doi.org/10.5281/zenodo.10473646): A structured SMP template accompanied by domain-aware guidance used across WUR research groups.
- [Netherlands eScience Center Practical Guide to SMPs](https://doi.org/10.5281/zenodo.7589725): A detailed, practitioner-focused guide offering examples and recommendations for creating effective SMPs in computational research projects.
- [Wellcome Trust Outputs Management Plans](https://wellcome.org/research-funding/guidance/prepare-to-apply/how-complete-outputs-management-plan): Although broader in scope, these plans include requirements relevant to software outputs and can inform funding-aligned SMP development. This approach seems to be adopted by several funders to cover diversity of research outputs.
- [forschungsdaten.info Software Management Plans](http://forschungsdaten.info): A guide summarising what an SMP should contain (administrative & technical info, software description, QA, maintenance & sharing, legal/ethical aspects, user support, costs and responsibilities).
