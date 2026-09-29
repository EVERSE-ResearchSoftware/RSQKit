---
title: "Creating and enforcing a code of conduct"
description: "How to draft a code of conduct for a research software project and run a credible process for enforcing it, including reporting channels and proportionate responses."
contributors: ["Jason Maassen"]
page_id: code_of_conduct
related_pages:
  tasks: [documenting_software_project, creating_good_readme]
quality_indicators: []
keywords: ["code of conduct", "community guidelines", "governance", "harassment policy", "contributor covenant", "reporting process"]
---

## How do you create a Code of Conduct for your research software project?

This page covers how to draft a Code of Conduct and how to enforce it once adopted.

### Description

A Code of Conduct sets expectations for how people in a project should treat one another, and what happens when they don't.
For research software, contributors may include RSEs, PhD students, faculty, and external collaborators with very different levels of seniority and exposure to open-source norms.
Without a clear, written standard, conflicts get resolved inconsistently, and new contributors have no way to know what behavior is acceptable before they encounter a problem.
A Code of Conduct protects contributors and maintainers: it provides a concrete set of rules to point to instead of relying on ad hoc judgment calls under pressure.

### Considerations

- Establish the Code of Conduct as early as possible, ideally when the project is created, rather than retrofitting it after a conflict has already occurred.
- Adopting a well-established, widely used template gives the community an instantly recognizable signal and saves from drafting standards from scratch.
- Customize the reporting contact, the scope, and any project-specific norms — a template alone does not constitute an enforcement plan.
- Research software projects often involve significant power imbalances (a PI versus a graduate student, a maintainer versus a first-time external contributor), so the enforcement process needs to work even when the reported person outranks the reporter.
- The scope of a Code of Conduct is easy to underspecify: people usually think first of issues, pull requests, and discussions, but a research software community also interacts at conferences, in chat tools, and at lab meetings, so decide explicitly whether those spaces are covered too.
- If the project sits within a university or institute, consider having the draft reviewed by a relevant stakeholder, such as a research integrity office or legal advisor, before publishing it.
- A Code of Conduct that exists but is never enforced is worse than no Code of Conduct at all — it signals that the stated values aren't actually taken seriously.

### Solutions

- Start from a widely used template rather than writing one from scratch; the {% tool "contributor-covenant" %} is the most commonly adopted code of conduct in open source and includes a builder tool to customize the reporting section.
- Place the document as `CODE_OF_CONDUCT.md` in the repository root, and link to it from the README and contributing guide so it is visible before anyone needs it; if the code is hosted on GitHub, it can also be added through the repository interface, which offers Contributor Covenant and Citizen Code of Conduct templates with a guided form.
- If your group maintains several repositories under one organization, add the file to a `.github` repository instead of duplicating it everywhere; GitHub will use it as the default for any repository that doesn't define its own.
- Keep the standards concrete: list specific examples of both welcome and unwelcome behavior rather than only abstract principles, so contributors can self-assess against real examples.
- State the scope explicitly — whether the Code of Conduct applies only to project spaces (issues, pull requests, mailing lists) or also to related spaces such as conferences, chat tools, or social media where someone represents the project.
- Beyond the repository file, surface the document where people are likely to read it before a conflict arises, such as project documentation, a pinned message in a chat tool, or a footer link on the project website.
- If you are unsure where to start, review codes of conduct from comparable research software projects to see how they scoped reporting and enforcement, then adapt rather than copy.

## How do you enforce a Code of Conduct for your research software project?

### Description

Adopting a Code of Conduct is only half the task — a credible process for what happens when it is violated is also needed. 
Without a defined enforcement process, reports go unanswered, maintainers improvise under stress, and contributors lose trust that raising an issue will lead anywhere.
This matters even more in research settings, where reporters may fear professional retaliation from a supervisor or collaborator they depend on for funding or authorship.
A working enforcement process needs a clear reporting channel, a defined set of people who handle reports, and a documented range of possible responses.

### Considerations

- Decide who receives reports before you need the process, and make sure there is an alternative contact for reports about the usual recipients themselves.
- If members of the enforcement team are involved in a report, they should refrain from handling the case and an alternative reviewer or contact should be identified.
- Reports may involve sensitive personal information; treat them as confidential by default and be explicit about who will see a report.
- A documented range of responses — from a private conversation to temporary suspension or permanent exclusion from the project — allows for a proportional response instead of either ignoring an issue or escalating immediately to the most severe option.
- Not every disagreement or uncomfortable interaction is a Code of Conduct violation; sometimes the right response is to clarify expectations with the person involved rather than treat it as a formal violation.
- Treat every report as worth investigating even if it doesn't match your own experience of the person involved, and gather more than one perspective before deciding what happened.
- Retaliation against someone who reports a concern or participates in an investigation should itself be treated as a serious violation of the Code of Conduct.
- Revisit the Code of Conduct periodically, since your community's needs and the available template versions both evolve over time.

### Solutions

- Provide a private reporting channel, typically an email address read by a small, named group of maintainers, and state in the document who that group is.
- Document a tiered response process: acknowledge the report, investigate by gathering information and multiple perspectives on what happened, decide on a response, and communicate the outcome to the reporter.
- Set expectations for response times, such as acknowledging receipt of a report within a few days, so reporters understand what will happen next and are not left wondering whether their report was received.
- Match the response to the severity of the violation: a first, less severe incident might warrant a private conversation explaining the impact of the behavior, while a public or repeated violation may call for a public warning, and serious or repeated misconduct may justify suspension or permanent removal.
- Write down, in advance, the range of possible consequences so decisions during an actual incident are guided by a plan rather than made under pressure.
- For projects with significant power imbalances, consider routing reports about senior project members to an external or institutional contact, such as an ombudsperson, rather than only to fellow maintainers.
- Look at enforcement guides from larger, established projects for a sense of how much process detail you may need; the [Contributor Covenant 3.0](https://www.contributor-covenant.org/version/3/0/code_of_conduct/) update reframes enforcement around addressing and repairing harm, which is a useful model for proportionate, restorative responses.

## Further Reading

- **[Contributor Covenant](https://www.contributor-covenant.org/)** — The most widely adopted code of conduct template in open source, with an interactive builder for customizing the reporting section to your project; useful as a drop-in starting document rather than writing one from scratch.
- **[Your Code of Conduct — Open Source Guide](https://opensource.guide/code-of-conduct/)** — GitHub's practical guide to adopting and enforcing a code of conduct, including concrete examples of how real projects structured their reporting contacts and enforcement notes; a good starting point for the operational side of this task.
- **[How to Create a Code of Conduct for an Open-Source Project — Open {re}Source](https://openresource.dev/articles/how-to-create-a-code-of-conduct-for-an-open-source-project/)** — A step-by-step walkthrough from goal-setting through publication, review cadence, and enforcement, with practical detail on hosting platform features such as GitHub's default community health files; useful for the full lifecycle of the document, not just the initial draft.
- **[Contributor Covenant 3.0 announcement](https://ethicalsource.dev/blog/contributor-covenant-3/)** — Explains the rationale behind the latest major revision, including its shift toward restorative, proportionate enforcement; useful background for understanding why enforcement processes look the way they do in current templates.
- **[Code of Conduct — Google Open Source](https://opensource.google/documentation/reference/releasing/template/CODE_OF_CONDUCT)** — A real-world example of a Contributor Covenant adaptation in production use at scale, useful as a reference for how a large organization phrased scope and maintainer responsibilities.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
