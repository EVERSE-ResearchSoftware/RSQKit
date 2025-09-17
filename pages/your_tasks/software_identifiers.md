---
title: Software identifiers
description: How to uniquely identify your software and its versions?
contributors: ["Shoaib Sufi", "Daniel Garijo", "Thomas Vuillaume", "Aleksandra Nenadic"] 
page_id: software_identifiers
related_pages:
  your_tasks: [releasing_software]
quality_indicators: [persistent_and_unique_identifier]
keywords: ["software identifier", "software release", "software version", "versioning"]
training:
  - name: "EVERSE TeSS"
    registry: TeSS
    url: "https://everse-training.app.cern.ch"
---


## Why do you need to identify your software?

### Description

Uniquely identifying software and its versions is critical for reproducibility, proper citation, and long-term accessibility of software.
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

There are multiple approaches to achieving this, including versioning schemes, digital identifiers (DOIs, UUIDs, checksums), and metadata standards. They come with advantages and disadvantages and can be used in combination.

Some methods for uniquely identifying software and versions include:

- {% tool "semantic-versioning" %} - a structured approach to versioning software in the format MAJOR.MINOR.PATCH.
- Digital Object Identifiers (DOIs) for software - a DOI (Digital Object Identifier) provides a globally unique, 
citable reference for a software artefact (software as a whole and its different releases) that integrates with academic and research systems. This is of particular importance for research software - see below for more details on obtaining DOIs for your software.
- Cryptographic hashes (checksums) - a cryptographic hash uniquely represents a software artefact (source code, binary, or package).
- Universally Unique Identifiers (UUIDs) - a UUID (or GUID) is a 128-bit identifier often used in distributed systems.
- Git commit hashes - for version-controlled software, a Git commit hash uniquely identifies a snapshot of the codebase.

Table below provides a summary to help you choose the right identifier combination.

| Method                       | Best use case                        | Limitations | |------------------------------|--------------------------------------|--------------------------------------| | Semantic Versioning (SemVer) | Standard software releases           | Doesn't provide global uniqueness outside of the software’s ecosystem | | DOIs                         | Research software, academic citation | Requires registration and is not commonly used in commercial software | | Cryptographic hashes        | Ensuring software integrity          | Changing even one bit of data creates a completely different hash | | UUIDs | Distributed systems, databases       | Not human-readable, doesn’t convey versioning semantics | | Git commit hashes | Development snapshots| Not always meaningful outside the development context |

