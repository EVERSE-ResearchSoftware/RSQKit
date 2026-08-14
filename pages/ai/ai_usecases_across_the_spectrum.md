---
title: "Usecases across the spectrum"
description: How real world tasks map to the Spectrum Intensity
contributors: [ "Michael Sparks", "Hugo Bacard" ]
page_id: ai_usecases_across_the_spectrum
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 15
---

![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-000.png)

# Use cases across the AI spectrum

## Introduction

Start with what you are trying to achieve, then choose the least intensive AI practice that helps you achieve it while preserving research correctness, guardrails, rollback and reproducibility.

The same task can be approached in several different ways across the AI spectrum. A [short conversation][CHAT] can clarify a problem; [selected files][CHAT_ZIPS] provide useful context; [repository-aware assistance][REPO_AGENT] helps when the work spans a project; an agent earns its place where [running tools and iterating][AUTO_AGENTS] actually saves effort.

The examples below therefore start from common kinds of research-software work rather than from particular AI tools or levels of intensity. For each, the aim is to show a sensible place to begin, what justifies moving towards a more intensive practice, and where increasing intensity is unlikely to help.

## 1 Plan, specify or design something

Before writing software, you need to understand what the research requires, decide what the software should do, identify constraints, or choose an appropriate design. This includes gathering requirements, thinking through architecture, selecting tools or infrastructure, and deciding how research and software concerns fit together.

### Worked example: designing a small piece of research software

Begin with **[Conversational Interaction][CHAT]**. Describe the research problem, what the software needs to support, the people who will use or maintain it, and any known constraints. Ask the AI to identify assumptions, missing requirements, alternative designs and trade-offs rather than immediately asking it to produce code.

If the design depends on existing material, **[Conversational Creation with Zip Files][CHAT_ZIPS]** can provide selected documents, interfaces, example data or relevant files as context. If the new component must fit into an existing project, **[Repository-aware assistance][REPO_AGENT]** helps trace interfaces, dependencies and conventions before proposing where the new work should live.

Don't reach for more AI intensity just to turn an uncertain design into implementation faster. If the research requirements or design choices are still unclear, more automation won't resolve that. Return to the people who understand the research or software constraints.

## 2 Understand, investigate or evaluate something

Sometimes the work is primarily about understanding: an unfamiliar codebase, an unexpected result, an error, a scientific assumption, or the behaviour of software in relation to the research question. This includes debugging, evaluating existing software, tracing behaviour through a project, or understanding feedback from users and collaborators.

### Worked example: diagnosing a failing analysis or test

Use **[Conversational Interaction][CHAT]** to explain the failure and explore likely causes. Ask for hypotheses, missing information and useful checks rather than a fix. This keeps the early work focused on understanding the problem.

Move to **[Conversational Creation with Zip Files][CHAT_ZIPS]** when the failing example, logs or relevant files provide necessary evidence. If the behaviour spans several parts of the project, **[Repository-aware assistance][REPO_AGENT]** can help locate relevant tests, call paths, configuration and assumptions. **[Constrained local tool-using agents][LOCAL_AGENTS]** become useful once the next step is to run tests or experiments repeatedly while investigating the cause.

If the AI starts making changes before the failure is understood, or changes tests to match the implementation, reduce the intensity. The purpose of debugging isn't to make the error disappear.

## 3 Create or modify software

This covers implementing new behaviour, making local changes, refactoring existing code, or modifying software to support a research need. The appropriate level of AI assistance depends heavily on how large the change is, how much project context matters, and how easily the result can be reviewed.

### Worked example: adding a small feature

If the change is small, **[Conversational artefact creation][CHAT_OUTPUT]**, **[IDE autocomplete and inline suggestions][IDE_COMPLETE]**, or an **[Editor-integrated local assistant][EDITOR_AGENT]** is usually enough. Define the intended behaviour yourself, including important inputs, outputs and constraints, and ask for a small reviewable change rather than an open-ended implementation.

If the feature depends on behaviour spread across several files, **[Repository-aware assistance][REPO_AGENT]** helps identify where the change belongs and which tests or documentation are affected. A **[Constrained local tool-using agent][LOCAL_AGENTS]** becomes useful when implementing the feature naturally requires a short edit-run-test cycle.

If review becomes harder than making the change directly, or the agent starts altering unrelated code, reduce the intensity. Increased capability shouldn't substitute for a clear specification or human judgement.

## 4 Check correctness and quality

Research software quality includes more than whether tests pass. The software must behave correctly for the research, respect scientific and numerical constraints, remain understandable and reproducible, and fail in ways that do not silently invalidate results.

### Worked example: testing software against scientific constraints

