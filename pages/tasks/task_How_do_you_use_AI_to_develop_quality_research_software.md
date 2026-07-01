---
title: How do you use AI to develop quality research software
description: How do you use AI to develop quality research software
contributors: [ "Michael Sparks" ]
page_id: ai_assisted_rs_development
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


## 0. No GenAI usage

### Overview

This is where we all start. Many will stay here too.

For the purpose of this spectrum, "No GenAI usage" means an active decision not to use GenAI.
There may be many diverse reasons for this:

* Policy: environmental concerns, institutional policy, formal assurance
* Legal: data sensitivity, contractual limits, secure environments, patent creation
* Personal: reviewer capacity, desire to learn a new skill, or being evaluated on skill acquisition

### Getting Started

Of these, policy and legal reasons are most likely to require action.
This is essentially project governance.

* Document clearly where it will be read (such as a project `README.md` file) by people or agents (in an `AGENTS.md` file) the decision for no GenAI usage.
* Include the reason where practical. Noting whether the reason is policy, legal or personal makes it easier for contributors to understand what is and is not acceptable.

The prohibited use may differ by context.
For example, GenAI use might be prohibited for code creation, code verification, documentation, diagrams, examples, tests, review comments or generated data.

One project may prohibit GenAI because the repository processes sensitive data about identifiable people who are at risk.
Another may prohibit it because the project owner has time to review contributions from people, not from machines.
Another may prohibit it because the work is being assessed as a learning exercise.

Useful preparation includes deciding:

* what data, code and documents must not be sent to unapproved tools
* whether any exceptions exist
* whether offline LLM use is allowed
* whether toy repositories or disposable branches may be used for experimentation
* whether GenAI-created images, diagrams, examples or documentation are allowed

If the answer is no, say no explicitly.

### Sample Appropriate Practice

A good first practice is simply to write down what the project currently allows and does not allow.
This can be a short note in the README, project documentation or local group guidance.
It should be as simple as practical.

While the assumption is "No GenAI usage", the considerations are similar to other levels:

* It should make clear whether AI-generated code (etc) is allowed under any circumstances. (no)
* What material may be shared with external tools (none)
* Who is responsible for warranting that submitted work follows the no-GenAI policy. (the contributor)
* What happens if GenAI was used despite the no-use policy, or if there is uncertainty.
  In most cases this should be disclosed so the project can decide what to do.
  Whilst this may be accidental, responses may vary from rejecting the work,
  through to appropriate legal or regulatory action.


### Concerns/Risks

Silence can be a risk.

If a project says nothing, contributors may assume that any available tool is acceptable.
They may assume that private use of offline GenAI tooling does not need to be disclosed.

This can lead to unreviewed AI-generated code, accidental data exposure,
unclear provenance, or disagreement later about what was acceptable.


### Quality Practice

If GenAI is not allowed, say no explicitly.
If there are exceptions, name them explicitly.
Include why where practical.

Do not leave people to infer the policy.

This reduces the risk of mistakes later.
It clarifies review expectations, disclosure norms, data restrictions, responsibility and the reasons for not using AI in this context.



### AI Intensity Considerations

This level is particularly suitable when:

* The purpose is learning or assessment
* Data or code cannot be shared safely
* Review capacity is limited
* Environmental or ethical concerns outweigh likely benefit
* The project has not agreed how AI-assisted work should be handled

If these criteria don't apply, it may be appropriate to consider a different level, if there are benefits in doing so.



<!-- --------------------------------------------------------- -->



## 1. Conversational Interaction

### Overview

This is the simplest use of GenAI.

At this level, the tool explains, discusses, challenges and argues.
It does not write project code, edit files, run commands or connect to repositories.
Changes are not made on your behalf.

This can help with error messages or summarising unfamiliar code.
You can discuss possible design choices, outline documentation gaps, or critique ideas.
You can ask for explanations of testing concepts.
It can suggest questions before changing analysis code.

Examples include ChatGPT, Claude, Gemini, Microsoft Copilot, or institutionally provided equivalents.

The important point is the practice. This is conversational interaction. It is not automated development.


### Getting Started

If asking for an explanation, include enough context.

For example, before asking for fixes, include:

* what you expected
* what happened instead
* the error message
* the command you ran
* the operating system or environment
* relevant package versions

If you think there may be multiple causes, you can ask for them, ask what needs checking and what information might be useful.
This keeps the task focused on diagnosis and learning.

If asking for a critique, you will usually need similar context.
For example:

* "What would the average researcher who codes make of this API?"
* "I'm thinking of using MPI in this project. Does that make sense?"


If weighing up an approach, placing the argument with a third person can help limit LLM sycophancy.

For example:

* "A colleague has suggested using lightweight fibers rather than operating system threads.
   I'm not sure this is a good idea given we will only have 20 users.
   What are the pros and cons?"

This reduces the chance that the system simply agrees with you.

It can be useful to ask the system to critique its answer before giving a final response.
That introspective step can encourage a better mode for explanations, critiques and arguments.

If you are copy/pasting content, remove sensitive details such as:

* private data
* local paths
* usernames
* server names
* tokens
* unpublished results
* other sensitive project details

Even error messages can reveal more than expected.

### Sample Appropriate Practice


Some sample prompts that you might use at this stage include:

* "Explain this pytest error.
  Do not write a fix yet.
  List likely causes.
  List missing information.
  List what I should check."

* "This function processes tabular data.
  It supports a published analysis.
  What assumptions does it make?
  Consider missing values, column names and ordering."

* "What tests would you expect for this command-line interface?"

* "What misunderstandings might a new developer have here?"

* "Explain this error message.
  I want to understand the system.
  I do not just want the error removed."

### Concerns/Risks

The main risk is false confidence.

A confident explanation is not a confirmed diagnosis.
An LLM can say "This is definitely the cause" several times in a row,
while giving several different causes.

The tool may explain a common problem, even when that is not your problem.

These tools invent commands, package names, APIs, configuration options, citations and project conventions.

There is a context-sharing risk.
A harmless-looking question may include private code.
You may inadvertently include unpublished results, sensitive file paths
or details relating to internal systems.

Conversational use is low intensity. It is not zero risk.


### Quality Practice

Treat the answer as a hypothesis that you need to check.
This is especially necessary with overconfident explanations.

Verify answers against project documentation, official documentation, tests or examples.
Ask a knowledgeable person where needed.

Watch for invented artefacts, such as APIs, packages, flags and citations.


These conversations should be honed toward improving your understanding, not replacing it.

Useful follow-up questions include:

* What could be wrong here?
* What assumptions are you making?
* What should I verify?
* What evidence would confirm this?
* Which parts need domain review?

### AI Intensity Considerations

Stay at this level when conversation is helping you understand the problem.

