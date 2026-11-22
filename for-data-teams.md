---
title: "Job board data for data teams: the full history as files or a Snowflake share"
description: >-
  The full Hiring Pulse history for data teams: daily hiring signals and job events for 21,922 companies on six job-board vendors, as monthly CSV or a Snowflake share. Schema, free sample, prices, access.
permalink: /for-data-teams/
jsonld: dataset
dataset_name: "Hiring Pulse full history: daily_signals, job_events, companies"
---
# For data teams: the full history as a feed

The weekly report is one view of a daily archive. The archive itself, every company, every day, every role opened or
closed, is available as a monthly feed for teams that build on it: hiring-momentum signals for sales and investing,
time-to-fill and department-demand benchmarks for talent teams, labour-market research on early-stage companies. No
personal data is collected; the sources are the job boards companies publish for embedding on their own sites.
Want rows now rather than files? Every day of the archive is a few dollars away on the
[Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed), pay per row; the
[other ways to get the data]({{ '/get-the-data/' | relative_url }}) are listed in one place.

## What is in it

Three tables, appended daily, with the history from the first day of collection.

| Table | One row per | Rows per day (Nov 2026) | Columns |
|---|---|---|---|
| `companies` | company | monthly refresh, {{ site.coverage.companies }} rows | key, name, job-board vendor and slug, careers URL, website; for the {{ site.coverage.with_industry }} YC-backed companies also industry, sub-industry, team size, batch |
| `daily_signals` | company × day | ≈ {{ site.coverage.companies }} | snapshot time, open roles, previous open roles, new and closed roles, net change, growth %, 30-day trend, roles opened and closed in 30 days, median days-to-fill, remote share, AI/ML roles and share, functions, seniority mix, top departments, top locations, snapshots recorded, one-word signal |
| `job_events` | role opened or closed | thousands | event type, company, vendor, slug, job id, title, department, location, remote flag, URL, first seen, closed at, days open; plus one baseline row per role that was already open when a board entered the archive |

Coverage: {{ site.coverage.companies }} companies with a public {{ site.coverage.vendors }} board, daily since
{{ site.coverage.companies_since }} ({{ site.coverage.companies_before }} companies from {{ site.coverage.daily_since }}); a
{{ site.coverage.yc_subset }}-company Y Combinator subset was collected daily from {{ site.coverage.yc_subset_since }}. The
30-day fields (growth, trend, roles opened and closed in 30 days, days-to-fill) mature through December 2026 as the
history passes 14 and 30 days. Weekly benchmark rows (the tables behind the report: per industry, size bucket, vendor and
function) can be included.

### Schema

The CSV headers in the sample below are authoritative and match the rows the
[Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) emits today, so a pipeline built on the sample
works on the feed and on the monthly files alike; a Snowflake DDL for the three tables comes with the feed files. Nested
fields (`functions`, `seniorityMix`, `topDepartments`, `topLocations`) are JSON arrays of `{name, count}` in the CSV
and VARIANT columns in Snowflake. Consumers deduplicate `job_events` on vendor, slug, job id and event type.

## Free sample

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from
  2026-11-22, the second day of full-universe collection (so trends are still flat; the 30-day fields fill in through
  December).
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the role events of the same day.
- The [baseline study of 2026-11-20]({{ '/reports/2026-11-20/' | relative_url }}) is computed from a 14-day history on the
  YC subset; the [weekly reports]({{ '/reports/' | relative_url }}) are the best preview of what the history supports.
- Any day or 30-day window of the full archive, filtered, is a few dollars away on the
  [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) (pay per row, no request needed).

## Delivery and pricing

| Offer | Delivery | Price |
|---|---|---|
| Monthly feed, 1-month term | CSV in S3 or AWS Data Exchange | $149 per month |
| Annual feed with the full history | CSV in S3 or AWS Data Exchange | $1,200 per year |
| Snowflake listing | Secure share, 30-day-lagged free sample | $249 per month |
| Enterprise: redistribution rights, custom cuts, SLA | As above | $5,000–8,000 per year |
| Per row, self-serve, today | Apify Store, pay per row | $0.01 per company-day, $0.004 per role event |

Prices are anchors as of November 2026; marketplace listings (AWS Data Exchange, Snowflake Marketplace) open once the
archive holds 30 days. Academic and journalistic use: ask, the answer is usually a free cut with attribution.

## Quality

The collection checks itself every day: fetched-OK rate, day-over-day stability, a careers-page re-count of 25
boards and a re-fetch of 10 closed roles, with alert thresholds. The checks and a healthy day's numbers are on the
[methodology]({{ '/methodology/' | relative_url }}) page.

## Request access

<p><a class="btn" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Open a data access request</a></p>

It is a short GitHub issue form (organisation, use, tables, delivery). We reply in the thread, usually within two
business days; if you would rather not discuss it in public, say so in the form and we take it off the thread.
