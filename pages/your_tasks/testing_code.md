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
- Validation and verification: testing ensures the software's output is correct (validation) and that the software is built correctly and performs as required (verification).
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

- Testing helps identify issues with our code early in the development process, when fixing these issues is easier (compared to when software is released and/or deployed) -  saving time and money.
- Testing allows us to demonstrate to ourselves and others that our code does what we claim (by sharing our tests alongside our code, we allow others to verify our software for themselves).
- The act of writing tests encourages us to structure our code better (e.g. into a number of smaller individual functions) and results in a more readable, modular and maintainable codebase that is easier to extend or repurpose.
- Software testing improves the reusability of our code - well-written software tests capture the expected behaviour of our code and can be used alongside documentation to help other developers quickly make sense of our code. In addition, a well-tested codebase allows developers to experiment with new features safe in the knowledge that tests will reveal if their changes have broken any existing functionality.
- Software testing underpins the FAIR practices and improves software quality by giving us the confidence to engage in open research practices - if we are not sure that our code works as intended and produces accurate results, we are unlikely to feel confident about sharing our code with others.

## How do we test our code?

There are many different types of software testing.

### Manual testing

Manual (or informal) testing is performed by a person who checks the functionality by manually executing the test cases.
For example, by running one function or a piece of code at a time and checking that they behave as expected. 
As input to our code/function we are testing, we typically use some input values for which we know what the correct return value should be.

We can and should extensively test our software manually - it is quick, easy and provides immediate feedback, and is particularly useful as we draft our code for the first time.
Manual testing is also well-suited to testing aspects such as graphical user interfaces and reconciling visual outputs against inputs. 
However, even with a good test plan, manual testing is prone to error, is very time consuming and suffers from certain other limitations:

- We must reload our functions and repeat our tests each time we change our code
- We must rely on memory to keep track of how we have tested our code, e.g. what input values we tried
- We must rely on memory to keep track of which functions (parts of the code) have been tested and which have not (informal testing may work well on smaller pieces of code but it becomes unpractical for a large codebase)
- Once we close our development environment, we lose all the manual test scenarios we have tried

Another style of testing is automated testing, where we write code that tests the functions of our software and stays and can be shared together with our software. 
Since computers are very good and efficient at automating repetitive tasks, we should take advantage of this wherever possible.

### Automated testing

Automated testing involves using tools or scripts to execute test cases automatically.

There are three main types of automated tests:

- [**Unit tests**][unit-testing] are tests for fairly small and specific units of functionality, e.g. determining that a particular function returns output as expected given specific inputs. Unit tests focus on testing individual functions in isolation ensuring that each small part of the software performs as intended.
- [**Integration tests**][integration-testing] work at a higher level and test functional paths through your code verifying that different modules work together. For example, given some specific inputs, a set of interconnected functions across a number of modules (or the entire code) produce the expected result. These are particularly useful for exposing faults in how functional units interact.
- **End-to-end** or [**system tests**][system-testing] are a special type of integration testing which checks that a program as a whole behaves as expected and tests the complete system to ensure it meets the specified requirements.

### Other Software Testing Tactics

There are many other [software testing tactics][software-testing-tactics] beside manual and automated testing.
A few examples are the following:
- [**Regression tests**][regression-testing] make sure that your software’s output has not changed over time, for example after making changes your code to add new functionality or fix a bug. They involve checking whether a program or part of a program still generates the same results after changes have been made.
- [**Functional tests**][functional-testing] verify functional aspects of the code, i.e. the correct functioning of some code unit, while [**non-functional tests**][non-functional testing] refer to the non-functional aspects of the code, e.g. performance, scalability, security, usability, etc.
- **White-box tests** are written knowing the implementation of a code unit, while **black-box tests** are written disregarding the implementation of a code unit.
- **Acceptance tests** verify that specific needs and requirements of users and business processes are met. Acceptance critera are defined by users or customers which determine whether to accept the system.
- **Performance tests** execute the system under specific load and determines how the system performs in terms of responsiveness and stability.
- **Usability tests** verify whether a user interface is easy to use and understand. 
- **Security tests** verify that the software prevents the intrusion by hackers.

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

[software-testing-tactics]: https://en.wikipedia.org/wiki/Software_testing_tactics
[unit-testing]: https://en.wikipedia.org/wiki/Unit_testing
[integration-testing]: https://en.wikipedia.org/wiki/Integration_testing
[functional-testing]: https://en.wikipedia.org/wiki/Functional_testing
[non-functional testing]: https://en.wikipedia.org/wiki/Non-functional_testing
[system-testing]: https://en.wikipedia.org/wiki/System_testing
[regression-testing]: https://en.wikipedia.org/wiki/Regression_testing
