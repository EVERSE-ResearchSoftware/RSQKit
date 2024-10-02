---
title: How to publish code from GitHub or GitLab to Zenodo
search_exclude: true
description: How to automatically publish your code from GitHub or GitLab to Zenodo when creating a release
contributors: ["Thomas Vuillaume",]
page_id: publish_to_zenodo
related_pages: [] # to add when pages are created: CI/CD, code releases, codemeta file, zenodo_doi
keywords: [zenodo, github, gitlab, code release]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->

## What is Zenodo and why publish your code to it?

### Description <!-- do not delete this heading and write your text below it -->

Publishing your code from GitHub or GitLab to Zenodo when creating a release is a valuable practice that enhances the visibility, citability, and long-term preservation of your research software. This process involves automatically archiving a snapshot of your code repository on Zenodo whenever you create a new release on GitHub or GitLab. Zenodo is a general-purpose open repository that allows researchers to deposit research papers, data sets, research software, reports, and any other research-related digital artifacts. By linking your code repository to Zenodo, you can:

1. Obtain a Digital Object Identifier (DOI) for your software, making it easier to cite and track.
2. Ensure long-term preservation of your code, even if the original repository becomes unavailable.
3. Increase the discoverability of your software through Zenodo's search functionality and metadata.
4. Comply with funding agency requirements for open science and data sharing.
5. Provide a stable, versioned archive of your software for reproducibility purposes.

This automated process simplifies the publication workflow, allowing you to focus on your research while ensuring that your code is properly archived and citable with each release.


### Considerations <!-- do not delete this heading and write your text below it -->

