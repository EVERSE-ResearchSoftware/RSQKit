---
title: "The name of your research software exemplar or use case" # short title - this is usually your software project name
search_exclude: true # set to false if you want this page to show up in search results (it's 'true for the template as we don't want that in search results)
description: "" # a description of the page - A brief description of the exemplar or use case and which problem it solves and which domains (or if its cross domain) it applies to. 
contributors: [] # a comma separated list of contributors' names, as found in _data/CONTRIBUTORS.yml (add yourself to the files if you do not have an entry)
page_id: # unique page id, ideally lowercase words separated by underscore(s) - for example page_id of 'Galaxy' could be galaxy
type: research_software_story
---

<!-- Please keep all sections and fill them in.
If this is not possible for any reason - you may remove them (you might need to explain to the Editorial Board in your pull request why certain sections are not present).
The text describing what is needed in the sections can be removed.
All comment sections can be removed before your submit a pull request.
-->

<!-- Once you have completed your research community entry - please add it to _data/sidebars/main.yml under the Research Software Stories entry in alphabetical order.
This comment can be deleted in your final page.
-->


## The Problem <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle for the description of the problem

Describe the problem(s) your software is trying to solve for your community.

**What scientific or practical problem does the software solve?**

**Questions:**

- What was difficult, fragile, slow, or unreliable before this software existed?
- What scientific question or workflow needed improvement?
- Why was existing tooling not enough?
- What assumptions sit behind the problem?
- What boundaries or limitations define the scope?

*Write 2-3 full sentences first, then add bullets if helpful.*


## The Community <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about the community/communities that use or will potentially use this software

Describe the community that uses your software


- Describe how the development is organised (e.g. is it one person, many, how are they organised and/or governed)
- Who are the users - how experienced are they in using your software?

**Who builds the software and who uses it?**

**Questions:**

- Who are the developers and contributors?
- Who relies on the software in their research?
- What roles or expertise are involved?
- How do these groups interact?
- Are there gaps, risks, or single points of failure?

*2-3 full sentences, then optional bullets.*

## Technical Aspects <!-- do not delete this heading and write your text below it -->

- What is the tier(s) of software involved (e.g. analysis code, prototype tools, research software infrastructure (including services))
- Technical specifications:
   - language(s)
   - any measures of the codebase (e.g. size, complexity, activity, how long it's been running)
   - deployment requirements (e.g. does it need a HPC infrastructure - what compute/data or contextual requirements does it require)

**What is the software, technically?**

**Questions:**

- What type of software is it (analysis tool, prototype, workflow, service…)?
- Which languages, frameworks, or technologies does it use?
- How large or complex is the codebase?
- What constraints shape it? (data size, performance, domain-specific rules)

*Begin with full sentences.*

### Libraries and Systems <!-- do not delete this heading and write your text below it -->

- List any domain/community specific libraries and systems you make use of in your software solutions.

**What major libraries, systems, or ecosystems does the software depend on?**

**Questions:**

- What scientific libraries, frameworks, or APIs does it rely on?
- Which external systems does it integrate with?
- What data formats or domain tools must it support?
- What does someone need to know before contributing?

*Write 2-3 clear sentences before listing items.*

## Software Practices <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about which software practices are being used and their benefits to the user community

- What practices do you use to develop the software (e.g. version control, contribution policy, licensing, other practices)?
- What benefits have the developers gained in building their software by applying these software quality practices?

**What practices guide development and collaboration?**

**Questions:**

- How do you use version control?
- Is there code review? Testing? Release processes?
- How are decisions made?
- How do people communicate about changes?
- What's informal but still important?

*First: 2-3 sentences capturing reality as it is.*

## Community <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about how the software is being adopted for usage and how a community is being built around it

- How do you onboard new developers?
- How do you onboard new users?
   - Explain your main user stories (the main types of users, what they want to achieve and what the benefit to them is) 

**How do new users and developers start using or contributing to the software?**

**Questions:**

- What is a typical user (developer) journey?
- What do new contributors usually do first?
- What examples, notebooks, wikis, or tutorials exist?
- How do people learn the workflow?
- What obstacles do newcomers face?

*Write full sentences about the “on-ramp”, then add bullets.*

## Tools <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about the other tools that help in improving your research software  

- List any tools that you use to help you improve or assess the software quality of your code and a short description of how they help your software. Please refer to [_data/tool_and_resource_list.yml](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/tool_and_resource_list.yml) file in the RSQKit repository and add any ones that are missing.
- What has been the benefit to the project of using these tools?

**Questions:**

- What linters, formatters, CI systems, test runners, or similar are used?
- How do you containerise or package the environment?
- What workflow or documentation tools help keep things stable?
- Which of these tools make daily development easier?

*Begin with sentences; bullets optional.*

## FAIR & Open <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about how your research software is aligned with FAIR and/or Open practices

 - FAIR: see the [FAIR software page in RSQKit](https://everse.software/RSQKit/fair_rs) and [Five recommendations for FAIR software](https://fair-software.eu/) for inspiration - e.g. are there a repository and a license, do you have a community registry/catalogue where the code is available, is it citable, do you have a “good software” checklist?
 - Open: cover how you follow open source practices and open development practices?
 - What has been the benefit of following these open source and open development practices?

**How does your software align with FAIR principles and open practices?** *2-3 sentences*

**Questions:**

- Is the code publicly findable? How?
- What licence do you use?
- How can others access the software and its documentation?
- What formats or standards promote interoperability?
- How can others reuse or build on your work?
- How open is the development process?

## Documentation <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about how documenting the research software helps the user community using the research software

 - How is the documentation for your software presented and maintained?

**What documentation exists, and where is it?**

**Questions:**

- Where is the main entry point?
- What forms of documentation exist (README, wiki, notebooks…)?
- What is missing or incomplete?
- What do users find most useful right now?
- What do *you* wish existed?

*Write sentences first, then bullets for specifics.*


## Sustainability <!-- do not delete this heading and write your text below it -->
### Add a short one-two liner subtitle about how is the research software being made sustainable

- How is the software development lifecycle managed, e.g. are there any governance structures in place?
- How active is the project? 
- How is it funded?
- How is the software maintained during and beyond the end of funding?

**How is the software managed, maintained, and supported over time?**

**Questions:**

- Who maintains it?
- How active is the project?
- What governance (formal or informal) exists?
- What funding supports development or maintenance?
- What risks or future uncertainties matter?
- What plans exist beyond current grants?

*Begin with a few sentences. Clarity beats detail.*

## References <!-- do not delete this heading and write your text below it -->

If this page has been inspired or derived from other resources, make sure to reference them here.

**What external material shapes or supports the project?**

**Questions:**

- Documentation
- Tools
- Research papers
- External standards
- Anything the story builds upon

*Write 1-2 sentences, then list items.*
