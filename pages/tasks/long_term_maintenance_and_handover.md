---
title: Long-term maintenance and handover
description: How to manage and plan for the long-term maintenance of research software and project before funding ends, and how to hand it over responsibly to a successor or into archival.
contributors: ["Kenneth Rioja"]
page_id: long_term_maintenance_and_handover
related_pages:
  tasks: [maintaining_research_software, archiving_software, software_management_planning, documenting_software_project, writing_research_software_story]
quality_indicators: [archived_in_scholarly_repository, archived_in_software_heritage, has_contribution_guidelines]
keywords: ["maintenance", "handover", "sustainability", "succession planning", "solo maintainer", "archiving", "organising software project"]
---

## Funding ends soon: How do you manage for the long-term maintenance of your research software?

### Description

Research software is usually built within a fixed-term grant, but the questions it answers and the users who depend on it often outlive the funding.
Without an explicit maintenance plan, software quietly stops working as dependencies age, operating systems change, and the people who understood it move on.
Planning for maintenance while you are still funded is far cheaper than trying to revive an abandoned project later.
This task is about project management, and more particularly deciding, early and deliberately, what level of upkeep your software needs and who will provide it.
In many research groups you may be the sole developer, maintainer, and infrastructure administrator for the lab's software, which makes this planning a personal responsibility as much as a technical one.

### Considerations

- Not all research software needs the same level of maintenance – a one-off analysis code has different needs from a research software infrastructure used by an active research community, so match your plan to the software's actual role and audience (see [the Three-Tier Model of Research Software](/three_tier_view)).
- As a solo maintainer, your departure creates an immediate risk for the codebase, which makes early, explicit conversations with your PI or lab leadership about boundaries and succession a necessity rather than an afterthought.
- A maintenance plan needs an owner, even if that owner is "no one after this date" – explicitly stating that the software will become unmaintained is more honest and more useful to users than silence.
- Funders and institutions increasingly expect a sustainability or software management plan as part of the proposal, so building maintenance thinking in from the start avoids scrambling at the end; see [Software Management Planning](/software_management_planning) for the fuller process.
- If you have multiple dependencies: Maintenance burden grows with every dependency, supported platform, and external integration; reducing scope before the end of funding reduces what someone else has to keep alive – see [Maintaining research software](/maintaining_research_software) for ongoing dependency-management practices.

### Solutions

**Conceptual guidance:**

- Decide, as early as possible, what "maintained" means for your project: security patches only, active feature development, or somewhere in between.
- Distinguish between technical maintenance (keeping the software running and dependencies current) and community maintenance (responding to issues, reviewing contributions, answering questions).
- If you are a solo maintainer, schedule an explicit sustainability conversation with your PI well before your contract ends to decide whether the project will be institutionalised, handed off, or archived.
- Maintenance in a research setting often extends beyond the codebase itself – keeping data pipelines running and documentation aligned with current institutional data-management requirements is part of the same job.

**Actionable steps:**

- Write a short sustainability statement in your repository so users know what to expect and do not rely unknowingly on code that is about to become unsupported. You can adapt a template like the one below directly into your README:

```markdown
## Project Sustainability and Maintenance Status

### Current Status
This software is actively maintained as part of [Project/Lab Name], funded by [Funder Name/Grant Number].

### Maintenance Timeline
- **Active Maintenance Phase:** core development and issue triaging are guaranteed until [End Date].
- **Extended Support Phase:** from [Start Date] to [End Date], the project receives security and compatibility patches only.
- **Archival Phase:** after [Final Date], the repository is placed in a read-only archived state.

### Contact and Handover
For questions or to discuss taking over maintenance, contact [PI Email Address].
```

- If a successor team, community, or institution is willing to take on maintenance, agree this explicitly and in writing before funding ends, rather than assuming it will happen informally.
- Set up automated checks (continuous integration, dependency update bots) so that basic problems surface without a human having to go looking for them – see our task page about [Continuous Integration and Continuous Delivery/Deployment ](/ci_cd).
- Archive a citable, versioned snapshot of the software in a long-term repository such as {% tool "zenodo" %} or {% tool "software-heritage" %}, so the software remains accessible and citable even if active development stops entirely – see [Archiving software](/archiving_software) for the full process.
- If you have multiple dependencies: Reduce your dependency footprint before funding ends, since every dependency removed is technical debt someone else won't inherit:
  - audit and prune unused packages,
  - replace heavy external libraries with lighter alternatives where practical,
  - pin exact versions in your environment configuration,
  - vendor small, critical helper scripts to remove fragile external dependencies.

