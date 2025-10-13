---
title: Publishing software
description: How do you publish your software for reuse by others?
page_id: publishing_software
indicators: []
child_tasks: [software_documentation, citing_software, software_identifiers, software_metadata, citing_software, archiving_software, packaging_releasing_software] 
keywords: ["software publishing", "software documentation", "software license", "software licence", "publish software", "software packaging", "software citation", "software identifiers", "software archiving"]
page_citation: false
---

Publishing research software means more than just putting the code online: it involves preparing it so others can find, understand, use, and cite it. 
Key tasks include: writing clear documentation and usage instructions, choosing and applying an appropriate open licence, creating a permanent archived release (e.g. via Zenodo or Software Heritage) with a DOI, adding metadata for discoverability, and ensuring reproducibility by capturing dependencies and environments (through containers, environment files, or workflow systems). 
Researchers should also consider citation files, contribution guidelines, and community practices to support reuse and credit.

This is the suggested order in which you should look at the related sub-tasks.

{% assign child_tasks = page.child_tasks | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_tasks sort=false col=5 %}
