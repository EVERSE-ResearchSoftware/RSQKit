---
title: "Research Software Story - GreenPhysECS"
description: "Applying ECS to Physics Simulation with Energy Tracking"
contributors: ["Michael Sparks"]
page_id: greenphysecs_research_software_story
type: research_software_story
---

## **The Problem**

### **Applying ECS to physics simulation to explore tractable parallelism**

Physics workloads are often embarrassingly parallel, yet parallel programming remains difficult in practice.
Many early career researchers default to highly linear simulation code that is hard to port to multi-core or GPU environments later.
The Entity Component System (ECS) model is widely used in game development for concurrent and data-parallel simulation, but its applicability to research physics problems remains largely unexplored.

The software addresses the question: **can ECS make building parallel physics simulations simpler for novices**, and if so, does this make such simulations more portable to future GPU-based or cluster-based environments? In the absence of this work, the status quo of linear simulation code would persist, and the potential architectural benefits of ECS to research computing would remain untested.

## **The Community**

### **Developed through supervised MPhys project work with future-facing research users**

The software was developed within the University of Manchester MPhys projects programme.
Two MPhys students selected this project and collaborated on development, with assessment remaining individual.
A Senior Research Software Engineer (SRSE) supervised and directed the technical environment, maintained the repository and containerised build system, and provided infrastructure such as the energy measurement workflow.

Current direct “users” are the students themselves, whose role is to build working simulations to answer the overarching question of ECS usefulness.
Potential future users include physicists, simulation developers, or research computing practitioners interested in exploring new architectural approaches for data-parallel scientific software.
The containerised pattern also makes the work relevant to research software mentors supervising heterogeneous student cohorts.

## **Technical Aspects**

The software is a **C++20 codebase** providing two libraries: a snapshot of the **Flecs ECS framework (v4.1.1)** and a small **energy tracking library** based on Intel’s RAPL interface.
It includes a **Docker-based containerised build and runtime environment**, allowing consistent execution across Linux, macOS, and Windows (via WSL).
Example simulations demonstrate ECS usage with different physics strategies.

Physics domains explored include simple harmonics (for bootstrapping and confidence building) and fluid systems.
While ECS is inherently concurrent and data-parallel, the project is currently single-threaded to reduce cognitive load for novice developers.
Multi-CPU and GPU execution are intentionally deferred.

Key constraints include: (i) physics domain choice, (ii) teaching and time constraints of an MPhys project, (iii) limited C++ experience among students, (iv) no control over student operating systems, (v) reproducibility needs, and (vi) batch-mode execution for energy tracking.
Students run their work locally, generate runs, and request energy measurement, which occurs on a dedicated SRSE-operated Linux machine in offline batch mode.

### **Libraries and Systems**

The container targets **Ubuntu 24.04.3 LTS**, using **g++ 13.3**, **GNU make 4.3**, and standard Linux build tooling.
The energy subsystem uses **RAPL** for measurement.
On macOS and Linux, key dependencies are **git** and **docker**; on Windows, **WSL** is additionally required.

The Flecs documentation is relied upon for ECS concepts, while the build infrastructure and examples provide onboarding for simulation work.
No interoperability with external HPC schedulers or GPU libraries exists at this stage, though batch-style execution makes eventual scheduler integration natural.

## **Software Practices**

### **Lean sketch-to-example development with open collaboration conventions**

Development follows a lean **“sketches → examples → (optional) infrastructure”** model adapted from the SRSE’s *Managing Creativity* workflow.
Each developer has a personal area under `Sketches/` for free experimentation.
Working sketches may be promoted to `Examples/` when they have demonstrated usefulness.
Pull requests are required for changes to shared infrastructure.

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

## **Community**

### **Early adopter experience via teaching, with experiential onboarding**

New contributors begin by installing **docker**, **git**, and **make**, cloning the repository, and running `make docker` to build the environment.
They are then given a Sketches area and shown how to copy the build infrastructure to create their first simulation.

Initial “wins” include running multi-step simulations and scaling entity counts.
Students often lack C++ and git/GitHub experience, so supervision time is used to teach practical git usage (staging, local vs remote, branches, tags, and PRs as communication tools).
Early examples include a minimal Flecs demo, a gravity simulation rendered to console in a toroidal space, and a version augmented with energy tracking.
Experienced developers would require less handholding.

## **Tools**

### **Minimal tooling appropriate to early exploration stage**

Primary tools are **git**, **GitHub**, and **PRs** for collaboration and visibility.
Documentation is produced using **Markdown \+ Pandoc**, with support for generating PDFs for writeups and presentations.
Debugging is currently print/log based, writing traces to an `output/` directory for visualisation.
Each developer uses their own editor (e.g., kate, VSCode).
Future expected tooling includes **gdb**, a testing framework, and eventually **CI/CD**, linters, and formatters if the project continues beyond exploratory status.

## **FAIR & Open**

### **Public codebase with planned archival and permissive licensing**

**Findable**

* Public repository under a named organisational GitHub: `UofM-Green-Compute/GreenPhysECS`  
* Discoverable through GitHub; not yet indexed in discipline-specific venues  
* Future discoverability via Zenodo and publications is planned

**Accessible**

* Code is fully accessible to the public via GitHub  
* Contributions accepted via PRs, including to Sketches

**Interoperable**

* Interoperability is not in scope for this phase  
* Build infrastructure is reusable for independent ECS-based simulation projects

**Reusable**

* Code intended to be licensed under Apache-2 (licence file pending)  
* Build environment and workflow practices are reusable beyond physics  
* Documentation and onboarding notes expected to expand in Phase 2

## **Documentation**

### **Bootstrap documentation with private notes and examples for early contributors**

Documentation is sparse.
Inline code documentation exists, and a `docs/` directory provides bootstrap build guidance.
Students’ lab books and reports (private) contain detailed reasoning and development history.
Additional documents include: build instructions, a git/GitHub cribsheet, Pandoc notes, and a detailed “gravity presentation” explaining a concrete physics implementation strategy.
Flecs documentation is relied on for ECS semantics.
Onboarding documentation is expected to grow during the next project phase.

## **Sustainability**

### **Stewards, risks, continuity, and future academic trajectory**

The project is active only when students choose it.
The SRSE maintains the repository, build environment, and energy subsystem.
Funding is internal and tied to teaching, with no external support.
Sustainability depends on future cohort interest and the central research question: **if ECS proves not useful, further investment is unnecessary**.

Risks include: knowledge loss without published outputs, dependence on SRSE stewardship, and external dependencies disappearing (e.g., the original energy library vanished from GitHub at project start, necessitating an in-house alternative).
Alignment with **Green Compute** and **EVERSE** supports both carbon-aware research computing and software quality practices.
Future plans include a Zenodo snapshot, publications, exemplars, and potentially tutorial or video materials illustrating the development model and physics techniques.

## **References**

* GreenPhysECS repository: [https://github.com/UofM-Green-Compute/GreenPhysECS/](https://github.com/UofM-Green-Compute/greenphysecs)  
* Managing Creativity presentation, PyCon UK 2007: [https://doi.org/10.5281/zenodo.17969796](https://doi.org/10.5281/zenodo.17969796)  
* Flecs ECS framework: [https://www.flecs.dev/](https://www.flecs.dev/)  
* Pandoc document system: [https://pandoc.org/](https://pandoc.org/)  
* AtomECS paper: [https://arxiv.org/abs/2105.06447](https://arxiv.org/abs/2105.06447)  
* AtomECS repository: [https://github.com/TeamAtomECS/AtomECS](https://github.com/TeamAtomECS/AtomECS)

