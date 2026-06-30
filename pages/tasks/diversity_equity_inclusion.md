---
title: "Fostering diversity, equity, and inclusion in reserach software projects"
description: "Practical guidance for research software projects on diversity, equity, and inclusion (DEI), covering inclusive contribution processes, accessible documentation and onboarding, support for underrepresented contributors, governance, and event accessibility, with attention to the academic power dynamics specific to research software."
contributors: ["Gavin J. Pringle"]
page_id: diversity_equity_inclusion
related_pages:
  tasks: [documenting_software_project, software_management_planning, credit_recognition_research_software]
quality_indicators: [has_contribution_guidelines, has_active_contributors, has_active_communication_channels, response_timeframe_ok]
keywords: ["diversity", "equity", "inclusion", "dei", "accessibility", "code of conduct", "underrepresented groups", "open source governance"]
---

## How do you foster diversity, equity, and inclusion in your research software project?

This page covers why diversity, equity, and inclusion (DEI) matter specifically for research software, and gives practical guidance across contribution processes, documentation, community building, governance, and events.
Diversity refers to the range of backgrounds, identities, and perspectives represented in your project; equity refers to fair access to opportunities and resources, accounting for the fact that people start from different positions; inclusion refers to whether people who are present can actually participate fully and feel they belong.
A project can be demographically diverse while still being inequitable — for example, if only contributors with institutional funding can attend in-person events — so the three need to be considered together rather than treating diversity alone as the goal.

Research software is usually built inside academic structures — labs, grants, supervisory relationships — that carry their own power imbalances on top of the usual open source ones.
A student contributing to their advisor's codebase, a postdoc dependent on a PI for authorship and references, or a research software engineer with no formal authority over the scientists who use their tool: these dynamics shape who can safely raise concerns, propose changes, or simply show up, in ways that general open source community-building advice doesn't fully capture.
Treating DEI as an ongoing practice rather than a one-off policy is what makes the difference for research software projects in particular, because the underlying academic hierarchy doesn't go away on its own.

## How do you design inclusive contribution processes?

### Description
Contribution processes determine who can realistically participate, not just who is formally welcome.
In academic settings, the visible "core team" is often a PI's students or postdocs, and unwritten norms about how decisions get made can be invisible to anyone outside that group.
Designing the process deliberately, rather than letting it default to "however the original author did it," is what opens the project to people without that insider context.

### Considerations
- Contribution norms that work for a single lab (informal chat in the office, decisions made verbally) typically exclude collaborators at other institutions, in other time zones, or without the same access to the original team.
- A formal review process protects contributors with less power in the academic hierarchy — for example, a student proposing a change to a senior researcher's code — by giving them a defined channel that doesn't depend on personal standing.
- Asynchronous, written processes (issues, pull requests, documented decisions) are more accessible than processes that depend on attending a particular meeting or being in a particular room.
- Response time matters: a contribution that sits unreviewed for months signals, intentionally or not, that outside contributions aren't really wanted.
- If AI tools are used to draft or review contributions, apply the same review standards and the same courtesy in feedback as you would for a human contributor; generated code carries no special exemption from review, and generated review comments should still be checked for tone before posting.

### Solutions
- Document your contribution process in a `CONTRIBUTING.md` file that covers how to propose a change, who reviews it, and how long that typically takes.
- Use pull requests and issue templates rather than informal channels (email, in-person requests) as the default route for proposing changes, so the same path is available to everyone regardless of their relationship to the team.
- Define and document review criteria in advance, so contributors know what is expected and reviewers aren't applying inconsistent or implicit standards.
- Separate the role of "reviews code" from "controls authorship or funding decisions" where possible, so that technical feedback doesn't carry an implicit threat to someone's academic standing.
- Acknowledge contributions explicitly — in release notes, a contributors file, or citation metadata — since in academic contexts, visible credit can matter for a contributor's career in a way it may not in purely industry open source projects.

## How do you make your documentation and onboarding accessible?

### Description
Documentation and onboarding are usually a new contributor's first real interaction with a project, and they set expectations for whether the project is worth the effort to join.
Research software documentation often assumes background that the original authors took for granted — a particular numerical method, a specific subfield's terminology, or familiarity with a lab's internal tools — which quietly filters out people from adjacent fields or earlier career stages.
Treating documentation as an accessibility surface, not just a reference, broadens who can actually start contributing.

