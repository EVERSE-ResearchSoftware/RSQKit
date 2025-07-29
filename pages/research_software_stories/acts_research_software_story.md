---
title: "Research Software Story - ACTS"
description: "ACTS - Toolkit for Track Reconstruction in Particle Physics Experiments"
contributors: ["Michael Sparks", "Caterina Doglioni", "Pratik Jawahar"]
page_id: acts_research_software_story
type: research_software_story
---

## The Problem

[Modern particle physics][CONCEPT_MODERN_PARTICLE_PHYS] experiments produce enormous volumes of data and
this is expected to grow in the near future.  One key challenge is
[track reconstruction][CONCEPT_TRACK_RECONSTRUCTION] - converting raw detector hits from charged particles into
estimated particle trajectories.  Historically, each experiment built its
own specialized tracking software, resulting in duplicated effort and the
lack of a common framework to collaborate and improve upon.  The ACTS
project (Acts Common Tracking Software) was created to provide a single,
experiment-independent toolkit for efficient track reconstruction.

## User Community

[ACTS][ACTS] began within the [ATLAS experiment][ATLAS] at [CERN][CERN], but it now serves many
high-energy and nuclear physics communities (including heavy-ion
experiments).  Contributors come from institutions worldwide.  ACTS is
[actively used in ATLAS][ACTS_SPRINGER], CERN's Experimental Physics R&D projects, and
various detector R&D studies.  It also attracts researchers developing new
[tracking algorithms][ACTS_TRACKING] for advanced computing architectures by acting as a
modular test suite and comparison baseline.  This broad adoption has created
a large, collaborative base of users and developers.

## Technical Aspects

ACTS is a high-performance, thread-safe library written in modern C++ ({% tool "cpp" %}).  Its
core components include:

- [Geometry description][ACTS_GEOMETRY]: An optimised detector geometry model for fast
  navigation.

- [Tracking algorithms][ACTS_TRACKING]: Tools for track finding and fitting, seeding, vertex
  finding, etc.

- [Event Data Model (EDM)][ACTS_EDM]: A standardised way to represent track data.

ACTS is optimised for speed, using compile-time polymorphism (templates)
instead of runtime inheritance to improve performance.  It keeps
non-optional dependencies to a minimum (mainly the Eigen linear algebra
library).  The toolkit uses {% tool "cmake" %} for building and runs on Linux with
multi-core support.  It can integrate with external geometry definitions
(eg.  [ROOT TGeo][ACTS_ROOT] or [DD4hep][ACTS_DD4HEP]), making it easier to use in different
experiments' software frameworks.

## Libraries and Systems

- [C++20][LANGUAGE_CPP_20]: Leverages modern C++ features for performance and concurrency.

- [Eigen][LIBRARY_EIGEN]: A linear algebra library used for efficient mathematical
  computations.

- **Geometry converters**: Interfaces to import detector geometry from [ROOT TGeo][ACTS_ROOT]
  and [DD4hep][ACTS_DD4HEP].

- [GPU acceleration][ACTS_GPU]: Experimental support for using GPUs to speed up certain
  computations.

- [ML integration][ACTS_ML]: Plugins like [Exa.TrkX for GNN based tracking][ACTS_EXA_TRKX] or [ONNX][LIBRARY_ONNX_ML] for
  development and testing of ML algorithms for ambiguity resolution, seed
  filtering etc.

## Software Quality Practices

ACTS development follows [strict software engineering standards][ACTS_CODING_GUIDELINES].  The project
is developed openly on GitHub, and every code submission [triggers automated][ACTS_GITHUB_ACTIONS]
CI tests to ensure nothing breaks and that thread-safety is maintained. 
Developers adhere to [coding][ACTS_CODING_GUIDELINES] and [contribution guidelines][ACTS_CONTRIBUTION_GUIDELINES], and use peer
reviews on merge requests.  [Issues are tracked transparently][ACTS_GITHUB_BUG_TRACKING], and frequent
[meetings][ACTS_MEETINGS] plus mailing list discussions keep contributors aligned and
informed.

## Developer Community

The ACTS community provides many resources to help onboard newcomers:

- [Contribution guidelines][ACTS_CONTRIBUTION_GUIDELINES]: A clear step-by-step guide for submitting code.

- [Interactive tutorials][ACTS_INTERACTIVE_TUTORIALS]: Hands-on guides for configuring and running
  tracking workflows.

