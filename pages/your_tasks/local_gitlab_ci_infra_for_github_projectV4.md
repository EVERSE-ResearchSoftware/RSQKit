---
title: "Using local GitLab CI infrastructure for your GitHub project"
search_exclude: true
description: "Leverage local GitLab CI runners and specialized hardware for GitHub-hosted projects when standard CI resources are insufficient"
contributors: []
page_id: github_gitlab_ci_integration
related_pages:
  your_tasks: [ci_cd, task_automation_github_actions, task_automation_gitlab_ci_cd]
training:
  - name: "GitLab CI/CD Documentation"
    registry: "GitLab"
    url: "https://docs.gitlab.com/ee/ci/"
  - name: "GitHub Actions Documentation"
    registry: "GitHub"
    url: "https://docs.github.com/en/actions"
  - name: "Alpaka Job Matrix Library"
    registry: "GitHub"
    url: "https://github.com/alpaka-group/alpaka-job-matrix-library"
---

## How can I use my organization's local GitLab CI infrastructure for a GitHub-hosted project?

### Description

Many research software projects are hosted on {% tool "github" %} to benefit from its large open-source community and collaboration features. However, GitHub's free CI resources may be insufficient for complex research software that requires specialized hardware (GPUs, specific CPU architectures), extensive testing matrices, or simply more computational resources than the free tier provides. Organizations often have local {% tool "gitlab" %} instances with powerful runners and specialized hardware that could address these limitations.

