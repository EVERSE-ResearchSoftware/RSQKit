---
title: Licensing software
description: How to apply a license to research software
contributors: ["Daniel Garijo", "Aleksandra Nenadic", "Shoaib Sufi"]
page_id: licensing_software
related_pages: []
---

## What is copyright and licensing?

Copyright allows a creator to state that they own the work they have created. This declaration is optional - even if the creator 
does not explicitly assert it, copyright of the work exists from the moment of creation. 
A license is a legal document which sets down the terms under which the creator is releasing what they have created for others to use, modify, extend or exploit. 


## Why should you assign a license to your research software? 

### Description 

A license defines what others are allowed to do with your software. This will take into account ownership rights (copyright).

There are large differences between how copyrights and subject rights are to be addressed.

Complying with copyright is primarily the responsibility of the user of the software. 
Copyright laws allow only the creator of a work to reproduce and use it. If anyone else wants to use the work, then that person needs explicit permission from the holder of the copyright. 
A license describes the nature of this agreement, and does not need a signature: the user can never deny the existence of any conditions, because without the license they would not be able to use the work at all.

Licensing is an important aspect of meeting the principle of reusability (the R in FAIR) in FAIR for Research Software (R1.1. Software is given a clear and accessible license[^1]). 
As part of the publication process, you need to decide under which license your software is made available to others. 
If this information is not provided, people will not be able to legally reuse your software, even if this was not your intention.


### Considerations

