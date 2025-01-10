---
title: Writing a CodeMeta file
description: What is CodeMeta and how to write a CodeMeta file for your software
contributors: ["Daniel Garijo"]
page_id: codemeta
related_pages:
  your_tasks: [zenodo_doi]
---
## What is CodeMeta?
[CodeMeta](https://codemeta.github.io/terms/) is a community standard for interchanging software metadata records. It consists on a set of properties that extend [Schema.org](https://schema.org) (a popular vocabulary designed to describe Digital Objects on the Web) with software-specific metadata (e.g., maintainer, build instructions, software documentation, etc.)

## Why do you need a CodeMeta file?

### Description <!-- do not delete this heading and write your text below it -->

By adding a `codemeta.json` file in your root source code repository, you will ease metadata propagation between different archival infrastructures. For example, when [obtaining DOIs for your code releases](https://everse.software/RSQKit/zenodo_doi), you won't need to fill in the corresponding software metadata again. CodeMeta is recognised and used by major code repositories and registries like {% tool "zenodo" %}, {% tool "inveniordm" %} and {% tool "softwareheritage" %}.

But how to create a `codemeta.json` file?

### Considerations <!-- do not delete this heading and write your text below it -->
* You use a code repository such as {% tool "github" %} as your software repository
* You are knowledgeable about the metadata you want to describe. See the [CodeMeta terms](https://codemeta.github.io/terms/) to understand which terms are expected. It is not needed to include a record of all terms, just the ones you know.

### Solutions <!-- do not delete this heading and write your text below it -->
* Create a `codemeta.json` file through any of the means below:
  * By using the {% tool "codemetagenerator" %}, a form-based service to help you describe valid CodeMeta records.
  * By using the {% tool "somef" %} command line and selecting the `-c` option to export a CodeMeta file generated from your README file and available documentation. 
    * Alternatively, the following {% tool "somefvider" %} will allow you downloading auto-generated CodeMeta files (remember to double check the results).
  * Manually, by using the following [template](https://github.com/codemeta/codemeta/blob/master/codemeta.json) as a reference. JSON-LD files can be validated with services like the {% tool "jasonldvalidator" %}.
* Copy the file in your source code root directory.

 
