---
title: Fast, Declarative, Reproducible and Composable Developer Environments using Nix 
description: "Going a step beyond just \"virtual envirnments\" - with advantages and drawbacks"
contributors:
  - "Nicole Dresselhaus"
page_id: developer_environments
related_pages:
  your_tasks: 
    - virtual_environments
---

## How are devenvs different from virtual software development environments?

Developer Environments (short {% tool "devenv" %}s) are a more holistic
approach to the classical virtual environments. Virtual environments - despite
their undisputed advantages - tend to break at similar steps in the real world.
An environment working on one machine might break on another because of
different operating system, the existence or absence of globally installed
packages, different hardware etc.
You local software might behave different as a docker-container, yield different
results or may not run at all.

## Advantages and Drawbacks

### Advantages

- The same definition runs nearly everywhere the same.
- Generating a docker-image of your software is included
- Automatically setting up multiple services that get started (and even seeded)
  automatically and can be used reproducibly, i.e.
  - Setting up a Database-Service in the backgrund
  - seeding initial data
  - sharing access via environment-variables
- Easy to use `git clone ... && cd ... && devenv shell` and you are done (after
  proper setup)

### Drawbacks

- Can be quite complicated to set up if you stray away from the common schemes
- Not suitable for "just trying stuff out"
- As it depends on nix you are forced to learn the nix-language and the
  nix-ecosystem


## How do you create such development environments? 

### Description

The start is quite humble and simple: Install devenv, do a `devenv init` and you
are ready to go.

Then you should best head over to the [documentation on languages](https://devenv.sh/languages/)
and find the language you actually work with. In most cases the bulk should be
done by enabling the language with a `languages.xxx.enable = true;` and
optionally a version (like python-2 vs python-3), dependencies, system-libraries
etc.

Also you can easily enable plugins and hooks for your team, if you prefer so.
There are already [git-hooks](https://devenv.sh/git-hooks/#1-make-sure-that-commits-are-well-formatted-at-commit-time)
prepared, that can be adapted to your liking. Never have code not up to standard
in your repository.



[devenv]: (https://devenv.sh)
