---
title: FAIR Research Software
---


## FAIR Research Software

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to
increase the visibility and usefulness of your research to others.
The FAIR data principles, first published [in 2016][fair-data-principles], are widely known and applied today.
Similar [FAIR principles for software][fair-principles-research-software] have now been defined too. In general, they mean:

* **Findable** - software and its associated metadata must be easy to discover by humans and machines.
* **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols, free and legally usable.
* **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through
  standardised protocols and application programming interfaces (APIs).
* **Reusable** - software should be usable (can be executed) and reusable
  (can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below.
This is not an exact science, and by all means the list below is not exhaustive,
but any of the practices that you employ in your research software workflow will bring you
closer to the gold standard of a fully reproducible research.

* Findable
  * Create a description of your software
  * Place your software in a public software repository (and ideally register it in a [software registry](https://github.com/NLeSC/awesome-research-software-registries))
  * Use a unique and persistent identifier (DOI) for your software (e.g. by depositing your code on Zenodo), 
  which is also useful for citations - note that depositing your data/code on GitHub and similar software repositories 
  may not be enough as they may change their open access model or disappear completely in the future
* Accessible
  * Make sure people can freely, legally and easily get a copy your software
  * Structure your code using common patterns and use coding conventions to make your code readable and understandable by people (once they obtain a copy of it)
* Interoperable
  * Explain the functionality of your software
  * Use standard formats for inputs and outputs
  * Communicate with other software via standard protocols and APIs
* Reusable
  * Document your software (including its functionality, and how to install and run it)
  * Follow best practices for software development (including coding conventions, code readability and verifying its correctness)
  * Test your software and make sure it works on different platforms/operating systems
  * Give a licence to your software clearly stating how it can be reused
  * State how to cite your software
 
  
## Tools 


There is a number of tools and practices to help us develop research software in a FAIR way.


[fair-principles-research-software]: https://www.nature.com/articles/s41597-022-01710-x
[fair-data-principles]: https://www.nature.com/articles/sdata201618
