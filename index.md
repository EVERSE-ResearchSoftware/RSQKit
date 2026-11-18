---
search_exclude: true
sidebar: false
layout: home
---

<!-- Page Content -->
<div class="landingpage">
    <section class="container g-lg-5 mb-5">
        <div>
            <h1 class="text-center">Research Software Quality Toolkit (RSQKit)</h1>
            <p class="text-center mt-2">
             Tasks, tools, stories, and resources to support your research software to be repeatable, reproducible, trustworthy, resilient, understandable, efficient, adaptable and maintainable.
            </p>
        </div>
    </section>
    <section id="search-section" class="bg-light py-5">
        <div class="container g-lg-5">
            <div class="homepage-search d-flex flex-column flex-md-row
                        align-items-md-center gap-2 gap-md-3">
                <label for="search-input"
                       class="homepage-search-label homepage-heading h2 mb-0 text-md-end">
                    Search RSQKit:
                </label>

                <div class="position-relative flex-grow-1 homepage-search-field">
                    <div class="d-flex justify-content-center">
                        <form role="search" class="input-group">
                            <span class="input-group-text" id="search-label">
                                <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
                            </span>
                            <input type="search" id="search-input"
                                   class="search-input form-control form-control-lg bg-white"
                                   autocomplete="off">
                        </form>
                        <div id="search-results" class="search-results"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="bg-light pb-5">
        <div class="container g-lg-5">
            <h2 class="no-anchor text-center mb-3 homepage-heading">Browse all topics by</h2>
            {%- assign sidebar = site.data.sidebars.main %}

            {% assign panel_order = "Roles|Tasks|Research software stories|Research software & quality|Guidance for AI|Research clusters or infrastructures" | split: "|" %}

            <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
                {% for title in panel_order %}
                    {% assign folder = sidebar.subitems | where: "title", title | first %}
                    {% if folder %}
                        <div class="col">
                            <div class="card bg-white h-100">
                                <img src="{{ folder.image_url | relative_url }}"
                                     class="card-img-top h-icon-6 mx-auto"
                                     alt="{{ folder.title }} icon"
                                     style="width: 15%; padding: 20px 5px 5px 0px;">
                                <div class="card-body text-center">
                                    <a href="{{ folder.url | relative_url }}" class="stretched-link">
                                        <h3 class="card-title no-anchor text-dark homepage-heading">{{ folder.title }}</h3>
                                    </a>
                                    <p class="card-text homepage-text">{{ folder.description }}</p>
                                </div>
                            </div>
                        </div>
                    {% endif %}
                {% endfor %}
            </div>
        </div>
        <hr width="100%" size="2">
        <div class="container g-lg-5">
            <h3 class="no-anchor text-center mb-3 homepage-heading">Further indicators, tools and resources</h3>
            {%- assign sidebar = site.data.sidebars.main %}
            <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4">
                {%- for folder in sidebar.subitems %}
                    {%- if folder.title == "All indicators" or folder.title == "All tools and resources" or folder.title == "Site Statistics" or folder.title == "Get involved" %}
                    <div class="col">
                        <div class="card bg-white h-100">
                            <img src="{{folder.image_url | relative_url}}" class="card-img-top h-icon-6 mx-auto" alt="{{folder.title}} icon" style="width: 15%; padding: 20px 5px 5px 0px;">
                            <div class="card-body text-center">
                                <a href="{{ folder.url | relative_url }}" class="stretched-link">
                                    <h4 class="card-title no-anchor text-dark homepage-heading">{{folder.title}}</h4>
                                </a>
                                <p class="card-text homepage-text">{{folder.description}}</p>
                            </div>
                        </div>
                    </div>
                    {%- endif %}
                {%- endfor %}
            </div>
        </div>
    </section>
</div>
