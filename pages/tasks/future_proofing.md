---
title: Future-proofing your research software
description: How to design and build research software so that it remains usable and reproducible years after the initial project ends
contributors: ["Giacomo Peru"]
page_id: future_proofing
related_pages: [using_version_control, reproducible_software_environments, licensing_software, releasing_software]
---

## How do you design research software for long-term reproducibility?

This page gives an overview of the practices that help keep research software usable and verifiable years after the experiments it supported were run.

### Description

Research software often needs to reproduce results long after the original development phase is complete — reviewers, collaborators, and your future self may need to re-run analyses months, years, or decades later.
Achieving this requires deliberate decisions at every stage: how you structure your code, which dependencies you choose, how you document your environment, and how you record what the software is supposed to do.
The goal is not perfection from day one, but a baseline level of reproducibility that you build on over time.

### Considerations

- A common scenario is a journal reviewer asking for the code that produced a result, or a PhD student joining a project who needs to re-run analyses from a paper written before they arrived — in both cases, software that "worked on my machine" is not enough.
- Reproducibility exists on a spectrum. At the minimum viable end: someone can clone your repository, install the stated dependencies, and re-run your analysis in under an hour. At the fuller end: every computational step is recorded, the exact environment is archived, and results can be reproduced on independent hardware. Most research benefits from reaching the minimum viable level first.
- Environment drift is one of the most common causes of reproducibility failure: Python 2 scripts written before 2015 are a familiar example — the language, many libraries, and platform assumptions have changed enough that running them today requires significant porting effort. The same risk applies to any software with undocumented or unpinned dependencies. See the [Reproducible software environments](/reproducible_software_environments) page for approaches to capturing and sharing environments.
- The longer the time horizon, the more you need to rely on open, documented standards rather than proprietary tools or formats. If your workflow depends on a commercial API, a cloud service, or a proprietary tool, a pricing change, a terms-of-service update, or a product discontinuation can make your software unrunnable with no technical fix available.
- Adopt modularity early: separating data loading, analysis logic, and visualisation into distinct components means each part can be tested, replaced, or ported independently. Software that mixes all of these in a single script is hard to maintain and fragile — a change to one concern can break everything else.
- Proprietary or obscure binary formats are a real archival risk: without the original software to open them, the data may be effectively inaccessible. Open, well-documented formats (CSV, JSON, HDF5, NetCDF, plain text) are more likely to remain readable as tools evolve, and are a core aspect of the interoperability principle in the [FAIR Principles for Research Software](https://doi.org/10.15497/RDA00068).

### Solutions

- **Capture your software environment explicitly.** Use a dependency file (`requirements.txt`, `environment.yml`, `pyproject.toml`, `renv.lock`) so that others can recreate the environment you used. See the [Reproducible software environments](/reproducible_software_environments) page for guidance on containers and environment managers.
- **Use containers for stronger environment guarantees.** A container image (Docker, Singularity/Apptainer) captures the full runtime environment and can be archived and re-executed years later.
- **Choose dependencies carefully.** Prefer well-maintained, widely-used libraries with a track record of stability over niche or single-author packages. Pin versions in your dependency file, and document *why* you depend on a given library so that future maintainers can evaluate alternatives if needed.
- **Prefer open, documented file formats.** Store data and results in formats that do not require proprietary software to read (e.g. CSV, JSON, HDF5, NetCDF, plain text) rather than formats tied to a specific tool or vendor.
- **Version and archive your software alongside your data.** Assign a version number to each release you use in a publication, and archive both the software and data together using a persistent identifier such as a Zenodo DOI. See the [Releasing software](/releasing_software) page for guidance.
- **Use version control throughout.** Version control is the foundation of reproducibility: it gives you an auditable record of what changed and when. See the [Using version control](/using_version_control) page.


## Further Reading

- **[FAIR Principles for Research Software (FAIR4RS)](https://doi.org/10.15497/RDA00068)** — The foundational document defining what it means for research software to be Findable, Accessible, Interoperable, and Reusable. The reusability principles (R1–R4) are especially relevant to readers of this page.
- **[The Turing Way — Guide for Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research)** — A comprehensive, community-developed handbook covering reproducible research practices from environment management to open publishing. The chapters on version control, containerisation, and computational environments extend the guidance on this page in depth.
- **[Software Sustainability Institute — Guides](https://www.software.ac.uk/guides)** — A curated collection of practical guides on sustainability topics including documentation, testing, licensing, and community building; particularly useful for RSEs looking for next steps on specific practices.
- **[Software Heritage](https://www.softwareheritage.org/)** — A global archive that preserves source code and development history for long-term access; relevant for readers who want to ensure their software remains accessible beyond the lifetime of any single hosting platform.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
