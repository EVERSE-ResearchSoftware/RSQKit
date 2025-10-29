---
title: Use of containers
description: How can you use containers and why should you use it in software development?
contributors: ["Shraddha Bajare"]
page_id: using_containers
related_pages: 
  your_tasks: [ci_cd]
keywords: ["containers", "docker", "apptainer", "software packaging", "reproducibility", "portability", "containerization", "software deployment"]
training:
  - name: "EVERSE TeSS"
    registry: TeSS
    url: "https://everse-training.app.cern.ch"
---

## How can you use containers in software development ?

### Description
Containers are a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

### Considerations

- The software may depend on specific libraries, versions, or system configurations.
- The code is expected to run across multiple platforms such as different collaborators machines, clusters, or cloud environments.
- Integration of software is required with automated workflows or CI/CD pipelines to ease testing and deployment
- The developed software applications needs ensuring for long term reproducibility and scalability.

## Why should you use containers in software development?

### Description
Sharing code with only a README or installation instructions frequently results in “dependency hell,” version mismatches, or broken setups. By contrast, containers package the entire environment including all dependencies and configurations so developer and collaborators can run the exact same setup, on differnt enviornment eliminating these issues.

### Why use Containers ?
Containers offer a different approach from coding directly on one platform or operating system. Building an application for a single environment makes moving it elsewhere difficult because the code might not work in the new setting. This often leads to bugs and errors that take extra time to fix, reducing productivity and causing frustration.

When you package an application in a container, you can move it across different platforms and systems. The container includes everything the app needs to run, so it works wherever you take it.

### Considerations

- Installation instructions sometimes omit crucial configuration or system level dependencies and is not consise.
- Differences in operating systems, library versions, or environment can cause failures.
- Re applying and re running experiments months later after the software is developed may fail if dependencies have changed.
- Ensuring reproducibility and portability with reducing setup overhead for collaborators and reviewers.

### Solutions

Containers have benefits such as:

- Reproducibility - Containers bundle everything your software needs, so it runs the same everywhere.
- Easy setup - Collaborators, reviewers can get started quickly by just pulling the application build image and run it.
- Version control -  You can tag containers to match specific versions of your code.
- Automation-friendly - Verion controled and containers itself can also be automated with [CI-CD][ci_cd] to keep test and deploymenet steps consistent.
- Lightweight and portable - Uses fewer resources than virtual machines. Works on laptops, servers, or the cloud with no system mismatch issues.

Follow the steps below to create and use containers with Docker or Apptainer for your research software.

#### 1. Build a container image using Docker or Apptainer

Depending on your environment and needs:

* {% tool "docker" %}: is ideal for general-purpose development and cloud deployment.  
* {% tool "apptainer" %}: (formerly Singularity) is better suited for HPC environments where users lack root access.

Example steps with {% tool "docker" %}:

* Choose a base image (e.g., `python:3.10-slim` for python projects or `ubuntu:22.04` for general purpose linux environments) 
* Install required packages and dependencies  
* Define the entry point for your main script (e.g., `CMD ["python", "script.py"]`)  
* Use multi-stage builds to optimize image size if needed  

With {% tool "apptainer" %}, you can build containers from existing Docker images using:

```bash
apptainer build my_container.sif docker://python:3.10-slim
```

#### 2. Run containers to execute application, experiments or tests

* Use `docker run` or `apptainer exec` to execute your software in a controlled environment.

Example {% tool "docker" %} command:

```bash
  docker run --rm -v /path/to/data:/data my-docker-image:1.0.0 python /data/experiment.py
```
Example {% tool "apptainer" %} command:
```bash
apptainer exec my-container.sif python /data/experiment.py
```

* Expose ports to run interactive services or web applications inside the container.

Example {% tool "docker" %} command:

```bash
docker run -p 8080:80 my-docker-image:1.0.0
```
Example {% tool "apptainer" %} command:
Apptainer generally does not support port mapping like Docker, as it is designed primarily for HPC environments. For networked services, Docker is usually preferred.

#### 3. Push and pull images using a container registry

* {% tool "docker" %} push and pull from Docker Hub or GitLab Container Registry.
* Tag and version your images to support reproducibility and traceability.

Example {% tool "docker" %} tag and push command:

```bash
docker tag my-docker-image:1.0.0 username/my-docker-image:1.0.0
docker push username/my-docker-image:1.0.0
```
Example {% tool "docker" %} pull command:

```bash
docker pull username/my-docker-image:1.0.0
```
Example {% tool "apptainer" %} tag, pull and push command:

{% tool "apptainer" %} uses built `.sif` image files and store them in institutional repositories or shared storage. And versioning is managed by naming the `.sif` files accordingly
e.g., `my-container-v1.0.0.sif`

 
#### 4. Use containers in CI/CD pipelines

* Integrate container builds and execution into platforms like GitLab CI.
* Run each job inside a clean, isolated container environment.  
* Ensures consistent building, testing, and documentation across different systems.

Example CI {% tool "docker" %}:

```yaml
pytest:
  stage: test
  image: my-docker-image:1.0.0 # Your custom Docker image
  before_script:
    - pip install -r requirements.txt  # Install additional dependencies if not already included in the image
  script:
    - python -m unittest discover tests/ 
```
Example CI {% tool "apptainer" %}:

```yaml
pytest:
  stage: test
  image: docker://my-docker-image:1.0.0  # Your custom Docker image
  before_script:
    - pip install -r requirements.txt  # Install additional dependencies if not already included in the image
  script:
    - apptainer exec my-container-v1.0.0.sif python -m unittest discover tests/
```

## References

[Docker documentation]: https://docs.docker.com/get-started/docker-overview/
[Docker reference docs for CLI, APIs, and platform behaviors]: https://docs.docker.com/reference/
[RedHat containerization]: https://www.redhat.com/en/topics/containers
[Apptainer user guide]: https://apptainer.org/docs/user/latest/index.html