- [Example framework][ACTS_EXAMPLES]: A sample project demonstrating how to use ACTS
  algorithms in practice.

In addition, [regular workshops][ACTS_WORKSHOP_24] and training [sessions][ACTS_SESSIONS] help new members start
using ACTS in their experiments.  New contributors are often mentored by
experienced developers, ensuring knowledge transfer and continuous growth of
the community.

## Tools

ACTS uses common tools to maintain quality and facilitate contributions:

- **Version control**: {% tool "git" %}, with repositories on [GitHub][ACTS_GITHUB] for collaborative
  development.

- **Continuous integration**: Automated testing pipelines using [GitHub Actions][ACTS_GITHUB_ACTIONS]

- **Documentation**: Documentation written with {% tool "sphinx" %} and published on
  [ReadTheDocs][ACTS_READTHEDOCS].

- **Build system**: {% tool "cmake" %} for consistent compilation across platforms.

- [Issue tracking][ACTS_GITHUB_BUG_TRACKING]: GitHub issue trackers for transparent bug reports and
  feature requests.

- **Forums**: [Github Discussions][ACTS_GITHUB_DISCUSSIONS], [Mattermost messaging][COLLABORATION_MATTERMOST] and e-mail lists for open
  communication with the core development team.

These tools streamline development, ensure reliability, and make it easier
for new users to adopt and contribute to ACTS.

## FAIR & Open

ACTS adheres to the [FAIR principles for research software][NATURE_FAIR4RS]:

* **Findable**: [ACTS is openly hosted on GitHub][ACTS_GITHUB] with clear versioning,
  and releases are [archived on Zenodo] and assigned DOIs for academic
  referencing.

* **Accessible** - Licensed under the [Mozilla Public License 2.0][MOZILLA_20_LICENSE], facilitating
  open access and wide adoption by diverse particle physics experiments.
  The code is described using [CITATION.cff metadata files][CFF_FILES].

* **Interoperable** - Designed to integrate seamlessly with standard detector
  geometry frameworks ([ROOT TGeo][ACTS_ROOT], [DD4hep][ACTS_DD4HEP]) and common data formats used
  in high-energy physics.

* **Reusable** - ACTS provides modular, documented, and tested components,
  enabling reuse and easy adaptation across multiple research projects
  and experiments.

ACTS's open development practices encourage transparent collaboration,
promoting shared improvements across the particle physics community
in multiple research communities.

## Documentation

ACTS offers thorough documentation for both users and developers:

- [User guides][ACTS_GETTING_STARTED]: Detailed instructions for installation, setup, and usage.

- [Developer docs][ACTS_INTERNALS]: Explanations of internal design, components, and APIs for
  contributors.

- [Tutorials and examples][ACTS_EXAMPLES]: Step-by-step examples demonstrating common use
  cases. 

The documentation is updated alongside the code to remain accurate and
up-to-date.  Documentation contributions are valued as highly as code
contributions, reflecting the importance of good documentation for ACTS's
usability. (this is reflected primarily in practice)

## Sustainability

