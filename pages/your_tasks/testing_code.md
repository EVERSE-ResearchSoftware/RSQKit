---
title: Testing code
description: Why and how to test your code
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

### Description

[**Code testing**][software-testing] is the process of evaluating code to identify errors or issues, ensuring that the software behaves as expected. 
It is an essential part of software development, aiming to verify that the code functions correctly, meets specified requirements, and performs as intended in various scenarios.

### Considerations

Key aspects of code testing include:

- **Detecting bugs** - testing helps identify problems in the code, such as logical errors, syntax mistakes, or runtime issues.
- **Validation and verification** - testing ensures the software's output is correct (validation) and that the software is built correctly and performs as required (verification).
- **Ensuring quality** - testing verifies that the software meets the quality standards.
- **Improving code** - testing helps developers refactor code and optimise it by identifying parts that can be improved.

## Why is it important to test our code?

### Description

Being able to demonstrate that a process generates the right results is important in any field of research, whether it is software generating those results or not. 
So when writing software we need to ask ourselves some key questions:

- Does the code we develop work the way it should do?
- Can we (and others) verify these assertions for themselves?
- Perhaps most importantly, to what extent are we confident of the accuracy of results that software produces?

If we are unable to demonstrate that our software fulfils these criteria, why would anyone use it?

### Considerations

Having well-defined tests for our software is crucial for several reasons, as it directly impacts the quality, functionality, reliability as well as reusability of our software.

- Testing helps identify issues with our code early in the development process, when fixing these issues is easier (compared to when software is released and/or deployed) -  saving time and money.
- Testing allows us to demonstrate to ourselves and others that our code does what we claim (by sharing our tests alongside our code, we allow others to verify our software for themselves).
- The act of writing tests encourages us to structure our code better (e.g. into a number of smaller individual functions) and results in a more readable, modular and maintainable codebase that is easier to extend or repurpose.
- Software testing improves the reusability of our code - well-written software tests capture the expected behaviour of our code and can be used alongside documentation to help other developers quickly make sense of our code. In addition, a well-tested codebase allows developers to experiment with new features safe in the knowledge that tests will reveal if their changes have broken any existing functionality.
- Software testing underpins the FAIR practices and improves software quality by giving us the confidence to engage in open research practices - if we are not sure that our code works as intended and produces accurate results, we are unlikely to feel confident about sharing our code with others.

## What types of software tests exist? 

### Description

As we have already seen, testing code involves checking whether it behaves as expected. 
There are two main types of testing: [**functional testing**][functional-testing] and [**non-functional testing**][non-functional-testing]. 
Each type addresses different aspects of the software’s performance and quality and can be achieved via different tests. 
Both should be used when testing our software.

#### Functional testing

Functional testing focuses on verifying functional aspects of the code, i.e. that the software's features and functions work as specified. 
It ensures that the application behaves according to the requirements and produces the correct outputs for given inputs.

Common types of functional testing include:

- [**Unit tests**][unit-testing] are tests for fairly small and specific units of functionality, e.g. determining that a particular function returns output as expected given specific inputs. For example, testing a function that calculates the sum of two numbers to confirm it returns the correct value.
- [**Integration tests**][integration-testing] work at a higher level and test functional paths through your code verifying that different modules or components work together correctly. For example, testing the interaction between a web application’s frontend and backend.
- **End-to-end** or [**system tests**][system-testing] are a special type of integration testing which checks that the complete application as a whole behaves as expected and all features work and are meeting the specified requirements. For example, testing an entire login workflow, from user input to authentication and redirection to a welcome page to simulate a real world scenario.
- [**User acceptance tests**][acceptance-testing] verify that specific needs and requirements of users and business processes are met. Acceptance criteria are defined by users or customers which determine whether to accept the system.
For example: asking end-users to test a new feature before releasing it to a wider audience.
- [**Regression tests**][regression-testing] make sure that your software’s output has not changed over time, for example after making changes to your code to add new functionality or fix a bug. They involve checking whether a program or part of a program still generates the same results after changes have been made. For example: re-running tests after a bug fix to verify that no new issues were introduced.

Some [**software testing tactics**][software-testing-tactics] for functional testing include:

- **Black-box testing** tests the functionality of the software without knowledge of the internal code or structure.
- **White-box testing** tests with knowledge of the internal workings of the code, focusing on specific paths or conditions.

#### Non-Functional testing

