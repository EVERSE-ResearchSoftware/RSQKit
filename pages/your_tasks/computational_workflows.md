---
title: Computational workflows
description: How to use computational workflows to automate and reproduce data pipelines?
contributors: [ "Aleksandra Nenadic"]
page_id: computational_workflows
related_pages:
  your_tasks: [reproducible_software_environments]
---


## What are computational workflows? 

Computational workflows are a special kind of software that **automate** multi-step, multi-code data 
pipelines, data analyses, and other data-handling operations, especially through the efficient use of computational 
resources to transform data inputs into desired outputs.

Computational workflows have two prominent characteristics:

1. workflows consist of a series (or a structure) of **interconnected components** that may include other workflows, 
software, code snippets, tools, or services. The workflow defines the order, structure, and logic governing how 
these components interact to process data from inputs to final outputs.
2. workflows **abstract** the flow of data between the components from the run mechanics in some form of a high-level 
**workflow definition language**.
Workflow definitions detail inputs, dependencies, computational environment, step definitions, conditional logic, 
parallelism, etc. A dedicated **workflow management system (WMS)** is typically responsible for executing the 
workflow based on its definition, handling and tracking data (provenance), task scheduling and resource management.

At the simplest end of the complexity spectrum, a workflow might consist of a script (e.g. Bash, Python, R) or 
enumerated stages in an electronic research notebook (e.g. Jupyter, RStudio, Apache Zeppelin, etc.) with a set of 
instructions that use inputs and outputs to pipe the results together.

At the more sophisticated end, workflows might employ workflow management systems such as {% tool "nextflow" %}, {% tool "galaxy" %},
{% tool "snakemake" %}, {% tool "apache-airflow" %} or {% tool "parsl" %} using a variety of high-level workflow definition 
languages (such as [Nextflow Domain Specific Language (DSL)][nextflow-dsl], [Snakefile][snakefile], 
[Workflow Description Language (WDL)][wdl], [Common Workflow Language (CWL)][cwl], [Apache Airflow DAG][apache-airflow-dag]).

In practice, researchers use mixtures of techniques from across the spectrum, such as chaining scripts from a WMS
that in turn is launched from a electronic research notebook.

## Why should I use computational workflows?

Using computational workflows offers several significant benefits for researchers dealing with complex or 
repetitive data processing and analysis tasks, including:

- **reproducibility** - workflows formalise each step of your analysis, including data inputs, tools used, parameters, 
and environment. This ensures that anyone (including your future self) can reproduce the same results by rerunning the workflow.
Read more on other aspects of [reproducible software environments](./reproducible_software_environments).
- **automation, efficiency and scaling** - once defined, a workflow can run automatically without manual intervention. 
This saves time, reduces human error, and makes it easier to repeat analyses across different datasets or experiments.
- **scalability and resource management** - WMSs can handle large-scale data and distribute tasks across HPC clusters or 
cloud resources efficiently — ideal for data-intensive research that would be impossible on individual machines.
- **transparency and provenance** - workflows serve as living documentation of your research process. 
They make your methods clear and transparent to collaborators, reviewers, and the broader community.
- **modularity and reuse** - similar to software code being built from functions and modules, workflows are built from 
smaller components that can be reused or swapped out. This makes your research more modular and easier to adapt to 
new questions or datasets.
- **collaboration and sharing** - clearly defined workflows enable easier discovery, collaboration across teams and disciplines. 
Everyone can understand and run the same processes, even across different systems.

## Describing & discovering workflows

How can we document and share our computational workflows and find other people's workflows for reuse?

**Workflow metadata** is descriptive information *about* a workflow — its purpose, requirements, inputs/outputs, 
dependencies, authorship, and provenance. Its purpose is slightly different to that of a workflow definition language,
which defines the workflow logic and tells a WMS *how* to execute it (e.g., for automation, parallelisation, and scheduling).
Workflow metadata is not for running the workflow but for understanding, managing and discovering it.

[Workflow RO-Crate][wf-ro-crate] is a lightweight, structured metadata format designed to package and describe computational workflows 
and their associated resources in a FAIR-compliant way, extending the more general [Bioschemas ComputationalWorkflow Profile][bioschemas-wf-profile]. 
It builds on the [RO-Crate][ro-crate] metadata standard to encapsulate not only the 
workflow definition (e.g. CWL, Nextflow DSL, Snakefile) but also key contextual information such as inputs/outputs (via [Bioschemas FormalParameter](bioschemas-formal-parameter), 
software dependencies, authorship, and execution environment. By using Workflow RO-Crate, researchers can make their 
workflows more discoverable, portable, and reproducible—enabling others to understand, reuse, and re-run analyses 
with greater ease and confidence. It simplifies workflow sharing, supports interoperability, and is especially useful 
for publishing workflows alongside datasets or in workflow registries.

Workflow RO-Crate is the metadata standard used by {% tool "workflowhub" %} registry and {% tool "lifemonitor" %} service 
for publishing computational workflows, enabling researchers to share, discover, and reuse 
workflows with rich, structured descriptions that support reproducibility and the FAIR principles.

## Integration with the FAIR principles

As digital objects to be shared, discovered, and reused, computational workflows benefit from adhering to [the 
FAIR principles](./fair_rs) in general and specifically the [FAIR recommendations for workflows][fair-workflows].
It can maximise their quality and value as research assets and facilitate their adoption by the wider community, which is essential for [modern research data management][rdmkit].

The [Workflows Community Initiative’s FAIR Workflows Working Group (WCI-FW)][WCI-FW], a global and open community of
researchers and developers working with computational workflows across disciplines and domains, has systematically
addressed the application of both FAIR data and software principles to computational workflows.


[apache-airflow-dag]: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
[cwl]: https://www.commonwl.org/
[wdl]: https://openwdl.org/
[snakefile]: https://snakemake.readthedocs.io/en/stable/snakefiles/writing_snakefiles.html
[nextflow-dsl]: https://www.nextflow.io/docs/latest/reference/syntax.html
[rdmkit]: https://rdmkit.elixir-europe.org/
[WCI-FW]: https://workflows.community/groups/fair/
[fair-workflows]: https://doi.org/10.1038/s41597-025-04451-9
[wf-ro-crate]: https://about.workflowhub.eu/Workflow-RO-Crate/
[ro-crate]: https://www.researchobject.org/ro-crate/\
[bioschemas-wf-profile]: https://bioschemas.org/profiles/ComputationalWorkflow/1.0-RELEASE
[bioschemas-formal-parameter]: https://bioschemas.org/types/FormalParameter/1.0-RELEASE
