---
title: "Research Software Story - xAODAnaHelpers"
description: "Analysis Framework for High-Level ATLAS Data"
contributors: ["Michael Sparks", "Caterina Doglioni", "Tobias Fitschen"]
page_id: xah_research_software_story
type: research_software_story
---

## The Problem

Experiments at the Large Hadron Collider (LHC), like ATLAS, generate vast amounts of processed collision data (xAOD). Physicists must analyse this data for physics signals using calibrations, object selections, and corrections. Historically, each analyst largely wrote their own code, leading to duplicate work, inconsistent methods, and reproducibility challenges. The community needed a centralised analysis framework to standardise workflows and ease maintenance.

## The Community

xAODAnaHelpers (xAH) is a common analysis framework widely used within the ATLAS experiment. It was created in 2015 by Giordon Stark and passed to new maintainers (Tobias Fitschen and Michael Hank) in 2023.

The xAH community consists mostly of ATLAS physicists (often early-career PhD students). They have strong physics expertise but less software engineering experience. Most contributions are user-driven via GitHub merge requests, and communication happens on a mailing list and through GitHub issues.

## Technical Aspects

xAH is a modular framework written mainly in C++, with Python 3 for configuration and job steering. It applies calibrations, object selections, and corrections to ATLAS xAOD data, producing structured outputs (ntuples and histograms). The framework integrates directly with ATLAS's official software (Athena and CP tools) to ensure consistent calibrations. Each analysis is configured with one Python file defining the sequence of algorithms, which enhances reproducibility. Jobs are portable and may be run on a personal computer or on the Worldwide LHC Computing Grid (WLCG).

## Libraries and Systems

- Languages: C++ for performance and integration with ATLAS software; Python 3 for flexible configuration.
- Integration: Direct interface to ATLAS Athena CP tools for calibrations and corrections.
- Execution Environment: Runs on both CERN's grid (WLCG) and local machines using the ATLAS software stack.

## Software Practices

xAH development follows standard open-source practices. The code is hosted on GitHub with Git for version control. Changes are submitted as GitHub merge requests and reviewed by the maintainers before merging. Basic Continuous Integration (CI) checks (automatic compilation and tests) run on each proposed change to catch issues early. The project has clear public contribution guidelines, and maintainers actively provide feedback and support to contributors.

## Community

New developers usually join the project after first being users of xAH. They become familiar with the tool in their analyses, then start contributing improvements via GitHub. In late 2023, the project openly invited new maintainers through ATLAS mailing lists, broadening its contributor base. Experienced maintainers mentor incoming contributors via GitHub issues and merge requests, helping new developers get up to speed.

New users often adopt xAH if their research group already uses it, creating a natural adoption path. The project provides documentation, example configurations, and tutorials to help beginners get started. A hands-on tutorial at the 2024 ATLAS UK workshop introduced xAH to more physicists. Ongoing user support is community-driven via the mailing list and GitHub, where questions and issues are addressed collaboratively.

## Tools

- Git: The code is managed with Git in a public GitHub repository (for version control and collaboration).
- GitHub Actions (CI): Automatically compiles and tests each proposed change (serving as the main quality gate, since no dedicated static analysis is used).
- GitHub Issues: Used for tracking bugs and user support queries.

Quality is further ensured by maintainers' manual code reviews and by continuous real-world use of xAH in ATLAS analyses (which quickly highlights any issues or needed improvements).

## FAIR & Open

xAH follows FAIR principles (Findable, Accessible, Interoperable, Reusable). For example:

- Open source: The code is publicly available on GitHub under an Apache 2.0 license, allowing broad use and modification.
- Citable: The software is archived on Zenodo with a DOI, enabling proper academic citation.
- Transparent: All development, issue tracking, and discussions are done openly on GitHub.
- Community support: An active public mailing list provides user support and communication.

While xAH is primarily tailored to ATLAS, its open approach improves the chance for cross-experiment visibility and reuse of its ideas.

## Documentation

xAH provides extensive documentation on ReadTheDocs (generated via Doxygen). It includes:

- Instructions for installation and initial setup.
- Usage guides and detailed explanations of analysis algorithms.
- Contributor guidelines and development workflow documentation.

There are also tutorials and examples (some are being updated to the latest version). The team plans to add a community wiki for user-contributed tips, examples, and troubleshooting guides.

## Sustainability

xAH does not have dedicated funding or a formal sustainability plan. Development relies on voluntary contributions from ATLAS physicists. ATLAS does offer some incentives through its Operational Task Points (OTP) system, which rewards members for software maintenance. In general, the longevity of xAH depends on its continued usefulness in ATLAS analyses and the community's willingness to support it.

The smooth handover to new maintainers in 2023 shows that the community is invested in xAH's future. Efforts to improve documentation and onboarding are positive signs for sustainability. However, a more structured long-term plan (eg. secured funding or institutional support) would further strengthen the project's future.

## References

- Fitschen, T. (2024). EOSC Pilot Project: xAODAnaHelpers - EVERSE WP4 Meeting. *Presentation at EVERSE WP4 Meeting*, University of Manchester.
- EVERSE Project (2024). Pilot Survey Responses for xAODAnaHelpers (ESCAPE Cluster). University of Manchester.
- xAODAnaHelpers GitHub Repository: <https://github.com/UCATLAS/xAODAnaHelpers>
- Zenodo DOI (v1.0): 10.5281/zenodo.7335128