Research projects like [PIConGPU](https://github.com/ComputationalRadiationPhysics/picongpu) and [Alpaka](https://github.com/alpaka-group/alpaka) demonstrate this challenge perfectly. These projects require testing across multiple hardware configurations and extensive parameter combinations that exceed GitHub's free tier capabilities, yet benefit from GitHub's collaborative ecosystem for open-source development.

### Considerations

- Resource limitations on GitHub: Free {% tool "github-actions" %} have monthly limits and lack access to specialized hardware like GPUs or alternative CPU architectures required for performance-portable research software
- Available local infrastructure: Your organization may have {% tool "gitlab-ci-cd" %} runners with specialized hardware including multiple CPU architectures (ARM, Power, AMD, Intel), GPUs (NVIDIA, AMD), HPC systems, or different operating systems (macOS, Windows)
- Fork contribution workflow: Contributors often work from forks, which complicates direct integration with external CI systems, especially important for open-source research projects with distributed contributors
- GitLab Premium limitations: GitLab's native GitHub integration requires Premium edition and has limitations with fork pull requests, making it unsuitable for many research organizations
- Security considerations: External contributors need access to CI results without compromising internal infrastructure security
- Webhook reliability: Ensuring consistent communication between GitHub events and GitLab CI execution
- Status reporting complexity: Maintaining clear CI status visibility on GitHub while running on external infrastructure

### Solutions

#### Repository Mirroring Infrastructure

- Implement GitLab native project mirroring: Configure {% tool "gitlab" %} to automatically synchronize your GitHub repository to a local GitLab instance. See [GitLab repository mirroring documentation](https://docs.gitlab.com/ee/user/project/repository/mirror/) for setup instructions. Initially mirror only local branches to maintain security and avoid unnecessary synchronization of all external forks. Note that GitLab's native mirroring requires push access to the source repository, which means you need either a deploy key or personal access token with write permissions to the GitHub repository.

- Configure selective branch mirroring: Set up mirroring rules that focus on main development branches and exclude temporary or experimental branches to reduce synchronization overhead. Configure branch filters using [GitLab's mirroring options](https://docs.gitlab.com/ee/user/project/repository/mirror/#mirror-only-protected-branches).

- Set up mirror monitoring: Implement monitoring to ensure mirroring remains active and responsive, with automated alerts for synchronization failures.

#### Fork Integration System

- Deploy automated fork mirroring bot: Create a webhook-driven bot that monitors GitHub pull request events from forks and automatically creates corresponding branches in the GitLab mirror. Use [GitHub webhooks documentation](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks) and [GitLab API for branch creation](https://docs.gitlab.com/ee/api/branches.html#create-repository-branch). Use systematic naming conventions such as `username-repo-feature-branch` to maintain organization and traceability.

- Implement webhook security: Configure webhook signatures and validation to ensure only legitimate GitHub events trigger mirroring operations, preventing unauthorized access to your internal GitLab infrastructure. Follow [GitHub webhook security best practices](https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks).

- Handle fork branch lifecycle: Implement automated cleanup of mirrored fork branches when corresponding pull requests are closed or merged, maintaining repository hygiene.

#### CI Status Integration

- Configure bidirectional status reporting: Implement a system that sends GitLab pipeline status back to GitHub using commit hashes for identification. Use [GitHub's commit status API](https://docs.github.com/en/rest/commits/statuses) to report build statuses from external CI systems and [GitLab CI/CD pipeline events](https://docs.gitlab.com/ee/user/project/integrations/webhook_events.html#pipeline-events). See also [GitLab's GitHub integration guide](https://docs.gitlab.com/ci/ci_cd_for_external_repos/github_integration/) for comprehensive setup instructions. This ensures pull request status checks are properly updated regardless of the execution platform. Use consistent naming patterns for external status checks, such as "gitlab-ci/pipeline-name" or "gitlab-ci/job-name", to avoid conflicts with other CI systems and maintain clear identification of status sources.

- Set up detailed status descriptions: Provide clear, descriptive status messages that indicate the testing platform, job types, and specific failure reasons to help developers understand CI results.

- Implement status aggregation: For complex pipelines with multiple stages, aggregate status information to provide clear pass/fail indicators while maintaining access to detailed logs.

#### Access Management and Security

- Establish guest access procedures: Create documented procedures for external contributors to access GitLab CI logs and results, including temporary guest access workflows that maintain security boundaries. Note that this is primarily relevant for non-public GitLab projects where CI logs are not publicly accessible. Practical implementation:
  1. Create a standard request template for CI log access (include GitHub username, PR number, specific job logs needed)
  2. Set up a dedicated GitLab group for external contributors with guest permissions
  3. Use GitLab's [temporary project access](https://docs.gitlab.com/ee/user/project/members/#add-users-to-a-project) with expiration dates (e.g., 7 days)
  4. Automate access removal using GitLab's API or scheduled cleanup scripts
  5. Document the process in your project's CONTRIBUTING.md file
  Configure using [GitLab project members management](https://docs.gitlab.com/ee/user/project/members/) and [guest permissions](https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions) for setting up access control.

- Configure permission mapping: Establish clear mapping between GitHub repository permissions and GitLab project access levels to ensure appropriate access control. Practical implementation:
  1. Document permission equivalencies:
     - GitHub repository admins → GitLab project maintainers (can manage runners, settings)
     - GitHub write access → GitLab developer role (can trigger pipelines, view logs)
     - GitHub read access → GitLab reporter role (can view pipeline results only)
  2. Create GitLab groups that mirror your GitHub team structure
  3. Use GitLab's [SAML/LDAP integration](https://docs.gitlab.com/ee/integration/saml.html) if available for automated synchronization
  4. Implement regular access reviews (monthly/quarterly) to ensure permissions stay synchronized
  5. Use [GitLab's audit events](https://docs.gitlab.com/administration/compliance/audit_event_reports/) to track permission changes
  Document these mappings and implement them consistently using [GitLab's role-based permissions](https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions).

- Implement audit logging: Maintain comprehensive logs of all cross-platform CI activities for security monitoring and troubleshooting. Configure logging for:
  - Webhook processing events and failures
  - Mirror synchronization activities
  - User access grants and revocations
  - Pipeline trigger events from GitHub
  Use [GitLab's audit events](https://docs.gitlab.com/administration/compliance/audit_event_reports/) and implement custom logging for webhook processing activities.

#### Infrastructure Configuration

- Deploy specialized GitLab runners: Configure runners with the specific hardware configurations your project requires. Follow [GitLab Runner installation guide](https://docs.gitlab.com/runner/install/) and [runner configuration documentation](https://docs.gitlab.com/runner/configuration/):

The following table shows common runner configurations for research software testing. Choose hardware specifications based on your project's specific computational requirements:

| Runner Type | Hardware Configuration | Use Case | Rationale |
|-------------|----------------------|----------|-----------|
| Standard | x86_64 CPU | Build testing, unit tests | Most common development environment |
| GPU-NVIDIA | x86_64 + NVIDIA GPU | CUDA development, GPU computing | NVIDIA ecosystem dominance in HPC |
| GPU-AMD | x86_64 + AMD GPU | ROCm/HIP testing, OpenCL | Alternative GPU vendor support |
| ARM | ARM64 CPU | Cross-platform validation | Growing ARM adoption in HPC/cloud |
| PowerPC | ppc64le CPU (little-endian PowerPC architecture commonly used in modern HPC systems)| HPC compatibility testing | Legacy HPC system support |

Hardware sizing considerations:

- Memory: Scale based on your largest datasets and compilation requirements (typically 8GB minimum, 32GB+ for large scientific codes)
- Storage: Ensure sufficient space for container images, build artifacts, and test data
- CPU cores: More cores reduce build times but increase infrastructure costs

- Configure runner tagging: Implement comprehensive tagging systems that allow jobs to target specific hardware configurations while maintaining flexibility for resource allocation. Practical implementation:
  
  ```toml
  # Example runner configuration with tags (config.toml format)
  [[runners]]
    name = "gpu-nvidia-runner"
    tags = ["gpu", "nvidia", "cuda", "high-memory"]
    
  [[runners]]
    name = "cpu-arm-runner"  
    tags = ["cpu", "arm64", "cross-platform"]
  ```

  ```yaml
  # Example job targeting specific runners
  cuda_tests:
    tags:
      - gpu
      - nvidia
    script:
      - nvcc --version
      - ./run_cuda_tests.sh
      
  arm_build:
    tags:
      - cpu
      - arm64
    script:
      - ./build_for_arm.sh
  ```

See [GitLab Runner tags documentation](https://docs.gitlab.com/ee/ci/runners/configure_runners.html#use-tags-to-control-which-jobs-a-runner-can-run).

- Organize runners by capability: Structure your runners based on hardware capabilities and project requirements to ensure fair resource distribution. Use GitLab's runner types strategically:
  - Shared runners: Available to all projects in your GitLab instance (good for standard builds)
  - Group runners: Shared within specific groups/organizations (good for department-level resources)  
  - Project-specific runners: Dedicated to individual projects (good for specialized hardware)
  
  Example conceptual organization strategy (conceptual hierarchy):
  
  ```yaml
  # Example runner configuration with types
  Shared Runners (Institute-wide):
  ├── standard-cpu (tags: cpu, x86_64)
  └── basic-gpu (tags: gpu, nvidia, shared)
  
  Group Runners (Research Group):
  ├── high-memory-cpu (tags: cpu, high-memory, research-group)
  └── specialized-gpu (tags: gpu, tesla, research-group)
  
  Project Runners (Specific Projects):
  └── hpc-powerpc (tags: powerpc, hpc, project-specific)
  ```
  
  See [GitLab runner types documentation](https://docs.gitlab.com/ee/ci/runners/runners_scope.html) for configuration guidance.

#### Monitoring and Maintenance

- Consider implementation complexity: The monitoring and maintenance requirements for this hybrid CI setup represent significant operational overhead that research software engineers should carefully consider. While the technical implementation provides powerful capabilities for complex research software testing, the ongoing maintenance requires dedicated infrastructure expertise and time investment that may exceed the capacity of smaller research teams.

- Implement comprehensive monitoring: Monitor webhook processing, mirroring bot health, runner availability, and pipeline execution metrics to ensure reliable service. Use [GitLab's monitoring features](https://docs.gitlab.com/ee/administration/monitoring/) and [runner monitoring](https://docs.gitlab.com/runner/monitoring/).

- Create automated monitoring scripts: Provide monitoring scripts for webhook health, GitLab API connectivity, and runner availability. These scripts can be integrated with GitLab's monitoring framework to provide practical monitoring solutions that can be deployed.

  Example webhook health monitoring script:

  ```bash
  #!/bin/bash
  # webhook_health_monitor.sh - Monitor webhook endpoint health
  
  WEBHOOK_URL="https://gitlab.example.com/webhook"
  ALERT_EMAIL="admin@yourorg.com"
  
  # Test webhook endpoint
  if ! curl -f -s -o /dev/null "$WEBHOOK_URL/health"; then
      echo "Webhook endpoint $WEBHOOK_URL is down" | mail -s "Webhook Alert" "$ALERT_EMAIL"
      exit 1
  fi
  
  # Check GitLab API connectivity
  if ! curl -f -s -H "Authorization: Bearer $GITLAB_TOKEN" \
       "https://gitlab.example.com/api/v4/projects" > /dev/null; then
      echo "GitLab API connectivity failed" | mail -s "GitLab API Alert" "$ALERT_EMAIL"
      exit 1
  fi
  
  echo "All systems healthy"
  ```

  Deploy this script via cron to run every 5 minutes by adding the following line to your crontab:

  ```bash
  # Add this line to your crontab (run: crontab -e)
  */5 * * * * /usr/local/bin/webhook_health_monitor.sh >/dev/null
  ```

  This runs the script every 5 minutes and suppresses output unless there's an error.

- Configure automated alerts: Set up alerting for critical failures in the integration chain, including mirroring delays, webhook processing errors, and runner unavailability.

- Establish maintenance procedures: Create documented procedures for routine maintenance, including runner updates, bot deployments, and mirror configuration changes.
  
- Monitor webhook processing metrics: Track webhook processing success rates, maintaining above 95% success rates to ensure reliable integration. Monitor GitLab pipeline trigger delays, as synchronization delays exceeding 5 minutes may indicate infrastructure issues requiring investigation. Track runner availability across different hardware types, particularly for specialized GPU or ARM runners that may have limited availability.

- Configure specific alerting thresholds: Set up alerts for webhook processing failures exceeding 3 consecutive failures, mirroring synchronization delays beyond 10 minutes, and runner unavailability lasting more than 30 minutes. Implement escalation procedures that automatically notify infrastructure administrators when automated recovery attempts fail.

- Establish regular maintenance schedules: Implement weekly runner health checks, monthly authentication token validation, and quarterly review of webhook configurations. Document these procedures with specific commands and expected outputs to ensure consistency across different team members managing the infrastructure.

## How do I ensure reliable integration between GitHub and GitLab CI systems?

### Description

Maintaining a stable, reliable integration between GitHub repositories and GitLab CI infrastructure requires careful attention to the communication pathways, error handling, and monitoring systems that connect these platforms. The integration must handle various failure modes gracefully while providing clear feedback to developers.

### Considerations

- Network reliability: Communication between GitHub and GitLab may experience intermittent failures, requiring robust retry mechanisms
- Authentication management: Maintaining valid authentication tokens across both platforms while ensuring security
- Rate limiting: Both GitHub and GitLab APIs have rate limits that must be respected to avoid service interruptions
- Error propagation: Failures in any part of the integration chain should be clearly communicated to developers
- Synchronization delays: Mirroring introduces latency that must be managed to provide timely feedback
- Configuration drift: Keeping webhook configurations and mirroring settings synchronized as projects evolve

### Solutions

- Implement robust webhook processing: Design webhook handlers that reliably process GitHub webhook events. Implement error handling for downstream operations (like GitLab API calls), queue failed operations for retry, and use dead letter queues for events that cannot be processed after multiple attempts. Note that GitHub handles webhook delivery retries automatically, but you must ensure reliable processing of received events. Practical implementation:
  1. Validate webhook signatures using GitHub's secret token
  2. Return HTTP 200 immediately to acknowledge receipt, then process asynchronously
  3. Use a message queue (Redis, RabbitMQ) to handle processing failures
  4. Implement exponential backoff for failed GitLab API calls
  5. Store failed events in a dead letter queue for manual review
  Example using Python/Flask:

  ```python
  @app.route('/webhook', methods=['POST'])
  def handle_webhook():
      # Validate signature first
      if not verify_signature(request):
          return 'Unauthorized', 401
      
      # Input Validation step
      if not request.json or 'action' not in request.json:
        return 'Bad Request', 400

      # Queue for async processing
      queue.enqueue(process_webhook, request.json)
      return 'OK', 200
  ```

- Configure webhook redundancy: Set up multiple webhook endpoints with failover mechanisms to ensure continuous operation even during maintenance or unexpected outages. Practical implementation:
  1. Configure multiple webhook URLs in your GitHub repository settings
  2. Use a load balancer (nginx, HAProxy) to distribute webhook traffic
  3. Deploy webhook handlers on multiple servers/containers
  4. Implement health checks for each endpoint
  5. Use monitoring to detect failed endpoints and route traffic accordingly
  
  Example nginx configuration:

  ```nginx
  upstream webhook_backends {
      server webhook1.example.com:8080 max_fails=3 fail_timeout=30s;
      server webhook2.example.com:8080 max_fails=3 fail_timeout=30s;
  }
  
  server {
      location /webhook {
          proxy_pass http://webhook_backends;
      }
  }
  ```

- Establish authentication token rotation: Implement automated token rotation for both GitHub and GitLab APIs to maintain long-term reliability without manual intervention. This includes updating webhook configurations simultaneously that use these tokens for authentication as webhook authentication will fail if tokens become desynchronized between platforms. Configure using [GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and [GitLab access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html). Automate webhook updates using [GitHub's webhook API](https://docs.github.com/en/rest/webhooks) and [GitLab's webhook API](https://docs.gitlab.com/api/project_webhooks/) when tokens are rotated. Note that GitHub tokens require "repo" and "admin:repo_hook" scopes for full functionality, while GitLab tokens need "api" scope for repository and webhook management.

- Create comprehensive error logging: Implement detailed logging throughout the integration pipeline to facilitate troubleshooting and identify patterns in failures.

- Set up health monitoring dashboards: Create monitoring dashboards that provide real-time visibility into the integration health, including webhook processing rates, mirroring delays, and CI execution metrics.

## How do I handle the complexity of managing both GitHub and GitLab workflows?

### Description

Running a hybrid GitHub-GitLab CI setup introduces workflow complexity that needs to be managed carefully to maintain developer productivity and project maintainability. This complexity is amplified when dealing with research software that requires specialized testing infrastructure and has contributors with varying levels of CI/CD expertise.

### Considerations

- Developer experience: Contributors should have a seamless experience regardless of which CI system is running their code
- Debugging complexity: Failed CI runs may require access to GitLab logs while the discussion happens on GitHub
- Permission management: Different access controls between GitHub and GitLab may create permission mismatches
- Documentation maintenance: Hybrid workflows require comprehensive documentation that stays current with both platforms
- Onboarding complexity: New contributors need to understand both the GitHub collaboration model and GitLab CI execution environment

### Solutions

- Provide comprehensive documentation: Create detailed documentation explaining the hybrid CI setup, including troubleshooting guides and examples specific to your research domain. Include step-by-step guides for common developer workflows.

- Implement automated documentation updates: Set up systems to automatically update documentation when CI configurations change, ensuring documentation remains current.

- Create developer onboarding guides: Develop specific onboarding materials that explain how to work with the hybrid system, including how to access logs, interpret status messages, and request runner access.

- Establish clear escalation procedures: Document clear procedures for developers to follow when they encounter CI issues that require GitLab access or infrastructure support.

- Implement automated issue routing: Create systems that automatically route CI-related issues to appropriate support channels based on whether they originate from GitHub or GitLab components.

## References

This approach was successfully implemented by the Helmholtz-Zentrum Dresden-Rossendorf for the Alpaka project, demonstrating how research organizations can effectively combine GitHub's collaborative features with local specialized CI infrastructure. The implementation showcases the infrastructure integration techniques that make complex research software CI pipelines practical and maintainable.

Further resources:

- [Continuous Integration in Complex Research Software - Handling Complexity](https://zenodo.org/records/14643958)
- [PIConGPU](https://github.com/ComputationalRadiationPhysics/picongpu)
- [Alpaka](https://github.com/alpaka-group/alpaka)
- [Alpaka Job Matrix Library](https://github.com/alpaka-group/alpaka-job-matrix-library)
- [Container Registry for CI Images](https://codebase.helmholtz.cloud/crp/alpaka-group-container)
- [Dynamic CI Pipelines in GitLab](https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#dynamic-child-pipelines)