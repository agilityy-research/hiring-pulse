---
title: "Methodology: how the startup hiring benchmarks are measured and checked"
description: >-
  How Hiring Pulse measures startup hiring: daily reads of 21,922 public job boards, how opened and closed roles and days-to-fill are defined, daily checks.
permalink: /methodology/
---
# Methodology

## Sources

- **Job boards.** Companies that publish a job board on {{ site.coverage.vendors }}. Each vendor offers a public feed
  that the company's own careers page is built from; we read that feed once a day per board. No login, no scraping
  of pages behind a login, no personal data.
- **Universe.** The list of companies comes from public accelerator directories and public web indexes, is rebuilt
  monthly, and every board is verified against the company name before it enters the list. Since
  {{ site.coverage.companies_since }} it holds {{ site.coverage.companies }} companies ({{ site.coverage.companies_before }} from
  {{ site.coverage.daily_since }} to {{ site.coverage.companies_since }}, on Greenhouse, Lever and Ashby); {{ site.coverage.with_industry }} of them are Y
  Combinator companies with industry, sub-industry, batch and team size from the public YC directory, which is where
  the industry and size segments come from.
- **Funding.** The funded-and-hiring products read the SEC's public EDGAR daily index and Form D filings. The weekly
  report does not use them.

## Definitions

- **Snapshot.** The set of open roles on a board at the time of the daily read. A role is identified by the vendor's
  job id.
- **Opened / closed.** A role is *opened* the first day it appears and *closed* the first day it is gone. If a board
  returns an empty list after having had roles, the previous snapshot is kept and no closures are recorded, so a vendor
  hiccup cannot show up as a mass lay-off.
- **Days-to-fill.** The age of a role on the day it closes, counted from the day it was first seen. Roles older than
  365 days at closure are excluded as evergreen postings. We do not know whether a closed role was filled or withdrawn;
  "days-to-fill" is the posting's lifetime.
- **Window.** Growth, roles opened and roles closed compare today with 30 days earlier for the same companies.
- **Stock and flow figures.** Open roles, functions, AI/ML share, remote share and seniority (the stock) are reported
  for every company with a snapshot in the last 3 days. Growth, roles opened and closed, days-to-fill and the movers
  (the flows) are reported for companies with at least 14 days of daily history; until {{ site.coverage.flows_from }}
  that is the Y Combinator subset collected from {{ site.coverage.yc_subset_since }}, from then on the whole universe.
- **Since previous edition.** Each Monday edition is compared with the one before it on the same definitions; the
  trend chart lengthens by one point per edition. When the universe changes size the report says so next to the number.
- **Segments.** A segment (industry, size bucket, vendor) is reported only when it has at least 5 companies. Growth is
  computed on the segment's total open roles; days-to-fill and remote share are medians across companies.
- **Function, seniority, AI/ML.** Assigned from the job title with a fixed, published keyword taxonomy, the same one
  the data products use, so numbers are comparable week to week. "AI/ML roles" means the title names machine
  learning, AI, LLM, data science or a close variant; a software engineer who will use AI tools is not counted.
- **Remote share.** Share of a company's open roles whose location or remote flag says remote.

## Verification: how we know the data is complete and accurate

Nobody eyeballs rows. The collection measures itself at the end of every run and writes a quality record for the day;
a monitoring job turns the thresholds below into alerts, and a run that fails them is repaired or re-run before the
next report.

| Check | How | Threshold |
|---|---|---|
| Fetched-OK rate | Boards that answered with a job list, over all boards in the universe | alert below 97% |
| Open-roles stability | Total open roles against the previous day, overall and per vendor | alert on a move of more than ±15% in a day |
| Careers-page agreement | Every run, 25 boards (a fixed sample for the date) are re-counted on the vendor's human careers page, HTML not JSON; agreement means within ±5% | alert below 90% agreement |
| Closure confirmation | Every run, 10 roles the diff just marked closed are re-fetched at their job URL; confirmed means gone, redirected or no longer naming the role | alert below 90% confirmed |
| Freshness | A day without a quality record | alert after 2 days |
| Suspicious empties | Boards returning zero roles after having some (previous snapshot kept) | reviewed when they cluster on one vendor |

A healthy day looks like: fetched OK about 99%, open roles within a few percent of yesterday, careers-page agreement
22 or more of 25, closures confirmed 10 of 10. The first full-universe day, 2026-11-22, measured 99.5% of boards
fetched, 21 of 21 verifiable boards in agreement and 10 of 10 closures confirmed.

## Known limits

- Only companies on the six vendors are covered. Companies with a custom careers site, or on Workday, iCIMS,
  Workable and the like, are not in the daily universe; the sample skews to venture-backed technology companies.
- A posting is not a hire. Days-to-fill measures how long a role stays advertised.
- Titles are classified by keywords; unusual titles land in "Other".
- Industry and size segments exist only for the YC-backed subset, where the public directory provides them.
- Daily history on the full universe starts on {{ site.coverage.daily_since }} ({{ site.coverage.companies_before }} companies) and
  {{ site.coverage.companies_since }} ({{ site.coverage.companies }}); the {{ site.coverage.yc_subset }}-company YC subset was collected
  from {{ site.coverage.yc_subset_since }}. Flow figures for the whole universe therefore mature through December 2026.

## Licence and citation

Reports are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cite as
"Agilityy Research, Hiring Pulse, week of YYYY-MM-DD" with a link to the report. Corrections and questions:
[open an issue](https://github.com/agilityy-research/hiring-pulse/issues) in the repository.