* [Structured in bullet points](style_guide#text) as much as possible, detailing things to consider about this problem in order to be able to find the right solution.

* ??

### Solutions <!-- do not delete this heading and write your text below it -->

By using [bullet point style](style_guide#text) as much as possible, try to describe when, why and for what is best to use a specific tool or resource. 
Avoid making long list of links to tools and resources.
Make sure to add the tools and resources mentioned in the text in the main "tools and resources" table.


## How to provide metadata to Zenodo?

### Description <!-- do not delete this heading and write your text below it -->

Metadata describes your software and is used by Zenodo to display information on each record and for discovery.

Zenodo has its own metadata schema that can be described in a `.zenodo.json` file. But it can also automatically retrieve metadata from other sources such as GitHub or `citation.cff` file. Alternatively, you can also convert other metadata formats (`codemeta.json`, `mailmap`...) to Zenodo's format using external tools.
Finally, you can always manually add or edit metadata after the deposit has been created directly on Zenodo website.

### Considerations <!-- do not delete this heading and write your text below it -->

* Metadata is essential for discoverability and citability of your software.
* Providing metadata in a `.zenodo.json` file is the best way to ensure that your software is described as you want.
* There is no way to validate the content of the `.zenodo.json` file, so you need to ensure it is correct using Zenodo's sandbox before depositing your software.
* The GitHub integration is the easiest way to provide metadata, but it may not cover all the metadata you want to provide (e.g., license, keywords, authors, etc.).

### Solutions 

* Provide metadata in a `.zenodo.json` file.
  * Create a `.zenodo.json` file in the root directory of your repository following the [Zenodo's metadata schema](https://developers.zenodo.org/#metadata).
  * Use the [Zenodo's sandbox](https://sandbox.zenodo.org/) to test your metadata.
  


## How to automatically publish your code from GitHub to Zenodo when creating a release? <!-- example: how to name a software release? -->
 
### Description <!-- do not delete this heading and write your text below it -->
Same as above

### Considerations <!-- do not delete this heading and write your text below it -->
Same as above

### Solutions <!-- do not delete this heading and write your text below it -->

## How to cite this page <!-- do not delete this heading and write your text below it -->
 contributors, page URL. Last date of access.

## Tools and resources <!-- do not delete this heading and write your text below it -->
List of relevant tools and resources for this task.

## References <!-- do not delete this heading and write your text below it -->
If work has been inspired or derived from other content (e.g., pages in RDMKit) make sure to reference it here. 

 
## How to automatically publish your code from GitLab to Zenodo when creating a release? 

### Description <!-- do not delete this heading and write your text below it -->

Automatically publishing your code from GitLab to Zenodo when creating a release is a process that can be set up for both GitLab.com and self-managed GitLab instances. The process involves configuring your GitLab repository to trigger an archive creation on Zenodo whenever a new release is made, ensuring that your software versions are consistently documented and preserved.

### Considerations <!-- do not delete this heading and write your text below it -->

* Ensure you have a Zenodo account (if you don't already have one, you can create it [here](https://zenodo.org/)).
* Verify that your GitLab repository can run CI/CD pipelines.
* Consider the size of your repository, as Zenodo has file size limits for uploads (50GB).
* Decide which branches or tags should trigger the Zenodo archiving process. Usually, you would want to archive all versioned releases.
* Determine if you want to include or exclude certain files or directories from the Zenodo archive.
* Plan your versioning strategy to align with meaningful releases that should be archived.
* Consider the metadata you want to include with each Zenodo archive to enhance discoverability.
* You will need to create a `.zenodo.json` file or a `codemeta.json` file in the root of your repository to specify the metadata for your Zenodo deposit.
* Be aware of any sensitive or proprietary information in your repository that shouldn't be publicly archived.
* Consider the long-term implications of archiving your code, as Zenodo archives are permanent.
* Familiarize yourself with Zenodo's terms of service and data policies.
* Prepare a README file that explains the purpose and usage of your software for potential users who find it through Zenodo.

### Solutions <!-- do not delete this heading and write your text below it -->


You can automate the publication of your GitLab project to the ESCAPE Open-Source Scientific Software Repository (OSSR) on Zenodo. Contrary to GitHub, there is no integration between the plateforms so we will use the CI/CD to upload the project to Zenodo.
You only need to do the setup once, and then every new release of your project will be automatically uploaded and published to the Zenodo.


1. Create a metadata file to describe your project as a `codemeta.json` file or `.zenodo.json` file in the root directory of your repository.

   * Create a `codemeta.json` file in the root directory of your repository.
   * Fill in the required fields.
   * Remove any existing `.zenodo.json` file, as `codemeta.json` replaces it.

For more information, see the metadata description page.

### 2. Link your GitLab project with Zenodo

1. Create a personal access token on Zenodo:
   - Go to [Zenodo's token creation page](https://zenodo.org/account/settings/applications/tokens/new/).
   - Name the token and select all three scopes.

2. Add the token as a masked environment variable in your GitLab project:
   - Go to your GitLab project.
   - Navigate to Settings > CI/CD > Variables > Add variable.
   - Name the variable `ZENODO_TOKEN` (or `SANDBOX_ZENODO_TOKEN` if using Zenodo sandbox).
   - Mask the variable to keep it secure.

### 3. Update your `.gitlab-ci.yml` file

1. Add the OSSR upload code snippet to your `.gitlab-ci.yml` file.
2. For the first run, remove `-id $ZENODO_PROJECT_ID` to create a new record.
3. After the first run, create a new CI variable `ZENODO_PROJECT_ID` (or `SANDBOX_ZENODO_PROJECT_ID`):
   - Go to https://zenodo.org/deposit (or https://sandbox.zenodo.org/deposit).
   - Click on your uploaded project.
   - Copy the number from the URL (e.g., `3884963` from `https://zenodo.org/record/3884963`).
   - Add this as a new environment variable in your GitLab project.

### 4. Publish your project to Zenodo

1. Go to your GitLab project.
2. Navigate to Project overview > Releases > New release.
3. Create a new release to trigger the pipeline.

## What happens during the GitLab-Zenodo CI process?

The GitLab runner will:

1. Search for the last release or commit of your project.
2. Look for a CodeMeta metadata file and convert it to Zenodo's format.
3. Upload a new record version to the OSSR, including the information from your metadata files.

By following these steps, you'll automate the publication of your GitLab project to the ESCAPE OSSR on Zenodo.


* Set up the integration between GitLab and Zenodo:
  * Log in to your Zenodo account and navigate to the "Applications" section.
  * Create a new personal access token with the "deposit:actions" and "deposit:write" scopes.
  * In your GitLab repository, go to "Settings" > "CI/CD" > "Variables".
  * Add a new variable named `ZENODO_TOKEN` with the value of your Zenodo personal access token. Make sure to mask this variable for security.




## How to cite this page <!-- do not delete this heading and write your text below it -->
 contributors, page URL. Last date of access.

## Tools and resources <!-- do not delete this heading and write your text below it -->
List of relevant tools and resources for this task.

## References <!-- do not delete this heading and write your text below it -->
If work has been inspired or derived from other content (e.g., pages in RDMKit) make sure to reference it here. 
