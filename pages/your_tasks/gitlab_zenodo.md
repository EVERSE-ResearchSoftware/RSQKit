---
title: Publishing software from GitLab to Zenodo
search_exclude: true
description: How to obtain a DOI via Zenodo for your code releases on GitLab
contributors: ["Thomas Vuillaume"]
page_id: gitlab_to_zenodo
related_pages: [releasing_code, github_zenodo, codemeta]
keywords: [zenodo, gitlab, code release]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->


## How can I get a Digital Object Identifier (DOI) for my code release on GitLab?

### Description 

Publishing your code to Zenodo is a valuable practice that enhances the visibility, citability, and long-term preservation of your research software. By linking your code repository to Zenodo, you can:

1. Obtain a Digital Object Identifier (DOI) for your software, making it easier to cite and track.
2. Ensure long-term preservation of your code, even if the original repository becomes unavailable.
3. Increase the discoverability of your software through Zenodo's search functionality and metadata.
4. Comply with funding agency requirements for open science and data sharing.
5. Provide a stable, versioned archive of your software for reproducibility purposes.

In this document, we describe how to automatically archive a snapshot of your code repository on Zenodo whenever you create a new release on GitLab. 

### Considerations

* You use a GitLab instance (either on gitlab.com or self-hosted) as your software repository
* You make software releases (e.g. using [semantic versioning][semantic-versioning])
* You use or are happy to make an account on the [Zenodo][zenodo] archive
* You would like to archive your code on Zenodo and obtain a DOI for each software release that people can use to cite your work
* You can provide metadata for your software in a `.zenodo.json` file or a `codemeta.json` file in the root of your repository to specify the metadata for your Zenodo deposit.
* Your GitLab repository can run CI/CD pipelines.

### Solutions

* Provide software metadata in a `.zenodo.json` or `codemeta.json` file.
  * Create a `.zenodo.json` file in the root directory of your repository following the [Zenodo's metadata schema](https://developers.zenodo.org/#metadata).
  * Use the [Zenodo's sandbox](https://sandbox.zenodo.org/) to test your metadata.
  
* Get a [Zenodo token](https://zenodo.org/account/settings/applications/tokens/new/) with publishing rights (`deposit:actions` and `deposit:write` scopes).

* Add the [eossr](https://escape-ossr.gitlab.io/eossr/gitlab_to_zenodo.html) or the [gitlab2zenodo](https://gitlab.com/sbeniamine/gitlab2zenodo) libraries in  your [GitLab-CI pipeline](https://docs.gitlab.com/ee/ci/yaml/) to automatically archive your code on Zenodo whenever you create a new release.

* [Create a GitLab release](https://everse.software/RSQKit/releasing_code) in your repository.
  * Go to your repository
  * Click on releases and then on New release
  * Use the same version number as specified in your metadata (e.g. `1.0.0`).
  * Add release notes
  * Click on Create release

* The CI pipeline will automatically push your code on Zenodo.

* Get the DOI:
   * After the GitLab release, go to Zenodo, where you will see your repository archived with a DOI assigned to it. Your badge is available in "Details":

![Badge in Zenodo](../../images/badge_zenodo.png)

* You may copy the badge in your README file:
   * Now you can add the Zenodo badge in your GitLab repository. Click on the blue DOI and copy the markdown in your README. It will show as follows:

![Badge in your repository](../../images/badge_in_repo.png)

## Tools and resources 

* Tools: [GitLab][gitlab], [Zenodo][zenodo], [eossr](https://escape-ossr.gitlab.io/eossr/), [gitlab2zenodo](https://gitlab.com/sbeniamine/gitlab2zenodo)

## References

[calver]: (https://calver.org/)
[datacite-doi-software]: (https://datacite.org/blog/doi-registrations-software/)
[doi]: (https://www.doi.org/)
[semantic-versioning]: (https://semver.org/) 
[what-are-pids]: (https://support.orcid.org/hc/en-us/articles/360006971013-What-are-persistent-identifiers-PIDs)
[zenodo]: (https://zenodo.org/)
[gitlab]: (https://gitlab.com/)
