---
title: Quality of Research Software
---

## What do we Mean by Research Software Quality?

**Quality of research software** refers to how well the software supports reliable, efficient, maintainable, and trustworthy research.
A key aspect of this quality is **reproducibility** — the ability for someone else (or your future self) to run the software and obtain the same results using the same inputs and environment.

When focusing on reproducibility, high-quality research software typically includes several aspects - for example:

- **Consistent and deterministic behavior** - the software produces the same results given the same inputs, every time.
- **Version control** and **documentation** - enabling people to track the exact version of the software used for a given result, along with dependencies, parameters, and instructions for use.
- **Automated testing** - ensuring that the code produces correct results for each test case and that changes to code 
do not break previous behavior or introduce unexpected bugs and that tests are run on each and every code change in a automated fashion.
- **Environment management** - using tools like containers or environment files (e.g., `requirements.txt`, `environment.yml`) allow others (and ourselves) to replicate the computational environment.
- **Clear** and **accessible** code - making sure the code is **readable**, well-structured, and includes **documentation** that explains how to use and understand it.

In short, **quality software** enables researchers to trust, share, and build upon computational work — an essential part of making science transparent and verifiable.
However, reproducible computational research often requires that researchers implement new practices and learn new tools to be able to produce **quality software**.

RSQKit is designed to offer [guidance](tasks) and introduce [tools](all_tools_and_resources) that have proven to be valuable across different [research communities](research_clusters_and_infrastructures) when developing software that supports scientific work in a reproducible and reliable way.
A key aspect of the project is the formal definition of [software quality dimensions](rs_quality) and the identification of various [indicators](rs_quality) that help assess and improve these aspects.

### FAIR Research Software

[FAIR software][fair-rs-nature] — i.e. software that is Findable, Accessible, Interoperable, and Reusable — sits squarely within the broader umbrella of **quality research software**.
Quality software is defined by multiple dimensions - e.g. correctness, performance, maintainability, usability, robustness, and reproducibility, among others.
Reproducibility often hinges on the FAIR principles: if your code and metadata are not findable or accessible, no one can rerun it; if it is not interoperable or reusable, others cannot adapt or extend or use it to verify your results.

FAIR is not a completely separate concern — it is a crucial subset of quality, primarily ensuring that your software can actually be discovered, understood, and exercised by others (or by you, months down the line).
A truly high-quality, reproducible research software package will typically satisfy both classical software-engineering criteria (tests, style, documentation, performance) and the FAIR principles.

So, FAIR - the “openness & reusability” slice of software quality - is essential for reproducibility, but most impactful when combined with all the other [quality practices](rs_quality) like [testing][testing_software], [version control][using_version_control], and [robust software design][robust_software_design].

## Formal Quality Dimensions & Indicators

The project is working on formally defining a number of research software quality [dimensions](https://w3id.org/everse/i/dimensions/) and their associated [indicators](https://w3id.org/everse/i/indicators) (which are to be used to assess the quality of software), based on [existing work on ensuring software quality][ensuring-software-quality] and [ISO standards for software and data quality](https://iso25000.com/index.php/en/).

[fair-rs-nature]: https://www.nature.com/articles/s41597-022-01710-x
[fair_rs]: ./fair_rs
[ensuring-software-quality]: https://doi.org/10.5281/zenodo.10723608
[using_version_control]: ./using_version_control
[testing_software]: ./testing_software
[robust_software_design]: https://www.nilebits.com/blog/2024/08/software-design-principles-building-applications/