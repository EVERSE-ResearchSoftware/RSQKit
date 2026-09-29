---
title: Software metadata
description: How to describe your software using metadata?
contributors: ["Daniel Garijo", "Aleksandra Nenadic"]
page_id: software_metadata
related_pages:
  tasks: [software_identifiers, citing_software, archiving_software]
quality_indicators: [descriptive_metadata, codemeta_completeness]
child_pages: [complete_software_metadata_codemeta]
keywords: ["software metadata", "codemeta", "software citation", "cff"]

---

## What is software metadata?

Software metadata is structured data that provides information about a software application, its components, and its behaviour.
It describes various attributes of the software, including:

- Authors: details about the developers or organisations that created the software.
- Build & runtime information: includes details like operating system compatibility, architecture (e.g., 32-bit or 64-bit), and runtime requirements.
- Dependencies: lists required libraries, frameworks, or other software needed for proper functioning.
- Description and keywords: details about what the software tool does, its features and purpose.
- License: specifies the software license (e.g., MIT, BSD, GPL, proprietary).
- Name & version: identifies the software and its release version.
- Support and maintenance information: contact details to get support and questions answered.

### Considerations

Providing metadata with your software is important because it provides the crucial context and (typically machine readable) information about your software and its components, enhancing its discoverability, reusability and interoperability with other tools. Software metadata is key to addressing many of the FAIR principles.

The type of metadata you need from software depends on your specific use case.

- If your main focus is academic credit for software, citation metadata is most important.
- If you're aiming to replicate an analysis, versioning and dependencies matter more than authorship or titles.
- If you're searching for new software suited to a particular task, keywords and descriptions are most relevant.

Often, developers of research software, repositories that host it, and users have multiple objectives—sometimes balancing several of these needs at once.

### Solutions

Include a metadata file together with your source code files. There are various kinds of software metadata standards with slightly different purposes and use cases, some of which are listed below.

General software metadata standards, for example:

- {% tool "codemeta" %} – a community standard JSON-LD metadata format for describing software projects to support the preservation, discovery, reuse, and attribution of research software. See our dedicated [page](complete_bibliographic_metadata_codemeta) for learning how to add a CodeMeta file in you repository.
- [Citation File Format](https://citation-file-format.github.io/) a metadata file for supporting software citation  purposes. See our dedicated [page](citing_software) for learning how to add a CFF file in your code repository.
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
- `Cargo.toml` - manages dependencies, scripts, and metadata for Rust projects.
- `Project.toml` - manages dependencies, scripts, and metadata for Julia projects.
- `DESCRIPTION` - manages dependencies, scripts, and metadata for R projects.
- `composer.json` - manages dependencies, scripts, and metadata for PHP projects.
- interoperability & integration metadata (e.g. [BioSchemas Computational Tool profile](https://bioschemas.org/profiles/ComputationalTool/1.1-DRAFT)) -
facilitates communication between different software components, ensuring they work together without conflicts.

Software container & deployment metadata helps automate builds, testing, and deployment by providing necessary configuration details.
For example:

- SBOM (Software Bill of Materials) – a comprehensive list of all components and dependencies in a software product.
- Open Container Initiative (OCI) Image Specification – standard metadata format for container images, including layers, dependencies, and authorship.
- Dockerfile - defines base images, environment variables, and configurations for containerised applications.
- Kubernetes metadata - provides metadata for managing deployments, services, and pods in Kubernetes clusters.

{% assign child_pages = page.child_pages | join: ', ' %}
{% if child_pages != null and child_pages != '' %}
## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}
{% endif %}