Consider greater AI intensity practice when the explanation has clarified a small artefact that would be useful and easy to review. For example, this might be a test skeleton, documentation draft or small example.

Consider dropping AI when the conversation starts replacing reading, debugging, testing or domain understanding.
Conversational use should build understanding - not bypass it.


<!-- --------------------------------------------------------- -->


## 2. Conversational artefact creation

### Overview

At this position, GenAI creates small artefacts rather than only explanations.

Suitable outputs include a short helper function, a test skeleton, a README paragraph,
a docstring, a regular expression, a small data-cleaning example, or a command-line
usage snippet.

"Small" here means small enough that you can read every line, explain what it does,
and check it against an example you understand.

If the output is too long to review carefully, it is too large for this practice.

This is perhaps best viewed as conversational collaborative creation.
The artefact may be small, but the discussion around it may be longer.
This is often where the most useful work happens.

The prompt can be lengthy and detailed even when the artefact is small.
Often this can require lengthy corrections and updates as part of the discussion.
Indeed, this often gives better results because the system has better material to work from.

The same chat systems used for conversational interaction can be used here.

### Getting Started

Give the tool the behaviour you want, the constraints, and a request for tests or examples.

Avoid broad prompts such as "write the module".
Prefer a bounded request.

A simple example of this might be:

"Write a function that does X. Use only the standard library. Include three examples covering normal input, missing input and malformed input."

Often a longer prompt is useful, especially when balancing design constraints.

For example, you might specify:

* the intended audience
* patterns to avoid
* acceptable complexity
* expected length
* performance expectations
* error-handling style
* examples that matter
* assumptions that must not be changed

These details may end up being specified over multiple messages.
The conversation gives the tool more useful context.

Do not treat "generated" as the same as "accepted".
Ask for the artefact, read it, challenge it, adapt it, then add it yourself.

This practice works best when you keep talking to the system and probing assumptions:

* why it made choices
* what edge cases it missed
* what assumptions it made
* Can you get a simpler/shorter version
* how it compares against metrics that matter to you

Many people underuse this level because they underestimate the value of the interaction.
The point is not to minimise conversation.
The point is to keep the generated artefact small enough to understand.

### Sample Appropriate Practice

Some simple prompts at this stage might look like this:

* "Write a Python function that validates these metadata fields.
  Use only the standard library.
  Return clear error messages.
  Include simple pytest tests."

* "Draft a README section explaining how to run the test suite.
  Keep it factual and mark anything you are unsure about."

* "Write three possible regression test cases for this bug report.
  Do not write implementation code."

* "Draft a docstring for this function based only on the code below.
  Mark any behaviour that is unclear."

A more useful prompt might look like this:

* "Write a small validation helper for these metadata fields.

  Design forces:
  - clear code matters more than clever code;
  - no new dependencies;
  - suitable for researchers who maintain scripts occasionally;
  - error messages should help the user fix the input;
  - missing values and malformed values should be handled separately.

  Keep the function small.
  Include examples and simple pytest tests.
  Note any assumptions."

### Concerns/Risks

Asking a model to check its own work can be problematic. The same misunderstandings used to create the artefact are likely used to check it. This can cause problems with generated tests and generated code. It will very likely be internally consistent, but not consistent with what you need.

If the model generates tests, check their scope carefully. This is especially true for BDD-style tests. The tests can simply copy the model's misunderstanding of the requirements. By contrast a person in the same situation would likely share your understanding of research requirements.

Generated artefacts can introduce dependencies, licence-sensitive copied patterns, hidden assumptions, inefficient code, weak error handling or misleading documentation. It can even generate code that does nothing except take up space and is never called.

Errors in code can be very easy to miss when the output is voluminous and looks idiomatic.

### Quality Practice

Treat generated snippets with caution. Like examples in documentation they can gloss over important details.

Check edge cases, error handling, data assumptions, performance, and dependency choices.
There can in some circumstances be licensing issues around the output. (This depends on your local jurisdiction)

If the code affects analysis results, compare it against known good results from trusted sources, such as hand-worked examples, known datasets, or domain expectations.

Do not accept generated tests that merely reproduce the implementation's assumptions.

Tests should ideally come from domain examples or stated requirements, not from the generated code itself.

Do not treat "the generated tests pass" as evidence that the behaviour is scientifically correct.

### AI Intensity Considerations

Stay at this level when the artefact is small enough to review,
and the conversation is helping you improve it.

Consider lower intensity AI practice when:

* the generated artefact is no longer small enough to review,
* the tool is inventing APIs or assumptions,
* the person interacting with the AI cannot explain the result.

Consider greater intensity AI practice when the task needs selected project context and the files can be shared safely.

A useful rule is to keep generated artefacts smaller than your review capacity.
This can mean that this practice is the sweet spot for your research, which should not be underestimated.


<!-- --------------------------------------------------------- -->


## 3. Conversational Creation with Zip Files (etc)

### Overview

At this position, the tool sees selected project context.

This context is often in the form of zip files, but may be a small group of files,
a minimal reproducible example, a failing test log, a diff, and so on.

This can help with code review, documentation review, test suggestions,
project-structure explanation, or debugging across a few files.

Some chat systems support direct file upload or project knowledge areas.
For example, a user may upload files to ChatGPT or Claude,
or use Claude Projects or similar mechanisms to keep selected material available.

This is more useful than pasting isolated snippets.

The important word here is "selected".
The practice is not "upload the whole project", but choosing the smallest useful context.

### Getting Started

First decide what the tool needs to see.
Select the smallest context that can answer the question.

Ensure you do not include secrets, tokens, private data, unpublished material and irrelevant generated files.

It can be useful to tell the tool what the files are (unless your prompt is "explain this project").
Tell it what kind of answer you want.
Ask it to identify uncertainty.
If you are asking for changes, ask for one change at a time, not to patch everything at once.

Practical ways to provide context include:

* paste one short file or function
* upload a small zip containing only relevant files
* create a minimal reproducible example
* provide a failing test log plus the relevant test file
* provide a `git diff` based patch for a specific change
* include `README.md`, test commands and package metadata where relevant

Avoid uploading the whole repository by default.
Do not include `.git`, `.env`, credentials, private datasets, large generated outputs, notebooks with hidden state, or irrelevant build artefacts.

If you create a zip file, double check what is in it before sharing it.
If you provide a diff, remember that it only shows changes.
It may not include enough surrounding context to judge the change safely.

### Sample Appropriate Practice

Some sample prompts at this stage might look like this:

* "These are the public files for a small research package.
   Please suggest missing tests and documentation gaps.
   Do not rewrite code."

* "This is a minimal failing example.
   Explain why the failure occurs.
   Propose the smallest change that would test the issue."

