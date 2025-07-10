---
title: Citing software
description: How can people cite your software?
contributors: ["Jason Maassen"]
page_id: citing_software
indicators: [software_has_citation]
related_pages:
  your_tasks: [software_identifiers, software_metadata]
training:
   - name: Training in EVERSE TeSS
     registry: TeSS
     url: https://everse-training.app.cern.ch/materials?q=%22citation%22+%22cff%22
---

## What is software citation?

Software citation refers to the practice of giving proper credit to software used in research, 
just as researchers cite articles, books and datasets. 
It involves including a structured reference to the software in publications, ensuring that the creators and contributors receive recognition for their work.

A software citation typically includes:
 
- software title
- specific version used in the research to ensure reproducibility
- authors/creators (people who developed or contributed to the software)
- a digital object identifier (DOI) or another stable reference link to the software (e.g. Zenodo)
- software repository or URL where the software can be accessed (e.g., GitHub, Zenodo, institutional repositories).

### Why does software citation matter? 

Proper software citation supports the integrity of research and ensures that software 
developers receive appropriate acknowledgement for their contributions. 
It ensures that future researchers can use the exact version of the software to replicate results and 
encourages continued development and maintenance of research software if it is important for research.
It helps with impact measurement as it enables tracking the impact of software in research through citation metrics.
Finally, acknowledging software use is part of good research (ethical and professional) practice.

### Solution 

To provide citation information for your software, typically you add a citation file to the root of your software repository 
or software package. A citation file can be a plain text (CITATION.txt) or a Markdown file (CITATION.md), 
but there are certain benefits to using use a special file format called the Citation File Format (CFF) in your citation 
file CITATION.cff, which provides a standard way to include richer metadata about your code, 
making it easy for both humans and machines to use this information.

We will cover Citation File Format in more detail below.

## What is the Citation File Format?

The [Citation File Format](https://citation-file-format.github.io/) lets you provide citation information for software by creating a `CITATION.cff` file in your source code 
repository. A `CITATION.cff` file is a plaintext file that uses a special and structured [metadata format](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md) 
that allows you to list a number of predefined properties for your software that is easy to read by both humans and machines.

### Why do you need a CITATION.cff file?

Correctly citing a paper is easy. All the necessary information (the metadata) can be found on the title page of the paper or the website of the publisher. You can often download this information in 
various ready-to-use formats.

Software has no title page, however. The relevant information to cite software is often less obvious and harder to find. What is the official name of the software? What is the appropriate set of people 
that should be cited as authors? What version of the software should be cited? Is there a paper about the software that should be cited instead? If you want people to cite your research software, you will 
need to help them do it properly.

By adding a `CITATION.cff` file in your source code repository, you can provide all relevant citation information in a concise and structured way. Not only does this give your users all the right 
information to cite your software correctly, but is also enables other tools and services, such as [GitHub](https://github.blog/news-insights/company-news/enhanced-support-citations-github/), 
[Zenodo](https://support.zenodo.org/help/en-gb/24-github-integration/96-how-does-a-citation-cff-file-affect-metadata-of-my-github-release) and [Zotero](https://www.zotero.org/), to re-use the citation 
metadata you provide.

### Solutions 

To create a `CITATION.cff` file for your software:

* use the [CFFinit](https://citation-file-format.github.io/cff-initializer-javascript/#/) online tool to create a valid `CITATION.cff` file which you can download, or
* manually copy and paste an [example snippet](https://github.com/citation-file-format/citation-file-format?tab=readme-ov-file#structure) 
into your `CITATION.cff` file and adapt it to your needs, then use [cffconvert](https://pypi.org/project/cffconvert/) to validate your `CITATION.cff` file. 

Once you have created a correct `CITATION.cff` file, can add it to the root directory of your source code repository.

You can also use the CFFinit tool to update an existing `CITATION.cff` file by pasting its contents in the tool's online form, updating the fields and saving it.

A more detailed description on how to create `CITATION.cff` files can be found in the [Turing Way's Handbook for Open and Reproducible Research](https://book.the-turing-way.org/communication/citable/citable-cff.html). 
You can find a list of additional tools to create, validate and convert `CITATION.cff` files in the [CFF GitHub Repository](https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench).

### Training materials
- [CodeRefinery: Software Citation guidelines](https://coderefinery.github.io/social-coding/software-citation/)
