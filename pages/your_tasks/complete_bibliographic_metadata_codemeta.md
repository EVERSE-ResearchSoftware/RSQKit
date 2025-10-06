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

### Description

Creating a `codemeta.json` file involves compiling comprehensive bibliographic metadata for your software project. This json file facilitates software citation, discovery, and reuse by providing structured metadata in a machine-readable format. Complete bibliographic metadata includes persistent identifiers, detailed contributor roles, and licensing information, thereby fulfilling the standard criteria for scholarly attribution.

### Considerations

When creating a `codemeta.json` file, it's important to ensure your software is discoverable, and by following the standard you ensure contributors get recognition and that legal aspects are clear.

- **Standard Compliance**: Follow the CodeMeta schema to ensure compatibility and interoperability with various platforms.
- **Updates**: Regularly update the file to reflect changes in the software, such as new versions or additional contributors.
- **JSON-LD Compliance**: Ensure the file is valid JSON-LD (see Validation below), and that it includes the `@context` property linking to the CodeMeta standard.
- **Persistent Identifiers (PIDs)**: Use DOIs in the `identifier` field for long-term reference, obtained from platforms like Zenodo.
- **Contributor Details**: Use the `Person` schema for contributors and include ORCID iDs in the `identifier` property for all primary `author` and `contributor` entries.
- **License Field**: Use a recognized SPDX identifier for unambiguous licensing, where SPDX stands for Software Package Data Exchange.
- **Funder Information**: Include funder details as `Organization` types with identifiers like Crossref Funder IDs.

For more detailed information on software metadata and the use of CodeMeta, refer to the [Software Metadata](./software_metadata) page.

### Solutions

To create a complete `codemeta.json` file:

- **Manual Creation**: Follow the CodeMeta schema to manually create the file, using the example template below as a reference.
- **Use Automated Generation and Augmentation**:
  - Utilize tools like {% tool "codemetagenerator" %} for an online form-based service or {% tool "somef" %} for command-line generation from existing documentation. Review and manually add detailed attribution (ORCIDs, funder information) afterwards.
- **Ensure Archival and Persistence**:
  - Archive a release of your software on a platform that assigns DOIs, such as {% tool "zenodo" %}. Add the resultant DOI to the CodeMeta file's `identifier` field.
- **Validation**:
  - Validate the JSON-LD file using a service like {% tool "jasonldvalidator" %} to ensure structural correctness.

#### Example Template

Here is an example of a `codemeta.json` file:

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

