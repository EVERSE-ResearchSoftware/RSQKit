---
title: "Using static analysis"
description: "How to use static analysis tools to detect bugs, enforce coding standards, check types, and improve the quality of research software before it runs."
contributors: ["Shoaib Sufi"]
page_id: static_analysis
related_pages:
  tasks: [ci_cd, code_review, writing_readable_code, testing_software, maintaining_research_software]
quality_indicators: [has_no_linting_issues, uses_tool_for_warnings_and_mistakes, static_analysis_common_vulnerabilities]
keywords: ["static analysis", "linting", "code quality", "type checking", "pre-commit", "security scanning"]
---

## How do you use static analysis to improve the quality of your research software?

### Description

Static analysis is the automated examination of your source code without executing it.
Tools in this category detect bugs, enforce coding standards, check types, and flag security vulnerabilities before your code runs.
For research software, where correctness directly affects the validity of your results, catching these issues early is worth the modest setup effort.
It does not replace testing or code review — a clean run means only that your code conforms to the rules you configured.

### Considerations

- Linting, type checking, and security scanning are distinct levels — a basic linter alone adds real value, and for many research scripts it is sufficient.
- Adopting static analysis on an established codebase will surface many pre-existing warnings, so use the baseline or ignore-file mechanism most tools provide to address them incrementally.
- Tool ecosystems vary by language: Python and R are well served, while Fortran and Julia options are more limited and less stable.
- Code generated with AI assistance has the same quality needs as hand-written code, so put it through the same checks.

### Solutions

You need the relevant language runtime and package manager, plus a service such as GitHub Actions or GitLab CI for the [CI step][ci-cd].

- Decide what you want static analysis to do — style, bug detection, type checking, or a combination — as this shapes your tool choice.
- Choose a tool for your language and goals, verifying it is still actively maintained — the ecosystem moves quickly:
  - *Python*: {% tool "ruff" %} (linting and formatting), {% tool "mypy" %} or {% tool "pyright" %} (type checking), {% tool "bandit" %} (security)
  - *R*: {% tool "lintr" %}
  - *C/C++*: {% tool "clang-tidy" %}, {% tool "cppcheck" %}
  - *Julia*: {% tool "jet-jl" %} (error detection), {% tool "aqua-jl" %} (package quality)
  - *Fortran*: options are limited and change often — check current community recommendations
- Run the tool with default configuration to get a starting point — for Python with ruff:
  ```
  ruff check .
  ```
- Agree what your team will enforce and how suppressions are handled — a rule you routinely suppress has stopped being useful — and document the configuration.
- Run the tool in CI on every push or pull request as a pass/fail check.
- Add a pre-commit hook with {% tool "pre-commit" %} for faster local feedback.
- Skip throwaway scripts and purely exploratory notebooks, where setup overhead outweighs the benefit — reconsider for notebooks that others will run or that form part of a reproducible pipeline.

## Further Reading

- **[Ruff documentation][ruff-docs]** — Covers installation, configuration, rule selection, and editor and CI integration, making it a practical starting point for introducing static analysis to a Python project.
- **[pre-commit documentation][pre-commit-docs]** — Explains how to manage code quality hooks that run locally before commits, useful for teams wanting consistent tool runs across contributors and languages.
- **[mypy documentation][mypy-docs]** — Shows how to add type annotations incrementally and interpret type errors, worth reading once basic linting is in place and you want stronger correctness guarantees.
- **[Research Software Engineering with Python][py-rse]** — A freely available book on software engineering practices for researchers, useful context for where static analysis fits within a broader quality practice.
- **[Software Engineering at Google][swe-book]** — Chapter 26 covers static analysis at scale — false positive rates, developer trust, and rollout — and maps directly onto introducing tools to an established project.

## AI Disclosure

This work was produced with the assistance of Claude Fable 5, under the strict editorial control and factual verification of the human author.

[ci-cd]: ./ci_cd
[mypy-docs]: https://mypy.readthedocs.io/
[pre-commit-docs]: https://pre-commit.com/
[py-rse]: https://third-bit.com/py-rse/
[ruff-docs]: https://docs.astral.sh/ruff/
[swe-book]: https://abseil.io/resources/swe-book
