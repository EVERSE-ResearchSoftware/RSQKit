---
title: "Research Software Story - xAODAnaHelpers"
description: "Analysis Framework for High-Level ATLAS Data"
contributors: ["Michael Sparks", "Caterina Doglioni", "Tobias Fitschen"]
page_id: xah_research_software_story
type: research_software_story
---

## The Problem

Experiments at the [Large Hadron Collider][CERN_LHC] (LHC), like [ATLAS][ATLAS_EXPERIMENT], generate vast amounts of processed collision data in a format called [xAOD][ATLAS_DATA_FORMAT].
Physicists must [analyse this data for physics signals][ATLAS_ANALYSIS] using calibrations, object selections, and corrections.
Historically, each analyst largely wrote their own code, leading to duplicate work, inconsistent methods, and reproducibility challenges.
The community needed a centralised analysis framework to standardise workflows and ease maintenance.


## User Community

[xAODAnaHelpers][XAH_WEBSITE] (xAH) is a common analysis framework widely used within the ATLAS experiment.
It was created in 2015 by Giordon Stark and passed to new maintainers (Tobias Fitschen and Michael Hank) in 2023.

The [xAH community][XAH_COMMUNITY_LINKS] consists mostly of ATLAS physicists (often early-career PhD students).
They have strong physics expertise but less software engineering experience.
Most contributions are user-driven via GitHub [pull requests][XAH_GITHUB_PULLREQUESTS], and communication happens on a mailing list and through [GitHub issues][XAH_GITHUB_ISSUES].


## Technical Aspects

xAH is a modular framework written mainly in {% tool "cpp" %}, with {% tool "python" %} 3 for configuration and job steering.
It applies calibrations, object selections, and corrections to [ATLAS xAOD][ATLAS_DATA_FORMAT] data, producing structured outputs (ntuples and histograms).
The framework integrates directly with ATLAS's official software [Athena][ATLAS_ATHENA_GITLAB] to ensure consistent configuration.

Each analysis is [configured with one Python file][XAH_CONFIGURING_SAMPLES] defining the sequence of algorithms.
This enhances reproducibility because it becomes natural to maintain such configuration with version control, tag releases - in a manner reminiscent of Workflows etc. Jobs are portable and may be run on a personal computer or on the Worldwide LHC Computing Grid ([WLCG][WLCG_GRID]).


## Libraries and Systems

- **Languages**: {% tool "cpp" %} for performance and integration with ATLAS software; {% tool "python" %} 3 for flexible configuration.
- **Integration**: Direct interface to [ATLAS Athena][ATLAS_ATHENA_GITLAB] CP tools for calibrations and corrections.
- **Execution Environment**: Runs on both CERN's grid ([WLCG][WLCG_GRID]) and local machines using the ATLAS software stack.


## Software Quality Practices

xAH development follows [standard open-source practices][XAH_DEVELOPMENT_WORKFLOW].
The code is hosted on [GitHub][XAH_GITHUB] with {% tool "cpp" %} for version control.
Changes are submitted as GitHub [pull requests][XAH_GITHUB_PULLREQUESTS] and reviewed by the maintainers before merging.
Basic [Continuous Integration][XAH_GITHUB_ACTIONS] (CI) checks (automatic compilation and tests) run on each proposed change to catch issues early.
The project has clear public [contribution guidelines][XAH_CONTRIBUTION_GUIDELINES], and maintainers actively provide feedback and support to contributors.


## Developer Community

New developers usually join the project after first being users of xAH.
They become familiar with the tool in their analyses, then start contributing improvements via [GitHub][XAH_GITHUB].
In late 2023, the project openly invited new maintainers through ATLAS mailing lists after the original maintainer stepped down.
Experienced maintainers mentor incoming contributors via [GitHub issues][XAH_GITHUB_ISSUES] and merge requests, helping new developers get up to speed.

New users often adopt xAH if their research group already uses it, creating a natural adoption path.
The project provides [documentation][XAH_READTHEDOCS], example [configurations][XAH_CONFIGURING_SAMPLES], and [tutorials][XAH_COMMUNITY_LINKS] to help beginners get started.
A hands-on [tutorial at the 2024 ATLAS UK workshop][XAH_WLCG_TRAINING] introduced xAH to more physicists.
Ongoing user support is community-driven via the mailing list and [GitHub][XAH_GITHUB], where questions and issues are addressed collaboratively.


## Tools

- {% tool "git" %}: The code is managed with Git in a [public GitHub repository][XAH_GITHUB] (for
  version control and collaboration).

- [GitHub Actions][XAH_GITHUB_ACTIONS] (CI): Automatically compiles and tests each proposed change
  (serving as the main quality gate, since no dedicated static analysis is used).

- [GitHub Issues][XAH_GITHUB_ISSUES]: Used for tracking bugs and user support queries.

Quality is further ensured by maintainers' manual code reviews and by continuous real-world use of xAH in ATLAS analyses (which quickly highlights any issues or needed improvements).


## FAIR & Open

xAH adheres to the [FAIR principles for research software][NATURE_FAIR4RS] as follows:

* **Findable**: Publicly hosted on [GitHub][XAH_GITHUB] and archived
  on [Zenodo][XAH_ZENODO_RECORDS] with a DOI, making the software easily discoverable and academically citable.

* **Accessible**: Distributed under an [Apache 2.0][LICENSE_APACHE2]
  open-source license, ensuring unrestricted access and modification rights for users.
  Metadata about the project is provided in [.zenodo.json][XAH_ZENODO_METADATA] standard format.

* **Interoperable**: Built specifically for ATLAS experiment
  data analysis, it interfaces directly with standard ATLAS data formats ([xAOD][ATLAS_DATA_FORMAT]), analysis software ([Athena][ATLAS_ATHENA_GITLAB]), and computing environments ([WLCG Grid][WLCG_GRID]).