ACTS is sustained by a strong community and multiple funding sources.  It
benefits from institutional support (for example, [CERN's EP R&D programme][FUNDING_CERN_EP_RD],
the NSF-funded [IRIS-HEP project][FUNDING_IRIS_HEP] in the US, the EU-funded [AIDAInnova project][FUNDING_AIDA_INNOVA],
and [CERN's Next Generation Triggers][FUNDING_CERN_NEXTGEN_TRIGGERS] initiative).  Having contributors from
many different experiments means ACTS isn't dependent on any single group or
grant.  The project has [clear governance and training practices][ACTS_GOVERNANCE] to retain
knowledge, which keeps ACTS resilient and ready to meet future needs.

(Correct as of July 2025)

## References

- ACTS GitHub Repository: <https://github.com/acts-project/acts>
- ACTS Official Documentation: <https://acts.readthedocs.io/>
- License: Mozilla Public License v2.0 (MPL-2.0)
- IRIS-HEP Project: <https://iris-hep.org/>
- Ai, X., Allaire, C., Calace, N.  et al.  A Common Tracking Software
  Project.  Comput Softw Big Sci 6, 8 (2022). 
  <https://doi.org/10.1007/s41781-021-00078-8>
- Varni, C.,The ATLAS collaboration.  Integration of the ACTS track
  reconstruction toolkit in the ATLAS software for HL-LHC operations (2025)
  <https://cds.cern.ch/record/2921878>

<!-- External References embedded as links -->

[ACTS]: https://acts.readthedocs.io/en/latest/acts_project.html
[ACTS_GITHUB_BUG_TRACKING]: https://github.com/acts-project/acts/issues
[ACTS_CODING_GUIDELINES]: https://acts.readthedocs.io/en/stable/codeguide.html
<!-- Yes, there are guidelines on contributing in different places, to reflect audience -->
[ACTS_CONTRIBUTING]: https://github.com/acts-project/acts/blob/main/CONTRIBUTING.rst
[ACTS_CONTRIBUTION_GUIDELINES]: https://acts.readthedocs.io/en/latest/contribution/guide.html
[ACTS_DD4HEP]: https://acts.readthedocs.io/en/stable/plugins/dd4hep.html
[ACTS_EDM]: https://cds.cern.ch/record/2919575
[ACTS_EXA_TRKX]: https://acts.readthedocs.io/en/stable/plugins/exatrkx.html
[ACTS_EXAMPLES]: https://github.com/acts-project/acts/tree/main/Examples
[ACTS_GEOMETRY]: https://acts.readthedocs.io/en/stable/core/geometry/index.html
[ACTS_GETTING_STARTED]: https://acts.readthedocs.io/en/latest/getting_started.html
[ACTS_GITHUB]: https://github.com/acts-project/acts
[ACTS_GITHUB_ACTIONS]: https://github.com/acts-project/acts/blob/main/.github/actions/dependencies/action.yml
[ACTS_GITHUB_DISCUSSIONS]: https://github.com/acts-project/acts/discussions
[ACTS_GOVERNANCE]: https://indico.cern.ch/event/1295479/contributions/5623605/
[ACTS_INTERNALS]: https://indico.cern.ch/event/849307/contributions/3569086/attachments/1935012/3206368/Concepts__design_and_Implementation_of_the_A_Common_Tracking_Software__Acts__project.pdf
[ACTS_INTERACTIVE_TUTORIALS]: https://atlassoftwaredocs.web.cern.ch/internal-links/tracking-tutorial/
[ACTS_GPU]: https://hepsoftwarefoundation.org/gsoc/2022/proposal_ACTS_GPU_pipeline_optimization.html
[ACTS_MEETINGS]: https://indico.cern.ch/category/7968/
[ACTS_ML]: https://acts.readthedocs.io/en/latest/plugins/MLAlgorithms.html
[ACTS_READTHEDOCS]: https://acts.readthedocs.io/
[ACTS_ROOT]: https://acts.readthedocs.io/en/stable/plugins/root.html
[ACTS_SESSIONS]: https://indico.cern.ch/category/7968/
[ACTS_SPRINGER]: https://link.springer.com/article/10.1007/s41781-021-00078-8
[ACTS_TRACKING]: https://acts.readthedocs.io/en/stable/tracking.html
[ACTS_WORKSHOP_24]: https://indico.cern.ch/event/1397634/
[ACTS_ZENODO]: https://zenodo.org/records/7733496
[ATLAS]: https://atlas.cern/
[CERN]: https://home.cern/about
[CFF_FILES]: https://citation-file-format.github.io/
[COLLABORATION_MATTERMOST]: https://mattermost.com/
[CONCEPT_TRACK_RECONSTRUCTION]: https://indico.cern.ch/event/666278/contributions/2830627/attachments/1579364/2495228/2018-01-04-Salzburger-Spatind-Conference.pdf
[CONCEPT_MODERN_PARTICLE_PHYS]: https://indico.cern.ch/event/447008/contributions/1953687/attachments/1184942/1717323/ParticlePhysicsFOR_TEACHERS.pdf
[FUNDING_CERN_NEXTGEN_TRIGGERS]: https://nextgentriggers.web.cern.ch/
[FUNDING_CERN_EP_RD]: https://ep-dep.web.cern.ch/node/7537
[FUNDING_IRIS_HEP]: https://iris-hep.org/
[FUNDING_AIDA_INNOVA]: https://aidainnova.web.cern.ch/
[LANGUAGE_CPP_20]: https://en.cppreference.com/w/cpp/20.html
[LIBRARY_EIGEN]: https://eigen.tuxfamily.org/
[LIBRARY_ONNX_ML]: https://onnx.ai/
[MOZILLA_20_LICENSE]: https://opensource.org/license/mpl-2-0
[NATURE_FAIR4RS]: https://www.nature.com/articles/s41597-022-01710-x
