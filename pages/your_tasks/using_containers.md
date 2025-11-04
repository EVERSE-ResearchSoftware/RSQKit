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

## Overview

Containers are a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

### Considerations

- The software may depend on specific libraries, versions, or system configurations.
- The code is expected to run across multiple platforms such as different collaborators machines, clusters, or cloud environments.
- Integration of software is required with automated workflows or CI/CD pipelines to ease testing and deployment
- The developed software applications needs ensuring for long term reproducibility and scalability.

## Why should you use containers in software development?

Sharing code with only a README or installation instructions frequently results in “dependency hell,” version mismatches, or broken setups. By contrast, containers package the entire environment including all dependencies and configurations so developer and collaborators can run the exact same setup, on differnt enviornment eliminating these issues.

Containers offer a different approach from coding directly on one platform or operating system. Building an application for a single environment makes moving it elsewhere difficult because the code might not work in the new setting. This often leads to bugs and errors that take extra time to fix, reducing productivity and causing frustration.

When you package an application in a container, you can move it across different platforms and systems. The container includes everything the app needs to run, so it works wherever you take it.

Containers have benefits such as:

- Reproducibility - Containers bundle everything your software needs, so it runs the same everywhere.
- Easy setup - Collaborators, reviewers can get started quickly by just pulling the application build image and run it.
- Version control -  You can tag containers to match specific versions of your code.
- Automation-friendly - Verion controled and containers itself can also be automated with [CI-CD][ci_cd] to keep test and deploymenet steps consistent.
- Lightweight and portable - Uses fewer resources than virtual machines. Works on laptops, servers, or the cloud with no system mismatch issues.

## Containerised Development for Python using Docker

{% tool "docker" %}: is ideal for general-purpose development and cloud deployment.  

### Example: Building a container image

- Choose a base image, e.g., ``python:3.10-slim`` for Python projects or ``ubuntu:22.04`` for general Linux environments.
- Install required packages and dependencies.
- Define the entry point for your main script, e.g., ``CMD ["python", "script.py"]``.
- Use multi-stage builds to optimize image size if needed.

### Example Dockerfile snippet

```
   FROM python:3.10-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   CMD ["python", "script.py"]
```

### Run the container

```
   docker run --rm -v /path/to/data:/data my-docker-image:1.0.0 python /data/experiment.py
```

### Expose ports for interactive services

```
   docker run -p 8080:80 my-docker-image:1.0.0
```

### Push and pull images using a registry

```
   docker tag my-docker-image:1.0.0 username/my-docker-image:1.0.0
   docker push username/my-docker-image:1.0.0
   docker pull username/my-docker-image:1.0.0
```

### Use Docker in CI/CD pipelines

```yaml
pytest:
  stage: test
  image: my-docker-image:1.0.0 # Your custom Docker image
  before_script:
    - pip install -r requirements.txt  # Install additional dependencies if not already included in the image
  script:
    - python -m unittest discover tests/
```

## Containerised Development for Python using Apptainer

{% tool "apptainer" %}: (formerly Singularity) is better suited for HPC environments where users lack root access.
It enables researchers to use containers for reproducible science and large-scale workloads.

### Build a container from a Docker image

```
   apptainer build my_container.sif docker://python:3.10-slim
```

### Run the container

```
   apptainer exec my-container.sif python /data/experiment.py
```

### Push and pull containers

Apptainer uses built ``.sif`` image files, stored in institutional repositories or shared storage.  
Versioning is managed by naming the files accordingly, e.g.:

``my-container-v1.0.0.sif``

### Use Apptainer in CI/CD pipelines

```yaml
pytest:
   stage: test
   image: docker://my-docker-image:1.0.0
   before_script:
      - pip install -r requirements.txt
   script:
      - apptainer exec my-container-v1.0.0.sif python -m unittest discover tests/
```

**Note:**  
Apptainer generally does not support port mapping like Docker.  
For networked services, Docker is usually preferred.

## References

[Docker documentation]: https://docs.docker.com/get-started/docker-overview/
[Docker reference docs for CLI, APIs, and platform behaviors]: https://docs.docker.com/reference/
[RedHat containerization]: https://www.redhat.com/en/topics/containers
[Apptainer user guide]: https://apptainer.org/docs/user/latest/index.html
