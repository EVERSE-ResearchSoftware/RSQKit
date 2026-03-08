---
title: Writing a Research Software Story
description: Capturing the context, community, and practices around a research software project.
contributors: ["Michael Sparks"]
page_id: writing_research_software_story
related_pages:
  tasks: [software_documentation, documenting_software_project, citing_software]
quality_indicators: [software_has_documentation]
keywords: ["research software", "software sustainability", "research software stories"]
---

## Task

### Description

Research software projects often accumulate a great deal of knowledge that is never written down.
The reasons a tool exists, the assumptions behind its design, how the community around it works, and the practices used to develop and maintain it frequently live in people's heads, issue trackers, or scattered conversations.

Capturing that context is surprisingly difficult.

A **Research Software Story** is a structured way to capture that context.

Rather than describing how to run or modify the software, a Research Software Story explains the role the software plays in research.
It captures the scientific problem it addresses, the community that builds and uses it, and the practices and tools that support it.

In effect, a Research Software Story records the *who, what, why, where, when, and how* of a project from a research software perspective.
The result is a concise narrative that helps others understand not only what the software does, but why it exists and how it fits within a wider research ecosystem.

Within RSQKit, Research Software Stories serve a simple purpose: **to share what works in practice**.
They make existing projects visible as examples of real research software development, including both strengths and areas where improvement may be possible.

Writing one is often surprisingly introspective.
The process encourages teams to reflect on how their software is developed, used, and sustained.

### Considerations

A Research Software Story is not technical documentation.
Documentation explains how to install or use a tool; a story explains the context around it.

Because of this, the emphasis is on clarity rather than technical depth.
A reader should be able to understand the purpose of the project, the community around it, and the practices that support it without needing to study the source code or read additional documentation.
(though both are good to do)

The audience for these stories is intentionally broad.
Researchers, early-career contributors, research software engineers, and project coordinators may all rely on them to gain a quick understanding of a project.
Funders and evaluators can also use them to understand the impact and sustainability of research software.

The goal is therefore not completeness, but usefulness.
A Research Software Story should capture what is true now, even if parts of the project are still evolving.

### Why write a Research Software Story?

Research Software Stories are useful because they help the real people who depend on a project:
the people who join it, maintain it, evaluate it, and rely on it for research.

Several groups benefit directly.

For **new users or developers,** a Research Software Story provides orientation.
Many research codebases evolve over time and contain layers of decisions, assumptions, and conventions that are not immediately visible in the code.
A short narrative describing the purpose of the software, its scope, and the community around it helps new contributors build a conceptual model before diving into implementation details.
This can significantly reduce the time needed to onboard to a project.

For **project leaders and coordinators,** a Research Software Story provides a clear way to explain the project to others.
It becomes useful when writing grant proposals, preparing reports, describing the project to collaborators, or explaining its value to institutional stakeholders.
Because the story captures the problem the software addresses and the community that depends on it, it provides a ready explanation of why the software matters.

For **funders, reviewers, and evaluators,** the story helps establish credibility.
These audiences rarely examine the code directly, but they do need to understand the purpose of the software, who uses it, and how sustainable the project is likely to be.
A Research Software Story makes that information visible in a structured way, making it easier to demonstrate feasibility, impact, and community relevance.

There is also a less obvious benefit that often turns out to be one of the most valuable.
**The act of writing a Research Software Story encourages teams to examine their own project more closely.**
When describing workflows, practices, and dependencies, teams frequently discover gaps or opportunities for improvement.
Missing documentation, fragile assumptions, unclear ownership, or absent development practices often become visible during the process.

In this sense, writing the story is not only an exercise in communication but also an exercise in reflection.
It can highlight where additional RSQKit tasks might be useful and help teams think about how their software could be made more sustainable over time.

### Solutions

Research Software Stories in RSQKit follow a template designed to capture the main aspects of a research software project.

These include:

* the **problem** the software addresses
* the **communities** that develop and uses it
* the **technical nature** of the system
* the **libraries and external systems** it depends on
* the **development practices** used by the team
* how **users and contributors are onboarded**
* the **tools and infrastructure** supporting development
* **documentation, FAIR and openness**
* **sustainability and governance**

Each section provides a different perspective on the project.
Taken together, they form a short narrative describing how the software functions within its research environment.

When writing a story it is usually best to begin simply.
Two or three sentences per section is enough to produce a useful first draft.
Additional detail can then be added where helpful.

### Producing a first draft

