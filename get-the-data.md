---
title: "How to buy: download, API or a bulk feed"
description: >-
  Three ways to get the daily hiring data behind Hiring Pulse: download JSON/CSV/Excel in the browser, call the API or schedule it, or take the full history as files or a Snowflake share
permalink: /get-the-data/
jsonld: dataset
dataset_name: "Hiring Pulse daily hiring signals and job events"
---
# How to buy

The numbers in every report come from a daily archive: one row per company per day (open roles, roles opened and
closed, growth, days-to-fill, function and seniority mix, AI/ML and remote share, a one-word signal) and one row per
role opened or closed. There are three ways to get it: download it in the browser, call it from code or a schedule,
or take the whole history as files. The first two run on the [Apify Store](https://apify.com/agilityy): you pay per
row, Apify bills you and adds a few cents of compute per run, there is no subscription and nothing to install.

## Pick the product

| You want | Product | One row is | Price |
|---|---|---|---|
| Yesterday's signals for every tracked company, or any day or 30-day window, filtered | [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) | one company, one day; or one role event | <span class="price">$0.01 per company-day</span>, $0.004 per role event |
| Daily tracking of your own list of companies, with history that compounds in your account | [Hiring Velocity Signals](https://apify.com/agilityy/hiring-velocity-signals) | one company per run | <span class="price">$0.025 per company</span> launch price (list $0.05), $0.004 per role event |
| One company checked right now: board found, roles by function and seniority, AI/ML and remote share | [Company Hiring Lookup](https://apify.com/agilityy/company-hiring-lookup) | one company | <span class="price">$0.02</span> |
| US companies that just raised money (SEC Form D), with a live hiring check and a lead score | [Funded &amp; Hiring Leads](https://apify.com/agilityy/funded-and-hiring-leads) | one lead | <span class="price">$0.015 per lead</span> launch price (list $0.03) |
| Every open role on one company's board, as rows | [Greenhouse](https://apify.com/agilityy/greenhouse-jobs-scraper), [Lever](https://apify.com/agilityy/lever-jobs-scraper), [Ashby](https://apify.com/agilityy/ashby-jobs-scraper) or [Workable](https://apify.com/agilityy/workable-jobs-scraper) Jobs Scraper | one role | <span class="price">$0.0015 per role</span> |

Launch prices until 2027-01-21; Apify adds a few cents of compute per run. The full catalogue with examples
is on [products and prices]({{ '/data/' | relative_url }}).

## 1. Run it in the browser and download JSON, CSV or Excel

<ol class="steps">
<li>Open the product page, for example the <a href="https://apify.com/agilityy/hiring-signals-feed">Hiring Signals Feed</a>, and click <b>Try for free</b>; a free Apify account takes a minute.</li>
<li>Set the input in the form: the day (default yesterday) or a window of up to 30 days, and any filters (vendor, industry, function, signal, minimum open roles, AI-only). Click <b>Start</b>; the rows are in the run within seconds.</li>
<li>Open the run's <b>Storage</b> tab and download the dataset as JSON, CSV, Excel, XML or HTML, or copy the download link into a spreadsheet.</li>
</ol>

## 2. Call it from code, or schedule it

Every product is an HTTP endpoint. Your API token is under Settings → API &amp; Integrations in the Apify Console.
One request runs the feed and returns the rows:

```bash
curl -X POST "https://api.apify.com/v2/acts/agilityy~hiring-signals-feed/run-sync-get-dataset-items?token=$APIFY_TOKEN&format=csv" \
  -H "Content-Type: application/json" -d '{"days": 1, "industries": ["Fintech"]}'
```

Python (`pip install apify-client`):

```python
from apify_client import ApifyClient
client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("agilityy/hiring-signals-feed").call(run_input={"days": 7, "functions": ["Data & AI"]})
rows = client.dataset(run["defaultDatasetId"]).list_items().items   # list of dicts, one per company-day
```

The output columns are the ones in the [free sample]({{ '/for-data-teams/' | relative_url }}#free-sample), so a
pipeline built on the sample works on the API.

To get the rows without code, click <b>Schedule</b> on the product page, set a cadence (the feed is refreshed daily by
07:00 UTC), and in the <b>Integrations</b> tab choose where they go: Google Sheets, Slack, a webhook, Airtable,
HubSpot, Zapier, Make or n8n ([Apify's integrations guide](https://docs.apify.com/platform/integrations)). AI
assistants can run the same products through Apify's MCP server at `https://mcp.apify.com`
([guide](https://docs.apify.com/platform/integrations/mcp)).

## 3. The full history for data teams: monthly files or a Snowflake share

For a warehouse, a model or a product you want the whole archive, every company and every day since
{{ site.coverage.daily_since }}, delivered as files or a share rather than fetched row by row. Three tables
(`companies`, `daily_signals`, `job_events`), appended daily, with a Snowflake DDL and the same columns as the free
sample.

| Route | Delivery | Price |
|---|---|---|
| Monthly CSV files, 1-month term | CSV files in S3 now; AWS Data Exchange listing from late December 2026 | $149 per month |
| Annual feed with the full history | CSV files in S3 now; AWS Data Exchange listing from late December 2026 | $1,200 per year |
| Snowflake share | Secure share now; Marketplace listing from late December 2026 | $249 per month |
| Enterprise: redistribution rights, custom cuts, SLA | As above | $5,000–8,000 per year |

Every bulk route starts with the short [data access request](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml)
form (organisation, use, tables, delivery); we reply within two business days; ask in the form for a private channel. Schema, sample rows and coverage details: [for data teams]({{ '/for-data-teams/' | relative_url }}).
Academic and journalistic use is usually a free cut with attribution.

## Terms for the data

- **Self-serve products** (the feed, the trackers, the lookup, the leads) are billed, refunded and supported under
  [Apify's terms](https://apify.com/terms-of-service); the rows you fetch are yours to use in your own analyses and products.
- **Bulk files and the Snowflake share** are licensed for internal use by the buying organisation. Raw rows may not be
  redistributed or resold; aggregates and derived metrics may be published with attribution to Agilityy Research.
- **Terms**: monthly plans can be cancelled at the end of any month; annual plans run twelve months. Invoices in USD,
  by card or bank transfer; the contracting entity and tax details are stated on the quote.
- **Support**: replies within two business days; a private channel on request.

## Free samples, no account needed

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from one day of collection, every column.
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the role events of the same day.
- The [weekly reports]({{ '/reports/' | relative_url }}) themselves are the best preview of what the history supports.
