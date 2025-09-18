---
title: Researcher who codes
page_id: researcher_who_codes
contributors: ["Robert Speck", "Aleksandra Nenadic"]
description: Software development and quality guidance for researchers who code
---

Researchers who code are academics or research domain experts who write software or scripts as part of their research workflow.
Their main focus is research, not the software — but coding is often essential for data analysis, simulations, modelling or automation in research.
They may come from disciplines like physics, life sciences, environmental sciences, humanities, etc. and their coding skills are often self-taught and developed organically out of necessity rather than formal training.
When compared to the role of an [Research Software Engineer (RSE)](./research_software_engineer) - whose primary goal is to build sustainable, reliable, and reusable software to support research often in different domains - the primary goal of researchers who code is to conduct novel research and use code to solve domain-specific problems and they focus on scientific questions, experimentation, and data interpretation.

While the term RSE is well established in many countries, not everyone involved in writing research software identifies with it.
Many researchers—whether they are physicists, biologists, engineers, or social scientists — prefer to define themselves by their domain rather than by their software contributions.
This broad community may not formally fall under the RSE label, but they still benefit greatly from adopting research software engineering practices.
Whether it is publishing code, choosing a license, or writing tests, these skills are essential for anyone developing software in a research context.
The term "researcher who codes" helps acknowledge and include this group — meeting them where they are, without requiring a shift in professional identity.
Primary focus and responsibilities of Research Software Engineers (RSEs) and researchers are compared in the table below.

| RSE                                                                                        | Researcher who codes                                                                                                       | |--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------| | Has deeper knowledge of software development practices (e.g., testing, CI/CD, versioning)  | Has basic to intermediate programming knowledge (often self-taught); but may have more advanced skills and knowledge without realising it                                                         | | Writes modular, maintainable, and reusable code, often across multiple projects or domains | Typically writes code (e.g., analysis scripts, simulations, prototype code) within a single project with short-term use; some are more advanced in their practice and increasingly write code with long-term usage in mind              | | Works alongside researchers to translate scientific problems into robust software          | Often works independently or with small teams, focusing on specific hypotheses or experiments                                    | | Builds workflows, automation pipelines, and scalable systems                               | Builds own scripts or uses existing tools and scripts to test hypotheses or analyse data                                   | | Aims to develop general-purpose tools or infrastructures usable by others                   | Writes code that is usually designed to support one research project or paper, and may not be intended for reuse by others (but this is also changing as focus shifts to sharing and reusability) | | Employs software engineering practices - software architecture, documentation and testing  | Often prioritises results over engineering - the emphasis is on getting results that support research goals                      |

## Software development & quality responsibilities, challenges & tasks

These are the key software-related things a researcher who codes is typically responsible for:

- Developing research-driven code to implement analyses, simulations, or models
- Processing and visualising data using scripting languages like Python, R, or MATLAB
- Managing research data — reading, transforming, cleaning, and storing data for analysis
- Organising project files and scripts in a way that supports reproducibility (to varying degrees)
- Documenting code (even minimally) to recall how it works or explain it in papers
- Validating results via debugging or comparing outcomes across test cases
- When projects grow more complex, researchers who code often benefit from working with [RSEs](./research_software_engineer) to improve code quality, scalability, and reusability.

## Software development & quality guidance

- [Organising software projects](./organising_software_projects) - a well-structured project directory facilitates collaboration, maintenance, and reproducibility
- [Adopting FAIR principles](./fair_rs) promotes transparency and facilitates wider adoption of research software
- Code quality best practices - [version control](./using_version_control), [testing](./testing_software), [documentation](./documenting_software) and [licensing](./licensing_software)
- [Software testing practices](./testing_software) and automating tests using [Continuous Integration](./ci_cd) (CI)
- Engaging in [code reviews](./code_review) - regular code reviews contribute to code quality and facilitate knowledge sharing among team members.