Non-functional testing evaluates the software's quality attributes, such as performance, usability, security, and scalability. 
It focuses on how well the software operates rather than just checking if it produces the correct outputs.

Some types of non-functional testing are:

- [**Performance tests**][performance-testing] measures how the application performs in terms of responsiveness and stability under various conditions (e.g., load, stress, and volume testing).
For example testing how many simultaneous users a web application can handle before slowing down or crashing.
- [**Usability tests**][usability-testing] verify whether a user interface is easy to use and understand. For example observing how users navigate through an app and
identifying areas that cause confusion.
- [**Security tests**][security-testing] check for vulnerabilities in the system and ensure data and system are protected from intrusion by hackers.
For example checking for weak password policies.
- [**Compatibility tests**][compatibility-testing] ensures the software works across different environments (e.g., browsers, operating systems, devices).
- **Compliance with standards tests** are used if the software needs to meet certain regulatory or quality standards (e.g., accessibility standards for web applications).

### Considerations

Which testing approach should you use?

- Start with functional testing - this is typically done first to ensure that all the features work correctly according to the requirements. Functional testing is essential for any software, regardless of its type or usage.
- Add non-functional testing based on requirements - e.g. if the software needs to handle many users or heavy traffic, consider performance and load testing; if user experience is important, run usability testing;
if the software needs to run on multiple platforms, perform compatibility testing.
- Depending on the context and purpose of the software tests different [software testing tactics][software-testing-tactics] can be chosen.
- **Test-First Policy** in [**Test Driven Development**][test-driven-development] is one promising approach to ensure to the testability of software under test (SUT).
  Tests are written just before writing the code that make the tests pass.
  By following this approach the software is written in and refactored into small testable units right from the start instead of refactoring the code for testability afterwards when tests are added to already existing implementations.
- **F.I.R.S.T. Principles of Testing** describe beneficial properties of software tests:
  - *Fast*: tests should run fast to ensure rapid feedback to detect errors fast and early.
  - *Isolated/Independent*: tests should focus on one particular responsibility or aspect in a software unit, other factors should not influence the result of the tests.
  - *Repeatable*: tests should be repeatable and deterministic. The result should not change with different environments.
  - *Self-validating/Self-checking*: tests should be automated and no manual steps should be made to check the test results. 
  - *Thorough/Timely*: tests should not only test the happy paths and not only aim for 100% of statement coverage. On the other hand, tests should be written at the right point in time and according to the Test-First Policy.
- Fundamental **Software Testing Principles** to be aware of:
  - *Testing shows the presence of defects*: on the contrary, it does not show the absence of defects.
  - *Exhaustive Testing is not possible*: in order to test all paths and states in a moderately large or complex software, you might be inclined to test all paths and states. This would most probably result in an almost close to infinite number of test cases, which renders this task impossible.
  - *Early Testing*: tests should be run early and often to give rapid feedback.
  - *Defect Clustering*: often defects tend to occur in clusters which means if you found a defect in one particular unit, it is very likely that you will find more defects there.
  - *Pesticide Paradox*: running the same tests abundantly will not give any further insights. It is important to add new test cases in order to find new defects.
  - *Testing is Context-Dependent*: depending on the software type, different software test approaches might be appropriate.
  - *Absence of Errors Fallacy*: there is no moderately large or complex software without defects.
- Consider [**software testing tactics**][software-testing-tactics] - choosing the right software testing tactics for your software and software quality criteria is essential for improving the software quality of your software.
- Use [**Software Quality Assurance (SQA)**][software-quality-assurance] - a comprehensive and systematic process that ensures the quality of the overall software development process by monitoring its development, testing, and maintenance and ensures that the final software product meets the specified requirements and quality standards. [Software testing][software-testing] is a specific activity within the SQA process that involves evaluating software to identify discrepancies between expected and actual behaviour and testing code to find and fix defects, but checks other aspects of SQA too.
- Use **Quality Gates** - in software development these are predefined checkpoints or criteria that code or software must meet before moving to the next phase in the development lifecycle. They act as "gates" or approval points that help ensure quality at each stage of the development process. If the software fails to meet the requirements of a quality gate, it is not allowed to proceed, and corrective actions are needed.

## How do we test our code?

### Description

#### Informal testing

Informal testing is performed by a person who checks the functionality by manually executing the test cases which are then often discarded.
It is usually done ad-hoc and without any structured approach - for checking new features or fixes quickly.
For example, by running one function or a piece of code at a time and checking that they behave as expected. 
As input to our code/function we are testing, we typically use some input values for which we know what the correct return value should be.