* It is useful to have a basic understanding of intellectual property terms and how copyrights (who owns) and licensing (what others can do with the IP of others) are. 
    * There are some good guides on the [qLegal website](https://www.qmul.ac.uk/qlegal/clients/resourcehub/ip/) for the UK context.
* If you are producing software and make it available to others, you should be explicit about what others are allowed to do with it. A document describing that is called a license.
* If you are reusing software that comes from somewhere, you will want to have a license that explains what you can do with it. Without a license the right to reuse software is undefined and is likely to be illegal.
* Note that smaller contributions to software may not be subject to copyright 
* Be sure of the ownership of intellectual property before publishing software.
    * Are there rights belonging to a third party?
    * As an employee your employer is likely to own all intellectual property related to your work - do you need to get permission
    * You may have specified how software will be made available in grants which fund the work - so making things open will be a condition of the grants and this will usually not require you to gain further permission from your organisation.


### Solutions

* Make your research software available under an appropriate license, which defines the constraints on using the software.
* Choose a license that ensures your software is correctly attributed and makes the terms of reusing your software explicit to the user.

## What license should you apply to your research software? 

### Description

What license to choose for your research software depends on the license of other people’s software you are including in your work (dependencies of your software) 
and also how you want this new combined work to be available to others. 
In addition, it might be governed by your employer policy or funders’ mandates - as mentioned above, your employer is likely to own all intellectual property over the work you produce while in employment.

There are a number of licenses that conform to the [open source definition](https://opensource.com/resources/what-open-source). 
Here are the most commonly used ones that will likely satisfy your needs.

#### Public domain

While not strictly a license, [public domain](https://en.wikipedia.org/wiki/Public_domain) is a concept that enables you to waive all your interests that may 
exist in your work and declare your work not protected by copyright. 
The [public domain](https://en.wikipedia.org/wiki/Public_domain) consists of all the creative work to which no exclusive intellectual property rights apply. 
Because no one holds the exclusive rights, anyone can legally use or reference those works without permission. 
Note that not having a license is not the same as releasing your work into the public domain - the former means no one can reuse your work whereas the latter means everyone can. 
For software, this may mean using an [unlicense](https://unlicense.org/) - a template for dedicating your software to the public domain.

#### Permissive licenses 

Permissive licenses impose minimal restrictions on the use and redistribution of covered software. Broadly speaking, these licenses require anyone redistributing the code 
to only include the license text and a copyright statement crediting the authors. 
This allows software released under these licenses to also be made into part of closed source programs.

The most commonly used and popular choices of permissive licenses include the [MIT license](https://en.wikipedia.org/wiki/MIT_License), 
the [BSD licenses](https://en.wikipedia.org/wiki/BSD_licenses) (there are a few variants) and the [Apache 2.0 license](https://en.wikipedia.org/wiki/Apache_License#Apache_License_2.0).

The MIT and BSD licenses are very simple and generally state that anybody receiving the software can copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software to anybody they like. 
The Apache 2.0 license is also similar, but also includes clauses about patent licensing which require any contributor to a program which is licensed under Apache 2.0 to allow their patents to be used free of charge by any user of the software.

#### Copyleft licenses

Copyleft licenses are a family of open source licenses that require any modifications, copies or redistributions of the original work be released under a compatible copyleft license. 
This can cause complications when combining code that is under copyleft with other licenses as now the entire new codebase must be released under the copyleft license. 
If there are any incompatible terms in the other license used  then this can prevent the two codebases from being combined.

The main advantage of copyleft licenses is that anyone who incorporates the code into another product must also keep that product open and this makes it harder for it to be subsumed 
into a commercial product that does not contribute improvements to the code back to the community which created it.

The most commonly known copyleft license is the [GNU Public License or GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License) (has several versions and used by a lot of popular software including the Linux kernel). 
Compared with the permissive licenses, GPL is quite a long license agreement and many of its clauses can be quite difficult for non-lawyers to fully understand. 

[GNU Lesser General Public License ](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) (LGPL) - a special version of GPL - 
allows developers and companies to use and integrate a software component released under the open source LGPL into their own (even proprietary) software without being required by the terms of a strong copyleft license 
to release the source code of their own components (which is the requirement of GPL). GPL requires that all its derivative works be licensed as a whole under the terms of the GPL. 
If an application links to a library licensed under GPL, it must also be licensed under GPL and the source code of the application must be provided. By contrast, libraries licensed under the LGPL may be linked to proprietary applications. 
If linked statically, the application code must also be released as LGPL, or everything that allows the user to re-link the application with a different version of the LGPL source code must be provided. 
As long as the application is linked dynamically to LGPL software, the proprietary code can be kept proprietary.

[GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License) (AGPL) is designed to address the issue for GPL software running on remote web servers - 
users are not receiving copies of such software on their machines but are interacting with them over computer networks and hence the person running the web server has no obligation to supply users with the source code. 
The AGPL requires that people running web applications licensed under the AGPL need to make the source code of such applications available to their users. 

#### Creative Commons licenses

All of the licenses we have  discussed so far are really only intended for source code. 
They are not suitable for documentation, datasets, drawings, logos, music, maps, etc. - which you may want to include as part of your software project. 
To solve this problem there are the [Creative Commons (CC) licenses,](https://creativecommons.org/share-your-work/cclicenses/) which are expressly built for anything other than source code. 

The CC licenses grant some of the following baseline rights:

* Attribution (BY) - all the Creative Commons licenses require you to give credit to the original creator (so all will have the BY component). This is very similar to what is required by all of the permissive code licenses.
* Share-Alike (SA) - requires any derivative works to be released under a compatible creative commons license. This is very similar to the way that copyleft licenses work.
* Non-Commercial (NC) - only allow for non-commercial use of the work.
* No Derivatives (ND) - users of the work cannot redistribute modified versions of it.

Combinations of various rights that are granted give us the following six Creative Commons licenses:

* [CC BY](https://creativecommons.org/licenses/by/4.0/) - Creative Commons Attribution
* [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) - Creative Commons Attribution Share Alike
* [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/) - Creative Commons Non Commercial
* [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) - Creative Commons Non Commercial Share Alike
* [CC BY-ND](https://creativecommons.org/licenses/by-nd/4.0/) - Creative Commons No Derivatives
* [CC BY-ND-NC](https://creativecommons.org/licenses/by-nc-nd/4.0/) - Creative Commons No Derivatives Non Commercial

In addition to the licenses above, Creative Commons also offers [CC0](https://creativecommons.org/publicdomain/zero/1.0/) - a public dedication tool, which enables creators to give up their copyright and put their works into the worldwide public domain. 

### Considerations

* Are you reusing code which is already under an open source license? What obligations do you have under those licenses?
* Do you want to ensure that anybody modifying and redistributing your code will release the source code of their changes?
* Do you want to ensure the least number of restrictions and that your code will be used as widely as possible? Even if that means it might end up in commercial products that do not release their source code and do not compensate you.
* Is there a preferred license used in your research community?
* Do not be tempted to write your own license (or modify an existing one) unless you are a copyright lawyer.
* Remember that the rights granted in a license cannot be revoked once it has been applied.


### Solutions

* [Choose an open license](https://choosealicense.com/) website is a great tool to help you choose a license that is appropriate for your needs.

## How do I add a license to my code repository?

### Description 

Once you have decided on the license to choose, you may add it as part of your code base. 
This is usually done by adding a file LICENSE with the text of the license. LICENSE.txt or LICENSE.md or LICENCE.txt or LICENCE.md are also commonly used variations for the license file name.


### Considerations 


### Solutions 

* If your software is located in GitHub, follow [GitHub's documentation for adding a license](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository).
Otherwise, create a new file called, e.g. LICENSE, in the root directory to your code base and copy the text of your chosen license into it.
* See an example from the [RSQkit](https://github.com/EVERSE-ResearchSoftware/RSQKit) which uses the Apache 2.0 license: [https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/LICENSE](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/LICENSE). 


## Tools and resources

| Tool or resource                                                                                            | Description                                                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [Choose an open license tool](https://choosealicense.com/)                                                  | A guided tool to help you choose a license for your resource  |
| [license selector for software](https://ufal.github.io/public-license-selector)                             | A question-guided tool to help you choose a software license  |
| [Spdx](https://spdx.org/licenses/) list of licenses                                                         | A list of commonly recognised licenses used in software       |
| [OpenSource guide](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project) | Guidelines on changing and editing licenses                   |


## How to cite this page

To be added.


## Credit

The contents of this page have been adapted from the ["Licensing" activity page](https://rdmkit.elixir-europe.org/licensing) in the [Research Data Management Kit (RDMKit)](https://rdmkit.elixir-europe.org/), contributed by Minna Ahokas, Nicola Soranzo, Rob Hooft and Siiri Fuchs.

      
## References

[^1]: [https://zenodo.org/records/6623556#.YqCJTJNBwlw](https://zenodo.org/records/6623556#.YqCJTJNBwlw) page 12

 
