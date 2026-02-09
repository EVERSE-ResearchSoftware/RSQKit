---
title: "Research Software Story - alpaka"
search_exclude: false
description: "alpaka is a header-only C++ template library that enables writing platform and performance portable applications. It can use CPUs with sequential and thread parallel code, GPUs via multiple programming paradigms and also FPGAs."
contributors: ["Guido Juckeland", "Srobona Ghosh"]
page_id: alpaka
type: research_software_story
---

## The Problem
### Achieving performance portability in an increasingly heterogeneous HPC landscape

alpaka is a header-only C++ template library that enables writing [platform and performance portable applications][ALPAKA_GITHUB]. 
It can use CPUs with sequential and thread parallel code, GPUs via multiple programming paradigms. 
The library addresses the fundamental challenge facing HPC developers: how to write high-performance code once and run it efficiently across diverse hardware platforms without maintaining separate implementations for each architecture.

Traditional approaches required separate code paths, within the user application, for NVIDIA GPUs ([CUDA][CUDA]), [AMD GPUs][HIP] ([HIP/ROCm][HIP]), [Intel GPUs][SYCL] ([oneAPI/SYCL][SYCL]), and multicore x86/ARM/RISCV CPUs ([OpenMP][OPENMP]). 
This multiplication of code creates enormous maintenance burdens and makes verification difficult. 
alpaka solves this by providing a single abstraction layer where developers write algorithms once using portable interfaces, then compile to native code for different hardware backends.

## User Community
### Joint development between HZDR and CERN serving the HPC community

alpaka is jointly developed at the [Helmholtz-Zentrum Dresden-Rossendorf (HZDR)][HZDR] and [CERN][CERN] (CMS experiment). 
The development team combines computer scientists and physicists, with work mainly driven through PhD and master's thesis projects alongside requirements from CERN's experimental collaborations.

**Development team composition:**
- HZDR and CMS are focused on core library architecture and performance optimization
- CMS collaboration developers at CERN driving requirements for high-energy physics data processing
- HZDR taking care of plasma physics simulation requirements
- HZDR is developing features based on external user requirements from [DLR][DLR] and [HZB][HZB]
- HZDR is developing the testing strategies and infrastructure to guarantee the code quality
- PhD and master's students contributing focused improvements and new features

**User base characteristics:**
- Advanced [C++][LANGUAGE_CPP] programmers working in HPC environments
- Researchers needing codes to work across different computing centers with varying hardware
- CMS experiment and other scientific collaborations requiring performance portability
- Users comfortable with parallel programming concepts and template-heavy C++ code

The community maintains connection through [online videos and onboarding documents][ALPAKA_DOCS], a [Mattermost][TOOL_MATTERMOST] team with core users, and personnel exchange visits between institutions.

## Technical Aspects
### Header-only C++ template library for compile-time code generation

alpaka is classified as Tier 3 Research Software Infrastructure (Services included), reflecting its critical enabling role for other scientific applications.

**Technical specifications:**
- **Language:** Modern [C++20][LANGUAGE_CPP20] for expressive template metaprogramming
- **Codebase size:** Approximately 45k lines of code (30k in core library headers) and 10k lines of comments
- **Architecture:** Header-only library that doesn't "run" but translates at compile time
- **Compilation approach:** Compiler processes templates to generate hardware-specific code ({% tool "cuda" %}, {% tool "hip" %}/{% tool "rocm" %}, {% tool "openmp" %}, etc.)
- **Performance:** Zero runtime overhead compared to hand-written platform-specific code

When developers write alpaka-based algorithms and compile with a specific backend selected, the compiler produces native code for that platform. 
Compiling the same source with different backends produces different optimized implementations from a single codebase.

### Libraries and Systems

alpaka's dependencies vary based on the selected compilation backend:

- **{% tool "cuda" %}:** Required when compiling for NVIDIA GPUs
- **[HIP][HIP]/{% tool "rocm" %}:** Required when targeting AMD GPUs
- **[OneAPI SYCL][SYCL]:** Required for Intel GPUs or optionally CPUs
- **{% tool "openmp" %}:** Used for thread-parallel CPU execution
- **[TBB (Threading Building Blocks)][TBB]:** Alternative for task-based CPU parallelism