Begin by identifying the properties that should always hold. These can include ordinary software behaviour, but also scientific invariants. A state that cannot physically return once exhausted shouldn't "come back to life". The energy in a closed system shouldn't exceed the level the model permits. Probabilities for mutually exclusive alternatives shouldn't sum to more than one.

Tests can also capture numerical behaviour. For example, an implementation might need explicit bounds on error, or calculations performed in log space to avoid underflow or loss of useful precision. **[Conversational Interaction][CHAT]** is useful here for asking what properties, edge cases and failure modes should be tested before asking the AI to write test code.

**[Conversational Creation with Zip Files][CHAT_ZIPS]** can help relate these constraints to selected implementation files, while **[Repository-aware assistance][REPO_AGENT]** can identify where assumptions enter the software and which existing tests exercise them. An **[Editor-integrated local assistant][EDITOR_AGENT]** or **[Constrained local tool-using agent][LOCAL_AGENTS]** can then help implement tests, run them, investigate failures and prepare small candidate fixes.

Passing the generated test suite isn't evidence that the science is correct. Reduce the intensity if the AI begins inventing scientific constraints, or weakens tests to match the implementation. Scientific correctness must remain anchored in the research rather than in the behaviour of the current code.

## 5 Document, package, release or publish

Once software is taking shape, it needs to be understandable, usable and shareable. That can include writing READMEs and documentation, adding metadata such as CodeMeta, packaging the software appropriately, and giving it a persistent identifier. Depending on the project, the work is then released, deployed, archived or published.

### Worked example: packaging software

If you already understand how the software should be packaged, **[Conversational artefact creation][CHAT_OUTPUT]** is usually enough to draft packaging metadata or configuration. If you are less familiar with the packaging system, start instead with **[Conversational Interaction][CHAT]**: ask what the relevant files mean, what information is required, and what assumptions the proposed configuration makes.

Use **[Conversational Creation with Zip Files][CHAT_ZIPS]** when package layout, dependencies or entry points matter. **[Repository-aware assistance][REPO_AGENT]** becomes useful when packaging depends on relationships across source layout, tests, documentation, build configuration and existing automation. A **[Constrained local tool-using agent][LOCAL_AGENTS]** helps once the task becomes building the package, running checks, inspecting failures and making small corrections.

Packaging a library rarely requires broad autonomy. If the tool wants to alter unrelated dependencies or release processes just to make the package build, reduce the intensity and review the underlying problem.

## 6 Preserve or reproduce work

Research software often needs to remain usable after the original development environment has changed. Reproducible environments, containers, provenance records, software and research artefact archiving, and persistent metadata all help other people — and your future self — reconstruct what was run and why.

### Worked example: creating a reproducible software environment

Begin by documenting the environment that is actually required: runtime versions, dependencies, operating-system assumptions, external tools, input data and any configuration needed to reproduce the work. **[Conversational Interaction][CHAT]** can help identify missing information and distinguish essential dependencies from incidental details of the developer's machine.

**[Conversational Creation with Zip Files][CHAT_ZIPS]** can use selected environment files, lock files, container definitions or CI configuration as evidence for suggesting improvements. **[Repository-aware assistance][REPO_AGENT]** helps discover undeclared dependencies or setup steps scattered through documentation and scripts. A **[Constrained local tool-using agent][LOCAL_AGENTS]** is useful for building the environment in a clean checkout and reporting what fails.

Reproducibility is not improved by automatically updating everything to the newest version or by silently replacing missing components. If the resulting environment no longer reproduces the conditions under which the research result was obtained, the automation has solved the wrong problem.

## 7 Maintain software and respond to change

Software changes after release. Dependencies evolve, platforms disappear, bugs are reported, users discover unexpected behaviour and research requirements change. Maintenance is therefore partly about making changes and partly about deciding which changes are actually justified.

### Worked example: updating a dependency after a breaking release

Begin with **[Conversational Interaction][CHAT]** or **[Repository-aware assistance][REPO_AGENT]** to investigate what changed in the dependency, which parts of the software are affected, and what tests or compatibility checks would provide useful evidence. Repository-aware assistance is particularly useful when the dependency is used in several places or when assumptions about it are distributed across the project.

A **[Constrained local tool-using agent][LOCAL_AGENTS]** can then try the new dependency in an isolated checkout, run the relevant tests and prepare a candidate patch. **[Managed or cloud coding agents][CLOUD_AGENTS]** help when clean environments, multiple versions or platform combinations are useful to the investigation.

Watch for maintenance turning into automatic churn. If an update has no clear benefit, or introduces unexplained behavioural changes, keeping the existing dependency is often the better choice.

## 8 Automate repeated or ongoing work

