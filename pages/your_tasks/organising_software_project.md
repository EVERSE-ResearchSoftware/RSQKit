---
title: How to organise your software project's directory
description: Good practice for organising files in a software project (or a research project in general) 
contributors: ["Aleksandra Nenadic"]
page_id: organising_software_project
related_pages:
  your_tasks: [how_to_make_a_good_readme, licensing_software, releasing_code, software_documentation]
---

## Why does it matter how we organise our software project's directory?

### Description

The directory structure for organising your software projects (or research projects in general) 
involves creating a clear and logical layout for files and data, ensuring easy navigation, collaboration and reproducibility.
One of the first steps that you should take to make your work more reproducible is to organise your projects well and consistent 
with commonly used practices - ensuring that people immediately know where to find things within your project, which is especially helpful 
for long-term projects or when working in teams.

### Considerations

Organising code or research project directories is important for several reasons:

- Clear structure makes it easier for you and others to understand the project's organisation.
- Future contributors can quickly find what they need without spending time deciphering a chaotic directory.
- Consistent naming and directory structures help team members share and review code or data efficiently and easily switch to 
other projects that follow similar naming and structure conventions.
- Proper separation of code, configuration files, and data helps in isolating and fixing bugs faster.
- For research projects - well organised code, data and documentation enable others to reproduce and validate results more easily.
- Well-documented directory structures ensure future research builds on existing work efficiently.

## What are some good practices in organising software projects?

### Description 
Below are some good practices for setting up and maintaining a software (or a research) project's directory structure and storing
code, data, results, tests, auxiliary information and metadata.

### Solution

- **Top-level directory of the project**
  - Put all files related to a project into a single directory. 
  - Choose a meaningful name that reflects the project’s purpose or topic.
  - Add a README file to describe the project and instructions on reproducing the results - see more on creating [README files][how_to_make_a_good_readme].
  - Add a LICENSE file to describe the how others can reuse your software - see more on [licensing software][licensing_software]. If you need separate licences for 
  aspects/subdirectories of your project (e.g. licence for your code may (and normally will) be different to that of your data) - include LICENSE files there as well.
- **Subdirectories of the project** - organise the project into clear, well-labeled sub-directories based on the type of content. Common categories include:
  - `data` - store raw, intermediate, and processed data in separate sub-directories to maintain clarity and avoid overwriting and losing your raw data.
  - `code` (or `scripts` or `src`) - for storing your source code.
  - `results` - for storing analysis outputs, summary statistics, or any data generated after processing.
  - `doc` - include a detailed project description and [documentation][software_documentation] on how the project is organised, methodologies, and file dependencies.
  - `figures` (or `fig`) - store all visualisations like charts, graphs, and figures generated from the analysis (these can also go in the results directory).
  - `papers` or `presentations` or `references` - a folder for research papers, articles, or any other literature cited or referenced in the research project.
- **Naming conventions for files and directories**
  - Avoid special characters or spaces (they can cause errors when read by computers); use underscores (_) or hyphens (-) to separate words instead
  - Name files to reflect their contents, version, or date (or use version control to track different versions).
- **Version control**
  - If possible, you should put the whole software project under version control and in its own repository
  - At the very least, code (and data) subdirectories should be version controlled; you can also version control documentation, manuscripts, results, etc. - i.e. anything that is written manually and not generated automatically
  - If data files are too large (or contain sensitive information) to track by version control, you should untrack them (e.g. using `.gitignore` file in Git). The same goes if you are storing passwords in files - they should not be version controlled.
  - Use tags or [releases][releasing_code] to mark specific versions of results (a version submitted to a journal, dissertation version, poster version, etc.) so as to avoid using version numbers in file names and proliferation of different files.

Below is an example of a directory structure for a generic research project.

```
project_name/
├── README                # overview of the project
├── LICENSE               # license (reuse terms) for the project as a whole
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
├── doc/                  # documentation for your project
├── index.html            # entry point into the documentation website    
└── ...
```


[how_to_make_a_good_readme]: /how_to_make_a_good_readme
[licensing_software]: /licensing_software
[releasing_code]: /releasing_code
[software_documentation]: /software_documentation