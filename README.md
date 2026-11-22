# Hiring Pulse — weekly hiring benchmarks across 10,000+ VC-backed companies

**Site: https://agilityy-research.github.io/hiring-pulse/** (becomes **https://hiring.agilityy.com** once the DNS
record below exists). **Agilityy Research** tracks the public job boards of more than 10,000 venture-backed companies
every day (Greenhouse, Lever, Ashby and Workable boards) and publishes a benchmark report here every Monday.

**Latest report → [reports/latest.md](reports/latest.md)** · archive in [`reports/`](reports/) (one file per week)

## What is in each report

- Open roles, roles opened and closed, and net growth over a 30-day window
- Share of companies accelerating vs contracting their hiring
- Median days-to-fill, measured from actual posting closures
- Open roles by function (Engineering, Sales, Data & AI, …) with days-to-fill per function
- Industry benchmarks: growth, opened/closed, days-to-fill
- AI/ML roles as a share of all open roles; remote share; seniority mix
- Leaderboards: largest net additions, fastest growing, biggest cuts

Coverage grows every week as more companies accumulate enough daily history to be benchmarked.
Numbers are computed from first-party daily snapshots, not from job aggregators, so a role counts once
and closures are observed rather than inferred. Full method: [methodology](methodology.md).

## Get the underlying data

The same pipeline is available as pay-per-event Actors on the Apify Store (no subscription, pay per result);
the full list with prices is on the site's [data page](data.md), the monthly feed for data teams on
[for-data-teams](for-data-teams.md).

| Actor | What it does |
|---|---|
| [Hiring Signals Feed](https://apify.com/agilityy/hiring-signals-feed) | Any day or 30-day window of this archive, filtered, pay per row |
| [Hiring Velocity Signals](https://apify.com/agilityy/hiring-velocity-signals) | Track any company's job board over time: new vs closed roles, growth %, 30-day trend, median days-to-fill, function and seniority mix |
| [Hiring Pulse Benchmarks](https://apify.com/agilityy/hiring-pulse-benchmarks) | The engine behind this report: benchmarks by industry, company size and ATS, plus leaderboards, from your own tracked set |
| [Funded & Hiring Leads](https://apify.com/agilityy/funded-and-hiring-leads) | Daily B2B leads from SEC Form D filings: operating companies that just raised money, with a live hiring check |
| [Company Hiring Lookup](https://apify.com/agilityy/company-hiring-lookup) | Give it company names, websites or careers URLs; get open roles by function and seniority, AI/ML roles, remote share |

More Actors from the same team: [apify.com/agilityy](https://apify.com/agilityy).

## How this repository works

- `reports/<YYYY-MM-DD>.md` and `reports/latest.md` are committed by the Hiring Pulse Benchmarks Actor at the end of
  every scheduled Monday run (plain Markdown, no front matter). Nothing else writes them.
- GitHub Pages builds the site with Jekyll from the `main` branch root. `_config.yml`, `_layouts/default.html` and the
  pages `index.md`, `reports/index.md`, `data.md`, `for-data-teams.md`, `methodology.md` are the whole site. Reports
  become pages through `jekyll-optional-front-matter` (a GitHub Pages default), the front page reads `reports/latest.md`
  at build time, and the archive list is generated from the files in `reports/`, so a new report needs no other step.
- `.github/ISSUE_TEMPLATE/data-access-request.yml` is the contact form for the data feed (no e-mail address anywhere).
- `.github/workflows/custom-domain.yml` watches DNS every six hours and switches the site to the custom domain by
  itself (below). It never changes DNS.
- `samples/` holds the free sample CSVs linked from the data-teams page.
- Local preview: `bundle install && bundle exec jekyll serve` (Ruby 3; the `Gemfile` pins the GitHub Pages gem).

## Custom domain: the one record to add

At the registrar or DNS host of `agilityy.com`, add:

| Type | Host / name | Value / target | TTL |
|---|---|---|---|
| CNAME | `hiring` | `agilityy-research.github.io` | default (3600) |

That is the only manual step. Within six hours the workflow sees the record, commits the `CNAME` file (which sets
the custom domain on the Pages site), GitHub issues the certificate, and on a later run the workflow enables
"Enforce HTTPS". The old `github.io` address then redirects to `https://hiring.agilityy.com/` with the path kept, so
every link already published keeps working. Check progress in the repository's Actions tab ("Custom domain") or at
Settings → Pages. Optional hardening: verify the domain for the organisation (Organisation settings → Pages →
Verified domains: a TXT record GitHub names) so nobody else can claim `hiring.agilityy.com` on GitHub Pages.

## Methodology in brief

- **Universe.** Companies with a public job board on Greenhouse, Lever, Ashby or Workable, drawn from accelerator
  lists and public web indexes; industry and size metadata where available.
- **Snapshots.** Every board is read once a day. A role is *opened* when it first appears and *closed* when it
  disappears; days-to-fill is the age of a role at closure. Postings older than a year at closure are excluded
  from days-to-fill as evergreen.
- **Window.** All growth figures compare open roles today with open roles 30 days earlier for the same companies.
- **Segments.** A segment is reported only when it has at least 5 companies.
- **Classification.** Function, seniority and AI/ML tags come from the job title using a fixed, published taxonomy
  (the same one the Actors use), so numbers are comparable week to week.
- **Verification.** The collectors measure fetch rate, day-over-day stability, careers-page agreement and closure
  confirmation every day; thresholds are on the [methodology](methodology.md) page.

## Licence and citation

Reports in this repository are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Quote freely with attribution: *"Agilityy Research, Hiring Pulse, week of YYYY-MM-DD"* and a link to this repository.

Questions, corrections or a custom cut of the data: open an issue here
(data requests: the [Data access request](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml) form).
