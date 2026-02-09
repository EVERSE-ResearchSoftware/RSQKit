---
title: "Research Software Story - GreenPhysECS"
description: "Applying ECS to Physics Simulation with Energy Tracking"
contributors: ["Michael Sparks"]
page_id: greenphysecs_research_software_story
type: research_software_story
---

## The Problem

### Applying ECS to physics simulation to explore tractable parallelism

Physics workloads are often [embarrassingly parallel][EMBARASSINGLY_PARALLEL], yet [parallel programming][PARALLEL_PROGRAMMING] remains difficult in practice.
Many early career researchers default to highly linear simulation code that is hard to port to [multi-core][MULTICORE] or [GPU][GPU] environments later.
The [Entity Component System][ECS_WIKIPEDIA] (ECS) model is widely used in game development for concurrent and data-parallel simulation, but its applicability to research physics problems remains largely unexplored.

The software addresses the question: **can ECS make building parallel physics simulations simpler for novices**, and if so, does this make such simulations more portable to future GPU-based or [cluster-based][CLUSTER_COMPUTING] environments? In the absence of this work, the status quo of linear simulation code would persist, and the potential architectural benefits of ECS to research computing would remain untested.

## User Community

### Developed through supervised MPhys project work with future-facing research users

The software was developed within the [University of Manchester][UNIMAN] MPhys projects programme within the [Physics and Astronomy][PHYSMAN] dept.
Two MPhys students selected this project and collaborated on development, with assessment remaining individual.
A [Senior Research Software Engineer][MS_SRSE] (SRSE) supervised and directed the technical environment, maintained the repository and containerised build system, and provided infrastructure such as the energy measurement workflow.

Current direct “users” are the students themselves, whose role is to build working simulations to answer the overarching question of ECS usefulness.
Potential future users include physicists, simulation developers, or research computing practitioners interested in exploring new architectural approaches for data-parallel scientific software.
The [containerised][CONTAINIZATION] pattern also makes the work relevant to research software mentors supervising heterogeneous student cohorts.

## Technical Aspects

The software is a [C++20 codebase][CPP_20] providing two libraries: a snapshot of the [Flecs ECS framework][FLECS_DEV] (v4.1.1) and a small [energy tracking library][CCENERGY] based on Intel’s RAPL interface.
It includes a [Docker-based][DOCKER] [containerised][CONTAINIZATION] build and runtime environment, allowing consistent execution across Linux, macOS, and Windows (via WSL).
Example simulations demonstrate ECS usage with different physics strategies.

Physics domains explored include simple harmonics (for bootstrapping and confidence building) and fluid systems.
While ECS is inherently concurrent and data-parallel, the project is currently single-threaded to reduce cognitive load for novice developers.
Multi-CPU and GPU execution are intentionally deferred.

Key constraints include: (i) physics domain choice, (ii) teaching and time constraints of an MPhys project, (iii) limited C++ experience among students, (iv) no control over student operating systems, (v) reproducibility needs, and (vi) batch-mode execution for energy tracking.
Students run their work locally, generate runs, and request energy measurement, which occurs on a dedicated SRSE-operated Linux machine in offline batch mode.

### Libraries and Systems

The container targets [Ubuntu 24.04.3 LTS][UBUNTU], using **g++ 13.3**, **GNU make 4.3**, and standard Linux build tooling.
The energy subsystem uses [RAPL][RAPL] for measurement.
On macOS and Linux, key dependencies are **git** and **docker**; on Windows, **WSL** is additionally required.

The [Flecs documentation][FLECS_DOCUMENTATION] is relied upon for ECS concepts, while the build infrastructure and examples provide onboarding for simulation work.
No interoperability with external HPC schedulers or GPU libraries exists at this stage, though batch-style execution makes eventual scheduler integration natural.

## Software Practices

### Lean sketch-to-example development with open collaboration conventions

Development follows a lean **“sketches → examples → (optional) infrastructure”** model adapted from the SRSE’s *[Managing Creativity][MANAGING_CREATIVITY]* workflow.
Each developer has a personal area under [Sketches/][SKETCHES_DIR] for free experimentation.
Working sketches may be promoted to [Examples/][EXAMPLES_DIR] when they have demonstrated usefulness.
[Pull requests][PRS] are required for changes to shared infrastructure. ([Older PRs][PRS_OLDER])

