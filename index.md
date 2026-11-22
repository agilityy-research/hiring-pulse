---
title: "Startup hiring benchmarks, every Monday, free"
description: >-
  Weekly startup hiring benchmarks from the public job boards of 10,000+ venture-backed companies: open roles, roles
  opened and closed, median days-to-fill, AI/ML share, remote share, by industry and function. Free report by
  Agilityy Research; the job board data behind it is for sale per record or as a feed.
permalink: /
---
{%- capture latest_raw %}{% include_relative reports/latest.md %}{% endcapture -%}
{%- assign sections = latest_raw | split: "## " -%}
{%- assign head = sections | first -%}
{%- assign head_lines = head | newline_to_br | split: "<br />" -%}
{%- assign title_line = head_lines[0] | strip -%}
{%- assign latest_date = title_line | split: "—" | last | strip -%}
{%- assign headline = head | remove_first: head_lines[0] -%}

# Startup hiring benchmarks, every Monday

<p class="lead">Agilityy Research reads the public job boards of more than 10,000 venture-backed companies every day
(Greenhouse, Lever, Ashby and Workable) and publishes what changed: roles opened and closed, net growth, median
days-to-fill, AI/ML and remote share, by industry and function. The weekly report is free and citable. The daily
data behind it is <a href="{{ '/data/' | relative_url }}">for sale per record</a> or
<a href="{{ '/for-data-teams/' | relative_url }}">as a feed for data teams</a>.</p>

<div class="card" id="latest">
<h2>Latest report: {{ latest_date }}</h2>
{{ headline | markdownify }}
{%- if sections[1] %}
{{ sections[1] | prepend: "### " | markdownify }}
{%- endif %}
<p><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">All weekly reports</a></p>
</div>

## What is in every report

- Open roles, roles opened and closed, and net growth over a 30-day window
- Share of companies accelerating vs contracting their hiring
- Median days-to-fill, measured from observed posting closures, overall and per function
- Open roles by function (Engineering, Sales, Data & AI, Clinical, …)
- Industry and company-size benchmarks; the job-board vendor split
- AI/ML roles as a share of all open roles; remote share; seniority mix
- Leaderboards: largest net additions, fastest growing, biggest cuts, heaviest AI hiring

Every number comes from first-party daily snapshots, not from job aggregators, so a role counts once and a closure is
observed rather than inferred. The collectors check their own completeness and accuracy every day; the
[methodology]({{ '/methodology/' | relative_url }}) page lists the checks and the thresholds.

## Get the data

<div class="grid">
<div class="card"><h3>Hiring Signals Feed</h3>
<p>Yesterday's signals for every tracked company, one row each, or any day or 30-day window, filtered by provider,
industry, function or signal. Pay per row, from the Apify Store, no scraping on your side.</p>
<p><a href="https://apify.com/agilityy/hiring-signals-feed">Open the feed</a> · <span class="price">$0.01 per company-day</span></p></div>
<div class="card"><h3>Track your own list</h3>
<p>Hiring Velocity Signals watches the companies you name and returns growth, opened and closed roles, days-to-fill
and a one-word signal every run. Company Hiring Lookup answers for one company now.</p>
<p><a href="{{ '/data/' | relative_url }}">All products and prices</a></p></div>
<div class="card"><h3>The full history</h3>
<p>Daily signals and job events for every company since collection began, delivered monthly as CSV or a Snowflake
share, with a free sample and a schema you can load today.</p>
<p><a href="{{ '/for-data-teams/' | relative_url }}">For data teams</a></p></div>
</div>

<p class="small muted">Reports are released under CC BY 4.0. Cite as "Agilityy Research, Hiring Pulse, {{ latest_date }}"
with a link to this site. Source files and history: <a href="https://github.com/agilityy-research/hiring-pulse">github.com/agilityy-research/hiring-pulse</a>.</p>