## Your contract ends soon: How do you hand over your research software?

### Description

Even with a maintenance plan in place, someone eventually has to actually do the work of stepping back, and someone else may need to step in.
A poorly executed handover loses tacit knowledge that was never written down: why a design decision was made, which parts of the code are fragile, and how to actually run the test suite.
This task is about the practical process of transferring responsibility for the software, whether to a new developer, a research group, or simply to its future, less-supported self.

### Considerations

- Academic contracts rarely allow for a clean overlap period with a successor, given funding gaps and hiring delays, so plan for an asynchronous handover – one that relies on self-contained documentation rather than assuming live training sessions will happen.
- Institutional knowledge about *why* the software is built the way it is tends to disappear fastest – code comments and commit history rarely capture design rationale on their own. To know more about it see [Research Software Stories](/writing_research_software_stories).
- The right handover process scales with project size: a single-developer script needs far less than a multi-contributor tool with external users, so do not over-engineer the handover for a small project or under-prepare it for a large one.
- Access and infrastructure (repository ownership, CI credentials, package registry accounts, domain names) are easy to forget during a handover and can quietly break the project later if they remain tied to one person.
- A clear, permissive software license set early avoids legal ambiguity that can block a handover or reuse later (see [Licensing Software](/licensing_software))

### Solutions

**Conceptual guidance:**

- Treat handover as a project in itself, with its own checklist and timeline, not as an afterthought tacked onto the end of a grant.
- Separate what must be handed over (working code, build/test instructions, access credentials) from what should be handed over if possible (design rationale, roadmap, known issues).

**Actionable steps:**

- Work through a handover checklist at least four weeks before your involvement ends:
  1. create a single document or repository issue that lists the location and status of all critical project infrastructure,
  2. document the build, deployment, and data pipeline steps clearly enough for a non-expert colleague to reproduce a working build from scratch. For data pipeline, see [Data Management Plan (DMP) explained in the RDMKit](https://rdmkit.elixir-europe.org/data_management_plan),
  3. confirm the automated test suite passes and record the exact command to run it in a clean environment,
  4. transfer administrative ownership of repositories, CI pipelines, package registries, and domain names to a shared institutional or lab account,
  5. hold a final debrief with your PI or lab head to confirm they hold working administrative access before your personal credentials expire.
- Record the project's design decisions and known limitations, even retrospectively – future maintainers benefit far more from "why" than from code alone. To write such a document, please follow the guided task [Writing Research Software Stories](/writing_research_software_stories#further-guidance-and-examples).
- Write or update a CONTRIBUTING or MAINTAINERS document – see [Documenting software project](/documenting_software_project) for the standard file set this fits into.
- If no successor is available, say so explicitly in the README and consider archiving the repository in read-only mode rather than leaving it in an ambiguous, silently abandoned state (See more in [Archiving software](/archiving_software)).
- For larger or community-facing projects, follow a structured handover guideline such as the one referenced below, which provides checklists scaled to project size.

## Further Reading

- **[Sustainable Research Software Hand-Over](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.307)** – A practical, checklist-driven guide to handing over research software, written from a developer's perspective and scaled separately for small (single-developer) and large (multi-contributor) projects. Most useful for anyone planning an actual handover rather than just a maintenance policy.
- **[Approaches to software sustainability](https://www.software.ac.uk/guide/approaches-software-sustainability)** – A Software Sustainability Institute guide that lays out the different strategies for sustaining research software depending on its maturity, importance, and available resources. A good starting point for deciding what level of sustainability effort your project actually needs.
- **[Software Heritage](https://www.softwareheritage.org/)** – A long-term archive for source code that preserves snapshots of software independent of any single hosting platform or maintainer. Worth understanding before deciding where to archive a project at end-of-life.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6 and Gemini 2.5 Pro during the [Research Software Quality Toolkit (RSQKit) Contentathon on June 30, 2026](https://indico.cern.ch/event/1688339/), under the strict editorial control and factual verification of the human author.
