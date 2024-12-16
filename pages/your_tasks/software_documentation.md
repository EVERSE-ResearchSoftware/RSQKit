---
title: Software documentation
description: How to write clear and useful software documentation for developers and end-users
contributors: ["Azza Gamgami"]
page_id: software_documentation
related_pages: [creating_readthedocs]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->

## How to craft effective software documentation?  <!-- example: how to version control my code? -->
<!-- What are the best practices for documenting software effectively?> 
 

### Description <!-- do not delete this heading and write your text below it -->

Software documentation is an essential part of the software development process, designed to provide clear communication between various stakeholders including developers, testers, users, and project managers. It helps align the expectations and goals of all parties, while also ensuring the software is easy to understand and use.

### Considerations <!-- do not delete this heading and write your text below it -->

* Software documentation should be clear, consistent, regularly updated, cover all key aspects, encourage feedback, and ideally be auto-generated.
* Each document should have a distinct purpose.
* There are two types of software documentation:
   * Product documentation targets both internal and external users (e.g., Requirements Documents, often in ReadMe files; Source Code Documentation, which includes code; End-User Documentation, like user guides and API references for usability).
   * Process documentation is primarily intended for the development team (e.g., Plans; Progress Reports track progress; Working Papers capture ideas and notes from the team).


### Solutions <!-- do not delete this heading and write your text below it -->

***Understand the Purpose and Audience***

* Define why the document is being created and who will be using it. 
* Understanding the purpose allows you to tailor the content accordingly.
* For example:
  * A developer-facing document will need in-depth technical details.
  * An end-user guide should focus on usability and clarity, offering step-by-step instructions.
 

* Create personas to represent your audience for better-targeted technical content, it helps categorize your help documentation.

***Write Comments as You Code***
 
