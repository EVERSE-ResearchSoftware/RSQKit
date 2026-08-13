---
title: "Open-ended autonomous agents (intensity 10)"
description: Practice Overview for Open-ended autonomous agents
contributors: [ "Michael Sparks" ]
page_id: open_ended_autonomous_agents
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 1010
---
![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-011.png)
<p style='text-align: right;'>
<a href="ci_pr_repository_agents">prev</a>
<a href="spectrum_of_intensity_of_ai_usage">spectrum</a>
</p>

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
