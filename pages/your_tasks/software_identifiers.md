---
title: Software identifiers
description: How to uniquely identify your software and its versions?
contributors: ["Shoaib Sufi", "Daniel Garijo", "Thomas Vuillaume", "Aleksandra Nenadic"] 
page_id: software_identifiers
related_pages:
  your_tasks: [zenodo_doi, releasing_code]
---


## Why do you need to identify your software?

### Description

Uniquely identifying software and its versions is critical for reproducibility, proper citation, and long-term 
accessibility of software.
Without clear versioning, managing updates, debugging, and maintaining software becomes chaotic.

### Considerations

Identifying and tracking software versions is crucial for:

- Ensuring compatibility - different software versions may be incompatible with certain hardware, operating systems, 
or dependencies. A structured versioning system helps users and developers determine which versions work together.
- Fixing bugs and vulnerabilities - new software versions often fix security vulnerabilities or bugs found in earlier 
releases. Without proper versioning, users may unknowingly use outdated, vulnerable software.
- Preventing breaking changes for users - software evolves over time, but not all users upgrade instantly. Versioning allows older versions
  to coexist while users transition to newer releases.
- Enabling reproducibility - allows researchers and users to reproduce results consistently and across different environments.
- Managing development and collaboration effectively - helps developers coordinate and manage changes systematically, and track who changed what and when.
- Continuous development & deployment - most modern software development follows agile and continuous 
integration/continuous deployment (CI/CD) practices. Versioning helps with automated testing, software updates and releases.

### Solutions

There are multiple approaches to achieving this, including versioning schemes, digital identifiers (DOIs, UUIDs, checksums), 
and metadata standards. They come with advantages and disadvantages and can be used in combination.

Some methods for uniquely identifying software and versions include:

- {% tool "semantic-versioning" %} - a structured approach to versioning software in the format MAJOR.MINOR.PATCH.
- Digital Object Identifiers (DOIs) for software - a DOI (Digital Object Identifier) provides a globally unique, 
citable reference for a software artifact (software as a whole and its different releases) that integrates with academic and research systems. This is of particular importance for 
research software - check out the related [Digital Object Identifiers (DOIs) for software page](./zenodo_doi) for more datails on obtaining DOIs for your software.
- Cryptographic hashes (checksums) - a cryptographic hash uniquely represents a software artifact (source code, binary, or package).
- Universally Unique Identifiers (UUIDs) - a UUID (or GUID) is a 128-bit identifier often used in distributed systems.
- Git commit hashes - for version-controlled software, a Git commit hash uniquely identifies a snapshot of the codebase.

Table below provides a summary to help you choose the right identifier combination.

| Method                       | Best use case                        | Limitations |
|------------------------------|--------------------------------------|--------------------------------------|
| Semantic Versioning (SemVer) | Standard software releases           | Doesn't provide global uniqueness outside of the software’s ecosystem |
| DOIs                         | Research software, academic citation | Requires registration and is not commonly used in commercial software |
| Cryptographic hashes        | Ensuring software integrity          | Changing even one bit of data creates a completely different hash |
| UUIDs | Distributed systems, databases       | Not human-readable, doesn’t convey versioning semantics |
| Git commit hashes | Development snapshots| Not always meaningful outside the development context |