We can and should extensively test our software manually - it is quick, easy and provides immediate feedback, and is particularly useful as we draft our code for the first time.
Manual testing is also well-suited to testing aspects such as graphical user interfaces and reconciling visual outputs against inputs. 
However, even with a good test plan, informal and manual testing is prone to error, is very time consuming and suffers from certain other limitations:

- We must reload our functions and repeat our tests each time we change our code
- We must rely on our memory to keep track of how we have tested our code, e.g. what input values we tried
- We must rely on our memory to keep track of which functions (parts of the code) have been tested and which have not (informal testing may work well on smaller pieces of code but it becomes unpractical for a large codebase)
- Once we close our development environment, we lose all the manual test scenarios we have tried

#### Writing test functions

A better way of testing code is writing specific test functions or scripts for parts of our software which can then be repeatedly executed (manually, but also automated to a large extent).
Since computers are very good and efficient at automating repetitive tasks, we should take advantage of this wherever possible.
Unlike with informal testing, these test functions are saved as part of our codebase (and easily be re-run) and shared alongside our code for others to use.

This is a much better approach as our test cases are documented in these test functions and can also be treated as a form of documentation and help others with understanding how our code is meant to work.
If our code changes - it is now much easier to change our test functions, compared to remembering everything we tested informally.

We can take this approach one step further by writing a test suite for our code as part of a testing framework - a set of tools used to fully automate the process of running tests and further 
reduce the risk of human error. 
The use of a testing framework becomes particularly important if your code grows beyond one or two scripts.

#### Use test frameworks to automate testing

Automated testing involves using special testing frameworks (e.g. testthat for R, Pytest for Python, JUnit for Java) to automate and control the execution of tests (which is software separate from the software being tested)
and the comparison of actual with predicted outcomes. 
A test framework comprises a set of rules for creating and designing test cases together with tools that are designed to run these tests efficiently.
For example, test frameworks typically automatically discover tests based on specific file and function naming patterns (e.g. they look for files or functions that start with “test_” or end with “_test”).
Such test files are typically located in a special sub-folder (e.g. called `tests`) within a software project, and are version controlled and shared along with the rest of the code.

