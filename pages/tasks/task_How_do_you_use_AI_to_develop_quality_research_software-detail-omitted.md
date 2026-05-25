---
title: How do you use AI to develop quality research software
description: How do you use AI to develop quality research software (spectrum detail omitted)
contributors: [ "Michael Sparks" ]
page_id: ai_assisted_rs_development_shorter
keywords: ["ai", "software development", "task automation", "github actions" ]
---

# How do you use AI to develop quality research software?

## Description

AI may democratise code-based innovation in ways not seen since the creation of the modern spreadsheet.
Research software is part of this shift.

Tools that broaden automation beyond specialist programmers are evolving quickly.
Sensible ways to use them are still emerging.

This matters for researchers who code.
It also matters for RSEs who support them.

AI tools can help with requirements analysis, testing, documentation, review, refactoring and maintenance.
They can also produce code, explanations and project activity that look plausible, but still need careful review.

The question is therefore not simply "should I use AI?"

A better question is:

* What kind of AI assistance is appropriate for this task?
* What can the tool see?
* What can the tool change?
* How will the result be checked?
* Who is responsible for accepting the work?
* What happens if the tool is wrong?

This page presents a spectrum of AI assistance based on "intensity of usage".
This roughly means the degree of context, automation, authority and autonomy involved: from no GenAI use, through conversational use, to agentic development.

Higher intensity does not mean better quality.
It does not imply greater developer maturity, skill level, or better practice.

Given the nature of the tooling, keeping research software verifiable and correct becomes more important, not less.
The software also needs to remain reviewable: understandable, maintainable and reproducible.

For each practice on the spectrum, this page asks:

* What is it?
* How might you start?
* What are appropriate tasks?
* What are the concerns and risks?
* What quality practices help?
* When might lower or higher intensity AI practices be appropriate?

Environmental sustainability matters here too.
It is as important to ask when lower-intensity AI use is enough as it is to ask when more automation is useful.

GenAI encourages faster code creation.
There is an old adage: if you want to go fast, go alone; if you want to go far, go together.

That balance is sharper here.
A GenAI tool may create code quickly, but the researcher still needs to understand, verify and validate the result.

The goal of this page is to support informed choice. It is not to promote adoption of any particular practice.

Even if you choose no GenAI use in your own tooling, understanding the implications of AI-generated systems and contributions from others is still useful.

This page gives an overview. It cannot be extensive on every practice.


## Considerations

The key considerations here are:

* What is the intensity of AI use?
* Does the result **look** correct, or is it correct?
* Are you mistaking ownership familiarity for understanding?
* What are the hazards, and what mitigations are needed?

These questions matter whether the detailed spectrum is used directly,
or whether the reader is only choosing between a few common AI practices.


### Intensity of AI Usage

This page uses "intensity of AI usage" to describe how much context, authority,
automation and autonomy a tool has.

This is not a maturity scale.

Higher intensity does not mean better practice.
It does not mean higher skill.
It does not mean better quality.

The phrase is deliberate because intensity correlates with other things:

* Amount of AI use in the workflow
* Risk of introduced errors
* Complexity of the AI setup
* Cost
* Environmental impact
* Severity of consequences of failure
* Level of autonomy
* Volume of output
* Difficulty of review
* Complexity and novelty of output
* Risk of burnout for the person driving the system

This is different from many software engineering tools. "More version control" is rarely a bad thing. "More static analysis" rarely increases project risk.

More AI can increase risk:

* More context means more exposure.
* More automation means more to review.
* More authority means larger blast radius.
* More output means more opportunity for plausible mistakes to hide.

As a result, moving along the spectrum is not levelling up.
A lower-intensity practice may be the better engineering choice.


### Apparent Correctness vs Correctness

Many LLMs produce language that signals intellect and understanding.

This matters because style affects trust.
Formal, fluent, high-reading-age prose can make weak reasoning look stronger than it is.

There is a saying: "to eat your cake and have it".
Many people remember the weaker version: "to have your cake and eat it".
Stated plainly, the error is visible.

Now consider this version:

