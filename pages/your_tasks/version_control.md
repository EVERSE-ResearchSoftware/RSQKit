---
title: Version control
description: Version control systems in research software engineering
contributors: ["Giacomo Peru"]
page_id: version_control
related_pages:
  your_tasks: []
---

## How do I choose the right version control system for my research project?

### Description

Selecting an appropriate version control system (VCS) is crucial for managing research software effectively. 
This decision impacts collaboration, data management, and long-term project sustainability.

### Considerations

* Project size and complexity
* Team size and geographical distribution
* Types of files (code, data, documents)
* Required integrations with other research tools
* Team's technical expertise
* Long-term goals and potential for open-source contribution
* Handling of large binary files common in research
* Compliance with institutional policies and grant requirements

### Solutions

* For most research projects, choose {% tool "git" %}:
   * Widely used in both academia and industry
   * Excellent for collaborative work and open-source projects
   * Large ecosystem of tools and hosting platforms ({% tool "github" %}, {% tool "gitlab" %})
* For projects with large binary files, consider:
   * {% tool "git-lfs" %} (LFS)
   * {% tool "perforce" %} , if dealing with extremely large datasets
* For teams new to version control:
   * Start with {% tool "git" %}, but provide thorough training
   * Consider {% tool "mercurial" %} as an alternative if {% tool "git" %} proves too complex
* For projects requiring strict access control - {% tool "subversion" %} (SVN) might be suitable, though less modern

## How do I implement version control in my research workflow?

### Description
Implementing version control in a research context involves more than just choosing a system. It requires establishing workflows, educating team members, and integrating with existing research practices.

### Considerations
* Current data management practices
* Reproducibility requirements of your research
* Collaboration patterns within your team and with external partners
* Integration with data analysis pipelines and tools
* Publication and open science practices
* Long-term archiving of research outputs

### Solutions
* Establish a clear workflow:
   * Define a branching strategy (e.g., Git Flow for larger projects)
   * Set guidelines for commit messages and code reviews
* Integrate with your development environment:
   * Set up your Integrated Development Environment (IDE), such as {% tool "vscode" %}, {% tool "rstudio" %}, {% tool "pycharm" %} or {% tool "eclipse" %}, or a text editor to work with your VCS
   * Implement continuous integration for automated testing
* Educate your team:
   * Provide training on basic VCS concepts and commands
   * Create documentation for your specific workflow
* Ensure reproducibility:
   * Use tags to mark versions used in publications
   * Include configuration files and dependencies in version control
* Facilitate collaboration:
   * Use a platform like GitHub or GitLab for easy sharing and collaboration
   * Implement code review practices to maintain quality
* Maintain your repository:
   * Regularly backup your repository
   * Periodically clean up old branches and review access permissions


