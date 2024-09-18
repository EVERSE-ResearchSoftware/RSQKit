---
title: How to make your code readable
description: Good practices to make your code readable
contributors: ["Aleksandra Nenadic"]
page_id: readable_code
related_pages: []
---


## Why is it important to make your code readable?

**Code readability** contributes to the *accessibility* and *reusability* of your code (the "A" and "R" in the [FAIR reseach software principles][fair-rs-principles][^1]) - 
once people freely, legally and easily obtain a copy your software - they need to be able to read and understand it to reuse and extend it. 
So, readable code helps create more reusable scientific software and can empower collaboration between researchers.

In order to develop readable code, we should ask ourselves: "If I re-read this piece of code in fifteen days or one year, will I be able to understand 
what I have done and why?" 
Or: "If a new person who has just joined the project reads my code, will they be able to understand what I have written?"

In addition, software requirements will likely change over time because software is dynamic in nature. 
When these requirements change, a developer (who is not necessarily the same person who wrote the original code) needs to make changes to the software
to satisfy these new and emerging needs. 
They do this by reading the original code to understand it and identify what needs to change. 
Readable code facilitates the the process of understanding the code, the evolution of the codebase, and saves future developers' time and effort.

## What practices are there to help me improve the readability of my code?

One of the most important things we can do to make sure our code is readable by others (and ourselves a few months down the line) is to make sure that it is descriptive, 
cleanly and consistently formatted and uses sensible, descriptive names for variable, function and module names. 
In order to help us format our code, we generally follow guidelines known as a style guide. 
A style guide is a set of conventions that we agree upon with our colleagues or community, to ensure that everyone contributing to the same project is producing code which 
looks similar in style. 
While a group of developers may choose to write and agree upon a new style guide unique to each project, in practice many programming languages have a single style guide 
which is adopted almost universally by the communities around the world. 

### Considerations

* Code is read much more often than it is written - style guidelines are intended to improve the readability of code and make it consistent across the wide spectrum of code
* Consistency with the style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important. However, know when to be inconsistent - sometimes style guide recommendations are just not applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best.
* 


### Solutions

- Choose function and variable names that help explain the purpose of the function or variable
- Write informative comments and docstrings for functions to provide more detail about what the code and is doing
- Organise code into reusable and modular functions that achieve a singular purpose and are more easier to understand, test and reuse
- Use standard and well-tested libraries for common tasks (e.g. reading and writing data in standard formats) over reimplementing functionality in custom, less readable and more error-prone code 


## Tools and resources

| Tool or resource                                                                | Description                                                                |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [PEP 8 style guide for Python][pep8]                                            | Python Enhancement Proposal 8, Style Guide for Python Code                 |
| [Python code style conventions](https://carpentries-incubator.github.io/python-intermediate-development-earth-sciences/15-coding-conventions/index.html) from ["Intermediate Research Software Development" course][intermediate-rs-dev]                            |  A chapter on Python Code Style Conventions | 
| [FAIR Reseach Software Principles][fair-rs-principles] | 

In Python, although we do have a choice of style guides available, the PEP 8 style guide is most commonly used. PEP here stands for Python Enhancement Proposals; PEPs are design documents for the Python community, typically specifications or conventions for how to do something in Python, a description of a new feature in Python, etc.

## How to cite this page

To be added.


## Credit

The contents of this page have been inspired by the ["Tools and Practices for FAIR Research Software" course][fair-rs][^1] 
and the ["Intermediate Research Software Development" course][intermediate-rs-dev][^2] developed by the [Software Sustainability Institute][ssi].

      
## References
[^1]: [Barker, M., Chue Hong, N.P., Katz, D.S. et al. Introducing the FAIR Principles for research software. Sci Data 9, 622 (2022). https://doi.org/10.1038/s41597-022-01710-x]

[fair-rs]: https://carpentries-incubator.github.io/fair-research-software
[ssi]: https://www.software.ac.uk/
[fair-rs-principles]: https://www.nature.com/articles/s41597-022-01710-x
[fair-rs]: https://carpentries-incubator.github.io/fair-research-software
[intermediate-rs-dev]: https://carpentries-incubator.github.io/python-intermediate-development/
[pep8]: https://peps.python.org/pep-0008/
