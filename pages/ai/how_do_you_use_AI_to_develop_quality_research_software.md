---
title: Developing Research Software with AI
description: How do you use AI to develop quality research software
contributors: [ "Michael Sparks", "Shoaib Sufi", "Aleksandra Nenadic" ]
page_id: developing_research_software_with_ai
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 1
---

![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

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

[Start from the work][ai_usecases_across_the_spectrum], not the tool or practice.

First decide whether AI is useful at all.
Then choose the practice that gives a clear benefit, preferably [at the lowest intensity that still fits the task][ai_intensity_considerations].

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

## Other Key Parts of this Guidance

* [Spectrum of Intensity of AI Usage][spectrum_of_intensity_of_ai_usage] exists to help make decisions around specific AI practices to use in developing research software quality - from No Gen AI through to swarms of autonomous agents.

* [Examples tools and mechanisms][example_tools_comparisons] brings together common current tools that can be useful when developing research software using AI. These are compared against each other and how they assist in different parts of the AI spectrum. Tools here are rapidly changing, so please do suggest new ones that are gaining traction.

* [Cross Cutting Practices][cross_cutting_practices] captures a number of quality practices that are worth consideration. These intend to illustrate and capture current best practices, rather than be exhaustive. Again, practice here is evolving.

## References and further reading

* Anthropic Claude Code documentation, "Claude Code overview" and "How Claude Code works", code.claude.com/docs.
* OpenAI Codex documentation and product overview, platform.openai.com/docs/codex and openai.com/codex.
* Ollama documentation, docs.ollama.com.
* Greg Wilson, "Twelve Ways to be Wrong about AI for Programming", Third Bit, 20 May 2026.
* OWASP Top 10 for LLM Applications, especially risks around excessive agency and insecure tool use.
* NIST Secure Software Development Framework and AI Risk Management Framework for broader security and governance context.
* International Energy Agency, "Energy and AI" and 2026 updates on data centre electricity demand and onsite gas-based generation, iea.org.
