---
title: "Packaging & releasing software" 
search_exclude: false 
description: "How to package and release your software for distribution and reuse?" 
contributors: ["Eva Martín del Pico"] 
page_id: packaging_releasing_software
related_pages:
  tasks: [releasing_software] 
quality_indicators: [has_published_package, software_has_releases]
keywords: ["package software", "packaging software", "releasing software", "release software", "pypi"]
---

## How to publish your software package to a package repository?

### Description

Publishing a software package to a package repository allows other developers to easily install and use it in their projects.
Different programming languages have their own package repositories, such as npm for JavaScript, PyPI for Python, and Maven Central for Java.
Additionally, there are general-purpose registries like GitHub Packages and GitLab Package Registry, which allow storing and distributing packages across multiple ecosystems.

This document specifically covers publishing Python packages to **{% tool "pypi" %} (Python Package Index)** and **GitLab Package Registry**, explaining the differences between these two so developers can decide where to publish their package.

#### Differences Between PyPI and GitHub Packages

* **PyPI**:
  * The official package repository for Python.
  * Packages published here are accessible via pip install.
  * Ideal for public distribution to the Python community.  

* **GitLab Package Registry**:
  * A registry integrated into GitLab, supporting multiple package formats including Python. 
  * Can be used for private package distribution within GitLab projects.
  * Supports CI/CD workflows within GitLab pipelines.

### Considerations

* Provide relevant information in package configuration files (e.g., package.json, pyproject.toml).

* Ensure all dependencies are correctly listed and compatible.

* You can use {% tool "semantic-versioning" %} to indicate changes clearly.

* Include a valid open-source or commercial license and relevant documentation for users. 

* Some repositories require authentication tokens or API keys to publish packages.

* To publish a package in a public repository, you need an account on the respective platform (e.g., npm, PyPI). 

* PyPI allows public package installations without authentication.

* GitLab Package Registry may require authentication to install packages, depending on repository settings. 


### Solutions

* **Publishing a Python package to PyPI**

  * Create a PyPI account at pypi.org and verify your email.

  * Create the package directory:

    ```bash
    mkdir my_python_package && cd my_python_package
    ```

  * Add a Python script (`my_module.py`) that serves as the main module of your package.

  * Create a `setup.py` file:

    ```python
    from setuptools import setup

    setup(
        name='my_python_package',
        version='0.1.0',
        py_modules=['my_module'],
        install_requires=[],
    )
    ```

  * Build the package:

    ```bash
    python setup.py sdist
    ```

  * Create an API token at your [PyPI account settings](https://test.pypi.org/manage/account/).

  * Create a configuration file (`.pypirc`) to store your API token securely (replace `YOUR_PYPI_API_TOKEN` with the token you generated in the previous step): 

    ```bash
    [pypi]
    username = __token__
    password = YOUR_PYPI_API_TOKEN
    ```

  * Install `twine` (allows secure upload to PyPI) and upload the package: 

    ```bash
    pip install twine
    twine upload --verbose --config-file .pypirc dist/*
    ```

  * Your package is now available on PyPI and can be installed using `pip install my_python_package`. 

  * **Using the PyPI Test Server (TestPyPI)**: If you want to test your package upload process without publishing it to the official PyPI, you can use TestPyPI. First, create an account there and generate an API token. Store the token in a `.pypirc` file (replace `YOUR_PYPI_API_TOKEN` with the token you generated in the previous step):
    ```bash
    [testpypi]
    username = __token__
    password = YOUR_PYPI_API_TOKEN
    ``` 

    Then upload your package with:
    ```bash
    twine upload --repository testpypi --verbose --config-file ./.pypirc  dist/* 
    ```  

    You can install the test package using:
    ```bash
    pip install --index-url https://test.pypi.org/simple/ my_python_package
    ```

* **Publishing a Python package to GitLab Package Registry**

  * Ensure you have a GitLab account and a project where the package will be hosted.

  * Generate a **Personal Access Token** in GitLab with `api` scopes (under User settings > Access Tokens). This token is used for authentication when uploading packages.

  * Find your **Project ID** in GitLab. You can locate this in your project settings under General > Project ID. This ID is required to correctly reference the package repository URL.

  * Create or update a `.pypirc` file in your home directory to store GitLab authentication:
    ```
    [distutils]
    index-servers =
        gitlab

    [gitlab]
    repository = https://gitlab.com/api/v4/projects/YOUR_PROJECT_ID/packages/pypi/
    username = __token__
    password = YOUR_GITLAB_ACCESS_TOKEN
    ``` 

  * Build the package:
    ```bash
    python setup.py sdist
    ```

  * Install `twine` and upload the package to GitLab Package Registry:
    ```bash
    pip install twine
    twine upload --repository --verbose gitlab dist/*
    ```

  *  Your package is now available in GitLab and can be installed with:
      ```bash
      pip install --index-url https://gitlab.com/api/v4/projects/YOUR_PROJECT_ID/packages/pypi/simple my_python_package
      ``` 

### Further guidance

- [How to package a Python project](https://py-pkgs.org/03-how-to-package-a-python) 
- [Python Packaging (Carpentries)](https://carpentries-incubator.github.io/python_packaging/)
- [Python 201 on Packaging](https://python-tutorial.dev/201/tutorial/packaging.html#packaging)
- [Managing Academic Software development: Release management](https://southampton-rsg.github.io/swc-project-novice/04-features/index.html)
- [Python Packaging User Guide - Packaging projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [TestPyPI - The Test Python Package Index](https://test.pypi.org/)
- [How to use TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/)
- [Twine - Uploading Python Packages](https://twine.readthedocs.io/en/latest/)
- [Python Packaging User Guide - The `.pypirc file`](https://packaging.python.org/en/latest/specifications/pypirc/)
- [GitLab Documentation - Publish a PyPI package](https://docs.gitlab.com/ee/user/packages/pypi_repository/index.html#publish-a-pypi-package)
- [Python Packaging Authority (PyPA)](https://www.pypa.io/en/latest/)
