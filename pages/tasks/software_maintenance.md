---
title: "Maintaining research software"
description: "Guidance on keeping research software functioning, understandable, and usable over time — covering ongoing maintenance practices, dependency management, documentation, versioning, and the management of technical debt."
contributors: []
page_id: maintaining_research_software
related_pages:
  tasks: [ci_cd, documenting_software_project, releasing_software, archiving_software, code_review]
quality_indicators:
  - dependency_management
  - has_ci-tests
  - repository_workflows
  - software_has_tests
  - software_has_documentation
  - support_issue_tracking
  - versioning_standards_use
  - has_releases
  - metadata_is_up_to_date
keywords:
  - "software maintenance"
  - "technical debt"
  - "dependency management"
  - "continuous integration"
  - "semantic versioning"
  - "changelog"
  - "refactoring"
  - "bus factor"
training:
  - name: "EVERSE TeSS"
    url: "https://everse-training.app.cern.ch"
---

This page provides an overview of key maintenance practices, practical guidance on keeping your software healthy and usable, and pointers to further resources.

## How do you maintain your research software over time?

### Description

Research software that is not actively maintained degrades in usefulness even without any intentional changes: dependencies become outdated, environments evolve, and the knowledge needed to run or extend the software quietly erodes.
Maintenance is **the work that keeps your software functioning correctly over time** — not just for you today, but for collaborators and future users (including your future self).
Without it, software that took significant effort to build can become unusable within months.

### Considerations

- **Maintenance should be ongoing, not optional.** A piece of software that runs correctly today may fail tomorrow if a dependency releases a breaking change or a runtime environment is updated. Plan for maintenance as a recurring cost, not a one-time activity.
- **The scope of maintenance grows with user base.** Software used only by its author needs less formal maintenance discipline than software shared with a team or community. Calibrate your effort to your context, but don't wait until the software is widely used before establishing good habits.
- **Documentation is part of maintenance.** Bug fixes are only part of the maintenance work.
  Code that works but cannot be understood, installed, or run by others is effectively unusable.
  Keeping your README, installation instructions, and usage examples up to date is as important as keeping the code itself working.
- **Dependencies are a liability as well as an asset.** Every dependency you take on is something that can change, deprecate, or introduce security issues.
  A smaller, well-understood dependency tree is easier to maintain than a large one. Choose your software's dependencies carefully from a set of already well-maintained projects.
- **Automated testing makes maintenance tractable.** Without a test suite, every change — including updates to dependencies or environments — carries unknown risk. Tests let you be more confident that the software still behaves correctly after any change.
- **Bus factor matters.** If only one person understands the software, it becomes unmaintainable the moment that person is unavailable.
  Onboarding documentation, code comments, and shared ownership all reduce this risk.

### Solutions

- **Write a thorough test suite and check your test coverage.** Use a coverage tool (e.g. {% tool "pytest-cov" %} for Python, {% tool "covr" %} for R) to understand how much of your code is exercised by tests, and identify gaps.
- **Set up a continuous integration (CI) pipeline** that runs your test suite automatically on every commit and on a scheduled basis (e.g. weekly).
  Scheduled runs catch breakage caused by external changes even when you are not actively developing.
  Tools such as {% tool "github_actions" %} or {% tool "gitlab-cicd" %} make this straightforward.
- **Pin and manage your dependencies explicitly.** Use a dependency management tool appropriate to your language (e.g. {% tool "pip" %}, {% tool "venv" %}, {% tool "pip-tools" %}, {% tool "uv" %} or {% tool "poetry" %} for Python, {% tool "renv" %} for R) to record exact versions and make updates deliberate and auditable.
  Consider using {% tool "dependabot" %} or {% tool "renovatebot" %} to automate dependency update pull requests.
