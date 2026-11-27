---
title: "Job board data for data teams: schema, sample and the daily history"
description: >-
  The daily data behind Hiring Pulse for data teams: daily signals and job events for 21,000+ companies. Schema, free sample, how to load it.
permalink: /for-data-teams/
jsonld: dataset
dataset_name: "Hiring Pulse full history: daily_signals, job_events, companies"
---
# For data teams: the tables, their schema and a sample

The weekly report is one view of the daily data: every company, every day, every role opened or closed. That is what
you build on: hiring-momentum signals for sales and investing, time-to-fill and department-demand benchmarks for talent
teams, labour-market research on early-stage companies. No personal data is collected; the sources are the job boards
companies publish for their own careers pages.

{% if site.beta_signup_action != "" %}During the beta, every company's daily files are free by e-mail until
{{ site.beta_end | date: "%-d %B %Y" }}: [sign up here]({{ '/get-the-data/' | relative_url }}#beta). {% endif %}For the
whole history or a regular feed into your own systems, [ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml). Daily collection began on {{ site.coverage.daily_since }}, so the history is short
today and grows by one day every day.

## What is in it

Three tables, appended daily, with the history from the first day of collection.

| Table | One row per | Rows per day | Columns |
|---|---|---|---|
| `companies` | company | one per company, refreshed monthly | key, name, job-board vendor and slug, careers URL, website; for the YC-backed companies ({{ site.coverage.with_industry }}) also industry, sub-industry, team size, batch |
| `daily_signals` | company × day | one per tracked company, {{ site.coverage.companies }} a day | snapshot time, open roles, previous open roles, new and closed roles, net change, growth %, 30-day trend, roles opened and closed in 30 days, median days-to-fill, remote share, AI/ML roles and share, functions, seniority mix, top departments, top locations, snapshots recorded, one-word signal |
| `job_events` | role opened or closed | about 2,000 (roughly 0.3% of open roles) | event type, company, vendor, slug, job id, title, department, location, remote flag, URL, first seen, closed at, days open; plus one baseline row per role that was already open when a board entered the history |

Coverage: {{ site.coverage.companies }} companies with a public {{ site.coverage.vendors }} board, daily since
{{ site.coverage.companies_since }} ({{ site.coverage.companies_before }} companies from {{ site.coverage.daily_since }}); a
{{ site.coverage.yc_subset }}-company Y Combinator subset was collected daily from {{ site.coverage.yc_subset_since }}. The
30-day fields (growth, trend, roles opened and closed in 30 days, days-to-fill) fill in through December 2026 as the
history passes 14 and 30 days. The weekly benchmark rows (the tables behind the report: per industry, size bucket,
vendor and function) can be added to a custom delivery.

### Schema

The CSV headers in the sample below are authoritative and match the daily files, so a pipeline you build on the
sample works on the full data without changes. Nested fields (`functions`, `seniorityMix`, `topDepartments`, `topLocations`)
are JSON arrays of `{name, count}` in the CSV and JSON objects in the JSON files; load them as VARIANT or JSON columns.
Deduplicate `job_events` on vendor, slug, job id and event type.

## Free sample

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from
  2026-11-22, the second day of full collection (so trends are still flat; the 30-day fields fill in through December).
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the role events of the same day.
- The [baseline study of 2026-11-20]({{ '/reports/2026-11-20/' | relative_url }}) is computed from a 14-day history on the
  YC subset; the [weekly reports]({{ '/reports/' | relative_url }}) are the best preview of what the history supports.

## Getting it into a warehouse

{% if site.beta_signup_action != "" %}During the beta the daily files arrive by e-mail as download links; a scheduled
job can fetch them each morning. {% endif %}A delivered history (files in your storage bucket, or a warehouse share) is
set up on request, because the daily history is only weeks old: [ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml)
and say what for. Academic and journalistic use: usually a free cut with attribution.

## Quality

The collection checks itself every day: the share of boards that answered, day-over-day stability, a careers-page
re-count of 25 boards and a re-fetch of 10 closed roles, each with an alert threshold. The checks and a healthy day's
numbers are on the [methodology]({{ '/methodology/' | relative_url }}) page. What you may do with the rows is in the
[terms for the data]({{ '/get-the-data/' | relative_url }}#terms-for-the-data).

## Next

<p>{% if site.beta_signup_action != "" %}<a class="btn" href="{{ '/get-the-data/' | relative_url }}#beta">Get the daily files free</a>
{% endif %}<a class="btn{% if site.beta_signup_action != "" %} alt{% endif %}" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for a history delivery</a></p>

The request form is a short GitHub issue (organisation, use, tables, delivery). We reply within two business days; if you
would rather not discuss it in public, say so in the form and we continue privately.
