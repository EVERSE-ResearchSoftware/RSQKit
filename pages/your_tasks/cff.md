---
title: Creating a CITATION.cff file
description: What is the Citation File Format and how to create a CITATION.cff for your software
contributors: ["Jason Maassen"]
page_id: cff
related_pages:
  your_tasks: [zenodo_doi, codemeta]
---
## What is the Citation File Format?
The [Citation File Format](https://citation-file-format.github.io/) lets you provide citation information for software by creating a `CITATION.cff` file in your source code 
repository. A `CITATION.cff` file is a plaintext file (using the [YAML format](https://yaml.org/spec/1.2.2/)) that is easy to read by both humans and machines. Using a list of properties, you can provide all 
information needed to cite your software in a concise and structured way. 

## Why do you need a CITATION.cff file?

### Description <!-- do not delete this heading and write your text below it -->

Correctly citing a paper is easy. All the necessary information (the metadata) can be found on the title page of the paper or the website of the publisher. You can often download this information in 
various ready-to-use formats.

Software has no title page, however. The relevant information to cite software is often less obvious and harder to find. What is the official name of the software? What is the appropriate set of people 
that should be cited as authors? What version of the software should be cited? Is there a paper about the software that should be cited instead? If you want people to cite your research software, you will 
need to help them do it properly.

By adding a `CITATION.cff` file in your source code repository, you can provide all of this information in a concise and structured way. Not only does this give your users all the right information to 
cite your software correctly, but is also enables other tools and services such as 
[GitHub](https://github.blog/news-insights/company-news/enhanced-support-citations-github/),
[Zenodo](https://support.zenodo.org/help/en-gb/24-github-integration/96-how-does-a-citation-cff-file-affect-metadata-of-my-github-release) and 
[Zotero](https://www.zotero.org/) to re-use the citation metadata you provide. 

But how do you create a `CITATION.cff` file?

### Considerations <!-- do not delete this heading and write your text below it -->
* You use a code repository such as {% tool "github" %} as your software repository
* You are knowledgeable about the metadata you want to describe. You can have a look at the [Citation File Format Guide](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md)
to get an overview of all supported metadata. Keep in mind that you do not have to include all fields, just the ones you know. 

### Solutions <!-- do not delete this heading and write your text below it -->
* Create a `CITATION.cff` file by either:
  * using the [CFFinit](https://citation-file-format.github.io/cff-initializer-javascript/#/) online form, which will help you create a valid `CITATION.cff` file which you can download.
  * manually copying and pasting the [example snippet](https://github.com/citation-file-format/citation-file-format?tab=readme-ov-file#structure) and adapting it to your needs. You can then use [cffconvert](https://pypi.org/project/cffconvert/) to validate your `CITATION.cff` file. 
* Once you have created a correct `CITATION.cff` file, you can add it to the root directory or your source code repository.

A more detailed description on how to create `CITATTION.cff` files can be found on the [Turing Way](https://book.the-turing-way.org/communication/citable/citable-cff.html). You can find a list of 
additional tools to create, validate and convert `CITATION.cff` files [here](https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench).
