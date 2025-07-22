---
title: "Research Software Story - ACTS"
description: "ACTS - Toolkit for Track Reconstruction in Particle Physics Experiments"
contributors: ["Michael Sparks", "Caterina Doglioni", "Pratik Jawahar"]
page_id: acts_research_software_story
type: research_software_story
---

## The Problem

[Modern particle physics][MODERN_PARTICLE_PHYS] experiments produce enormous volumes of data and
this is expected to grow in the near future.  One key challenge is
[track reconstruction][TRACK_RECONSTRUCTION] - converting raw detector hits from charged particles into
estimated particle trajectories.  Historically, each experiment built its
own specialized tracking software, resulting in duplicated effort and the
lack of a common framework to collaborate and improve upon.  The ACTS
project (Acts Common Tracking Software) was created to provide a single,
experiment-independent toolkit for efficient track reconstruction.

[MODERN_PARTICLE_PHYS]: https://indico.cern.ch/event/447008/contributions/1953687/attachments/1184942/1717323/ParticlePhysicsFOR_TEACHERS.pdf
[TRACK_RECONSTRUCTION]: https://indico.cern.ch/event/666278/contributions/2830627/attachments/1579364/2495228/2018-01-04-Salzburger-Spatind-Conference.pdf

## The Community
## User Community

[ACTS][ACTS] began within the [ATLAS experiment][ATLAS] at [CERN][CERN], but it now serves many
high-energy and nuclear physics communities (including heavy-ion
experiments).  Contributors come from institutions worldwide.  ACTS is
[actively used in ATLAS][ACTS_SPRINGER], CERN's Experimental Physics R&D projects, and
various detector R&D studies.  It also attracts researchers developing new
[tracking algorithms][ACTS_TRACKING] for advanced computing architectures by acting as a
modular test suite and comparison baseline.  This broad adoption has created
a large, collaborative base of users and developers.

[ACTS]: https://acts.readthedocs.io/en/latest/acts_project.html
[ATLAS]: https://atlas.cern/
[CERN]: https://home.cern/about
[ACTS_TRACKING]: https://zenodo.org/records/15005414
[ACTS_SPRINGER]: https://link.springer.com/article/10.1007/s41781-021-00078-8

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

[ACTS_GEOMETRY]: https://acts.readthedocs.io/en/stable/core/geometry/index.html
[ACTS_TRACKING]: https://acts.readthedocs.io/en/stable/tracking.html
[ACTS_EDM]: https://cds.cern.ch/record/2919575
[ACTS_ROOT]: https://acts.readthedocs.io/en/stable/plugins/root.html
[ACTS_DD4HEP]: https://acts.readthedocs.io/en/stable/plugins/dd4hep.html

<!-- TODO: This is an interesting point - having one Python file defining the sequence of algorithms - you mentioned that this enhances reproducibility - it would be good to add a reason e.g. ', which enhances reproducibility because ...' --> 

## Libraries and Systems

- [C++20][CPP_20]: Leverages modern C++ features for performance and concurrency.

- [Eigen][EIGEN]: A linear algebra library used for efficient mathematical
  computations.

- Geometry converters: Interfaces to import detector geometry from [ROOT TGeo][ACTS_ROOT]
  and [DD4hep][ACTS_DD4HEP].

- [GPU acceleration][ACTS_GPU]: Experimental support for using GPUs to speed up certain
  computations.

- [ML integration][ACTS_ML]: Plugins like [Exa.TrkX for GNN based tracking][ACTS_EXA_TRKX] or [ONNX][ONNX_ML] for
  development and testing of ML algorithms for ambiguity resolution, seed
  filtering etc.

[CPP_20]: https://en.cppreference.com/w/cpp/20.html
[EIGEN]: https://eigen.tuxfamily.org/
[ACTS_GPU]: https://hepsoftwarefoundation.org/gsoc/2022/proposal_ACTS_GPU_pipeline_optimization.html
[ACTS_ML]: https://acts.readthedocs.io/en/latest/plugins/MLAlgorithms.html
[ACTS_EXA_TRKX]: https://acts.readthedocs.io/en/stable/plugins/exatrkx.html
[ONNX_ML]: https://onnx.ai/

<!-- TODO: Up to now a lot of external systems and tools have been mentioned - it would be really good for these to be linked e.g. the Eigen library, geometry converters mentioned and the ML plugins -->

<!-- TODO: Up to now a lot of external systems and tools have been mentioned - it would be really good for these to be linked e.g. the Eigen library, geometry converters mentioned and the ML plugins -->

## Software Practices
## Software Quality Practices

