---
title: Writing a CodeMeta file
description: What is CodeMeta and how to write a CodeMeta file for your software
contributors: ["Daniel Garijo"]
page_id: codemeta
related_pages: [zenodo_doi]
---
## What is CodeMeta?
[CodeMeta](https://codemeta.github.io/terms/) is a community standard for interchanging software metadata records. It consists on a set of properties that extend [Schema.org](https://schema.org) (a popular vocabulary designed to describe Digital Objects on the Web) with software-specific metadata (e.g., maintainer, build instructions, software documentation, etc.)

## Why do you need a CodeMeta file?

### Description <!-- do not delete this heading and write your text below it -->

By adding a `codemeta.json` file in your root source code repository, you will ease metadata propagation between different archival infrastructures. For example, when [obtaining DOIs for your code releases](https://everse.software/RSQKit/zenodo_doi), you won't need to fill in the corresponding software metadata again. CodeMeta is recognised and used by major code repositories and registries like [Zenodo](https://zenodo.org/) ([Invenio RDM](https://inveniosoftware.org/products/rdm/)) and [Software Heritage](https://www.softwareheritage.org/).

But how to create a `codemeta.json` file?

### Considerations <!-- do not delete this heading and write your text below it -->
* You use a code repository such as [GitHub][github] as your software repository
* You are knowledgeable about the metadata you want to describe. See the [CodeMeta terms](https://codemeta.github.io/terms/) to understand which terms are expected. It is not needed to include a record of all terms, just the ones you know.

### Solutions <!-- do not delete this heading and write your text below it -->
* Create a `codemeta.json` file through any of the means below:
  * By using the [CodeMeta Generator](https://codemeta.github.io/codemeta-generator/), a form-based service to help you describe valid CodeMeta records.
  * By using the [Software Metadata Extraction Framework](https://github.com/KnowledgeCaptureAndDiscovery/somef/) command line and selecting the `-c` option to export a CodeMeta file generated from your README file and available documentation. 
    * Alternatively, the following [service](https://somef.linkeddata.es/) will allow you downloading auto-generated CodeMeta files (remember to double check the results).
  * Manually, by using the following [template](https://github.com/codemeta/codemeta/blob/master/codemeta.json) as a reference. JSON-LD files can be validated with services like the [JSON-LD Playground](https://json-ld.org/playground/)
* Copy the file in your source code root directory

## How to cite this page <!-- do not delete this heading and write your text below it -->
 TO DO.

## Tools and resources <!-- do not delete this heading and write your text below it -->
* [CodeMeta Generator](https://codemeta.github.io/codemeta-generator/): Online form to help manually create and validate CodeMeta files.
* [JSON-LD validator](https://json-ld.org/playground/): Service to validate JSON-LD files.
* [Software Metadata extraction framework (SOMEF)](https://github.com/KnowledgeCaptureAndDiscovery/somef/): Library designed to extract CodeMeta files from source code documentation.
* [Somef vider](https://somef.linkeddata.es/): A service running SOMEF to obtain CodeMeta files.
* [Sample CodeMeta file](https://github.com/codemeta/codemeta/blob/master/codemeta.json): CodeMeta example to use as a template for your repository.

## References <!-- do not delete this heading and write your text below it -->
<!--If work has been inspired or derived from other content (e.g., pages in RDMKit) make sure to reference it here. -->
To be added.


[github]: (https://github.com/)
 
