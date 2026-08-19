---
title: Developing Research Software with AI
description: How do you use AI to develop quality research software
contributors: [ "Michael Sparks", "Shoaib Sufi", "Aleksandra Nenadic" ]
page_id: how_do_you_use_AI_to_develop_quality_research_software
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 1
---
![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

## Description

AI may democratise code-based innovation in ways not seen since the modern spreadsheet. Research software is part of this shift.

Tools that extend automation beyond specialist programmers are evolving quickly. Sensible ways to use them are still emerging. This matters for researchers who code and RSEs who support them.

AI tools can help with requirements analysis, testing, documentation, review, refactoring and maintenance. They can also produce plausible code, explanations and project activity that still need careful review.

The question is therefore not simply "should I use AI?". Better questions are:

* What AI assistance is appropriate for this task?
* What can the tool see and change?
* How will the result be checked?
* Who is responsible for accepting the work?
* What happens if the tool is wrong?

This page presents a spectrum of AI assistance based on "intensity of usage". This roughly means the autonomy, automation, authority and context involved, from no GenAI use through conversational use to agentic development.
Higher intensity does not mean better quality, greater developer maturity, higher skill or better practice.

As these tools spread, keeping research software verifiable and correct becomes more important, not less. Software must also remain reviewable: understandable, maintainable and reproducible.

For each practice, this page asks:

* What is it?
* How might you start?
* What tasks suit it?
* What are the risks?
* What quality practices help?
* When is lower or higher intensity appropriate?

Environmental sustainability matters too. It is as important to ask when lower-intensity AI is enough as when more automation helps.

GenAI encourages faster code creation. There is an old adage: if you want to go fast, go alone; if you want to go far, go together. A GenAI tool may create code quickly, but the researcher must still understand, verify and validate it.

The goal is informed choice, not adoption of any particular practice. Even if you use no GenAI yourself, understanding AI-generated systems and contributions from others remains useful.

This page gives an overview, not an exhaustive treatment of every practice.

## Considerations

The key questions are:

* What is the intensity of AI use?
* Does the result **look** correct, or is it correct?
* Are you mistaking ownership familiarity for understanding?
* What hazards exist, and what mitigations are needed?

These matter whether you use the full spectrum or choose between a few common practices.

### Intensity of AI Usage

"Intensity of AI usage" primarily describes how much autonomy a tool has, not necessarily compute level. ie how much work can be done without your intervention.

It is not a maturity scale. Higher intensity does not mean better practice, higher skill or better quality.

The term "intensity" is chosen because correlates with:

* Amount of AI use
* Risk of introduced errors
* Setup complexity
* Cost
* Environmental impact
* Consequences of failure
* Autonomy
* Output volume
* Review difficulty
* Complexity and novelty of output
* Burnout risk for the person driving the system

Also, this differs from many software engineering tools. More version control is rarely bad. More static analysis rarely raises project risk.

More AI can:

* expose more context
* create more material to review
* increase the blast radius
* give plausible mistakes more places to hide

Moving along the spectrum is therefore not levelling up. Lower-intensity practice may be the better engineering choice.

### Apparent Correctness vs Correctness

Many LLMs produce language that signals intellect and understanding. That matters because style affects trust. Formal, fluent, high-reading-age prose can make weak reasoning seem stronger.

There is a saying: "to eat your cake and have it". Many people remember the weaker version: "to have your cake and eat it". Stated plainly, the error is visible.

Now consider:

> It would, I think, be entirely proper to indicate that, where consumption of
> the cake has been established in advance, the matter may proceed indecisively
> towards possession without any necessary procedural contradiction.

It sounds more sophisticated. It is not more correct. LLM output can have the same problem. Fluent prose may sound authoritative while being wrong. The same applies to code. It may look idiomatic and still fail.

For example:

```python
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        pool = ThreadPoolExecutor(max_workers=4)  # latent bug
        future = pool.submit(work, 12)
        result = future.result()
```

This has a serious operational bug but may pass simple functionality tests. Shown alone, many people will spot it. Buried as five lines in a 300-line patch, it is easier to miss. (This specific threadpool example may disappear from generated results. The general problem remains)

The problem is not syntax. It is that the code may pass tests yet fail under real use. That makes it harder to catch when you did not write it.

**The appearance of correctness while being incorrect is an ongoing risk.**

Research software is especially exposed. A tidy change may pass basic tests while altering assumptions about units, missing data, tolerances, ordering, thresholds, sampling, model behaviour or data provenance.

### Mistaking Ownership Familiarity for Understanding

When reviewing colleagues' work, people build familiarity.

You may think:

* this person is usually right
* this person is improving
* this person often makes API mistakes
* this person writes code I can learn from

That familiarity is imperfect. People still make mistakes. Teams may argue over small pull requests from new contributors, then waive through large ones from "known good" people.

With people, shared context can partly mitigate this. A person can learn the codebase, explain intent, answer questions and improve through review.  LLMs do not improve in the same way. Without a model or tool change, the system is not learning your project judgement as a person does.

AI-generated work can also create false familiarity. You caused the code to exist. You may recognise it and have discussed it with the tool. That does not mean you understand it.

This matters later - six months or two years on, someone may need to know:

* why a change was made
* what requirement it met
* what assumptions it used
* which tests mattered
* what was not checked

If AI-generated work enters a project without clear rationale, the project inherits code without memory. That can be dangerous in research software, where scientific assumptions may not be obvious from code alone.

**Ownership of generated code is not the same as understanding generated code.**

### Risk Analysis

Risk rises as autonomy, authority and context increase. Asking a chat tool to explain an error has one kind of risk. Letting it edit a repository, run shell commands, open pull requests or interact with external systems has another.

Ask:

* What can the tool see?
* What can it change?
* What happens if it is wrong?
* What prevents harm before someone notices?
* **How large is the blast radius?**

More generated code, commits, comments or pull requests do not necessarily improve research software.
There are many valid reasons not to use AI, including:

* Skill development / craft honing
* learning
* reviewer capacity
* confidentiality
* data protection
* formal assurance
* cost
* environmental impact
* ethical concerns
* lack of project agreement

Specific risk considerations include:

* This is a probabilistic tool, not a person. Treating it as a person capable of understanding, memory and deterministic action will trip you up. (Asking the talkie toaster to be an expert does not make it one)

* Correctness often matters more than apparent correctness.

* Scientific assumptions may depend on domain knowledge, data provenance, experimental context or research claims that code alone does not reveal.

* Consequences scale with software maturity and use. A quick visualisation script has different requirements from clinical, safety-critical or other high-consequence software.

* The same AI practice may be reasonable in one context and unacceptable in another.

* GenAI tools are powerful but fallible tool-using systems. They can be useful, but can also damage code, data, files or systems they can access. This follows from the probabilistic nature of current systems.

* Natural language is not a control. Nor is asking a system to "check its own work". Such instructions may influence behaviour but cannot guarantee it. Where guarantees matter, secondary controls are needed. Their importance rises with AI intensity.

* Where consequences matter, use structural controls:
  - least privilege
  - read-only access
  - isolated checkouts
  - restricted tokens
  - protected branches
  - approval gates
  - audit logs
  - backups
  - limits on cost, time and tool access

* Simple "approval before action" is insufficient for sensitive data, credentials, unpublished results, private repositories, controlled information or high-consequence work.

The aim is not just to describe AI practices. It is to identify risks, choose proportionate intensity and keep research software reviewable, reproducible and correct.

## Solutions

[Start from the work][ai_usecases_across_the_spectrum], not the tool.

First decide whether AI is useful. Then choose a practice with clear benefit, preferably [the lowest intensity that still fits the task][ai_intensity_considerations].

For each practice:

* Define the task.
* Decide whether its AI intensity is appropriate.
* Decide what context the tool may access.
* Decide what systems it may control.
* Identify quality checks and safeguards.
* Decide how correctness will be reviewed.
* Complete that review before the result enters the research record or shared project.

"Keep the human in the loop" hides an important problem. The loop exists because someone wants work done. If that person becomes only a reviewer of generated material, rather than a creator, designer or investigator, false familiarity can build quickly.

Reviewing plausible output can feel like understanding. It is not the same.  Reviewer capacity and mental health matter too. Switching from creator to reviewer can itself have an impact. A workflow that turns a researcher or maintainer into a rubber stamp is not a quality workflow.

Beyond this:

* Pick the lowest-intensity tooling that meets the need. This limits generated work you must understand, evaluate and test.

* Do not allow access to production data, production systems or backups unless explicitly governed.

* Treat AI output as candidate work. AI may prepare artefacts, branches, patches or pull requests. A responsible person accepts, commits, promotes, merges, publishes or deploys them.

* Keep generated artefacts small enough to review. If you cannot understand the code, documentation or output, you cannot rely on it.

* Give every important part of the system a named owner. This includes generated code, tests, documentation, prompts, configuration, workflows and acceptance criteria.

* Use strong testing. Generated test-driven or behaviour-driven tests still need validation by the person responsible for the result. You might write high-level acceptance tests yourself and ask the system for supporting tests. Those remain your responsibility.

* For editor and repository-aware tools, use small branches or separate local checkouts. Ask for small changes. Avoid broad prompts such as "refactor this code" without explicit guidance. Require rationale. Run tests, but do not treat passing tests as proof of correctness.

* For agentic systems, give the tool its own local copy of what it needs. For example, use a separate checkout and remove or disable Git remotes where appropriate. You can then pull or copy candidate changes while preventing direct pushes, pull request creation, merges or deployment from that checkout. This is a guardrail, not a complete security control.

* For open repositories, include an `AGENTS.md` or equivalent instruction file. Explain what is acceptable, what is not, and why. Such files guide behaviour but are not security controls.

* For open repositories, consider separating the repository used by people from the repository or staging area used by machines. This gives human issues, pull requests and discussions more prominence while retaining a management funnel for machine-generated contributions.

Most importantly, keep asking:

* Is this approach still right?
* Is it maintainable?
* Is the review burden acceptable?
* Are responsible people still making important decisions?
* Does the workflow improve the software, or only increase activity?

Evaluate whether AI improves the system as a whole: maintainability, review burden, reproducibility, security, researcher understanding, provenance and maintainer attention.

## Other Key Parts of this Guidance

* [Spectrum of Intensity of AI Usage][spectrum_of_intensity_of_ai_usage] supports decisions about AI practices for developing quality research software, from No Gen AI to swarms of autonomous agents.

* [Examples tools and mechanisms][example_tools_comparisons] compares common current tools and how they support different parts of the spectrum. These tools change quickly, so new examples are welcome.

* [Cross Cutting Practices][cross_cutting_practices] captures quality practices worth considering. It reflects current best practice rather than attempting to be exhaustive.

## References and further reading

* Anthropic Claude Code documentation, "Claude Code overview" and "How Claude Code works", code.claude.com/docs.
* OpenAI Codex documentation and product overview, platform.openai.com/docs/codex and openai.com/codex.
* Ollama documentation, docs.ollama.com.
* Greg Wilson, "Twelve Ways to be Wrong about AI for Programming", Third Bit, 20 May 2026.
* OWASP Top 10 for LLM Applications, especially risks around excessive agency and insecure tool use.
* NIST Secure Software Development Framework and AI Risk Management Framework for broader security and governance context.
* International Energy Agency, "Energy and AI" and 2026 updates on data centre electricity demand and onsite gas-based generation, iea.org.
