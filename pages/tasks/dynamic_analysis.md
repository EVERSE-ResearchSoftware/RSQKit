---
title: "Conducting dynamic analysis"
description: "How to use runtime observation techniques — memory checkers, sanitizers, profilers, and fuzzing — to find bugs and performance issues in research software that static analysis and unit tests miss."
contributors: ["Shoaib Sufi"]
page_id: dynamic_analysis
related_pages:
  tasks: [testing_software, ci_cd, static_analysis, research_software_security]
quality_indicators: [uses_fuzzing, software_test_coverage, has_ci-tests]
keywords: ["dynamic analysis", "fuzzing", "memory checking", "sanitizers", "profiling", "valgrind", "runtime analysis", "coverage"]
---

## How do you conduct dynamic analysis of your research software?

### Description

Dynamic analysis means running your software and observing it at runtime to find problems that static checks and unit tests miss: memory errors, undefined behaviour, performance bottlenecks, or inputs that crash it.
When your software depends on numerical correctness or runs on high-performance computing systems, these defects are hard to detect because they may not surface under normal test conditions.
It complements static analysis by exercising the code under real or adversarial inputs and resource limits.
It reports only on the paths and inputs you actually run, so a clean run is not proof of correctness.

### Considerations

- Memory-unsafe languages (C, C++, Fortran) are most exposed to the errors dynamic analysis catches; in memory-safe languages the highest-value checks are performance and concurrency.
- Sanitizers and memory checkers add significant runtime overhead, so run them in dedicated test or CI builds, not in release builds.
- Fuzzing (feeding your program many automatically generated, often malformed, inputs to find ones that make it crash or misbehave) reaches input-handling paths that hand-written tests rarely cover.
- Profiling results depend on input data and system state, so one dataset's profile may not predict performance on another, particularly for data-dependent scientific algorithms.
- In research software, numerical correctness often matters more than crash detection, so match your checks to the failure modes that would invalidate your results.
- The tools named here reflect the time of writing; check for current alternatives before adopting one.

### Solutions

- For memory-unsafe code, run your test suite under {% tool "valgrind" %}, or under {% tool "addresssanitizer" %} and {% tool "undefinedbehaviorsanitizer" %} for lower overhead by compiling with `-fsanitize=address,undefined -g` on GCC or Clang.
- Run the sanitizer build and tests in CI on every pull request, with a separate {% tool "threadsanitizer" %} job for multithreaded code, as it cannot be combined with AddressSanitizer.
- Profile representative workloads with {% tool "perf" %}, {% tool "gprof" %}, or Valgrind's Callgrind for compiled code, Python's cProfile module, or {% tool "scorep" %} for parallel HPC applications.
- Measure coverage in CI — {% tool "gcov" %} with {% tool "lcov" %} for C and C++, {% tool "coverage-py" %} or {% tool "pytest-cov" %} for Python, {% tool "covr" %} for R — so you know which code your sanitizer and test runs exercised.
- Fuzz code that processes external input with {% tool "aflpp" %} for C and C++ or {% tool "atheris" %} for Python, seeded with valid inputs and run in a sandbox for a fixed time budget.
- For web-facing software, add a dynamic scanner such as {% tool "zap" %} to your pipeline to find vulnerabilities that static scanners miss.
- Compare numerical results with stored reference outputs under sanitizer and optimised builds, and use {% tool "verrou" %} or {% tool "verificarlo" %} to find results sensitive to floating-point rounding.
- Record every finding as an issue with the triggering input, execution environment, and tool output, and add that input to your regression tests so the bug stays fixed.

## Further Reading

- **[Valgrind documentation][valgrind-manual]** — The reference manual for a widely used general-purpose memory checker, covering its analysis tools (Memcheck, Callgrind, Cachegrind, Helgrind, DRD) with practical usage guidance.
- **[Sanitizers wiki][sanitizers-wiki]** — Documentation for AddressSanitizer, ThreadSanitizer, MemorySanitizer, and LeakSanitizer, covering build flags, how to read their reports, and known limitations.
- **[AFL++][aflpp]** — The maintained successor to the original American Fuzzy Lop fuzzer, with installation instructions, a quick start, and in-depth guidance on writing harnesses and building a seed corpus.
- **[ClusterFuzzLite][clusterfuzzlite]** — A guide to running continuous fuzzing inside your own CI pipeline, fuzzing each pull request and producing coverage reports, for projects that are not part of Google's hosted OSS-Fuzz service.
- **[The Python Profilers][python-profilers]** — The standard library documentation for cProfile and profile, the first place to look for where a Python program spends its time before you need more specialised tools.

## AI Disclosure

This work was produced with the assistance of Qwen 3.8(27B), under the strict editorial control and factual verification of the human author.
Claude Fable 5.1 was then used as a second step to review and reformulate the draft and then checked again by the human author.

[aflpp]: https://aflplus.plus/
[clusterfuzzlite]: https://google.github.io/clusterfuzzlite/
[python-profilers]: https://docs.python.org/3/library/profile.html
[sanitizers-wiki]: https://github.com/google/sanitizers/wiki
[valgrind-manual]: https://valgrind.org/docs/manual/