> It would, I think, be entirely proper to indicate that, where consumption of
> the cake has been established in advance, the matter may proceed indecisively
> towards possession without any necessary procedural contradiction.

That sounds more sophisticated. It is not more correct.

LLM output can have this problem.
The prose may be fluent.
The answer may sound authoritative.

The same can and does occur with code. The code may look idiomatic. The result may still be wrong.

For example, this code has a serious operational bug, but would likely pass simple functionality tests:

```python
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        pool = ThreadPoolExecutor(max_workers=4)  # latent bug
        future = pool.submit(work, 12)
        result = future.result()
```

Presented alone, many people will say "of course that is wrong".
In a larger patch - 5 lines in 300 or more - it is much easier to miss.

The problem is not syntax or that, when pointed out, the code obviously fails.
The problem is that it may pass tests while failing under real use.

That makes it an operational error. This also makes it harder to catch if you are not the one writing the code.

This specific threadpool example may disappear from generated results over time.
The general problem will remain.

**The appearance of correctness while being incorrect is an ongoing risk.**

Research software is especially exposed to this.
A change can look tidy, pass basic tests, and still alter assumptions about units,
missing data, tolerances, ordering, thresholds, sampling, model behaviour or
data provenance.

### Mistaking Ownership Familiarity for Understanding

When reviewing work from colleagues, people build familiarity.

You may start to think:

* this person is usually right
* this person is improving
* this person often makes API mistakes
* this person writes code I can learn from

That familiarity is not perfect - people still make mistakes.

People sometimes argue over small pull requests from new contributors, then waive through large pull requests from "known good" people.

With people, this can be partly mitigated because shared context grows.
A person can learn the codebase.
They can answer questions.
They can explain intent.
They can improve through review.

With LLMs, that pattern does not work in the same way.

Without a model or tool change, the system is not learning your project judgement
in the way a person does.

AI-generated work can create false familiarity.
You caused the code to exist.
You may recognise it.
You may have discussed it with the tool.
That does not mean you understand it.

This matters when the work is reviewed later.

Six months later, or two years later, someone may need to know:

* why this change was made
* what requirement it satisfied
* what assumptions it relied on
* what tests were meaningful
* what was not checked

If AI-generated work enters the project without a clear rationale, the project inherits code without memory.

That is potentially dangerous in research software.

Research code often encodes scientific assumptions that are not obvious from the code alone.

**Ownership of generated code is not the same as understanding generated code.**

### Risk Analysis

Risk increases as context, authority and autonomy increase.

Asking a chat tool to explain an error message has one kind of risk.
Allowing a tool to edit a repository, run shell commands, open pull requests, or interact with external systems has another.

The core questions are:

* What can the tool see?
* What can the tool change?
* What happens if it is wrong?
* What prevents harm before a person notices?
* **How large is the blast radius?**

More generated code, commits, comments or pull requests do not necessarily mean better research software.

There can be good reasons not to use AI, including:

* learning
* reviewer capacity
* confidentiality
* data protection
* formal assurance
* cost
* environmental impact
* ethical concerns
* lack of project agreement

When considering and mitigating risk, there are a number of specific considerations:

* Correctness often matters more than apparent correctness.

* Scientific assumptions embedded in code may not be obvious from the code.
  They may depend on domain knowledge, data provenance, experimental context, or research claims.

* Consequences scale with code maturity and use. The more mature or used a tool is the greater the risks. A quick visualisation script has different quality requirements from software used in clinical, safety-critical or high-consequence contexts.

* The same AI practice can be reasonable in one context and unacceptable in another.

* GenAI tools are best treated as powerful but fallible tool-using systems. They can be useful.
  They can also damage any code, data, files or systems they can access.
  This is simply a consequence of the probablistic nature of how these systems currently operate.


* Natural language is not a strong control. Nor is asking the system to "check its own work". At best such controls suggest specific control flows which may be followed, but without guarantee. Where guaranteed controls are needed, secondary measures and systems will be necessary. These become more important as the level of AI intensity usage increases.

