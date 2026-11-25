---
title: "Hiring data products and prices: daily data, trackers, lookup, funded leads, scrapers"
description: >-
  Hiring data per row: daily hiring signals for 21,000+ companies, tracking of your own list, a one-company lookup, SEC Form D funded leads, job board scrapers.
permalink: /data/
jsonld: dataset
dataset_name: "Hiring Pulse data products"
---
# Products and prices

Every product below is sold per row on the [Apify Store](https://apify.com/agilityy). There is no subscription: you pay
for the rows you receive plus a few cents of computing cost per run, and Apify bills you. Every product can run on a
schedule, be called from code, or be used from an AI assistant. The first $5 of usage each month is free on any Apify
account.

**Not sure where to start?** Most buyers want the first product, the Hiring Signals Feed: it is the daily data the
weekly report is computed from. [How to buy]({{ '/get-the-data/' | relative_url }}) walks you through a purchase with
worked prices; [for data teams]({{ '/for-data-teams/' | relative_url }}) has the column list and a free sample.

## The daily data behind the report

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-signals-feed">Hiring Signals Feed</a></h3>
<p>One row per company per day (a "company-day") for the {{ site.coverage.companies }} companies with public job boards on
{{ site.coverage.vendors }}, served from our stored history, so your rows arrive within seconds. Pick a day (default:
yesterday) or a window of up to 30 days, filter by company, job-board vendor, industry, function, signal or minimum open
roles, and download. Each row carries: open roles, roles opened and closed, net change, growth, 30-day trend, median
days-to-fill (how long a posting stays up before it closes), remote share, AI/ML roles and share, function and seniority
mix, top departments and locations, and a one-word signal (accelerating, steady, flat or contracting). You can also take
one row per role opened or closed that day.</p>
<p><b>Filled in today:</b> open roles, roles opened and closed, function and seniority mix, AI/ML and remote share, signal.
<b>From the edition of 2026-12-07:</b> 14-day growth and days-to-fill; <b>from 2026-12-22:</b> the 30-day trend. The
history is young, and these columns fill in as it grows.</p>
<p><span class="price">$0.01 per company-day</span> · <span class="price">$0.004 per role event</span>.
A whole day of every company is about $219; one industry or a watch list costs cents to a few dollars a day.</p></div>

## Track your own companies

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-velocity-signals">Hiring Velocity Signals</a></h3>
<p>For companies that are not in our benchmark, or when you want the reads to happen in your own account. Give it your
list (names, websites or careers URLs). Each run reads every company's public job board, compares it with the previous
run and returns one row per company with the same columns as the Hiring Signals Feed, plus one row per role opened or
closed if you ask for it. Each run is stored in your Apify account, so your own history builds up run by run.</p>
<p><span class="price">$0.025 per company per run</span> launch price (list $0.05) · <span class="price">$0.004 per role event</span>.
Tracking 200 companies every day is about $150 a month at the launch price.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/yc-companies-hiring-tracker">YC Companies Hiring Tracker</a></h3>
<p>Hiring Velocity Signals with a verified list of 650+ Y Combinator job boards built in: run it with no input to track
all of YC, schedule it daily, and get the same per-company rows and role events, with batch, industry and team size
attached.</p>
<p><span class="price">$0.05 per company signal</span> · <span class="price">$0.004 per role event</span>.</p></div>

## Check one company right now

<div class="card"><h3><a href="https://apify.com/agilityy/company-hiring-lookup">Company Hiring Lookup</a></h3>
<p>One company in, one row out, immediately: whether a board was found, open roles by function and seniority, AI/ML
roles, remote share, locations, sample titles and job links. No history and no list to maintain. Built for sales
enrichment (one call per account) and for AI assistants that call one tool per company.</p>
<p><span class="price">$0.02 per company looked up</span>.</p></div>

## Companies that just raised money

<div class="card"><h3><a href="https://apify.com/agilityy/funded-and-hiring-leads">Funded &amp; Hiring Leads</a></h3>
<p>Every US private company that raises money under Regulation D files a Form D with the SEC within 15 days. This
product reads the SEC's daily index, drops the funds, SPVs and real-estate syndications (about 80% of filings) and gives
you one CRM-ready lead per operating company: executives and directors, signer, amount raised, offering size, investor
count, industry, filing links, a live check of whether the company is hiring, and a 0–100 lead score.</p>
<p><span class="price">$0.015 per lead</span> launch price (list $0.03). A daily run yields roughly 20–60 leads.
Lighter variant without the hiring check: <a href="https://apify.com/agilityy/startup-funding-monitor">Startup Funding Monitor</a>, $0.02 per company.</p></div>

## Every open role on a board

One row per open role (title, department, location, remote flag, apply URL, posted date, function, seniority, AI/ML
flag) from any company's board on the vendor named, read through the vendor's official public endpoint: no login, no
proxies. Give it company names, board slugs or board URLs. These read any board you point them at, including boards
outside our benchmark.

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

<p class="small muted">Launch prices hold until 2027-01-21. Apify adds its computing charge, a few cents per run. Billing, refunds and support for these products run under <a href="https://apify.com/terms-of-service">Apify's terms</a>; what you may do with the rows is in the <a href="{{ '/get-the-data/' | relative_url }}#terms-for-the-data">terms for the data</a>.</p>

## Next

Ready to buy? [How to buy]({{ '/get-the-data/' | relative_url }}) shows the three steps and what a typical purchase
costs. Need the whole history delivered, or a product that is not listed? [Ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml)
and say what for.