- **Keep your documentation current.** Review your README, installation guide, and usage examples whenever you make a substantive change to the software. If you cannot install and run your own software from scratch using only your documentation, it needs updating.
- **Establish a clear issue tracker.** Use GitHub Issues, GitLab Issues, or an equivalent to record known bugs, planned improvements, and technical debt. This makes the maintenance backlog visible and shared, rather than held only in one person's head.
- **Use {% tool "semantic-versioning" %}** to communicate the nature of changes to users. Following Semantic Versioning conventions (MAJOR.MINOR.PATCH) signals whether an update is a breaking change, a new feature, or a bug fix — helping users decide when and whether to upgrade.
- **Write a CHANGELOG** and update it with each release. A clear record of what changed, when, and why is valuable both for your users and for your future self trying to understand the history of the software.
- **Reduce the bus factor.** If you are the sole maintainer, document the key decisions, architecture, and operational knowledge in the repository itself — not just in your head. If possible, share ownership with at least one other person who can act if you are unavailable.
- **Recruit help from the community of developers or users.** Ask for help maintaining your project, label your issues clearly for low-entry barriers to contributing (e.g. `good first issue`), organise regular maintenance sprints to work on the software with your collaborators.
- **Apply for funds specifically for software maintenance.** Funders are increasingly recognising the importance of investment in maintenance of key research software (e.g. see the [Software Sustainability Institute's Research Software Maintenance Fund](https://www.software.ac.uk/programmes/research-software-maintenance-fund)) to ensure it remains reliable and accessible.
- **Archive or deprecate software you can no longer maintain.** If you are unable to sustain active maintenance, make that clear in the repository (e.g. a prominent notice in the README, a repository archive, or an explicit deprecation statement). This is more helpful to users than silent abandonment.

---

## How do you track and manage technical debt in your research software?

### Description

Technical debt accumulates when shortcuts are taken, design decisions are deferred, or code grows without refactoring.
In research software, this is often unavoidable — early-stage code is written quickly to test a hypothesis, and there is rarely time to refactor before moving on.
The risk is that this debt compounds: the harder the code is to understand and change, the slower and riskier future development becomes.
Actively tracking and managing technical debt keeps your software maintainable and reduces the cost of future changes.

### Considerations

- **Not all technical debt is equal.** Some debt — a temporary workaround, a known simplification — is intentional and acceptable.
Unintentional debt (unclear code, missing tests, hardcoded values) is more dangerous because it is harder to reason about.
- **Debt that is not recorded is invisible.** If known problems are only held in memory, they will be forgotten and will not be addressed systematically.
Recording debt in an issue tracker or in code comments makes it visible and actionable.
- **Paying down debt requires protected time.** Technical debt does not reduce itself.
If maintenance and refactoring work is not explicitly allocated time alongside feature development, it will always be deferred.
- **Refactoring without tests is risky.** Before paying down significant structural debt, ensure you have tests that verify correct behaviour — otherwise you cannot be confident that your refactoring has not introduced regressions.

### Solutions

- **Use your issue tracker to record known technical debt.** Create issues (or a label/tag such as `tech-debt`) for known problems, shortcuts, and areas that need refactoring.
This makes the debt visible to everyone working on the project and allows it to be prioritised alongside other work.
- **Add `TODO` and `FIXME` comments in code** at the point where debt exists, with enough context for a future reader to understand the problem.
Consider using a linting tool to surface these systematically.
- **Allocate explicit time for maintenance and refactoring.** Whether this is a regular "maintenance sprint", a rule that a fixed fraction of each sprint is reserved for debt reduction, or simply scheduled time in your calendar — intentionality is required.
Without it, debt will grow.
- **Refactor incrementally, not all at once.** Large-scale rewrites are high risk.
Prefer small, targeted improvements — renaming for clarity, extracting a function, adding a missing test — that can be reviewed and validated individually.
- **Use static analysis tools** to surface code quality issues automatically.
Tools like {% tool "ruff" %} (Python), {% tool "lintr" %} (R), or {% tool "sonarqube" %} can flag common problems and track quality metrics over time.
- **Practice refactoring on a realistic codebase.** The Carpentries Incubator lesson [Intermediate Research Software Development in Python][intermediate-rs-python] includes a dedicated episode on code refactoring (Section 3.4) that walks through decoupling, abstractions, and incremental improvement with tests in place — directly applicable to managing technical debt.

---

## Further Reading

- **[Intermediate Research Software Development in Python][intermediate-rs-python]** — a Carpentries Incubator lesson (beta, actively maintained) developed by the Software Sustainability Institute, covering the full lifecycle of research software from environment setup and testing through to CI, code review, and managing software improvement over time. Section 5 ("Managing and Improving Software Over Its Lifetime") is directly relevant to this page; Sections 2 and 3 cover automated testing, CI, and refactoring in depth. Well-suited to researchers who write Python and want to move beyond ad hoc practices.

- **[Building Better Research Software][better-rs-python]** — a Carpentries Incubator lesson (beta, actively maintained) that teaches good software practices through a practical scenario: inheriting a broken, undocumented Python codebase and improving it step by step. Topics include reproducible environments, code readability, testing, documentation, and open software management. Particularly valuable for anyone who learns best by working through a realistic, messy starting point.

- **[The Turing Way: Reproducible Research](https://book.the-turing-way.org/reproducible-research/reproducible-research)** — a community-developed guide to good practices in research software and data science, with chapters directly relevant to maintenance, testing, and documentation. Practical, opinionated, and freely accessible; an excellent reference for researchers new to software engineering best practices.

- **[Software Sustainability Institute Guides](https://www.software.ac.uk/resources/guides)** — a curated collection of short, practical guides on topics including software maintenance, licensing, citation, and community building. Written specifically for the research software context and freely available; particularly valuable for researchers who need concise, actionable guidance.

- **[Semantic Versioning specification](https://semver.org/)** — the authoritative reference for the MAJOR.MINOR.PATCH versioning convention. Essential reading before you start releasing versioned software; explains the precise meaning of each version component and the commitments they carry for your users.

- **[Working Effectively with Legacy Code — Michael Feathers](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)** — a highly regarded book on the practical challenge of maintaining and improving software that lacks tests or clear structure. Directly applicable to research codebases that have grown organically; covers techniques for safely adding tests to untested code and reducing technical debt incrementally. Available via library or purchase.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.


[better-rs-python]: https://carpentries-incubator.github.io/better-research-software/
[intermediate-rs-python]: https://carpentries-incubator.github.io/python-intermediate-development/