* Where the consequence matters, use structural controls:
  - least privilege
  - read-only access
  - isolated checkouts
  - restricted tokens
  - protected branches
  - approval gates
  - audit logs
  - backups
  - limits on cost, time and tool access

* Simple "approval before action" is not enough for sensitive data, credentials,
  unpublished results, private repositories, controlled information or
  high-consequence work.

* The aim of this page is therefore not only to describe AI practices.
  It is to help identify the risks, choose a proportionate level of AI intensity,
  and apply quality practices that keep research software reviewable, reproducible
  and correct.


## Solutions

Start from the work, not the tool or practice.

First decide whether AI is useful at all.
Then choose the practice that gives a clear benefit, preferably at the lowest intensity that still fits the task.

For each AI practice you choose:

* Define the task
* Consider if the intensity of AI usage is appropriate for that task
* Decide what context the tool may access
* Decide what systems the tool may control
* Identify the quality checks and balances
* Consider how you will review correctness.
* Perform that review before the result becomes part of the research record or shared project.

The phrase "keep the human in the loop" hides an important problem.

The loop exists because a person wants the work done.
If that person becomes only a reviewer of generated material, rather than a creator, designer or investigator, false familiarity can build quickly.

Reviewing a stream of plausible output can feel like understanding.
It is not the same thing.

It also matters for reviewer capacity and mental health.
There is also potentially a mental health impact of switching from creator to reviewer
A workflow that turns a researcher or maintainer into a rubber stamp is not a quality workflow.

Beyond the above:

* Pick the lowest intensity tooling that matches your need.
  This limits the volume of generated work you need to understand, evaluate and test.

* Do not allow access to production data, production systems or backup systems
  unless that access is explicitly governed.

* Treat AI output as candidate work.
  The AI may prepare artefacts, branches, patches or pull requests.
  A responsible person accepts, commits, promotes, merges, publishes or deploys them.

* Keep generated artefacts small enough to review.
  If you cannot understand the code, documentation or output, you cannot rely on it.

* Every important part of the system needs a named owner.
  This includes generated code, generated tests, documentation, prompts,
  configuration, workflows and acceptance criteria.

* Strong testing is necessary.
  If you generate test-driven or behaviour-driven tests, those tests still need validation by the person responsible for the result.
  You might write high-level acceptance tests yourself and ask the system to fill in supporting tests.
  That supporting material is still your responsibility.

* For editor and repository-aware tools, use small branches or separate local checkouts.
  Ask for small changes.
  Avoid broad prompts such as "refactor this code" without explicit guidance.
  Require a clear rationale for changes.
  Make sure tests are run, but do not treat passing tests as proof of correctness.

* For agentic systems, give the tool its own local copy of what it needs.
  For example, use a separate checkout and remove or disable Git remotes where appropriate.
  This lets you pull or copy candidate changes from the AI working copy, while preventing direct push, pull request creation, merge or deployment from that checkout.
  This is a guardrail, not a complete security control.

* For open repositories, include an `AGENTS.md` or equivalent instruction file.
  Use it to guide tools and contributors on what is acceptable, what is not, and why.
  These files guide behaviour; they are not security controls.

* For open repositories, consider separating the repository used by people from the repository or staging area used by machines.
  This gives issues, pull requests and discussions from people greater prominence.
  It does not prevent GenAI-based contribution.
  It provides a management funnel for dealing with machine-generated issues, suggestions and pull requests.

Most importantly, keep asking:

* Is this approach still right?
* Is it maintainable?
* Is the review burden acceptable?
* Are the responsible people still making the important decisions?
* Does the workflow improve the software, or only increase activity?

Evaluate whether AI use improves the system as a whole:
maintainability, review burden, reproducibility, security, researcher understanding,
provenance and maintainer attention.

## Spectrum of Intensity of AI Usage

### Overview

The spectrum below describes AI usage practices by intensity.

The numbering is for convenience. Higher numbers *imply* more intense AI use. They do not imply better practice, greater maturity or better quality.

A whiteboard on the door of a shared space may be the simplest way to book use of that space. It may also be the optimal mechanism.