Check out the [section "How do we automate code testing?"](#how-do-we-automate-code-testing) for more details.

### Solutions

- Write clear, understandable and independent tests - ensure test cases are easy to understand and maintain, use descriptive names for test functions and methods that clearly convey their purpose, and make each test independent (tests should not rely on the results or state of other tests to function correctly).
- Write tests early and often - begin testing as early as possible in the development process as writing tests alongside code development helps catch defects sooner and reduces the cost of fixing them.
- Use both functional and non-functional tests in combination to ensure not only that the software functions correctly and according to its specification but also performs well, is secure, and offers a good user experience. At a minimum write unit tests to test individual functions or methods of your code in isolation and ensure they perform as expected.
- Maintain a balance between automated and manual testing; use manual testing for exploratory or usability testing where human judgement is essential.
- Aim for high code coverage (percentage of the code that is tested) to reduce the likelihood of undetected bugs, but avoid focusing solely on achieving 100% coverage as some code may not be relevant to test (e.g. built-in functions for your programming language or functions imported from well-known and well-tested libraries). Remember, test coverage of 100% does not mean that your code is bug-free. Prioritise testing of critical paths through your code, complex logic, edge cases, and parts of our code that carry the greatest “reputational risk”, i.e. that could affect the accuracy of your reported results.
- Use [automated test frameworks](#how-do-we-automate-code-testing) to run tests frequently and consistently.


## How do we automate code testing?

### Description 

In test automation, we usually use [test automation frameworks][test-automation-frameworks] to let the computer execute our test cases. 
Thus is in contrast to [manual testing][manual-testing], where a person is executing test cases by hand.
Test automation frameworks typically accept a list of test cases that need to be executed, run them, compare the actual output with the expected output and summarise the test results in a report.
Compared to manual testing, test automation can cover a larger number of test cases, is less costly, less time-consuming and less error prone.
Test automation is also critical for [Continuous Integration (CI)][continuous-integration] (including continuous testing) and Continuous Delivery (CD).

[Continuous Integration (CI)][continuous-integration] is the process of integrating code changes into the main development branch of your software 
early and often. 
For this to be possible, we need to be able to execute steps such as building and testing the software automatically each time there is a change in the code.
Hence, testing is an integral part and a widely accepted use case of CI.
Testing in a CI pipeline goes one step further compared to the sole use of test automation frameworks.
In addition to using the test automation framework locally and starting the execution of test within it manually, 
CI determines when and how to execute our test cases automatically and runs them on an integration machine.
For example, as soon as a commit is pushed or a merge to a software development branch is performed, the integration machine starts a CI pipeline and 
executes the test cases and reports the test results in the so-called CI job log.
Popular examples of CI infrastructures include [GitHub Actions][github-actions] and [GitLab CI/CD][gitlab-ci-cd].

### Considerations 

Benefits of using automated testing frameworks:

- Improved test efficiency and development speed - it allows for the quick execution of repetitive and complex test cases, significantly speeding up the testing process compared to manual or informal testing and increasing the pace with which the software is developed.
- Lower maintenance costs - it enables early error detection so less development time is spent on debugging and fixing errors in code.
- Minimal manual intervention - it automates repetitive test cases and reduces the amount of manual testing effort required. This frees up developers' time to focus on more complex scenarios, exploratory testing, or new feature development.
- Maximum test coverage - it enables the execution of a large number of test cases, including various test scenarios, edge cases and configurations (operating systems, environments, platforms, etc.) that would be difficult to cover with manual testing.
- Increased reusability of code - it reduces the effort required to write new test scripts for similar test cases and promotes a modular approach to testing.

[**Test Patterns**][test-patterns] describe good practices that can be applied to your test automation as well as test cases. 
Here are a few examples of these principles:

- *Fully Automated*:
  - To make most use of test automation it is the best idea to fully automate the testing, so that no manual steps are involved.
- *Self-Checking*:
  - Everything that is needed to compare the actual output with the predicted output is encoded in the test.
- *Repeatable Test*:
  - Each run of a test should result in the same output given the same input.
- *Robust Test*:
  - As the test base grows we try to minimise the impact of a change in one test case on other test cases and thereby minimise the overlap between the tests.
  - We also ensure that the test environment does not impact our tests by isolating the system under test (SUT) from the environment as much as possible.
- *Simple Test*:
  - Keep the tests small and they should test only one thing at a time.
- *Expressive Tests*:
  - Tests should be as expressive as possible, so that they are easily understood.
- *Do No Harm*:
  - Tests should not do harm and introduce risks that's why we must not add tests to the production environment, they should only be added to the test environment.
- *Verify One Condition per Test*:
  - Tests need to be focused and to make them better understood they should only verify one condition per test.
- *Keep Tests Independent*:
  - Tests must not interact and influence each other, they need to be independent.

### Solutions

- [**Testing Frameworks**][test-automation]
  - Test automation frameworks are utilised to control the execution of tests, the comparison of actual outcomes with predicted outcomes, and also the reporting of the test results back to the user.
  - Use test automation frameworks to run tests frequently and consistently
- [**Continuous Integration**][continuous-integration]
  - Continuous Integration is the process of continuously integrating code into the mainline of your code developments and thereby automate the build of the software as well as the tests the software in so-called Continuous Integration pipelines.
  - Continuous Integration automates repetitive tests, saves time and ensures tests are run consistently across different environments and platforms.

## How to cite this page

To be added.

## Tools and resources <!-- do not delete this heading and write your text below it -->

- [Python testing framework Pytest][pytest]
- [Unit Testing for R - testthat][testthat]
- [GitHub Actions CI infrastructure][github-actions]
- [GitLab CI/CD infrastructure][gitlab-ci-cd]

## References <!-- do not delete this heading and write your text below it -->


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
[compatibility-testing]: https://en.wikipedia.org/wiki/Compatibility_testing
[test-driven-development]: https://en.wikipedia.org/wiki/Test-driven_development
[test-automation]: https://en.wikipedia.org/wiki/Test_automation
[test-automation-frameworks]: https://en.wikipedia.org/wiki/Test_automation#Framework_approach_in_automation
[manual-testing]: https://en.wikipedia.org/wiki/Manual_testing
[continuous-integration]: https://en.wikipedia.org/wiki/Continuous_integration
[github-actions]: https://docs.github.com/en/actions
[gitlab-ci-cd]: https://docs.gitlab.com/ee/topics/build_your_application.html
[pytest]: https://docs.pytest.org/en/stable/
[testthat]: https://testthat.r-lib.org/
[test-patterns]: http://xunitpatterns.com/
