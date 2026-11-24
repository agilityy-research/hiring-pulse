---
title: "Job board data for data teams: schema, sample and the daily archive"
description: >-
  The daily archive behind Hiring Pulse for data teams: daily signals and job events for 21,000+ companies. Schema, free sample, how to load it.
permalink: /for-data-teams/
jsonld: dataset
dataset_name: "Hiring Pulse full history: daily_signals, job_events, companies"
---
# For data teams: the archive, its schema and a sample

The weekly report is one view of a daily archive. The archive itself, every company, every day, every role opened or
closed, is what teams build on: hiring-momentum signals for sales and investing, time-to-fill and department-demand
benchmarks for talent teams, labour-market research on early-stage companies. No personal data is collected; the
sources are the job boards companies publish for embedding on their own sites. Any day or 30-day window of the archive
is available now, pay per row, on the [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed);
[how to buy]({{ '/get-the-data/' | relative_url }}) has worked prices. Daily collection began on
{{ site.coverage.daily_since }}, so the history is short today and grows by one day every day.

## What is in it

Three tables, appended daily, with the history from the first day of collection.

| Table | One row per | Rows per day | Columns |
|---|---|---|---|
| `companies` | company | one per company, refreshed monthly | key, name, job-board vendor and slug, careers URL, website; for the {{ site.coverage.with_industry }} YC-backed companies also industry, sub-industry, team size, batch |
| `daily_signals` | company × day | one per tracked company, {{ site.coverage.companies }} a day | snapshot time, open roles, previous open roles, new and closed roles, net change, growth %, 30-day trend, roles opened and closed in 30 days, median days-to-fill, remote share, AI/ML roles and share, functions, seniority mix, top departments, top locations, snapshots recorded, one-word signal |
| `job_events` | role opened or closed | about 2,000 (roughly 0.3% of open roles), plus a one-off baseline row per open role on a board's first day | event type, company, vendor, slug, job id, title, department, location, remote flag, URL, first seen, closed at, days open; plus one baseline row per role that was already open when a board entered the archive |

Coverage: {{ site.coverage.companies }} companies with a public {{ site.coverage.vendors }} board, daily since
{{ site.coverage.companies_since }} ({{ site.coverage.companies_before }} companies from {{ site.coverage.daily_since }}); a
{{ site.coverage.yc_subset }}-company Y Combinator subset was collected daily from {{ site.coverage.yc_subset_since }}. The
30-day fields (growth, trend, roles opened and closed in 30 days, days-to-fill) mature through December 2026 as the
history passes 14 and 30 days. Weekly benchmark rows (the tables behind the report: per industry, size bucket, vendor and
function) can be included.

### Schema

The CSV headers in the sample below are authoritative and match the rows the
[Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) emits today, so a pipeline built on the sample
works on the feed and on the API alike. Nested
fields (`functions`, `seniorityMix`, `topDepartments`, `topLocations`) are JSON arrays of `{name, count}` in the CSV
and JSON objects in the API output; load them as VARIANT or JSON columns. Consumers deduplicate `job_events` on vendor, slug, job id and event type.

## Free sample

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from
  2026-11-22, the second day of full-universe collection (so trends are still flat; the 30-day fields fill in through
  December).
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the role events of the same day.
- The [baseline study of 2026-11-20]({{ '/reports/2026-11-20/' | relative_url }}) is computed from a 14-day history on the
  YC subset; the [weekly reports]({{ '/reports/' | relative_url }}) are the best preview of what the history supports.
- Any day or 30-day window of the full archive, filtered, is available immediately, pay per row, on the
  [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) (pay per row, no request needed).

## Getting it into a warehouse

Today the archive is fetched per row from the feed: one scheduled run a day, written to S3, BigQuery or Snowflake
through Apify's integrations or a few lines of code against the API, at $0.01 per company-day and $0.004 per role
event. A delivered history (files or a warehouse share) is not a listed product yet, because the daily history is
only weeks old; if you need one, [ask](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml)
and say what for. Academic and journalistic use: usually a free cut with attribution.

## Quality

The collection checks itself every day: fetched-OK rate, day-over-day stability, a careers-page re-count of 25
boards and a re-fetch of 10 closed roles, with alert thresholds. The checks and a healthy day's numbers are on the
[methodology]({{ '/methodology/' | relative_url }}) page.

## Terms for the data

- **Self-serve products** (the feed, the trackers, the lookup, the leads) are billed, refunded and supported under
  [Apify's terms](https://apify.com/terms-of-service); the rows you fetch are yours to use in your own analyses and products.
- **Custom deliveries** (history cuts, files, a warehouse share) are licensed for internal use by the buying organisation. Raw rows may not be
  redistributed or resold; aggregates and derived metrics may be published with attribution to Agilityy Research.
- **Support**: replies within two business days; a private channel on request.

## Request access

<p><a class="btn" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Open a data access request</a></p>

It is a short GitHub issue form (organisation, use, tables, delivery). We reply within two business days; if you would rather not discuss it in public, say so in the form and we continue privately.