* **Reusable**: The openness and documentation of xAH facilitate
  reuse within ATLAS analyses, enabling consistent and reproducible workflows.
  Also, while xAH is primarily tailored to ATLAS, its open approach improves the chance for cross-experiment visibility and reuse of its ideas.

Additionally, the project is open source: The code is publicly available on [GitHub][XAH_GITHUB] under an [Apache 2.0 license][LICENSE_APACHE2], allowing broad use and modification.
Development is transparent with [issue tracking][XAH_GITHUB_ISSUES], and discussions are done openly on GitHub.
Beyond this an active public mailing list provides user support and communication.


## Documentation

xAH provides extensive documentation on [ReadTheDocs][XAH_READTHEDOCS] (generated via Doxygen).
It includes:

- Instructions for [installation and initial setup][XAH_INSTALLATION].

- [Usage guides][XAH_USAGE] and detailed explanations of [analysis algorithms][XAH_ALGORITHMS].

- [Contributor guidelines][XAH_CONTRIBUTION_GUIDELINES] and development workflow documentation.

There are also [tutorials and examples][XAH_COMMUNITY_LINKS] (some are being updated to the latest version).
The team hopes to add a community wiki for user-contributed tips, examples, and troubleshooting guides.


## Sustainability

As of July 2025, xAH does not have dedicated funding or a formal sustainability plan.
Development relies on voluntary contributions from ATLAS physicists.
ATLAS does offer some incentives through its Operational Task Points ([OTP][ATLAS_OTP]) system, which rewards members for software maintenance.
In general, the longevity of xAH depends on its continued usefulness in ATLAS analyses and the community's willingness to support it.

<!-- Note: Most of the links relating to OTP are behind a cern login -->

The smooth handover to new maintainers in 2023 shows that the community is invested in xAH's future.
Efforts to improve documentation and onboarding are positive signs for sustainability.
However, a more structured long-term plan (eg.
secured funding or institutional support) would further strengthen the project's future.


## References

- Fitschen, T.  (2024).  User analysis software in a large collaboration
  (xAODAnaHelpers): development, maintenance and training, WLCG/HSF Workshop 2024, 13-17 May 2024, <https://indico.cern.ch/event/1369601/contributions/5883628/>

- EVERSE Project (2024). Pilot Survey Responses for xAODAnaHelpers (ESCAPE Cluster). University of Manchester.
- xAODAnaHelpers GitHub Repository: <https://github.com/UCATLAS/xAODAnaHelpers>
- Zenodo DOI (v1.0): [10.5281/zenodo.7335128][ZENODO_7335128]

<!-- External References embedded as links -->

[ATLAS_ANALYSIS]: https://cds.cern.ch/record/1282996/files/ATL-PHYS-SLIDE-2010-229.pdf
[ATLAS_ATHENA_GITLAB]: https://gitlab.cern.ch/atlas/athena
[ATLAS_DATA_FORMAT]: https://indico.cern.ch/event/887763/contributions/3785010/subcontributions/302546/attachments/2008042/3354193/c_240320.pdf
[ATLAS_EXPERIMENT]: https://atlas.cern/

<!-- Note: Most of the links relating to OTP are behind a cern login -->

[ATLAS_OTP]: https://indico.mpp.mpg.de/event/4493/contributions/10569/attachments/8279/9189/OTP_Overview.pdf
[CERN_LHC]: https://home.cern/science/accelerators/large-hadron-collider
[LICENSE_APACHE2]: https://www.apache.org/licenses/LICENSE-2.0
[NATURE_FAIR4RS]: https://www.nature.com/articles/s41597-022-01710-x
[WLCG_GRID]: https://www.home.cern/science/computing/grid
[XAH_ALGORITHMS]: https://xaodanahelpers.readthedocs.io/en/latest/Algorithms.html
[XAH_COMMUNITY_LINKS]: https://xaodanahelpers.readthedocs.io/en/latest/Community.html
[XAH_CONFIGURING_SAMPLES]: https://xaodanahelpers.readthedocs.io/en/latest/UsingUs.html#configuring-samples
[XAH_CONTRIBUTION_GUIDELINES]: https://github.com/UCATLAS/xAODAnaHelpers/blob/main/CONTRIBUTING.md
[XAH_DEVELOPMENT_WORKFLOW]: https://xaodanahelpers.readthedocs.io/en/latest/Development.html
[XAH_GITHUB]: https://github.com/UCATLAS/xAODAnaHelpers
[XAH_GITHUB_ACTIONS]: https://github.com/UCATLAS/xAODAnaHelpers/actions
[XAH_GITHUB_ISSUES]: https://github.com/UCATLAS/xAODAnaHelpers/issues
[XAH_GITHUB_PULLREQUESTS]: https://github.com/UCATLAS/xAODAnaHelpers/pulls
[XAH_INSTALLATION]: https://xaodanahelpers.readthedocs.io/en/latest/Installing.html
[XAH_READTHEDOCS]: https://xaodanahelpers.readthedocs.io/en/latest/index.html
[XAH_USAGE]: https://xaodanahelpers.readthedocs.io/en/latest/UsingUs.html
[XAH_WEBSITE]: https://ucatlas.github.io/xAODAnaHelpers/
[XAH_WLCG_TRAINING]: https://indico.cern.ch/event/1369601/contributions/5883628/
[XAH_ZENODO_METADATA]: https://github.com/UCATLAS/xAODAnaHelpers/blob/main/.zenodo.json
[XAH_ZENODO_RECORDS]: https://zenodo.org/records/7335128
[ZENODO_7335128]: https://zenodo.org/records/7335128