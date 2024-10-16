---
title: Testing Code
search_exclude: false
description: Explains useful aspects about why and how to test code.
contributors: ["Aleksandra Nenadic", "Christian Hüser", "Fredo Erxleben"]
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

### Description

Code testing is the process of evaluating software code to identify errors or issues, ensuring that the software behaves as expected. 
It is an essential part of software development, aiming to verify that the code functions correctly, meets specified requirements, and performs as intended in various scenarios.

### Considerations

Key aspects of code testing include:

- Detecting bugs: testing helps identify problems in the code, such as logical errors, syntax mistakes, or runtime issues.
- Validation and verification: testing ensures the software's output is correct (validation) and that the software is built correctly and performs as required (verification).
- Ensuring quality: testing verifies that the software meets the quality standards.
- Improving code: testing helps developers refactor code and optimise it by identifying parts that can be improved.

### Solutions

- Various [**software testing**][software-testing] methods and tools to ensure that your software functions in a way that is intended and defined by its specification.

## Why is it important to test our code?

### Description

Being able to demonstrate that a process generates the right results is important in any field of research, whether it is software generating those results or not. 
So when writing software we need to ask ourselves some key questions:

- Does the code we develop work the way it should do?
- Can we (and others) verify these assertions for themselves?
- Perhaps most importantly, to what extent are we confident of the accuracy of results that software produces?

If we are unable to demonstrate that our software fulfills these criteria, why would anyone use it?

### Considerations

Having well-defined tests for our software is crucial for several reasons, as it directly impacts the quality, functionality, reliability as well as reusability of our software.

- Testing helps identify issues with our code early in the development process, when fixing these issues is easier (compared to when software is released and/or deployed) -  saving time and money.
- Testing allows us to demonstrate to ourselves and others that our code does what we claim (by sharing our tests alongside our code, we allow others to verify our software for themselves).
- The act of writing tests encourages us to structure our code better (e.g. into a number of smaller individual functions) and results in a more readable, modular and maintainable codebase that is easier to extend or repurpose.
- Software testing improves the reusability of our code - well-written software tests capture the expected behaviour of our code and can be used alongside documentation to help other developers quickly make sense of our code. In addition, a well-tested codebase allows developers to experiment with new features safe in the knowledge that tests will reveal if their changes have broken any existing functionality.
- Software testing underpins the FAIR practices and improves software quality by giving us the confidence to engage in open research practices - if we are not sure that our code works as intended and produces accurate results, we are unlikely to feel confident about sharing our code with others.

### Solutions

- [**Software Quality Assurance**][software-quality-assurance] - a systematic process that ensures the quality of software by monitoring its development, testing, and maintenance and ensures that the final software product meets the specified requirements and quality standards.
- **Quality Gates** - in time in a software development life cycle at which the quality is checked and the software develoment process does not pass these gates if the quality is not sufficient. Software testing can be a quality gate, i.e. the software should not be accepted and used unless it is possible to demonstrate its software quality by software tests.

## How do we test our code?

### Description

There are many different [software testing tactics][software-testing-tactics].

#### Manual testing

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

#### Automated testing

Automated testing involves using tools or scripts to execute test cases. 
They can be further automated by using automated testing tools and frameworks (e.g., JUnit, pytest, Selenium) to run tests frequently and consistently.

There are three main types of automated tests:

- [**Unit tests**][unit-testing] are tests for fairly small and specific units of functionality, e.g. determining that a particular function returns output as expected given specific inputs. Unit tests focus on testing individual functions in isolation ensuring that each small part of the software performs as intended.
- [**Integration tests**][integration-testing] work at a higher level and test functional paths through your code verifying that different modules work together. For example, given some specific inputs, a set of interconnected functions across a number of modules (or the entire code) produce the expected result. These are particularly useful for exposing faults in how functional units interact.
- **End-to-end** or [**system tests**][system-testing] are a special type of integration testing which checks that a program as a whole behaves as expected and tests the complete system to ensure it meets the specified requirements.

#### Other Software Testing Tactics

There are many other software testing tactics beside manual and automated testing.
A few examples are the following:
- [**Regression tests**][regression-testing] make sure that your software’s output has not changed over time, for example after making changes your code to add new functionality or fix a bug. They involve checking whether a program or part of a program still generates the same results after changes have been made.
- [**Functional tests**][functional-testing] verify functional aspects of the code, i.e. the correct functioning of some code unit, while [**non-functional tests**][non-functional-testing] refer to the non-functional aspects of the code, e.g. performance, scalability, security, usability, etc.
- [**White-box tests**][white-box-testing] are written knowing the implementation of a code unit, while [**black-box tests**][black-box-testing] are written disregarding the implementation of a code unit.
- [**Acceptance tests**][acceptance-testing] verify that specific needs and requirements of users and business processes are met. Acceptance critera are defined by users or customers which determine whether to accept the system.
- [**Performance tests**][performance-testing] execute the system under specific load and determines how the system performs in terms of responsiveness and stability.
- [**Usability tests**][usability-testing] verify whether a user interface is easy to use and understand. 
- [**Security tests**][security-testing] verify that the software prevents the intrusion by hackers.

### Considerations

- Depending on the context and purpose of the software tests different **software testing tactics** can be chosen.
- The **Test-First Policy** in [**Test Driven Development**][test-driven-development] is one promising approach to ensure to the testability of software under test (SUT).
  Tests are written just before writing the code that make the tests pass.
  By following this approach the software is written in and refactored into small testable units right from the start.
