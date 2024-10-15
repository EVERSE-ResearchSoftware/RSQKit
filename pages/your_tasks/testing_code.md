---
title: Testing Code
search_exclude: false
description: 
contributors: ["Aleksandra Nenadic", "Christian Hüser"]
page_id: testing_code
related_pages: []
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---

## What is code testing?

Code testing is the process of evaluating software code to identify errors or issues, ensuring that the software behaves as expected. 
It is an essential part of software development, aiming to verify that the code functions correctly, meets specified requirements, and performs as intended in various scenarios.

Key aspects of code testing include:

- Detecting bugs: testing helps identify problems in the code, such as logical errors, syntax mistakes, or runtime issues.
- Validation and verification: ensures the software's output is correct (validation) and that the software is built correctly and performs as required (verification).
- Ensuring quality: testing verifies that the software meets the quality standards.
- Improving code: testing helps developers refactor code and optimise it by identifying parts that can be improved.

## Why is it important to test our code?

Being able to demonstrate that a process generates the right results is important in any field of research, whether it is software generating those results or not. 
So when writing software we need to ask ourselves some key questions:

- Does the code we develop work the way it should do?
- Can we (and others) verify these assertions for themselves?
- Perhaps most importantly, to what extent are we confident of the accuracy of results that software produces?

If we are unable to demonstrate that our software fulfills these criteria, why would anyone use it? 
Having well-defined tests for our software is crucial for several reasons, as it directly impacts the quality, functionality, reliability as well as reusability of our software.

- Testing helps identify issues with our code early in the development process, when fixing these issues is easier and less costly (compared to when software is released and/or deployed).
- Testing allows us to demonstrate to ourselves and others that our code does what we claim (by sharing our tests alongside our code, we allow others to verify our software for themselves).
- The act of writing tests encourages us to structure our code better (e.g. into a number of smaller individual functions) and results in a more readable, modular and maintainable codebase that is easier to extend or repurpose.
- Software testing improves the reusability of our code - well-written software tests capture the expected behaviour of our code and can be used alongside documentation to help other developers quickly make sense of our code. In addition, a well-tested codebase allows developers to experiment with new features safe in the knowledge that tests will reveal if their changes have broken any existing functionality.
- Software testing underpins the FAIR practices and improves software quality by giving us the confidence to engage in open research practices - if we are not sure that our code works as intended and produces accurate results, we are unlikely to feel confident about sharing our code with others.

### Considerations <!-- do not delete this heading and write your text below it -->

* [Structured in bullet points](style_guide#text) as much as possible, detailing things to consider about this problem in order to be able to find the right solution.

### Solutions <!-- do not delete this heading and write your text below it -->

By using [bullet point style](style_guide#text) as much as possible, try to describe when, why and for what is best to use a specific tool or resource. 
Avoid making long list of links to tools and resources.
Make sure to add the tools and resources mentioned in the text in the main "tools and resources" table.

* Bullet point solution 1
  * Sub-point
* Bullet point solution 2

## How do we test our code?
 
### Description <!-- do not delete this heading and write your text below it -->

There are many different types of software testing.

- [Unit tests][unit-testing] focus on testing individual functions in isolation. They ensure that each small part of the software performs as intended.
  By verifying the correctness of these individual units, we can catch errors early in the development process.
- Integration tests check how different parts of the code (or a bigger software system) work together.
- Regression tests are used to ensure that new changes or updates to the codebase do not adversely affect the existing functionality.
  They involve checking whether a program or part of a program still generates the same results after changes have been made.
- End-to-end tests are a special type of integration testing which checks that a program as a whole behaves as expected.

### Considerations <!-- do not delete this heading and write your text below it -->
Same as above

### Solutions <!-- do not delete this heading and write your text below it -->


## How do we automate code testing?
 
### Description <!-- do not delete this heading and write your text below it -->
Same as above

### Considerations <!-- do not delete this heading and write your text below it -->
Same as above

### Solutions <!-- do not delete this heading and write your text below it -->


## How to cite this page <!-- do not delete this heading and write your text below it -->
 contributors, page URL. Last date of access.

## Tools and resources <!-- do not delete this heading and write your text below it -->
List of relevant tools and resources for this task.

## References <!-- do not delete this heading and write your text below it -->
If work has been inspired or derived from other content (e.g., pages in RDMKit) make sure to reference it here. 


[unit-testing]: https://en.wikipedia.org/wiki/Unit_testing
