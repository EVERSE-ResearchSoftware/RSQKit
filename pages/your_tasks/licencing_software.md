---
title: Licensing software
search_exclude: true
description: Applying a licence to research software
contributors: ["Daniel Garijo", "Aleksandra Nenadic", "Shoaib Sufi"]
page_id: licencing_software
related_pages: [<!---REPLACE THIS with the page comma-separated page IDs of the pages that are related to the current page--->]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->

## What is copyright and licensing?

Copyright allows a creator to state that they own the work they have created. This declaration is optional - even if the creator 
does not explicitly assert it, copyright of the work exists from the moment of creation. 
A licence is a legal document which sets down the terms under which the creator is releasing what they have created for others to use, modify, extend or exploit. 


## Why should you assign a licence to your research software? 

### Description 

A licence defines what others are allowed to do with your software. This will take into account ownership rights (copyright).

There are large differences between how copyrights and subject rights are to be addressed.

Complying with copyright is primarily the responsibility of the user of the software. 
Copyright laws allow only the creator of a work to reproduce and use it. If anyone else wants to use the work, then that person needs explicit permission from the holder of the copyright. 
A licence describes the nature of this agreement, and does not need a signature: the user can never deny the existence of any conditions, because without the licence they would not be able to use the work at all.

Licensing is an important aspect of meeting the principle of reusability (the R in FAIR) in FAIR for Research Software (R1.1. Software is given a clear and accessible licence[^1]). 
As part of the publication process, you need to decide under which licence your software is made available to others. 
If this information is not provided, people will not be able to legally reuse your software, even if this was not your intention.


### Considerations

