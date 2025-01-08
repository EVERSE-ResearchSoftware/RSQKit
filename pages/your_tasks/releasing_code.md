---
title: Releasing code
description: How to create software releases
contributors: ["Christian Hüser", "Shoaib Sufi", "Daniel Garijo"]
page_id: releasing_code
related_pages:
  your_tasks: [zenodo_doi]

---

## How to Create Code Releases
 
### Description

A software release is the process of making a new or updated version of software available to users. 
It's an important phase in software development cycle that involves several other stages, including: planning, 
development, testing, deployment, and maintenance.

### Considerations

* A software release is a new version of a software product, and a **release log** (changelog) is a document that records the changes 
made to the software over time and is published with the software at the time of the release.
* **Software versioning** is the process of assigning either unique version names or unique version numbers to software releases. 
Naming schemes can vary - for example {% tool "semantic-versioning" %} (e.g. "1.0.2") and {% tool "calendar-versioning" %} (e.g. "24.10").
* Attachments like built binaries or packages or other software artefacts can be provided with the release.

### Solutions

Software Project Management Platforms like {% tool "github" %} and {% tool "gitlab" %} offer features to help 
with releasing software automatically.

For example, to perform a software release on GitHub:

- Go to your source code repository on GitHub.
- Prepare changelog ahead of the release process.
- Click on `Releases` and then on `Draft a new release` button.
- Decide on a software versioning scheme you will use and use a unique name or number for this release.
- Add release notes - a short and non overly technical summary of the changelog intended for end-users.
- Click on `Publish release`.
- If your repository is [integrated with Zenodo](./zenodo_doi) - a new DOI for this software release will automatically 
be minted by {% tool "zenodo" %}.
