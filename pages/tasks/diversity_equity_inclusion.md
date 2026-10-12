---
title: "Fostering diversity, equity, and inclusion in research software projects"
description: "Practical guidance for research software projects on diversity, equity, and inclusion (DEI), covering inclusive contribution processes, accessible documentation and onboarding, support for underrepresented contributors, governance, and event accessibility, with attention to the academic power dynamics specific to research software."
contributors: ["Gavin Pringle"]
page_id: diversity_equity_inclusion
related_pages:
  tasks: [documenting_software_project, software_management_planning, credit_recognition_research_software]
quality_indicators: [has_contribution_guidelines, has_active_contributors, has_active_communication_channels, response_timeframe_ok]
keywords: ["diversity", "equity", "inclusion", "dei", "accessibility", "code of conduct", "underrepresented groups", "open source governance"]
---

## How do you foster diversity, equity, and inclusion in your research software project?

This page briefly outlines why diversity, equity, and inclusion (DEI) matter specifically for research software, and then gives practical guidance across contributions, documentation, governance and community activities.

- Diversity refers to the range of backgrounds, identities, and perspectives represented in your project;
- Equity refers to fair access to opportunities and resources, accounting for the fact that people start from different positions;
- Inclusion refers to whether people who are present can actually participate fully and feel they belong.

A project can be demographically diverse while still being inequitable, for example, only contributors with institutional funding can attend in-person events.  As such, the three need to be considered together rather than treating diversity alone as the goal.

Research software is usually built inside academic structures, such as labs, grants, supervisory relationships, etc., which introduce power dynamics beyond those typical of open source. Whether it is a student contributing to an advisor's codebase, a postdoc depending on a PI, or a research software engineer lacking authority over users, these hierarchies influence who can safely raise concerns or propose changes. Because these academic structures persist, treating diversity, equity, and inclusion as an ongoing practice rather than a static policy is essential for research software projects.

DEI is closely linked to software sustainability, quality, and innovation. Projects accessible to a broad range of contributors attract and retain maintainers while preventing knowledge concentration. Furthermore, varied backgrounds and life experiences bring diverse perspectives to light, helping to identify requirements, reveal unaddressed use cases, and inspire distinct solutions.

## How do you design inclusive contribution processes?

### Description
Contribution processes determine who can realistically participate, not just who is formally welcome.
In research software projects, informal ways of working and undocumented decisions create barriers for contributors outside the core team.
Designing the process deliberately, rather than letting it default to the original author's habits, opens the project to people without that insider context.

### Considerations
- Lab-specific contribution norms, such as informal office chats or verbal decisions, exclude collaborators at other institutions, in different time zones, or without direct access to the core team.
- A formal review process protects contributors lower in the academic hierarchy, such as a student proposing a change to a senior researcher's code, by providing a defined channel indepentebt of personal standing.
- Asynchronous, written processes (issues, pull requests, documented decisions) are more accessible than processes requiring attendance at a specific meeting or location.
- Response time matters: a contribution that sits unreviewed for months signals, intentionally or not, that outside input is unwelcome.
- If AI tools are used to draft or review contributions, apply the same review standards and courtesy in feedback as you would for a human contributor. Generated code still requires review, and AI review comments should be checked for tone before posting.

### Solutions
- Document your contribution process in a `CONTRIBUTING.md` file that covers how to propose a change, who reviews it, and how long that typically takes.
- Use pull requests and issue templates as the default route for proposing changes rather than informal channels, such as email or in-person requests. This ensures the same path is available to everyone regardless of their relationship to the team.
- Define and document review criteria in advance, so contributors know what is expected and reviewers aren't applying inconsistent or implicit standards.
- Separate the role of "reviews code" from "controls authorship or funding decisions" where possible to ensure technical feedback does not threaten academic standing.
- Acknowledge contributions explicitly, i.e., in release notes, a contributors file, or citation metadata, since in academic contexts, visible credit directly impacts a contributor's career in a way it may not in purely industry open source projects.

## How do you make your documentation and onboarding accessible?

