---
title: "Methodology: how the startup hiring benchmarks are measured and checked"
description: >-
  How Hiring Pulse measures startup hiring: daily reads of 21,000+ public job boards, how opened and closed roles and days-to-fill are defined, daily checks.
permalink: /methodology/
---
# Methodology

This page tells you where every number on the site comes from, what each term means, how the collection checks itself,
and what the numbers cannot tell you. If you want to quote a figure or build on the data, read this first.

## Where the numbers come from

- **Company job boards.** Most startups run their careers page on job-board software: {{ site.coverage.vendors }}.
  We call those six systems the *vendors*. Each vendor publishes a public list of a company's open roles, the same list
  the company's careers page is built from. We read that list once a day for every company we track. No login, no
  pages behind a login, no personal data.
- **Which companies.** The list of companies is built from public accelerator directories and public web indexes,
  refreshed monthly, and every board is checked against the company name before it enters the list. Since
  {{ site.coverage.companies_since }} it holds {{ site.coverage.companies }} companies ({{ site.coverage.companies_before }} from
  {{ site.coverage.daily_since }} to {{ site.coverage.companies_since }}, on Greenhouse, Lever and Ashby). Of these,
  {{ site.coverage.with_industry }} are Y Combinator companies with industry, sub-industry, batch and team size
  from the public YC directory; that is where the industry and company-size breakdowns come from.

## What each term means

- **Daily read.** The set of open roles on a company's board at the time we read it that day (called a *snapshot* in the column names of the data). A role is identified by
  the vendor's job id, so a retitled role is still the same role.
- **Opened and closed.** A role is *opened* the first day it appears and *closed* the first day it is gone. If a board
  returns an empty list after having had roles, we keep the previous day's list and record no closures, so a vendor
  outage cannot show up as a mass lay-off.
- **Days-to-fill.** How many days a posting stayed up: the age of a role on the day it closes, counted from the
  posting date the job board publishes (Greenhouse may give only a last-updated date), or, where it publishes none, from
  the first day we read the role. The figure is the median over the closed roles. We do not know whether a closed role was filled or withdrawn, so "days-to-fill" is the posting's
  lifetime, not the hiring time. Roles older than 365 days at closure are left out as evergreen postings.
- **Growth and the 30-day window.** Growth, roles opened and roles closed compare today with 30 days earlier for the
  same companies. While the history is shorter than 30 days, the report says which span it measured (for example
  "16 days earlier").
- **Figures that need history, and figures that do not.** Open roles, functions, AI/ML share, remote share and
  seniority need only today's read, so they cover every company read in the last 3 days. Growth, roles opened and
  closed, days-to-fill and the movers need history, so they cover companies with at least 14 days of daily reads:
  until {{ site.coverage.flows_from }} that is mostly the Y Combinator subset read daily since {{ site.coverage.yc_subset_since }}
  (each edition gives the exact count),
  from then on every company.
- **Signal.** One word per company per day that sums up the change in its open roles over the window: accelerating,
  steady, flat or contracting. It is derived from the same growth figures by the same rule for every company, so you can
  filter on it without reading the numbers.
- **Since previous edition.** Each Monday edition is compared with the one before it on the same definitions; the
  trend chart gains one point per edition. When the job-title rules or a figure's definition change (last on 27 November
  2026: revised title rules, and days-to-fill taken over closed roles instead of across companies), the figures they
  affect are not compared with the edition before, and the report says so. When the set of companies changes size, the report says so next to the number.
- **Segments.** An industry, company-size bucket or vendor is reported only when it has at least 5 companies. Growth is
  computed on the segment's total open roles; days-to-fill is the median over its closed roles and remote share the median across its companies.
- **Function, seniority, AI/ML.** Function comes from the job title, or from the posting's department when the title
  names no function; seniority and AI/ML come from the title. All use a fixed, published list of keywords, the same one
  the data products use, so numbers compare week to week. "AI/ML roles" means the title names AI, machine learning, LLMs,
  generative AI, deep learning, NLP, computer vision, or an applied or research scientist role. A data scientist title
  on its own is not counted, nor is a software engineer who will use AI tools, an employer tagline such as "(AI x
  Greentech)" or an AI-training gig ("AI Trainer").
- **Remote share.** In the weekly report and on the homepage: the share of open roles whose location or remote flag says
  remote, over all open roles. The data pages instead count the work mode a posting states (remote, hybrid or on-site) and
  give each share of the roles that state one, so their remote figure is a different measure and is higher.

## How we know the data is complete and accurate

No manual review: the collection measures itself at the end of every run and writes a quality record for the day. A
monitoring job turns the thresholds below into alerts, and a run that fails them is repaired or re-run before the
next report.

