---
title: How to Automate Your Software Tests with Test Frameworks and Continuous Integration
description: Explains useful aspects about automating sofware tests with test frameworks and Continuous Integration.
contributors: ["Aleksandra Nenadic", "Christian Hüser"]
page_id: automating_tests_with_test_frameworks_and_ci
related_pages: []
---

## How to Automate Your Software Tests with Test Frameworks and Continuous Integration
 
### Description

Software tests are an integral part in the software development process.
Test automation provides rapid feedback and serves as quality gate which is essential for a efficient software development process.
We give an example that makes use of [Python][python], [Pytest][pytest] as the test framework, and GitHub Actions for Continuous Integration (CI) to exemplify the automation of tests with CI.

### Considerations 

- The **Test-First Policy in Test Driven Development** is one promising approach to ensure to the testability of software under test (SUT).
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

- [Test automation with Pytest][pytest]
  - A popular test framework for Python applications.
- [Automated testing of Python code with GitHub Actions][github-actions-for-python-tests]
  - GitHub Actions can be used to automate your software tests that utilize Pytest as the test framework for a Python application.
  - Your Pytest software tests are executed in a GitHub Actions CI pipeline and the results and feedback can be inspected in the CI job log.

## How to cite this page 

To be added.

## Tools and resources

- [Python][python]
- [Pytest][pytest]
- [Automated testing of Python code with GitHub Actions][github-actions-for-python-tests]

[python]: https://www.python.org
[pytest]: https://docs.pytest.org
[github-actions-for-python-tests]: https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#testing-your-code
