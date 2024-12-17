---
title: Environmental sustainability of research software
description: Guide to improving environmental sustainability of software
contributors: ["Kirsty Pringle"]
page_id: environmental_sustainability

related_pages: [<!---REPLACE THIS with the page comma-separated page IDs of the pages that are related to the current page--->]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---
<!-- Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page. -->

## How to monitor and reduce the environmental impact of my software? 
 
### Description 

There is an urgent need to reduce the environmental impact of our activities, and research is no exception.  Many research institutes and funders have committed to achieving Net Zero (essentially a 90% reduction in carbon equivalent emissions) by 2050 or earlier.  There are a range of tools and practices which researchers can adopt to reduce the environmental impact of their software.

### Considerations 

While vital for society, research is a significant source of carbon emissions.  Thankfully there are a number of steps which can be taken to reduce emissions. 

The Green Software Foundation suggests three aspects to consider:

1. Energy efficacy - design software to consume as little energy as possible.
2. Hardware efficiency - use the least amount of embodied carbon as possible.
3. Carbon awareness - do more when the energy supply is clean and less when it is dirty.

There are a number of tools and programming techniques which can be used to first monitor then improve the energy efficiency of software (detailed below).  Hardware efficacy considers emissions from the creation and disposal of the hardware used (embodied emissions), this can be maximised by extending the lifetime of hardware and (for cloud and HPC) increasing the utilisation of the device.  Finally, the amount of clean electricity in an energy supply depends on location and time of the use. Software that is carbon aware tries to shift usage away from energy that is low in clean energy, through shifting in either time or space. 

Similarly, the GREENER software principles ([https://www.nature.com/articles/s43588-023-00461-y](https://www.nature.com/articles/s43588-023-00461-y)) sets out a series of principles to help guide the  transition to more environmentally responsible computing including:

* Governance and Responsibility: All stakeholders, including grassroots movements, institutions, funding bodies, and industry partners, must take responsibility for reducing greenhouse gas (GHG) emissions in computational science. Both top-down and bottom-up approaches are necessary.
* Estimation: It is crucial to estimate and report the energy consumption and carbon footprints of computational processes to identify inefficiencies and raise awareness of environmental impacts.
* Energy and Embodied Impacts: Reducing the carbon intensity of computing requires addressing both operational energy consumption and the environmental cost of manufacturing hardware. Geographic location, hardware procurement, and data storage play significant roles.
* New Collaborations: International cooperation is vital to ensure that researchers, particularly in low- and middle-income countries, have access to low-carbon computing resources.
* Education and Research: Raising awareness about sustainable computational practices through training and integrating sustainability into educational curricula is essential. Research must also focus on creating energy-efficient algorithms and technologies.
  

### Solutions

* Training
    * Green software foundation provides a [free course](https://learn.greensoftware.foundation/introduction) that introduces the basic concepts including embodied carbon, carbon intensity, demand shifting (and shaping) and measurement approaches. The course takes about 2 hours to complete. 
    * green-coding.io provide (paid for) [workshops & training](https://www.green-coding.io/services/workshops-and-trainings) that focus on energy-efficient coding, environmentally responsible software design, and practical tools 
* Certification
    * [GreenDiSC](https://www.software.ac.uk/GreenDiSC) is a certification scheme for research groups (and central sustainability teams) that focuses on hardware and software.  
    * [Green IT Professional (GITP)](https://ifgict.org/green-it-professional-gitp/) is a personal certification program that covers green ICT standards, carbon footprint calculation, and life cycle assessments. 
* Evaluation Frameworks
    * [Software Carbon Intensity (SCI) Specification](https://greensoftware.foundation/standards/sci) is an assessment framework for assessing and reducing software carbon intensity.
* Tools to monitor emissions
    * [CodeCarbon](https://codecarbon.io/) estimates the CO2 emissions from computing resources used by software. 
    * [Green Algorithm](http://www.green-algorithms.org) is an online tool to estimate the carbon footprint of computational tasks using a web calculator. Currently being extended for use on HPC platforms. 
    * Carbontracker is a tool that monitors and predicts energy and carbon footprint for training machine learning models.
    * [EcoInfo](https://ecoinfo.green) (formerly Greenspector) measures energy usage and resource efficiency in web and mobile applications.
    * [EcoGrader](https://www.ecograder.com) evaluates website sustainability based on design and operational efficiency.


## How to cite this page <!-- do not delete this heading and write your text below it -->
TODO

## Tools and resources <!-- do not delete this heading and write your text below it -->
TODO

## References <!-- do not delete this heading and write your text below it -->
TODO
 
