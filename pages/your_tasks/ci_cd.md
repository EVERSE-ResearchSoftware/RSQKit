---
title: Continuous Integration and Continuous Delivery/Deployment
description: How can you use CI/CD in software development?
contributors: ["Aleksandra Nenadic"]
page_id: ci_cd
indicators: [software_has_ci-tests]
related_pages: 
  your_tasks: [task_automation_github_actions, task_automation_gitlab_ci_cd]
training:
   - name: EVERSE TeSS
     url: https://everse-training.app.cern.ch
     query: ci cd continuous integration continuous deployment
---

## How can you use CI/CD in software development?

### Description 

CI (Continuous Integration) and CD (Continuous Delivery/Continuous Deployment) are software development 
practices aimed at automating and improving the process of software integration, testing, and delivery.

#### Continuous Integration (CI)

Continuous Integration refers to the practice of frequently integrating code changes into a shared repository, 
ideally multiple times a day. Every code change/integration is verified by an automated build which:

- Helps detect code errors and integration issues quickly. 
- Automates the testing and building process to increase developer productivity.

#### Continuous Delivery (CD)

Continuous Delivery ensures that code changes are automatically prepared for release to production, but the actual
deployment to production is still a manual decision.

- Ensures software is always in a deployable state.
- Minimises manual steps in the release process.
- Ensures quick rollbacks to a previous deployment if issues arise.

#### Continuous Deployment (CD)

Continuous Deployment goes a step further than Continuous Delivery by automating the deployment of changes directly to production without manual intervention.

- Automates the entire process, from integration to deployment.
- Delivers features and fixes to users faster.

### Considerations

CI/CD practices and tools support various aspects of software development and usage, including:

- Automated builds - every change triggers an automatic build process, including compilation and tests.
- Version control integration - CI/CD systems typically integrate with version control systems that trigger CI/CD 
workflows on each commit, ensuring no major conflicts or issues accumulate.
- Code testing - automated unit, integration, and regression tests are run with every integration to ensure software stability and 
to ensure the software works across different environments and platforms.
- Code quality - CI can enforce coding standards through the use of static code analysis or linters.
- Deployment pipelines - software is automatically tested and packaged, ready to be deployed to production.
- Automated monitoring - monitoring software in production exists to catch any issues after deployment.
- Rollback mechanisms - ability to quickly roll back to a previous stable version if issues arise.

### Solutions

CI/CD tools and platforms for different stages of code development and deployment include:

- Version Control Systems (VCS) are essential for managing code and version control. Some such tools (like GitHub, GitLab, Bitbucket)
also provide CI/CD processes and services built around code repositories - e.g. [GitHub Actions][task_automation_github_actions], [GitLab CI/CD][task_automation_gitlab_ci_cd] and BitBucket Pipelines.
  - Additional tools such as {% tool "precommit" %} can be used alongside VCS to ensure code quality is maintained.
- CI/CD pipelines - automate the entire process from code integration to deployment. Common tools include:
  - {% tool "github-actions" %} - integrated CI/CD directly within GitHub, with [easy-to-set-up workflows (called actions)][task_automation_github_actions].
  - {% tool "gitlab-ci-cd" %}: integrated CI/CD directly within GitLab.
  - BitBucket Pipelines: integrated CI/CD directly within BitBucket.
  - {% tool "jenkins" %}: highly customisable and widely used for CI/CD pipelines.
  - CircleCI: focuses on simplicity and speed for building and testing.
  - {% tool "travis" %}: a cloud-based CI service often used for open-source projects.
  - Azure Pipelines: part of the Azure DevOps suite, supports various languages and platforms.
- Testing tools - automated testing tools like JUnit, Selenium, Cypress, and Postman integrate with CI/CD workflows/pipelines to ensure the code meets quality standards.
- Artefact repositories - tools like Artifactory or Nexus Repository store build artefacts (e.g., Docker images, binaries) for deployment.
- Containerisation and orchestration
  - {% tool "docker" %} - to help standardise environments for applications by packaging them in containers.
  - {% tool "kubernetes" %} - for orchestration, enabling deployment, scaling and management of containerised applications.
- Monitoring - tools like Prometheus, Grafana, and New Relic are used for real-time monitoring in production to ensure system health.
- Infrastructure as Code (IaC) - tools like {% tool "terraform" %}, {% tool "vagrant" %} or {% tool "ansible" %} automate infrastructure provisioning and configuration, ensuring consistency across environments.
 

[task_automation_github_actions]: ./task_automation_github_actions
[task_automation_gitlab_ci_cd]: ./task_automation_gitlab_ci_cd
