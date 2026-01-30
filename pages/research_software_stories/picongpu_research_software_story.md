---
title: "PIConGPU - a fully relativistic 3D3V particle-in-cell code"
search_exclude: false
description: "PIConGPU is used to simulate nonlinear plasma physics, from laser plasma accelerators to astrophysics research."
contributors: ["Guido Juckeland"]
page_id: picongpu
type: research_software_story
---

## The Problem
### Simulating extreme laser-plasma physics for next-generation accelerators

PIConGPU is a particle-in-cell code used to simulate nonlinear plasma physics. 
It is primarily used for laser plasma acceleration, such as laser wakefield and target normal sheath acceleration, but it is also frequently applied to astrophysical scenarios, such as magnetic reconnection and shear surface instabilities in interstellar jets.
These extreme physical conditions require a fully relativistic approach and three-dimensional (3D) modeling of spatial coordinates and velocity space, which presents a substantial computational challenge. 
This software provides accurate, high-performance simulations that can run on modern supercomputing architectures, supporting experimental design and theoretical understanding in plasma physics research.
## User Community
### Collaborative development driven by physics and computer science experts

PIConGPU is primarily developed at the Helmholtz-Zentrum Dresden-Rossendorf (HZDR), where the team combines expertise from computer science and physics. 
The development of physics capabilities is primarily driven by students as part of their Ph.D. or master's thesis work. This creates a dynamic environment in which early-career researchers can contribute to the project while advancing their own research goals under the supervision of a senior computational physicist.
In parallel, RSEs (research software engineers) mainly drive workflow design, domain-specific coupling between the computer science domain and physics simulations, and overall code maintenance.

The development team consists of:
- A few computer scientists focused on software architecture and performance
- A larger group of physicists driving scientific requirements
- PhD and master's students as primary contributors of new features

Users of PIConGPU are mainly researchers simulating laser-driven particle acceleration. 
They tend to be advanced C++ users with strong computational backgrounds, capable of working within complex HPC environments and handling the sophisticated build requirements of the software.

The community maintains connection through online videos and onboarding documents, a Mattermost team with core users, and personnel exchange visits that facilitate knowledge transfer between institutions.

## Technical Aspects
### Modern C++ with extensive compilation infrastructure

PIConGPU is classified as Tier 1 Research Software Infrastructure (Services included), reflecting its maturity and the comprehensive support provided to users.

**Technical specifications:**
- **Language:** Modern C++20 for the source code, with Python bindings available for easier interaction
- **Codebase size:** Approximately 80k lines of code (including the PMacc library) plus roughly 55k lines of comments and documentation
- **Build system:** CMake for building and installation
- **Deployment:** Can ideally install on local machines if prerequisites are satisfied, but primarily targets HPC systems
- **Compilation characteristics:** Long compile times (~3+ minutes) for each setup due to heavy use of C++ templates for performance optimization
- **Parameter handling:** Simulation parameters are transported via CMake into the code, requiring recompilation when input parameters change

This compilation-time parameter binding allows aggressive compiler optimizations but creates a different workflow than traditional runtime configuration approaches.

### Libraries and Systems

PIConGPU builds on several key dependencies:

