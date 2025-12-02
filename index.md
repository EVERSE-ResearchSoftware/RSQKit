---
search_exclude: true
layout: home
---

<!-- Page Content -->
<div class="landingpage">
    <section class="container g-lg-5 mb-5">
        <div>
            <h1 class="text-center">Research Software Quality Toolkit (RSQKit)</h1>
            <p class="text-center mt-2">
             Tasks, tools, and resources to support your research software to be repeatable, reproducible, trustworthy, resilient, understandable, efficient, adaptable and maintainable.
            </p>
        </div>
    </section>
    <section id="search-section" class="bg-light py-5">
        <div class="container g-lg-5">
            <div class="row">
                <h2 class="no-anchor text-center mb-3 homepage-heading">What can we help you find?</h2>
                <div class="position-relative">
                    <div class="d-flex justify-content-center">
                        <form role="search" class="input-group">
                            <span class="input-group-text" id="search-label"><i class="fa-solid fa-magnifying-glass"></i></span>
                            <input type="search" id="search-input" class="search-input form-control form-control-lg bg-white" tabindex="0"
                                   placeholder="Search RSQKit ..." aria-label="Search {{ site.title }}" autocomplete="off">
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
            {%- assign sidebar = site.data.sidebars[page.sidebar] %}
            <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
                {%- for folder in sidebar.subitems %}
                    <div class="col">
                        <div class="card bg-white h-100">
                            <img src="{{folder.image_url | relative_url}}" class="card-img-top h-icon-6 mx-auto" alt="{{folder.title}} icon" style="width: 15%; padding: 20px 5px 5px 0px;">
                            <div class="card-body text-center">
                                <a href="{{ folder.url | relative_url }}" class="stretched-link">
                                    <h3 class="card-title no-anchor text-dark homepage-heading">{{folder.title}}</h3>
                                </a>
                                <p class="card-text homepage-text">{{folder.description}}</p>
                            </div>
                        </div>
                    </div>
                {%- endfor %}
            </div>
        </div>
    </section>
</div>
