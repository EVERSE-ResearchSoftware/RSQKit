---
title: "Phoenix2"
search_exclude: false
description: "An ecosystem of minimalist, modular and extensible libraries for transverse topics in data acquisition and analysis software in C++, Python and Rust."
contributors: ["Vincent Pollet", "Thibaut Oprinsen"]
page_id: phoenix2
type: research_software_story
---

## The Problem
### Software design for long-term sustainability and maintainability

Science experiments are often build and operated over periods of several decades. During this time, computing hardware is regularly replaced every few years. Each new piece of hardware brings its lot of new features, deprecated usages and requires to adapt software to use it, let alone use it optimally. In fields such as data acquisition (DAQ) or high-performance computing (HPC) which are by nature close to the hardware, the cost of adapting software to new hardware can become unbearable if the software is not designed appropriately.

Unfortunately, the libraries of the DAQ or HPC ecosystems don't always make it easy to integrate them with little strings attached. For instance, the [boost libraries](https://www.boost.org/) implement many helpful tools such as a unit testing framework, argument parsing libraries, etc. that would be useful in a C++ research software. Unfortunately, the libraries are distributed as monolithic archives, so users have to decide between getting the whole stack even if they are only interested in a single feature, re-implement themselves the desired feature or live without it. In all cases the maintainability is hindered by the lack of modularity: either by unnecessary dependencies pinning the environment, by additional code to maintain or by worsened implementation.  
In the DAQ world, there are many message passing libraries one can use for data transfer. While all these libraries rely under the surface on unix sockets, they do not have a consistent API for users, therefore a research software carelessly integrating a library becomes dependent on the library. In 10, 20 or 30 years the research experiment may still operate, but the external messaging library may not be maintained, forcing the users to undergo an expensive update to switch to another solution. The maintainability is hindered by the lack of consistency and uniformity among similar libraries.

The phoenix libraries try to minimize the maintainability issues of long-term software by implementing an **ecosystem** of libraries: each functionality is expressed as an abstract API and the actual interaction with the hardware (or any underlying technology) are encapsulated into "backends" which can be easily replaced or exchanged. The purpose of this **modular** approach is to improve **maintainability**, **extensibility** and **reusability** of research software.

- provide modular and extensible solutions to data acquisition and analysis software
- provide general purpose utilities for research programs
- enable multi-language, multi-platform yet consistent and reproducible software and development environments
- improve software quality with extensive usage of continuous integration for testing, documentation, packaging and deployment

The phoenix libraries don't aim to solve each and every issue in DAQ and HPC software, but to provide a foundation for building high-quality and easily maintainable data acquisition and analysis software. Phoenix users typically don't need all the phoenix libraries for their usage, but may pick to use a few utilities (eg. C++ unit testing or CI/CD catalog) to help them develop and/or an application specific feature (eg. mockable socket abstraction) with a dedicated back-end matching their requirements. If the existing backends are not suitable, implementing and contributing a new one should take a minimal amount of time as only the backend must be written. The goal is to enable users to develop only what they need, while making it instantly re-usable for others, with as little strings attached as possible.

One particularly interesting aspect of the phoenix libraries is the possibility to develop one's software use "mock-up" back-ends. Let's say you are writing an analysis software and need to gather data from several detectors to analyse them together. Unfortunately your detectors are not build yet and won't be available before 5 years. By using the "mock" back-end, you are able to develop your software without committing _now_ to a solution. When the detectors are finally available, you will be able to switch to the most relevant solution at that time without effort, due to the back-end consistency! Even better: you will be able to test and benchmark all possible back-ends and decide, looking at measured numbers and not expected performances on future (currently non-existing) hardware!


## User Community
### Phoenix is completely open-source and free-licensed: anyone is welcomed to use and contribute!

