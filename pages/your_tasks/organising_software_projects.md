---
title: Organising software projects
description: How to organise your software project?
contributors: ["Aleksandra Nenadic"]
page_id: organising_software_projects
related_pages:
  your_tasks: [citing_software, creating_good_readme, documenting_software, software_metadata]
quality_indicators: []
training:
   - name: Training in EVERSE TeSS
     registry: TeSS
     url: https://everse-training.app.cern.ch/materials?q=%22organise+project%22
---

## Why does organising your software project matter?

### Description

The directory structure for organising your software projects (or research projects in general) 
involves creating a clear and logical layout for files and data, facilitating easy navigation, collaboration and reproducibility.
A well-structured and consistent project organisation, aligned with common practices, is essential for making your work more accessible. 
This approach helps others (and yourself) quickly locate information, which is particularly valuable for long-term projects or collaborative efforts.

### Considerations

Organising code or research project directories in a consistent manner is essential for several reasons:

- A clear structure makes it easier for you and others to understand the project's layout.
- Contributors can quickly locate necessary resources without navigating a cluttered or chaotic directory.
- Consistent naming conventions and directory structures enable efficient code sharing, review, and seamless transitions between projects that follow similar conventions.
- Proper separation of code, configuration files, and data facilitates faster issue isolation and resolution.
- In research projects, well-organised code, data, and documentation support easier result reproduction and validation.
- Well-documented and consistent directory structures help future research build upon existing work more effectively.

## What are some good practices in organising software projects?

### Description 
Below are some good practices for setting up and maintaining a software (or a research) project's directory structure and storing
code, data, results, tests, auxiliary information and metadata.

### Solution

- **Top-level directory of the project**
  - Put all files related to a project into a single directory. 
  - Choose a meaningful name that reflects the project’s purpose or topic.
  - Add `README` file to describe the project and instructions on installing and running the code and reproducing the results - see more on creating good [README files][creating_good_readme].
  - Add `LICENSE` file to describe the how others can reuse your software or work - see more on [licensing software][licensing_software].
  - Add [`CITATION.cff`][cff] file to describe how to cite the project - see more on [citing software][citing_software].
  - Add `codemeta.json` file (or similar metadata standard) to describe your software's metadata - see more on [software metadata][software_metadata].
- **Subdirectories of the project** - organise the project into sub-directories clearly labelled based on the type of their content, for example:
  - `data` - for storing your data. Further organise raw, cleaned, intermediate, and/or processed data in separate subdirectories (e.g. `data/raw`, `data/clean`, `data/processed`) to maintain clarity and prevent overwriting or losing the original raw data. 
  - `code` (or `scripts` or `src`) - for storing your source code.
  - `results` - for storing analysis outputs, summary statistics, or any data generated after processing.
  - `doc` - for storing detailed code/project description (e.g. on how the project is organised, methodologies, and file dependencies) and detailed [software documentation][software_documentation].
  - `figures` (or `fig`) - for storing all visualisations like charts, graphs, and figures generated from the code/analysis (alternatively, these can go in the `results` directory).
  - `papers` or `presentations` or `references` - a folder for research papers, articles, or any other literature cited or referenced in the research project.
  - If specific subdirectories in your project require distinct descriptions or licenses (for example, the license for your code may differ from that of your data, which is often the case), include separate README or LICENSE files in those subdirectories to apply to the files within them.
- **Naming conventions for files and directories**
  - Avoid special characters or spaces (they can cause errors when read by computers); use underscores (_) or hyphens (-) to separate words instead
  - Name files to reflect their contents, version, or date (or, even better, use version control to track different versions).
- **Version control**
  - If possible, you should put the whole software project under [version control][version_control] and in its own repository
  - At the very least, code (and data) sub-directories should be version controlled; you can also version control documentation, manuscripts, results, etc. - i.e. anything that is written manually and not generated automatically
  - If data files are too large (or contain sensitive information) to track by version control and expose in public repositories, you should untrack them (e.g. using `.gitignore` file in Git). The same goes if you are storing passwords in files - they should not be version controlled.
  - Use tags or [releases][releasing_code] to mark specific versions of results (a version submitted to a journal, dissertation version, poster version, etc.) so as to avoid using version numbers in file names and proliferation of different files.

### Example project structures

Below is an example of a directory structure for a generic research project. This is not the only way to organise your project folder (there is no official or standard way and you may not have 
all the same subfolders in your project), but it is a good practice to follow that will be understandable by many others.

```
project_name/
├── README                # overview of the project
├── LICENSE               # license (reuse terms) for the project as a whole
├── CITATION.cff          # citation information for the project
├── data/                 # data files used in the project
│   ├── README            # describe the origin of your data
│   ├── raw/              # store your raw data and do not modify it
│   └── processed/        # store cleaned/processed/modified data separately 
├── manuscript/           # manuscript describing the results
├── results/              # results of the analysis (data, tables)  
│   ├── preliminary/
│   └── final/
├── figures/              # results of the analysis (figures)
│   ├── comparison_plot.png
│   └── regression_chart.pdf
├── src/                  # contains source code for the project
│   ├── LICENSE           # license that just applies to the code
│   ├── requirements.txt  # software requirements and dependencies
│   ├── main_script.py    # main script/code entry point
│   └── ...
├── doc/                  # documentation for your software
│   ├── index.html            # entry point into the documentation website    
│   └── ...
└── ...
```

For research projects that contain code, if you are using Python - check out the following two tools:

- {% tool 'fair-python-coockiecutter' %} is a command-line template tool that can help you set up a Python software project skeleton that uses modern state-of-the-art development tools and helps you follow best practices for code and metadata quality. It generates project directories from predefined templates and ensures consistency by scaffolding a standardised project layout, including folders like `src/` for code, `tests/` for tests (shown below), and configuration files such as `pyproject.toml`, `README`, and `.gitignore`. This is especially helpful for teams or when starting new software projects, as it reduces setup time and enforces best practices.
-  {% tool "poetry" %} is a dependency and packaging manager that simplifies Python project management. It uses a single `pyproject.toml` file to declare dependencies, manage virtual environments, and handle versioning and publishing.
In addition, {% tool "poetry" %} will also create a new directory with the necessary structure for you if you are starting a new Python project from scratch.
{% tool "poetry" %} itself does not enforce a specific directory structure, but it encourages and works well with the "src layout" (shown below), which is a widely adopted best practice in modern Python development (as does {% tool 'fair-python-coockiecutter' %}).

```
project_name/
├── pyproject.toml         # Poetry config: dependencies, metadata, build system
├── README.md              # Project description
├── src/                   # Source code root (recommended layout)
│   └── your_package/      # Actual Python package/module
│       ├── __init__.py
│       └── ...
├── tests/                 # Unit and integration tests
│   └── test_something.py
└── .gitignore
```

For best practices and guidance for designing research projects in particular focused on data - check out [the Turing Way Project's Guide for project design][turing-project-design]. 

[creating_good_readme]: ./creating_good_readme
[licensing_software]: ./licensing_software
[releasing_code]: ./releasing_software
[software_documentation]: ./documenting_software
[version_control]: ./using_version_control
[software_metadata]: ./software_metadata
[cff]: https://citation-file-format.github.io/
[citing_software]: ./citing_software
[turing-project-design]: https://book.the-turing-way.org/project-design/pd-design-overview/project-repo/project-repo-advanced
[directory-structure-poetry]: https://medium.com/@sjalexandre/python-tutorial-managing-projects-with-poetry-cd2deab72697