Several practical approaches can help produce an initial version.

The most obvious, straightforward method is to work directly through the template and write a short description for each section.
This works well when the author already has a clear understanding of the project and the structure of a Research Software Story.
It is often the hardest approach in practice.

The most satisfying and productive approach is often for two developers or researchers to work together.
In this situation, one of them takes the role of an interviewer, and the other answers as the interviee who knows about the project.
The interviewer then uses the template as a means of structuring an interview/conversation, while recording and transcribing the conversation.
A really useful technique here is to repeat back the gist of the interviewee's answers and say "did we miss anything?".
Often the answer is "yes" leading to more Q&A notes.

This interview technique can be fairly brief and use common tools like Zoom, MS Teams or more dedicated tooling.
By asking questions based on the template and transcribing the responses, it is often possible to produce a surprisingly complete first draft.
This interview-based approach can capture language and explanations that might otherwise be difficult to reconstruct later.

Lastly, sitting somewhere between the two, is a structured prompting approach.
This uses a language language model (eg ChatGPT) in the role of interviewer.
Using a system prompt it's possible to flip the interaction from you asking the model questions to it asking you questions.
The system prompt can also be instructed to request supporting material such as README files, previous notes, or transcripts.
It can then be instructed to focus on gaps in the information and probe for additional detail.
The model asks questions corresponding to each section of the template, repeats it back and again asks "is there anything else?"

Once all the sections have been answered, the model can assemble the responses into a draft narrative.
The aim is not to write the story automatically, but to help capture the relevant knowledge in a structured form.
Indeed, the default example prompt explicitly requires the model to prefer the interviee's text over paraphrasing, and is explicitly told not to fill in any gaps.
This can often give a good high quality draft as well.

In practice the most important step is simply producing a **version-zero draft**.
Once the core information has been captured, editing and refinement become much easier.

Often three things need refinement:

* Are the processes actually used by the project captured clearly enough for others to learn from them?

* Are we linking to all the key tools used in the project?
  Not every tool used, just the key/most important ones.

* Are links to documentation, code, tutorials, or videos included and working?
  Are they sufficient?
  In a project with lots of documentation/etc, pointing at the key starting points can make all the difference.

In this way Research Software Stories act as practical examples of how research software is developed and sustained in real projects.

A collection of example Research Software Stories is available within RSQKit and can provide useful reference points when writing a new one.

### Further guidance and examples

The approach described here was originally developed as part of an EVERSE training seminar on Research Software Stories.
The seminar walks through the motivation, the structure of the template, and a live guided writing session showing how a story can be created from an interview.

The full seminar recording is available here:

* EVERSE seminar: *Research Software Stories*
  <https://www.youtube.com/watch?v=enx7sBsaQws>

The recording is fairly long, but it is structured as a series of shorter segments:

* Introduction — what research software stories are and where they came from
  <https://www.youtube.com/watch?v=enx7sBsaQws&t=145s>

* What a Research Software Story contains
  <https://www.youtube.com/watch?v=enx7sBsaQws&t=913s>

* Why writing one is useful
  <https://www.youtube.com/watch?v=enx7sBsaQws&t=1662s>

* Walkthrough of the template
  <https://youtu.be/enx7sBsaQws?t=2687>

The seminar also demonstrates the guided writing approach described above, including recording an interview, transcribing it, and producing an initial "version-zero" story:

* Guided writing overview
  <https://youtu.be/enx7sBsaQws?t=4096>

* Interview demonstration
  <https://youtu.be/enx7sBsaQws?t=4345>

* Transcription and assembly of the first draft
  <https://www.youtube.com/watch?v=enx7sBsaQws&t=6295s>

The notes and supporting material used in the seminar are available here:

* Seminar summary and handout
  <https://github.com/sparkslabs/EVERSE-Seminar-Nov2025-ResearchSoftwareStories/blob/main/Session_Summary_Handout.pdf>

* Detailed seminar notes
  <https://github.com/sparkslabs/EVERSE-Seminar-Nov2025-ResearchSoftwareStories/tree/main/DetailedNotes>

Tools for a sample guided prompting approach are also available:

* Prompt tools for guided story creation
  <https://github.com/sparkslabs/EVERSE-Seminar-Nov2025-ResearchSoftwareStories/tree/main/GPT-PromptTools>

Lastly, an example Research Software Story created using this approach can be found here:

* GreenPhysECS research software story
  <https://everse.software/RSQKit/greenphsecs_research_software_story>

