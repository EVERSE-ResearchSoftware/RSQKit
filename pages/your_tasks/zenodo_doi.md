---
title: Digital Software Identifiers (DOI) for Software
description: Obtaining a DOI via Zenodo for software 
contributors: ["Shoaib Sufi", "Daniel Garijo"] 
page_id: zenodo_doi
related_pages:
  your_tasks: [releasing_code]
---

## What is a Digital Object Identifier?

A Digital Object Identifier (DOI) is a [persistent identifier][what-are-pids] or a handle used to uniquely identify 
various objects, such as journal articles, research reports, dataset or software, standardised by the International 
Organization for Standardisation (ISO).

A DOI fits within the URI (Uniform Resource Identifier) system, and also resolves to its target - the information 
object to which the DOI refers. 
This is achieved by binding the DOI to metadata about the object, such as a URL where the object is located. 

Obtaining a DOI for software has become [increasingly popular][datacite-doi-software] to indicate to others how to
cite your software (either in a publication or as an independent way of referring to your software).

There are many services that can "mint" DOIs, i.e. perform the process of creating and assigning a DOI to an object.
We will explore how you can do that for your software using {% tool "zenodo" %}, a general-purpose open archive and 
publishing repository developed under the European OpenAIRE program and operated by CERN.

## How can I get a Digital Object Identifier (DOI) for code using Zenodo?

### Description 

Zenodo's DOI versioning feature allows users to create a **concept DOI** (which represents the software package as a 
whole, including all its versions) and multiple **release DOIs** for software packages (with each DOI representing a 
specific version of the software package).
In other words, the concept DOI is a reference to a software project as a whole, while the software version DOI is a 
reference to a particular software release.

### Considerations 

* While this is not mandatory, using {% tool "github" %} as your software repository can help with issuing DOIs for your software due to its integration with Zenodo.
If you are not using GitHub, you will need to upload each software version to Zenodo manually.
* You want to publish a software release of your code (e.g. using [semantic versioning][semantic-versioning]).
* You need an account on {% tool "zenodo" %} and you can create is using your GitHub account (effectively linking the two). 
If you already have a Zenodo account that is not linked to your GitHub account - you can always link them from Zenodo later.

### Solutions 

* If you do not have a Zenodo account - create a Zenodo account now preferably with your GitHub account.
* If you already have a Zenodo account, link your GitHub account to Zenodo as follows:
	* Go to Zenodo website.
	* Navigate to your [Zenodo profile page](https://zenodo.org/account/settings/profile).
	* Select the `GitHub` tab, then click on `Connect`.
	* Authorise Zenodo to access your GitHub account
	* Choose which repository you would like to create a DOI for under the repositories sections
		* You may need to scroll down to find the repository if you have access to many repositories
* From Github, [create a release](./releasing_code) for the software repository you have enabled: 
	* Go to your repository software repository on GitHub.
	* Click on `Releases` and then `Draft a new release` button.
	* Remember to use a version number ([semantic versioning][semantic-versioning] is commonly used  but there are other schemes such as [CalVer][calver] which is date based)
* Zenodo will automatically archive this release due to its integration with GitHub:
	* Once your GitHub repository is linked to Zenodo, any new release you publish on GitHub will be archived by Zenodo.
	* Zenodo will automatically issue a DOI for each new release.
* Get the DOI:
	* After making the release in GitHub, go back to the [GitHub option on Zenodo for your account][your-zenodo-github] where you will see 
  your repository archived with a DOI assigned to it. If you click on it - you will be taken to the Zenodo record for 
  your software. You can see the Zenodo DOI badge under `Details`:

![Badge in Zenodo](../../images/badge_zenodo.png)

* Copy the badge to the README file in your software repository in GitHub:
	* Click on the blue DOI badge - a window will pop up with badge in various formats. 
    * Copy the Markdown version to your README. It will show in GitHub as follows:

![Badge in GitHub repository](../../images/badge_in_repo.png)

Also check:

- [GitHub's Documentation on Referencing and Citing Content][github-referencing-and-citing-content]
- [GitHub Integration FAQ on Zenodo][github-faq-zenodo]
- [Making code citable with Zenodo and GitHub][citable-github-ssi] guide from Software Sustainability Institute


[calver]: https://calver.org/
[citable-github-ssi]: https://www.software.ac.uk/blog/making-code-citable-zenodo-and-github
[datacite-doi-software]: https://datacite.org/blog/doi-registrations-software/)
[doi]: https://www.doi.org/
[github]: https://github.com/
[github-faq-zenodo]: https://support.zenodo.org/help/en-gb/24-github-integration
[github-referencing-and-citing-content]: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
[semantic-versioning]: https://semver.org/ 
[what-are-pids]: https://support.orcid.org/hc/en-us/articles/360006971013-What-are-persistent-identifiers-PIDs
[your-zenodo-github]: https://zenodo.org/account/settings/github/


