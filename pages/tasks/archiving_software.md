---
title: Archiving software
description: How can you archive your software for preservation?
contributors: ["Aleksandra Nenadic"]
page_id: archiving_software
indicators: [archived_in_software_heritage, archived_in_scholarly_repository, listed_in_registry]
related_pages:
  tasks: [publishing_software, software_identifiers, software_metadata, documenting_software, licensing_software]
keywords: ["archiving software", "software preservation"]
---


## How to ensuring long-term reproducibility and access to research software?

In research domains that rely heavily on computation, software is not just a tool — it is an integral part of the scientific process. 
However, software is inherently fragile: it evolves rapidly, becomes deprecated, and often depends on specific environments, libraries, or hardware. 
As a result, many research outputs become irreproducible or unusable within just a few years due to the lack of access to the original software environment.
Without systematic software archiving, research risks losing critical components of its provenance, making long-term validation, replication, and reuse of results impossible.

Putting code on {% tool "github" %} or {% tool "gitlab" %} (or any similar code hosting service) is good practice for [code sharing (publishing)](./publishing_software), versioning (e.g. using tags or releases on GitHub/GitLab) and even code packaging (e.g. with {% tool "github-packages" service), it is not enough for long-term software archiving.
This is because these are commercial services - if they change their policies, remove repositories (e.g. for inactivity, or security reasons), or even shut down (which has happened to code sharing platforms in the past), your code could disappear.

Archival means long-term preservation independent of any one platform.

### Benefits for research communities

Implementing proper software archiving practices brings significant value:

- Reproducibility - future researchers can rerun computational experiments with the exact same software stack.
- Preservation of scientific value - the loss of valuable tools, simulations or models that underpin published work is prevented.
- Compliance with Open Science mandates - meeting funder and journal requirements for software availability and preservation.
- Collaboration and reuse - archived software can be rediscovered, cited, and reused by other researchers, accelerating innovation.

### Considerations

Effective software archiving in research is more complex than simply saving source code. 
It requires addressing multiple interrelated technical aspects:

- Environment preservation - dependencies on compilers, libraries (e.g., NumPy, R packages), OS-level features, and system architectures must be captured.
- Build reproducibility - binary reproducibility is often non-trivial due to non-deterministic build processes or missing historical dependencies.
- Versioning and provenance - capturing software version history, commit hashes, and linkages to specific datasets or publications is essential.
- Emulation and virtualisation - for legacy software, virtual machines or emulators may be necessary to recreate the execution environment.
- [Licensing][licensing_software] constraints - proprietary software dependencies can limit what can legally be archived and shared.
- [Metadata][software_metadata] and [documentation][documenting_software] - proper archival demands machine- and human-readable metadata, including usage instructions, authorship, and configuration settings.

Archiving software does not mean that development has ended or that the software is no longer being maintained. 
Archiving preserves a specific version of the software — often corresponding to a project deliverable, software release or a research publication — for long-term access, citation, and reproducibility, while development and maintenance may continue in parallel.
Software may therefore be archived multiple times throughout its [lifecycle](./life_cycle) as new releases are produced.

### Archival solutions for research software

Several archival solutions for research software are emerging:

- Institutional repositories and {% tool "zenodo" %} provide [DOI-backed software][software_identifiers] archiving linked to publications, ensuring persistent citation and access.
- {% tool "software-heritage" %} can provide an universal archive of source code, capturing the development history of open-source software at scale.
- {% tool "reprozip" %} captures the execution environment of research software, enabling portability and reproducibility across platforms.
- {% tool "guix" %} / {% tool "nixos" %} are functional package managers that enable reproducible builds and isolated software environments.
- Containers (e.g., {% tool "docker" %}, {% tool "singularityce" %}) are popular tools for bundling applications with dependencies, especially in high-performance computing.
- VM snapshots are used when containerisation is not feasible, particularly for GUI-based or legacy software.
- [RO-Crate](https://www.researchobject.org/ro-crate/) has an honourable mention here, while it is not an archival mechanism it is a critical metadata format that ensures items (e.g., [workflows](computational_workflows)) that are archived are described, understandable and reusable.

Archiving software on services such as {% tool "zenodo" %} typically involves uploading a compressed archive (e.g. a ZIP or TAR.GZ file) containing the software source code, together with metadata and supporting documentation for a specific version.
Archiving research software can be streamlined by connecting a development repository (e.g. on GitHub) to an archival service (e.g. Zenodo). 
After the integration is set up, each tagged software release on GitHub is automatically packaged into an archive and archived in Zenodo, eliminating the need to manually upload software archives.
Connecting GitHub and Zenodo seamlessly links software publishing and archiving steps in the [software lifecycle](./life_cycle).

### Conclusion

Software archiving is now a foundational component of digital research infrastructure. 
As the scientific community moves toward open, reproducible, and [FAIR (Findable, Accessible, Interoperable, Reusable) principles][fair_rs], robust software preservation practices are essential. 
Researchers must adopt workflows and tools that not only produce results but also ensure those results can be trusted and reused decades from now.

{% assign child_pages = page.child_pages | join: ', ' %}
{% if child_pages != null and child_pages != '' %}
## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}
{% endif %}


[fair_rs]: fair_rs.md
[software_metadata]: ./software_metadata
[documenting_software]: ./software_documentation
[software_identifiers]: ./software_identifiers
[licensing_software]: ./licensing_software.md