### Considerations
- Documentation written for "someone like the original author" tends to assume shared disciplinary background, native-English fluency, and familiarity with specific tools, none of which are safe assumptions for a broader contributor base.
- A working "quick start" that gets a new contributor to a successful first run is more valuable for onboarding than exhaustive reference material that nobody reads end to end.
- Accessibility in the technical sense (screen-reader-compatible formats, sufficient color contrast in diagrams, captioned video walkthroughs) is frequently overlooked in research software documentation, which skews toward static text and equations.
- A glossary or links to background concepts costs little to add and substantially lowers the barrier for contributors from outside the immediate subfield.
- If documentation is partly AI-generated, check it for unstated assumptions and jargon in the same pass as for tone, since generated text tends to default to the register of its training data rather than to your specific audience.

### Solutions
- Write a "quick start" guide that takes a newcomer from zero to a working example in a small number of steps, separate from the full reference documentation.
- Define unavoidable jargon and domain-specific terms the first time they appear, or link to a short glossary.
- Check that diagrams and figures have text alternatives, and that any video content has captions or a written summary alongside it.
- Test your onboarding documentation with someone outside the immediate team — ideally someone from a different subfield or career stage — and treat their points of confusion as documentation bugs.
- Provide setup instructions that don't assume access to your specific institutional infrastructure (a particular cluster, license, or internal tool); where that access genuinely is required, say so explicitly rather than letting newcomers discover it by failing silently.

## How do you welcome and support contributors from underrepresented groups?

### Description
Welcoming underrepresented contributors is not the same as having a public statement that the project welcomes them; it requires concrete practices that reduce the specific friction those contributors are more likely to encounter.
In research software, this includes researchers from underrepresented disciplines or institutions (not only demographic groups), since the field's prestige hierarchy shapes whose contributions get taken seriously.
Sustained support, not a one-time outreach effort, is what determines whether contributors stay involved after their first contribution.

### Considerations
- A single onboarding event or call for contributors can attract first-time contributors, but without ongoing mentorship and a low-friction path to a second contribution, many won't return.
- Tokenism — inviting underrepresented contributors into highly visible but low-influence roles — is a recognized failure mode and tends to be noticed by the people it's meant to include.
- Contributors from under-resourced institutions may have less reliable internet access, older hardware, or less institutional support for open source work; assuming otherwise in scheduling or tooling choices excludes them by default.
- Mentorship relationships work best when expectations and time commitment are explicit on both sides, rather than left as an informal, unstructured arrangement.
- Measuring participation (who contributes, who is retained, who advances into maintainer roles) gives you evidence of whether your practices are working, rather than relying on impressions.
- Demographic data (sex, gender, sexual orientation, disability status, race or ethnicity) is the most direct way to measure whether underrepresented groups are actually attending or contributing, but it is sensitive personal data: in the EU it falls under GDPR's special category rules, so collection must be optional, clearly explained, and stored separately from anything that could identify an individual.

### Solutions
- Set up a lightweight mentorship path for new contributors — even informally pairing a newcomer with an existing contributor for their first few contributions — and make clear how someone can request it.
- Participate in or model your onboarding on established programs aimed at broadening participation, such as Google Summer of Code or Outreachy, which have tested structures for first-time contributor support.
- Track basic participation metrics over time (number of distinct contributors, retention after a first contribution, representation in maintainer roles) to check whether your practices are having the intended effect.
- Avoid placing a single underrepresented contributor in a highly visible "diversity" role without real decision-making authority; if you create such roles, give them genuine scope and support.
- Be explicit in calls for contributors about flexible time commitments and asynchronous participation, since assuming everyone can attend synchronous meetings in a specific time zone excludes contributors elsewhere.
- If you run events, talks, or webinars, add an optional demographic question at registration — a dropdown such as male, female, intersex, prefer to self-identify, and prefer not to say works well for sex, and a similar approach can be adapted for sexual orientation, disability, or race — so you can see over time which sessions and topics attract underrepresented groups and which don't.
- Use that data to act, not only to report on it: promote specific sessions more heavily where attendance from a particular group is low, and deliberately invite presenters and chairs from underrepresented groups, since visible representation in those roles signals the project is genuinely open, not only welcoming as an audience.
- A "prefer to self-identify" free-text option alongside fixed categories, plus a "prefer not to say" option, respects people who don't fit the listed categories without forcing disclosure.
- This kind of deliberate, targeted effort — promoting underrepresented categories more heavily, actively recruiting presenters and chairs from underrepresented groups — is sometimes called positive action; what is permissible varies by jurisdiction and funder policy, so check applicable rules before designing quotas or eligibility criteria around protected characteristics.