The same applies here. Use the practice that fits the work.



* **0. No GenAI usage** - We all start here, but there can be good reasons to choose this level. Examples: learning exercises, controlled data, secure environments, formal assurance, environmental or ethical concerns, or projects that have not agreed a policy.

* **1. Conversational interaction** - Conversations asking for explanations, background, design trade-offs, unfamiliar errors and conceptual help. Examples: "Explain this compiler error", "What should I test?", "What assumptions does this numerical method make?", "What misunderstandings might the average developer have based on this code?" (for sanity checking API design)

* **2. Conversational artefact creation** - Chat-based creation of small, reviewable outputs. Examples: a helper function, a test skeleton, a README paragraph, a regular expression, or a command-line usage example.

* **3. Conversational Creation with Zip Files (etc)** - Providing selected files, snippets, logs or zip files so the tool can reason about the content. Examples: "Suggest tests for these files", "Review this small package structure", "Explain why this minimal example fails."

* **4. IDE autocomplete and inline suggestions** - AI suggestions appear while editing. Examples: completing boilerplate, filling repetitive test cases, suggesting docstrings or small local code patterns.

* **5. Editor-integrated local assistant** - The assistant can make bounded edits inside the editor. Examples: refactor a function, add type hints, generate tests for a module, update these docstrings.

* **6. Repository-aware assistance** - The tool can search and reason across the repository. Examples: trace where a setting is used, identify tests for a feature, propose where to add a new option.

* **7. Constrained local tool-using agents** - An agent can edit files, run commands and iterate locally under supervision. Examples: fix a failing test on a disposable checkout, run linting, prepare a patch without pushing.

* **8. Managed or cloud coding agents** - A hosted or managed agent works in a configured environment, often asynchronously. Examples: ask a cloud coding agent to implement a small issue, run tests, and prepare a branch or PR for review.

* **9. CI/PR/repository agents** - Agents are integrated into shared project workflows. Examples: review PRs, suggest CI fixes, triage issues, draft dependency updates, or maintain an AI staging repository.

* **10. Open-ended autonomous agents** - Broad tool-using systems with persistence, scheduling or external integrations. Examples: agents that can act across repositories, services, email, cloud resources or multiple tools over time.


<!-- --------------------------------------------------------- -->


## Examples of tools and mechanisms

**Where tool names are included in this document, they are examples, not recommendations**

They are included because otherwise the spectrum is too abstract to be useful.
Due to rapid change in this area, the tools will likely change.

Talking about version control without mentioning git, GitHub or GitLab would be odd.
The same applies here: it's important to be clear what sorts of tools and mechanisms are being referred to.

Despite shorthand, a product name is not the same thing as a practice.
The same tool may be used as a chat system, an autocomplete tool, repository-aware assistant, local agent, or cloud workflow depending on configuration.
Similar tools may have very different levels of context, authority and autonomy.

Features, licensing, data-handling terms, institutional approval and availability all change.
**These examples make the discussion concrete, but should not be read as endorsement.**

Where project data, private repositories, sensitive data or credentials are involved, use only tools approved for that context.
If in doubt, use a lower intensity practice and discuss with other people before giving a tool access.
This may include an RSE, data steward, information security colleague or maintainer.

| Spectrum area                       | Examples and mechanisms |
|-------------------------------------|-------------------------|
| Chat and explanation                | ChatGPT, Claude, Gemini, Microsoft Copilot, institutionally provided chat tools |
| File or context chat                | ChatGPT file upload, Claude file upload, Claude Projects, selected zip files, minimal reproducible examples, pasted logs, pasted `git diff` output |
| IDE autocomplete                    | GitHub Copilot, Gemini Code Assist, Cursor, Continue, JetBrains AI Assistant, editor-specific plugins |
| Editor and repository assistance    | GitHub Copilot Chat/Edits in VS Code, Cursor, Codex in an IDE, Continue, Cline, Zoo Code, JetBrains AI Assistant |
| Local tool-using agents             | Claude Code, Codex CLI, Aider, Cline, Zoo Code, Gemini CLI and similar terminal or editor agents |
| Project instructions and extensions | `AGENTS.md`, `.github/copilot-instructions.md`, `CLAUDE.md`, Cursor Rules, `SKILL.md`-style skill folders, MCP servers |
| Managed or cloud coding agents      | Codex web/cloud, GitHub Copilot coding agent, Google Jules, Devin, Replit Agent and similar hosted coding agents |
| PR, CI and repository agents        | GitHub Copilot pull request summaries or review, GitLab Duo merge request support, Gemini Code Assist pull request review, repository bots, dependency-update automation, AI staging repositories |

