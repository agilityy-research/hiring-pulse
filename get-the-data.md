---
title: "How to buy: pay per row, download or API"
description: >-
  How to buy the daily hiring data behind Hiring Pulse: pay per row on the Apify Store, download JSON/CSV/Excel in the browser, or call the API and schedule it
permalink: /get-the-data/
jsonld: dataset
dataset_name: "Hiring Pulse daily hiring signals and job events"
---
# How to buy

{% if site.beta_signup_action != "" %}
<p id="beta-thanks" class="beta-thanks card"><b>Thanks.</b> Check your inbox for the confirmation e-mail and click its link; the next morning's files arrive by about 07:30 UTC. Nothing there? Look in the spam folder, or sign up again below.</p>

## Free during the beta: every company's daily files by e-mail

Until {{ site.beta_end | date: "%-d %B %Y" }}, the whole daily data is free. Sign up with a work e-mail and two short
answers, confirm the address from the e-mail we send, and every morning you get:

- **Two CSV files for the day**, every tracked company: `daily_signals` (one row per company: open roles, roles opened
  and closed, growth, days-to-fill, function and seniority mix, AI/ML, remote and pay shares, a one-word signal) and
  `job_events` (one row per role opened or closed). The columns are those of the
  [free sample]({{ '/for-data-teams/' | relative_url }}#free-sample) plus location and pay fields.
- **The six days before**, linked in the same e-mail. Every link works for 7 days, so a missed morning costs nothing.
- **Who moved**: the companies that added and cut the most roles since the day before.

Each e-mail ends with one question; replies reach us directly, and they decide what the paid version looks like. After
the beta the full daily files will be $99 a month; we will write two weeks before the end date, and nothing is charged
unless you choose to subscribe then.

{% include beta-signup.html %}

## Pay per row: the Apify Store

{% endif %}
The numbers in every report come from the daily data: one row per company per day (open roles, roles opened and
closed, growth, days-to-fill, function and seniority mix, AI/ML and remote share, a one-word signal) and one row per
role opened or closed. You buy those rows on the [Apify Store](https://apify.com/agilityy), in a product called the
[Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed). You pay for the rows you receive, Apify bills you
and adds a few cents of computing cost per run, there is no subscription and nothing to install. You get the rows two
ways: download them in the browser, or call them from code or a schedule.

## What it costs

One row for one company on one day (a "company-day") is $0.01. One row for a role opened or closed is $0.004. Typical
purchases:

- **A watch list of 100 companies, every day for a month:** 3,000 rows, about $30. Runs on a schedule into a sheet or Slack.
- **One industry (about 700 companies) for one day:** 700 rows, about $7.
- **Every company for one day:** about 21,600 rows, about $219. This is the day the Monday report is computed from.
- **A small cut, to try it:** up to 500 rows, $0. Every Apify account has $5 of free usage a month.

Spending above the free $5 needs an Apify plan, from $19 a month, paid to Apify. The whole history delivered to your
own warehouse is not a listed product yet; if you need it, [ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml)
and say what for.

{%- if site.stripe_payment_link != "" %}
## Hiring Pulse Daily: everything, every day, $99 a month

For teams that want the whole benchmark every morning without an Apify account: a flat plan, billed by Stripe,
cancel any time.

- Every tracked company, every day: `daily_signals` (one row per company per day) and `job_events` (one row per role
  opened or closed), the latest day plus the previous 30 days, as CSV and JSON, the same columns as the
  [free sample]({{ '/for-data-teams/' | relative_url }}#free-sample).
- New files by 07:00 UTC. One URL per file with your key, for `curl`, Python, a scheduled job or a Google Sheet
  (`IMPORTDATA`). The key is shown once after checkout; the welcome page has copy-paste examples.
- Card, invoices and cancellation in the Stripe customer portal, linked from the welcome page.

<p><a class="btn" href="{{ site.stripe_payment_link }}">Subscribe to Hiring Pulse Daily, $99 a month</a></p>

{% endif %}
## Which product

| You want | Product | Price |
|---|---|---|
| Yesterday's rows for every company in the benchmark, or any day or 30-day window, filtered | [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) | <span class="price">$0.01 per company-day</span>, $0.004 per role event |
| Daily tracking of your own list of companies, with the history building up in your account | [Hiring Velocity Signals](https://apify.com/agilityy/hiring-velocity-signals) | <span class="price">$0.025 per company per run</span> launch price (list $0.05), $0.004 per role event |
| One company checked right now: board found, roles by function and seniority, AI/ML and remote share | [Company Hiring Lookup](https://apify.com/agilityy/company-hiring-lookup) | <span class="price">$0.02 per company</span> |
| US companies that just raised money (SEC Form D), with a live hiring check and a lead score | [Funded &amp; Hiring Leads](https://apify.com/agilityy/funded-and-hiring-leads) | <span class="price">$0.015 per lead</span> launch price (list $0.03) |
| Every open role on one company's board, as rows | [Greenhouse](https://apify.com/agilityy/greenhouse-jobs-scraper), [Lever](https://apify.com/agilityy/lever-jobs-scraper), [Ashby](https://apify.com/agilityy/ashby-jobs-scraper) or [Workable](https://apify.com/agilityy/workable-jobs-scraper) Jobs Scraper | <span class="price">$0.0015 per role</span> |

Launch prices hold until 2027-01-21; Apify adds a few cents of computing cost per run. What each product returns is on
[products and prices]({{ '/data/' | relative_url }}).

## 1. Run it in the browser and download JSON, CSV or Excel

<ol class="steps">
<li>Open the product page, for example the <a href="https://apify.com/agilityy/hiring-signals-feed">Hiring Signals Feed</a>, and click <b>Try for free</b>; a free Apify account takes a minute.</li>
<li>Set the input in the form: the day (default yesterday) or a window of up to 30 days, and any filters (job-board vendor, industry, function, signal, minimum open roles, AI-only). Click <b>Start</b>; the rows are in the run within seconds.</li>
<li>Open the run's <b>Storage</b> tab and download the dataset as JSON, CSV, Excel, XML or HTML, or copy the download link into a spreadsheet.</li>
</ol>

## 2. Call it from code, or schedule it

Every product is an HTTP endpoint. Your API token is under Settings → API &amp; Integrations in the Apify Console.
One request runs the Hiring Signals Feed and returns the rows:

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
pipeline you build on the sample works on the API.

To get the rows every day without code, click <b>Schedule</b> on the product page, set a cadence (the daily data is
refreshed by 07:00 UTC), and in the <b>Integrations</b> tab choose where they go: Google Sheets, Slack, a webhook,
Airtable, HubSpot, Zapier, Make or n8n ([Apify's integrations guide](https://docs.apify.com/platform/integrations)). AI
assistants can run the same products through Apify's MCP server at `https://mcp.apify.com`
([guide](https://docs.apify.com/platform/integrations/mcp)).

## Free samples, no account needed

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from one day of collection, every column.
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the role events of the same day.
- The [weekly reports]({{ '/reports/' | relative_url }}) themselves are the best preview of what the history supports.

## Terms for the data

- **Self-serve products** (the Hiring Signals Feed, the trackers, the lookup, the leads) are billed, refunded and supported under
  [Apify's terms](https://apify.com/terms-of-service); the rows you fetch are yours to use in your own analyses and products.
- **Custom deliveries** (history cuts, files, a warehouse share) are licensed for internal use by the buying organisation. Raw rows may not be
  redistributed or resold; aggregates and derived metrics may be published with attribution to Agilityy Research.
{%- if site.beta_signup_action != "" %}
- **Free beta files** (by e-mail, until the beta end date) are licensed for internal use by the subscriber's
  organisation. Raw rows may not be redistributed or resold; aggregates and derived metrics may be published with
  attribution to Agilityy Research. Provided as is, read from public job boards once a day, with no guarantee that every
  board answered on a given day. Unsubscribe at any time from any e-mail.
{%- endif %}
- **Support**: replies within two business days; a private channel on request.
{%- if site.stripe_payment_link != "" %}
- **Hiring Pulse Daily subscribers**: the files are licensed for internal use by the subscribing organisation; raw rows
  may not be redistributed or resold, aggregates and derived metrics may be published with attribution. Cancel any time
  in the customer portal; access runs to the end of the paid month. The data is provided as is, read from public job
  boards once a day, with no guarantee that every board answered on a given day; the daily quality checks are on the
  methodology page. Support within two business days.
{%- endif %}

## Next

<p><a class="btn" href="https://apify.com/agilityy/hiring-signals-feed">Open the Hiring Signals Feed on the Apify Store</a></p>

Loading the rows into a warehouse, or need the column list first? See [for data teams]({{ '/for-data-teams/' | relative_url }}).
