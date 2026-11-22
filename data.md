---
title: "Hiring data products and prices: feed, trackers, lookup, funded leads, scrapers"
description: >-
  Hiring data per row: a daily signals feed for 21,000+ companies, tracking of your own list, a one-company lookup, SEC Form D funded leads, job board scrapers.
permalink: /data/
jsonld: dataset
dataset_name: "Hiring Pulse data products"
---
# Products and prices

Everything below is sold per row on the [Apify Store](https://apify.com/agilityy): no subscription, you pay for the
rows you receive plus a few cents of compute per run, Apify bills you, and every product can run on a schedule, be
called from code or be used from an AI assistant. The six ways to get any of them are on
[how you get the data]({{ '/get-the-data/' | relative_url }}); the whole history as files or a share is on
[for data teams]({{ '/for-data-teams/' | relative_url }}). The weekly report on this site is computed from the same data.

## Hiring signals

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-signals-feed">Hiring Signals Feed</a></h3>
<p>Daily hiring signals and opened/closed role events for {{ site.coverage.companies }} companies with public job boards
({{ site.coverage.vendors }}), served from the archive rather than scraped: pick a day (default: yesterday) or a window
of up to 30 days, filter by company, vendor, industry, function, signal or minimum open roles, and the matching rows
are in your run within seconds. One row per company per day: open roles, roles opened and closed, net change, growth,
30-day trend, median days-to-fill, remote share, AI/ML roles and share, function and seniority mix, top departments
and locations, one-word signal. Growth, trend and days-to-fill fill in from December 2026 as the daily history
passes 14 and 30 days.</p>
<p><span class="price">$0.01 per company-day</span> · <span class="price">$0.004 per role event</span>.
A whole day of every company is about $219; one industry or a watch-list costs cents to a few dollars a day.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-velocity-signals">Hiring Velocity Signals</a></h3>
<p>Give it your own list of companies (names, websites or careers URLs). Each run it reads every company's public
job board, compares it with the previous run and returns one row per company: open roles, roles opened and
closed, growth, 30-day trend, median days-to-fill, department mix, remote and AI/ML share, and a one-word signal
(ACCELERATING, STEADY, FLAT, CONTRACTING). Optionally one row per role opened or closed. Your history compounds
in your own account.</p>
<p><span class="price">$0.025 per company per run</span> launch price until 2027-01-21 (list $0.05) · <span class="price">$0.004 per role event</span>.
Tracking 200 companies daily is about $150 a month at the launch price.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/company-hiring-lookup">Company Hiring Lookup</a></h3>
<p>One company in, one row out, immediately: board found or not, open roles by function and seniority, AI/ML roles,
remote share, locations, sample titles and job links. No history and no list to maintain; shaped for sales enrichment
waterfalls and for AI assistants that call one tool per company.</p>
<p><span class="price">$0.02 per company looked up</span>.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/yc-companies-hiring-tracker">YC Companies Hiring Tracker</a></h3>
<p>Hiring Velocity Signals with a verified list of 650+ Y Combinator job boards built in: run it with empty input to
track all of YC, schedule it daily, and get the same per-company signals and role events, with batch, industry and
team size attached.</p>
<p><span class="price">$0.05 per company signal</span> · <span class="price">$0.004 per role event</span>.</p></div>

## Funding signals

<div class="card"><h3><a href="https://apify.com/agilityy/funded-and-hiring-leads">Funded &amp; Hiring Leads</a></h3>
<p>Every US private company that raises money under Regulation D files a Form D with the SEC within 15 days. This
reads the SEC's daily index, drops the funds, SPVs and real-estate syndications (about 80% of filings) and returns one
CRM-ready lead per operating company: executives and directors, signer, amount raised, offering size, investor count,
industry, filing links, a live check of whether the company is hiring, and a 0–100 lead score.</p>
<p><span class="price">$0.015 per lead</span> launch price until 2027-01-21 (list $0.03). A daily run yields roughly 20–60 leads.
Lighter variant without the hiring check: <a href="https://apify.com/agilityy/startup-funding-monitor">Startup Funding Monitor</a>, $0.02 per company.</p></div>

## Job board scrapers

One row per open role (title, department, location, remote flag, apply URL, posted date, function, seniority, AI/ML
flag) from any company's board on the vendor named, via the vendor's official public endpoint: no login, no proxies.
Company names, slugs or board URLs in. These read any board you point them at; the daily archive behind the report
covers {{ site.coverage.vendors }} boards.

<div class="grid">
<div class="card"><h3><a href="https://apify.com/agilityy/greenhouse-jobs-scraper">Greenhouse Jobs Scraper &amp; API</a></h3><p>boards.greenhouse.io</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/lever-jobs-scraper">Lever Jobs Scraper &amp; API</a></h3><p>jobs.lever.co</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/ashby-jobs-scraper">Ashby Jobs Scraper &amp; API</a></h3><p>jobs.ashbyhq.com</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/workable-jobs-scraper">Workable Jobs Scraper &amp; API</a></h3><p>apply.workable.com</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
</div>

## Benchmarks on your own list

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-pulse-benchmarks">Hiring Pulse Benchmarks</a></h3>
<p>Turns a Hiring Velocity Signals history, yours or ours, into benchmark rows by industry, company size and job-board
vendor, leaderboards, and a publish-ready report with findings and charts in the same format as the editions on this site.</p>
<p><span class="price">$0.10 per benchmark row</span> · <span class="price">$0.02 per leaderboard row</span>. A weekly report over a few hundred companies is about $6.</p></div>

<p class="small muted">Prices are the Store list prices on 2026-11-22 and are shown on each listing; Apify adds its compute
charge (cents per run). Launch prices run until 2027-01-21.</p>