Bear in mind that if you register your software in a repository or registy, a persistent identifier for it (or its metadata) is often created automatically. To find an appropriate registry for your research software, please have a look at the following [awesome list](https://github.com/NLeSC/awesome-research-software-registries).

## How to obtain and use DOIs for research software?

A Digital Object Identifier (DOI) is a [persistent identifier][what-are-pids] or a handle used to uniquely identify various objects, such as journal articles, research reports, dataset or software, standardised by the International Organization for Standardisation (ISO).

A DOI fits within the URI (Uniform Resource Identifier) system, and also resolves to its target - the information object to which the DOI refers.
This is achieved by binding the DOI to metadata about the object, such as a URL where the object is located.

Obtaining a DOI for software has become [increasingly popular][datacite-doi-software] to indicate to others how to cite your software (either in a publication or as an independent way of referring to your software).

There are many services that can issue (or mint) DOIs, i.e. perform the process of creating and assigning a DOI to an object.
We will explore how you can do that for your software using {% tool "zenodo" %}, a general-purpose open archive and publishing repository developed under the European OpenAIRE program and operated by CERN.

Zenodo's DOI versioning feature allows users to create a **concept DOI** (which represents the software package as a whole, including all its versions) and multiple **release DOIs** for software packages (with each DOI representing a specific version of the software package).
In other words, the concept DOI is a reference to a software project as a whole, while the software version DOI is a reference to a particular software release.

### Why are DOIs important?

Publishing your software in digital research artefact archive services is a valuable practice that enhances the visibility, citability, and long-term preservation of your research software:

- Obtaining a DOI for your software makes it easier to cite and track your work and research output.
- Ensures long-term preservation of your code, even if the original software repository becomes unavailable.
- Provides a stable, versioned archive of your software for reproducibility purposes.
- Increases the discoverability of your software through Zenodo's search functionality and metadata.
- Helps with complying with your funding agency's requirements for open science and research sharing.

### Getting a DOI for software hosted on GitHub

Zenodo and GitHub provide an integration between the two services which makes issuing DOIs for your software stored in GitHub by Zenodo and archiving your software releases on Zenodo easier.

* If you do not have a Zenodo account - create one now (preferably using your GitHub account). This effectively links the two accounts. 
If you already have a Zenodo account, you can link it to your GitHub account bu navigation to your [Zenodo profile page](https://zenodo.org/account/settings/profile), selecting the `GitHub` tab, then clicking on `Connect` and authorising Zenodo to access your GitHub account.
* Once connected to GitHub, choose which GitHub repository you would like to create a DOI for under the `Repositories` section in Zenodo.
This will tell Zenodo to create a DOI for your software project as well as issue a new DOI each time you release a new version of software via GitHub.
* Back on GitHub, create a release for your software repository (also check out the [releasing software procedure][releasing_software]).
  * Go to your software repository's home page on GitHub.
  * Click on `Releases` and then `Draft a new release` button.
* Zenodo will automatically archive this release due to its integration with GitHub. Each new release you do on GitHub will receive a new DOI and 
will be archived on Zenodo too.

Check out other relevant documentation:

- [GitHub's Documentation on Referencing and Citing Content][github-referencing-and-citing-content]
- [GitHub Integration FAQ on Zenodo][github-faq-zenodo]
- [Making code citable with Zenodo and GitHub][citable-github-ssi] guide from Software Sustainability Institute

### Getting a DOI for software hosted on GitLab

If your software is stored on GitLab, below is the procedure to obtain a DOI for your software via Zenodo.

* Provide software metadata in a CodeMeta file (`codemeta.json`) at the root of your software repository. See more on [software metadata](./software_metadata) and {% tool "codemeta" %} standard.
* Get a [Zenodo token](https://zenodo.org/account/settings/applications/tokens/new/) with publishing rights (`deposit:actions` and `deposit:write` scopes).
* Add the {% tool "eossr" %} or the [gitlab2zenodo](https://gitlab.com/sbeniamine/gitlab2zenodo) libraries in  your [GitLab-CI pipeline](https://docs.gitlab.com/ee/ci/yaml/) to automatically archive your code on Zenodo whenever you create a new release.
  * Note that if using gitlab2zenodo, you will need to convert your `codemeta.json` file to a `.zenodo.json` file, e.g. using the `eossr`.
* Back on GitLab, create a release for your software repository (also check out the [releasing software procedure][releasing_software]).
* The CI pipeline will automatically push an archive of your software release to your account on Zenodo, which will generate a DOI and publish it.

Check out other relevant documentation:
- [How to create DOI (Digital Object Identifier) for GitLab.com repository?](https://forum.gitlab.com/t/how-to-create-doi-digital-object-identifier-for-gitlab-com-repository/3749)
- [Obtaining a DOI for a GitLab release or repo](https://forum.gitlab.com/t/obtaining-a-doi-for-a-gitlab-release-or-repo/30259)
- [GitLab to Zenodo](https://escape-ossr.gitlab.io/eossr/gitlab_to_zenodo.html)

### Linking the DOI with your software repository

After making a software release, go back to your Zenodo profile where you will find your repository archived with a DOI assigned to it.
For software located and released via GitHub, there is a special [GitHub section in your account on Zenodo][your-zenodo-github] where you will find your published and archived releases.

Find the particular release for your software and click on it - you will be taken to the Zenodo record for your software release.
You can see the Zenodo DOI badge under `Details`:

![Badge in Zenodo](../../images/badge_zenodo.png)

* Click on the blue DOI badge - a window will pop up with badge in various formats. Copy the Markdown version of the badge
  and paste to the [README file][creating_good_readme] in your software repository. It will show as follows:

![Badge in a software repository](../../images/badge_in_repo.png)


[calver]: https://calver.org/
[citable-github-ssi]: https://www.software.ac.uk/blog/making-code-citable-zenodo-and-github
[datacite-doi-software]: https://datacite.org/blog/doi-registrations-software/)
[doi]: https://www.doi.org/
[github]: https://github.com/
[github-faq-zenodo]: https://support.zenodo.org/help/en-gb/24-github-integration
[github-referencing-and-citing-content]: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
[semantic-versioning]: https://semver.org/
[what-are-pids]: https://support.orcid.org/hc/en-us/articles/360006971013-What-are-persistent-identifiers-PIDs
[your-zenodo-github]: https://zenodo.org/account/settings/github/
[releasing_software]: ./releasing_software
[creating_good_readme]: ./creating_good_readme