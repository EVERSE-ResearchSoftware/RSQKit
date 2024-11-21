---
title: Gitlab CI
description: How to use and set up Gitlab CI for your Gitlab repository
contributors: ["Tom François"]
page_id: gitlab_ci
related_pages: []
---

## What is CI/CD?

CI/CD is a continuous method of software development, where you continuously build, test, deploy, and monitor iterative code changes.

This iterative process helps reduce the chance that you develop new code based on buggy or failed previous versions. GitLab CI/CD can catch bugs early in the development cycle, and help ensure that the code deployed to production complies with your established code standards.

## What is Gitlab CI?

### Description

Gitlab CI is the tool used in Gitlab hosted projects to run CI/CD pipelines. It is the equivalent of Github Actions on github.com hosted repositories.

Motivations to setup a Gitlab CI pipeline:

- running unit tests
- build your application
- build a docker container
- deploy documentation
- deploy and generate package
- check dependencies
- ...

### Considerations

To create and run your first pipeline:

- ensure you have runners available to run your jobs. If tou are using gitlab.com, you can skip this step as gilab.com provides instance runners for you.
- create a `.gitlab-ci.yml` file at the root of your repository. This file defines the pipelines and jobs you want to run.

### Solutions




## How to cite this page <!-- do not delete this heading and write your text below it -->
 contributors, page URL. Last date of access.

## Tools and resources

- [Gitlab CI documentations](https://docs.gitlab.com/ee/ci/)
- [Gitlab CI examples](https://docs.gitlab.com/ee/ci/examples/)

## References

[^gitlabci_first_tuto]: [https://docs.gitlab.com/ee/ci/quick_start/](https://docs.gitlab.com/ee/ci/quick_start/)

[^gitlabci-antipatterns]: [https://dev.to/zenika/gitlab-ci-10-best-practices-to-avoid-widespread-anti-patterns-2mb5](https://dev.to/zenika/gitlab-ci-10-best-practices-to-avoid-widespread-anti-patterns-2mb5)