The most important question is not simply "which tool is this?".

The important question is:

* What can this tool see?
* What can this tool change?
* What can this tool trigger?
* What resources can this tool use?
* What happens if it is wrong?
* What prevents harm before a person notices?
* **How large can the blast radius be if you get this wrong?**


## Cross Cutting Practices

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


<!-- --------------------------------------------------------- -->

## High-level comparison: Claude Code, OpenAI Codex and Ollama-based approaches

The tool landscape changes quickly, so this comparison should be treated as a way to think about classes of tool rather than as a permanent product ranking. The important differences are where the model runs, how much repository context it can access, what tools it can call, how permissions are managed, and how easy it is to create a reproducible reviewable workflow.


| **Approach** | **Typical shape** | **Strengths** | **Main cautions** |
|--------------|-------------------|---------------|-------------------|
| Claude Code-style terminal agents \
| Agentic coding tool in or near the developer terminal; can read a codebase, edit files, run commands and integrate with development workflows. \
| Good for local iterative work, debugging, documentation, tests and repository navigation where a developer can supervise commands and diffs. \
| Powerful because it can act. Use sandboxes, command approval, restricted credentials and clear "no push/deploy/delete" rules. Treat shell access as a major boundary. |
| OpenAI Codex-style managed/cloud agents \
| Coding agent working in a configured cloud environment or connected repository, often asynchronously and sometimes in parallel workspaces. \
| Good for isolated tasks, parallel candidate patches, routine issues, tests and documentation when the environment is well specified. \
| Repository permissions, cloud context and PR creation need governance. Provide setup docs and tests; avoid broad organisation access and sensitive data. |
| Ollama/local-model approaches \
| Local runtime for running models on local hardware, often combined with editor plugins, scripts or custom agent harnesses. \
| Useful where local control, experimentation, cost control or data locality matters. Can support private prototypes and custom workflows. \
| Local does not automatically mean safe or high quality. Smaller/local models may perform worse on complex code; custom harnesses need their own permission, logging and review design. |

In practice these approaches overlap. A terminal agent may call remote models. A cloud agent may work from a repository with local-style tests. An Ollama-based setup may be connected to an editor or agent framework. For research software, the selection question is less "which is best?" and more "which mode gives enough help while keeping context, permissions, review and reproducibility under control?"

For cautious adoption, a sensible route is: conversational explanation; small generated artefacts; editor assistance on low-risk files; repository-aware read-only exploration; local agent in a disposable branch; then managed or CI-integrated agents only when project governance is ready. This is not a ladder. Stop at the least-automated pattern that gives genuine value, and step back when quality, learning, confidentiality, reviewer capacity, cost or environmental impact argue for less automation.

## References and further reading

* Anthropic Claude Code documentation, "Claude Code overview" and "How Claude Code works", code.claude.com/docs.
* OpenAI Codex documentation and product overview, platform.openai.com/docs/codex and openai.com/codex.
* Ollama documentation, docs.ollama.com.
* Greg Wilson, "Twelve Ways to be Wrong about AI for Programming", Third Bit, 20 May 2026.
* OWASP Top 10 for LLM Applications, especially risks around excessive agency and insecure tool use.
* NIST Secure Software Development Framework and AI Risk Management Framework for broader security and governance context.
* International Energy Agency, "Energy and AI" and 2026 updates on data centre electricity demand and onsite gas-based generation, iea.org.