| Check | How | Threshold |
|---|---|---|
| Boards answered | Boards that returned a job list, over all boards tracked | alert below 97% |
| Day-to-day stability | Total open roles against the previous day, overall and per vendor | alert on a move of more than ±15% in a day |
| Careers-page agreement | Every run, 25 boards (a fixed sample for the date) are re-counted on the vendor's human careers page, HTML not JSON; agreement means within ±5% | alert below 90% agreement |
| Closures confirmed | Every run, 10 roles just marked closed are re-fetched at their job URL; confirmed means gone, redirected or no longer naming the role | alert below 90% confirmed |
| Freshness | A day without a quality record | alert after 2 days |
| Suspicious empties | Boards returning zero roles after having some (previous day's list kept) | reviewed when they cluster on one vendor |

A healthy day looks like: about 99% of boards answered, open roles within a few percent of yesterday, careers-page
agreement on 22 or more of 25 boards, closures confirmed 10 of 10. The first full day, 2026-11-22, measured 99.5% of
boards answered, 21 of 21 verifiable boards in agreement and 10 of 10 closures confirmed.

## Who is in the benchmark, and who is not

We track every company with a public job board on the six vendors that our monthly refresh can find. That is mostly
venture-backed technology companies, but a public board does not make a startup. **Large employers, staffing and
recruiting agencies, franchise networks, hospitals, universities and public bodies, and vendors' own test boards are
tracked in the daily data but excluded from the benchmark**: the findings, charts, headline numbers and tables. A company
is excluded when our company record tags it with a reason, or, until it is tagged, when its board lists more than 1,000
open roles, a size very few startups reach. Every edition states how many companies were excluded and why. The rule was
introduced on 2026-11-24 after the first full edition listed Domino's, AECOM and two staffing agencies among the largest
"startup" boards.

## Cities, work mode, pay and skills

Since 25 November 2026 every role we read carries the city and country its posting names, its work mode, its advertised
pay range and the skills its description names. The [hiring by city]({{ '/data/cities/' | relative_url }}), [salary benchmarks]({{ '/data/salaries/' | relative_url }})
and [skills in demand]({{ '/data/skills/' | relative_url }}) pages are recomputed with every Monday edition, over the same companies as the benchmark.

- **City.** Taken from the vendor's structured address where there is one, otherwise from the location text. A role counts
  once, in the first city its posting names. Spellings of one city are merged (NYC and New York City, München and Munich); a
  city written without a country takes the country most of its other roles name. A city is listed only when five or more
  companies are hiring there. "Washington" is Washington, DC: almost all of its postings name DC; the few that give only
  "Washington" are counted with it.
- **Work mode.** Remote, hybrid or on-site from the vendor's field (Lever, Ashby, SmartRecruiters, Recruitee) or, where the
  vendor has none (Greenhouse, Personio), from words in the title or location. Shares are of the roles that state a mode; the
  pages say how many do.
- **New roles.** First seen (or posted, where the vendor publishes a date) in the last seven days, counted only at companies
  we have read for longer than that.
- **Pay.** The range as the posting states it. Postings rarely say whether it is base salary or, as in many sales roles,
  on-target earnings including commission, so the two are not separated; equity is not counted. Where a Greenhouse posting
  lists several ranges (for example by location), the first one is used. Pay is read from Greenhouse, Lever, Ashby and
  Recruitee; SmartRecruiters publishes pay only on each posting's own page, which we do not read yet, and Personio's feed
  carries no pay, so their roles are not in the pay figures. Lever and Ashby ranges written only in the description text
  are not read. Each row shows three figures: the **median** (each role counted at the midpoint of its range), the
  **typical range** (the median posted minimum to the median posted maximum) and the **high end** (one role in ten has
  a range top at or above it; it is not the highest salary posted). Salary figures use roles located in the United States:
  the posting, or the job board's own country field, places the role in the US (a US city or state, or "Remote US"); a
  remote posting with no country is left out. Hourly rates
  are a separate figure, never converted into salaries. A title and range that one company posts several times counts
  once, after the US filter. Levels come from words in the title and are compared within one function at a time; the
  salaries page lists the main words (for example "Member of Technical Staff" and "Solutions Architect" carry no level,
  "Chief of Staff" is not C-level, and "Associate" is not entry level for lawyers, physicians, dentists and veterinarians, or at a law firm). A figure needs 30 roles
  from 8 companies, and no single company may supply more than half of it. Unreadable or implausible ranges are dropped:
  a yearly figure below $10,000 or above $2 million, or a top more than five times the bottom. Figures are rounded half
  up ($162,500 shows as $163k).
- **Skills.** Each description is matched against one fixed vocabulary of about 480 terms (languages, frameworks, cloud and
  data platforms, business tools, methods, certifications, licences and spoken languages); short or ambiguous names match
  only in their exact form. The skills page is published once nine in ten descriptions have been read with the vocabulary.

## What the numbers cannot tell you

- Only companies on the six vendors are covered. Companies with a custom careers site, or on Workday, iCIMS,
  Workable and the like, are not tracked daily; the sample leans to venture-backed technology companies.
- A posting is not a hire. Days-to-fill measures how long a role stays advertised.
- Titles and departments are classified by keywords; roles neither one places land in "Other".
- Industry and company-size breakdowns exist only for the Y Combinator subset, where the public directory provides them.
- Pay is what a posting advertises, and only some postings advertise it; cities are the first one a posting names.
- Daily history on the full set of companies starts on {{ site.coverage.daily_since }} ({{ site.coverage.companies_before }} companies) and
  {{ site.coverage.companies_since }} ({{ site.coverage.companies }}); the YC subset ({{ site.coverage.yc_subset }} companies in the 20 November baseline) was collected
  from {{ site.coverage.yc_subset_since }}. The history-based figures for every company therefore fill in through December 2026.

## Quoting the reports

Reports are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cite as
"Agilityy Research, Hiring Pulse, YYYY-MM-DD" (the edition date) with a link to the report. Found an error or have a
question about a definition? [Contact us]({{ '/contact/' | relative_url }}).

## Next

- Read [this week's report]({{ '/reports/latest/' | relative_url }}), measured exactly as described here.
- Want the rows behind it, for your own companies and days? See [get the data]({{ '/get-the-data/' | relative_url }}).