- The **F.I.R.S.T. Principles of Testing** describe beneficial properties of software tests:
  - *Fast*:
    - Tests should run fast to ensure rapid feedback to detect errors fast and early.
  - *Isolated/Independent*:
    - Tests should focus on one particular responsibility or aspect in a software unit, other factors should not influence the result of the tests.
  - *Repeatable*:
    - Tests should be repeatable and deterministic. The result should not change with different environments.
  - *Self-validating/Self-checking*:
    - Tests should be automated and no manual steps should be made to check the test results. 
  - *Thorough/Timely*:
    - Tests should not only test the happy paths and not only aim for 100% of statement coverage. On the other hand, tests should be written at the right point in time and according to the Test-First Policy.
- There are fundamental principles such as the **Software Testing Principles** that every tester should be aware of:
  - *Testing shows the presence of defects*:
    - On contrary, it does not show the absence of defects.
  - *Exhaustive Testing is not possible*:
    - In order to test all paths and states in a moderately large or complex software, you might be inclined to test all paths and states. This would most probably result in an almost close to infinite number of test cases, which renders this task impossible.
  - *Early Testing*:
    - Tests should be run early and often to give rapid feedback.
  - *Defect Clustering*:
    - Often defects tend to occur in clusters which means if you found a defect in one particular unit, it is very likely that you will find more defects there.
  - *Pesticide Paradox*:
    - Running the same tests abundantly will not give any further insights. It is important to add new test cases in order to find new defects.
  - *Testing is Context-Dependent*:
    - Depending on the software type, different software test approaches might be appropriate.
  - *Absence of Errors Fallacy*:
    - There is no moderatly large or complex software without defects.

### Solutions

- Write tests early and often - begin testing as early as possible in the development process as writing tests alongside code development helps catch defects sooner and reduces the cost of fixing them.
- Use a combination of testing types, if possible, but at least use unit testing to test individual functions or methods of your code in isolation to ensure they perform as expected.
- Use automated testing tools and frameworks (e.g., JUnit, pytest, Selenium) to run tests frequently and consistently - automating repetitive tests saves time and ensures tests are run consistently across different environments.
- Maintain a balance between automated and manual testing; use manual testing for exploratory or usability testing where human judgment is essential.
- Aim for high code coverage (percentage of the code that is tested) to reduce the likelihood of undetected bugs, but avoid focusing solely on achieving 100% coverage as some code may not be relevant to test (e.g. built-in functions for your programming language or functions imported from well-known and well-tested libraries) and test coverage of 100% does not mean that your code is bug-free. Prioritise testing of critical paths through your code, complex logic, edge cases, and parts of our code that carry the greatest “reputational risk”, i.e. that could affect the accuracy of your reported results.
- Write clear, understandable and independent tests - ensure test cases are easy to understand and maintain, use descriptive names for test functions and methods that clearly convey their purpose, and make each test independent (tests should not rely on the results or state of other tests to function correctly)
- Consider [**Software Testing Tactics**][software-testing-tactics] - choosing the right software testing tactics for your software and software quality criteria is essential for improving the software quality of your software

## How do we automate code testing?

### Description 

### Considerations 

### Solutions

- [**Test Automation**][test-automation]
  - Test automation frameworks are utilized to control the execution of tests and the comparison of actual outcomes with predicted outcomes.
- [**Continuous Integration**][continuous-integration]
  - Continuous Integration is the process of continuously integrating code into the mainline of your code developments and thereby automate the build of the software as well as the tests the software in so-called Continuous Integration pipelines.

## How do we automate tests of a Python application?

### Description 

### Considerations 

### Solutions

- [**Test Automation of Python applications with Pytest**][pytest]
  - Pytest is a popular test framework for [Python][python] applications.
- [**Continuous Testing of a Python application with GitHub Actions**][github-actions-for-python-tests]
  - GitHub Actions can be used to automate your software tests that utilize Pytest as the test framework for a Python application.
  - Your Pytest software tests are executed in a GitHub Actions CI pipeline and the results and feedback can be inspected in the CI job log.

## How to cite this page

To be added.

## Tools and resources <!-- do not delete this heading and write your text below it -->
List of relevant tools and resources for this task.

## References <!-- do not delete this heading and write your text below it -->
If work has been inspired or derived from other content (e.g., pages in RDMKit) make sure to reference it here. 

[software-testing]: https://en.wikipedia.org/wiki/Software_testing
[software-quality-assurance]: https://en.wikipedia.org/wiki/Software_quality_assurance
[software-testing-tactics]: https://en.wikipedia.org/wiki/Software_testing_tactics
[unit-testing]: https://en.wikipedia.org/wiki/Unit_testing
[integration-testing]: https://en.wikipedia.org/wiki/Integration_testing
[system-testing]: https://en.wikipedia.org/wiki/System_testing
[regression-testing]: https://en.wikipedia.org/wiki/Regression_testing
[functional-testing]: https://en.wikipedia.org/wiki/Functional_testing
[non-functional-testing]: https://en.wikipedia.org/wiki/Non-functional_testing
[white-box-testing]: https://en.wikipedia.org/wiki/White-box_testing
[black-box-testing]: https://en.wikipedia.org/wiki/Black-box_testing
[acceptance-testing]: https://en.wikipedia.org/wiki/Acceptance_testing
[performance-testing]: https://en.wikipedia.org/wiki/Software_performance_testing
[usability-testing]: https://en.wikipedia.org/wiki/Usability_testing
[security-testing]: https://en.wikipedia.org/wiki/Security_testing
[test-driven-development]: https://en.wikipedia.org/wiki/Test-driven_development
[test-automation]: https://en.wikipedia.org/wiki/Test_automation
[continuous-integration]: https://en.wikipedia.org/wiki/Continuous_integration
[python]: https://www.python.org
[pytest]: https://docs.pytest.org
[github-actions-for-python-tests]: https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#testing-your-code
