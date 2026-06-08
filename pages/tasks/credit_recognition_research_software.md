---
title: "Credit and recognition for research software and RSEs"
description: "Guidance on making software contributions visible, citable, and verifiable, and on building the evidence needed for career progression as a Research Software Engineer."
contributors: ["Mehdi Zoubiri", "Federica Quaglia", "Thanasis Vergoulis", "Maria Makaronidou", "Shoaib Sufi"]
page_id: credit_recognition_research_software
related_pages:
tasks: [citing_software, archiving_software, publishing_software, complete_bibliographic_metadata_codemeta, fair_rs]
quality_indicators: [software_has_citation, persistent_and_unique_identifier, archived_in_scholarly_repository, descriptive_metadata, codemeta_completeness, versioning_standards_use]
keywords: ["credit", "recognition", "orcid", "citation", "doi", "codemeta", "citation.cff", "research software engineer", "rse", "open science", "career progression", "contributor roles"]


---

## How do you ensure contributors to your research software receive appropriate credit?

Research software, along with the people who develop, maintain, and train others in its use, is fundamental to modern science. Yet traditional research assessment still prioritises publications over code, workflows, and maintenance. This page provides practical guidance on making software contributions visible, citable, and verifiable — and on building the evidence base you need for career progression as an RSE.

### Description

Software contributions — maintenance, bug fixes, code review, documentation — are routinely invisible in academic assessment systems designed around publications. Making them visible requires structured metadata that connects contributors to their specific roles via persistent identifiers, and tools that integrate with your development workflow rather than adding to it. Without this infrastructure, even substantial contributions remain unattributable and uncreditable.

### Considerations

- Reward actions over roles. Labels like "Developer" or "Maintainer" are static and obscure the actual effort involved. Focus on verifiable, specific activities — a bug fix, a new feature, a test suite improvement — rather than generic role names.
- That said, defining diverse contributor roles (maintainers, developers, testers, documentation authors) using standards such as the [Contributor Roles Ontology (CRO)](https://data.bioontology.org/ontologies/CRO) or [CRediT](https://credit.niso.org/) still matters for interoperability with automated systems and institutional workflows.
- All contributors should register with {% tool "orcid" %}. This gives everyone an unambiguous persistent identifier that flows automatically into professional records without manual intervention.
- Your software must be findable and citable — via a DOI — before it can be formally recognised in research assessment. A contribution no one can point to will not be counted.
- Manual crediting does not scale in active projects. Prioritise tools that integrate directly with your development workflow and generate contribution records automatically.

### Solutions

#### Make your software citable with standard metadata

- Add a `CITATION.cff` file to your repository root. This machine-readable format tells tools and platforms exactly how to cite your software. Use the {% tool "cffinit" %} to create one without writing it by hand.
- Add a `codemeta.json` file using {% tool "codemeta" %} to provide richer discovery metadata. This feeds into aggregators such as the OpenAIRE Graph and makes your software more findable across platforms.
- Include a `CONTRIBUTORS` file alongside these machine-readable files to document your project team in a human-readable form.

#### Give your software a persistent identifier

- Release your software via {% tool "zenodo" %} or {% tool "figshare" %} to obtain a DOI, making your code a formal, citable research object recognised by publishers, funders, and institutions.
- Apply {% tool "semantic-versioning" %} (SemVer) across all releases — including {% tool "github" %} tags and distribution artefacts such as Docker images — so each citable version is clearly identifiable and reproducible.

#### Automate credit capture using recognition platforms

- [APICURON](https://apicuron.org/) lets you define the activities you want to recognise and push contribution events to its API. It generates badges, medals, and community leaderboards, and surfaces contributions directly on contributors' {% tool "orcid" %} profiles — moving recognition from self-reported to externally validated.
- {% tool "bip-scholar" %} leverages OpenAIRE Graph metadata (from {% tool "zenodo" %} DOIs and similar sources) to generate open science indicators such as software popularity and reuse metrics, integrating these into multi-dimensional researcher profiles.

---

## How do you demonstrate the impact of your research software for career progression?

### Description

Impact in research software is not captured by citation counts alone. For RSEs and research software contributors, impact spans reuse, community adoption, and technical excellence — but these do not translate automatically into the kind of evidence that hiring committees, promotion panels, and grant reviewers can assess. You need to actively build and present that evidence in terms that non-technical reviewers can understand.

### Considerations

- Quantitative indicators such as download counts are useful, but must be paired with narrative descriptions of technical complexity and scientific impact. Numbers tell reviewers how much; narrative tells them why it matters.
- Check explicitly whether your institution or funder — for example, Horizon Europe — recognises non-traditional outputs such as software in its assessment frameworks. The policies that apply to you will shape which types of evidence to prioritise.
- Include a "Credit and Recognition" section in your Software Management Plan, and treat contribution tracking as a process-over-product matter: record how contributions are captured from the start, not retrospectively.
- Externally validated evidence can enhance self-reported claims. Contribution records generated by platforms offer additional credibility in formal assessment contexts alongside your self-compiled information.

### Solutions

#### Build a verifiable evidence base from your tracked contributions

- [APICURON](https://apicuron.org/) and {% tool "bip-scholar" %} together provide structured, externally validated evidence of your work. APICURON's contribution tracking covers the activity record; BIP! Scholar adds reach and reuse metrics. Together they give you concrete, citable data points to anchor your career narrative in a CV or promotion case.

#### Link your software releases to your ORCID record

- Ensure all releases deposited via {% tool "zenodo" %} or {% tool "figshare" %} are connected to your {% tool "orcid" %} record. This creates a permanent, verifiable link between your identity and your technical outputs, visible to any reviewer who looks you up.

#### Document adoption and reuse concretely

- Beyond contribution tracking, evidence of how widely your software is used carries significant weight. Useful proxies include download counts on package managers ({% tool "pypi" %}, {% tool "cran" %}), inclusion in major research infrastructures, dependency graphs, and papers that directly cite or use your software. If it’s made easier to compile these actively it makes it easier to give reviewers tangible measures of reach and scientific relevance.

#### Build credibility through peer recognition

- Participation in initiatives such as [HiddenREF](https://hidden-ref.org/) or [SSI Fellowships](https://www.software.ac.uk/programmes/fellowship-programme) signals community standing in ways that metrics alone cannot. These carry particular weight with reviewers unfamiliar with how to evaluate technical work, because they represent an external judgement of quality and leadership within the Research Software Community.

---

## Further Reading

- **[ELIXIR-STEERS Policy Brief: Strategies for enhancing the credit and recognition of research artefacts](https://elixir-europe.org/news/elixir-steers-policy-brief)** — A concise policy brief from the ELIXIR network covering practical and institutional strategies for making research software contributions visible and formally creditable. Particularly relevant if you are making the case for recognition within a European research or ELIXIR-affiliated context.

- **[EVERSE Landscape Analysis D5.1: Existing rewards and mechanisms for research software](https://zenodo.org/records/14978474)** — A systematic review of current reward and recognition mechanisms for research software, produced as part of the EVERSE project. Essential background if you want to understand what infrastructure and initiatives already exist before building your own approach.

- **[CoARA: Coalition for Advancing Research Assessment](https://coara.eu/)** — The primary international coalition driving reform of research assessment criteria to go beyond publications. If you are navigating institutional or funder assessment processes, CoARA is the framework your institution is most likely referencing, and understanding it will help you make the case for software recognition.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6 reviewing the human authors draft, subsequent changes were accepted under the strict editorial control and factual verification of the human authors.
