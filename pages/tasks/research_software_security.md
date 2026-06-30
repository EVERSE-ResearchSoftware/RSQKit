---
title: "Improving research software security"
description: "How to improve the security of research software by managing repository risks, secrets, dependencies, static analysis, CI/CD checks, and vulnerability reporting."
contributors: ["Shoaib Sufi"]
page_id: research_software_security
related_pages:
  tasks: [code_review, testing_software, ci_cd, maintaining_research_software, software_management_planning]
quality_indicators: [dependency_management, no_critical_vulnerability, no_leaked_credentials, has_no_linting_issues, static_analysis_common_vulnerabilities, repository_workflows, human_code_review_requirement]
keywords: ["research software security", "secure coding", "secrets management", "dependency scanning", "static analysis", "software supply chain", "ci/cd", "vulnerability management"]
---

## How do you improve the security of your research software?
This page explains how you can understand, prioritise, and implement security practices in your research software to protect data, results, and collaborators.

### Description
Research software security is about protecting your code, data, systems, and users from unauthorised access, tampering, disruption, or misuse.
Weak security can compromise research integrity, expose sensitive data, and undermine reproducibility.
Because research software often depends on open-source components and distributed collaboration, it is particularly exposed to risks such as supply chain attacks, vulnerable dependencies, and credential leaks.

### Considerations
- Your software needs to protect confidentiality, integrity, and availability of data, results, and services.
- You should treat security as part of software quality, not as a separate activity that happens only before release.
- Research software is often developed under time pressure, which can lead to security being added late rather than designed in from the start.
- Your dependencies are part of your security boundary, because third-party packages can introduce known vulnerabilities or supply chain risks.
- Your repository configuration matters as much as your code, because branch protection, review requirements, CI checks, token permissions, and signed releases affect how easily code or artefacts can be tampered with.
- Your credentials need special handling, because secrets committed to a repository may remain exposed through Git history, forks, clones, or cached copies even after the file is changed.
- Security tools can find common problems, but they do not prove that your software is secure.
- AI-generated code, copied snippets, and generated configuration should receive the same review, testing, and security checks as code written manually.
- Security involves trade-offs between openness, usability, collaboration, and protection, especially when your project handles sensitive data or supports external users.

### Solutions
- **Start with a lightweight security baseline for your repository.**
  Use {% tool "openssf-scorecard" %} to assess repository-level security risks and identify which practices to improve first.
  OpenSSF Scorecard can help you evaluate your own repository or dependencies you may want to reuse.
  Relevant checks include branch protection, code review, CI tests, dependency update tooling, pinned dependencies, signed releases, token permissions, binary artefacts, and security policies.

- **Detect exposed secrets before they become incidents.**
  Use {% tool "gitleaks" %} to scan repositories, files, and standard input for passwords, API keys, tokens, and other secrets.
  If your project is hosted on GitHub, enable {% tool "github-secret-scanning" %} to detect hardcoded credentials across repository history and related GitHub content.
  If a secret has already been committed, revoke or rotate it rather than relying only on deleting it from Git history.

```bash
gitleaks detect --source .
```

- **Check your source code for security issues.**
  Use {% tool "bandit" %} for Python projects to find common security issues by scanning Python files and reporting findings.
  Bandit supports recursive scanning, configuration files, severity and confidence filters, baselines, and machine-readable output formats.
  For multi-language projects, use {% tool "sonarqube" %} or another static analysis tool that fits your language stack.
  Treat static analysis findings as review prompts: confirm whether each finding is relevant, fix real issues, document accepted risks, and tune noisy rules over time.

```bash
bandit -r src/
```

- **Scan dependencies for known vulnerabilities.**
  Use {% tool "owasp-dependency-check" %} to identify project dependencies and check whether they contain publicly disclosed vulnerabilities.
  Dependency-Check provides command line, build tool, and CI/CD integrations.
  If your project uses GitLab, use GitLab dependency scanning through {% tool "gitlab-cicd" %} to identify known vulnerabilities in runtime, development, and transitive dependencies.

```bash
dependency-check --project "my-project" --scan .
```

- **Keep dependencies up to date automatically.**
  Use {% tool "dependabot" %} or {% tool "renovatebot" %} to open update pull requests when dependencies, build tools, or GitHub Actions need updating.
  Treat automated dependency updates as review prompts rather than automatic approvals.
  Combine dependency update tools with tests and vulnerability scanning so that updates are checked before they are merged.