## How do you build DEI into your project's governance?

### Description
Governance — who makes decisions, how leadership roles are filled, how disputes are resolved — determines whether DEI commitments are durable or dependent on whichever individuals currently happen to care about them.
Academic research software projects frequently default to governance by whoever wrote the original grant or runs the lab, which concentrates power in a way that can be invisible until someone tries to challenge a decision.
Writing governance down, even briefly, is what makes DEI commitments survive a change in personnel.

### Considerations
- Informal governance ("the PI decides") is common in research software but makes it hard for anyone to challenge a decision without risking their relationship with someone who controls their funding, supervision, or career prospects.
- A documented governance structure doesn't need to be elaborate; even a short document naming who has decision authority over what, and how that can change, removes significant ambiguity.
- Succession planning matters more in academic projects than in typical open source ones, since maintainers often leave when a grant ends, a student graduates, or a postdoc moves on, and an undocumented project can effectively die with them.
- A documented code of conduct with a real enforcement process is a governance commitment, not just a community-facing document, and needs a designated person or process for handling reports.
- Power imbalances between a project's nominal leadership and its day-to-day maintainers (for example, a PI listed as lead but a research software engineer doing the actual maintenance) should be reflected honestly in how credit and decision-making authority are described.

### Solutions
- Write a short governance document stating who can make which kinds of decisions (technical direction, releases, adding maintainers) and how that can change over time.
- Adopt and publish a code of conduct with a named contact or process for reports, separate from the project's primary technical leadership where feasible, so reports aren't only routed through the person they might concern.
- Plan explicitly for maintainer turnover — document onboarding steps for new maintainers and identify a backup decision-maker, rather than assuming the current lead will always be available.
- Where a research group's internal hierarchy (PI, postdocs, students) maps onto project roles, document this openly rather than letting it operate as an unstated default, so external contributors understand how decisions actually get made.
- Review governance periodically as the project and team change, rather than treating an initial document as permanent.

## How do you make your project's events accessible?

### Description
Research software projects often run or participate in events — workshops, hackathons, conference sprints, community calls — and these are frequently where new contributors decide whether the project is worth their time.
An inaccessible event (in scheduling, venue, or format) silently excludes people before they ever get to the technical content.
Event accessibility spans physical access, scheduling, cost, and the social experience of attending, and all of these affect who actually shows up.
Running events in hybrid mode — combining in-person and online participation rather than choosing one or the other — is one of the highest-leverage single changes available, since it directly removes physical-access barriers rather than working around them.

### Considerations
- Scheduling a recurring event in a single time zone systematically excludes contributors elsewhere, even with no intent to do so.
- In-person events have real costs (travel, accommodation, registration) that are not equally absorbable across institutions, career stages, or countries, and that shape who can attend regardless of interest.
- Childcare, dietary needs, and physical accessibility (venue access, captioning, quiet spaces) are concrete, addressable factors, not abstract concerns, and are often easiest to address by asking attendees directly in advance rather than guessing.
- A code of conduct that applies in principle but isn't actively enforced at an event provides little real protection; someone needs to be visibly responsible for handling concerns during the event itself.
- Hybrid formats remove physical-travel barriers entirely for people with mobility impairments or limited travel budgets, and let neurodivergent attendees who find in-person events overstimulating choose a lower-intensity way to participate, but they introduce their own accessibility considerations, such as ensuring remote participants have genuine influence on outcomes rather than passive observer status.
- A broader, more diverse pool of attendees and contributors is widely cited as a driver of innovation in technical fields, since people with different backgrounds and experiences tend to surface different problems, use cases, and solutions; hybrid access is one practical lever for broadening that pool, though it is one factor among several rather than a guarantee of more innovative outcomes on its own.

