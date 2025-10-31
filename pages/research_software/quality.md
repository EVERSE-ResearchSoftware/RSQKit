---
title: Quality of Research Software
---

## What Questions Should I Ask About My Research Software?

When we talk about research software quality, we are really asking: can I trust my software and the results it produces?

**Quality** here means the software supports reliable, efficient, maintainable, and trustworthy research. 
One of the biggest indicators of that quality is **reproducibility** — can someone else (or my future self) run this software again and get the same results with the same data and environment?

To think about reproducibility and quality in practice, we might ask ourselves:

- Does my software behave consistently?
If I run it today and tomorrow with the same inputs, do I get the same results every time?

- How do I know my code is giving the right results?
Am I testing my code and results for correctness? Am I checking for edge cases of my input values? And checking correctness of results whenever the code changes?

- Would another researcher be able to read and understand my code?
Is it clearly written, structured, and documented so others can learn from or build on it?
 
- Can others (or I) see exactly what version was used to produce a given result?
Do I keep track of dependencies, parameters, and instructions for use?

- Can someone else easily recreate my computational environment, run my code and get the same results?
Am I recording and sharing what is needed to run the code?

Asking these kinds of questions helps ensure that the software we write can be trusted, shared, and built upon — which in turn makes my research more transparent and verifiable.
Developing reproducible and high-quality computational research often means adopting new tools and habits — but it is an investment that pays off in credibility and collaboration.

RSQKit is here to help with that: it provides [guidance](./tasks), examples, and [tools](all_tools_and_resources) used successfully across research communities to develop software that is reproducible and reliable. 

### Aspects of Research Software Quality

When focusing on reproducibility, high-quality research software typically includes several aspects (as mentioned above) - for example:

- **Consistent and deterministic behavior** - the software produces the same results given the same inputs, every time.
- **Version control** and **documentation** - enabling people to track the exact version of the software used for a given result, along with dependencies, parameters, and instructions for use.
- **Automated testing** - ensuring that the code produces correct results for each test case and that changes to code 
do not break previous behavior or introduce unexpected bugs and that tests are run on each and every code change in a automated fashion.
- **Environment management** - using tools like containers or environment files (e.g., `requirements.txt`, `environment.yml`) allow others (and ourselves) to replicate the computational environment.
- **Clear** and **accessible** code - making sure the code is **readable**, well-structured, and includes **documentation** that explains how to use and understand it.

These aspects are more [formally defined][rs_quality] as [dimensions of software quality][quality-dimensions] and related [indicators][indicators] for each dimension that can help assess and improve quality aspects.

### FAIR Research Software

[FAIR software][fair-rs-nature] — i.e. software that is Findable, Accessible, Interoperable, and Reusable — sits squarely within the broader umbrella of **quality research software**.
Quality software is defined by multiple dimensions - as we have seen above - including correctness, usability, robustness, maintainability, performance and reproducibility, among others.

Reproducibility often hinges on the FAIR principles: if your code and documentation and auxiliary information about your code (called software metadata) are not findable or accessible, no one can rerun it; if it is not interoperable or reusable, others cannot adapt or extend or use it to verify your results.

FAIR is not a completely separate concern — it is a crucial subset of quality, primarily ensuring that your software can actually be discovered, understood, and exercised by others (or by you, months down the line).
A truly high-quality, reproducible research software package will typically satisfy both classical software-engineering criteria (tests, style, documentation, performance) and the FAIR principles.

So, [FAIR software][fair_rs] - the “openness & reusability” slice of software quality - is essential for reproducibility, but most impactful when combined with all the other [quality practices](rs_quality) like [testing][testing_software], [version control][using_version_control], and [robust software design][robust_software_design].

## Formal Quality Dimensions & Indicators

The EVERSE project (the home of RSQKit) is working on formally defining a number of research software quality [dimensions][quality-dimensions] and their associated [indicators](https://w3id.org/everse/i/indicators) (which are to be used to assess the quality of software), based on [existing work on ensuring software quality][ensuring-software-quality] and [ISO standards for software and data quality](https://iso25000.com/index.php/en/).

[fair-rs-nature]: https://www.nature.com/articles/s41597-022-01710-x
[fair_rs]: ./fair_rs
[ensuring-software-quality]: https://doi.org/10.5281/zenodo.10723608
[using_version_control]: ./using_version_control
[testing_software]: ./testing_software
[robust_software_design]: https://www.nilebits.com/blog/2024/08/software-design-principles-building-applications/
[quality-dimensions]: https://w3id.org/everse/i/dimensions/
[indicators]: https://everse.software/indicators/website/indicators.html#
[rs_quality]: ./rs_quality