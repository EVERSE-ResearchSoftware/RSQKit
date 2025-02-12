---
title: "A title for the task or a problem you are trying to solve" # short title
search_exclude: true # set to false if you want this page to show up in search results
description: "" # a description of the page
contributors: [] # a comma separated list of contributors' names, as found in _data/CONTRIBUTORS.yml
page_id: # unique page id, e.g. lowercase title words separated by underscore(s) - for example page_id of 'version control' page could be version_control
related_pages:
  your_tasks: [] # A comma-separated page_ids of the task pages that are related to the current page
training: # A list of training resources relevant for this task or problem (e.g from TeSS registry or elsewhere)
  - name:
    registry:
    url:
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

Make sure to add the tools and resources mentioned in the text in the [_data/tool_and_resource_list.yml](_data/tool_and_resource_list.yml) file and then
tag the page with such entries.

Repeat the same structure for other problems you wish to mention on the page, as needed, e.g. as follows.

## Concrete problem 2, formulated as a question <!-- example: how to use GitHub to share code ? -->
 
### Description <!-- do not delete this heading and write your text below it -->

### Considerations <!-- do not delete this heading and write your text below it -->

### Solutions <!-- do not delete this heading and write your text below it -->


## References <!-- do not delete this heading and write your text below it -->
If this page has been inspired or derived from other resources, make sure to reference them here.

There is no need to reference other relevant pages from RSQKit here - rather list them in the page's *frontmatter* 
using parameter `related_pages` and they will be listed in the page automatically under "Related pages" section.

 
