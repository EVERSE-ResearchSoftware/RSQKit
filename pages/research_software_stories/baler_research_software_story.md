---
title: "Research Software Story - BALER"
description: "Machine-Learning-Based Compression of Scientific Data in Real Time"
contributors: ["Michael Sparks", "Caterina Doglioni", "James Smith"]
page_id: baler_research_software_story
type: research_software_story
---

## The Problem

Modern scientific experiments generate massive datasets, straining available storage and bandwidth. Fields like particle physics, astrophysics, and computational fluid dynamics (CFD) produce data faster than it can be stored or transmitted. Traditional compression techniques are often ineffective on these specialised datasets. New methods are needed to drastically shrink data size without losing important scientific information.

## The Community

BALER is developed by a diverse team primarily composed of early-career researchers (students and postdocs). Contributors often join through their graduate studies or programmes like Google Summer of Code. The team experiences frequent turnover and varied experience levels - many members are new to machine learning or to the specific scientific domains of the data. To maintain consistency, experienced mentors hold regular meetings and guide the development process.

Users of BALER come from multiple disciplines: particle physics, astrophysics, CFD, and even industry. Most users have basic knowledge of Python and machine learning. The software is designed to be straightforward to use out-of-the-box, while still allowing advanced users to customise or extend functionality as needed.

## Technical Aspects

BALER is a prototype tool (considered "Tier 2" software) that applies machine learning (autoencoder models) for domain-specific lossy data compression. It is implemented mostly in Python and builds on the PyTorch library for neural network training.

BALER can run on standard CPUs and GPUs, and it also supports deployment on Field Programmable Gate Arrays (FPGAs) for real-time use cases. The software is distributed via Docker containers to simplify deployment on local machines or High-Performance Computing (HPC) clusters. The entire codebase (including example datasets) is roughly 400 MB and is publicly available on GitHub.

## Libraries and Systems

- PyTorch: Used to implement and train the autoencoder neural networks (with full GPU support).
- Docker: Used to containerise BALER for consistent and reproducible deployment across different systems.
- FPGA toolchains: Integrates with tools like *hls4ml* and Xilinx Vivado HLS to deploy the compression model on FPGAs for real-time data acquisition.

## Software Practices

BALER's development follows standard software engineering practices. All code is managed on GitHub, and contributions are submitted via pull requests for peer review. Continuous Integration (via GitHub Actions) runs automated tests and enforces code style (using Black) on each change to maintain quality. Docker container built only if syntax/code quality rules satisfied (badge on repository)

Every contribution is reviewed by senior developers, which helps ensure robustness and facilitate knowledge transfer. BALER recently changed its license to Apache 2.0 (from MIT) to encourage wider use (including in commercial contexts). Major releases are archived on Zenodo with DOIs to provide citable versions for research. This is made visible to users via a CITATION.cff resource.

## Community

New developers are onboarded through hands-on tasks, tutorials, and example code. Regular project meetings and mentorship from senior members create a supportive environment for them to learn and contribute effectively.

For users, BALER provides interactive Jupyter notebooks and tutorials to help them get started quickly. An early version of BALER is also available on the ESCAPE Virtual Research Environment (VRE), allowing anyone to experiment with it online without complex setup.

BALER addresses the common need for efficient data compression that preserves essential data quality. For example, high-energy physics experiments can use BALER to compress huge volumes of collision data, and astronomers can apply it to reduce streaming telescope data in real time before transmission or storage.

## Tools

- GitHub Actions: Automates continuous integration and testing for every update.
- Black: Automatically formats the code to enforce a consistent style.
- Docker: Ensures reproducible runtime environments for testing and deployment.

Using these tools improves the software's reliability and maintainability, making it easier for contributors to collaborate and for users to deploy BALER.

## FAIR & Open

BALER aligns with FAIR principles. The source code is openly available on GitHub under the Apache 2.0 license, enabling broad access and reuse. Each major release is archived on Zenodo with a DOI, which improves its findability and allows precise citation in publications.

The team evaluated BALER against a FAIR software checklist and scored well on open licensing and accessibility. They identified some areas to improve, such as refining versioning practices and making outputs more interoperable (currently, compressed outputs are NumPy arrays that require the corresponding ML model to decode).

The BALER developers also engage in the broader community on software sustainability and FAIR practices. For instance, they participate in an ESCAPE working group focused on sustainable and FAIR machine learning tools.

## Documentation

BALER's documentation is primarily hosted on its GitHub repository and wiki. The main README provides instructions for installation and basic usage.

The team also archives key documents (research papers, presentations, internal design reports) on Zenodo, and the project wiki links to these resources. By layering the documentation (README, tutorials, wiki, archived reports), BALER ensures that knowledge is preserved despite frequent team turnover. This makes it easier for new users and developers to learn the tool and contribute.

## Sustainability

The BALER team emphasises sustainability by preserving knowledge and following structured processes. All code is under version control (Git), and major versions are archived on Zenodo for long-term access and reproducibility. Documentation and design notes are routinely published online so that information remains available over time.

Project governance includes oversight by postdoctoral researchers with guidance from senior academic staff, which provides stability and a long-term vision. Since many contributors are students who may only work on BALER for a short period, the team aligns development goals with the academic calendar to maintain steady progress.

Long-term funding, as always, is a challenge. BALER currently relies on a variety of short-term project grants and volunteer effort. By integrating BALER into larger initiatives, the team aims to secure more sustainable resources and support for continued development.


## References

- BALER GitHub Repository: <https://github.com/baler-collaboration/baler>
- BALER: Bespoke data compression using autoencoders, WLCG/HSF Workshop 2024, 13–17 May 2024, https://indico.cern.ch/event/1369601/contributions/5883636/
- Baler - Machine Learning Based Compression of Scientific Data; Fritjof  Bengtsson Folkesson, Caterina  Doglioni, Per Alexander  Ekman, Axel  Gallén, Pratik  Jawahar, Marta  Camps Santasmasas, Nicola  Skidmore; EPJ Web of Conf. 295 09023 (2024) DOI: 10.1051/epjconf/202429509023
- BALER v1.4.0 Software Release (2023), Zenodo: DOI 10.5281/zenodo.10723669