### Solutions
- Rotate or stagger meeting and event times across time zones where there is a recurring schedule, rather than fixing it permanently to one region.
- Offer travel or registration grants where budget allows, and be transparent about the application process and criteria.
- Ask registrants in advance about accessibility, dietary, and childcare needs, and act on the responses rather than treating the question as a formality.
- Name a specific person or team responsible for code of conduct enforcement at the event, and make sure attendees know how to reach them during the event, not just in a document published beforehand.
- Default to hybrid for recurring meetings and community calls, not only flagship events, since the accessibility benefit applies to routine project activity, not just conferences.
- Design at least part of the agenda (for example, decision-making sessions, Q&A, and voting) so remote attendees have a real role rather than only watching a stream — a chat-monitored question queue and a remote-attendee speaking slot are minimal ways to do this.

## How do you find good DEI resources and frameworks for your project?

### Description
DEI in open source and research software is an active area with established communities producing practical, freely available guidance; you do not need to design your approach from first principles.
Using existing frameworks gives you a tested starting point and a shared vocabulary with other projects, rather than reinventing terminology and practices project by project.
The two resources below are specifically curated for open source and research-adjacent communities, which makes them a more direct fit than general DEI material aimed at other industries.

### Considerations
- DEI resource quality varies widely; prefer resources maintained by communities with direct open source or research software experience over generic corporate DEI material, since the specific barriers differ.
- A resource hub or checklist is most useful as a starting point for prioritization, not as a compliance list to complete in full — partial, well-implemented changes tend to outperform many superficial ones.
- Frameworks built for general open source communities (not specifically research software) are still valuable, but you should expect to adapt them for the academic power dynamics covered above.
- Revisit these resources periodically; DEI practice in open source continues to develop, and a resource hub that is actively maintained will reflect that better than a static document from several years ago.

### Solutions
- Browse the [All In for Maintainers DEI Resource Hub](https://allinopensource.org/maintainers/DEI-resources/), a curated, topic-organized collection of DEI resources for open source maintainers covering accessibility, community building, code of conduct, inclusive language, and governance; use its topic index to find material relevant to whichever sub-topic on this page you want to go deeper on.
- If your project runs events of any kind, work through the [NumFOCUS DISCOVER Cookbook](https://discover-cookbook.numfocus.org/intro.html), which is built specifically for organizers of scientific computing conferences and events and explicitly distinguishes high-impact, low-effort actions from larger commitments, so you can prioritize realistically.
- Treat both resources as living references to return to as your project grows, rather than a one-time read, since they are updated as practice in the field develops.

## Further Reading

- **[The All In for Maintainers DEI Resource Hub](https://allinopensource.org/maintainers/DEI-resources/)** — A curated, regularly updated archive of DEI resources for open source maintainers, organized by topic (accessibility, community building, code of conduct, governance, and more); useful as a first stop for going deeper on any sub-topic covered on this page.
- **[The NumFOCUS DISCOVER Cookbook](https://discover-cookbook.numfocus.org/intro.html)** — A practical guide built specifically for organizers of scientific computing conferences and events, with suggestions ranked by impact and effort; directly relevant to research software projects that run workshops, sprints, or community calls.
- **[The Turing Way: Diversity and Inclusion](https://book.the-turing-way.org/index.html)** — An open, collaboratively written handbook on reproducible and inclusive research practice, with chapters addressing equity and inclusion written specifically for research and research software contexts.
- **[GitHub's Open Source Guides: Building Welcoming Communities](https://opensource.guide/building-community/)** — Practical, example-driven guidance on growing a healthy contributor base; a useful general complement to the research-specific resources above.
- **[corsa-center/oss-documents](https://github.com/corsa-center/oss-documents)** — A community-maintained collection of governance, contributing, code of conduct, and DEI resources for open source projects, including the two resources above alongside related material on governance and contribution documents.
- **[GDPR Article 9: Processing of special categories of personal data](https://gdpr-info.eu/art-9-gdpr/)** — The official regulation text, with commentary, covering sex, racial or ethnic origin, sexual orientation, and other sensitive categories; the right starting point before adding any demographic question to an event registration form, since it sets out when such data can be collected and what conditions apply.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