This backend architecture means deploying alpaka-based code requires only the specific toolchain relevant to the target hardware, keeping deployment practical despite broad platform support.

## Software Quality Practices
### Comprehensive testing across thousands of hardware configurations

alpaka follows disciplined development practices essential for a library supporting such diverse platforms:

- **Version control:** {% tool "git" %} with the main repository on [GitHub][ALPAKA_GITHUB]
- **Contribution guidelines:** Detailed guidelines in [CONTRIBUTING.md][ALPAKA_CONTRIBUTING] maintain consistency across contributors
- **Code review:** Mandatory peer review before merging changes
- **Coding standards:** Comprehensive [guidelines documented][ALPAKA_STYLE] for maintaining code quality

The most remarkable quality practice is the extensive continuous integration infrastructure testing every change across thousands of configurations. 
The CI system routes code from {% tool "github" %} through [GitLab.com][GITLAB] to HZDR's local GitLab CI infrastructure with access to diverse hardware accelerators. 
Each change triggers:

- Static code quality checks through linting
- Compilation testing across all supported C++ compilers, hardware backends, and configurations
- Test suite execution verifying correctness on each platform

Results push back to GitHub pull requests, providing immediate feedback about cross-platform compatibility. 
The code also integrates into multiple HPC compiler vendor and hardware manufacturer CI/CD test environments.

## Developer Community
### Individualized onboarding for template metaprogramming expertise

Onboarding new alpaka developers requires attention to the specialized C++ template metaprogramming knowledge needed to work effectively with the library. 
The process is highly individualized, tailored to each contributor's background and the specific areas where they'll work.

**Resources for developers:**
- Online videos introducing alpaka's architecture and design philosophy
- [Written documentation][ALPAKA_DOCS] explaining the template machinery
- [Mattermost][TOOL_MATTERMOST] team for real-time support from experienced developers
- Personnel exchange visits for intensive knowledge transfer through pair programming

**Typical user journey:**
New users typically start by adapting existing code from one platform (e.g., {% tool "cuda" %}) to use alpaka's portable interfaces. 
They begin by compiling only for familiar backends to verify correctness, then experiment with other platforms while comparing performance and debugging platform-specific issues.

## Tools
### Performance profiling across diverse accelerator platforms

alpaka works well with standard profiling tools for various platforms:

- **[NVIDIA Nsight][NVIDIA_NSIGHT]** for NVIDIA GPU performance analysis
- **[AMD Omniperf][AMD_OMNIPERF]** for AMD GPU optimization
- **[Score-P][SCOREP]** for general parallel performance analysis

Profiling can be challenging due to the highly asynchronous nature of GPU execution and complex control flow from template-based abstractions. 
The development team uses these tools to verify memory access patterns are efficient and that kernel launches don't introduce unnecessary overhead.

Like PIConGPU, alpaka has been incorporated into compiler vendor and hardware manufacturer testing environments, where it serves as a stress test for C++ template implementations and optimization capabilities.

## FAIR & Open
### Open development supporting collaborative cross-institution research

alpaka adheres to the [FAIR principles for research software][FAIR_PRINCIPLES]:

* **Findable**: The code is openly available on [GitHub][ALPAKA_GITHUB] with clear versioning, and releases are archived with assigned DOIs for academic referencing.

* **Accessible**: Core licensed under [MPLv2 (Mozilla Public License v2.0)][LICENSE_MPL2], examples under [ISC (Internet Systems Consortium)][LICENSE_ISC] allowing incorporation into projects with different licensing requirements; documentation under [CC-BY 4.0][LICENSE_CCBY].

* **Interoperable**: Designed to work seamlessly with standard HPC frameworks and supports multiple hardware backends ({% tool "cuda" %}, {% tool "hip" %}, {% tool "openmp" %}, [SYCL][SYCL]), enabling integration across diverse computing environments.

* **Reusable**: alpaka provides well-documented, tested components with comprehensive [coding guidelines][ALPAKA_STYLE] and clear [contribution process][ALPAKA_CONTRIBUTING], enabling reuse and easy adaptation across multiple research projects.

