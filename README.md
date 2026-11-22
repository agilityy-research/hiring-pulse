# Hiring Pulse — weekly hiring benchmarks across 10,000+ VC-backed companies

**Agilityy Research** tracks the public job boards of more than 10,000 venture-backed companies every day
(Greenhouse, Lever, Ashby and Workable boards) and publishes a benchmark report here every Monday.

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
and closures are observed rather than inferred.

## Get the underlying data

The same pipeline is available as pay-per-event Actors on the Apify Store (no subscription, pay per result):

| Actor | What it does |
|---|---|
| [Hiring Velocity Signals](https://apify.com/agilityy/hiring-velocity-signals) | Track any company's job board over time: new vs closed roles, growth %, 30-day trend, median days-to-fill, function and seniority mix |
| [Hiring Pulse Benchmarks](https://apify.com/agilityy/hiring-pulse-benchmarks) | The engine behind this report: benchmarks by industry, company size and ATS, plus leaderboards, from your own tracked set |
| [Funded & Hiring Leads](https://apify.com/agilityy/funded-and-hiring-leads) | Daily B2B leads from SEC Form D filings: operating companies that just raised money, with a live hiring check |
| [Company Hiring Lookup](https://apify.com/agilityy/company-hiring-lookup) | Give it company names, websites or careers URLs; get open roles by function and seniority, AI/ML roles, remote share |

More Actors from the same team: [apify.com/agilityy](https://apify.com/agilityy).

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

## Licence and citation

Reports in this repository are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Quote freely with attribution: *"Agilityy Research, Hiring Pulse, week of YYYY-MM-DD"* and a link to this repository.

Questions, corrections or a custom cut of the data: open an issue here.
