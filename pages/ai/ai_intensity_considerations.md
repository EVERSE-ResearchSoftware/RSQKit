---
title: "AI Intensity Considerations"
description: Making good choices on AI intensity decisions
contributors: [ "Michael Sparks", "Caterina Doglioni" ]
page_id: ai_intensity_considerations
keywords: ["AI", "sustainability" ]
order: 40
---

![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

## Introduction

The purpose of the AI Spectrum is to allow you to make a conscious decision as to when to use a more or less AI intense practice.
There are many reasons for or against using different levels of intensity - or even using AI at all. Always start from the work, not the tool. You may also have local policies recommending the least level of AI intensity due to ethical or environmental concerns.

Different AI practices provide different amounts of context, capability and autonomy. More intensive AI use is not inherently better. The appropriate level depends on the task, the available review capacity, the sensitivity of the material, and the degree of access or authority that can safely be granted.

This page describes considerations for deciding whether to stay with a particular practice, move towards a less intensive practice, or make use of a more intensive one. These are not maturity levels or steps that projects are expected to progress through. For some tasks, conversational interaction may be the most appropriate practice; for others, repository-aware or agentic approaches may provide useful benefits. In some cases, not using generative AI at all will be the right choice.

## 0 - No Gen-AI Usage

Work undertaken without generative AI assistance. This is included, not just because it's the default but because it can be necessary due the nature of the task. Reasons include: learning or assessment goals, restrictions on sharing information, limited review capacity, or wider ethical and environmental considerations. It also applies to projects that have not agreed a policy.

This level is particularly suitable when:

* The purpose is learning or assessment
* Data or code cannot be shared safely
* Review capacity is limited
* Environmental or ethical concerns outweigh likely benefit
* The project has not agreed how AI-assisted work should be handled

If these criteria don't apply, it may be appropriate to consider a different level, if there are benefits in doing so.


## 1 - Conversational Interaction

Conversations asking for explanations, background, design trade-offs, unfamiliar errors and conceptual help. Examples: "Explain this compiler error", "What should I test?", "What assumptions does this numerical method make?", "What misunderstandings might the average developer have based on this code?" (for sanity checking API design)

Stay at this level when conversation is helping you understand the problem.

Consider greater AI intensity practice when the explanation has clarified a small artefact that would be useful and easy to review. For example, this might be a test skeleton, documentation draft or small example.

Consider dropping AI when the conversation starts replacing reading, debugging, testing or domain understanding.
Conversational use should build understanding - not bypass it.

## 2 - Conversational artefact creation

This is chat-based creation of small, reviewable outputs. Examples: a helper function, a test skeleton, a README paragraph, a regular expression, or a command-line usage example.

Stay at this level when the artefact is small enough to review,
and the conversation is helping you improve it.

Consider lower intensity AI practice when:

* the generated artefact is no longer small enough to review,
* the tool is inventing APIs or assumptions,
* the person interacting with the AI cannot explain the result.

Consider greater intensity AI practice when the task needs selected project context and the files can be shared safely.

A useful rule is to keep generated artefacts smaller than your review capacity.
This can mean that this practice is the sweet spot for your research, which should not be underestimated.

## 3 - Conversational Creation with Zip Files

This builds on the previous level by providing selected files, snippets, logs or zip files so the tool can reason about the content. Examples: "Suggest tests for these files", "Review this small package structure", "Explain why this minimal example fails."

Stay at this level when selected project context is enough,
and the result still remains small enough to review.

Consider lower intensity AI practice when:

* Context upload creates confidentiality, licensing, provenance or environmental concerns.
* The model becomes more confident than the evidence allows.

Consider greater intensity AI practice when repeatedly describing and editing files becomes the main task, and when the files can be shared safely.

More context can produce better answers. It also increases exposure and the chance of misplaced confidence.

## 4 - IDE autocomplete and inline suggestions

This is the first step outside the browser into a local tool. AI suggestions appear while editing the current file. Examples: completing boilerplate, filling repetitive test cases, suggesting docstrings or small local code patterns.

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

## 5 - Editor-integrated local assistant

The assistant can make more substantial edits - changes rather than suggestions - inside the editor. Examples: refactor a function, add type hints, generate tests for a module, update these docstrings.

Stay at this level when the assistant is helping with small, local changes that you can review as a single coherent patch.
This is useful for adding tests, updating docstrings, simplifying one function, or making a small change across a few closely related files.

Consider lower intensity AI practices when:

* The assistant is making changes faster than you can review them.
* The work shifts to mainly learning, debugging or understanding.

In those cases, conversational interaction or autocomplete may be more appropriate.

Perhaps consider more intense AI practices when the task depends on wider project structure. This might include call paths, configuration, tests, documentation, packaging, or behaviour spread across several files. This increases intensity because the task needs broader context. This is only useful if you can still review the result. In that case, repository-aware assistance may be more useful than local editor edits.

Do not increase intensity simply because the tool offers a more powerful mode - your judgement is more important than speed.
This is especially the case where changes have greater impact on the research.


## 6 - Repository-aware assistance

At this level of intensity, the AI tooling reasons across a whole project - which may be small or large. The tool can search and reason across the repository. Examples: trace where a setting is used, identify tests for a feature, propose where to add a new option.

Stay at this level when repository search and explanation are enough.

This is useful when you need orientation, call paths, test locations, configuration details, or documentation gaps.

Consider less intensive AI usage when:

* One file, one snippet, or a short conversation is enough.
* The repository contains material the tool should not see.

Perhaps consider more intensive AI usage when the task genuinely needs edit-run-fix cycles. This usually means the project has tests or checks that can guide the process, and you have a safe local checkout where the tool can act.

Do not use repository awareness as a shortcut around project judgement. It helps navigation.
It does not replace understanding.

## 7 - Constrained local tool-using agents

At this level this is where the local tool goes beyond repository analysis, but is an agent that can edit files, run commands and loop locally under supervision. Examples: fix a failing test on a disposable checkout, run linting, prepare a patch without pushing.

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

## 8 - Managed or cloud coding agents

This is where the agents have access to your network services of some kind. The most basic level is access to your github account, but may be a remote hosted agent runner. A hosted or managed agent works in a configured environment, often asynchronously. Examples: ask a cloud coding agent to implement a small issue, run tests, and prepare a branch or PR for review.

Use this level when remote execution helps, and when the project can still control the result.

Stay at this level when remote or managed execution solves a real project problem.
For example, it may reduce setup problems, run checks in a clean environment,
or allow several candidate approaches to be explored without disrupting local work.

Reasons to consider downgrading AI intensity usage may include:

* When a local editor assistant, repository-aware tool, or separate local checkout is enough.
* When cloud execution exposes private context or increases review burden uses shared resources without clear benefit
* When activity increases without maintainable value.

By contrast you may only want to increase AI intensity levels when the project can govern the extra access it grants. That means clear permissions, contribution rules, review capacity, CI protections, and separation between automation work and team development flow.


## 9 - CI/PR/repository agents

Agents are integrated into shared project workflows. Examples: review PRs, suggest CI fixes, triage issues, draft dependency updates, or maintain an AI staging repository.

Stay at this level when repository automation provides a clear workflow benefit.
For example, it may help with PR summaries, review checklists, CI diagnosis, release-note drafting, or maintenance triage.
Open-ended autonomy should be justified by need - repository activity is not the same as project progress.

Reasons to decrease AI usage intensity here include:

* When the same benefit can be achieved through other means - such as templates, documentation, CI, scripts, scheduled jobs, or a staged automation workflow.

* When automation causes problems - such as hiding team discussions, increases review burden, weakens provenance, or creates activity without maintainable value.

Use more AI only as a separate governance decision - based on known issues and specific benefits. This may make sense when the project has a clear need for broader automation, a separated automation space, explicit ownership, review capacity, rate limits, restricted permissions, and a way to stop or roll back the workflow.

## 10 - Open-ended autonomous agents

Broad tool-using systems with persistence, scheduling or external integrations. Examples: agents that can act across repositories, services, email, cloud resources or multiple tools over time.

A hypothethical concrete example: you could create an agent to track new releases and security issue reports (CVEs) for tools and libraries you use. You can set such an agent to keep your code / libraries up to date and working with new release updates. PRs for such changes can be pushed for you.

Stay at this level only when there is a clear governed need for broad autonomy.
The project must be able to observe, limit, stop and audit the system.

Use less AI, or remove agent authority, if the agent produces broad diffs, cannot explain its changes, repeatedly changes tests to fit implementation, requires excessive review time, follows instructions from untrusted content, or acts outside the task boundary.

At this level, the right response is often not a better prompt.
It is less authority, less context, fewer tools, stronger permissions, or no AI for that task.

## Summary

Choose the AI practice that fits the task rather than the most capable tool available.

Greater intensity can provide broader context, more automation and greater ability to act, but it can also increase exposure, resource use, review burden and the consequences of mistakes. Higher intensity also increased environmental costs, as a reasonable policy **may** be ***"use the lowest intensity you can justify"***.

Move towards greater intensity when it solves a real problem and the additional context, access and authority can be governed safely. Move towards lower intensity when a simpler practice provides the same benefit, when understanding or review cannot keep pace, or when the additional access and automation are not justified.

The appropriate point on the spectrum may vary between tasks within the same project. Moving down the spectrum, switching interaction mode, or choosing not to use generative AI are all legitimate engineering decisions.