Development happens openly with features, architectural decisions, and bug reports discussed in public [GitHub Issues][ALPAKA_ISSUES]. 
The MPLv2 licensing ensures the library remains free and open while accommodating use by large experimental collaborations with complex software licensing requirements.

## Documentation
### Multi-level resources for diverse technical audiences

alpaka documentation is organized to serve different user groups:

- **Conceptual overviews:** Explaining the programming model and abstraction design
- **Installation guides:** Configuration for different backends and integration into projects
- **Tutorials:** Demonstrating common usage patterns through concrete examples
- **Developer documentation:** Architecture explanations and contribution guidance
- **API reference:** Technical specifications for library interfaces

The primary documentation lives at <https://alpaka.readthedocs.io> using [Read the Docs][READTHEDOCS] for versioned access. 
Documentation is mainly written and maintained by the core development team, with contributions often arriving as part of pull requests introducing new features.

## Sustainability
### Institutional funding and community governance ensure long-term evolution

alpaka's sustainability model supports evolution over multi-decade timescales:

**Funding and staffing:**
- Part of Helmholtz base-funded research activities at HZDR
- Permanently funded RSE as maintainer, ensuring continuity
- Coordination between HZDR and CERN ensures alignment with both general HPC and experimental collaboration needs

**Governance:**
- Project builds on well-established FOSS community practices
- Guidance from experienced researchers and RSEs maintains coherent architecture
- Thesis-driven development provides fresh contributions while experienced maintainers preserve long-term vision

**Recognition:**
- Author and contributor lists maintained in the software repository
- Software authors for specific scientific applications listed as co-authors on academic publications
- Citeable DOI enables proper acknowledgment in publications

The combination of institutional support, dual-institution governance, and established community practices positions alpaka well for continued evolution as hardware platforms and programming models advance.

## References

- alpaka GitHub Repository: <https://github.com/alpaka-group/alpaka>
- Main publication: Matthes, A., et al. (2016). Tuning and optimization for a variety of many-core architectures without changing a single line of implementation code using the alpaka library. <https://doi.org/10.1109/IPDPSW.2016.50>
- alpaka Documentation: <https://alpaka.readthedocs.io>
- Coding Guidelines: <https://alpaka.readthedocs.io/en/latest/dev/style.html>
- Software Citation: [DOI 10.5281/zenodo.595380](https://doi.org/10.5281/zenodo.595380)

<!-- External link definitions -->
[HZDR]: https://www.hzdr.de/
[CERN]: https://home.cern/
[DLR]: https://www.dlr.de/
[HZB]: https://www.helmholtz-berlin.de/
[LANGUAGE_CPP]: https://en.cppreference.com/w/cpp
[LANGUAGE_CPP20]: https://en.cppreference.com/w/cpp/20
[TOOL_MATTERMOST]: https://mattermost.com/
[CUDA]: https://developer.nvidia.com/cuda-toolkit
[HIP]: https://rocm.docs.amd.com/projects/HIP/en/latest/
[SYCL]: https://www.khronos.org/sycl/
[OPENMP]: https://www.openmp.org/
[TBB]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/onetbb.html
[ALPAKA_GITHUB]: https://github.com/alpaka-group/alpaka
[ALPAKA_CONTRIBUTING]: https://github.com/alpaka-group/alpaka/blob/develop/CONTRIBUTING.md
[ALPAKA_STYLE]: https://alpaka.readthedocs.io/en/latest/dev/style.html
[ALPAKA_ISSUES]: https://github.com/alpaka-group/alpaka/issues
[ALPAKA_DOCS]: https://alpaka.readthedocs.io
[GITLAB]: https://gitlab.com
[NVIDIA_NSIGHT]: https://developer.nvidia.com/nsight-systems
[AMD_OMNIPERF]: https://rocm.docs.amd.com/projects/omniperf/en/latest/
[SCOREP]: https://www.vi-hps.org/projects/score-p/
[FAIR_PRINCIPLES]: https://www.nature.com/articles/s41597-022-01710-x
[LICENSE_MPL2]: https://www.mozilla.org/en-US/MPL/2.0/
[LICENSE_ISC]: https://opensource.org/license/isc-license-txt
[LICENSE_CCBY]: https://creativecommons.org/licenses/by/4.0/
[READTHEDOCS]: https://readthedocs.org/