Weekly meetings combine stand-ups with action learning sets, captured in shared notes structured as: Agenda, Progress, Admin/Discussion Planning, Discussion Points, and AOB.
Each attendee reports: Done/Doing/Next, Blocked, Wins, and On My Mind.
Discussion points are extracted from these entries and scheduled according to project needs and assessment timelines.

Informal norms include:

* working code is preferred over perfection
* share all work, including dead-ends, to surface reasoning
* PRs for shared components
* containerisation for reproducibility
* energy measurement via batch runs on a dedicated machine

Two releases have occurred: one at end of semester, and a second after consolidation of experiments into curated examples.
No CI/CD or automated tests currently exist; correctness is established by comparing expected versus observed simulation behaviour.

## Developer Community

### Early adopter experience via teaching, with experiential onboarding

New contributors begin by installing {% tool "docker" %} , {% tool "git" %} , and **make**, cloning the repository, and running `make docker` to build the environment.
They are then given a [Sketches area][SKETCHES_DIR] and shown how to copy the build infrastructure to create their first simulation.

Initial “wins” include running multi-step simulations and scaling entity counts.
Students often lack C++ and git/GitHub experience, so supervision time is used to teach practical git usage (staging, local vs remote, branches, tags, and PRs as communication tools).
Early examples include a minimal Flecs demo, a gravity simulation rendered to console in a toroidal space, and a version augmented with energy tracking.
Experienced developers would require less handholding.

## Tools

### Minimal tooling appropriate to early exploration stage

Primary tools are **git**, **GitHub**, and **PRs** for collaboration and visibility.
Documentation is produced using **Markdown \+ Pandoc**, with support for generating PDFs for writeups and presentations.
Debugging is currently print/log based, writing traces to an `output/` directory for visualisation.
Each developer uses their own editor (e.g., kate, VSCode).
Future expected tooling includes **gdb**, a testing framework, and eventually **CI/CD**, linters, and formatters if the project continues beyond exploratory status.

## FAIR & Open

### Public codebase with planned archival and permissive licensing

**Findable**

* Public repository under a named organisational GitHub: [UofM-Green-Compute/GreenPhysECS][GREENPHSECS_GITHUB]
* Discoverable through GitHub; not yet indexed in discipline-specific venues
* Future discoverability via [Zenodo][ZENODO] and publications is planned

**Accessible**

* Code is fully accessible to the [public via GitHub][GREENPHSECS_GITHUB]
* Contributions accepted via [Pull Requests][PRS], including to [Sketches][SKETCHES_DIR]

**Interoperable**

* Interoperability is not in scope for this phase  
* Build infrastructure is reusable for independent ECS-based simulation projects

**Reusable**

* Code intended to be licensed under Apache-2 (licence file pending)
* Build environment and workflow practices are reusable beyond physics
* Documentation and onboarding notes expected to expand in Phase 2

## Documentation

### Bootstrap documentation with private notes and examples for early contributors

Documentation is sparse.
Inline code documentation exists, and a `docs/` directory provides [bootstrap build guidance][BUILD_BOOTSTRAP].
Students’ lab books and reports (private) contain detailed reasoning and development history.
Additional documents include: build instructions, a [git][GIT_CRIBSHEET]/[GitHub][GITHUB_CRIBSHEET] cribsheet, Pandoc notes, and a detailed [“gravity presentation”][GRAVITY_EXAMPLE_PRESENTATION] explaining a concrete physics implementation strategy.
[Flecs documentation][FLECS_DOCUMENTATION] is relied on for ECS semantics.
Onboarding documentation is expected to grow during the next project phase.

## Sustainability

### Stewards, risks, continuity, and future academic trajectory

The project is active only when students choose it.
The SRSE maintains the repository, build environment, and energy subsystem.
Funding is internal and tied to teaching, with no external support.
Sustainability depends on future cohort interest and the central research question: **if ECS proves not useful, further investment is unnecessary**.