* Use integrated development environments (IDEs) that automatically generate documentation strings, such as [Eclipse](https://eclipseide.org/),[Pycharm](https://www.jetbrains.com/fr-fr/pycharm/) for Python and [Visual Studio Code](https://code.visualstudio.com/) using extensions like [JSDoc](https://jsdoc.app/) or [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).
* Ensure you strike a balance in the amount of commenting.

***Include Examples (and Lots of Them)***

* Examples help users understand and experiment with the software. 
* Unlike with comments, there’s no such thing as too many examples if they showcase different aspects of your software. 
* If your documentation becomes too cluttered, consider moving examples to a dedicated section. 
* For instance, [Keras](https://github.com/keras-team/keras/tree/master/examples)  provides example scripts to demonstrate its functionalities along with a README file that outlines.

***Include a Quickstart Guide***

* A quickstart guide enables users to move quickly from idea to experimentation. 
* This can take the form of an example, tutorial, or video. 
* For instance, [the quickstart guide for TPOT](https://link.springer.com/chapter/10.1007/978-3-319-31204-0_9)  includes an animated GIF and minimal code snippets.

***Include a README File with Basic Information***

* The README acts as a homepage for your project and should be easily readable. 
* It include a link to the full documentation. 
* [See more details about the README file](link to "how create a good readme?" page)

***Include a Help Command for Command Line Interfaces***

* An effective way to document CLIs is to implement a `help` command that provides instructions on how to use the software. 
* This approach ensures that users don’t have to search for documentation to complete basic tasks. 
* The help command should cover 
  * Usage instructions (how to execute the command).
  * Relevant subcommands 
  * Options and/or arguments
  * Applicable environment variables
  * And ideally, some examples. 

* In Python, tools like [Click](https://click.palletsprojects.com/en/8.1.x/)  can assist you not only in creating your help command but also in building your interface.

* A great example of a CLI is the one included in [Magic-BLAST](https://ncbi.github.io/magicblast/). It features a concise help command, `-h` which offers : 
  * Information about the tool and its usage.
  * Instructions for accessing the help documentation.

***Version Control Your Documentation***

* Since your documentation is a crucial component of your code, it should also be under version control. 
* Store your documentation within your [Git repository](https://docs.github.com/en/get-started/using-git/about-git#about-repositories) alongside your other files. This approach allows you to access your documentation at any stage of the project’s history. 
* Services like [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.org) and [Zenodo](https://zenodo.org/) facilitate this process by archiving a fully rendered version of your documentation each time you release a new version of your software.
* Here are details about [how to create a readthedocs page](https://everse.software/RSQKit/creating_readthedocs). 

* A noteworthy example of a bioinformatics library effectively managing version control for its documentation is [khmer](https://github.com/dib-lab/khmer/). This library features a comprehensive changelog that details new features, bug fixes (categorized based on relevance to users or developers), known issues, and a list of contributors for each release . 



***Fully Document Your Application Programming Interface (API)*** 

* Your API documentation should be complete and accessible, serving as a reference for users. 
* Maintaining a consistent style in your API documentation is crucial. 

* [The Google style guide](https://google.github.io/styleguide/) offers recommendations for API documentation across various programming languages, including Python, Java, R, C++, and Shell. 

***Use Automated Documentation Tools***

* While no software can completely handle your documentation needs, several tools can significantly ease the process:
* Tools like [Sphinx](https://www.sphinx-doc.org/en/master/) and [Doxygen](https://www.doxygen.nl/) can generate documentation in multiple formats (HTML, PDF) and automatically extract comments from your codebase.

* [MkDocs](https://www.mkdocs.org/) enable the creation of professional-looking documentation websites using Markdown, making navigation easy for users.

* Tools such as [Swagger](https://swagger.io/) automatically generate interactive API documentation, providing user-friendly interfaces for developers.

* [Roxygen](https://github.com/r-lib/roxygen2) and [JSDoc](https://jsdoc.app/) simplify the process of generating documentation from annotated code in R and JavaScript, respectively.

* Please find a more comprehensive list of the documentation tools provided [below](#tools-and-resources).


***Write Error Messages That Provide Solutions or Point to Your Documentation***

* Error messages should clearly state :
  * What went wrong
  * The state of the software 
  * When the error occurred
  * How to fix it or where to find relevant information. 
  
* For example, instead of a vague error message, provide specifics that help users troubleshoot.

***Tell People How to Cite Your Software***

* Ensure that your documentation includes clear instructions on how to cite your work.
* See [How to cite your code repository and maintain a Citation File (CFF)].



## How to cite this page <!-- do not delete this heading and write your text below it -->
 contributors, page URL. Last date of access.

## Tools and resources <!-- do not delete this heading and write your text below it -->
List of relevant tools and resources for this task.
| Tool or resource    | Description  |
| ------------------- | ------------ |
|[Sphinx](https://www.sphinx-doc.org/en/master/) | A documentation generator primarily designed for Python but compatible with any programming language. It reads comments in the code to create detailed API documentation. |
|[Roxygen](https://github.com/r-lib/roxygen2) |  A documentation generator specifically designed for R packages.          | 
| [MkDocs](https://www.mkdocs.org/) | A documentation generator from Markdown files. |
| [Doxygen](https://www.doxygen.nl/) | A documentation generator from annotated source code in multiple programming languages. |
| [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.org) | A platform that automatically rebuilds documentation with each code update. |
| [Doctest](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html)  |  A Sphinx extension that verifies code examples in documentation to ensure they work as described. |
|  [Napoleon](https://github.com/sphinx-contrib/napoleon)| A Sphinx extension that enables support for Google and NumPy style docstrings to generate API documentation. |
|[Swagger](https://swagger.io/)|A tool for generating interactive documentation for RESTful APIs. |
|[Click](https://click.palletsprojects.com/en/8.1.x/)|A library for creating user-friendly command-line interfaces (CLIs), enabling structured commands and automatic help generation. |
|[Zenodo](https://zenodo.org/)|Zenodo supports version control for documentation by archiving and storing different versions of project’s documentation.|
|[khmer](https://github.com/dib-lab/khmer/)|A library that offers a comprehensive changelog detailing features, bug fixes, known issues, and contributors, along with accessible documentation for previous versions. |
|[Google style guide]( https://google.github.io/styleguide/)|The Google style guide offers comprehensive recommendations for maintaining consistency in API documentation across multiple programming languages, such as Python, Java, R, C++, and Shell.| 
|[Eclipse](https://eclipseide.org/)              | IDE offering features to generate Javadoc comments for Java classes and methods based on their signatures.
| [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) | A powerful IDE for Python development, featuring intelligent code assistance and built-in documentation generation. |
| [Visual Studio Code](https://code.visualstudio.com/) | A popular code editor that supports various languages and allows the use of extensions for documentation generation. |
| [JSDoc](https://jsdoc.app/)                   | An extension to generate documentation from comments in JavaScript code.                              |
| [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) | An extension for Visual Studio Code that automatically generates docstrings for Python functions and classes.      |

## Credit <!-- do not delete this heading and write your text below it -->

The contents of this page have been inspired by
* [Ten Simple Rules for documenting scientific software](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301674/). [[1]](#references)
* [Best Practices for Scientific Computing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/pdf/pbio.1001745.pdf). [[2]](#references)
* [Ten Simple Rules for Taking Advantage of Git and GitHub](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947). [[3]](#references)
* [How to Write Software Documentation in 7 Simple Steps](https://technicalwriterhq.com/documentation/software-documentation/how-to-write-software-documentation/)

## References
1. [Lee B. D., Ten Simple Rules for documenting scientific software](https://doi.org/10.1371/journal.pcbi.1006561)
2. [Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P.Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)
3. [Perez-Riverol Y, Gatto L, Wang R, Sachsenberg T, Uszkoreit J, Leprevost FdV, et al. Ten Simple Rules for Taking Advantage of Git and GitHub](https://doi.org/10.1371/journal.pcbi.1004947)