### Description
Documentation and onboarding form a new contributor's first interaction with a project, setting expectations for whether joining is worth the effort. Research software documentation often relies on implicit knowledge, such as specialized numerical methods, subfield terminology, or internal lab tools. This quietly excludes people from adjacent fields or earlier career stages. Treating documentation as an accessibility surface rather than merely a reference broadens who can successfully contribute.

### Considerations
- Documentation written for "someone like the original author" tends to assume shared disciplinary background, native-English fluency, and familiarity with specific tools, none of which are safe assumptions for a broader contributor base. A glossary or background links lower entry barriers for outsiders at minimal cost.
- Language choices can also affect accessibility and inclusion. Avoid unnecessary jargon, unexplained acronyms, and wording that assumes a particular cultural background or personal circumstance.
- A working "quick start" that gets a new contributor to a successful first run is more valuable for onboarding than exhaustive reference material that nobody reads end to end.
- Accessibility in the technical sense, such as screen-reader-compatible formats, sufficient colour contrast in diagrams, and captioned video walkthroughs, is frequently overlooked in research software documentation, which skews toward static text and equations.
- If documentation is partly AI-generated, check it for unstated assumptions and jargon in the same pass as for tone, as AI output defaults to its training data register rather than your target audience.

### Solutions
- Write a "quick start" guide that takes a newcomer from zero to a working example in a small number of steps, separate from the full reference documentation.
- Define unavoidable jargon and domain-specific terms the first time they appear, or link to a short glossary.
- Check that diagrams and figures have text alternatives, and that any video content has captions or a written summary alongside it.
- Test your onboarding with outsiders from different subfields or career stages, treating confusion as documentation bugs.
- Provide setup instructions that don't assume access to your specific institutional infrastructure, such as a particular cluster, licence, or internal tool). Where such access is genuinely required, say so explicitly rather than letting newcomers discover it through failure.

## How do you welcome and support contributors from underrepresented groups?

### Description
Welcoming underrepresented contributors is not the same as having a public statement that the project welcomes them; it requires concrete practices that reduce the specific friction those contributors are more likely to encounter.
In research software, this applies to researchers from underrepresented disciplines or institutions as well as demographic groups, since the field's prestige hierarchy shapes whose contributions get taken seriously.
Sustained support, rather than one-time outreach effort, determines whether contributors remain engaged in the long-term.

### Considerations
- A single onboarding event or call for contributors can attract newcomers, but without ongoing mentorship and a low-friction path to a second contribution, many won't return.
- Tokenism: inviting underrepresented contributors into highly visible but low-influence roles is a recognised failure mode and tends to be noticed by the people it's meant to include.
- Contributors from under-resourced institutions may have less reliable internet access, older hardware, or less institutional support for open source work; therefore, scheduling and tooling choices should accommodate these constraints.
- Mentorship relationships work best when expectations and time commitment are explicit on both sides, rather than left as an informal, unstructured arrangement.
- Measuring participation (who contributes, who is retained, who advances into maintainer roles) gives you evidence of whether your practices are working, rather than relying on impressions.
- Demographic data (sex, gender, sexual orientation, disability status, race or ethnicity) directly measures whether underrepresented groups are participating, but it constitutes sensitive personal data. Under GDPR, its collection must be optional, clearly explained, and strictly anonymised or stored separately from identifying information.

### Solutions
- Set up a lightweight mentorship path for new contributors, such as informally pairing a newcomer with an existing contributor for their initial contributions, and clearly explain how to request this support.
- Participate in or model onboarding on established programs like "Google Summer of Code" or "Outreachy", which offer tested structures for first-time contributor support.
- Track basic participation metrics over time, including the number of distinct contributors, retention after a first contribution, and representation in maintainer roles, to check whether your practices are having the intended effect.
- Avoid placing a single underrepresented contributor in a highly visible "diversity" role without real decision-making authority; if you create such roles, give them genuine scope and support.
- Be explicit in calls for contributors about flexible time commitments and asynchronous participation, as assuming attendance at synchronous meetings in specific time zones excludes international contributors.
- If you run events, talks, or webinars, add an optional demographic question at registration, i.e., a dropdown such as "male", "female", "intersex", "prefer to self-identify" with a free-text option, and "prefer not to say" works well for sex, and a similar approach can be adapted for sexual orientation, disability or race so you can see over time which sessions and topics attract underrepresented groups and which don't.
- Always give people a clear way to skip demographic questions, and never make attending or participating depend on answering them.
- Whenever you collect demographic data, clearly explain why you need it, how you will use it, who can access it, and how long you will keep it.
- Use data to drive action rather than just report on it: identify participation gaps, understand the underlying barriers, and adjust outreach, event design, and community practices. For instance, invite presenters and chairs from underrepresented groups, as visible representation demonstrates that your community is truly welcoming.
- This targeted approach to recruiting underrepresented presenters and chairs is known as positive action. Permissible practices vary by jurisdiction and funder policy, so check applicable regulations before setting quotas or eligibility criteria around protected characteristics.