Risks include: knowledge loss without published outputs, dependence on SRSE stewardship, and external dependencies disappearing (e.g., the original energy library vanished from GitHub at project start, necessitating an in-house alternative).
Alignment with [Green Compute][GREEN_COMPUTE] and [EVERSE][EVERSE] supports both carbon-aware research computing and software quality practices.
Future plans include a [Zenodo][ZENODO] snapshot, publications, exemplars, and potentially tutorial or video materials illustrating the development model and physics techniques.


## References

* GreenPhysECS repository: <https://github.com/UofM-Green-Compute/GreenPhysECS/>
* Managing Creativity presentation, PyCon UK 2007: <https://doi.org/10.5281/zenodo.17969796>
* Flecs ECS framework: <https://www.flecs.dev/>
* Pandoc document system: <https://pandoc.org/>
* AtomECS paper: <https://arxiv.org/abs/2105.06447>
* AtomECS repository: <https://github.com/TeamAtomECS/AtomECS>

<!-- External References embedded as links -->

[ATOMECS_PAPER]: https://arxiv.org/abs/2105.06447
[ATOMECS_GITHUB]: https://github.com/TeamAtomECS/AtomECS
[BUILD_BOOTSTRAP]: https://github.com/UofM-Green-Compute/GreenPhysECS/blob/main/docs/building-the-codebase.md
[CCENERGY]: https://github.com/UofM-Green-Compute/GreenPhysECS/tree/main/include/ccenergy
[CLUSTER_COMPUTING]: https://en.wikipedia.org/wiki/Computer_cluster
[CONTAINIZATION]: https://en.wikipedia.org/wiki/Containerization_(computing)
[CPP_20]: https://en.wikipedia.org/wiki/C%2B%2B20
[DOCKER]: https://www.docker.com/
[ECS_WIKIPEDIA]: https://en.wikipedia.org/wiki/Entity_component_system
[EMBARASSINGLY_PARALLEL]: https://www.freecodecamp.org/news/embarrassingly-parallel-algorithms-explained-with-examples/
[EVERSE]: https://everse.software/
[EXAMPLES_DIR]: https://github.com/UofM-Green-Compute/GreenPhysECS/tree/main/examples
[FLECS_DEV]: https://www.flecs.dev/flecs/
[FLECS_DOCUMENTATION]: https://www.flecs.dev/flecs/md_docs_2Docs.html
[GIT_CRIBSHEET]: https://github.com/UofM-Green-Compute/GreenPhysECS/blob/main/docs/git-instructions.md
[GITHUB_CRIBSHEET]: https://github.com/UofM-Green-Compute/GreenPhysECS/blob/main/docs/getting-to-grips-with-git.md
[GPU]: https://en.wikipedia.org/wiki/Graphics_processing_unit
[GREEN_COMPUTE]: https://github.com/UofM-Green-Compute/
[GREENPHSECS_GITHUB]: https://github.com/UofM-Green-Compute/GreenPhysECS
[GRAVITY_EXAMPLE_PRESENTATION]: https://github.com/UofM-Green-Compute/GreenPhysECS/blob/main/Sketches/MPS/starter/docs/gravity_presentation/presentation.md
[MANAGING_CREATIVITY]: https://doi.org/10.5281/zenodo.17969796
[MULTICORE]: https://en.wikipedia.org/wiki/Multi-core_processor
[MS_SRSE]: https://orcid.org/0009-0001-3059-0000
[PARALLEL_PROGRAMMING]: https://en.wikipedia.org/wiki/Parallel_computing
[PHYSMAN]: https://www.physics.manchester.ac.uk/
[PRS]: https://github.com/UofM-Green-Compute/GreenPhysECS/pulls
[PRS_OLDER]: https://github.com/UofM-Green-Compute/flecs-in-docker/pulls
[SKETCHES_DIR]: https://github.com/UofM-Green-Compute/GreenPhysECS/tree/main/Sketches
[UNIMAN]: https://www.manchester.ac.uk/
[ZENODO]: https://zenodo.org/

