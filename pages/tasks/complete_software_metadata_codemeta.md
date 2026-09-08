---
title: "Creating software metadata with CodeMeta"
description: "Guidance on creating a CodeMeta file for software projects."
contributors: ["Gavin Pringle", "Daniel Garijo"] # Add contributors' names here
coordinators: ["Gavin Pringle"]
page_id: complete_software_metadata_codemeta
related_pages:
  your_tasks: [software_metadata]
quality_indicators: [codemeta_completeness, descriptive_metadata] # Add relevant quality indicators here
keywords: ["codemeta", "bibliographic metadata", "software citation"]
---

### Description 

{% tool "codemeta" %} is a community-developed metadata standard designed to describe and exchange metadata about research software projects in a structured way.
It provides a machine-readable JSON-LD format (in the form of `codemeta.json` file attached to your software project) for storing metadata about software, including authorship, licensing, dependencies, versioning, and more.
It consists of a set of properties that extend [Schema.org](https://schema.org) (a popular metadata vocabulary designed to describe Digital Objects on the Web) with software-specific metadata (e.g. maintainer, build instructions, software documentation, etc.).

Creating a `codemeta.json` file is like giving your software a passport. It was created to standardise metadata across different repositories and programming ecosystems, making it easier to share, discover, and cite software.
See the [CodeMeta terms](https://codemeta.github.io/terms/) to understand which terms are used to describe software.

### Who uses CodeMeta?

- GitHub & GitLab code repositories support it to help document software for better discoverability.
- Researchers use it to cite research software in academic papers.
- Software repositories & archives like {% tool "zenodo" %}, {% tool "figshare" %}, {% tool "inveniordm" %} and {% tool "software-heritage" %}, as well as many institutional repositories use it as a standardised metadata format across platforms.
- FAIR data initiatives support the use of CodeMeta format to [help with findability](https://zenodo.org/records/13996966/files/DASH_FAIR_CodeMeta_Oct_2024.pdf).

### Considerations 

When you're setting up a `codemeta.json` file, keep these things in mind:

- **Keep It Current**: Update the file whenever your software changes. New version? New contributor? Make sure it's reflected.
- **Check for Errors**: Use a JSON-LD validator to catch any mistakes, e.g., {% tool "jasonldvalidator" %}.
- **Use Persistent Identifiers**: Add a Digital Object Identifier (DOI) for the software release itself for long-term citation (e.g., from Zenodo). Ensure ORCID iDs are included for all people.
- **Link to a Publication**: Use the `referencePublication` property to link to the corresponding journal article, including the paper's DOI as its `identifier`.
- **Detail Contributors**: Use the `Person` schema and include ORCID iDs (the persistent identifier for people) for authors and contributors.
- **Clarify Licensing**: Use a Software Package Data Exchange (SPDX) identifier to make the license clear.
- **Acknowledge Funders**: Include funder details with identifiers like Crossref Funder IDs.

For more on software metadata, check out the [Software Metadata](./software_metadata) page.

### Solutions 

- **Do It Yourself**: You can manually create the file using the CodeMeta schema. Check out the example below, or use the [CodeMeta template](https://github.com/codemeta/codemeta/blob/master/codemeta.json) as a reference. JSON-LD files can be validated with services like {% tool "jasonldvalidator" %}
- **Use Tools**:  
  - {% tool "codemeta-generator" %} for a manual form-based approach  
  - {% tool "auto-codemeta" %} for an interactive tool that helps you create a `codemeta.json` file step by step by retrieving existing metadata in your code repository.
  - {% tool "somef" %} for command-line generation  
  - {% tool "somef-vider" %} will allow you to download auto-generated CodeMeta files (remember to double check the results).
  
  - Always review and add details like ORCID iDs and funder information.
- **Archive Your Work**: Release your software on a platform that assigns DOIs, like {% tool "zenodo" %}. Add the DOI to your `codemeta.json` as an `identifier`.
- **Validate**: Use a service like {% tool "jasonldvalidator" %} to ensure everything is correct.

#### Example Template

Here's a sample `codemeta.json` file to get you started:

```json
{
  "@context": "https://w3id.org/codemeta/3.0",
  "@type": "SoftwareSourceCode",
  "name": "Your Software Name",
  "description": "A brief description of your software.",
  "version": "1.0.0",
  "referencePublication": {
    "@type": "ScholarlyArticle",
    "headline": "A New Algorithm for Applied Mathematics using Python and NumPy",
    "identifier": "https://doi.org/10.1016/j.jsc.2023.10.001"
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
      "identifier": "https://orcid.org/0000-0001-9999-9999"
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
    "numpy = 2.5.2",
    "pandas = 3.0.5"
  ],
  "relatedLink": "https://yourwebsite.com",
  "identifier": "https://doi.org/10.1234/exampledoi",
  "funder": [
    {
      "@type": "Organization",
      "name": "Funder Name",
      "identifier": "https://doi.org/10.13039/100000001"
    }
  ],
  "funding":"Grant number"
}
```
By following these steps, you can provide complete bibliographic metadata for your software project in a CodeMeta file, enhancing its discoverability and citation.

{% assign child_pages = page.child_pages | join: ', ' %}
{% if child_pages != null and child_pages != '' %}
## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}
{% endif %}