* "This is a `git diff` for a proposed change.
   Please review it for missing tests, unclear behaviour and documentation gaps.
   Do not suggest unrelated refactoring."

* "These files are from a public package.
   Please list the assumptions you can infer.
   Also list the assumptions you cannot determine from the code."

A more detailed prompt might look like this:

* "I am uploading selected files from a small research package.

   Context:
   - the package is public;
   - the task is documentation and test review;
   - the scientific algorithm should not be changed;
   - new dependencies should be avoided;
   - broad refactoring is out of scope.

   Please return:
   - what you think the package does;
   - missing tests;
   - documentation gaps;
   - assumptions you can infer;
   - assumptions that need a maintainer or domain expert."

### Concerns/Risks

The main risks are context leakage and misplaced confidence.

A tool that has seen more files may sound as though it understands the project.
It will likely still miss scientific intent, historical decisions, domain conventions or institutional constraints.

More context does not always mean a better answer.
It can make the answer more confident.
It can make the answer more diffuse and harder to check.

There may be extra costs.
These can include time, money, review burden and environmental cost.

The tool may focus on software tidiness.
That is not always the same as research correctness.

A suggested refactor may make code look cleaner.
It may obscure why the code was written that way.

### Quality Practice

Keep the workflow staged.

First ask for analysis.
Then ask for possible changes.
Then ask for the changes, and review any proposed patch manually.

Check that every recommendation relates to actual files, stated requirements, or explicit assumptions.

You can ask the tool to separate these categories:

* What it can see in the files
* What it is inferring
* What it cannot know
* What needs maintainer or domain review

Again, before sharing files, check for sensitive data. Sensitive data includes: passwords, tokens, API keys, private URLs, personal data, participant data, unpublished results, embargoed material, private notebook comments, local paths, or generated files that are not needed for the task.

Record material AI assistance where it affects analysis code, dependencies, reproducibility or published outputs.

### AI Intensity Considerations

Stay at this level when selected project context is enough,
and the result still remains small enough to review.

Consider lower intensity AI practice when:

* Context upload creates confidentiality, licensing, provenance or environmental concerns.
* The model becomes more confident than the evidence allows.

Consider greater intensity AI practice when repeatedly describing and editing files becomes the main task, and when the files can be shared safely.

More context can produce better answers. It also increases exposure and the chance of misplaced confidence.


<!-- --------------------------------------------------------- -->


## 4. IDE autocomplete and inline suggestions

### Overview

This is sometimes referred to as "autocorrect on steroids". It has all the benefits this phrasing suggests as well as many of the problems this phrase can imply.

Some editors and IDEs can show AI-generated suggestions while you type.
These may appear as greyed-out completions, suggested lines, function bodies, comments, tests or repeated patterns.
Not every IDE has this feature. Some projects or institutions may disable it.

Common examples include GitHub Copilot in Visual Studio Code and other supported editors, Gemini Code Assist in VS Code and JetBrains IDEs, Cursor, Continue, JetBrains AI Assistant, and editor-specific plugins.
The exact behaviour depends on tool, editor, plan and configuration.

Where available and approved, inline suggestions can be useful for boilerplate, repetitive patterns, simple tests, straightforward docstrings, API usage examples and small local transformations.

They are less suitable for scientific design, security-sensitive logic, numerical methods, or anything where hidden assumptions matter more than syntax.

### Getting Started

Enable the tool only in repositories where its use is allowed.
Start with non-sensitive, low-consequence files such as documentation, tests or small utility modules.
Treat suggestions as typed drafts, not accepted truth.
Reject suggestions that introduce unexplained dependencies, broad behaviour changes or code you cannot explain.

Check what context the tool may use.
Some tools use the current file. Some use open files.
Some use broader workspace or repository context.

This matters if the project contains private code, unpublished work, sensitive data, or material that must not be shared with the tool.

### Sample Appropriate Practice

Suitable uses include:

* Accepting a repeated test case after you have written the first one yourself
* Completing simple argument parsing after the behaviour is already decided
* Drafting a docstring that you then check against the actual code

A poor use is letting autocomplete decide how important behaviour should work.

Examples include missing data, units, thresholds, random seeds, file deletion,
authentication, network access or dependency selection.

Useful practice patterns include:

* Write the test name yourself, then let the tool suggest the body
* Write the function signature and expected behaviour yourself
* Use suggestions for repetitive patterns, not scientific judgement

All of these need checking for correctness. In the same way autocorrect can create problems and misunderstandings this form of auto-correct has similar issues. If you don't understand the generated code, work through or reject the code until you understand how to change it.


### Concerns/Risks

The main risk is passive acceptance.

Because autocomplete appears while you type, it can feel like your own code.
This can create false familiarity.
You can inadvertently accept code without really understanding whether it is correct.

Inline suggestions may introduce dependencies, global state,  network access, random behaviour, inefficient patterns or security-sensitive mistakes.

Because the suggestion is accepted inside the editor, it may not feel like an
external contribution needing review.

That makes it easier for weak code to enter the project quietly.

### Quality Practice

Use autocomplete for typing assistance, not for deciding behaviour.


Be especially careful where the code makes decisions about data, state or side effects.
Some examples may include data parsing, missing values, units, coordinate systems, statistics, and numerical tolerances.
Some may be less reversible like authentication, file deletion, network access and dependency choices.

Run tests frequently. Inspect changes carefully, since tests may not catch accidental behaviour changes.

While all changes need review, take extra care over security-sensitive code. The reason is it's very easy to treat these changes as "what you typed" - but this can sidestep the thinking process.

It is important to turn suggestions off when they distract from learning, debugging or careful reasoning. A reasonable alternative is to switch interaction mode.


### AI Intensity Considerations

Stay at this level when autocomplete is helping, and you can still understand every suggestion you accept.

Consider a lower intensity practice when suggestions start to move faster than your understanding.
This may happen when you are learning, debugging carefully, or trying to reason through unfamiliar code.
In those cases, switch suggestions off or return to conversational interaction.

A reasonable alternative is to switch interaction mode rather than simply accept or reject suggestions.
For example, instead of accepting an inline completion, ask a chat tool to explain the code,
list assumptions, or suggest tests.

Consider a higher intensity practice when inline suggestions are too syntactic or too local.
This may be the case when the task needs extensive multi-line edits,
a change across several files, help with documentation, or understanding of wider project structure.

Do not move up simply because the tool offers a more powerful mode.
Move up only when the task needs it, and when you can still review the result.


<!-- --------------------------------------------------------- -->


## 5. Editor-integrated local assistant

### Overview

Some editor-integrated assistants can make changes to files for you.
They do more than suggest the next line.


At this level, the assistant may edit files, but should not be assumed to control version control.
You should still be using version control yourself.

