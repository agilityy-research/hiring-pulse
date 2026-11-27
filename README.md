# Hiring Pulse — weekly startup hiring benchmarks from 21,000+ public job boards

**Site: https://hiring.agilityy.com/** (becomes **https://hiring.agilityy.com** once the DNS
record below exists). **Agilityy Research** reads the public job boards of 21,000+ companies every day (Greenhouse,
Lever, Ashby, SmartRecruiters, Recruitee and Personio boards; 10,000+ companies before 2026-11-22) and publishes a
benchmark report here every Monday at 07:00 UTC.

**This week → [reports/latest.md](reports/latest.md)** · archive in [`reports/`](reports/) (one file per week,
charts in [`reports/charts/`](reports/charts/)) · [Atom feed](https://hiring.agilityy.com/feed.xml)

## What is in each edition

1. **Key findings**: three to five sentences on where hiring moved this week (open roles and their change, the
   biggest movers, days-to-fill, AI/ML share, remote share).
2. **Charts**: open roles by function, the largest movers, and the edition-by-edition trend; SVG files drawn from the
   same numbers as the tables, light and dark mode, no scripts.
3. **Headline numbers** with the change since the previous edition.
4. The full tables: open roles by function (with days-to-fill), industries, leaderboards (largest additions and
   reductions, fastest growing, contracting, fastest to fill, heaviest AI/ML hiring, most remote), largest boards.

Stock figures (open roles, functions, AI/ML share, remote share, seniority) cover every tracked company; flow figures
(growth, roles opened and closed, days-to-fill, movers) cover companies with 14 days of daily history, which is the
whole universe from 2026-12-07. Numbers are first-party daily reads, not aggregator counts, so a role counts once and
a closure is observed rather than inferred. Full method: [methodology](methodology.md).

## Get the data

Every tracked company's daily numbers, free by e-mail during the beta: [get the data](get-the-data.md). Schema and a
free sample: [for data teams](for-data-teams.md). The whole history or a custom cut:
[ask us](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml).

## How this repository works

- `reports/<YYYY-MM-DD>.md`, `reports/latest.md` and `reports/charts/<YYYY-MM-DD>-*.svg` are committed in one commit
  per edition by the scheduled Monday run of the pipeline (plain Markdown, no front matter). Only a scheduled run can
  commit here; test and manual runs keep their report to themselves. Nothing else writes these files.
- `reports/2026-11-20.md` is a one-off baseline study (14 days on 639 Y Combinator companies); `_config.yml` lists
  it under `baseline_reports` so the archive and the feed label it instead of counting it as a weekly edition.
- GitHub Pages builds the site with Jekyll from the `main` branch root. `_config.yml` (also the coverage facts every
  page quotes), `_layouts/default.html` (titles, descriptions, canonical URLs, Open Graph and Twitter cards, JSON-LD:
  Organization, WebSite, Report per edition, Dataset on the data pages, CollectionPage on the archive) and the pages
  `index.md`, `reports/index.md`, `get-the-data.md`, `data.md`, `for-data-teams.md`, `methodology.md`, `feed.xml`
  (Atom), `robots.txt` are the whole site; `jekyll-sitemap` writes `sitemap.xml`. Reports become pages through
  `jekyll-optional-front-matter` (a GitHub Pages default), the front page reads `reports/latest.md` at build time and
  shows its key findings and charts, and the archive list is generated from the files in `reports/`, so a new edition
  needs no other step.
- `.github/ISSUE_TEMPLATE/data-access-request.yml` is the contact form for the data feed (no e-mail address anywhere).
- `.github/workflows/custom-domain.yml` watches DNS every six hours and switches the site to the custom domain by
  itself (below). It never changes DNS.
- `samples/` holds the free sample CSVs; `assets/og-card.png` is the social card.
- Local preview: `bundle install && bundle exec jekyll serve` (Ruby 3; the `Gemfile` pins the GitHub Pages gem).

## Custom domain: the one record to add

At the registrar or DNS host of `agilityy.com`, add:

| Type | Host / name | Value / target | TTL |
|---|---|---|---|
| CNAME | `hiring` | `agilityy-research.github.io` | default (3600) |

That is the only manual step. Within six hours the workflow sees the record and commits the `CNAME` file, which sets
the custom domain on the Pages site; GitHub then issues the certificate and serves the site over HTTPS. The old
`github.io` address redirects to `https://hiring.agilityy.com/` with the path kept, so every link already published
keeps working, and canonical URLs, the sitemap, the feed and the report footers follow the new host at the next build
and the next edition. Check progress in the repository's Actions tab ("Custom domain") or at Settings → Pages.

One setting the workflow's own token is not allowed to change: "Enforce HTTPS" (redirecting `http://` to `https://`;
the site is already served over HTTPS either way). When the certificate is issued the workflow tries, and if GitHub
refuses it fails once and e-mails the owner: either tick **Settings → Pages → Enforce HTTPS** (one click) or add a
repository secret `PAGES_TOKEN` (a fine-grained token for this repository with the permission *Pages: read and
write*) and the next scheduled run does it. Optional hardening: verify the domain for the organisation (Organisation
settings → Pages → Verified domains: a TXT record GitHub names) so nobody else can claim `hiring.agilityy.com` on
GitHub Pages.

## Methodology in brief

- **Universe.** Companies with a public job board on Greenhouse, Lever, Ashby, SmartRecruiters, Recruitee or
  Personio, drawn from accelerator lists and public web indexes, verified against the company name; industry and size
  metadata for around 700 YC-backed companies.
- **Snapshots.** Every board is read once a day. A role is *opened* when it first appears and *closed* when it
  disappears; days-to-fill is the age of a role at closure. Postings older than a year at closure are excluded
  from days-to-fill as evergreen.
- **Window.** All growth figures compare open roles today with open roles 30 days earlier for the same companies.
- **Segments.** A segment is reported only when it has at least 5 companies.
- **Classification.** Function, seniority and AI/ML tags come from the job title using a fixed, published taxonomy
  (the same one the data products use), so numbers are comparable week to week.
- **Verification.** Fetch rate, day-over-day stability, careers-page agreement and closure confirmation are measured
  every day; thresholds are on the [methodology](methodology.md) page.

## Licence and citation

Reports in this repository are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Quote freely with attribution: *"Agilityy Research, Hiring Pulse, week of YYYY-MM-DD"* and a link to this repository.

Questions, corrections or a custom cut of the data: open an issue here
(data requests: the [Data access request](https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml) form).
