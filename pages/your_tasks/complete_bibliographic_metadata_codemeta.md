---
title: "How to provide complete bibliographic metadata as a CodeMeta file"
search_exclude: false
description: "Guidance on creating a complete CodeMeta file for software projects."
contributors: [Gavin J. Pringle] # Add contributors' names here
page_id: complete_bibliographic_metadata_codemeta
related_pages:
  your_tasks: [software_metadata]
quality_indicators: [] # Add relevant quality indicators here
keywords: ["codemeta", "bibliographic metadata", "software citation"]
training: 
  - name: "EVERSE TeSS"
    registry: TeSS
    url: "https://everse-training.app.cern.ch"
---

## How to provide complete bibliographic metadata as a CodeMeta file?

### Why It Matters

Creating a `codemeta.json` file is like giving your software a passport. 
It makes your project easy to find, cite, and use. 
This file helps others understand what your software does and who contributed to it.

### What to Focus On

When you're setting up a `codemeta.json` file, keep these things in mind:

- **Stick to Standards**: Use the CodeMeta schema. It keeps your file compatible with different platforms.
- **Keep It Current**: Update the file whenever your software changes. New version? New contributor? Make sure it's reflected.
- **Check for Errors**: Use a JSON validator to catch any mistakes, e.g., {% tool "jasonldvalidator" %}.
- **Use Persistent Identifiers**: Add a DOI for long-term reference. Zenodo is a good place to get one.
- **Detail Contributors**: Use the `Person` schema and include Open Researcher and ORCID iDs for authors and contributors.
- **Clarify Licensing**: Use a Software Package Data Exchange (SPDX) identifier to make the license clear.
- **Acknowledge Funders**: Include funder details with identifiers like Crossref Funder IDs.

For more on software metadata, check out the [Software Metadata](./software_metadata) page.

### How to Create It

- **Do It Yourself**: You can manually create the file using the CodeMeta schema. Check out the example below.
- **Use Tools**: Try {% tool "codemetagenerator" %} for a form-based approach or {% tool "somef" %} for command-line generation. Always review and add details like ORCIDs and funder info.
- **Archive Your Work**: Release your software on a platform that assigns DOIs, like {% tool "zenodo" %}. Add the DOI to your `codemeta.json`.
- **Validate**: Use a service like {% tool "jasonldvalidator" %} to ensure everything is correct.

#### Example Template

Here's a sample `codemeta.json` file to get you started:

```json
{
  "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
  "@type": "SoftwareSourceCode",
  "name": "Your Software Name",
  "description": "A brief description of your software.",
  "version": "1.0.0",
  "author": [
    {
      "@type": "Person",
      "givenName": "First Name",
      "familyName": "Last Name",
      "email": "email@example.com",
      "identifier": "https://orcid.org/0000-0002-1825-0097",
      "affiliation": {
        "@type": "Organization",
        "name": "Organization Name"
      }
    }
  ],
  "license": "MIT",
  "codeRepository": "https://github.com/yourusername/your-repo",
  "issueTracker": "https://github.com/yourusername/your-repo/issues",
  "programmingLanguage": "Python",
  "keywords": ["software", "example", "codemeta"],
  "dateCreated": "Wednesday 1 October 2023",
  "dateModified": "Wednesday 10 October 2023",
  "softwareRequirements": [
    "numpy",
    "pandas"
  ],
  "relatedLink": "https://yourwebsite.com",
  "identifier": "https://doi.org/10.1234/exampledoi",
  "funder": [
    {
      "@type": "Organization",
      "name": "Funder Name",
      "identifier": "https://doi.org/10.13039/100000001"
    }
  ]
}
```
By following these steps, you can provide complete bibliographic metadata for your software project in a CodeMeta file, enhancing its discoverability and citation.

