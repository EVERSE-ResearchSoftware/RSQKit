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

- **Keep It Current**: Update the file whenever your software changes. New version? New contributor? Make sure it's reflected.
- **Check for Errors**: Use a JSON-LD validator to catch any mistakes, e.g., {% tool "jasonldvalidator" %}.
- **Use Persistent Identifiers**: Add a Digital Object Identifier (DOI) for the software release itself for long-term citation (e.g., from Zenodo). Ensure ORCID iDs are included for all people.
- **Link to the Paper**: Use the `referencePublication` property to link to the corresponding journal article, including the paper's DOI as its `identifier`.
- **Detail Contributors**: Use the `Person` schema and include ORCID iDs (the persistent identifier for people) for authors and contributors.
- **Clarify Licensing**: Use a Software Package Data Exchange (SPDX) identifier to make the license clear.
- **Acknowledge Funders**: Include funder details with identifiers like Crossref Funder IDs.

For more on software metadata, check out the [Software Metadata](./software_metadata) page.

### How to Create It

- **Do It Yourself**: You can manually create the file using the CodeMeta schema. Check out the example below.
- **Use Tools**:  
  - {% tool "codemetagenerator" %} for a form-based approach  
  - {% tool "somef" %} for command-line generation  
  - {% tool "autocodemeta %} for an interactive tool that guides you through creating a `codemeta.json` file step by step: https://w3id.org/autocodemeta
  - NB Always review and add details like ORCID iDs and funder info.
- **Archive Your Work**: Release your software on a platform that assigns DOIs, like {% tool "zenodo" %}. Add the DOI to your `codemeta.json` as an `identifier`.
- **Validate**: Use a service like {% tool "jasonldvalidator" %} to ensure everything is correct.

#### Example Template

Here's a sample `codemeta.json` file to get you started:

```json
{
  "@context": "https://doi.org/10.5063/schema/codemeta-3.1",
  "@type": "SoftwareSourceCode",
  "name": "Your Software Name",
  "description": "A brief description of your software.",
  "version": "1.0.0",
  "referencePublication": {
    "@type": "ScholarlyArticle",
    "headline": "A New Algorithm for Applied Mathematics using Python and NumPy",
    "identifier": "https://doi.org/10.1016/j.jsc.2023.10.001",
  },
"author": [
    {
      "@type": "Person",
      "givenName": "First",
      "familyName": "Author",
      "email": "first.author@example.com",
      "identifier": "https://orcid.org/0000-0002-1825-0097", 
      "affiliation": {
        "@type": "Organization",
        "name": "University of Edinburgh"
      }
    },
    {
      "@type": "Person",
      "givenName": "Second",
      "familyName": "Author",
      "identifier": "https://orcid.org/0000-0003-0000-0000"
    }
  ],
  "contributor": [
    {
      "@type": "Person",
      "givenName": "Key",
      "familyName": "Contributor",
      "identifier": "https://orcid.org/0000-0001-9999-9999",
    }
  ],
  "license": "https://spdx.org/licenses/MIT",
  "codeRepository": "https://github.com/yourusername/your-repo",
  "issueTracker": "https://github.com/yourusername/your-repo/issues",
  "programmingLanguage": "Python",
  "keywords": ["software", "example", "codemeta"],
  "dateCreated": "2023-10-01",
  "dateModified": "2023-10-10",
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

