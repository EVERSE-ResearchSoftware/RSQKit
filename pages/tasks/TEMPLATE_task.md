---
title: "A title for the task or a problem you are trying to solve" # short title (e.g. "Creating a good README")
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

<!-- GUIDANCE

** The following should be the approach taken when writing RSQKit task pages:

   - Explain why the topic matters.
   - Be accurate.
   - Provide a good enough level of content so that if it's the only resource read:
      - It gives the correct impression.
      - Readers can apply the information correctly.
      - If sufficient, gives a conceptual overview and then point to existing high quality material. 
   - Motivate further learning by providing links. 

** The format of the task pages are sets of headings:

Task 
   - The task or sub-task description e.g., "Why is it important to have a good README file?" and a further sub-task might be, "What key sections should a README include?"
Description 
   - A short description of what the task or problem is about and why it matters.
Considerations 
   - Benefits, audience, choices, characteristics of solutions, key insights, etc; things to keep in mind when thinking about this task. 
   - You could use a bulleted list for brevity.
Solutions
  - Steps and aspects of undertaking the task that takes into account the considerations. 
  - You could use a bulleted list for brevity.

This structure (task-description-considerations-solutions) should be repeated if the overall task breaks down into distinct sub-tasks.

Add any missing tools into the _data/tool_and_resource_list.yml file; when referring to a tool on the page use the {% tool "<id>" %} format. 

** Read existing pages to get inspiration

Read some of the existing task pages on RSQKit - https://everse.software/RSQKit/tasks and copy the approach of those you like and ideally align with the above.
  
** All markdown comments and page metadata comments can be removed before making a pull request.

-->


## Task (or sub-task) 

### Description 

### Considerations 

### Solutions 


## Tool or domain specific tasks <!-- OPTIONAL (remove this till end of page if not needed) -->

<!--
Use this section to list tool or domain specific (sub-)tasks. List the pages in the `child_pages:` attribute in the page metadata. Then uncomment the following, including it in the page:

{% assign child_pages = page.child_pages | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=4 %}
-->
