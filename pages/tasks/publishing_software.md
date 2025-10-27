---
title: Publishing software
description: How do you publish your software for reuse by others?
page_id: publishing_software
indicators: []
child_pages: [software_documentation, software_metadata, software_identifiers, citing_software, packaging_software, releasing_software, archiving_software] 
#keywords: ["software publishing", "software documentation", "software license", "software licence", "publish software", "software packaging", "software citation", "software identifiers", "software archiving"]
page_citation: false
---

Publishing research software comprises more than just putting the code online into a public code repository such as GitHub or Gitlab.
While it is a great start, publishing software may involve additional steps to prepare you software so others can find, understand, use, and cite it. 

Tasks to consider when publishing your software include:

* writing release notes, a changelog, documentation and usage instructions, 
* adding metadata for discoverability, and ensuring reproducibility by capturing dependencies and environments (through containers, environment files, or workflow systems),
* choosing and applying an appropriate open licence, 
* adding citation files, contribution guidelines, and community practices to support reuse and credit,
* versioning and releasing a stable, usable and installable version of your software (e.g. as a "package" in a package registry or by tagging a specific version as an official release in code repositories),
* archiving the release (e.g. on Zenodo or Software Heritage) with a DOI.

This is the suggested order in which you should look at the related sub-tasks.

{% assign child_pages = page.child_pages | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_pages training=false sort=false col=3 %}
