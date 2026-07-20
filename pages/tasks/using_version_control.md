---
title: Using version control
description: How do you choose and implement version control for your research software?
contributors: ["Giacomo Peru"]
page_id: using_version_control
related_pages:
  tasks: []
quality_indicators: [version_control_use]
keywords: ["version control", "source control", "git", "github", "gitlab"]

---
## Why does version control matter for your research software?
 
### Description
 
Without version control, most researchers end up managing change through file naming. This approach breaks down quickly, and you lose track of what changed, you cannot recover a working state without manually comparing files, and collaborators overwrite each other's work.
Version control solves all of this by recording a complete, searchable history of every change to your project, so you can always see what changed, when, why, and who made the change.

### Considerations
 
* Every change you commit is stored as a snapshot with a timestamp, your name, and a message you write, so the history of your project becomes a reliable record, not a guess.
* Version control tracks changes *inside* files, not just whole-file copies, which means two collaborators editing different parts of the same file can usually merge their work automatically.
* Branching lets you experiment on a parallel copy of your project without touching the version that works, so you can try something risky and discard it cleanly if it fails.
* A version-controlled project is recoverable: if something breaks, you can return to any earlier snapshot rather than trying to manually undo changes.
* Reproducibility in research depends on knowing exactly which version of your code produced a given result; version control makes that traceable.

### Solutions
 
* Understand the distinction between {% tool "git" %} and platforms like {% tool "github" %} or {% tool "gitlab" %}, they are separate things.
  * {% tool "git" %} is the version control system itself; it runs on your own computer and needs no internet connection.
  * {% tool "github" %} and {% tool "gitlab" %} are websites that host a copy of your git repository online, giving you a remote backup, a place to collaborate, and tools for discussing and reviewing changes.
* Start by tracking your project's code, configuration files, and dependency lists, the text-based files that define how your software works.
* Commit often and write clear messages: a message like "fix normalisation bug in preprocessing step" is useful six months later; "update" is not.
* Use tags to mark the exact commit that produced results reported in a paper or report, so you can always return to the precise state your results came from.


## How do you choose the right version control system for your research project?

### Description

Choosing the right version control system (VCS) shapes how easily you and your collaborators can track changes, recover earlier work, and merge contributions without overwriting each other.
The right choice depends on your project's size, the types of files you work with, and how your team is structured.
Getting this decision right early saves you from a painful migration later, once your history and workflows are already built around the wrong tool.

### Considerations

* Project size and complexity: Your project's size and complexity affect how much branching and merging overhead is worth taking on.
* Team size and geographical distribution: Your team's size and geographical distribution determine how much you rely on remote collaboration features.
* Types of files: The types of files you track (code, data, documents) affect which VCS handles them well; most systems are built for text, not large binaries.
* Required integrations with other research tools: Any required integrations with other research tools, such as notebooks, pipelines, or data repositories, can narrow your options.
* Team's technical expertise: Your team's existing technical expertise affects how steep a learning curve you can realistically absorb.
* Long-term goals: Your long-term goals, including any plans to open-source the project, affect which platforms and licenses fit best.
* Compliance with institutional policies and grant requirements: Institutional policies or grant requirements may dictate where and how your data and code can be stored.

### Solutions

* For most research projects, choose {% tool "git" %}:
   * It is widely used in both academia and industry, which makes it easier to find collaborators, documentation, and support.
   * It works well for collaborative and open-source projects.
   * It has a large ecosystem of hosting platforms, including ({% tool "github" %} and {% tool "gitlab" %})
* For projects with large binary files, consider {% tool "git-lfs" %} to keep your repository fast, or {% tool "perforce" %} if you are dealing with extremely large datasets.
* For teams new to version control, start with {% tool "git" %} but invest in proper training; {% tool "mercurial" %} is a reasonable alternative if {% tool "git" %}'s model proves too complex at first.
* For projects requiring strict access control - {% tool "subversion" %} (SVN)  can still be a suitable choice, though it is less commonly used for new projects today.
* These recommendations reflect common practice at the time of writing; verify current tool popularity and feature sets before committing to one, since the landscape shifts over time.


## How do you implement version control in your research workflow?

### Description 

Choosing a VCS is only the first step. You also need to establish a working routine: how you structure commits, how you collaborate with others, and how you connect version control to the rest of your research process. Without this, you can have git installed and still lose track of what changed, when, and why.

### Considerations

* Current data management practices: Your current data management practices affect how much of your workflow you can fold into version control versus what stays separate.
* Reproducibility requirements of your research: Your research's reproducibility requirements shape how rigorously you need to tag, document, and preserve specific versions.
* Collaboration patterns within your team and with external partners: Your collaboration patterns, both within your team and with external partners, affect what branching and review process makes sense.
* Integration with data analysis pipelines and tools: How your VCS integrates with your data analysis pipelines and tools determines how much friction you will feel day to day.
* Publication and open science practices: Your publication and open-science practices may require you to make specific versions of your code citable and permanently accessible.
* Long-term archiving of research outputs: Your plans for long-term archiving of research outputs affect where and how you store your repository beyond your own machine.

### Solutions

* Establish a clear workflow:
   * Define a branching strategy appropriate to your project's size, something like Git Flow can help for larger projects, but a single main/master branch with short-lived feature/dev branches is often enough for smaller projects.
   * Set guidelines for commit messages and code review, so changes are easy to understand later.
* Integrate version control into your development environment:
   * Set up your Integrated Development Environment (IDE), such as {% tool "vscode" %}, {% tool "rstudio" %}, {% tool "pycharm" %} or {% tool "eclipse" %}, or a text editor to work with your VCS
   * Add continuous integration so tests run automatically on each change.
* Train your team:
   * Cover the core concepts and commands first; depth can come later.
   * Create documentation for your specific workflow
* Protect reproducibility:
   * Use tags to mark versions used in publications
   * Include configuration files and dependencies in version control
* Support collaboration:
   * Host your repository on a platform such as {% tool "github" %} or {% tool "gitlab" %} so others can find, fork, and contribute to it.
   * Use code review, through pull or merge requests, before merging changes into your main branch.
* Maintain your repository over time:
   * Regularly backup your repository
 * Automate cleanup where possible: enable the "delete source branch" option on merge/pull requests so feature branches are removed as soon as they're merged.
* Periodically clean up any remaining stale branches and review who has access.

{% assign child_pages = page.child_pages | join: ', ' %}
{% if child_pages != null and child_pages != '' %}
## Tool- or Domain-Specific Tasks

This is a suggested list tool-specific sub-tasks to have a look at.

{% include section-navigation-tiles.html type="tasks" custom=child_pages sort=false col=2 %}
{% endif %}

## Further Reading
 
- **[Pro Git book](https://git-scm.com/book/en/v2)** — The free, comprehensive reference for git, written by its maintainers. Useful once you have the basics and want to go deeper into branching models, internals, and advanced workflows.
- **[GitHub Docs: Getting started](https://docs.github.com/en/get-started)** — GitHub's own onboarding guide, covering repository setup, collaboration, and pull requests. A practical starting point if you are new to hosting and sharing a git repository.
- **[Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/)** — A hands-on, lesson-based introduction to git aimed at researchers with no prior version control experience. Particularly good if you prefer learning by working through exercises rather than reading documentation.
- **["Ten Simple Rules for Taking Advantage of Git and GitHub" (Perez-Riverol et al., 2016)](https://doi.org/10.1371/journal.pcbi.1004947)** — A peer-reviewed paper aimed at researchers and research software engineers, framing git and GitHub adoption specifically around scientific reproducibility and collaboration.


## AI Disclosure
 
This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
