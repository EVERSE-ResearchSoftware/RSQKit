---
title: Research Software Quality Dimensions
---

We distinguish between abstract quality dimensions (high-level categories like reliability or maintainability defined by standards such as [ISO/IEC 25010][iso-25010] and concrete quality indicators (measurable proxies like test coverage or community engagement). 
While indicators provide empirical evidence, they cannot fully capture the subjective, context-dependent nature and dimensions of "good" software.

Assessing research software for quality requires balancing "fit for purpose" (the ability of a tool to solve a specific scientific problem) against long-term goals of reusability and sustainability as championed by the FAIR4RS principles.
This assessment is further complicated by the non-linear relationship between technical quality and scientific impact, as well as the potential for software to be repurposed for unintended uses, which may shift the relevant quality criteria entirely.
 
We build upon the nine top-level [ISO software quality dimensions][ISO-IEC-25010] to bridge the gap between the nature or research software quality (e.g. community around research software) and engineering standards.

## Quality Dimension Definitions

EVERSE project is working to formally define a number of [research software quality dimensions](https://w3id.org/everse/i/dimensions) along with a [formal schema](https://w3id.org/everse/rsqd) to be used in machine readable metadata embedded in various resources.

Each of the quality dimensions will be an umbrella for a number of [quality indicators](https://w3id.org/everse/i/indicators), representing a specific software quality aspect that can be measured.

Current research software quality dimensions are described below.
This is still work in progress - we expect indicators in particular to be updated in the near future.

{% include dimensions.html %}

[iso-25010]: https://iso25000.com/en/iso-25000-standards/iso-25010