## How do you build DEI into your project's governance?

### Description
Governance, that is, who makes decisions, how leadership roles are filled, how disputes are resolved, etc., determines whether DEI commitments endure or rely solely on individual advocates.
Academic research software projects often default to informal control by grant holders or lab leads, concentrating power that can be invisible until someone tries to challenge a decision.
Writing governance down, even briefly, is what makes DEI commitments survive a change in personnel.

### Considerations
- Informal governance ("the PI decides") is common in research software but makes it hard for anyone to challenge a decision without risking their relationship with those who controls their funding, supervision, or career prospects.
- A documented governance structure doesn't need to be elaborate; even a short document naming who has decision authority over what, and how that can change, removes significant ambiguity.
- Succession planning is particularly critical in academic projects because maintainers often leave when grants end, students graduate, or postdocs move on. Without documented processes, a project can effectively die when these individuals depart.
- A documented Code of Conduct with an active enforcement process is a core governance commitment rather than a simple community-facing document.  It needs a designated person or defined procedure to manage reports effectively.
- Power imbalances between a project's nominal leadership and its day-to-day maintainers, such as a PI listed as lead while a research software engineer conducts the actual maintenance, should be reflected accurately in how credit and decision-making authority are desfined.

### Solutions
- Write a short governance document stating who can make which kinds of decisions (technical direction, releases, adding maintainers) and how that can change over time.
- Adopt and publish a code of conduct with a named contact or process for reports, separate from the project's primary technical leadership where feasible, ensuring reports aren't routed solely through individuals who may be involved.
- Plan explicitly for maintainer turnover by documenting onboarding steps for new maintainers and identifying a backup decision-maker, rather than assuming the current lead will always be available.
- Where a research group's internal hierarchy (PI, postdocs, students) maps onto project roles, document this explicitly rather than letting it operate as an unstated default.  This ensures external contributors understand how decisions are actually made.
- Review governance periodically as the project and team evolve, rather than treating an initial document as permanent.

## How do you make your project's events accessible?

### Description
Research software events, such as workshops, hackathons, conference sprints, and community calls, are often where new contributors decide whether the project is worth their time.
Inaccessible venues, schedules, or formats silently exclude people before they ever get to the technical content.
Event accessibility spans physical access, scheduling, financial cost, and the social experience of attending, and all of these affect who actually shows up.
Running events in hybrid mode, combining in-person and online participation rather than choosing one or the other, is one of the highest-leverage single changes available, since it directly removes physical-access barriers rather than working around them.

### Considerations
- Scheduling a recurring event in a single time zone systematically excludes contributors in other regions.
- In-person events involve substantial travel, accommodation, registration costs that are not equally absorbable across institutions, career stages, and countries, shaping who can attend regardless of interest.
- Childcare, dietary needs, and physical accessibility (venue access, captioning, quiet spaces) are concrete, addressable factors, not abstract concerns, and are often easiest to address by asking attendees directly in advance rather than guessing.
- A code of conduct that applies in principle but isn't actively enforced at an event provides little real protection; someone needs to be visibly responsible for handling concerns during the event itself.
- Hybrid formats remove physical-travel barriers entirely for people with mobility impairments or limited travel budgets, and let neurodivergent attendees who find in-person events overstimulating choose a lower-intensity way to participate, but they introduce their own accessibility considerations, such as ensuring remote participants have genuine influence on outcomes rather than passive observer status.
- Hybrid participation allows for a broader range of contributors, is one practical way to help projects identify a wider variety of requirements, use cases, and potential solutions.

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
