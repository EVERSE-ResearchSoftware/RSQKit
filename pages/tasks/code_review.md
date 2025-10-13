---
title: Performing a code review
description: How do you review code?
contributors: ["Aleksandra Nenadic"]
page_id: code_review
related_pages:
  tasks: []
quality_indicators: [human_code_review_requirement]
keywords: ["code review"]
training:
  - name: "EVERSE TeSS"
    registry: TeSS
    url: "https://everse-training.app.cern.ch"
---

## Code Review in Research Software Development

### Description

What is code review?
Code review is a software quality assurance practice and the process of systematically examining someone else’s code (or your own, after some time) to find bugs, improve quality, and ensure adherence to coding standards.
It’s a collaborative practice aimed at improving software reliability, readability, and maintainability.

#### Why it matters in research?

Rigorous inspections can remove 60-90% of errors from the code even before the first tests are run (Fagan, 1976).
Furthermore, the cost to remedy a defect in the early (design) stage is 10 to 100 times less compared to fixing the same defect in the development and maintenance stages, respectively.
Since the cost of bug fixes grows in orders of magnitude throughout the software lifecycle, it is far more efficient to find and fix defects as close as possible to the point where they were introduced.

In research settings, where software often evolves rapidly and is reused over long periods, code review helps:

- catch errors early before they affect research outcomes
- increase knowledge within a team - someone checks your design or code for errors and gets to learn from your solution; having to explain code to someone else clarifies your rationale and design decisions in your mind too.
- promote code reusability and reproducibility of the research it implements by ensuring clarity and documentation
- encourage best practices like modular design and testing
- facilitate collaboration, especially in multi-disciplinary teams
- support onboarding of new team members with shared knowledge and best coding practices used in the team.

### Consideration - what to look for in a review?

When conducting a code review, you should focus on checking the following:

- Correctness – does the code do what it is supposed to?
- Style and consistency – are naming conventions, formatting, and structure consistent?
- Testing – are there tests? Do they cover expected use cases and edge cases?
- Documentation – are functions, classes, and scripts clearly documented?
- Modularity – is the code organised into reusable and testable components?
- Performance – is the code efficient enough for the task?

### Consideration - what not to look for in a review?

While code reviews are essential for quality, it is just as important to avoid nitpicking or overstepping.
Here are things that should not be the focus of a code review:

- Personal style preferences - avoid debating minor style choices (e.g., single vs. double quotes) if the team has not agreed on a standard. Let linters and formatters handle those.
- Rewriting everything - do not suggest rewriting large sections of code unless there is a clear and necessary reason (like a bug or major design issue). Aim to improve, not take over.
- Blaming or criticising individuals - the goal is to improve the code, not judge the coder. Always keep feedback constructive and kind.
- Perfecting on the first try - code does not need to be perfect before it is merged. If it is functional, well-tested, and clear, minor improvements can come later.
- Marking non-Blocking comments as blocking - if a suggestion is minor or subjective, label it as such. Do not hold up progress for tweaks that can be addressed later.
- Expecting mastery of everything - especially in research, people have varying backgrounds. Do not expect full knowledge of advanced software engineering concepts from domain experts/researchers who code.  

### Solution - code review tips & tools

- Use pull requests - in systems like GitHub or GitLab, use pull/merge requests to structure reviews.
- Keep it constructive - offer clear, kind feedback. Ask questions rather than criticise.
- Automate where possible - use linters and formatters to catch simple issues before review.
- Focus on learning - code reviews are a two-way street—reviewers can learn as much as authors

Tools that can help:

- {% tool "github" %} and {% tool "gitlab" %} have built-in review tools for code review discussions and suggestions
- {% tool "code-linters" %} (e.g., flake8, eslint, {% tool "pylint" %}) ensure code style consistency
- [CI pipelines](./ci_cd) automatically run tests and checks on submitted code

Initiatives:

- [CODECHECK](https://codecheck.org.uk/) aims to tackle the challenge of supporting codecheckers in computational science with a workflow, guidelines and tools to evaluate computer programs underlying scientific papers.