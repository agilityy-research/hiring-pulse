---
title: "All weekly reports: startup hiring benchmarks, one edition per Monday"
description: >-
  Every weekly Hiring Pulse edition, one per Monday: startup hiring benchmarks from 21,000+ job boards with key findings, charts, movers, days-to-fill, AI share.
permalink: /reports/
---
# All weekly reports

A new edition every Monday at 07:00 UTC, computed from that morning's read of {{ site.coverage.companies }} company job
boards. Each edition gives you the week's key findings and charts first, then the headline numbers with their change since
the previous edition, then the full tables by function, industry, company size and job-board vendor. Every edition is free
to read and to quote under CC BY 4.0.

The newest edition is always at [reports/latest]({{ '/reports/latest/' | relative_url }}). To get each new one as it
appears, subscribe with the [Atom feed]({{ '/feed.xml' | relative_url }}) in your feed reader; the Markdown source and chart
files are in the [GitHub repository](https://github.com/agilityy-research/hiring-pulse/tree/main/reports).

{%- assign report_pages = site.pages | where_exp: "p", "p.path contains 'reports/'" | where_exp: "p", "p.name != 'index.md'" | where_exp: "p", "p.name != 'latest.md'" | sort: "name" | reverse %}
{%- assign weekly = "" | split: "" %}{%- assign baselines = "" | split: "" %}
{%- for p in report_pages %}{%- assign d = p.name | remove: ".md" %}{%- if site.baseline_reports contains d %}{%- assign baselines = baselines | push: p %}{%- else %}{%- assign weekly = weekly | push: p %}{%- endif %}{%- endfor %}

## Weekly series

{%- if weekly.size > 0 %}
<ul class="report-list">
{%- for p in weekly %}
<li><a href="{{ p.url | relative_url }}">Hiring Pulse {{ p.name | remove: ".md" }}</a>{% if forloop.first %} <span class="muted small">(latest)</span>{% endif %}</li>
{%- endfor %}
</ul>
{%- else %}
<p>The first Monday edition is published next Monday at 07:00 UTC. Until then the
<a href="{{ '/reports/latest/' | relative_url }}">preview edition</a> shows the current numbers in the same format.</p>
{%- endif %}

**Reading the early editions.** Daily collection of the full set of companies began on {{ site.coverage.daily_since }}, so the
figures that need history (growth, roles opened and closed, days-to-fill and the movers) are computed, until
{{ site.coverage.flows_from }}, only from the companies that already have 14 days of daily history. The figures that need
only today's read (open roles, functions, AI/ML share, remote share, seniority, the largest boards) always cover every
company in the benchmark. From {{ site.coverage.flows_from }} the history-based figures cover every company too, and the
"since previous edition" columns and the trend chart lengthen with each edition. The definitions are in the
[methodology]({{ '/methodology/' | relative_url }}).

## Baseline study

{%- for p in baselines %}
<ul class="report-list">
<li><a href="{{ p.url | relative_url }}">Hiring Pulse {{ p.name | remove: ".md" }}</a> <span class="tag">Baseline study</span>
<span class="muted small">A 14-day readout on {{ site.coverage.yc_subset }} Y Combinator companies, collected daily from {{ site.coverage.yc_subset_since }}: the first look at
growth, days-to-fill and movers before the full set of companies had history. Not part of the weekly series.</span></li>
</ul>
{%- endfor %}

## Want the numbers behind a report?

Each edition is computed from one row per company per day. You can buy those rows, for the companies and days you
choose, on the Apify Store: [how to buy]({{ '/get-the-data/' | relative_url }}) has the prices with worked examples.
