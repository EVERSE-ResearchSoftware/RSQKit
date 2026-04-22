---
title: "Using static analysis"
description: "How to use static analysis tools to detect bugs, enforce coding standards, and improve the quality of research software."
contributors: ["Claude Sonnet", "Shoaib Sufi"]
page_id: static_analysis
related_pages:
  tasks: [ci_cd, code_review, languages_tools_infrastructures, reproducible_software_environments]
quality_indicators: [has_no_linting_issues, uses_tool_for_warnings_and_mistakes, static_analysis_common_vulnerabilities]
keywords: ["static analysis", "linting", "code quality", "type checking", "code smells", "pre-commit"]
training:
  - name: "EVERSE TeSS"
    url: "https://everse-training.app.cern.ch"
---

## How do you use static analysis to improve the quality of your research software?

This page provides an overview of static analysis, guidance on choosing appropriate tools, and pointers to further resources for common research software languages.

### Description

Static analysis is the automated examination of source code without executing it, used to detect bugs, enforce coding standards, identify security vulnerabilities, and flag code quality issues. When you are working on research software where correctness is critical and code often evolves rapidly across a team, static analysis catches whole classes of errors — type mismatches, undefined variables, unreachable code — before they reach your results. It is one of the lowest-effort, highest-return quality practices you can adopt.

### Considerations

- **Static analysis complements but does not replace your tests** — it catches structural and stylistic issues that your tests may not exercise, but cannot verify that your code produces scientifically correct results.
- **Different tools serve different purposes** — linters enforce style and flag obvious errors; type checkers verify type correctness; security scanners look for known vulnerability patterns. You may need more than one.
- **Your language matters** — tool ecosystems vary significantly. Python, R, Fortran, C/C++, and Julia each have different levels of static analysis support and different community norms.
- **Strictness is configurable** — most tools can be tuned. Starting with a permissive configuration and tightening it over time is more practical than enforcing maximum strictness on an existing codebase all at once.
- **Integration into your development workflow is what makes it stick** — static analysis run only occasionally has limited value; run automatically on every commit or pull request, it becomes a reliable quality gate.
- **False positives are real** — all static analysis tools produce some false positives. You and your team should agree on which rules to enable and be prepared to suppress specific warnings with justification.
- **Your existing codebase may have many pre-existing issues** — when introducing static analysis to legacy code, consider fixing issues incrementally rather than all at once, to avoid overwhelming your team.

### Solutions

**Conceptual guidance**

- Decide what you want static analysis to do for your project: enforce a consistent style, catch bugs early, check types, or all three. This shapes which tools you need.
- Treat static analysis warnings as a quality signal, not a bureaucratic hurdle. A warning that you always suppress without review is a warning that has stopped being useful.

**Actionable steps**

- **Choose a tool appropriate for your language and goals:**
  - *Python*: [`[ruff](https://docs.astral.sh/ruff/)`](https://docs.astral.sh/ruff/) (fast linter and formatter), [`[mypy](https://mypy.readthedocs.io/)`](https://mypy.readthedocs.io/) or [`[pyright](https://github.com/microsoft/pyright)`](https://github.com/microsoft/pyright) (type checking), [`[bandit](https://bandit.readthedocs.io/)`](https://bandit.readthedocs.io/) (security)
  - *R*: [`[lintr](https://lintr.r-lib.org/)`](https://lintr.r-lib.org/) (linting and style)
  - *C/C++*: [`[clang-tidy](https://clang.llvm.org/extra/clang-tidy/)`](https://clang.llvm.org/extra/clang-tidy/) (linting and bug-finding), [`[cppcheck](https://cppcheck.sourceforge.io/)`](https://cppcheck.sourceforge.io/) (static analysis)
  - *Fortran*: [`[fortran-linter](https://github.com/cphyc/fortran-linter)`](https://github.com/cphyc/fortran-linter), [`[flint](https://github.com/JonasToth/flint)`](https://github.com/JonasToth/flint) (options are more limited than for modern languages)
  - *Julia*: [`[JET.jl](https://aviatesk.github.io/JET.jl/stable/)`](https://aviatesk.github.io/JET.jl/stable/) (type-based error detection), [`[Aqua.jl](https://juliatesting.github.io/Aqua.jl/stable/)`](https://juliatesting.github.io/Aqua.jl/stable/) (package quality checks)
- **Start with the tool's default or recommended configuration** — don't spend time customising rules before you understand what the tool flags in your codebase.
- **Integrate into your CI pipeline** — run static analysis automatically on every pull request or push. Most tools produce output that CI systems (GitHub Actions, GitLab CI, etc.) can surface as pass/fail checks.
- **Add a pre-commit hook** — running a fast linter locally before you commit catches issues earlier and reduces CI noise. [`[pre-commit](https://pre-commit.com/)`](https://pre-commit.com/) is a widely used framework for managing this across languages.
- **Agree team conventions** — document which tools you are using, which rules are enabled, and how suppressions should be handled. This prevents individual developers from working around warnings silently.
- **Fix issues incrementally** — if you are introducing static analysis to an existing project, use the tool's baseline or ignore-file mechanism to suppress pre-existing issues, then address them in batches over time.

## Further Reading

The following are authoritative and highly regarded resources for going deeper on static analysis tools, strategies, and integration practices. Practical and tool-focused resources are listed first, followed by broader texts that provide strategic and theoretical context.

- **[[Ruff documentation](https://docs.astral.sh/ruff/)](https://docs.astral.sh/ruff/)** — The reference documentation for Ruff, now the most widely adopted Python linter and formatter. Exceptionally well-written, it covers the rationale behind individual rules and serves as a practical model for how a modern static analysis tool should work. Useful even if you only skim it for its approach to rule configuration and suppression.

- **[[pre-commit framework documentation](https://pre-commit.com/)](https://pre-commit.com/)** — The definitive guide to wiring static analysis and other checks into your local development workflow across any language. Covers installation, hook configuration, and CI integration — the most direct path from "I have a tool" to "the tool runs automatically".

- **[[Software Engineering at Google](https://abseil.io/resources/swe-book)](https://abseil.io/resources/swe-book) — Winters, Manshreck & Wright (O'Reilly, freely available online)** — Chapter 20 covers how to think about static analysis at scale, including false positive rates, developer trust, and rolling tools out to large codebases. The strategic framing maps directly onto the considerations above, particularly if you are introducing static analysis to an established project.

- **[[Continuous Delivery](https://continuousdelivery.com/)](https://continuousdelivery.com/) — Jez Humble & David Farley** — The authoritative text on building automated delivery pipelines with quality gates built in. If you want to understand why static analysis belongs in your CI pipeline rather than being run ad hoc, and how it fits alongside testing and other automated checks, this is the place to start.

- **[[Code Complete](https://www.microsoftpressstore.com/store/code-complete-9780735619678)](https://www.microsoftpressstore.com/store/code-complete-9780735619678) — Steve McConnell (Microsoft Press)** — A foundational text on software construction quality. Not exclusively about static analysis, but provides the broader context for why code quality practices matter and how they interact. Most useful if you want to understand the principles behind the tools rather than just use them.

