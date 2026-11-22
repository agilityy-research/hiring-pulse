---
title: "Hiring signals data and job board scrapers, pay per record"
description: >-
  Buy hiring signals data per record: the daily Hiring Signals Feed for 10,900+ companies, job board trackers for your
  own company list, a company hiring lookup, SEC Form D funded-and-hiring leads, and Greenhouse, Lever, Ashby and
  Workable job scrapers. Prices per record, no subscription, on the Apify Store.
permalink: /data/
---
# The data, per record

Everything below runs on the Apify Store under the account [agilityy](https://apify.com/agilityy): no subscription,
you pay per record returned plus a few cents of compute per run, and you can schedule any of them daily. The same
code produces the weekly report on this site. Want the whole history instead of records?
See [for data teams]({{ '/for-data-teams/' | relative_url }}).

## Hiring signals

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-signals-feed">Hiring Signals Feed</a></h3>
<p>Daily hiring signals and opened/closed role events for 10,900+ companies on Greenhouse, Lever and Ashby, served
from our archive rather than scraped: pick a day (default: yesterday) or a window of up to 30 days, filter by
company, provider, industry, function or signal, and the matching rows are in your run within seconds.</p>
<p><span class="price">$0.01 per company signal</span> (one company, one day) · <span class="price">$0.004 per role event</span>.
A whole day of every company is about $109; one industry or a watch-list costs cents to a few dollars a day.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-velocity-signals">Hiring Velocity Signals</a></h3>
<p>Give it your own list of companies (names, websites or careers URLs). Each run it reads every company's public
job board, compares it with the previous run and returns one record per company: open roles, roles opened and
closed, growth, 30-day trend, median days-to-fill, department mix, remote and AI/ML share, and a one-word signal
(ACCELERATING, STEADY, FLAT, CONTRACTING). Optionally one record per role opened or closed. Your history compounds
in your own account.</p>
<p><span class="price">$0.05 per company per run</span> · <span class="price">$0.004 per role event</span>.
Tracking 200 companies daily is about $300 a month.</p></div>

<div class="card"><h3><a href="https://apify.com/agilityy/company-hiring-lookup">Company Hiring Lookup</a></h3>
<p>One company in, one record out, immediately: board found or not, open roles by function and seniority, AI/ML roles,
remote share, locations, sample titles and job links. No history and no list to maintain; shaped for sales enrichment
waterfalls and for AI agents that call one tool per company.</p>
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
<p><span class="price">$0.03 per lead</span>. A daily run yields roughly 20–60 leads.
Lighter variant without the hiring check: <a href="https://apify.com/agilityy/startup-funding-monitor">Startup Funding Monitor</a>, $0.02 per company.</p></div>

## Job board scrapers

One row per open role (title, department, location, remote flag, apply URL, posted date, function, seniority, AI/ML
flag) from any company's board on the vendor named, via the vendor's official public endpoint: no login, no proxies.
Company names, slugs or board URLs in.

<div class="grid">
<div class="card"><h3><a href="https://apify.com/agilityy/greenhouse-jobs-scraper">Greenhouse Jobs Scraper &amp; API</a></h3><p>boards.greenhouse.io</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/lever-jobs-scraper">Lever Jobs Scraper &amp; API</a></h3><p>jobs.lever.co</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/ashby-jobs-scraper">Ashby Jobs Scraper &amp; API</a></h3><p>jobs.ashbyhq.com</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
<div class="card"><h3><a href="https://apify.com/agilityy/workable-jobs-scraper">Workable Jobs Scraper &amp; API</a></h3><p>apply.workable.com</p><p><span class="price">$0.0015 per role</span>, $1.50 per 1,000</p></div>
</div>

## The engine behind the report

<div class="card"><h3><a href="https://apify.com/agilityy/hiring-pulse-benchmarks">Hiring Pulse Benchmarks</a></h3>
<p>Turns a Hiring Velocity Signals history, yours or ours, into benchmark rows by industry, company size and job-board
vendor, leaderboards, and a publish-ready Markdown report like the ones on this site.</p>
<p><span class="price">$0.10 per benchmark row</span> · <span class="price">$0.02 per leaderboard row</span>. A weekly report over a few hundred companies is about $6.</p></div>

<p class="small muted">Prices are the Store list prices on 2026-11-22 and are shown on each listing; Apify adds its compute
charge (cents per run). Listings published in the last few days can take a day to appear in Store search; the direct
links above work as soon as each one is public.</p>
