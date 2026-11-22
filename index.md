---
title: "Startup hiring benchmarks, every Monday, from 21,000+ job boards"
description: >-
  Where startup hiring accelerates and stalls this week: open roles, movers, days-to-fill, AI/ML and remote share across 21,000+ job boards. Free every Monday.
permalink: /
---
{%- capture nl %}
{% endcapture -%}
{%- capture nl2 %}{{ nl }}{{ nl }}{% endcapture -%}
{%- capture latest_raw %}{% include_relative reports/latest.md %}{% endcapture -%}
{%- assign sections = latest_raw | split: "## " -%}
{%- assign title_line = sections[0] | split: nl | first -%}
{%- assign latest_date = title_line | split: "—" | last | strip -%}
{%- assign coverage_line = sections[0] | remove_first: title_line | strip -%}
{%- assign findings = "" -%}{%- assign charts = "" -%}{%- assign headline = "" -%}
{%- for s in sections -%}
  {%- if s contains "Key findings" and forloop.index0 > 0 and findings == "" -%}{%- assign findings = s | remove_first: "Key findings" -%}
  {%- elsif s contains "This week in charts" and charts == "" -%}{%- assign charts = s | remove_first: "This week in charts" -%}
  {%- elsif s contains "Headline numbers" and headline == "" -%}{%- assign headline = s | remove_first: "Headline numbers" -%}
  {%- endif -%}
{%- endfor -%}
{%- comment -%} Findings come as "- **headline** detail" with an indented "  - *audience*" line; the last paragraph is a coverage note. {%- endcomment -%}
{%- assign items = findings | split: "- **" -%}
{%- assign findings_note = findings | strip | split: nl2 | last | strip -%}
{%- if findings_note contains "- " or findings_note contains "**" -%}{%- assign findings_note = "" -%}{%- endif -%}
{%- assign hero = "" -%}
{%- comment -%} Stat strip from the headline table: value in column 2, change in column 4. {%- endcomment -%}
{%- assign v_companies = "" -%}{%- assign v_open = "" -%}{%- assign d_open = "" -%}{%- assign v_fill = "" -%}{%- assign d_fill = "" -%}{%- assign v_ai = "" -%}{%- assign d_ai = "" -%}{%- assign v_remote = "" -%}{%- assign d_remote = "" -%}
{%- assign hrows = headline | split: nl -%}
{%- for r in hrows -%}
  {%- assign cells = r | split: "|" -%}
  {%- if r contains "| Companies tracked |" -%}{%- assign v_companies = cells[2] | strip -%}
  {%- elsif r contains "| Open roles |" -%}{%- assign v_open = cells[2] | strip -%}{%- assign d_open = cells[4] | strip -%}
  {%- elsif r contains "| Median days-to-fill |" -%}{%- assign v_fill = cells[2] | strip -%}{%- assign d_fill = cells[4] | strip -%}
  {%- elsif r contains "| AI/ML share of open roles |" -%}{%- assign v_ai = cells[2] | strip -%}{%- assign d_ai = cells[4] | strip -%}
  {%- elsif r contains "| Remote roles, share of open roles |" -%}{%- assign v_remote = cells[2] | strip -%}{%- assign d_remote = cells[4] | strip -%}
  {%- endif -%}
{%- endfor -%}

# Where startup hiring is moving this week

{%- if items.size > 1 %}
{%- assign first = items[1] | split: nl2 | first -%}
{%- assign hero = first | split: "**" | first -%}
<p class="hero">{{ hero }}</p>
{%- endif %}
<p class="muted small">Edition of {{ latest_date }}. {{ coverage_line | markdownify | strip_html | strip }} The weekly report is free to quote; the daily data behind it, every company and every role opened or closed, is <a href="{{ '/get-the-data/' | relative_url }}">yours per row, as a feed or through an AI assistant</a>.</p>

{%- if v_open != "" %}
<div class="stats" aria-label="Headline numbers">
<div class="stat"><b>{{ v_open }}</b><span>open roles</span>{% if d_open != "" and d_open != "—" %}<span class="delta">{{ d_open }} vs previous edition</span>{% endif %}</div>
{%- if v_companies != "" %}<div class="stat"><b>{{ v_companies }}</b><span>companies, boards read daily</span></div>{% endif %}
{%- if v_fill != "" and v_fill != "—" %}<div class="stat"><b>{{ v_fill }}</b><span>median days to fill a role</span>{% if d_fill != "" and d_fill != "—" %}<span class="delta">{{ d_fill }}</span>{% endif %}</div>{% endif %}
{%- if v_ai != "" %}<div class="stat"><b>{{ v_ai }}</b><span>of open roles are AI/ML</span>{% if d_ai != "" and d_ai != "—" %}<span class="delta">{{ d_ai }}</span>{% endif %}</div>{% endif %}
{%- if v_remote != "" and v_remote != "—" %}<div class="stat"><b>{{ v_remote }}</b><span>of open roles are remote</span>{% if d_remote != "" and d_remote != "—" %}<span class="delta">{{ d_remote }}</span>{% endif %}</div>{% endif %}
</div>
{%- endif %}

