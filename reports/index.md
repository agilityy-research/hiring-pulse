---
title: "All weekly Hiring Pulse reports"
description: >-
  Archive of every weekly Hiring Pulse report: startup hiring benchmarks from 10,000+ job boards, one report per
  Monday since November 2026, by Agilityy Research. Open roles, days-to-fill, AI share, industry and function tables.
permalink: /reports/
---
# All weekly reports

One report per week, generated on Mondays from the previous day's snapshots and published here by the pipeline itself.
The newest is always at [reports/latest]({{ '/reports/latest/' | relative_url }}); the Markdown sources are in the
[GitHub repository](https://github.com/agilityy-research/hiring-pulse/tree/main/reports).

{%- assign report_pages = site.pages | where_exp: "p", "p.path contains 'reports/'" | sort: "path" | reverse %}
<ul class="report-list">
{%- for p in report_pages %}
{%- if p.name != "latest.md" and p.name != "index.md" %}
<li><a href="{{ p.url | relative_url }}">Hiring Pulse {{ p.basename }}</a>{% if forloop.first %} <span class="muted small">(latest)</span>{% endif %}</li>
{%- endif %}
{%- endfor %}
</ul>

Early editions (before any company had 14 days of daily history) report what the boards showed on the day: open
roles, functions, AI share, seniority and remote share. From the first edition after 2026-12-05 every report also
carries growth, roles opened and closed, days-to-fill and the leaderboards; coverage grows each week as more of the
tracked companies pass the 14-day mark. How the numbers are measured: [methodology]({{ '/methodology/' | relative_url }}).
