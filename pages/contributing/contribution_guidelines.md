---
title: Contribution Guidelines
---

The RSQKit is currently in a startup phase and still under heavy development which means its structure and content is likely to change a lot.
During this phase, we organise contributions through the EVERSE project's internal documents and communication channels, and welcome reports on
issues and problems with existing pages, fixes to existing content, and reviews of proposed changes.
At some point in the future, we will move towards a fully GitHub-centered contribution workflow.

The content of RSQKit is currently being approved and curated by the [RSQKit Editorial Board][editorial-board], who are also acting as the official
**Maintainers** of the RSQKit repository.
The RSQKit **Editorial Board Members** work together with Internal Contributors from the EVERSE project and External Contributors (jointly known as [**Contributors**][contributors])
to identify where and how their contribution fits best in RSQKit.

## Contributor Agreement

By contributing, you agree that we may redistribute your work under [our
license][licence]. In exchange, we will address your issues and/or assess
your change proposal as promptly as we can.

## Markdown Content

RSQKit's content mainly consists of [pages][pages] in Markdown (in addition to [data and metadata][data] in YAML). 
Markdown is a lightweight and human-readable markup language that gets translated into HTML pages that consequently get served as web pages.
For more information about the Markdown format, please check the [Markdown guidelines](https://guides.github.com/features/mastering-markdown/).

You may also find the ["Markdown Cheatsheet" from RDMKit][markdown-cheatsheet] very useful as a quick reference.

## How to Contribute

We accept contributions in different ways.

### Via GitHub

The easiest way to get started is to contribute via the [RSQKit repository in GitHub][rsqkit-repository].
For this - you will require a [GitHub][github] account. If you do not have it - you can [create one][github-join].
For this method of contribution - you do not need to know how to use Git.

You can report problems (e.g., a spelling mistake, some awkward wording, or a factual error) or 
suggest improvements by [creating an issue][issues]. This allows us to assign the item to someone and to respond to 
it in a threaded discussion.

If you are comfortable with GitHub, and would like to add or change material, you can submit a pull request (PR) 
directly from GitHub. 
Instructions for doing this are [included below](#creating-a-pull-request).

### Using Git from Command Line

Working in GitHub interface is convenient, but does not allow for spelling checking and lots of spelling mistakes can 
creep in this way if you are writing a lot of content. Hence, it is better to create your own fork of the RSQKit 
repository and then clone it locally on your machine. This way, you can edit files in a text editor with spelling 
checking and other capabilities (instead in GitHub's online editor) and also test your work extensively before 
[creating a PR](#creating-a-pull-request).

Working with Git from command line is technically more challenging, as you will need to understand and install Git
on your machine, but it much more flexible and less error prone.

Check out [the instructions on how to fork and set up RSQKit locally on your machine][installation-instructions].

### Other Ways to Contribute

Note that you do not have to use Git or contribute via GitHub to be included as a Contributor - 
any significant discussion or contributions via other methods
(e.g. email, internal project documents used to collect information, etc.) are accepted.
Email the [Editorial Board][contact] with a short explanation of your contributions and you will be 
appropriately acknowledged.

## What to Contribute

Whichever contribution route you choose, we welcome the following types of contributions:

- [reports on issues, bugs and typos](#reporting-an-issue) in the RSQKit content
- suggestions for new content by creating a [new issue](#reporting-an-issue) for discussion
- comments on [existing issues][issues] and reviews of [existing pull requests][pull-requests]
- [pull requests](#creating-a-pull-request) to fix issues, bugs and typos in the RSQKit content

If you plan to submit a pull request that adds new content or significantly changes existing content,
please [contact the Editorial Board][contact] to discuss this first so that
the effort is only spent on making a change that will be be accepted.

### Reporting an Issue

Issues, bugs or remarks or suggestions for new content are tracked via [GitHub's issues][issues].
You can create an issue and a member of the Editorial Board will review it and assign a person responsible for looking into it.
Alternatively, you can [email the Editorial Board][contact] and they will create a GitHub issue on your behalf.

Here are some guidelines for reporting issues.

- Add a clear and concise description of what the issue is
- Provide a URL of the page where the issue occurs, if applicable
- Add screenshots to help explain the issue, if applicable
- For bug reports, provide the platform information you used when a bug was detected - for example operating system (e.g. iOS), browser type and version (e.g. Firefox 132.0.2)
- Add any additional context that may be helpful in addressing the issue

### Creating a Pull Request

If you choose to contribute via Git/GitHub's pull requests, you may want to look at [How to Contribute to an Open Source Project on GitHub][how-contribute].

1. Open an issue for your pull request first (unless already opened).
2. Create a separate branch for your work - either in your own fork of the RSQKit repository or directly in RSQKit repository if 
you have write access to it. Note that you cannot directly modify the `main` branch in RSQKit repository - you have to do it via 
a branch and a PR (and this is true for Editors/Maintainers as well). 
3. Make sure that your changes in your (fork and) branch are tested and render correctly in the Web site.
4. Submit a pull request from your branch back to the RSQKit repository.
5. If you receive feedback from Editors/Maintainers, make changes on your branch and your pull request will update automatically.

Editorial Board Members will review pull requests and have a final say over what gets merged into RSQKit.

## What *Not* to Contribute

At this point, we do not welcome contributions that create or change the underlying RSQKit infrastructure - for example,
data files in `_data/` folder in the repository, `_config.yml` and other infrastructure files
(such as CSS files, page templates and files in the `_includes/` folder).
If you think some of these files should be updated, please [contact the Editorial Board][contact].

## Contributor Responsibilities

When contributing to this project, please keep in mind the following:

- Follow our [**Page Style Guidelines**][page-style-guidelines] for the sake of page consistency.
- Check our [**Metadata Guidelines**][metadata-guidelines] in order to be able to fill in the data and page metadata and to format the layout correctly.
- Make sure that the content you provide respects copyright.
- Check the [**Editors Checklist**][editors-checklist] and make sure you have complied with the requirements, to avoid having to resolve many issues during the revision process.
- If others assisted with your contribution by writing or supplying resources like diagrams or links, be sure to acknowledge them after obtaining their permission.
- Check [**Installation Instructions**][installation-instructions] if you want to develop and test changes locally on your machine.

## Acknowledgement of Contributions

Contributors will appear at the bottom of every Web page they contributed to.
For that to happen, they need to be added to [CONTRIBUTORS.yaml][contributors] and then listed in the metadata of the Markdown source file for each of the pages they contributed to.
Editorial Board Members will make sure that this is done at the time the contributions are merged into RSQKit.

## Ownership of Content

No individual Contributor owns the project's content or has the authority to dictate its content.
The RSQKit content is a collaborative effort, with contributions from many people.
At the moment, decisions are made by consensus among the [Editorial Board Members][editorial-board].

The content is periodically updated, meaning that if you create content for RSQKit, others may modify it without notifying you.
However, the [Editorial Board][editorial-board] ensures that any changes are made for valid reasons.
They strive to accommodate the legitimate concerns and diverse viewpoints of all contributors and ensure that the content reflects the most widely accepted consensus on any topic.

If you find any content unsatisfactory, please feel free to report about it by [creating an issue](#reporting-an-issue).

[contact]: mailto:rsqkit@lists.certh.gr
[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github
[issues]: https://github.com/EVERSE-ResearchSoftware/RSQKit/issues
[editorial-board]: ./editorial_board
[contributors]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/CONTRIBUTORS.yaml
[pull-requests]: https://github.com/EVERSE-ResearchSoftware/RSQKit/pulls
[github-why-should-i-fork]: https://stackoverflow.com/questions/31209669/github-why-should-i-fork
[licence]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/LICENSE.md
[installation-instructions]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/INSTALL.md
[page-style-guidelines]: ./page_style_guidelines
[metadata-guidelines]: ./metadata_guidelines
[editors-checklist]: ./editors_checklist
[markdown-cheatsheet]: https://rdmkit.elixir-europe.org/markdown_cheat_sheet
[pages]: https://github.com/EVERSE-ResearchSoftware/RSQKit/tree/main/pages
[data]: https://github.com/EVERSE-ResearchSoftware/RSQKit/tree/main/_data
[rsqkit-repository]: https://github.com/EVERSE-ResearchSoftware/RSQKit
