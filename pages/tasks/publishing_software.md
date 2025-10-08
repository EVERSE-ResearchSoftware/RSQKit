---
title: Publishing software
description: How do you publish your software for reuse by others?
page_id: publishing_software
indicators: []
child_tasks: [software_identifiers, software_metadata, citing_software, archiving_software, packaging_releasing_software] 
keywords: ["software publishing", "publish software", "software packaging", "software citation", "software identifiers", "software archiving"]
page_citation: false
---

Here are the tasks that you should consider for publishing your software.

{% if page.child_tasks %}
    {% assign child_tasks = page.child_tasks | join: ', ' %}
    {% include section-navigation-tiles.html type="tasks" custom=child_tasks sort=false col=5 %}
{% endif %}