Some tools can run Git commands. If so, extra care is needed. This moves closer to agentic behaviour, even if the tool appears inside an editor.

Depending on the tool, they may add tests, refactor a function, improve docstrings, update type hints, explain a symbol, or make a small change across related files.

Examples include VS Code with GitHub Copilot Chat, Edits or agent features; Cursor's assistant or agent modes; Codex in an IDE; Continue; Cline; Zoo Code; and JetBrains AI Assistant.

These tools vary: some suggest edits, or apply patches and some can run commands and interact with version contro. This may require extra guardrails.

This is a step up from autocomplete.
The tool may produce a patch: a set of changes you must review.

Use this only when the change is bounded enough to inspect.
You need to compare the old version with the new version.
If you cannot inspect the change, this is the wrong level of intensity.


### Getting Started

Use a fresh branch, or preferably a separate local checkout as described
in the cross-cutting practices.
State the task narrowly.

Ask for a plan before applying changes, if the tool supports that.
Do not start with broad editing - like "clean up this module".

Prefer:

* "add tests for this function"
* "extract this duplicated block without changing behaviour"

If the tool offers modes such as "ask", "plan", "edit", "agent" or "act", start with ask or plan mode.

Using the least powerful mode that works allows you to retain greater control.

After the edit, inspect the diff before committing anything.
If the tool can run commands, inspect the diff before letting it run broad checks.

If you are unfamiliar with branches or diffs, review the relevant RSQKit pages first before using this mode of usage.
Briefly - a branch is a separate line of work; a diff is the list of changes between two versions; reviewing the diff is how you check what the assistant actually changed.

The basic loop is:

* describe the task
* ask for a plan
* approve or correct the plan
* apply a small edit
* inspect the diff
* run checks
* commit only what you understand


### Sample Appropriate Practice

Some sample prompts at this stage might look like this:

* "Add pytest tests for this function.
   Do not change implementation code.
   Include edge cases for empty input and invalid units."

* "Refactor this function to reduce duplication.
   Preserve public behaviour.
   Show the intended changes before editing."

* "Update these docstrings so they match the current function signatures.
   Do not change code behaviour."

* "Suggest a plan for adding type hints to this file.
   Do not edit until I approve the plan."

* "Split this broad refactor into smaller reviewable steps.
   Do not edit files yet.
   Explain what each step is intended to preserve."


### Concerns/Risks

The assistant may change more than you asked for.

This can happen because the tool is working at patch level, not just line level.
These changes can be easy to miss if they are mixed into a larger patch.
Broad prompts such as "clean this up" or "make this better" are risky.
They give the tool room to make design decisions without knowing the research context.

It may rename variables, alter defaults, change numerical tolerances, move code, update documentation inaccurately, alter formatting, or add dependencies.

The main risks are scope creep and semantic drift.
Scope creep means the assistant changes files or behaviour outside the task.
Semantic drift means the code still looks reasonable, but now means something different.
This matters especially in research software.

Generated documentation can become misleading.
It may describe what the assistant thinks the code should do,
rather than what the code actually does.

If the tool can run commands or use Git, there is an additional risk.
It may change files, stage changes, switch branches or alter local state in ways that are not obvious from the conversation.

The concern is not only whether the assistant produced a useful edit.
The concern is whether you can still see, understand and own the change.

Crucially, a patch can look tidy while changing the scientific meaning of the code.

### Quality Practice

Review the change as a patch, not as a conversation.

Use tests before and after the edit.

For refactoring, add or identify behaviour-preserving tests first.
For documentation, check that generated prose describes actual behaviour.
It should not merely describe intended behaviour.

For scientific code, require an example that focusses on the domain, a reference output or reviewer who understands the underlying method.

Before accepting the edit, check:

* what files changed
* whether only expected files changed
* whether behaviour changed
* whether tests were added or updated
* whether defaults, tolerances or dependencies changed
* whether documentation still describes actual behaviour

Watch for small "helpful" changes slipped into a larger edit: renamed variables, changed defaults, altered tolerances or added dependencies.

Use version control deliberately as part of this. Commit small atomic changes where practical.
Consider asking the AI to break broad refactoring into smaller steps to make such changes easier to understand.

Work on a branch or local checkout. If the assistant can run git commands, disable git remotes for the local checkout (see cross cutting practices for detail).

Before committing, consider whether you understand the changes adequately.
You will need to be able to describe not only what changed generally, but what specifically changed and why before doing so. If you can't do this, then you have lost control of the changes.

The commit message and rationale should be owned by a specific person, even if the assistant drafts text.

The important thing is that a person can explain why the change is correct, and how it was checked.


### AI Intensity Considerations

Stay at this level when the assistant is helping with small, local changes that you can review as a single coherent patch.
This is useful for adding tests, updating docstrings, simplifying one function, or making a small change across a few closely related files.

Consider lower intensity AI practices when:

* The assistant is making changes faster than you can review them.
* The work shifts to mainly learning, debugging or understanding.

In those cases, conversational interaction or autocomplete may be more appropriate.

Perhaps consider more intense AI practices when the task depends on wider project structure. This might include call paths, configuration, tests, documentation, packaging, or behaviour spread across several files. This increases intensity because the task needs broader context. This is only useful if you can still review the result In that case, repository-aware assistance may be more useful than local editor edits.

Do not increase intensity simply because the tool offers a more powerful mode - your judgement is more important than speed.
This is especially the case where changes have greater impact on the research.


<!-- --------------------------------------------------------- -->


## 6. Repository-aware assistance

### Overview

At this position, the tool can inspect or search across a repository.

This is different from uploading a zip file or pasting selected context.
The tool may be working inside an editor, a local checkout, a repository service,
or a coding assistant that can see more than the current file.

It can help you find where an option is defined, which tests relate to a feature,
how a command flows through the code, where documentation is out of date,
or where a small change might belong.

Examples include Cursor, GitHub Copilot in VS Code, Codex, Claude Code,
Sourcegraph-style code search assistants, Continue, Cline, Zoo Code and similar tools.

The important feature is that the tool can search, summarise or reason across the repository.

This can be very helpful for orientation, especially in unfamiliar research codebases.

Finding relevant files is not the same as understanding the scientific reason for the code.


### Getting Started

Begin read-only.

Use this practice first to understand the repository, not to change it.

A good first task is to ask the tool to map one thing: a command, a data-processing step, a configuration option,  a failing test,  a documented example, an installation or test workflow.

Ask the tool to cite the files, functions or configuration entries it used.
Then check that those references are real.

For example, ask:

* "Find where this command starts.
   List the files and functions involved.
   Do not edit files."

This is useful because many research projects have implicit structure.
A script may call a package.
A notebook may call a helper module.
A command may depend on configuration.
A test may be checking a convention that is not written down elsewhere.

