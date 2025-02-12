---
title: Editors Checklist
summary: Checklist for Editors before approving and merging a pull request (PR).
---

### General Guidelines for Approving Pull Requests

Before approving and merging a pull request (PR), the Editors will check that:

- The modified page(s) layout looks correct on the RSQKit website (either by checking Netlify's "Deploy Preview" on the 
PR in RSQKit, or downloading and checking the PR branch locally on the Editor's machine, or checking the deployment or a PR in a fork in GitHub).
- The Contributors implemented the requested changes and comments, if needed.
- The Contributors are acknowledged and thanked for their efforts and informed about the publication of their content.
- The PR is linked to related issues and can be merged into the main branch with no conflicts.


### Specific Checkst for Metadata

- All relevant metadata fields in a specific page or data files are correctly filled in - check the [**Metadata Guidelines**][metadata_guidlines].
- In particular, ids should not contain spaces - rather use hyphens (-) or underscores (_) to separate words.


### Specific Checks for Task & Other Content Pages

- If needed, the new page is linked in the appropriate sidebar menu. When adding the page to the sidebar navigation, ensure that the sidebar entry's 'title' matches the page's 'title'."
- Make sure that all tools and resources mentioned on a page are added to the ["tools and resources" data file][tools_and_resources] and then tagged in the text of the page
using the `{% raw  %}{% tool 'tool_or_resource_id' %}{% endraw  %}` directive.

### Specific Checks for Contributors' Data

- A Contributor has provided at least their GitHub username/handle, as GitHub IDs are used to uniquely identify Contributors in RSQKit.
- A Contributor is listed in the [CONTRIBUTORS file][contributors] and each page they contributed to (in the [page metadata][metadata_guidlines]).

[metadata_guidlines]: https://everse.software/RSQKit/metadata_guidelines
[tools_and_resources]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/tool_and_resource_list.yml
[contributors]: https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/CONTRIBUTORS.yml
