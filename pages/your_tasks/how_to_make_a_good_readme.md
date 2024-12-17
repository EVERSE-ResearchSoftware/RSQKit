---
title: Creating README documents for software
description: How to make a good README document for research software projects
contributors: ["Esteban González", "Aleksandra Nenadic", "Daniel Garijo"]
page_id: good_README
related_pages: []
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->

## Why is it important to have a good README file? <!-- example: how to version control my code? -->
 
### Description <!-- do not delete this heading and write your text below it -->

The README file is the entry point to the documentation associated with a software. The main purpose of the README is to:
* Describe the structure of the project and its purpose.
* Facilitate the installation and execution of the software stored in the repository.
* Detail the use of the software.

In the case of research software, additional features must be taken into account:
* Document the process to reproduce/replicate of experiments.
* Citation information (it can be included in the file or in an additional file)
* Relation with other research outputs such as publications, datasets, etc. These research outputs can be in the repository or in external repositories.


### Considerations <!-- do not delete this heading and write your text below it -->
* A good README favours the use of your software[^1].
* A good README increments the transparency of your research.
* A good README will help you to maintain the software during the software lifecycle.
 

## Which sections should be addressed in a good README? <!-- example: how to name a software release? -->
 
### Description <!-- do not delete this heading and write your text below it -->
A README file is the first document that a researchers read when they are interested on using a software. For this reason, should contain all the relevant information to install and to execute it. It includes references to additional information such as API documentation, specifications, scientific publications related, tutorials, guidelines, etc.

A basic software documentation emphasises these aspects[^2] :
* Understandability: a user can comprehend the structure and the purpose of the software.
* Usability: a user can understand how to use the software.
* Attribution: how a user should cite the software.

These aspects should be addressed in different sections of the README. 

### Considerations <!-- do not delete this heading and write your text below it -->
* A good README should describe the purpose and the features of the software.
* A good README should describe how to execute and to use the code. 
* In a research context, a good README should indicate how the software should be cited.
* In a research context, a good README should indicate the funding agency and the proper acknowledgements.
* In the context of a scientific experiment, a good README should facilitate its reproducibility.

### Solutions <!-- do not delete this heading and write your text below it -->

The following sections can be included in the README to facilitate the use of the software and to allow its citation.

**Description**

In this section, you will have to describe the purpose and the features of your software.

**Requirements**

In this section, you can include the requirements needed to install and to execute the software. These requirements can be software (e.g. operative system) or hardware (e.g. CPU, memory, etc.). There is no need to include low level requirements like language library dependencies. These requirements must be provided with the appropriate mechanism of each language. For example, in Python by using the requirements.txt file. 

This is a non exhaustive list of requirements categories that you can consider:
- Operating system version
- Operating system libraries version 
- Version of the interpreter (e.g. Python 3.9, Java 7, etc.)
- Additional software needed to execute the software. For example, a database, a workflow engine, etc.
- Infrastructure requirements (e.g. number of CPUs, memory, disk, etc.)  

**Installation process**

In this section, you can describe the installation steps needed to install the software. You have to assume that the user has no knowledge about operative systems or programming languages, so you need to be exhaustive. It is important to reflect all the commands that must be executed by the user.

In case you need to install additional software, like a Java Virtual Machine or a database, you will have to add a link to additional information that describes how to install it. 

If you have multiple options for installing the software (e.g. installing a library, docker, script) you should describe them.

**Configuration**

Sometimes, software needs to be configured to be executed. Usually, this task is done by filling in a configuration file. You will need to add this information to the README. In case you have documentation that describes the fields of the configuration file, you can also add it to the README.

**Usage**

In this section, you should include all the steps needed to use the application. For example, if it is a command line tool, you will need to describe all the parameters. As we mentioned in the installation section, you have to assume no skills in the user, so you will need to be exhaustive.

It is recommended to add examples of the application usage in order to illustrate users in the software management. This information can be complemented with links to tutorials in different formats (e.g. video, PDF, notebooks, etc.)  

Research software can be developed to execute experiments whose results are shown in a scientific publication. For this reason, and to add transparency to the research, it is important to show how the results can be achieved. You can use this section to describe the process to get the results. 

**Contribution**

Research software should be a collaborative effort, so a mechanism to allow other researchers to collaborate with the project is needed. In this section, you can describe how this mechanism is. For example, if you want to add a new feature, you can create a pull request to integrate this new feature.

**Acknowledgement**

All funders of the research software should be mentioned in the README - check the acknowledgement policy of each institution for how best to do it.

**Citation**

Citation is fundamental in a research context. In this section, you can add how you want your software to be cited in a publication. It is a common practice to add this information in a `CITATION.cff` file but it is a recommended practice to add it to the README file too (e.g., in Bibtex format). 

Remember that you can include badges in your README file to add visual information about your software project. You can see a list of them used to make your project more fair in the [Howfairis project](https://github.com/fair-software/howfairis). 

**License**

Software without a license cannot be reused in other applications. While having a [license file](https://everse.software/RSQKit/licensing_software) is a common practice in code repositories, you may also add this information explicitly as a section of your README file. For more information, see [our guidelines](https://everse.software/RSQKit/licensing_software) on how to select an appropriate license.


## How to cite this page <!-- do not delete this heading and write your text below it -->
<!--González E., [URL](https://everse.software/RSQKit/good_README). October, 16th 2024-->
TO DO


## Tools and resources <!-- do not delete this heading and write your text below it -->
* [README best practices](https://tilburgsciencehub.com/topics/collaborate-share/share-your-work/content-creation/readme-best-practices/)
* [Guidelines for creating a README file](https://data.4tu.nl/s/documents/Guidelines_for_creating_a_README_file.pdf)
* [SOMEF](https://github.com/KnowledgeCaptureAndDiscovery/somef). SOMEF is a tool to extract information from README files. It is not an assessment tool for README files, but can be used for detecting missing parts of a README file. 
* [Howfairis](https://github.com/fair-software/howfairis) 

## References <!-- do not delete this heading and write your text below it -->
[^1]:Wang, T., Wang, S., & Chen, T. H. P. (2023). Study the correlation between the readme file of GitHub projects and their popularity. Journal of Systems and Software, 205, 111806.
[^2]: Mao, A., Garijo, D., & Fakhraei, S. (2019, December). SoMEF: A framework for capturing scientific software metadata from its documentation. In 2019 IEEE International Conference on Big Data (Big Data) (pp. 3032-3037). IEEE.

 
