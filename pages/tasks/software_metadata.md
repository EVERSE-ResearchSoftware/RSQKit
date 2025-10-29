---
title: Software metadata
description: How to describe your software using metadata?
contributors: ["Daniel Garijo", "Aleksandra Nenadic"]
page_id: software_metadata
related_pages:
  tasks: [software_identifiers]
quality_indicators: [descriptive_metadata, codemeta_completeness]
keywords: ["software metadata", "codemeta", "software citation", "cff"]
---

## What is software metadata?

Software metadata is structured data that provides information about a software application, its components, and its behaviour.
It describes various attributes of the software, including:

- Name & version: identifies the software and its release version.
- Authors: details about the developers or organisations that created the software.
- Dependencies: lists required libraries, frameworks, or other software needed for proper functioning.
- License: specifies the software license (e.g., MIT, BSD, GPL, proprietary).
- Build & runtime information: includes details like operating system compatibility, architecture (e.g., 32-bit or 64-bit), and runtime requirements.
- Support and maintenance information: contact details to get support and questions answered.

### Considerations

Providing metadata with your software is important because it provides the crucial context and (typically machine readable) information about your software and its components, enhancing its discoverability, reusability and interoperability with other tools.

The type of metadata you need from software depends on your specific use case.

- If your main focus is academic credit for software, citation metadata is most important.
- If you're aiming to replicate an analysis, versioning and dependencies matter more than authorship or titles.
- If you're searching for new software suited to a particular task, keywords and descriptions are most relevant.

Often, developers of scientific software, repositories that host it, and users have multiple objectives—sometimes balancing several of these needs at once.

### Solutions

There are various kinds of software metadata standards with slightly different purposes and use cases, some of which are listed below.

General software metadata standards, for example:

- {% tool "codemeta" %} – a standardised JSON-LD metadata format for describing software projects to support the preservation, discovery, reuse, and attribution of research software.
- {% tool "spdx" %} – used for documenting software licenses, components, and security information.
- [Dublin Core](https://www.dublincore.org/) – a general purpose metadata standard and vocabulary for describing resources of any type 
(first developed for describing web content in the early days of the World Wide Web), now often used for software documentation.
- [Schema.org](https://schema.org/) – promotes schemas for structured data on the Internet including software applications and digital assets, e.g. 
[BioSchemas Computational Tool profile](https://bioschemas.org/profiles/ComputationalTool/1.1-DRAFT) enables you to describe how to run software, including its input and output parameters.

Software development, build, package and dependency metadata helps developers track software versions, dependencies, and compatibility, making development, running and maintenance easier.
For example:

- PyPI metadata (Python) - `setup.py` and `pyproject.toml` define package metadata for Python packages and projects.
- `pom.xml` (Maven – Java) - defines project dependencies, build configurations, and plugins in Java projects.
- `package.json` (Node.js / npm) - manages dependencies, scripts, and metadata for JavaScript projects.
- interoperability & integration metadata (e.g. [BioSchemas Computational Tool profile](https://bioschemas.org/profiles/ComputationalTool/1.1-DRAFT)) -
facilitates communication between different software components, ensuring they work together without conflicts.

Software container & deployment metadata helps automate builds, testing, and deployment by providing necessary configuration details.
For example:

- SBOM (Software Bill of Materials) – a comprehensive list of all components and dependencies in a software product.
- Open Container Initiative (OCI) Image Specification – standard metadata format for container images, including layers, dependencies, and authorship.
- Dockerfile - defines base images, environment variables, and configurations for containerised applications.
- Kubernetes metadata - provides metadata for managing deployments, services, and pods in Kubernetes clusters.

## Using CodeMeta to describe software

{% tool "codemeta" %} is a community-developed metadata standard designed to describe and exchange metadata about research software projects in a structured way.
It provides a machine-readable JSON-LD format (in the form of `codemeta.json` file attached to your software project) for storing metadata about software, including authorship, licensing, dependencies, versioning, and more.
It consists of a set of properties that extend [Schema.org](https://schema.org) (a popular metadata vocabulary designed to describe Digital Objects on the Web) with software-specific metadata (e.g. maintainer, build instructions, software documentation, etc.).

It was created to standardise metadata across different repositories and programming ecosystems, making it easier to share, discover, and cite software.
See the [CodeMeta terms](https://codemeta.github.io/terms/) to understand which terms are used to describe software.

### Who uses CodeMeta?

- GitHub & GitLab code repositories support it to help document software for better discoverability.
- Researchers use it to cite research software in academic papers.
- Software repositories & archives like {% tool "zenodo" %}, {% tool "figshare" %}, {% tool "inveniordm" %} and {% tool "softwareheritage" %}, as well as many institutional repositories use it as a standardised metadata format across platforms.
- FAIR data initiatives support the use of CodeMeta format to [help with findability](https://zenodo.org/records/13996966/files/DASH_FAIR_CodeMeta_Oct_2024.pdf).

### How can you use CodeMeta?

You can use the [CodeMeta terms](https://codemeta.github.io/terms/) to create a `codemeta.json` file for your software projects and share it in the root of the source code repository (e.g. on GitHub & GitLab) along with your code.

You can create the `codemeta.json` file:
* by using {% tool "codemetagenerator" %}, an online form-based service to help you describe valid CodeMeta records.
* by using {% tool "somef" %} command line tool and using the `-c` flag to export the CodeMeta file generated from your README file and available documentation. 
Alternatively, {% tool "somefvider" %} will allow you to download auto-generated CodeMeta files (remember to double check the results).
* manually, e.g. by using the [CodeMeta template](https://github.com/codemeta/codemeta/blob/master/codemeta.json) as a reference. JSON-LD files can be validated with services like {% tool "jasonldvalidator" %}.

Using CodeMeta file to describe your software will propagate between different archival infrastructures, platforms and services which understand CodeMeta descriptions and can ingest existing `codemeta.json` files automatically ({% tool "zenodo" %}, {% tool "figshare" %}, {% tool "inveniordm" %} and {% tool "softwareheritage" %}).
This means you will not have to duplicate the work when using such services - e.g. when [obtaining a DOI for your software](./software_identifiers), if you have `codemeta.json` file already you will not have to fill in the corresponding software metadata again.