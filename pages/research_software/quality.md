---
title: Quality of Research Software
---

## What Questions Should I Ask About My Research Software?

When thinking about the **quality of our research software** in practice, we might start by asking ourselves:

- If I run this code again tomorrow, will I get the same result?
- Can someone else reproduce my analysis using my code and data?
- How do I know my code is doing what I think it’s doing?
- If I change something, could it break something else?
- Would another researcher be able to understand, run, and build on my software?
- Is my software efficient — does it make good use of time and computational resources?
- Can I and my collaborators maintain and update it easily as my research evolves?

**Quality** here means the software supports reliable, efficient, maintainable, and trustworthy research.
One of the biggest indicators of that quality is **reproducibility** — can someone else (or my future self) run this software again and get the same results with the same data and environment?

Asking these kinds of questions helps ensure that the software we write can be trusted, shared, and built upon — which in turn makes our research more transparent and verifiable.
Developing reproducible and quality computational research often means adopting new tools and habits — but it is an investment that pays off in credibility and collaboration.

RSQKit is here to help with that - it is designed to help researchers turn reflective questions about their software into practical steps for improving quality and reproducibility.
Rather than starting from abstract standards, it begins with the kinds of questions researchers naturally ask when using or sharing their code — and then connects those questions to recognised software quality aspects.
RSQKit provides [guidance](./tasks), examples, and [tools](all_tools_and_resources) used successfully across research communities to develop software that is reproducible and reliable.


## Aspects of Research Software Quality

These questions can be translated into software quality aspects — the foundations of reproducible and trustworthy research software - for example:

- **Consistent and deterministic behavior** - the software produces the same results given the same inputs, every time.
- **Version control** - enabling people to track the exact version of the software used for a given result, along with dependencies, parameters, and instructions for use (**software documentation**).
- **Automated testing** - ensuring that the code produces correct results for each test case and that changes to code 
do not break previous behavior or introduce unexpected bugs and that tests are run on each and every code change in a automated fashion.
- **Environment management** - using tools like containers or environment files allows others (and ourselves) to replicate the computational environment.
- **Clear** and **accessible** code - making sure the code is **readable**, well-structured, and includes **documentation** that explains how to use and understand it.
- **Efficiency** – the software performs its tasks in a reasonable time and uses computational resources effectively, minimising unnecessary CPU or memory usage, avoiding redundant disk writes, and using data structures and algorithms that scale appropriately with the size of the problem. 
- **Maintainability** – the codebase is structured in a way that makes it easy to update, fix, or extend without introducing errors — supporting the longevity of research projects.

These aspects are more [formally defined][rs_quality_dimensions] as dimensions of software quality and related indicators (see below) that can help assess and improve quality aspects.

### FAIR Research Software

[FAIR software][fair-rs-nature] — i.e. software that is Findable, Accessible, Interoperable, and Reusable — sits squarely within the broader umbrella of **quality research software**.
Quality software has many aspects, including correctness, usability, robustness, maintainability, performance and reproducibility, among others.

Reproducibility often hinges on the [FAIR principles][fair-rs-nature]: if your code and documentation and auxiliary information about your code (called software metadata) are not findable or accessible, no one can rerun it; if it is not interoperable or reusable, others cannot adapt or extend or use it to verify your results.

FAIR is not a completely separate concern — it is a crucial subset of quality, primarily ensuring that your software can actually be discovered, understood, and exercised by others (or by you, months down the line).
A truly high-quality, reproducible research software package will typically satisfy both classical software-engineering criteria (tests, style, documentation, performance) and the FAIR principles.

So, adopting the [FAIR software practices][fair_rs] - the “openness & reusability” slice of software quality - is essential for reproducibility, but most impactful when combined with all the other [quality practices](rs_quality_dimensions) like [testing][testing_software], [version control][using_version_control], and [robust software design][robust_software_design].

## Software Quality Dimensions & Indicators

Quality dimensions (or characteristics) represent high-level categories of software attributes. 
They define "what" quality looks like in a specific context. 
For example, the ISO/IEC 25010 standard defines dimensions such as Maintainability, Security, and Performance Efficiency. They are often qualitative and reflect the needs of stakeholders (users, developers, or maintainers).

Quality imdicators (or metrics) are measurable, objective variables used to assess the status of a specific dimension. 
An indicator provides the evidence required to determine if a dimension is being satisfied. 
For example, "Unit Test Coverage" is one of the indicators for the Reliability dimension.

See the related page on [software quality dimensions in RSQKit](rs_quality_dimensions) where we cover the [definitions of the dimensions](quality-dimensions) and links to associated tools in [TechRadar](techradar).

See the [all indicators page](all_indicators) where we list [software quality indicators](indicators), their definitions and related RQDKit task pages.

The EVERSE project (the home of RSQKit) is working on formally defining a number of research software [quality dimensions][quality-dimensions] and their associated [indicators](https://w3id.org/everse/i/indicators) (which are to be used to assess the quality of software), based on [existing work on ensuring software quality][ensuring-software-quality] and [ISO standards for software and data quality](https://iso25000.com/index.php/en/).

[fair-rs-nature]: https://www.nature.com/articles/s41597-022-01710-x
[fair_rs]: ./fair_rs
[ensuring-software-quality]: https://doi.org/10.5281/zenodo.10723608
[using_version_control]: ./using_version_control
[testing_software]: ./testing_software
[robust_software_design]: https://www.nilebits.com/blog/2024/08/software-design-principles-building-applications/
[quality-dimensions]: https://w3id.org/everse/i/dimensions/
[indicators]: https://everse.software/indicators/website/indicators.html#
[rs_quality_dimensions]: ./rs_quality_dimensions
[techradar]: https://everse.software/TechRadar/