Consider adding a project instruction file such as `AGENTS.md`,
`.github/copilot-instructions.md`, `CLAUDE.md`, Cursor Rules,
or a tool-specific equivalent.

These files can describe:

* How to install the project, run tests or build documentation
* Style conventions, forbidden actions and domain cautions
* Assumptions that should not be changed

As elsewhere, they guide behaviour - they are not security controls.

This is a good place for support from an RSE.
A small amount of setup can make these tools much more useful: clear test commands, a short project map, known entry points, and a few domain cautions.

### Sample Appropriate Practice

Some sample prompts at this stage might look like this:

* "Find where configuration option X is parsed, validated and used.
   Do not edit files.
   Return the relevant files and a short explanation."

* "Identify tests that should cover this bug.
   If none exist, suggest where a new regression test should go.
   Do not change anything yet."

* "Map how the command `analyse-sample` works in this repository.
   Return the entry point, main files, configuration read, tests involved and uncertainties.
   Do not propose code changes yet."

* "Find where the project assumes input rows are sorted.
   List the files and functions involved.
   Then suggest tests that would fail if this assumption were broken."

* "Review the README and project configuration.
   Tell me how a new contributor would install the project and run the tests.
   Identify anything that is unclear or inconsistent."

### Concerns/Risks

Repository awareness can hide misunderstanding.

The tool may identify real files and functions but still misunderstand their purpose.
It may confuse old code paths with current ones.
It may miss assumptions that are only known to the research group.
It may suggest changes that are tidy from a software perspective, but wrong for the analysis.

Treat repository-aware answers as maps of code/problem-space, not decisions.

The tool can help you orient yourself.
It should not decide scientific meaning, project policy, dependency strategy or release behaviour.

There is a context risk. A repository may contain private code, unpublished work, sensitive paths, credentials, local notes, generated files, or old notebooks with hidden state.

Assume repository-aware tools will see more than you expected.


### Quality Practice

Keep investigation and modification separate.

First ask the tool to map, explain or locate.
Only later ask for a candidate change.

Require file and function references where possible.
Then verify them.

If the tool cannot point to real files, its answer is probably not reliable enough to act on.

Check whether its answer matches the project as it is, not a project it has inferred from common patterns.

Be cautious with dependencies, package metadata, CI, release configuration, data-processing code and numerical thresholds.

For research software, check that any proposed change preserves reproducibility and does not silently change analysis semantics.

If this stage produces useful understanding, capture it.
For example, update documentation, an issue, `AGENTS.md`, or a contributor note.
Do not leave useful repository knowledge trapped only in a chat transcript.


### AI Intensity Considerations

Stay at this level when repository search and explanation are enough.

This is useful when you need orientation, call paths, test locations, configuration details, or documentation gaps.

Consider less intensive AI usage when:

* One file, one snippet, or a short conversation is enough.
* The repository contains material the tool should not see.

Perhaps consider more intensive AI usage when the task genuinely needs edit-run-fix cycles. This usually means the project has tests or checks that can guide the process, and you have a safe local checkout where the tool can act.

Do not use repository awareness as a shortcut around project judgement. It helps navigation.
It does not replace understanding.


<!-- --------------------------------------------------------- -->


## 7. Constrained local tool-using agents

### Overview

This is where the workflow changes substantially.

The tool is no longer only producing text.
It may edit files, run commands, run tests, inspect failures and try again.

Examples include fixing a failing test, updating documentation and running link checks,
applying a formatter, preparing a small patch, or investigating a bug in a disposable checkout.

Examples of local or locally controlled coding agents include Claude Code, Codex CLI,
Aider, Cline, Zoo Code, Gemini CLI and similar terminal or editor agents.

These tools can read files, propose edits, make edits, and in some configurations run commands.

This is the sort of practice many professional non-research software engineers are now being encouraged to adopt.
For research software the question is not simply "can this make changes faster?"
The question is whether the project is ready for this style of work.

That often depends on tests, documentation, reproducible setup, version control practice, and whether someone can review what the agent has done.

Several related mechanisms may appear at this level:

* **Instruction files** such as `AGENTS.md`, `.github/copilot-instructions.md`, `CLAUDE.md`, Cursor Rules or tool-specific files tell agents how to work in a repository.
  They guide behaviour; they are not security controls.

* **Skills**, often represented by folders containing a `SKILL.md`, package task-specific instructions, resources and sometimes scripts.
  They can make an agent more capable for a repeated workflow, but they  need review.

* **MCP servers** connect an AI application to external tools, data sources or workflows.
  MCP can be useful, but every connection is also a permission grant.

For first use, avoid MCP, skills and broad command approval.
Start with a disposable checkout, read-only investigation, and manual approval before edits or commands.

### Getting Started

Use a separate local checkout where practical.
Treat that checkout as the tool's working area, not your main working copy.

Many of these tools, such as Claude Code, have an interactive interface.
This is part conversational and part operational.
Claude Code is mentioned here because it is widely used, can be used with different model backends, and has substantial external guidance available.

When getting started, the interactive interface is worth using.
If the tool offers to create or update a `CLAUDE.md` file, that can be useful initially.
Review that file before relying on it. It is project guidance, not a control.

Gemini, Codex and other tools have similar mechanisms.

Follow the cross-cutting practice: let the agent prepare changes, then pull or copy candidate changes into your own checkout.

Do not give the tool direct push access to a shared repository.
If the tool can run Git commands, remove or disable Git remotes in its checkout.

Start with a narrow task.

A good first local-agent task is not: "fix the project"

A better first task is: "Run the tests, explain the failures, and propose a plan. Do not edit files yet."

Give the agent a list of the following:

* the task
* the allowed files or areas
* the commands it may run
* the commands it must not run
* the checks that define success
* whether it may edit files
* whether it may install dependencies
* whether it may access the network

If the tool supports command approval, use it.
If it supports read-only mode, start there.

A shell command is an instruction run in the terminal.

Some shell commands are harmless, such as listing files.
Others can install packages, overwrite files, delete data, contact external services or change your Git repository.

If you are not sure what a command does, do not approve it.

This is another place where help from an RSE can be valuable.
A friendly setup pass can identify the right test command, create an `AGENTS.md`, prepare a clean checkout, and make the first task much safer.

### Sample Appropriate Practice

Some sample prompts at this stage might look like this:

* "You are working in a disposable checkout.
   Investigate this failing test.
   First explain the likely cause and propose a plan.
   Do not edit files yet."

* "After I approve the plan, make the smallest local change.
   Run only the relevant tests first.
   Do not push, create a PR, install dependencies, or modify CI."
   * Note: enforce these constraints where possible. Do not rely only on the prompt.

