---
title: Choosing languages, tools & infrastructures
description: How to decide which programming languages, tools and infrastructures to use?
contributors: ["Patrick Bos"]
page_id: languages_tools_infrastructures
related_pages:
   your_tasks: []
quality_indicators: []
keywords: ["programming language", "software infrastructure", "software tool"]
training:
  - name: "EVERSE TeSS"
    registry: TeSS
    url: "https://everse-training.app.cern.ch"
---

## How to choose programming languages, tools and infrastructures?

There are many different kinds of software-related choices to make over the course of a research software project.
We briefly describe some main categories before going into the considerations of making choices.

Code written in _programming languages_ are the main form of expression of the [research software engineer](research_software_engineer).
Some [examples of programming languages often used in research](#good-default-languages) are listed below.
Like the language of your research articles, the programming language determines not only the contents (i.e. the functionality) of your research software, but also its [readability](writing_readable_code) - depending on how complex the language is and how many people know it - and its expressiveness - which may or may not allow you to formulate your "thoughts" efficiently and effectively and hence may determine the pace of your project.

By _tools_ and _frameworks_ we mean abstraction layers written in certain languages (or with interfaces in certain languages).
These layers typically consist of classes, functions and other structures that are often used for some particular problem or in some particular domain.
Examples are frameworks for web development, like [React](https://react.dev), machine learning, like [PyTorch](https://pytorch.org), workflows and data analysis, like [Galaxy](https://galaxyproject.org), or data processing and statistical modelling, like [ROOT](https://root.cern).
Note that we use this term loosely.
There may well be overlap with terms like "library", "toolkit", "platform" or "API".
The main point is that someone did the work on useful abstractions in a certain domain and that you can use them in your research software or code.

_Infrastructures_ more broadly describe the different kinds of software (or even hardware) that you may want to integrate into or apply in your applications.
These typically require some background knowledge to use in an optimal way.
Examples are database technologies, accelerator hardware programming (e.g. general purpose GPU programming, or programming FPGAs), machine learning, web and user interface design, analytics (statistics, visualisation, etc.), .
Again, the term is used somewhat imprecisely and one may in some cases prefer terms like "expertise" or "skill set" and "tool" or "service" in other cases.
The point is that we speak here of a broader, more topical, more knowledge-oriented set of techniques than with the much more programming-oriented frameworks.

Regardless of the exact categorisation, all these software-related topics can mean defining choices in a (research) software project.

### Considerations

Most of the following considerations apply to software languages, frameworks and technologies alike, unless explicitly noted otherwise.

#### People and community
- What software is used widely in your field already? It may make sense for interoperability and reusability (the I and R in [FAIR](fair_rs)) to choose the same software, if possible.
- Similarly, what existing practices and experience are available in your community? Can you benefit from this?
   * Also look at the expertise available at your institute/organisation.
     Having an expert at a nearby desk to ask questions or even coach you can be invaluable.
- What languages, frameworks or technologies do you know already? Which ones do you like? Take into account personal preference and expertise.
   * If you have project partners, work in a team or plan to do so, make sure you take their preferences into account as well.

#### Language and ecosystem

- Does the language or (packages in its) ecosystem offer features that you need for your project?
- Does the language or ecosystem offer features or frameworks that will save you time?
- Is the language or framework expressive enough to encode your envisioned design?
- Is the language or framework not too complicated? Is it overkill for your purposes?
- Can't choose? It may still be possible to change choices later if you design your software in a modular way or introduce proper abstractions to "hide" certain choices behind a layer, so that the rest of your application doesn't get tied to some choice's specific implementation details.

#### Project lifecycle and tiers

Apart from the above considerations, there are a couple of different situations that offer their own specific constraints.
We highlight three typical cases, related loosely to the [three tiers of research software](three_tier_view) and [research software life cycle](life_cycle):

1. _Rapid prototyping: quickly testing an approach to a problem for the first time._ In this situation, you'll typically want to go with a language, framework or technology you already know or a new one you want to try out.
   The key part here is that your preference weighs more heavily than in "higher" tiers or later life cycle stages.
   If you don't know any programming language yet, getting familiar with {% tool "python" %} is a good choice for rapid prototyping.
2. _Starting a new development project._ When you get past the rough sketching stage, the considerations in the rest of this document apply.
   This means there are a lot of factors to weigh, not just on the feature-side but also taking social and personal aspects into account.
   [Always remember Betamax](https://en.wikipedia.org/wiki/Videotape_format_war): it is hard to predict that as project will succeed based solely on technical merit.
3. _Joining an existing project._ In this case, you are typically not free to choose.
   Projects sometimes switch languages, but not often.
   Also switching frameworks is typically a rather big choice that is not taken lightly.
   However, the reason for you joining the project may be exactly to apply some new technology, possibly using some existing framework.
   In such cases the above social considerations would apply, but you will still be constrained in your choices by the existing languages or frameworks in the project.


### Good default languages 

What follows is a somewhat opinionated list of good starting choices of programming languages for research software engineering projects.
Your mileage may vary, but you will not be far off choosing the following languages for the listed purposes and domains.

When starting fresh, there are a few languages with a proven track record and active communities in research:
- {% tool "python" %}: quick prototyping (interactive, not compiled), gluing other code together, data analysis, ML. A general purpose language that is easy to get started in, that can yield very good and efficient software (especially when using the many available efficient externally packaged modules) and that is easily adoptable by many scientific communities.
- {% tool "cpp" %}: high performance (compiled), strongly typed, multi-paradigm (many "dialects": C-style, object oriented, functional, templated), considered unsafe (though using modern standards instead of raw pointers avoids that)
- {% tool "javascript" %}/{% tool "typescript" %}: anything with a serious web component, also possibly UI for non-web applications.
- {% tool "r" %}: statistical analysis, in particular for social sciences, medical research and the like.
- {% tool "fortran" %}: computationally intensive numerical simulations, particularly in scientific and engineering applications where high performance computing (HPC) is required due to its excellent ability to handle large arrays and optimise complex mathematical calculations with high speed and precision.

If you are excited by the prospect of having to pioneer a bit more due to a smaller and somewhat less mature ecosystem of available modules, the following are popular modern choices:
- {% tool "julia" %}: great for mathematical modelling, has very elegant semantics (e.g. multiple dispatch). It is JIT compiled, meaning you can use it interactively like Python, but it compiles each statement before running, so that it can run fast.
- {% tool "rust" %}: high performance, safety-first. Rust is sometimes described as "C++ done right". It is more focused on functional programming and lacks some core object oriented paradigm support like classes.

A few special purpose languages that are also good to consider are:
- {% tool "cuda" %}/{% tool "opencl" %}: general purpose GPU programming, for accelerating parallelisable computations using GPU hardware.
- Shell scripting (e.g. {% tool "bash" %}, {% tool "powershell" %}): for simple tasks around text processing, setting up runtime environments and automating running of multiple commands in a simple pipeline, shell scripts are still unsurpassed. Unlocking the full power of shell scripting also requires knowledge of command line tools.

### Getting off to a flying start

You chose a language, framework or technology.
Whether you are already an experienced programmer or you start out completely fresh, it will be helpful to start out reading up on some basic guides to get up to date on the latest features and developments and also to get to know the jargon, to know the keywords to find more material. After getting acquainted with the basics, you may want to get started coding as fast as possible.

#### Solution: use templates 

Both in case of starting fresh with a new language or a new framework or other type of software, it is a good idea to look out for good templates.
They offer community curated best practices ready for use, saving time for the RSE or researcher.
There are specific templates built specifically for research software, but also more general ones or templates that help you set up for some specific framework (e.g. some web or UI framework) or technology (like database software or some particular HPC system).

By contributing to such templates, one can also multiply one's effort in figuring out current best practices by all the template's future users (possibly including yourself!).
Template communities can be places where best practices are discussed and set, in addition to spreading them.

Note that alternatives that perform a similar function can be as simple as finding some copy-pasteable snippets, but also IDEs and AI assistants (LLM-based or otherwise) offer basic templates and inline autocompletion that can help you adhere to good programming practices.
Using these is definitely encouraged, as these are useful in their own right.

Full-blown project boilerplate generators still offer a good starting point, especially when they are tailor-made for your field or for research software specifically, and hence include aspects that may not be readily available from generic programming tools and guides.

Some interesting templates to consider for research software:
- [The Netherlands eScience Center Python template](https://github.com/NLeSC/python-template): create a Python package that follows research software best practices
- [BestieTemplate.jl](https://github.com/JuliaBesties/BestieTemplate.jl): Julia package template for research software
- For R, the [usethis](https://usethis.r-lib.org) package provides a good basis for developing R packages.

Of course, the RSQKit itself also uses templates to create pages, like [the one used for this task page](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/your_tasks/TEMPLATE_your_tasks.md)!

## Training materials 

Below you can find introductory materials to the most commonly used programming languages used in Research Software:
- Python: [Research Software Engineering with Python](https://alan-turing-institute.github.io/rse-course/html/index.html), [programming with Python](https://swcarpentry.github.io/python-novice-inflammation/index.html), [leveling up your Python](https://henryiii.github.io/level-up-your-python/notebooks/0%20Intro.html), [Python introduction for libraries](https://librarycarpentry.org/lc-python-intro/), [Python traps and pitfalls](https://gitlab.in2p3.fr/informatique-des-deux-infinis/pheniics/python-traps)
- R: [Introduction to R](https://carpentries-lab.github.io/metagenomics-R/), [Software Carpentry: R for Reproducible Scientific Analysis](), [Software Carpentry: Programming with R](https://swcarpentry.github.io/r-novice-inflammation/), [Getting Used to R, RStudio, and R Markdown](https://rbasics.netlify.app/), [Modern Dive into R and the Tidyverse](https://moderndive.netlify.app/)
- Julia: [Introduction to Julia](https://enccs.github.io/julia-intro/), [Julia for high-performance scientific computing](https://enccs.github.io/julia-for-hpc/), [Julia for high-performance data analytics](https://enccs.github.io/julia-for-hpda/), [Programming with Julia](https://carpentries-incubator.github.io/julia-novice/)
- CMake: [hands-on workshop](https://enccs.github.io/cmake-workshop/)
- Matlab: [Software Carpentry: Programming with MATLAB](https://swcarpentry.github.io/matlab-novice-inflammation/)
- C++: [Modern Scientific C++](https://github.com/chavid/ModernScientificCpp)




## Credit The first version of this page was inspired by content in and discussions on the [Netherlands eScience Center Guide to software development](https://guide.esciencecenter.nl).
