## Contribution Guidelines

The RSQKit is currently in a startup phase and still under heavy development which means its structure and content is likely to change a lot.
During this phase, we organise contributions through the EVERSE project's internal documents and communication channels, and welcome reports on 
issues and problems with existing pages, fixes to existing content, and reviews of proposed changes.
At some point in the future, we will move towards a fully GitHub-centered contribution workflow.

The content of RSQKit is currently being approved and curated by the [RSQKit Editorial Board][editorial-board], who are also acting as the current 
Maintainers of the RSQKit repository.
The RSQKit Editorial Board Members work together with Internal Contributors from the EVERSE project and External Contributors (jointly known as Contributors) 
to identify where and how and their contribution fits best in RSQKit.

### Contributor Agreement

By contributing, you agree that we may redistribute your work under [our
license](LICENSE). In exchange, we will address your issues and/or assess
your change proposal as promptly as we can.

### How to Contribute

The easiest way to get started is to file an issue to tell us about a spelling
mistake, some awkward wording, or a factual error.

1. If you do not have a [GitHub][github] account, you can [send us comments by
   email][contact]. However, we will be able to respond more quickly if you use
   one of the other methods described below.

2. If you have a [GitHub][github] account, or are willing to [create
   one][github-join], but do not know how to use Git, you can report problems
   or suggest improvements by [creating an issue][issues]. This allows us to
   assign the item to someone and to respond to it in a threaded discussion.

3. If you are comfortable with GitHub, and would like to add or change material,
   you can submit a pull request (PR). Instructions for doing this are
   [included below](#creating-a-pull-request).

### What to Contribute

At this moment, we welcome:

- [reports on issues, bugs and typos][#reporting-an-issue] in RSQKit content
- suggestions for new content by creating a [new issue][#reporting-an-issue] for discussion
- comments on [existing issues][issues] and reviews of [existing pull requests][pull-requests]
- [pull requests][#creating-a-pull-request] to fix issues, bug and typos in the RSQKit content

If you plan to submit a pull request that adds new content or significantly changes existing content, 
please [contact the Editorial Board][contact] to discuss this first so that 
the effort is not spent by making a change that may not be accepted.

#### Reporting an Issue

Issues, bugs or remarks or suggestions for new content are tracked via [GitHub's issues][issues].
You can create an issue and a member of the Editorial Board will review it and assign a person responsible for looking into it. 
Alternatively, you can [email the Editorial Board][contact] and they will create a GitHub issue on your behalf.

Here are some guidelines for reporting issues.

- Add a clear and concise description of what the issue is.
- Provide a URL of the page where the issue occurs, if applicable
- Add screenshots to help explain the issue, if applicable
- For bug reports, provide platform information used, for example operating system (e.g. iOS), browser type and version (e.g. Firefox 132.0.2)
- Add any additional context that may be helpful in addressing the issue

#### Creating a Pull Request

If you choose to contribute via GitHub's pull requests, you may want to look at [How to Contribute to an Open Source Project on GitHub][how-contribute]. 

1. Open an issue for your pull request first (unless already opened).
2. Create your own fork of RSQKit repository (even if you have write access to the RSQKit repository) and set it up to render RSQKit pages as a Web site. An even better 
way is to create a branch in your fork for each significant change (pull request), as then you can create multiple pull requests in parallel.
3. Make sure that your changes in your fork/branch are tested and render correctly in the Web site.
4. Submit a pull request from your fork to RSQKit repository (this repository).
5. If you receive feedback, make changes on your fork and your pull request will update automatically.

Editorial Board Members will review pull requests and have a final say over what gets merged into RSQKit.

> [!NOTE]
> The reason why we recommend working in your own forks of this repository versus a branch of this repository is mainly 
> because by having a separate fork, you can render your own version of RSQKit as a website and see what your changes will look like
> before creating a pull request. 
> It also allows reviewers to easily check and test your changes and make sure everything is correct before merging to the main branch.
> 
> Working in GitHub interface is convenient, but does not allow for spelling checks and loads of typos creap in this way.
> If you can - a better way of working would be to clone your fork locally on your machine, and edit files 
> in a good IDE or text editor with spelling checking capabilities.

### What *Not* to Contribute

At this point, we do not welcome contributions that create or change the underlying RSQKit infrastructure - for example, 
data files in `_data/` folder in the repository, `_config.yml` and other infrastructure files 
(such as CSS files, page templates and files in the `_includes/` folder).
If you think some of these files should be updated, please [contact the Editorial Board][contact].

## Contributor responsibilities

When contributing to this project, please keep in mind the following:

- It is your responsibility to make sure that the content you provide respects copyright. 
- To avoid having to resolve many issues during the revision process, please check the Editor checklist and make sure you have complied with the requirements.
- If others assisted with your contribution by writing or supplying resources like diagrams or links, be sure to acknowledge them after obtaining their permission.

## Acknowledgement of Contributions

Contributors will appear at the bottom of the Web page they contributed to. 
For that to happen, they need to be added to [CONTRIBUTORS.yaml][contributors] and then listed in the metadata of the Markdown source file for the page. 

If you are doing a contribution via a pull request, you can also include adding yourself to [CONTRIBUTORS.yaml][contributors] and the pages you changed.

You do not have to contribute via GitHub to be included as a Contributor - any significant discussion or contributions via other methods 
(e.g. email, internal project documents used to collect information, etc.) are accepted too.
In this case, email the [Editorial Board][contact] with your GitHub account/handle, ORCID, and preferred email address and a short explanation of your contributions 
and you will be added to [CONTRIBUTORS.yaml][contributors] and appropriately acknowledged in relevant pages. 


## Ownership of Content

No individual Contributor owns the project's content or has the authority to dictate its content. 
The RSQKit content is a collaborative effort, with contributions from many people. 
At the moment, decisions are made by consensus among the [Editorial Board Members][editorial-board].

The content is periodically updated, meaning that if you create content for RSQKit, others may modify it without notifying you. 
However, the [Editorial Board][editorial-board] ensures that any changes are made for valid reasons. 
They strive to accommodate the legitimate concerns and diverse viewpoints of all contributors and ensure that the content reflects the most widely accepted consensus on any topic.

If you find any content unsatisfactory, please feel free to report about it by "creating an issue" request.

[contact]: mailto:rsqkit@lists.certh.gr
[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github
[issues]: https://github.com/EVERSE-ResearchSoftware/RSQKit/issues
[editorial-board]: http://everse.software/RSQKit/editorial_board
[contributors]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/CONTRIBUTORS.yaml
[pull-requests]: https://github.com/EVERSE-ResearchSoftware/RSQKit/pulls