* "Prepare a documentation-only patch for the public API described in these files.
   Do not change implementation code.
   Run the documentation checks if available."

* "Run the test suite and report failures.
   Do not edit files yet.
   Group failures by likely cause."

* "Investigate whether this warning is caused by our code or a dependency.
   Do not change dependency versions.
   Do not modify lock files."

A safe local agentic loop is:

* Read-only investigation
* You approve or correct the plan
* Agent edits locally
* Agent runs narrowly scoped checks
* You review the diff
* You run broader checks
* You commit or discard

This preserves the productivity benefit while keeping consequential action with the person responsible for the work.


### Concerns/Risks

The agent may "fix" a failing test by changing the test, weakening the check, removing coverage, altering fixtures, or changing behaviour outside the intended scope.

It may run commands that install packages, alter lock files, download data, call the network, change Git state, or modify files outside the expected area.

Local agents can accumulate hidden state. They may leave generated files, caches, changed environments, temporary data, modified notebooks or altered configuration behind.

Prompt injection matters here.
The agent may read files, logs, issues or documentation that contain misleading instructions.
Once the tool can act, untrusted project content is not just text.
It can influence actions.

For some projects, this practice is best used with a clean copy,
visible command approval, and a supervisor, maintainer or RSE available
if the agent proposes unfamiliar actions.

### Quality Practice

The key discipline is containment.

The agent should not have production credentials, secrets, write access to canonical repositories, or access to sensitive data unless explicitly approved.

Avoid broad shell authority.
Do not allow destructive commands, dependency installation, network access or external service calls by default.

Review **actions** as well as outputs.

Check:

* what files changed, commands run, files created and tests run
* whether lock files, dependencies, notebooks or generated files changed
* whether the agent changed tests to fit the implementation
* whether the final changes still match the original task

Treat test success as evidence of action, **not proof of correctness**.

An agent can make the tests pass by weakening the test, deleting coverage, changing fixtures, altering behaviour, or moving the failure somewhere else.

Keep command output and tool transcripts where practical. They are part of the audit trail for what happened.

**Commit only changes you understand.** The commit message and rationale should be owned by the person accepting the work, even if the agent drafts text.


### AI Intensity Considerations

Stay at this level when a local supervised agent solves a real problem.
This may be useful when the project has a reproducible setup, tests that can guide the work, and a task small enough to review.

Consider lower AI intensity practices when:

* Repository-aware explanation is enough
* The task is mainly learning, debugging or understanding
* The project cannot provide a clean setup
* Tests are weak
* The agent wants unfamiliar commands
* Review takes longer than doing the work directly

Consider higher AI intensity practices when:

* Local supervised work is not enough and isolated parallel work, clean remote environments, or asynchronous execution would solve a real bottleneck.

Do not increase intensity because the tool can do more. Increase intensity only when the project can govern the extra access, cost and review burden.


<!-- --------------------------------------------------------- -->


## 8. Managed or cloud coding agents

### Overview

Managed coding agents run outside your local editor, usually in a hosted or configured environment.
They may clone a repository, work in an isolated branch or worktree, run tests, and prepare a change for review.

This can be useful for routine issues, documentation updates, test additions, small refactors, dependency chores, or parallel investigation of several candidate approaches.

Examples include Codex web/cloud, GitHub Copilot coding agent, Google Jules, Devin, Replit Agent and similar hosted coding agents.

This is different from local editor assistance because the work may happen outside your machine.
This can reduce time to setup, but it also changes the risk.

The repository, configuration, logs and sometimes other project context may be processed by an external or centrally managed service.
This makes remote execution a governance boundary, not just a more convenient development environment.

### Getting Started

For a concrete first example, let's assume a GitHub repository using a GitHub-hosted coding agent such as GitHub Copilot coding agent. There are many other systems that match the concept of managed or cloud coding agents, but this has been chosen to avoid being too abstract.

Good practice would be to have the agent operate on a clone of the repository you want to work with, rather than the main project repository. (In the same way you would have external contributors make local changes and suggest PRs)

Do not start with an important private analysis pipeline. Start with a low-risk repository.

Good first choices include:

* A public test repository
* A fork of a non-sensitive repository
* A private test repository containing no sensitive material
* A small documentation-only project
* A toy package created to evaluate the workflow

Before enabling or assigning the agent, check the repository.

In particular, you should do this on a repository you own.

Additionally you should check whether:

* The code is public or private
* Unpublished research is included
* Sensitive data may be present
* The repository contains secrets or private URLs

Additionally you should check whether the agent can:

* Create branches or pull requests
* Trigger CI
* Use paid or shared compute resources

Lastly, you should confirm your project or institution allows use of AI with this repository in this way.

Add basic project guidance before asking the agent to work.

For GitHub Copilot, this might include repository custom instructions such as
`.github/copilot-instructions.md`. For other systems, this might be an `AGENTS.md` file.

That guidance should include:

* How to install the project
* How to run tests
* How to build documentation
* Hhat files are in scope
* What files are out of scope
* Whether new dependencies are allowed
* Whether pull requests may be created
* What counts as a successful result

If the agent needs extra setup, use the project mechanism for this.
For GitHub Copilot, this may include a `copilot-setup-steps.yml` workflow.

For the first task, use an issue with a narrow goal.

A reasonable first issue might be:

* "Update the tutorial so that it matches the current command-line interface.
   Do not change implementation code.
   Do not add dependencies.
   Run the documentation checks.
   Report what changed, what passed, and what was not checked."

Assign the issue to the coding agent only after the issue is clear.

For the first few runs, prefer tasks where the expected result is easy to inspect:

* Documentation updates
* Additional tests for a public bug
* Broken example fixes
* Simple CI failure diagnosis
* Dependency investigation without applying the upgrade

Avoid tasks involving:

* Private data
* Unpublished results
* Production systems
* Release configuration
* Deployment
* Package publishing
* Authentication
* Scientific algorithm changes
* Clinical, safety-critical or dual-use behaviour

After the agent runs, review the branch or pull request as candidate work.

Checks you should make include:

* Files changed
* Which tests or checks were run, and which if any failed
* What was not checked
* Assumptions that were made
* Whether CI was triggered, and the outcome of this
* What credentials, services or paid resources were used (if any)

Do not treat a branch or pull request as accepted simply because the agent created it.
Promote only work that a responsible person has reviewed, understood and accepted.

Review AI-generated contributions as critically as you would review work from outside the project team.
The issue is not bad intent; it is that plausible, familiar-looking work may still be wrong
In this case, familiarity does not imply correctness.

### Sample Appropriate Practice

Some sample prompts at this stage might look like this. Bear in mind at this stage the examples describe the high level concepts. The examples here are larger and more ambitious that other practices in the spectrum with lower levels of AI intensity usage.
For these to be actually good prompts would require a significant amount of extra good quality context.

