---
title: "Conversational Interaction (intensity 1)"
description: Practice Overview for Conversational Interaction
contributors: [ "Michael Sparks" ]
page_id: conversational_interaction
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 1001
---
![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-002.png)
<p style='text-align: right;'>
<a href="no_genai_usage">prev</a>
<a href="spectrum_of_intensity_of_ai_usage">spectrum</a>
<a href="conversational_artefact_creation">next</a>
</p>

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


