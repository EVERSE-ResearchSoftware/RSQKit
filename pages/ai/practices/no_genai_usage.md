---
title: "No Gen-AI Usage (intensity 0)"
description: Practice Overview for No GenAI Usage
contributors: [ "Michael Sparks" ]
page_id: no_genai_usage
keywords: ["ai", "software development", "task automation", "github actions" ]
order: 1000
---
![Spectrum of AI Intensity Usage](../../images/ai/AI_Spectrum-001.png)
<p style='text-align: right;'>
&nbsp; &nbsp; &nbsp; &nbsp;
<a href="spectrum_of_intensity_of_ai_usage">spectrum</a>
<a href="conversational_interaction">next</a>
</p>

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



