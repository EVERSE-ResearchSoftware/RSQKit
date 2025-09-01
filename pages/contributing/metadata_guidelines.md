---
title: Metadata Guidelines
summary: Descriptions of different metadata schemas used to describe various resources and pages in RSQKit.
---

This page explains the metadata that can be used to describe various resources and pages in RSQKit. 
These guidelines have been adapted from the ELIXIR Toolkit theme's [page metadata guide](https://elixir-belgium.github.io/elixir-toolkit-theme/page_mechanics)
and [tools and resources guide](https://elixir-belgium.github.io/elixir-toolkit-theme/resource_table).

## Contributor metadata

Contributors are listed in the [contributors file (`_data/CONTRIBUTORS.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/CONTRIBUTORS.yml)
starting with the contributor's full name, followed by the following optional metadata/attributes:

* `git`: contributor's GitHub id (serving as an identifier together with contributor's full name).
* `orcid`: contributor's ORCID id.
* `role`: role of the contributor in the RSQKit. Possible values:
  * `editor` - member of the [Editorial Board](./editorial_board)
  * `author` - someone who creates content, e.g. task and other pages
  * `contributor` - everyone else contributing to RSQKit who is not an editor or author, e.g. with edits and fixes in pages (adding/fixing links, tools and resources, typo and style fixes, curating pages), significant discussions, etc.
* `affiliation`: contributor's affiliation(s) as a single string (if multiple affiliations need to be listed, use a separator - e.g. "/". 
Also note that while affiliations should match those listed in the [affiliations file (`_data/affiliations.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/affiliations.yml) (see below) this is not enforced.
* `image_url`: absolute path to contributor's image or avatar (defaults to contributor's GitHub profile image if GitHub id is provided).

You can reference contributors by their name in the metadata section of content pages using parameter `contributors` - see [page metadata section](#page-metadata) for more details. 

An example contributor definition is given below:

```yml
Fotis Psomopoulos:
    git: fpsom
    orcid: 0000-0002-0222-4273
    email: email.@org.edu
    role: editor
    affiliation: Institute of Applied Biosciences (INAB|CERTH) / ELIXIR-GR
```

## Affiliation metadata

Affiliations are listed in the [affiliations file (`_data/affiliations.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/affiliations.yml)
and can be used as means of listing all institutions in the project or institutions/affiliations of all contributors. 

Affiliations can be described using the following metadata/attributes (all of which are optional apart from the `name`):

* `name`: name of the institution.
* `expose`: flag to indicate whether to show the affiliation in affiliation listings or not.
* `type`: type of affiliation, e.g. `institution`.
* `url`: URL of the affiliation.
* `pid`: persistent identifier of the affiliation (e.g. Research Organisation Registry (ROR) id).
* `image_url`: absolute path to affiliation's image.

An example affiliation definition is given below:

```yml
- name: The University of Manchester
  image_url: /images/institutions/logo-university-of-manchester.svg
  expose: true
  type: institution
  url: https://www.manchester.ac.uk/
  pid: https://ror.org/027m9bs27
```

## Page metadata

Each page in RSQKit can be described with the following metadata/attributes (which can either be included 
in the "front matter" header of the page or applied to a group of pages via `_config.yml` repository file):

* `title`: page title (used as the H1 HTML header in the rendered version of the page).
* `summary`: a short page summary, displayed under the page title.
* `description`: a short page description, used when pages are listed as "tiles" (e.g. in search results, related pages sections or when all pages of certain type are listed).
* `type`: page type, used to classify pages into categories. Each page type is displayed differently in the website. Possible values: `research_community`, `task_page`.
* `contributors`: a list of contributors that authored or contributed significantly to the page in some way (e.g. via discussions). Each contributor must also be listed in the `_data/CONTRIBUTORS.yml` repository file.
* `search_exclude`: a boolean value indicating if the page should be excluded from search results. Default: `false`.
* `sitemap`: a boolean value indicating if the page should appear in the `sitemap.xml`. Default: `true`.
* `no_robots`: a boolean value indicating if the page should not end up in the search results of Google or any other search engines. Default: `false`.
* `hide_sidebar`: a boolean value indicating if the page should not appear in the sidebar. Default: `false`.
* `keywords`: a list of lowercase keywords that can be used to find the page using the search facility of RSQKit.
* `sidebar`: name of the left-hand side navigation sidebar that should be displayed for the page. Default sidebar: `main`. The sidebar file `<SIDEBAR_NAME.md>` named after the sidebar must exist under `_data/sidebars/` in the repository.
* `toc`: a boolean value indicating if a table of contents should be included at the top right of the page. Default: `false`.
* `page_id`: unique identifier of the page, usually a shortened version of the page title (with words separated with underscores or dashes and spaces avoided). This identifier is used in `related_pages` parameter to list pages related to this page. 
* `datatable`: a boolean value indicating the activation of the pagination, sorting and searching in tabular representations of pages.
* `related_pages`: a list of `page_id`s that are related to this page and will appear under "Related pages" section on the page, grouped by page type.
* `page_citation`: When set to `true`, it will cause the citation section for the page to be generated in the format: "<author names>. <page title>. <site domain>. <page URL>. <date accessed>". Defaults to `true` for task pages; `false` for other page types.
* `keywords`: a list of keywords related to the topic of the page, typically used to search training materials and other resources from external registries (such as TeSS training registry)
* `training`: a list of training registry entries, each having the following three properties - `name` (registry display name), `registry` (registry type, e.g. "TeSS", "TechRadar", "SSHOC", "ENVRI Hub") and `url` (registry's base URL that gets combined with keywords to form a search URL taking the user to search results using the `keywords` within that registry).

Training entries will show up under the "More information | Training" section on the page.

An example of a training registry entry: 

```yml
keywords: ["ci", "cd", "continuous integration", "continuous deployment"]
training:
   - name: "EVERSE TeSS"
     registry: TeSS
     url: "https://everse-training.app.cern.ch"
```

## Tools and resources metadata

Tools and resources are described in the [tool and resource data file (`_data/tool_and_resource_list.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/tool_and_resource_list.yml) using the 
following attributes (a subset of the [EVERSE Research Software metadata schema](https://w3id.org/everse/rs#)): 

* `name`: name of the tool or resource.
* `description`: a short description of the tool or resource.
* `id`: identifier used to refer to the tool or resource in pages.
* `url`: URL of the tool or resource
* `quality_indicator`:  research software quality indicators associated with this tool. We have not settled 100% on the format of attribute yet - this is still work in progress. 
Most likely it will be a list of research software quality indicators (defined in the [quality indicators data file (`_data/quality_indicators.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/quality_indicators.yml)).

An example of a tool definition is given below:

```yml
- description: > 
    The System Package Data Exchange (SPDX) License List is a list of commonly found licenses 
    and exceptions used in free and open or collaborative software, data, hardware, or 
    documentation, and is an integral part of the SPDX Specification.
  id: spdx
  name: SPDX License List
  url: https://spdx.org/licenses/
```

Pages in RSQKit can include references to tools and resources. Such references will appear visually different on a page - 
with a little wrench icon and a pop-up window which shows up on hover over and includes the tool/resource description and a website link.

To refer to a tool or a resource in a page, use the following syntax:

{% raw %}
```
{% tool "tool-id" %}
```
{% endraw %}

All tools and resources mentioned on a page will be listed in a table at the bottom of the page as well as under "[All Tools and Resources](all_tools_and_resources)" page. 
Have a look at an [example task page](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/your_tasks/zenodo_doi.md) for how this syntax is used in practice.

## Software quality indicator metadata

Research Software Quality (RS Quality) indicators are described in the [quality indicators data file (`_data/quality_indicators.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/quality_indicators.yml) using the
following attributes (a subset of the [EVERSE Research Software indicator metadata schema](https://w3id.org/everse/rsqi/)):

* `identifier`: identifier associated with the indicator.
* `contact`: contact person or organisation associated with the indicator.
* `name`: name of the indicator (title).
* `description`: a brief description of the indicator, stating its purpose and how to measure it. 
* `keywords`: keywords to ease finding the indicator.
* `quality_dimension`: Research Software Quality (RS Quality) dimension associated with the indicator (see [https://w3id.org/everse/rsqd](https://w3id.org/everse/rsqd) for a full list).
* `version`: if the indicator has a version (e.g., some ISO standards specify indicators), it should be included here.
* `source`: the standard or reference document where the indicator was first proposed.
* `status`: status of the indicator (e.g. deprecated, obsolete, active, etc.).
* `created`: date of creation of the indicator.

An example of an RS Quality indicator definition is given below:

```yml
- identifier: Do1 
  description: >
    Software includes clear contribution instructions, software purpose on project website, 
    feedback channels, and version control practices.
  contact: Daniel Garijo
  name: Contribution Process and Project Purpose
  keywords:
    - contribution guidelines
    - feedback channel
    - software purpose
  qualityDimension:
    - documentation 
  source: https://www.bestpractices.dev/en/criteria/0
  status: active
```

## Software quality dimension metadata  

Research Software Quality indicators can be grouped according to common categories or quality dimensions.
Research Software Quality dimensions are described in the [quality dimensions data file (`_data/quality_dimensions.yml`)](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/_data/quality_dimensions.yml) using the
following attributes from the [EVERSE Research Software dimension metadata schema](https://w3id.org/everse/rsqd/): 

* `identifier`: identifier associated with the dimension.
* `description`: description of the dimension.
* `name`: name of the dimension (title).
* `source`: the standard(s) or reference document(s) where the dimension was proposed, or adapted from.

An example of an RS Quality dimension definition is given below:

```yml
- identifier: documentation 
  description: >
    Ability of the system to provide information helpful for identifying and resolving issues 
    when it fails to work correctly. Existence of a helpdesk or issue tracking, bug reporting, 
    enhancements and general support
  name: Documentation and Supportability
  source: 
    - https://www.iso.org/standard/35733.html
    - https://doi.org/10.5281/zenodo.10723608
```
