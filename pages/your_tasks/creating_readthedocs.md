---
title: Creating a ReadTheDocs Page
description: Explain aspects about creating a ReadTheDocs page.
contributors: ["Christian Hüser"]
page_id: creating_readthedocs
related_pages: []
---

## How to Create a ReadTheDocs Page
 
### Description

Documentation is often part of software projects.
Most of the time this documentation are static pages that are built with tools such as [Sphinx][sphinx] or [MkDocs][mkdocs]. 
Software Project Management Platforms like [GitHub][github] or [GitLab][gitlab] have features to host static documentation pages.
A popular alternative is a service called [ReadTheDocs][readthedocs].
ReadTheDocs can be used independently or in combination with Software Project Management Platforms.
In the former case you can import the project to ReadTheDocs, in the latter case you can use these platforms to import a ReadTheDocs project.
A remote repository can also be used to automatically import the ReadTheDocs project via Continuous Integration (CI) provided by GitHub Actions or GitLab CI/CD and an API token.
After importing the project it is built and published automatically.

### Considerations

- In a ReadTheDocs project you need to use a configuration file `.readthedocs.yaml`.
- A Git repository can be used to version control the project and a remote repository can be hosted on GitHub or GitLab.
- Tools such as Sphinx or MkDocs can be used write the static documentation pages.
- CI that is offered by GitHub and GitLab helps automating the import task. Changes can be imported on different occations, e.g. on each push to the repository or merge to the default branch.

### Solutions

- ReadTheDocs
  - Publish static documentaiton pages publicly.
- Sphinx
  - Write static documentation pages based on reStructuredText.
- MkDocs
  - Write static documentation pages based on Markdown.
- GitHub
  - Host your remote repository and use GitHub Actions for automated imports.

## How to cite this Page

To be added.

## Tools and resources

- [ReadTheDocs][readthedocs]
- [Sphinx][sphinx]
- [MkDocs][mkdocs]
- [GitHub][github]

[readthedocs]: https://readthedocs.org
[sphinx]: https://www.sphinx-doc.org
[mkdocs]: https://www.mkdocs.org
[github]: https://github.com
[gitlab]: https://about.gitlab.com
