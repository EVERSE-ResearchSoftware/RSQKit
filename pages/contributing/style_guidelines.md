---
title: Page Style Guidelines
---

In general, we follow the European Commission's [Web Writing Style Guide](https://wikis.ec.europa.eu/display/WEBGUIDE/02.+Web+writing+guidelines) and their more detailed [English Style Guide](https://commission.europa.eu/system/files/2023-11/styleguide_english_dgt_en.pdf). 
Below are the style guidelines specific to the pages in RSQKit (adapted from [RDKkit Style Guide](https://rdmkit.elixir-europe.org/style_guide)). 

## General style and tone

* Keep the tone informal and use "you". Imagine you were explaining something verbally to someone - how would you say it?
* Use short, active sentences and short paragraphs (3-4 sentences).
* Make use of headings and bullet points to break text up so it is easy to scan.
* Remember that the site is there to help people, so make it clear to the readers how the information can benefit them.
* Try to make the content concise, avoid repeating things that have been well described and documented elsewhere - instead point out to these external resources.
* Use the words your readers would use. Think of the terms they would use when searching for their problem, and use those terms.

## Page templates
  
We provide page templates for certain content types in RSQKit to keep the structure of such pages consistent. 
If in doubt when creating new content, have a look at other existing content of the same type and try to mimic that.
  
* [Task page template](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/your_tasks/TEMPLATE_your_tasks.md) for pages addressing common issues or describing commonly performed tasks around research software quality. For an example - see ["How to make a good README" task page](https://everse.software/RSQKit/how_to_make_a_good_readme).

  
## Content

* **Acronyms:** spell them out the first time they are mentioned.
* **Ampersands (&):** do not use these in the main text or headings. It is fine to use them in menus if you need to save space for menu items.
* **Capitals:** do not use all capitals for emphasis or in headings (unless it is contained in the name of a resource).
* **Data:** treat it as singular ("data is..."). (Whether "data" is singular or plural is contentious - see the [Wikipedia article](https://en.wikipedia.org/wiki/Data_(word)) and this [Guardian article](https://www.theguardian.com/news/datablog/2010/jul/16/data-plural-singular).)
* **Dates:** use Wednesday 7 July 2021 (not Wednesday 7th July 2021, or other variations).
* **Datasets:** not "data sets".
* **Email:** not "e-mail".
* **Email addresses:** spell these out and make the email address the link, e.g. [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org). Do not hide the email address behind a word or phrase like "contact us".
* **Etc.** should be avoided. Try using ‘for example’ or ‘such as’ or ‘including’ at the start of a listing. If etc. is used, put a comma before it if it is in a list, like "A, B, etc.". 
* **Gender:** avoid using gender-specific words like "he" or "she".
* **Headings:**
   * Only the first word is capitalised unless other words are proper nouns.
   * Headings must be hierarchical. They must go down in order (level one, level two, level three) and not skip a level. It is fine to skip levels when moving back up, e.g. you can skip from level four to level two.
* **-ise/-ize:** use the "-ise" form.
* **Life cycle:** two separate words (not "lifecycle").
* **Links:** make the link text say where the link goes, e.g. "the Contribute page", not "click here". Avoid using the url as the link text.
* **Lists:** 
   * _A list of short items_: introduce with a colon, start each bullet point with a capital and don't use punctuation at the end of each bullet point:
      * Item 1
      * Item 2
    * _A list of longer items following an incomplete introductory sentence (e.g. a sentence ending in a colon)_: each item ends with a semi-colon and the final item ends with a full stop. Do not capitalise the first letter of each item, e.g. This is the first part of a sentence that includes:
       * a longer item 1;
       * a longer item 2;
       * a longer item 3.
    * _A list following a complete sentence (with a full stop)_: each item ends with a full stop, and each point begins with a capital letter, e.g. This a complete sentence.
       * This is item 1 of the list.
       * This is item 2 of the list.
       * This is item 3 of the list.
* **Numbers:** spell the numbers one to ten out. After that, write the numbers (11, 12, 13, etc.).
* **Quotations:** use double quotes for quotations and single quotes for quotes within quotes.
* **That/which:** use "that" when you are defining something and "which" when you are adding extra information about it e.g.:
 * "The cat that was on the table suddenly got up" is telling us which cat it was. It is important to the meaning of the sentence because you are not talking about any cat, just the cat on the table.
 * "The cat, which was sitting on the table, suddenly got up" is giving us extra information about the cat. The information is not necessary to understand the sentence. You can remove the clause, and the sentence will still be clear. Clauses starting with "which" usually begin with a comma.
* **Titles (the "title" in the front matter of pages):** only the first word, proper nouns and acronyms are capitalised.
* **Training:** training is an uncountable noun and cannot have a plural. You can write "training courses" and "training materials" but not "trainings".

## Page graphics

  * **White space:** make sure there is plenty of space so that the main elements stand out and the text does not appear overwhelming.
  * **Colours:** We recommend for graphs and tables where possible to take into account those who are colour blind. 
  * **Fonts:** Exo 2 is used for headings and main branding font, Open Sans for body text.
  * **Icons:** the icons used in the data life cycle diagram come from the [Noun Project](https://thenounproject.com/ELIXIRCommunications/kit/rdmkit/). We have a Pro license and the right to publish them without attribution. Other icons on this site are either desgined by Xènia Pérez Sitjà or come from [Font Awesome](https://fontawesome.com/).
  * **Illustrations:** use the colours listed above. The icons we use for illustrations come from the [Noun Project](https://thenounproject.com/ELIXIRCommunications/kit/rdmkit/). Please use these icons in any illustrations. If you need extra icons or any help with illustrations, [open a new issue](https://github.com/elixir-europe/rdmkit/issues) on GitHub or email [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org).
  * **Images:**
    * Do not use images to display text.
    * Include an 'alt' attribute in images.
   
## Naming of files, tags, keywords, and navigation titles

* **Markdown file names:**
  * Do not contain spaces or special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are unique across the website.
  * Are lowercase, except for acronyms.
* **Tags for tools, resources and pages:**
  * Do not contain special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are lowercase, except for acronyms.
  * Are short if possible but distinguishable from existing tags.
  * Can contain spaces but this is not recommended
* **Keywords:**
  * Are lowercase.
  * Can contain spaces.
* **Titles in the navigation side panel:**
  * First word and acronyms capitalised.
  * Should contain the same words as the filename where this title points to.
