---
title: "Managing complex CI testing matrices for research software"
search_exclude: true
description: "Efficiently test research software across multiple compilers, libraries, architectures, and platforms while managing CI resource constraints and maintaining fast feedback loops"
contributors: []
page_id: complex_ci_testing_matrix
related_pages:
  your_tasks: [ci_cd, task_automation_github_actions, task_automation_gitlab_ci_cd]
training:
  - name: "Pairwise Testing with allpairspy"
    registry: "PyPI"
    url: "https://pypi.org/project/allpairspy/"
  - name: "GitLab Dynamic Child Pipelines"
    registry: "GitLab"
    url: "https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#dynamic-child-pipelines"
  - name: "Docker Multi-stage Builds"
    registry: "Docker"
    url: "https://docs.docker.com/build/building/multi-stage/"
---

## How can I efficiently test my research software across multiple compiler versions, library dependencies, and target platforms?

### Description

Research software, particularly performance-portable libraries and simulation codes, often needs to support extensive combinations of compilers, library versions, target architectures, and runtime environments. For example, accelerator abstraction libraries like [Alpaka](https://github.com/alpaka-group/alpaka) require testing across multiple GCC versions, Clang versions, CUDA SDK versions, CMake versions, and Boost versions. A naive approach testing all combinations can create thousands of test jobs, making CI pipelines impractically long and resource-intensive.

Consider this real-world example from accelerator development:

- 4 GCC compiler versions
- 6 Clang compiler versions  
- 10 CUDA SDK versions
- 4 CMake versions
- 7 Boost library versions

This results in **2,800 potential combinations**, requiring approximately **~9.3 hours** of compute time at 6 minutes per job, even with 30 parallel runners.

### Considerations

- Combinatorial explosion: The number of possible combinations grows exponentially with each additional parameter (compilers × architectures × libraries × versions)
- Resource constraints: CI runners have limited capacity, and excessive parallelization can monopolize shared infrastructure across multiple projects
- Time constraints: Full test matrices can take many hours to complete, creating bottlenecks in development workflows
- Hardware diversity: Different combinations may require specific hardware (NVIDIA GPUs, AMD GPUs, ARM processors, PowerPC architectures)
- Invalid combinations: Some parameter combinations may be incompatible (e.g., older CUDA versions with newer GCC compilers)
- Coverage vs efficiency: Need adequate test coverage without redundant or meaningless test combinations
- Maintenance overhead: Large test matrices become difficult to update and debug when new versions are released

### Solutions

#### Pairwise Testing Implementation

- Use dynamic child pipelines: Dynamic child pipelines are essential for implementing pairwise testing as they allow programmatic generation of CI configurations at runtime. Leverage CI systems that support programmatically generated pipeline configurations based on computed test matrices, enabling runtime optimization based on available resources.

- Implement pairwise testing algorithms: Use mathematical approaches that ensure every combination of two parameter values appears in at least one test job, dramatically reducing total tests while maintaining comprehensive interaction coverage.

- Use specialized job generation libraries: Implement dynamic job generators using tools like `allpairspy`:
  
  ```python
  from allpairspy import AllPairs

  parameters = {
      "host_compiler": ["gcc-8", "gcc-9", "gcc-10", "gcc-11"],
      "device_compiler": ["clang-10", "clang-11", "clang-12", "clang-13", "clang-14", "clang-15"],
      "cuda_sdk": ["cuda-10.2", "cuda-11.0", "cuda-11.1", "cuda-11.2", "cuda-11.3",
                   "cuda-11.4", "cuda-11.5", "cuda-11.6", "cuda-11.7", "cuda-11.8"],
      "cmake": ["cmake-3.18", "cmake-3.19", "cmake-3.20", "cmake-3.21"],
      "boost": ["boost-1.68", "boost-1.70", "boost-1.72", "boost-1.74",
                "boost-1.75", "boost-1.76", "boost-1.78"]
  }

  keys = list(parameters.keys())
  values = [parameters[key] for key in keys]

  for i, pairs in enumerate(AllPairs(values)):
      config = dict(zip(keys, pairs))
      print(f"Job {i+1}: {config}")

  # This reduces 2800 combinations to ~60-100 jobs
  # Each combination of compiler + CUDA version appears at least once
  ```

- Develop domain-specific combination rules: Create libraries that encode your project's specific compatibility requirements and testing priorities, such as the [Alpaka](https://github.com/alpaka-group/alpaka) approach.

- Implement exclusion logic: Define rules to automatically exclude known incompatible combinations:
  
  ```yaml
  # Example exclusion rules for GPU computing
  exclusions:
    - cuda_version: "11.0"
      gcc_version: "gcc-11"  # Incompatible combination
    - architecture: "ppc64le"
      cuda_version: "*"      # CUDA not available on PowerPC
  ```

#### Mathematical Optimization Analysis

| Testing Approach      | Total Jobs | Estimated Runtime (30 jobs parallel, 6 mins/job) | Coverage Type |
|-----------------------|------------|---------------------------------------------------|---------------|
| Full matrix (naive)   | 2800       | ~9.3 hours                                        | 100% combinations |
| Pairwise testing      | ~60–100    | ~20–30 minutes                                    | All 2-way interactions |
| Random sampling       | ~200       | ~40 minutes                                       | Statistical coverage |

## How can I optimize CI pipeline performance while maintaining comprehensive testing?

### Description

Even with reduced test matrices, complex research software CI pipelines face performance challenges. Multiple optimization strategies are needed to provide fast developer feedback while maintaining thorough testing coverage across diverse computing environments.

### Considerations

- Build time bottlenecks: Repeatedly compiling large dependency sets (like HPC libraries, scientific computing frameworks, or large C++ template libraries) wastes significant time
- Resource competition: Simultaneous job execution can overwhelm shared CI infrastructure, affecting other projects
- Failure feedback delays: Critical bugs may not be detected until late in pipeline execution
- Development vs production workflows: Full test suites may be unnecessary during iterative development
- Storage and bandwidth: Large scientific computing containers and datasets impact transfer times
- Platform-specific testing: Different hardware platforms may have varying performance characteristics

### Solutions

#### Container Optimization Strategies

- Implement pre-built container strategies: Create and maintain container images with pre-compiled dependencies. Multi-stage builds allow you to separate dependency installation from application code, producing smaller, faster final images by copying only necessary artifacts from build to runtime:
  
  ```dockerfile
  # Multi-stage build for scientific computing dependencies
  FROM nvidia/cuda:11.8-devel as builder
  RUN apt-get update && apt-get install -y \
      gcc-10 g++-10 clang-12 \
      cmake libboost-all-dev \
      libomp-dev libfftw3-dev
  
  FROM builder as runtime
  COPY --from=builder /usr/local /usr/local
  # Application-specific layers added dynamically
  ```

- Deploy container registry optimization: Host container images in the same data center as CI runners to minimize transfer times and bandwidth costs. Use container registries that support layer caching (reusing unchanged layers between builds) and delta compression (only transferring changed parts of images). Check your registry documentation if it advertises support for these features - most modern registries like GitLab Container Registry, Harbor, and AWS ECR support them.

- Optimize container layer caching: Structure container builds to maximize reuse of intermediate layers and minimize rebuild times. Group frequently changing components in separate layers from stable dependencies. For best practices, see [Docker's layer caching guide](https://docs.docker.com/build/cache/). You can also follow this tutorial for hands-on learning: [Docker Layer Caching Tutorial by Earthly](https://docs.earthly.dev/earthly-0.6/docs/guides/cache).

#### Wave Scheduling Implementation

Running all jobs simultaneously can overwhelm shared infrastructure and delay results. By grouping jobs into sequential stages ("waves"), critical tests can run earlier and free up resources faster. Hence, wave scheduling prevents resource monopolization by running jobs in stages, allowing other projects to use CI infrastructure between waves while providing early feedback on critical tests.

- Use wave scheduling for resource management: Distribute jobs across pipeline stages to periodically release CI resources:
  
  ```yaml
  # GitLab CI wave scheduling example
  stages:
    - wave1_critical
    - wave2_compatibility  
    - wave3_performance
    - wave4_extended
  
  # Critical tests run first for fast feedback
  test_core_functionality:
    stage: wave1_critical
    script: [run core unit tests]
  
  # Extended testing runs after resources freed
  test_gpu_performance:
    stage: wave4_extended
    script: [run performance benchmarks]
  ```

- Implement intelligent job prioritization: Order jobs to maximize early failure detection:
  - Place strict compiler configurations in early waves
  - Run compatibility tests with cutting-edge tool versions first
  - Schedule resource-intensive performance tests in later stages

- Visualize wave scheduling structure:

```
Wave 1 ─────▶ Fast compile checks, style, small matrix
                   ↓
Wave 2 ─────▶ Medium-sized combinations, functional tests
                   ↓
Wave 3 ─────▶ Full matrix, slowest GPU/HPC tests
```

This structure helps fail early and frees resources for other users.

#### Development Workflow Optimization

- Enable selective testing during development: Allow developers to run targeted subsets of CI pipeline during development using commit-message-based filtering to avoid running full pipeline for iterative development work. This reduces pipeline load during focused development:
  
  ```yaml
  # GitLab CI example - Allow developers to run tests based on commit message tags
  rules:
    - if: '$CI_COMMIT_MESSAGE =~ /\[cuda-only\]/'
      variables:
        TEST_FILTER: "cuda"
    - if: '$CI_COMMIT_MESSAGE =~ /\[cpu-only\]/'
      variables:
        TEST_FILTER: "cpu"
  ```

  ```bash
  # Example usage - commit message to run only CUDA tests
  git commit -m "Add CUDA kernel optimization [ci:cuda-only]"
  ```

## How can I manage the infrastructure complexity required for multi-platform research software testing?

### Description

Supporting comprehensive test matrices for research software requires sophisticated CI infrastructure that can handle diverse hardware requirements, manage resources efficiently across multiple projects, and provide reliable service for computationally intensive workloads.

### Considerations

- Hardware diversity requirements: Research software often targets HPC systems, requiring testing on multiple CPU architectures (x86, ARM, PowerPC), GPU vendors (NVIDIA, AMD), and specialized accelerators
- Resource scheduling complexity: Balancing competing demands from multiple research projects while ensuring fair resource allocation
- Performance benchmarking: Validating not just correctness but also performance characteristics across different hardware configurations
- HPC system integration: Connecting CI pipelines with production HPC environments for realistic performance testing
- Cost and sustainability: Managing infrastructure costs while supporting open-source research software development
- Reliability at scale: Maintaining consistent performance as research groups add more complex testing requirements

### Solutions

#### Performance Testing Integration

- Implement performance regression detection: Integrate performance benchmarking into CI pipelines to catch performance regressions early:

  ```yaml
  # Example performance testing job
  performance_benchmark:
    stage: performance
    script:
      - cmake --build build --target benchmark
      - python benchmark_analysis.py --baseline previous_results.json
      - python performance_regression_check.py
    artifacts:
      reports:
        performance: performance_results.json
  ```

- Configure performance thresholds: Establish automated performance regression detection with configurable thresholds for different hardware configurations and algorithm implementations.

#### Comprehensive Testing Strategy Implementation

- Monitor and profile pipeline performance: Track job duration, resource usage, and failure patterns to continuously optimize the pipeline structure:

  | Metric | Target | Monitoring Method |
  |--------|---------|------------------|
  | Job Duration | <10 minutes average | Pipeline analytics |
  | Queue Time | <5 minutes | Runner utilization metrics |
  | Failure Rate | <5% for stable configurations | Historical trend analysis |
  | Resource Utilization | 70-90% of capacity | Real-time monitoring |

These metrics can be obtained from your CI platform's monitoring dashboard analytics ([Gitlab CI/CD Analytics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html), GitHub Actions insights) or third-party monitoring tools like Prometheus or Grafana with GitLab Runner exporters, or APIs.

- Use matrix optimization libraries: Leverage existing tools and libraries for combinatorial testing, such as specialized job matrix libraries developed for performance-portable software testing.

## How can I implement this approach for my research software project?

### Description

Transitioning from simple CI testing to comprehensive multi-platform testing matrices requires careful planning, tool selection, and gradual implementation to avoid disrupting existing development workflows.

### Considerations

- Current CI maturity: Existing testing infrastructure and team familiarity with CI/CD concepts
- Project complexity: Size of parameter space and critical compatibility requirements
- Resource availability: Access to diverse hardware platforms and CI infrastructure budgets
- Team expertise: Developer familiarity with containerization, CI configuration, and testing strategies
- Integration requirements: Compatibility with existing development tools and workflows

### Solutions

- Start with parameter identification: Systematically catalog all dimensions that require testing validation:
  
  ```python
  # Example parameter definition for scientific computing library
  testing_parameters = {
      'compilers': ['gcc-9', 'gcc-10', 'gcc-11', 'clang-12', 'clang-13', 'clang-14'],
      'cuda_versions': ['11.0', '11.2', '11.4', '11.6', '11.8', '12.0'],
      'cmake_versions': ['3.18', '3.20', '3.22', '3.24'],
      'boost_versions': ['1.72', '1.75', '1.78', '1.80', '1.82'],
      'architectures': ['x86_64', 'arm64'],
      'build_types': ['Release', 'Debug']
  }
  ```

- Implement gradual migration strategy:
  1. Begin with core compatibility testing using pairwise algorithms
  2. Add specialized hardware testing incrementally  
  3. Introduce performance testing for stable configurations
  4. Expand to full multi-platform validation

- Use established toolchains: Leverage proven solutions from successful research software projects:
  - Job matrix generation: Implement using libraries like `allpairspy` or domain-specific tools
  - Container strategies: Base images on established scientific computing containers
  - CI integration: Use GitLab dynamic child pipelines or GitHub Actions matrix strategies

- Document testing rationale: Maintain clear documentation explaining testing parameter choices and exclusion rules to facilitate maintenance and onboarding.

- Consider resource sustainability: Even with optimized matrices, extensive testing may be technically possible, but consumes computational resources and energy. Balance testing thoroughness with environmental impact by running full matrices only when necessary (e.g., before releases) and using smaller subsets for regular development work. Consider tradeoffs between coverage and efficiency when designing your matrix and scheduling jobs.

## References

This approach was successfully implemented by the Helmholtz-Zentrum Dresden-Rossendorf for the Alpaka performance-portability library and PIConGPU particle-in-cell simulation code, demonstrating significant reductions in CI resource usage while maintaining comprehensive testing coverage across multiple compilers, accelerator platforms, and HPC architectures.

Further resources:

- [Continuous Integration in Complex Research Software - Handling Complexity](https://zenodo.org/records/14643958)
- [PIConGPU](https://github.com/ComputationalRadiationPhysics/picongpu)
- [Alpaka](https://github.com/alpaka-group/alpaka)
- [Alpaka Job Matrix Library](https://github.com/alpaka-group/alpaka-job-matrix-library)
- [Container Registry for CI Images](https://codebase.helmholtz.cloud/crp/alpaka-group-container)
- [Dynamic CI Pipelines in GitLab](https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#dynamic-child-pipelines)