The Phoenix libraries are primarily developed by engineers and researchers at [LAPP](https://www.lapp.in2p3.fr/) for their own and other developers usage. It is and will be published under free licenses and is currently hosted by the [IN2P3 gitlab](https://gitlab.in2p3.fr/CTA-LAPP/PHOENIX_LIBS2). Anyone is welcome to use it or contribute, either to the main repositories managed by LAPP or as a extension in your own repositories, under your control.

Phoenix intends to be a generic base layer for research software, providing reliable and modular libraries or executables that can be build upon by research experiments. Currently, the targeted users are the "big science" data acquisition and analysis software in particle physics and astronomy where the LAPP is involved. New users are however always welcome! As an example, the [CTAO](https://www.ctao.org/) real-time analysis will use the testing (mocks), serialization and data exchange phoenix libraries to implement its solution. The LAPP team is committed to phoenix long-term support to enable its usage by other long-running experiments.


## Technical Aspects

The phoenix libraries are aiming to **facilitate the development and improve the quality** of data acquisition and data analysis software. Therefore, they include some field specific tools for data exchange between processes, abstract socket API with build-in mock-ups, serialization, ... but also a lot of general purpose utilities for research software: testing, benchmarking, configuration and argument parsing, string manipulation, code generation... Phoenix also provides a complete CI/CD workflow ({% tool "gitlab-ci-cd" %}) for projects managed with {% tool "pixi" %}.

Thanks to its modular design, a user interested in a specific subset of the features can install only the required packages, keeping their environment lightweight. Phoenix packages are implemented in either `C++`, `Rust` and `python` and packaged with {% tool "pixi" %} to the platform and language agnostic `conda` package format. Packages are available for the `linux-64` and `linux-aarch64` platforms. Additional platforms could be added upon request.

Phoenix is a research software infrastructure tier set of libraries. It is being developed at [LAPP](https://www.lapp.in2p3.fr/) (Laboratoire d'Annecy de Physique des Particules) for over 6 years and will support long-term research experiments. Currently, Phoenix provides a suite of tools for:
- Data serialization
- Data exchange via sockets
- Program arguments and configuration parsing and validation
- Code generation
- Clock and time measurement
- single instruction multiple data (SIMD) programming using intrinsics
- Unit testing, benchmarking and memory analysis
- Continuous integration and deployment using {% tool "gitlab" %}


### Libraries and Systems
Phoenix is implemented in `C++`, `Rust`, and `python`. Each library is packaged with {% tool "pixi" %} to the `conda` format, enabling easy **multi-platform builds and language-agnostic installation**. This approach simplifies dependency management and deployment for users: one can create a working environment simply by running [`pixi install --frozen`](https://pixi.prefix.dev/latest/python/tutorial/#installation-pixi-install) in a phoenix repository. [`pixi global install`](https://pixi.prefix.dev/latest/reference/cli/pixi/global/install/#pixi-global-install) can be used to install a phoenix tool in a isolated environment available to the user everywhere on the machine, without requiring administrator privileges. As an example, `pixi global install -c https://prefix.dev/phoenix -c conda-forge rustyphoenixcodemeta` installs a tool to generate a {% tool "codemeta" %} file from a pixi manifest.

Phoenix packages mostly rely on the standard library of their language, but specific backend implementation often require additional dependencies (for instance the ZMQ socket backend requires [ZMQ](https://zeromq.org/)). All dependencies outside phoenix are taken from the [`conda-forge`](https://conda-forge.org/docs/) community-maintained distributions. {% tool "nanobind" %} is used to wrap C++ code to python for consistent multi-language interfaces.


## Software Practices
### Phoenix heavily leverages continuous integration and deployment best practices, and can help you do too!

Phoenix strives to follow robust software development practices and heavily leverages {% tool "gitlab-ci-cd" %} [components](https://docs.gitlab.com/ci/components/) and {% tool "pixi" %}[tasks](https://pixi.prefix.dev/dev/workspace/advanced_tasks/) to standardize and automatize as many development and maintenance tasks as possible.
- The entire codebase is **version-controlled**.
- **Continuous integration** validates the code, which is **thoroughly tested** by unit tests usually covering over 90% of the code.
- Phoenix uses a **commit convention** that enables automatic detection of new releases according to [semantic versioning](https://semver.org/). 
- Releases are built in CI/CD and deployed as `conda` packages and/or OCI containers, along with updated documentation. 
- A {% tool "renovate" %} bot continuously monitors and updates dependencies, ensuring the codebase remains up to date. Code review is strongly encouraged.
- Phoenix CI/CD is centralized in [CI/CD catalogs](https://gitlab.in2p3.fr/CTA-LAPP/PHOENIX_LIBS2/citoolkit) that are available for usage in your own repositories!


## Developer Community
### Research Software Community and beyond

Phoenix core developers are working at [LAPP](https://www.lapp.in2p3.fr/), with the goal to **support long-term research experiment** data acquisition and data analysis software by enabling the development of modular, extensible and maintainable solutions. Phoenix is currently being used by the [LST](https://lst.iac.es/) and [CTAO](https://www.ctao.org/) collaboration for its real-time stereo analysis. However, been completely open-source and free-licensed, as well as easily extensible, new usage or contribution are always possible.

New contributors are very welcome and can join by proposing merge requests to any repository, requesting access to the phoenix GitLab group or any specific repository. Contributions to the LAPP owned repositories are encouraged and discussed with collaborators, with the final decision resting with the core maintainers. Building upon Phoenix in external repositories under your control, for instance in your institution developer platform, is also encouraged and will be supported whenever possible.  
An overview of all Phoenix repositories is available [in this README](https://gitlab.in2p3.fr/CTA-LAPP/PHOENIX_LIBS2/PHOENIX2) ; the main documentation is hosted on [gitlab pages](https://cta-lapp.pages.in2p3.fr/PHOENIX_LIBS2/PHOENIX2/). Each repository has its own documentation hosted with {% tool "gitlab-pages" %} in addition to their `README`. New contributors can start by reading the documentation and tests, they are also welcome to reach out to the core maintainer via issues or mail.  
In order to work on a phoenix repository, only installing {% tool "pixi" %} is required: other tools and dependencies will be downloaded and installed in isolated environments when running {% tool "pixi" %}[tasks](https://pixi.prefix.dev/dev/workspace/advanced_tasks/).


## Tools
### Phoenix uses languages specific tools for quality/testing sometimes enhanced with custom tools

C++ phoenix projects make use of {% tool "ctest" %} to implement unit test. `CMake` utilities are provided by [PhoenixCMake](https://gitlab.in2p3.fr/CTA-LAPP/PHOENIX_LIBS2/PhoenixCMake). Python repositories use {% tool "pytest" %} and {% tool "ruff" %} for testing and linting. Rust repositories rely on {% tool "cargo" %}. 

All projects are packaged using {% tool "pixi" %} to the `conda` package format. {% tool "pixi" %} also ensures that the development and deployment environments are **reproducible** via the mandatory check-in of the lock files in source control. It also standardizes the most common development tasks such as building packages, running tests, rendering documentation...  
The packages are uploaded to 2 `conda` channels: the [phoenix channel](https://prefix.dev/channels/phoenix) hosts released, forever available versions, while the [phoenix-dev channel](https://prefix.dev/channels/phoenix-dev) hosts development versions that are eventually removed once merged in the stable distribution. In addition, containers are provided for applications and hosted in the projects container registries on {% tool "gitlab" %}. The projects documentation are written in `LaTeX` or `markdown`.

In addition, Phoenix provides some tools to help developing high quality software:
- arbitrary data serialization (used to write mock-ups files)
- built-in mock-up capability in Socket and Clocks enabling single-thread, latency-free integration tests.
- code generator for data classes from HDF5 or serialized format
- intrinsic abstractions for easier SIMD maintenance
- benchmarking tools to measure execution time of C++ routines
- Reporter tool aggregating results from {% tool "maqao" %}, {% tool "valgrind" %}, {% tool "malt" %} and benchmarks
- documentation generation from `LaTeX` or `markdown`
- {% tool "gitlab-ci-cd" %} catalog relying on {% tool "pixi" %}[tasks](https://pixi.prefix.dev/dev/workspace/advanced_tasks/) to centralize CI/CD definitions.


## FAIR & Open
### Phoenix strives to implement FAIR principles and open-source and free software

- **Findable**: Phoenix is [publicly available](https://gitlab.in2p3.fr/CTA-LAPP/PHOENIX_LIBS2) on the IN2P3 GitLab instance and {% tool "zenodo" %}.
- **Accessible**: The software can be cloned from GitLab ; releases versions can be download from GitLab releases or Zenodo. Documentation is included in the source code and publicly hosted with {% tool "gitlab-pages" %}. Phoenix packages are available on [public conda channels](https://prefix.dev/channels/phoenix) hosted at [prefix.dev](https://prefix.dev/channels) by the company developing {% tool "pixi" %}. To use the packages it is recommended to add `https://prefix.dev/phoenix` to your {% tool "pixi" %} or {% tool "conda" %} workspace channels.
- **Interoperable**: Phoenix is packaged in the `conda` format which supports many platforms and operating systems and allowing easy installation for users without administrative rights. {% tool "pixi" %}[tasks](https://pixi.prefix.dev/dev/workspace/advanced_tasks/) automatize environment creation and running development tasks.
- **Reusable**: Phoenix's modular design allows users to easily reuse any library. Dependencies are managed using {% tool "pixi" %}, enabling the creation of reproducible environments described in lock files.

Phoenix is licensed under the **CeCILL-C** license, granting users the freedom to copy, modify, and distribute the software.


## Documentation
### User Documentation is improving

The main entrypoint to phoenix documentation is [available via gitlab pages](https://cta-lapp.pages.in2p3.fr/PHOENIX_LIBS2/PHOENIX2/index.html). Each repository also contains a `README` and a dedicated documentation page hosted with {% tool "gitlab-pages" %} as well as documented tests.

All phoenix projects should have a detailed documentation for both users and developers of the libraries, including the API documentation generated from the code. Unfortunately, the current content of the documentation is lacking for some projects, and the maintainers are working to improve the situation. Until the situation improves, users are welcome to reach out to the maintainer to get the missing information.


## Sustainability
### Phoenix is maintained by permanent engineers and researchers at LAPP who commit to long-term support of research experiment software

Phoenix is sustained by a core team of software research engineers at LAPP, who are committed to its long-term maintenance and development. There are currently no threats to its continued development, which is actively progressing. In addition to the core team, additional developers can be funded by other sources, as is currently the case with the [OSCARS Starlight](https://oscars-project.eu/projects/starlight-stereo-telescopes-analysis-real-time-leading-edge-innovation-gamma-high) project.


## References
Phoenix has a community on Zenodo: [Phoenix2 Community](https://zenodo.org/communities/phoenix2).  

The [Phoenix socket design](https://zenodo.org/records/18798133) has been presented at the deRSE 2026 conference: [deRSE 2026](https://events.hifis.net/event/2945/contributions/21299/).