* "Add regression tests for this public bug report and prepare a candidate patch."

* "Update this tutorial to match the current command-line interface.
   Run the documentation checks."

* "Investigate whether dependency X can be upgraded.
   Report failing tests and likely breaking changes before editing."

* "Prepare a candidate branch for this documentation issue.
   Do not change implementation code."

### Concerns/Risks

Managed agents can make multiple plausible changes quickly.
That is useful for routine engineering work, but risky for scientific code where correctness depends on domain assumptions.

Require explicit domain review for changes to analysis logic, preprocessing, model evaluation, numerical methods, units, thresholds or data interpretation.

The risk is not only that the agent writes bad code.
It may receive too much repository access, expose private project structure, run in an environment that differs from yours, create branches or pull requests that someone then has to review.

It may use compute or paid resources without clear benefit.

In private or collaborative research, connecting the wrong repository can be a governance problem as well as a software problem.

### Quality Practice

Treat the agent output as candidate work.

Review it as critically as work from outside the project team.
The issue is that plausible, familiar-looking work may still be wrong.

Start from the original task or issue and check that this was done.
Do not let a useful-looking branch redefine the task after the fact.

Ask the agent to summarise:

* What it changed and why
* which tests or checks it ran and what failed
* What it did not verify and what assumptions it made
* What files, services or systems it accessed
* Whether it used paid or shared compute resources

Then confirm this is true - check the branch or pull request yourself.

In particular, check whether:

* Only expected files changed or implementation code changed unexpectedly
* Dependencies or lock files changed or CI, packaging or release files changed
* Documentation matches actual behaviour and tests check the requirement, not just the generated implementation
* Whether scientific assumptions, units, thresholds or data handling changed. The larger the change, the harder this can be.

The key point is to review **actions** as well as outputs. Not just the patch that was produced but also what the agent read, changed, ran, accessed or triggered.

Make sure the environment has no unnecessary secrets.
Avoid giving cloud agents access to sensitive data, private submodules, deployment credentials or broad organisation permissions.

If the agent can create a pull request, consider whether that is desirable.
It may be better for the agent to prepare a branch, patch or report for a responsible person to promote.

A branch prepared by an agent is not an accepted contribution.
A pull request created by an agent is not an accepted contribution.
It is candidate work.

Only promote work that someone responsible for the project understands, accepts, and can explain.


### AI Intensity Considerations

Use this level when remote execution helps, and when the project can still control the result.

Stay at this level when remote or managed execution solves a real project problem.
For example, it may reduce setup problems, run checks in a clean environment,
or allow several candidate approaches to be explored without disrupting local work.

Reasons to consider downgrading AI intensity usage may include:

* When a local editor assistant, repository-aware tool, or separate local checkout is enough.
* When cloud execution exposes private context or increases review burden uses shared resources without clear benefit
* When activity increases without maintainable value.

By contrast you may only want to increase AI intensity levels when the project can govern the extra access it grants. That means clear permissions, contribution rules, review capacity, CI protections, and separation between automation work and team development flow.


<!-- --------------------------------------------------------- -->


## 9. CI/PR/repository agents

### Overview

Here AI becomes part of the shared repository workflow.

This is different from asking a managed coding agent to work on one task. At this level, AI is present in the project process itself.

It may summarise pull requests, comment on proposed changes, suggest review checklists, explain failing CI, triage issues, draft release notes, suggest dependency updates, or create a stream of candidate maintenance work.

This is usually a maintainer or project-team decision. It is not normally an individual researcher decision.

CI means automated checks run by the project. These may include tests, linting, type checking or documentation builds.

A PR, or pull request, is a proposed change submitted for review before it becomes part of the main project. Similar ideas exist in GitLab as merge requests.

Examples include GitHub Copilot pull request summaries or review, GitLab Duo merge request support, Gemini Code Assist pull request review, dependency-update bots, repository automation, and project-specific AI checks.

At this level the question is less: "Can this help one person?"

The question is: "What does this do to the shared project workflow?"

### Getting Started

As with other examples of interaction with a repository, follow the guidance around maintaining a separate repository for automation support from the repository used by team members. Such separation can make it simpler to maintain team development flow while taking advantage of automation benefits.

For a concrete first example, assume a GitHub repository. As before, this is to avoid being abstract and similar techniques will apply to scenarios using GitLab, Jenkins, JFrog Artifactory, etc. (Integration details will differ)

Do not start by allowing AI to create pull requests, merge code, update dependencies across the project, or act on every issue.

Start with low-intrusion support.

For example:

* Enable AI-generated pull request summaries
* Ask for a review checklist on selected pull requests
* Ask for an explanation of a failing CI job
* Use AI to draft release notes for maintainer review
* Use AI to suggest missing tests, without changing code

This keeps the AI close to explanation and review support. It does not give it authority over the project workflow.

Before enabling repository-level automation, decide:

* Who is allowed to enable it
* Which repositories it applies to
* Whether it can comment automatically, create issues or pull requests, trigger CI, access secrets, update dependencies
* How AI-generated activity will be labelled
* Who is expected to review the output (and how)

Start with one repository and one workflow.

A reasonable first trial might be:

* "Use AI to summarise pull requests and suggest reviewer checklists.
   Do not allow AI-created pull requests.
   Do not allow automatic dependency updates.
   Do not allow automatic merge.
   Review whether the summaries help maintainers or add noise."

If the project later enables AI-created issues or pull requests, add stronger
controls:

* Clear labels for AI-generated or AI-assisted activity
* Rate limits
* Branch protection
* Required review by a maintainer or designated reviewer
* Restricted CI permissions
* No access to secrets from untrusted code
* No automatic merge
* No automatic release or publish step

If you are not a maintainer, do not add repository agents, bots or automated pull request tools to a shared project without agreement from the project owner or maintainers.

The aim when getting started is to identify benefits to the project. The risk at this stage is mistaking activity for improved project workflow. Starting small, with separation, makes that easier to evaluate.


### Sample Appropriate Practice

* **Useful project pattern**

Consider an AI staging repository or bot-only staging area.

The canonical repository remains the project-governed space.
An `AGENTS.md` or equivalent instruction file can tell agents not to open PRs directly against the main repository.
Instead, agents prepare candidate patches elsewhere.

Maintainers or designated contributors can review, adapt and promote selected work through the normal contribution process.
This reduces blast radius.
It provides a place to evaluate which AI-generated contributions are actually useful.

* **Low-intrusion starting point**

Use AI to draft a PR summary, suggest a review checklist, or explain a CI failure.
Keep decision, review and merge authority with maintainers or designated reviewers.

### Concerns/Risks

The main risk is maintainer overload.

