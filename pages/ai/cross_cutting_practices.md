---
title: Cross Cutting Practices
description: General guidance useful at all levels
contributors: [ "Michael Sparks", "Caterina Doglioni", "Shoaib Sufi", "Ahmad Alam" ]
page_id: cross_cutting_practices
keywords: [ "llm", "AI-Assisted", "AI as an Assistant" ]
order: 20
inbeta: true
---

![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

## Cross Cutting Practices

### Start With the work, Start Simple, Extend later

This applies both in terms of how to get started, but also in terms of how to apply practices. It's very easy to read practices like this page, and assume that we're advocating doing everything at once. These are practices, designed to keep your code, your work, your research, understandable, reproducible and safe. If you're playing with ideas some of the practices make no sense. If you're managing a project that requires reproducibility and dependability you probably want to consider which of these practices give you the largest benefit.

The key thing is to start with the work you want to achieve, then identify the practices that are actually useful to you and your project.


### Use strong specifications and tests

Strong tests and specifications give people and AI tools a stable target. New code can then be checked against that target.

AI-assisted coding works better when intended behaviour is kept separate from the implementation.

Tests can provide a shared, executable description of what the software should do. [BDD][BDD]-style [acceptance tests][ACCEPTANCETESTS] (eg using [Gherkin][GHERKIN]) can capture key behaviour in terms people can review and discuss. Lower-level unit tests, often developed with [TDD][TDD] (eg using Python's [`unittest`][UNITTESTS]), can capture details, edge cases and interfaces.

This is useful when code may be rewritten or regenerated. The aim is not to reproduce the same lines of code. It is to reproduce the behaviour that matters.

Tests also help when moving from exploratory work to production software. A researcher may first create a sketch or prototype. They can then capture its key behaviour as AI-written acceptance tests for verification. This is important before asking an AI tool to refactor, extend or reimplement it.

AI can help write tests and specifications. It can also check its own homework. But those checks should be independently verified by a person or a different AI system. This helps avoid the same misunderstanding appearing in both the code and its tests.

### You promote the work, the AI does not

A useful default is:

* AI prepares candidate work
* a person reviews it
* a person pulls, commits, merges, publishes or deploys it

A generated branch, patch or pull request is not an accepted contribution.
It is a candidate contribution.

This matters because AI tools can create plausible work quickly.
The question is not just whether the work exists.
The question is whether a person understands it, accepts it, and can explain why it is correct.

For individual work, this may mean copying the change into your own checkout, committing it yourself, and recording why you accepted it.

For a shared project, this may mean a maintainer reviews, adapts and merges it through the normal contribution process.

For research outputs, this may mean the researcher responsible for the result can explain how the generated artefact was checked.

### Use a separate AI working copy

Where practical, give AI tooling its own local checkout.
Treat that checkout as owned by the tool, not as your main working copy.

The aim is to let the AI prepare changes without giving it authority to change shared project state.

A useful pattern is:

* create a separate local checkout for the AI tool
* remove or disable remote push access from that checkout
* keep your own normal checkout separate
* add the AI checkout as a local remote, or copy patches across manually
* inspect and pull individual changes into your own checkout
* commit and push only changes you understand and approve

Removing a Git remote is a useful guardrail. It is not a complete security control.

Do not give the tool credentials, tokens, or access it does not need.

This is especially useful where the AI tool can run Git commands, stage files,
commit changes, create branches, or interact with repository tooling.

The point is not that this makes AI output safe.
The point is that it gives the people working with AI a clear review boundary.

### Treat remote execution as a governance boundary

When an AI tool runs outside your local machine, the risk changes.

A managed or cloud agent may receive repository access, logs, configuration, test output, project structure, private package names or other context.

Before connecting a remote service, decide:

* What code, code and logs it may see
* What repositories it may access
* What permissions it receives
* Whether it can create branches or pull requests
* Whether it can use paid or shared compute resources

Remote execution may be useful. It can reduce setup difficulties and run checks in a clean environment.
It should **not** be treated as merely a more convenient local editor - due to greater risks.


### Protect maintainer attention

Maintainer attention is an irreplaceable limited resource.

AI-generated activity can look useful while consuming review capacity.
This includes duplicate issues, noisy comments, plausible but low-value pull requests, dependency updates, broad refactors, and repeated suggestions.

For research software, this matters because important project knowledge is often held in discussion:
scientific assumptions, validation choices, roadmap decisions, domain constraints and user needs.

If automation overwhelms or hides those conversations, it is damaging the project.

Useful controls include:

* rate limits
* clear labels
* AI staging repositories
* Agent only staging areas
* maintainer opt-in review
* no expectation that every AI-generated suggestion will be reviewed

The aim is to stop machine-generated volume from becoming a second inbox with unmanageable priority.

### Review actions as well as outputs

Once AI tools can act, review is not only about code.

You may need to check what the tool did:

* Files read or changed
* Commands and tests that were ran
* Data and services accessed and contacted
* What branches, commits or pull requests it created
* Assumptions underlying these actions and changes
* Last, but not least - what it did not verify

This becomes more important as tools gain access to repositories, terminals, CI systems, issue trackers, cloud resources or external APIs.

The risks include unsafe action and bad code.

### Do not treat prompts as controls

Natural language instructions are useful.
They are suggestions (guidance), rather than controls.

You need to treat AI as untrusted rather than potentially untrustworthy. Currently and for the foreseeable future the probablistic nature of GenAI based systems requires this stance. While such systems are generally good at following instructions, they will occasionally ignore such guidance.

Natural language guidance should be backed up by actual guardrails. For example:

* "Do not push" needs backing up with "this checkout cannot push".
* "Ask before deleting" is weaker than "this account cannot delete".
* "Do not access production data" is weaker than "production data is unavailable".

Where the consequence matters, structural controls follow standard best practices for untrusted domains.

* least privilege
* read-only access
* restricted tokens
* protected branches
* no production credentials
* no unnecessary secrets
* allowlists
* audit logs
* Approval gates managed by designated people
* immutable backups
* time and cost limits

The safe behaviour should not depend only on the model choosing correctly.

### Keep the intensity justified

Higher-intensity AI use should solve a real problem.

It may be justified when it reduces setup difficulties, improves reviewable output,
runs checks in a reproducible environment, or helps explore several candidate approaches.

It is not justified simply because the tool offers the feature.

Periodically ask:

* Is this still helping?
* Is the review burden reasonable?
* Is the project easier to understand?
* Are maintainers being helped or overloaded?
* Are people still making the important decisions?
* Would a lower-intensity practice be enough?

Often the right response is not a better prompt.
It is less authority, less context, fewer tools, or no AI for that task.
<!-- References -->

[BDD]: https://cucumber.io/docs/bdd/
[GHERKIN]: https://cucumber.io/docs/gherkin/reference/
[TDD]: https://agilealliance.org/glossary/tdd/
[UNITTESTS]: https://docs.python.org/3/library/unittest.html
[ACCEPTANCETESTS]: https://en.wikipedia.org/wiki/Acceptance_testing