## What the data says this week

{%- if items.size > 1 %}
<div class="insights">
{%- for item in items offset: 1 %}
{%- assign body = item | split: nl2 | first -%}
{%- assign head = body | split: "**" | first -%}
{%- assign rest = body | remove_first: head | remove_first: "**" -%}
{%- assign who = "" -%}{%- assign detail = rest | strip -%}
{%- if rest contains "- *" -%}{%- assign rp = rest | split: "- *" -%}{%- assign detail = rp[0] | strip -%}{%- assign who = rp[1] | split: "*" | first -%}{%- endif -%}
{%- assign wp = who | split: ": " -%}
<div class="card">
<h3>{{ head | strip }}</h3>
{%- if detail != "" %}<p>{{ detail | markdownify | strip_html }}</p>{% endif %}
{%- if who != "" %}<p class="who">{% if wp.size > 1 %}<b>{{ wp[0] }}:</b> {{ who | remove_first: wp[0] | remove_first: ": " }}{% else %}{{ who }}{% endif %}</p>{% endif %}
</div>
{%- endfor %}
</div>
{%- if findings_note != "" %}<p class="muted small">{{ findings_note | markdownify | strip_html }}</p>{% endif %}
{%- else %}
{{ sections[0] | remove_first: title_line | markdownify }}
{%- endif %}

{%- if charts != "" %}
<div class="charts">
{{ charts | markdownify }}
</div>
{%- endif %}
{%- if headline != "" %}
<details><summary>All headline numbers and the change since the previous edition</summary>
{{ headline | markdownify }}
</details>
{%- endif %}
<p><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">How you get the data</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a></p>

## Get the data behind it

<div class="grid">
<div class="card"><h3>Hiring Signals Feed</h3>
<p>Yesterday's signals for every tracked company, one row each, or any day or 30-day window, filtered by vendor,
industry, function or signal. Download as JSON, CSV or Excel, call it from code, or ask for it from Claude or Cursor.</p>
<p><span class="price">$0.01 per company-day</span> · <a href="https://apify.com/agilityy/hiring-signals-feed">Open the feed</a></p></div>
<div class="card"><h3>Your own company list</h3>
<p>Daily growth, roles opened and closed, days-to-fill and a one-word signal for the companies you name; or one
company checked right now; or companies that just raised money, with a live hiring check.</p>
<p><a href="{{ '/data/' | relative_url }}">Products and prices</a></p></div>
<div class="card"><h3>The whole history</h3>
<p>Every company, every day, every role event since collection began: monthly CSV files or a Snowflake share, with
a free sample and the schema to load today.</p>
<p><a href="{{ '/for-data-teams/' | relative_url }}">For data teams</a></p></div>
</div>

<p><a class="btn" href="{{ '/get-the-data/' | relative_url }}">All six ways to get the data</a></p>

## Why these numbers hold up

- **First-party.** Every company's own job board ({{ site.coverage.vendors }}) is read once a day. A role is counted
  once, from the source, and a closure is observed the day the posting disappears, not inferred from an aggregator.
- **Broad.** {{ site.coverage.companies }} companies since {{ site.coverage.companies_since }}, {{ site.coverage.companies_before }} before that; mostly venture-backed
  technology companies, {{ site.coverage.with_industry }} of them with industry and team size for the segment tables. The exact
  count of the day is in every report.
- **Comparable.** Functions, seniority and the AI/ML flag come from one fixed title taxonomy, so this week's figures
  compare with last week's and with yours.
- **Checked daily.** Fetch rate, day-over-day stability, a careers-page re-count and a re-fetch of closed roles are
  measured every day with alert thresholds. The [methodology]({{ '/methodology/' | relative_url }}) lists them.

## Who uses it

<div class="grid">
<div class="card"><h3>Talent and recruiting teams</h3>
<p>Which functions are hard to fill and how long roles stay open, by industry and company size. Benchmark your
days-to-fill against companies like yours, and see which competitors are opening or closing teams.</p></div>
<div class="card"><h3>Sales and revenue operations</h3>
<p>A company that just doubled its open roles is buying tools, office space, payroll and insurance. Hiring momentum
per company, refreshed daily, is the earliest public signal of a budget.</p></div>
<div class="card"><h3>Investors and analysts</h3>
<p>Portfolio and sector hiring trends from first-party job-board reads, not aggregator counts: roles opened and
closed, net growth, AI/ML share, remote share, comparable week after week.</p></div>
<div class="card"><h3>Journalists and researchers</h3>
<p>Citable numbers every Monday under CC BY 4.0, with the method published. A custom cut of the history for a story
or a paper is usually free with attribution.</p></div>
</div>

<p class="small muted">Reports are released under CC BY 4.0. Cite as "Agilityy Research, Hiring Pulse, {{ latest_date }}"
with a link to this site. New edition every Monday 07:00 UTC; subscribe to the <a href="{{ '/feed.xml' | relative_url }}">Atom feed</a>.
Source files: <a href="https://github.com/agilityy-research/hiring-pulse">github.com/agilityy-research/hiring-pulse</a>.</p>
