---
title: "A title for the task or a problem you are trying to solve" # short title
search_exclude: true # set to false if you want this page to show up in search results
description: "" # a description of the page
contributors: [] # a comma separated list of contributors' names, as found in _data/CONTRIBUTORS.yml
page_id: # unique page id, e.g. lowercase title words separated by underscore(s) - for example page_id of 'version control' page could be version_control
related_pages:
  tasks: [] # A comma-separated page_ids of the task pages that are related to the current page
child_pages: [] # A comma-separated page_ids of the task pages that are children to the current page in some sense (describes either "task/subtask" relationship or "general task/task using specific tool or applied to domain" relationship)
quality_indicators: [] # a comma separated list of indicators related to this page, according to the ids in https://w3id.org/everse/i/indicators/
keywords: [] # a comma separated list of keywords related to this page (surround multi-word terms in quotes), e.g. keywords: ["ci", "cd", "continuous integration", "continuous deployment"] - these terms will be used to automatically discover relevant training
---

## Concrete problem 1, formulated as a question <!-- example: how to version control code? -->

### Description <!-- do not delete this heading and write your text below it -->

Short explanation of what the problem is about.

### Considerations <!-- do not delete this heading and write your text below it -->

Detail things to consider about this problem in order to be able to find the right solution - e.g. using a bullet point list.

- Consideration 1
- Consideration 2
  - Sub-point
- Consideration 3 
  - Sub-point 
  - Sub-point

### Solutions <!-- do not delete this heading and write your text below it -->

Briefly describe the use of specific tools or resources to solve the problem - e.g. using a bullet point list.

- Solution 1
  - Sub-point
- Solution 2

Make sure to add the tools and resources mentioned in the text in the [_data/tool_and_resource_list.yml](_data/tool_and_resource_list.yml) file and then tag the page with such entries.

Repeat the same structure for other problems you wish to mention on the page, as needed, e.g. as follows.

## Concrete problem 2, formulated as a question <!-- example: how to use GitHub to share code ? -->

### Description <!-- do not delete this heading and write your text below it -->

### Considerations <!-- do not delete this heading and write your text below it -->

### Solutions <!-- do not delete this heading and write your text below it -->

## Tool- or Domain-Specific Tasks <!-- do not delete this heading and write your text below it - this is an optional section to list relevant tool- or domain-specific sub-pages -->

<!--
You can use this section to list tool- or domain-specific (sub-)tasks here - list them in the page's *frontmatter* using parameter `child_pages` and then use that list in this section as follows:

This is a suggested list tool-specific sub-tasks to have a look at.

{% assign child_pages = page.child_pages | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=4 %}
-->