AI-generated activity can look helpful while consuming attention.
This includes duplicate issues, plausible but low-value PRs, repeated suggestions, noisy review comments, or dependency updates that are technically correct but not useful.

For open-source research software, maintainers are often few and domain context is high.
Attention is a scarce resource.

AI-generated work can bury the conversations that matter:
scientific assumptions, validation, roadmap choices, user needs and domain constraints.

If automation overwhelms or hides those conversations, it is harmful to the project and the individuals working on it.

There is a provenance risk.
If AI-generated work enters the project through ordinary-looking PRs, it may become unclear who owns the change, who checked it, and why it is correct.

### Quality Practice

At this level, quality practice is partly project workflow design.

Configure the repository so that AI activity cannot bypass normal controls.
Use branch protection, required reviews, restricted tokens, secret isolation, dependency review and clear contribution rules.

Make provenance visible.
Label AI-generated or AI-assisted activity where appropriate.
This includes issues, comments, pull requests, dependency updates and staged patches.

Require rationale curated by team members for promoted changes.
This is especially important where scientific methods, dependencies, CI/CD, release configuration or data processing are affected.

Track whether repository AI is actually helping.
Do not only count the number of suggestions, comments or pull requests.

Useful questions include:

* How many suggestions are useful after review?
* How much maintainer time do they consume?
* Do they create quality debt?
* Do they hide or improve project discussion?
* Do they produce duplicate or low-value activity?
* Is the rationale for each change clear? Can its provenance be tied back to a specific issue, requirement, or decision? Are changes small and atomic enough to review?
* Are changes small enough that `git blame` and commit history remain useful when debugging later?

These questions aren't just about governance. They're about being able to identify under time pressure (eg 4am system failure) the key details around the who, what, why, where, when and how of a change without difficulty.

For AI staging repositories, make the obligation clear. Maintainers should not be expected to review everything the machine produces. The staging area is a filter. It is not a second inbox with unmanageable priority.

If automation overwhelms or hides project discussion, treat that as a quality problem. The tool may be producing activity while making the project harder to maintain.

### AI Intensity Considerations

Stay at this level when repository automation provides a clear workflow benefit.
For example, it may help with PR summaries, review checklists, CI diagnosis, release-note drafting, or maintenance triage.
Open-ended autonomy should be justified by need - repository activity is not the same as project progress.

Reasons to decrease AI usage intensity here include:

* When the same benefit can be achieved through other means - such as templates, documentation, CI, scripts, scheduled jobs, or a staged automation workflow.

* When automation causes problems - such as hiding team discussions, increases review burden, weakens provenance, or creates activity without maintainable value.

Use more AI only as a separate governance decision - based on known issues and specific benefits. This may make sense when the project has a clear need for broader automation, a separated automation space, explicit ownership, review capacity, rate limits, restricted permissions, and a way to stop or roll back the workflow.


<!-- --------------------------------------------------------- -->


## 10. Open-ended autonomous agents

### Overview

Open-ended autonomous agents have broad tool access, persistence, scheduling or external integrations.

They may work across repositories, services, terminals, email, cloud resources, issue trackers, documentation sites and CI systems over time.

Examples include broad autonomous software-engineering agents, multi-agent coding environments, scheduled agent workflows, or custom systems built from coding agents plus MCP/tool integrations.

Products in this space may include Devin, Replit Agent, Codex web/cloud workflows, Claude Code used with broad tool access, GitHub Copilot coding agent workflows, and custom systems built around MCP or similar tool protocols.

Remember: product names do not define the level; permissions, context, persistence and authority do.

This is not ordinary coding assistance.
In research software it should be rare, deliberate and governed.

Most researchers should not start here.
Many projects should never need this level of AI intensity.

### Getting Started

It should go without saying: do not start here. Only start here once you have established experience with other areas of the AI intensity usage spectrum.

First establish successful practice with the following:

* clear tasks
* reproducible environments
* tests
* review norms
* least-privilege access
* logging
* rollback
* cost limits
* a clear stop mechanism

Then run a pilot in a sandbox with no sensitive data and no external side effects. When doing so, you will want to define:

* Exactly what the agent may do and what it may **not** do. (you will need to enforce the things it may not do)
* How it stops.
* How actions are logged.
* Who reviews outcomes.

For some projects, this may require agreement from the supervisor, project owner or institutional support team. This is due to the increased levels of risk from a fully autonomous agent.

The first trial should not have: sensitive data, credentials, private repositories, external side effects, production systems. It should have a clear way to forcibly interrupt and stop the agent as a guardrail outside the agent - such as shutting it down.

### Sample Appropriate Practice

Reasonable early tasks include monitoring public documentation for broken links, preparing draft maintenance reports, running non-privileged checks, or generating candidate patches in an isolated staging area.

Inappropriate early tasks include direct deployment, production data changes, sending messages, deleting files or records, changing permissions, publishing packages, modifying release pipelines, or acting on clinical, safety-critical, wrong-recipient, wrong-target or dual-use systems.

A reasonable first pilot should produce information or candidate artefacts.
It should not directly change shared, external or consequential systems.

### Concerns/Risks

Many research environments blur development, analysis and production-like activity.

A notebook may contain real credentials.
A local directory may hold sensitive data.
A script may directly affect published results.

Before giving an autonomous agent access, assume the environment contains more consequential material than expected.
Reduce the blast radius accordingly.

The agent may act faster than a person can supervise.
It may follow misleading instructions from files, logs, webpages or issues.
It may make many small changes whose combined effect is hard to review.

It may perform actions that are not code changes at all:
sending messages, changing settings, deleting files, modifying permissions, publishing artefacts, spending cloud resources or changing external systems.

At this level, the failure may happen before anyone reviews any output.


### Quality Practice

Prompts are not controls. The safe behaviour should be structurally enforced.

This means no production credentials, no secrets, no direct push to canonical repositories, no force-push, no merge, no deploy, no send, no delete, no publish, and no access to sensitive data unless explicitly governed.

Use allowlists, audit logs, approval gates managed by designated people, immutable backups, time limits and cost limits.

Review both outputs and actions.
The risk is not only bad code.
The risk is unsafe action.

Do not rely on the agent promising to ask first. Use permissions, environment design and workflow gates to make unsafe actions impossible or difficult.

### AI Intensity Considerations

Stay at this level only when there is a clear governed need for broad autonomy.
The project must be able to observe, limit, stop and audit the system.

Use less AI, or remove agent authority, if the agent produces broad diffs, cannot explain its changes, repeatedly changes tests to fit implementation, requires excessive review time, follows instructions from untrusted content, or acts outside the task boundary.

At this level, the right response is often not a better prompt.
It is less authority, less context, fewer tools, stronger permissions, or no AI for that task.


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


