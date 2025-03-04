---
title: Writing readable code
description: How to write code readable and understandable by others
contributors: ["Aleksandra Nenadic"]
page_id: readable_code
related_pages:
  your_tasks: []
---


## Why is it important to make your code readable?

### Description

**Code readability** contributes to *reusability* of code (the "R" in the [FAIR research software principles][fair-rs-principles][^1]) - 
once people obtain a copy of your software, they need to be able to understand it to reuse and extend it. 

In order to develop readable code, we should ask ourselves: 

* if I re-read this piece of code in fifteen days or in one year, will I be able to understand what I have done and why? 
* if a new person joins the project and looks at my code, will they be able to understand what I have written?

In addition, software requirements will likely change over time because software is dynamic in nature. 
When these requirements change, a developer (who is not necessarily the author of the original code) needs to make 
changes to the software to satisfy these new and emerging needs. 
They do this by reading the original code to understand it and identify what needs to change. 

Readable code facilitates the process of understanding the code, the evolution of the codebase, 
and saves future developers' time and effort.

### Considerations

- Code is read much more often than it is written - [some sources][code-is-read-more-than-it-is-written] report that in a typical project the code 
"read vs write" ratio is 7:1, i.e. code is read seven times more than it is written.
- Readable code is easier to understand, maintain, debug and extend (reuse) - saving time and effort.
- Readable code can also make it better and more secure in a way, as it is easier for reviewers to pick out errors.


### Solutions

What practices are there to help us improve code readability?

One of the most important things we can do to make sure our code is readable by others (and ourselves a few months down 
the line) is to make sure that it is commented, cleanly and consistently formatted and uses sensible, 
descriptive names for variable, function, class and module names. 

In order to help us format our code, we generally follow guidelines known as a style guide. 
A style guide is a set of conventions that the community of developers or colleagues on a project agree upon, 
to ensure that everyone contributing to the same project is producing code which looks similar in style. 
While a group of developers may choose to write and agree upon a new style guide unique to each project, 
in practice many programming languages have a single style guide which is adopted almost universally by the communities 
around the world. 

For example, see {% tool "pep8" %} (style guide for Python) or {% tool "r-language-style-guide" %}.
{% tool "google-programming-style-guide" %} offers recommendations for style guides for various programming languages, 
including Python, Java, R, C++, and Shell.

Another good practice to help readability is to [create code that is modular][modular-code] - structured and split into 
small, reusable functions that are easier to read, understand and test.
Functions with a common goal are further grouped into reusable libraries and packages. 
Use the [common code patterns][design-patterns] for creating software - [design patterns][design-patterns-book] 
describe a relatively small, well-defined aspect (i.e. functionality) of code intended to leverage an 
existing concept/solution rather than re-invent it. 
This can decrease the time to develop software and increase the quality of the resulting code and its readability.

Expanding on the code structure theme, following conventions on consistent and informative directory structure for your 
projects will ensure people will immediately know where to find things within your project, especially helpful for 
long-term research projects or when working in teams. 
The directory structure for organising your research software project (or research projects in general) involves 
creating a clear and logical layout for files and data, ensuring easy navigation, collaboration and reproducibility.

Here is the summary of some of the practices to follow to make your code more readable:

- Use consistent formatting - consistent indentation and spacing make code easier to understand and parse. 
- Break code into sections - use blank lines to separate different parts of your code, like classes and functions. 
- Use descriptive names for function, class and variable names that help explain their purpose.
- Keep lines short - avoid long lines, and instead write blocks of lines that are horizontally short and vertically long. 
- Use indentation to show the hierarchy of your code and mark the beginning and end of control structures. 
- Write informative comments and docstrings for functions to provide more detail about what the code and is doing, transmit understanding and context 
- Follow a code style guide for your programming language that is agreed upon by the community and other programmers will find easy to read. 
Style guidelines are intended to improve the readability of code and make it consistent across the wide spectrum of code. 
Consistency with a style guide is important but consistency within a project or a module is more important - if you 
are joining an existing project, look at the existing code and make sure to adopt whatever practices are already in place.
- Follow [guidelines and conventions](https://carpentries-incubator.github.io/fair-research-software/07-code-structure.html#directory-structure-for-software-projects)
  on consistent and informative directory structure for your software or research projects - this way, people will immediately know where to find things within your project
- Automate style checks to help ensure your code is consistent. Many modern Integrated Development Environments (IDEs), such as {% tool "vscode" %}, {% tool "pycharm" %}, {% tool "rstudio" %} or {% tool "eclipse" %}, 
have built-in support for checking conformance to style conventions and they will warn you when you deviate or even autocorrect things for you.
- Use {% tool "code-linters" %} - static code analysis tools (such as {% tool "pylint" %}) used to flag code consistency issues, stylistic errors, suspicious language constructs, and even programming errors and bugs.
- Organise code into reusable and modular functions that achieve a singular purpose and are more easier to understand, test and reuse.
- Use existing and well-tested libraries or packages for common functionality and tasks (e.g. reading and writing data in standard formats) to avoid duplication and reimplementing
functionality in custom, more error-prone code.

      
## References
[^1]: Barker, M., Chue Hong, N.P., Katz, D.S. et al. Introducing the FAIR Principles for research software. Sci Data 9, 622 (2022). [https://doi.org/10.1038/s41597-022-01710-x](https://doi.org/10.1038/s41597-022-01710-x)

[fair-rs]: https://carpentries-incubator.github.io/fair-research-software
[ssi]: https://www.software.ac.uk/
[fair-rs-principles]: https://www.nature.com/articles/s41597-022-01710-x
[fair-rs]: https://carpentries-incubator.github.io/fair-research-software
[intermediate-rs-dev]: https://carpentries-incubator.github.io/python-intermediate-development/
[pep8]: https://peps.python.org/pep-0008/
[r-guidelines]: https://google.github.io/styleguide/Rguide.html
[code-linters]: https://en.wikipedia.org/wiki/Lint_%28software%29
[modular-code]: https://best-practice-and-impact.github.io/qa-of-code-guidance/modular_code.html
[design-patterns-book]: https://refactoring.guru/design-pattern
[design-patterns]: https://en.wikipedia.org/wiki/Software_design_patterns
[code-is-read-more-than-it-is-written]: https://primalskill.blog/code-is-read-more-than-it-is-written

