---
title: "All weekly Hiring Pulse reports: the startup hiring archive"
description: >-
  Every weekly Hiring Pulse edition, one per Monday: startup hiring benchmarks from 21,000+ job boards with key findings, charts, movers, days-to-fill, AI share.
permalink: /reports/
---
# All weekly reports

A new edition every Monday at 07:00 UTC, computed from that morning's reads of {{ site.coverage.companies }} company job
boards. Each edition opens with the week's key findings and charts, then the headline numbers with their change since
the previous edition, then the full tables. The newest is always at [reports/latest]({{ '/reports/latest/' | relative_url }});
subscribe with the [Atom feed]({{ '/feed.xml' | relative_url }}). Markdown sources and chart files are in the
[GitHub repository](https://github.com/agilityy-research/hiring-pulse/tree/main/reports).

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
<p>The first Monday edition is published on 2026-11-23 at 07:00 UTC. Until then the
<a href="{{ '/reports/latest/' | relative_url }}">preview edition</a> shows the current numbers in the same format.</p>
{%- endif %}

Editions before {{ site.coverage.flows_from }} carry the stock figures for the whole universe (open roles, functions,
AI/ML share, remote share, seniority, the largest boards) and the flow figures (growth, roles opened and closed,
days-to-fill, movers) for the companies that already have 14 days of daily history. From {{ site.coverage.flows_from }}
the flow figures cover the whole universe, and the "since previous edition" columns and the trend chart lengthen
with every edition. How the numbers are measured: [methodology]({{ '/methodology/' | relative_url }}).

## Baseline study

{%- for p in baselines %}
<ul class="report-list">
<li><a href="{{ p.url | relative_url }}">Hiring Pulse {{ p.name | remove: ".md" }}</a> <span class="tag">Baseline study</span>
<span class="muted small">14-day readout on {{ site.coverage.yc_subset }} Y Combinator companies, collected daily from {{ site.coverage.yc_subset_since }}; the first look at
growth, days-to-fill and movers before the full universe had history. Not part of the weekly series.</span></li>
</ul>
{%- endfor %}