- **alpaka** (https://alpaka.readthedocs.io/): Core abstraction library enabling portability across different accelerators
- **CMake:** Build configuration and management
- **MPI:** Parallel execution across multiple nodes
- **Boost:** Essential C++ utilities and data structures
- **OpenPMD-api:** HPC IO abstraction library for parallel ADIOS2 or HDF5 

The focused dependency set reflects a deliberate strategy of relying on well-established, widely-available libraries rather than accumulating numerous smaller dependencies.

## Software Quality Practices
### Rigorous testing across thousands of hardware configurations

PIConGPU follows disciplined software engineering practices with comprehensive version control and contribution guidelines:

- **Version control:** Git, with the main repository hosted on GitHub
- **Contribution process:** Guidelines documented in CONTRIBUTING.md within the repository
- **Code review:** Changes reviewed before integration to maintain quality

The most distinctive aspect of PIConGPU's quality infrastructure is its extensive continuous integration setup. 
The CI workflow moves code from GitHub via GitLab.com to HZDR's local GitLab CI infrastructure, then pushes all pipeline results back to GitHub pull requests. 
This complex pipeline:

- Checks static code quality through linting and code style enforcement
- Compiles test cases for all supported combinations of hardware architectures, accelerators (GPUs), and libraries
- Generates hundreds of CI jobs per change
- Runs tests and validates output against expected results

The code also integrates with multiple HPC compiler and hardware vendor CI/CD test environments, serving as a real-world stress test for their tools.

## Developer Community
### Structured support for physicists learning computational methods

The PIConGPU project provides multiple resources to help newcomers:

- Online videos and comprehensive onboarding documents introducing the software's purpose and architecture
- A Mattermost team where developers and users can ask questions and share solutions
- Personnel exchange visits allowing researchers to work directly with core developers

The typical user journey starts with learning to run existing simulation setups and modify parameters. 
As users gain experience, they progress to adapting simulation geometries and incorporating new initial conditions. 
Advanced users eventually contribute new physical models or extend the code's capabilities for their specific research needs.

## Tools
### Performance profiling across diverse accelerator architectures

PIConGPU works well with industry-standard performance profiling tools including:

- **NVIDIA Nsight** for NVIDIA GPUs
- **AMD Omniperf** for AMD GPUs
- **Score-P** for general parallel performance analysis

The highly asynchronous nature of particle-in-cell algorithms makes profiling challenging, as GPU operations may overlap with CPU work and communication in complex ways. 
Despite these challenges, detailed profiling helps developers identify bottlenecks and optimize critical code paths.

## FAIR & Open
### Transparent development with strong licensing and citability

PIConGPU exemplifies FAIR research software principles:

- **Repository:** Openly available on GitHub (https://github.com/ComputationalRadiationPhysics/picongpu)
- **License:** GPLv3+ for the main code, LGPLv3+ for libraries, and CC-BY 4.0 for documentation
- **Citeable:** Yes, with DOI 10.5281/zenodo.591746
- **Discussion community:** Via GitHub Issues for transparent community engagement
- **Software Quality Checklist:** Commit Rules documented at https://github.com/ComputationalRadiationPhysics/picongpu/blob/dev/docs/COMMIT.md

Development happens openly, with discussions about features, bugs, and design decisions occurring in public GitHub issues. The GPL licensing ensures that improvements benefit the entire community rather than being captured in proprietary forks.

## Documentation
### Multi-level resources serving diverse user needs

PIConGPU provides documentation organized for different audiences:

- **User documentation:** Installation guides, tutorials, and usage examples
- **Developer documentation:** Code structure explanations and contribution guidelines
- **Maintainer documentation:** Release processes and long-term decisions on code structure

The primary documentation lives at https://picongpu.readthedocs.io, using Read the Docs for versioned, searchable access. 
Documentation is mainly written and maintained by the core development team, with contributions often arriving as part of pull requests when new features are added.

## Sustainability
### Institutional commitment ensures long-term viability

PIConGPU benefits from stable institutional support:

**Funding model:**
- Part of Helmholtz base-funded research activities at HZDR
- Permanently funded RSEs serving as maintainer, ensuring continuity beyond individual researchers
- Further RSEs funded via European project for HPC and plasma research

**Governance:**
- Project builds on well-established FOSS community practices
- Development guided by experienced researchers and RSEs who maintain overall architecture
- Benefits from thesis-driven development while maintaining coherent long-term vision

**Recognition:**
- Author and contributor lists maintained in the software repository
- Software authors for specific scientific use cases listed as authors on academic publications

The combination of permanent funding, experienced maintainers, and established community practices positions PIConGPU well for long-term sustainability as computing architectures and research needs evolve.

## References

- PIConGPU GitHub Repository: https://github.com/ComputationalRadiationPhysics/picongpu
- Main publication: Bussmann, M., et al. (2013). Radiative signatures of the relativistic Kelvin-Helmholtz instability. https://doi.org/10.1145/2503210.2504564
- PIConGPU Documentation: https://picongpu.readthedocs.io
- Software Citation: DOI 10.5281/zenodo.591746

