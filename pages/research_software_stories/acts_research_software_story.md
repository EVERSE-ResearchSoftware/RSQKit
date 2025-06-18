---
title: "Research Software Story - ACTS"
description: "ACTS - Toolkit for Track Reconstruction in Particle Physics Experiments"
contributors: ["Michael Sparks", "Caterina Doglioni", "Pratik Jawahar"]
page_id: acts_research_software_story
type: research_software_story
---

## The Problem

Modern particle physics experiments produce enormous volumes of data. One key challenge is track reconstruction - converting raw detector hits into meaningful particle trajectories. Historically, each experiment built its own tracking software, resulting in duplicated effort and limited sharing of improvements. The ACTS project (Acts Common Tracking Software) was created to provide a single, experiment-independent toolkit for efficient track reconstruction.

## The Community

ACTS began within the ATLAS experiment at CERN, but it now serves many high-energy and nuclear physics communities (including heavy-ion experiments). Contributors come from institutions worldwide. ACTS is actively used in ATLAS, CERN's Experimental Physics R&D projects, and various detector R&D studies. It also attracts researchers developing new tracking algorithms and advanced computing architectures. This broad adoption has created a large, collaborative base of users and developers.

## Technical Aspects

ACTS is a high-performance, thread-safe library written in modern C++ (C++20). Its core components include:

- Tracking algorithms: Tools for track fitting, seeding, and vertex finding.
- Geometry description: An optimised detector geometry model for fast navigation.
- Event Data Model (EDM): A standardised way to represent track data.

ACTS is optimised for speed, using compile-time polymorphism (templates) instead of runtime inheritance to improve performance. It keeps non-optional dependencies to a minimum (mainly the Eigen linear algebra library). The toolkit uses CMake for building and runs on Linux with multi-core support. It can integrate with external geometry definitions (eg. ROOT TGeo or DD4hep), making it easier to use in different experiments' software frameworks.

## Libraries and Systems

- C++20: Leverages modern C++ features for performance and concurrency.
- Eigen: A linear algebra library used for efficient mathematical computations.
- Geometry converters: Interfaces to import detector geometry from ROOT TGeo and DD4hep.
- GPU acceleration: Experimental support for using GPUs to speed up certain computations.

## Software Practices

ACTS development follows strict software engineering standards. The project is developed openly on GitLab/GitHub, and every code submission triggers automated CI tests to ensure nothing breaks and that thread-safety is maintained. Developers adhere to coding guidelines and use peer reviews on merge requests. Issues are tracked transparently, and frequent meetings plus mailing list discussions keep contributors aligned and informed.

## Community

The ACTS community provides many resources to help onboard newcomers:

- Contribution guidelines: A clear step-by-step guide for submitting code.
- Interactive tutorials: Hands-on guides for configuring and running tracking workflows.
- Example framework: A sample project demonstrating how to use ACTS algorithms in practice.

In addition, regular workshops and training sessions help new members start using ACTS in their experiments. New contributors are often mentored by experienced developers, ensuring knowledge transfer and continuous growth of the community.

## Tools

ACTS uses common tools to maintain quality and facilitate contributions:

- Version control: Git, with repositories on GitHub/GitLab for collaborative development.
- Continuous integration: Automated testing pipelines using GitHub Actions and GitLab CI.
- Documentation: Documentation written with Sphinx and published on ReadTheDocs.
- Build system: CMake for consistent compilation across platforms.
- Issue tracking: GitHub/GitLab issue trackers for transparent bug reports and feature requests.

These tools streamline development, ensure reliability, and make it easier for new users to adopt ACTS.

## FAIR & Open

ACTS adheres to FAIR principles. The code is publicly available under the Mozilla Public License 2.0 (MPL-2.0), allowing broad use and collaboration. Each release is archived with a DOI, so the software is easy to find and cite. ACTS supports standard data formats and geometry descriptions, which ensures it is interoperable with various experimental frameworks. By developing the toolkit in the open, ACTS fosters reuse across multiple research communities.

## Documentation

ACTS offers thorough documentation for both users and developers:

- User guides: Detailed instructions for installation, setup, and usage.
- Developer docs: Explanations of internal design, components, and APIs for contributors.
- Tutorials and examples: Step-by-step examples demonstrating common use cases.

The documentation is updated alongside the code to remain accurate and up-to-date. Documentation contributions are valued as highly as code contributions, reflecting the importance of good documentation for ACTS's usability.

## Sustainability

ACTS is sustained by a strong community and multiple funding sources. It benefits from institutional support (for example, CERN's EP R&D programme, the NSF-funded IRIS-HEP project in the US, the EU-funded AIDAInnova project, and CERN's Next Generation Triggers initiative). Having contributors from many different experiments means ACTS isn't dependent on any single group or grant. The project has clear governance and training practices to retain knowledge, which keeps ACTS resilient and ready to meet future needs.

## References

- ACTS GitHub Repository: <https://github.com/acts-project/acts>
- ACTS Official Documentation: <https://acts.readthedocs.io/>
- ACTS Project Website: <https://acts-project.github.io/>
- License: Mozilla Public License v2.0 (MPL-2.0)
- IRIS-HEP Project: <https://iris-hep.org/>
- Ai, X., Allaire, C., Calace, N. et al. A Common Tracking Software Project. Comput Softw Big Sci 6, 8 (2022). https://doi.org/10.1007/s41781-021-00078-8