* It is useful to have a basic understanding of intellectual property terms and how copyrights (who owns) and licensing (what others can do with the IP of others) are. 
    * There are some good guides on the [qLegal website](https://www.qmul.ac.uk/qlegal/clients/resourcehub/ip/) for the UK context.
* If you are producing software and make it available to others, you should be explicit about what others are allowed to do with it. A document describing that is called a licence.
* If you are reusing software that comes from somewhere, you will want to have a licence that explains what you can do with it. Without a licence the right to reuse software is undefined and is likely to be illegal.
* Note that smaller contributions to software may not be subject to copyright 
* Be sure of the ownership of intellectual property before publishing software.
    * Are there rights belonging to a third party?
    * As an employee your employer is likely to own all intellectual property related to your work - do you need to get permission
    * You may have specified how software will be made available in grants which fund the work - so making things open will be a condition of the grants and this will usually not require you to gain further permission from your organisation.


### Solutions

* Make your research software available under an appropriate licence, which defines the constraints on using the software.
* Choose a licence that ensures your software is correctly attributed and makes the terms of reusing your software explicit to the user.

## What licence should you apply to your research software? 

### Description

What licence to choose for your research software depends on the licence of other people’s software you are including in your work (dependencies of your software) 
and also how you want this new combined work to be available to others. 
In addition, it might be governed by your employer policy or funders’ mandates - as mentioned above, your employer is likely to own all intellectual property over the work you produce while in employment.

There are a number of licences that conform to the [open source definition](https://opensource.com/resources/what-open-source). 
Here are the most commonly used ones that will likely satisfy your needs.

#### Public Domain

While not strictly a licence, [public domain](https://en.wikipedia.org/wiki/Public_domain) is a concept where you wish to waive all your interests that may 
exist in your work and your work is not protected by copyright. 
The [public domain](https://en.wikipedia.org/wiki/Public_domain) consists of all the creative work to which no exclusive intellectual property rights apply. 
Because no one holds the exclusive rights, anyone can legally use or reference those works without permission. 
Note that not having a licence is not the same as releasing your work into the public domain - the former means no one can reuse your work whereas the latter means everyone can. 
For software, this may mean using an [unlicence](https://unlicense.org/) - a template for dedicating your software to the public domain.

#### Permissive licences 

Permissive licences impose minimal restrictions on the use and redistribution of covered software. Broadly speaking, these licences require anyone redistributing the code 
to only include the licence text and a copyright statement crediting the authors. 
This allows software released under these licences to also be made into part of closed source programs.

The most commonly used and popular choices of permissive licences include the [MIT licence](https://en.wikipedia.org/wiki/MIT_License), 
the [BSD licences](https://en.wikipedia.org/wiki/BSD_licenses) (there are a few variants) and the [Apache 2.0 licence](https://en.wikipedia.org/wiki/Apache_License#Apache_License_2.0).

The MIT and BSD licences are very simple and generally state that anybody receiving the software can copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software to anybody they like. 
The Apache 2.0 licence is also similar, but also includes clauses about patent licensing which require any contributor to a program which is licensed under Apache 2.0 to allow their patents to be used free of charge by any user of the software.

#### Copyleft licences

Copyleft licences are a family of open source licences that require any modifications, copies or redistributions of the original work be released under a compatible copyleft licence. 
This can cause complications when combining code that is under copyleft with other licences as now the entire new codebase must be released under the copyleft licence. 
If there are any incompatible terms in the other licence used  then this can prevent the two codebases from being combined.

The main advantage of copyleft licences is that anyone who incorporates the code into another product must also keep that product open and this makes it harder for it to be subsumed 
into a commercial product that does not contribute improvements to the code back to the community which created it.

The most commonly known copyleft licence is the [GNU Public License or GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License) (has several versions and used by a lot of popular software including the Linux kernel). 
Compared with the permissive licences, GPL is quite a long licence agreement and many of its clauses can be quite difficult for non-lawyers to fully understand. 

[GNU Lesser General Public License ](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)(LGPL) - a special version of GPL - 
allows developers and companies to use and integrate a software component released under the open source LGPL into their own (even proprietary) software without being required by the terms of a strong copyleft licence 
to release the source code of their own components (which is the requirement of GPL). GPL requires that all its derivative works be licensed as a whole under the terms of the GPL. 
If an application links to a library licensed under GPL, it must also be licensed under GPL and the source code of the application must be provided. By contrast, libraries licensed under the LGPL may be linked to proprietary applications. 
If linked statically, the application code must also be released as LGPL, or everything that allows the user to re-link the application with a different version of the LGPL source code must be provided. 
As long as the application is linked dynamically to LGPL software, the proprietary code can be kept proprietary.

[GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License) (AGPL) is designed to address the issue for GPL software running on remote web servers - 
users are not receiving copies of such software on their machines but are interacting with them over computer networks and hence the person running the web server has no obligation to supply users with the source code. 
The AGPL requires that people running web applications licensed under the AGPL need to make the source code of such applications available to their users. 

#### Creative Commons licences

All of the licences we have  discussed so far are really only intended for source code. 
They are not suitable for documentation, datasets, drawings, logos, music, maps, etc. - which you may want to include as part of your software project. 
To solve this problem there are the [Creative Commons licences,](https://creativecommons.org/share-your-work/cclicenses/) which are expressly built for anything other than source code. 

There are several different types of Creative Commons licences:

* CC0 - Creative Commons Zero or CC0 is the simplest licence and is effectively a public domain licence, but is suitable for use world wide.
* Attribution (BY) - all the Creative Commons licences apart from CC0 require you to give credit to the original creator. This is very similar to what is required by all of the permissive code licences.
* Share-a-like (SA) - requires any derivative works to be released under a compatible creative commons licence. This is very similar to the way that copyleft licences work.
* Non-Commercial (NC) - only allow for non-commercial use of the work.
* No Derivatives (ND) - users of the work cannot redistribute modified versions of it.

Combinations of Creative Commons Licences are also possible:

* CC-BY - Creative Commons Attribution
* CC-BY-SA - Creative Commons Attribution Share Alike
* CC-BY-NC - Creative Commons Non Commercial
* CC-BY-NC-SA - Creative Commons Non Commercial Share Alike
* CC BY-ND - Creative Commons No Derivatives
* CC BY-ND-NC - Creative Commons No Derivatives Non Commercial

### Considerations

* Are you reusing code which is already under an open source licence? What obligations do you have under those licences?
* Do you want to ensure that anybody modifying and redistributing your code will release the source code of their changes?
* Do you want to ensure the least number of restrictions and that your code will be used as widely as possible? Even if that means it might end up in commercial products that do not release their source code and do not compensate you.
* Do not be tempted to write your own licence (or modify an existing one) unless you are a copyright lawyer.
* Remember that the rights granted in a licence cannot be revoked once it has been applied.


### Solutions

* [Choose an open licence](https://choosealicense.com/) website is a great tool to help you choose a licence that is appropriate for your needs.

## How do I add a licence to my code repository?

### Description 

Once you have decided on the licence to choose, you may add it as part of your code base. 
This is usually done by adding a file LICENSE with the text of the licence. LICENSE.txt or LICENSE.md or LICENCE.txt or LICENCE.md are also commonly used variations for the licence file name.


### Considerations 


### Solutions 

* Copy the appropriate licence text into a, e.g. LICENCE.txt file, and deposit this file in the root level of your code base so as to apply it to the whole software project and
  it can be easily seen by third parties and users of your software.
* To add a licence file to a repository on GitHub, follow [GitHub's documentation](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository).
* See an example from the [RSQkit](https://github.com/EVERSE-ResearchSoftware/RSQKit), which uses the Apache 2.0 licence: [https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/LICENSE](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/LICENSE). 


## Tools and resources

| Tool or resource                                                                                            | Description                                             |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [Choose an open licence tool](https://choosealicense.com/)                                                  | A guided tool to help you choose a licence              |
| [Spdx](https://spdx.org/licenses/) list of licenses                                                         | A list of commonly recognized licenses used in software |
| [OpenSource guide](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project) | Guidelines on changing and editing licenses             |


## How to cite this page

To be added.

## Contributors (fixed heading)

* Daniel Garijo
    * orcid: https://orcid.org/0000-0003-0454-7145
    * github: https://github.com/dgarijo
    * affiliation: Universidad Politécnica de Madrid
* Aleksandra Nenadic
    * orcid: https://orcid.org/0000-0002-2269-3894
    * github: https://github.com/anenadic
    * affiliation: University of Manchester
* Shoaib Sufi
    * orcid: https://orcid.org/0000-0001-6390-2616
    * github: https://github.com/shoaibsufi
    * affiliation: University of Manchester
      
## References

[^1]: [https://zenodo.org/records/6623556#.YqCJTJNBwlw](https://zenodo.org/records/6623556#.YqCJTJNBwlw) page 12

 
