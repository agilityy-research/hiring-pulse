---
title: "Get the data: every company's daily hiring numbers"
description: >-
  The daily data behind Hiring Pulse: every tracked company's open roles, roles opened and closed, growth, pay and work mode, as files each morning. Free by e-mail during the beta.
permalink: /get-the-data/
jsonld: dataset
dataset_name: "Hiring Pulse daily hiring signals and job events"
---
# Get the data

Every number in the weekly report comes from the daily data: one line per company per day (open roles, roles opened
and closed, growth, days-to-fill, function and seniority mix, AI/ML, remote and pay shares, a one-word signal) and one
line per role opened or closed.

{% if site.beta_signup_action != "" %}
<p id="beta-thanks" class="beta-thanks card"><b>Thanks.</b> Check your inbox for the confirmation e-mail and click its link; the next morning's files arrive before the US workday starts. Nothing there? Look in the spam folder, or sign up again below.</p>

## Free during the beta: every company's daily files by e-mail

Until {{ site.beta_end | date: "%-d %B %Y" }}, the whole daily data is free. Sign up with a work e-mail and two short
answers, confirm the address from the e-mail we send, and every morning you get:

- **Two spreadsheets for the day** that open in Excel or Google Sheets. One has a line per company: open roles, roles
  opened and closed, growth, how long roles stay open, the mix of functions and seniority, the AI/ML, remote and pay
  shares, and a one-word signal (accelerating, steady, flat or contracting). The other has a line per role opened or closed. The columns are those of the
  [free sample]({{ '/for-data-teams/' | relative_url }}#free-sample) plus location and pay fields.
- **The six days before**, linked in the same e-mail. Every link works for 7 days, so a missed morning costs nothing.
- **Who moved**: the companies that added and cut the most roles since the day before.

Each e-mail ends with one question; replies reach us directly, and they decide what the paid version looks like. After
the beta the full daily files will be $99 a month; we will write two weeks before the end date, and nothing is charged
unless you choose to subscribe then.

{% include beta-signup.html %}

{% endif %}
{%- if site.stripe_payment_link != "" %}
## Hiring Pulse Daily: everything, every day, $99 a month

For teams that want the whole benchmark every morning: a flat plan, billed by Stripe,
cancel any time.

- Every tracked company, every day: `daily_signals` (one row per company per day) and `job_events` (one row per role
  opened or closed), the latest day plus the previous 30 days, as CSV and JSON, the same columns as the
  [free sample]({{ '/for-data-teams/' | relative_url }}#free-sample).
- New files every morning, before the US workday starts. One URL per file with your key, for `curl`, Python, a scheduled job or a Google Sheet
  (`IMPORTDATA`). The key is shown once after checkout; the welcome page has copy-paste examples.
- Card, invoices and cancellation in the Stripe customer portal, linked from the welcome page.

<p><a class="btn" href="{{ site.stripe_payment_link }}">Subscribe to Hiring Pulse Daily, $99 a month</a></p>

{% endif %}
## Something else: the whole history, a custom cut, a feed into your systems

The daily history goes back to {{ site.coverage.daily_since }} and grows by one day every day. If you need it as files
in your own storage, a regular feed into your warehouse, or a cut of particular companies, industries or days,
[ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml) and say what it is for. Journalists and researchers usually get a cut free, with attribution.
The column list and loading notes are on [for data teams]({{ '/for-data-teams/' | relative_url }}).

## Free samples, no sign-up needed

- [daily_signals_sample.csv]({{ '/samples/daily_signals_sample.csv' | relative_url }}): 200 companies from one day of collection, every column.
- [job_events_sample.csv]({{ '/samples/job_events_sample.csv' | relative_url }}): the roles opened and closed on the same day.
- The [weekly reports]({{ '/reports/' | relative_url }}) themselves are the best preview of what the history supports.


## Terms for the data

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

{% if site.beta_signup_action != "" -%}
<p><a class="btn" href="#beta">Get the daily files free</a> <a class="btn alt" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for something else</a></p>
{%- elsif site.stripe_payment_link != "" -%}
<p><a class="btn" href="{{ site.stripe_payment_link }}">Subscribe to Hiring Pulse Daily, $99 a month</a> <a class="btn alt" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for something else</a></p>
{%- else -%}
<p><a class="btn" href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for the data</a></p>
{%- endif %}

Loading the files into a warehouse, or need the column list first? See [for data teams]({{ '/for-data-teams/' | relative_url }}).
