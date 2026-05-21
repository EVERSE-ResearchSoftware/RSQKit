---
title: "Using static analysis"
description: "How to use static analysis tools to detect bugs, enforce coding standards, check types, and improve the quality of research software before it runs."
contributors: ["Shoaib Sufi"]
page_id: static_analysis
related_pages:
  tasks: [ci_cd, code_review, languages_tools_infrastructures, reproducible_software_environments]
quality_indicators: [has_no_linting_issues, uses_tool_for_warnings_and_mistakes, static_analysis_common_vulnerabilities]
keywords: ["static analysis", "linting", "code quality", "type checking", "pre-commit", "security scanning"]
training:
  - name: "EVERSE TeSS"
    url: "https://everse-training.app.cern.ch"
---

## How do you use static analysis to improve the quality of your research software?

This page provides an overview of static analysis, practical guidance on choosing and running tools, and pointers to further resources for common research software languages.

### Description

Static analysis is the automated examination of source code without executing it. Tools in this category detect bugs, flag potential errors, enforce coding standards, check for type inconsistencies, and identify security vulnerabilities — all before the code runs. For research software, where correctness directly affects the validity of results, catching these issues early is worth the modest effort of setting a tool up. Static analysis does not replace testing or code review, but it catches a different class of problem and does so consistently and cheaply.

### Considerations

- **Static analysis works at several levels** — linting and style enforcement, type checking, and security scanning are distinct activities. A basic linter alone adds real value; you do not need to adopt all three levels at once, and for many research scripts a linter is entirely sufficient.
- **Your existing codebase may already have issues** — introducing static analysis to an established project will typically surface a long list of pre-existing warnings. This is normal. Most tools provide a baseline or ignore-file mechanism so you can address issues incrementally rather than all at once.
- **Warnings you always suppress have stopped being useful** — if your team routinely disables a rule without review, the rule is not earning its place. Configure tools to reflect what you actually want to enforce.
- **Tool choice depends on your language and goals** — the ecosystem varies considerably by language. Python and R are well served; Fortran and Julia options are more limited and less stable. Verify that any tool you adopt is actively maintained.
- **Static analysis is not a substitute for judgement** — a clean linter run does not mean the code is correct. It means it conforms to the rules you have configured.
- **If you use AI code generation tools**, static analysis is a useful check on generated code. AI-generated code can have the same category of issues — style inconsistencies, type errors, unused variables — that linters catch reliably.

### Solutions

**Prerequisites:** you will need the relevant language runtime installed (e.g. Python 3.8+, R 4.x), a package manager (pip, conda, or equivalent), and basic familiarity with running commands in a terminal. For CI integration you will also need access to a CI service such as GitHub Actions or GitLab CI.

**Conceptual guidance**

- Decide what you want static analysis to do for your project — enforce consistent style, catch likely bugs, check types, or some combination. This shapes which tools you need and keeps configuration purposeful.
- Treat static analysis as a quality signal for the whole team, not a gatekeeping mechanism. Introduce it with a short conversation about what the team will enforce and how suppressions should be handled.
- For a new project, start with default or recommended tool configuration before customising. For an existing project, use the tool's baseline feature to suppress pre-existing issues and address them in batches.

**Actionable steps**

- **Choose a tool appropriate for your language and goals.** Tool recommendations below reflect current practice but the ecosystem moves quickly — check that any tool you adopt is still actively maintained before committing to it:
  - *Python*: {% tool "ruff" %} (widely used linter and formatter), {% tool "mypy" %} or {% tool "pyright" %} (type checking), {% tool "bandit" %} (security)
  - *R*: {% tool "lintr" %} (linting and style)
  - *C/C++*: {% tool "clang-tidy" %} (linting and bug-finding), {% tool "cppcheck" %} (static analysis)
  - *Fortran*: options are more limited and the tooling landscape changes — check current community recommendations before adopting a specific tool
  - *Julia*: {% tool "jet-jl" %} (type-based error detection), {% tool "aqua-jl" %} (package quality checks)

- **Run the tool on your codebase to get a starting point.** For Python with ruff, the minimal starting command is:
  ```
  ruff check .
  ```
  This runs ruff against all Python files in the current directory using default rules and prints any issues found. Most tools have an equivalent minimal invocation — consult the tool's documentation.

- **Integrate into your CI pipeline** — run static analysis automatically on every pull request or push. Most tools produce output that CI systems can surface as pass/fail checks, making it visible without requiring manual runs.

- **Add a pre-commit hook for fast local feedback** — running a linter locally before committing catches issues earlier and reduces CI noise. {% tool "pre-commit" %} is a widely used framework for managing this across languages.

- **Document your configuration** — record which tools you are using, which rules are enabled, and how the team handles suppressions. This prevents warnings from being worked around silently.

**When static analysis may not be the right fit**

Static analysis is less valuable for very short throwaway scripts unlikely to be reused, and for Jupyter notebooks used purely for exploratory data analysis rather than as part of a reproducible pipeline. In these contexts the overhead of configuring and running a tool may outweigh the benefit. For notebooks that form part of a reproducible workflow, or that others will run, it is worth reconsidering.

## Further Reading

- **[Ruff documentation](https://docs.astral.sh/ruff/)** — The reference documentation for ruff, a widely used Python linter and formatter. Covers installation, configuration, rule selection, and integration with editors and CI. A practical starting point for anyone introducing static analysis to a Python project.

- **[pre-commit documentation](https://pre-commit.com/)** — Documentation for the pre-commit framework, which manages and runs code quality hooks locally before commits. Particularly useful for teams wanting consistent tool runs across contributors and languages without relying solely on CI.

- **[mypy documentation](https://mypy.readthedocs.io/)** — The reference documentation for mypy, Python's established static type checker. Explains how to add type annotations incrementally and interpret type errors. Useful once basic linting is in place and you want stronger correctness guarantees.

- **[Research Software Engineering with Python](https://third-bit.com/py-rse/)** — A freely available book covering software engineering practices for researchers using Python, including material on code quality, testing, and automation. Provides useful context for readers who want to understand where static analysis fits within a broader quality practice.

- **[Software Engineering at Google](https://abseil.io/resources/swe-book) — Winters, Manshreck & Wright (O'Reilly, freely available online)** — Chapter 26 covers how to think about static analysis at scale, including false positive rates, developer trust, and rolling tools out to large codebases. The strategic framing maps directly onto the considerations above, particularly if you are introducing static analysis to an established project.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.

