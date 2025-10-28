---
title: Software documentation
description: How do you document your software (code and project) for use by various different audiences?
page_id: software_documentation
contributors: ["Azza Gamgami", "Aleksandra Nenadic", "Laura Portell-Silva"]
child_pages: [documenting_software_project, documenting_code]
quality_indicators: [software_has_documentation]
#keywords: ["software documentation", "documentation", "code documentation", "code comments", "readme", "mkdocs", "readthedocs"]
page_citation: false
---

Software documentation is an essential part of the software development process, designed to provide clear communication between various stakeholders including developers, administrators, testers, users and project managers. 

Good documentation is essential for making research software understandable (easy to read), reusable (its functionality can be effectively extended or reused), and sustainable (easy to maintain).
It helps others (and your future self) know what your software does, how to use it, and how to contribute to it.

There are two main aspects of software documentation:

* Project documentation — describes the software as a whole: its purpose, audience, installation instructions, usage examples, licensing, and contribution guidelines. 
This information typically appears in files such as a README, INSTALL, or CONTRIBUTING, and helps users and collaborators understand how to work with the project.
* Code documentation — explains how the code works internally. 
This includes, for example, comments, docstrings, software architecture and API documentation that describe the functions, classes, and modules. Code documentation supports developers who maintain or extend the code by making its logic and structure easier to follow.

Both levels are important: project documentation helps people use and adopt your software, while code documentation helps people develop and sustain it.

{% assign child_pages = page.child_pages | join: ', ' %}
{% include section-navigation-tiles.html type="tasks" custom=child_pages training=false sort=false col=3 %}