<!-- TODO: Wondering if we should change the name of this section to Software Quality Practices - but does that mean the other sections have nothing to do with quality - in which case - might be better to leave it as Software practices as it's more flexible - any thoughts about this @sparkslabs --> 

ACTS development follows [strict software engineering standards][ACTS_CODING_GUIDELINES].  The project
is developed openly on GitHub, and every code submission [triggers automated][ACTS_ACTIONS]
CI tests to ensure nothing breaks and that thread-safety is maintained. 
Developers adhere to [coding][ACTS_CODING_GUIDELINES] and [contribution guidelines][ACTS_CONTRIBUTION_GUIDELINES], and use peer
reviews on merge requests.  [Issues are tracked transparently][ACTS_BUG_TRACKING], and frequent
[meetings][ACTS_MEETINGS] plus mailing list discussions keep contributors aligned and
informed.

[ACTS_CODING_GUIDELINES]: https://acts.readthedocs.io/en/stable/codeguide.html
[ACTS_CONTRIBUTION_GUIDELINES]: https://acts.readthedocs.io/en/latest/contribution/guide.html
[ACTS_BUG_TRACKING]: https://github.com/acts-project/acts/issues
[ACTS_MEETINGS]: https://indico.cern.ch/category/7968/

<!-- TODO: This information is the crux of this Research Software Story - it really needs links - linking to the software engineering standards that are used, link to the GitHub (if it's public), are there links to the automated CI tests, the coding and contribution guidelines are they accessible etc -->

## Community
## Developer Community

The ACTS community provides many resources to help onboard newcomers:

- [Contribution guidelines][ACTS_CONTRIBUTION_GUIDELINES]: A clear step-by-step guide for submitting code.

- [Interactive tutorials][INTERACTIVE_TUTORIALS]: Hands-on guides for configuring and running
  tracking workflows.

[INTERACTIVE_TUTORIALS]: https://atlassoftwaredocs.web.cern.ch/internal-links/tracking-tutorial/
  
<!-- references in presentations --> 

- [Example framework][ACTS_EXAMPLES]: A sample project demonstrating how to use ACTS
  algorithms in practice.

[ACTS_EXAMPLES]: https://github.com/acts-project/acts/tree/main/Examples

In addition, [regular workshops][ACTS_WORKSHOP_24] and training [sessions][ACTS_SESSIONS] help new members start
using ACTS in their experiments.  New contributors are often mentored by
experienced developers, ensuring knowledge transfer and continuous growth of
the community.

[ACTS_WORKSHOP_24]: https://indico.cern.ch/event/1397634/
[ACTS_SESSIONS]: https://indico.cern.ch/category/7968/

<!-- TODO: I think links to the contribution guidelines, interactive tutorials and example framework would make this section richer. Also feel free to update the Community title in these software stories and I can update the template to follow. -->

## Tools

ACTS uses common tools to maintain quality and facilitate contributions:

- Version control: {% tool "git" %}, with repositories on [GitHub][ACTS_GITHUB] for collaborative
  development.

[ACT_GITSHUB]: https://github.com/acts-project/acts

- Continuous integration: Automated testing pipelines using [GitHub Actions][ACTS_ACTIONS]

[ACTS_ACTIONS]: https://github.com/acts-project/acts/blob/main/.github/actions/dependencies/action.yml

- Documentation: Documentation written with {% tool "sphinx" %} and published on
  [ReadTheDocs][ACTS_READTHEDOCS].

[ACTS_READTHEDOCS]: https://acts.readthedocs.io/

- Build system: {% tool "cmake" %} for consistent compilation across platforms.

- [Issue tracking][ACTS_BUG_TRACKING]: GitHub issue trackers for transparent bug reports and
  feature requests.
[ACTS_BUG_TRACKING]: https://github.com/acts-project/acts/issues

- Forums: [Github Discussions][ACTS_DISCUSSIONS], [Mattermost messaging][MATTERMOST] and e-mail lists for open
  communication with the core development team.

[ACTS_DISCUSSIONS]: https://github.com/acts-project/acts/discussions

[MATTERMOST]: https://mattermost.com/

These tools streamline development, ensure reliability, and make it easier
for new users to adopt and contribute to ACTS.

<!-- TODO: This is just a comment - and perhaps something we need to bring up with the ETT folk - lots of tools are mentioned here - and it's unfortunate that we can't use the {% tool "" %} syntax to create tool tips - perhaps this is something we need to ask Bert - i.e. can we do this on arbitrary sections or is it special magic just for the task pages. --> 

## FAIR & Open

ACTS adheres to FAIR principles.  The code is publicly available under the
Mozilla Public License 2.0 (MPL-2.0), allowing broad use and collaboration. 
Each release is archived with a DOI, so the software is easy to find and
cite.  ACTS supports standard data formats and geometry descriptions, which
ensures it is interoperable with various experimental frameworks.  By
developing the toolkit in the open, ACTS fosters reuse across multiple
research communities.

ACTS adheres to the FAIR principles:

* Findable: ACTS is openly hosted on GitHub with clear versioning,
  and releases are archived and assigned DOIs for academic referencing.

* Accessible - Licensed under the Mozilla Public License 2.0, facilitating
  open access and wide adoption by diverse particle physics experiments.
  The code is described using CITATION.cff metadata files.

* Interoperable - Designed to integrate seamlessly with standard detector
  geometry frameworks (ROOT TGeo, DD4hep) and common data formats used
  in high-energy physics.

* Reusable - ACTS provides modular, documented, and tested components,
  enabling reuse and easy adaptation across multiple research projects
  and experiments.

ACTS's open development practices encourage transparent collaboration,
promoting shared improvements across the particle physics community.

<!-- TODO: Is it worth having a bullet list for FAIR, a separate Open statement would be needed. --> 

<!-- TODO: This is fine as is - just a suggestion that we might better with a bullet list

ACTS adheres to the FAIR principles:

Finable - The code is publicly available ....
Accessible - ....
Interoperable - ....
Reusable - ....

-->

<!-- TODO: Detailing out in bullets how the project adheres / promotes FAIR software practices would be good so make the bullet list

Findable
Accessible
Interoperable
Reusable
Open source is a category or consideration by itself as something can be FAIR but not Open - the other categories - citable, transparent and community support may fit better under the FAIR headings.

See https://www.nature.com/articles/s41597-022-01710-x - although I don't think we need to start talking about compliance levels - i.e. this is F2 and F1.2 - just if something matches we can put it under that Findable bullet. -->

<!--
-->

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
usability.

[ACTS_GETTING_STARTED]: https://acts.readthedocs.io/en/latest/getting_started.html
[ACTS_INTERNALS]: https://indico.cern.ch/event/849307/contributions/3569086/attachments/1935012/3206368/Concepts__design_and_Implementation_of_the_A_Common_Tracking_Software__Acts__project.pdf
[ACTS_CONTRIBUTING]: https://github.com/acts-project/acts/blob/main/CONTRIBUTING.rst
[ACTS_EXAMPLES]: https://github.com/acts-project/acts/tree/main/Examples

<!-- TODO: Links here to the different docs would be great.

TODO: Also - something intriguing is said here - 'Documentation contributions are values as highly as code contributions, ...' <-- is there any concrete evidence of this - e.g. it said somewhere or does it come out is some type of project behaviour / credit / recognition process.
-->

## Sustainability

ACTS is sustained by a strong community and multiple funding sources.  It
benefits from institutional support (for example, [CERN's EP R&D programme][CERN_EP_RD],
the NSF-funded [IRIS-HEP project][IRIS_HEP] in the US, the EU-funded [AIDAInnova project][AIDA_INNOVA],
and [CERN's Next Generation Triggers][NEXTGEN_TRIGGERS] initiative).  Having contributors from
many different experiments means ACTS isn't dependent on any single group or
grant.  The project has [clear governance and training practices][ACTS_GOVERNANCE] to retain
knowledge, which keeps ACTS resilient and ready to meet future needs.

(Correct as of July 2025)

[CERN_EP_RD]: https://ep-dep.web.cern.ch/node/7537
[IRIS_HEP]: https://iris-hep.org/
[AIDA_INNOVA]: https://aidainnova.web.cern.ch/
[NEXTGEN_TRIGGERS]: https://nextgentriggers.web.cern.ch/
[ACTS_GOVERNANCE]: https://indico.cern.ch/event/1295479/contributions/5623605/


<!-- TODO: If the funding initiatives and CERNS EP R&D programme could have links - that would be great. --> 

<!-- TODO: I am just wondering about the timelessness of these comments on sustainability - a lot of the rest of the article is pretty timeless - especially if it links out to relevant parts of the project, RSQKit and other resources (and we will get to know about broken links when the linkchecker is fully up and running) - but things around sustainability might change so I am wondering if it's worth putting in a status date here - e.g.
"This is the situation as of July 2025 and funding and sustainability can and does change and this is here as a note on being open about challenges and not the ultimate source of information for the project/tool" <-- or something like that. --> 

<!-- TODO: I know there is a general point on links - and having a link to the OTP system would be great - as part of EVERSE in WP5 is around recognition and reward and this is an interesting point. Also really like the fact that you have added a sustainability challenge here and possible mitigations - it's closer to the reality for many research software products/projects. -->

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
