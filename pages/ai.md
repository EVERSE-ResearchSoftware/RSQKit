---
title: AI Guidance and Practice
description: Tasks and practices using AI to improve the quality of research software
contributors: [ "Michael Sparks", "Ahmad Alam", "Shoaib Sufi", "Aleksandra Nenadic" ]
keywords: [ "ai" ]
---

![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

## How do you use AI to develop quality research software?

This section of RSQKit is focussed on guidance and practices using AI to
creating high quality research software.  When considering where to start -
always **start from the work, not the tool or practice.**

Most pages include multiple different approaches for improving quality.  If
you do not have the time to apply all of them, **practicality beats purity** -
focus on the key aspects:

* Research correctness of output
* Guardrails
* Ability to rollback
* Reproducibility


**Guidance**

Guidance pages focus on overview, high level, and cross cutting concerns.

**Practices**

Practice pages focus on specific guidance for a given style of usage, ordered by intensity level.
Each practice has guidance on the following topics

* **Overview** - what is the practice, when is it useful?
* **Getting Started** - how to get started
* **Sample/Example Appropriate Practice** - example scenarios
* **Concerns/Risks** - What risks are related to this practice?
* **Quality Practice** - What quality practices can you apply to this practice to help/assist with research software quality at this level
* **AI Intensity Considerations** - Why might you consider using more or less
  AI?

### Spectrum of Intensity of AI Usage

The organising principle used in this section is a [Spectrum of Intensity of AI Usage][spectrum_of_intensity_of_ai_usage] .
The purpose of the spectrum is to assist in deciding what level of intensity is suitable for your work.

This correlates with how much context, authority,and autonomy a tool has.
It is not a maturity scale.
Higher intensity does not mean better practice.
It does not mean higher skill.
It does not mean better quality.

It is also worth remembering that a key part of any evaluation infrastructure
for AI-assisted practice is your manual practice. AI doesn't
replace your skills - it requires your skills more than ever.


Intensity correlates with a number of other issues including:

* Level of AI use/autonomy in the workflow
* Complexity of the AI setup
* Cost, Environmental impacts
* Severity of consequences (blast radius) of failure
* Volume, complexity and novelty of output

**Questions to consider of your project and of yourself:**

* Where does your project sit? Where should it sit?
* Where do you sit? Where do you **want** to be? Where **should** you be?


{% assign task_pages = site.pages
  | where: "type", "tasks_ai"
%}

{% assign introductory_pages = task_pages
  | where_exp: "item", "item.order < 999"
  | sort: "order"
%}

{% assign practice_pages = task_pages
  | where_exp: "item", "item.order >= 1000"
  | sort: "order"
%}

{% assign introductory_ids = introductory_pages
  | map: "page_id"
  | join: ", "
%}

{% assign practice_ids = practice_pages
  | map: "page_id"
  | join: ", "
%}


## Guidance

Guidance pages focus on overview, high level, and cross cutting concerns.

{% include section-navigation-tiles.html
  custom=introductory_ids
  sort=false
  search=false
  col=3
%}


## Practices

Practice pages focus on specific guidance for a given style of usage,
ordered by intensity level.

{% include section-navigation-tiles.html
  custom=practice_ids
  sort=false
  search=false
  col=3
%}