Some work is valuable precisely because it happens repeatedly: running tests, building documentation, checking multiple configurations, preparing releases, monitoring dependencies or performing routine maintenance. Automation can range from ordinary CI scripts through repository-integrated agents to persistent systems that act when external conditions change.

### Worked example: automating tests with CI

Begin with conventional automation. Define the tests that matter, make them reproducible locally, and then configure CI to run them consistently. **[Conversational Interaction][CHAT]** or **[Conversational artefact creation][CHAT_OUTPUT]** can help explain CI configuration or draft a workflow, but the underlying commands should remain understandable and runnable without the AI.

**[Repository-aware assistance][REPO_AGENT]** can help understand an existing CI setup or identify duplicated and missing checks. **[CI/PR/repository agents][CI_REPO_AGENTS]** become useful for diagnosing failures, summarising results, maintaining complex testing matrices or preparing candidate fixes.

For recurring maintenance, **[Open-ended autonomous agents][AUTO_AGENTS]** are appropriate where the useful behaviour is to monitor an external condition and initiate work when it changes. For example, an agent or small collection of agents might monitor dependency releases and CVEs, determine whether a project is affected, test a candidate update, and prepare a PR for review.

Reserve agents for problems ordinary scripts, CI or scheduled jobs don't already solve. If automation starts producing repository activity without useful outcomes, or obscures ownership, simplify it.

## 9 Hone the skills needed to evaluate AI-assisted work

Using AI well depends on being able to judge what it produces. That judgement does not appear automatically as AI intensity increases: developers still need to understand code, tests, architecture, scientific constraints, debugging, review and project context well enough to recognise when an answer is plausible, incomplete or simply wrong.

Bluntly: Manual practice is part of the evaluation infrastructure for AI-assisted practice.

Practising those skills manually is therefore not just a fallback for situations where AI cannot be used; it is part of maintaining the ability to use higher-intensity AI responsibly.

### Worked example: practising the manual equivalent of a higher-intensity task

For a task you would normally perform with [Repository-aware assistance][REPO_AGENT] or a [Constrained local tool-using agent][LOCAL_AGENTS], deliberately perform an equivalent piece of work using [No Gen-AI Usage][NOGENAI]. Trace the relevant code yourself, identify the tests, form a hypothesis, make the change and evaluate the result. The aim is not to prove that manual work is superior, but to keep the skills needed to assess whether an AI-assisted version of the same process is sound.

As tasks become larger, evaluation also needs to evolve. Reading every generated line is practical for a small artefact, but it doesn't scale to repository-wide or agentic work. At higher intensities, evaluation relies more on independently derived tests, invariants, reproducible checks, targeted review and even adversarial agents that look for weaknesses in another agent's implementation or evaluation. Those techniques reduce some of the review burden, but they still depend on people having enough expertise to design the checks and recognise weak evidence.

Higher-intensity evaluation mechanisms aren't a substitute for maintaining the underlying skills. If you can no longer confidently perform or reason about a representative lower-intensity version of the work, it's hard to tell whether the automation is actually helping or just looking like it.

## Summary

Different kinds of work justify different forms of AI assistance, and the right choice changes as the work progresses. A task can begin as **[Conversational Interaction][CHAT]**, move temporarily into **[Repository-aware assistance][REPO_AGENT]** or agentic work, and return to a lower-intensity practice when understanding or judgement becomes the important part again.

Start from the work rather than the tool. Increase intensity when additional context, editing capability or automation solves a real problem, and reduce it when the same result can be achieved more simply or when review and understanding can no longer keep pace.

Whatever level you use, preserve the things that matter most: research correctness, effective guardrails, the ability to roll back changes, and reproducibility. And remember that **manual practice is the core skill for evaluating  AI-assisted practice** : maintaining the skills needed to understand, test and challenge the work is what makes higher-intensity assistance usable responsibly.


[NOGENAI]: practices/no_genai_usage.md
[CHAT]: practices/conversational_interaction.md
[CHAT_OUTPUT]: practices/conversational_artefact_creation.md
[CHAT_ZIPS]: practices/conversational_creation_with_zip_files_etc.md
[IDE_COMPLETE]: practices/ide_autocomplete_and_inline_suggestions.md
[EDITOR_AGENT]: practices/editor_integrated_local_assistant.md
[REPO_AGENT]: practices/repository_aware_assistance.md
[LOCAL_AGENTS]: practices/constrained_local_tool_using_agents.md
[CLOUD_AGENTS]: practices/managed_or_cloud_coding_agents.md
[CI_REPO_AGENTS]: practices/ci_pr_repository_agents.md
[AUTO_AGENTS]: practices/open_ended_autonomous_agents.md