- **Run security checks in CI/CD rather than relying on local discipline.**
  Use {% tool "github_actions" %} or {% tool "gitlab-cicd" %} to run secret scanning, static analysis, dependency scanning, and tests automatically on pull requests.
  For GitHub projects, combine CI with tools such as {% tool "gitleaks" %}, {% tool "bandit" %}, {% tool "owasp-dependency-check" %}, and {% tool "openssf-scorecard" %}.
  For GitLab projects, use GitLab CI/CD with dependency scanning and project-specific security jobs.

```yaml
name: security-checks

on:
  pull_request:
  push:
    branches: [main]

jobs:
  python-security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Bandit
        run: |
          pip install bandit
          bandit -r src/
      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
```

- **Use repository controls to reduce supply chain risk.**
  Enable branch protection, require code review, require passing CI checks, and restrict workflow token permissions.
  Use {% tool "openssf-scorecard" %} to check repository practices such as binary artefacts, branch protection, pinned dependencies, signed releases, and token permissions.
  These controls make it harder for accidental changes, compromised accounts, or unsafe automation to alter your default branch or release process unnoticed.

- **Use signed releases when users depend on your published artefacts.**
  Signed releases help downstream users verify that release artefacts have not been tampered with.
  Consider this especially when users install your software from release archives, package registries, containers, or workflow registries.
  Use repository and release tooling that supports verifiable release artefacts, and include release checks in your security baseline.

- **Choose security tools that match your project language and risk profile.**
  For Python, start with {% tool "bandit" %}, {% tool "pytest" %}, {% tool "gitleaks" %}, and {% tool "owasp-dependency-check" %}.
  For Java, combine {% tool "maven" %}, {% tool "owasp-dependency-check" %}, {% tool "sonarqube" %}, and CI-based tests.
  For C and C++, combine {% tool "cmake" %}, {% tool "ctest" %}, compiler warnings, static analysis, and dependency review.
  For GitHub-hosted projects, add {% tool "openssf-scorecard" %} to assess repository-level supply chain practices.
  Verify tool recommendations against the current documentation before adopting them, because security tooling and platform features change quickly.

- **Document your security expectations.**
  Add a `SECURITY.md` file explaining how people should report vulnerabilities, which versions are supported, and what information is useful in a report.
  If your software handles sensitive data, clinical data, personal data, credentials, or externally exposed services, involve institutional security, data governance, or information governance colleagues early.
  Make security decisions visible in your documentation so that contributors understand what is expected and users understand the level of care applied.

- **Do not treat tools as a substitute for security judgement.**
  Automated tools find common problems, but they do not replace threat modelling, design review, code review, testing, or incident response planning.
  Review findings regularly, fix issues that matter, document accepted risks, and revisit your choices when the software gains users, handles more sensitive data, or becomes part of a wider workflow.

## Further Reading

- **[OWASP Secure Coding Practices Quick Reference Guide](https://owasp.org/)** — This is a practical checklist of secure coding practices that can be integrated into the software development lifecycle.
It is useful when you want concrete coding requirements covering areas such as input validation, authentication, access control, cryptography, error handling, data protection, and file management.

- **[OWASP Developer Guide](https://devguide.owasp.org/)** — This guide introduces software security concepts for developers and points to deeper OWASP resources.
It is a good starting point when you need an accessible map of application security principles, secure development practices, verification, operations, and security culture.

- **[NIST Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)** — The SSDF provides a structured set of secure software development practices for reducing vulnerabilities and improving communication about secure development.
It is most useful when you need a framework for planning, assessing, or explaining security practices across a project or organisation.

- **[OpenSSF Scorecard](https://openssf.org/projects/scorecard/)** — OpenSSF Scorecard provides automated checks for repository-level security practices in open source projects.
It is useful for assessing your own project baseline and for reviewing the security posture of dependencies you may want to reuse.

- **[Evaluating Software Supply Chain Security in Research Software](https://arxiv.org/abs/2508.03856)** — This paper examines supply chain security in research software repositories and highlights the relevance of practices such as signed releases and branch protection.
It is especially relevant if you want research-software-specific evidence for why repository and dependency security matter.

## AI Disclosure

This work was produced with the assistance of M365 Copilot based on GPT-5 reasoning model, under the strict editorial control and factual verification of the human author.

