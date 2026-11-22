---
title: "Startup hiring benchmarks, every Monday, from 21,000+ job boards"
description: >-
  Where startup hiring accelerates and stalls this week: open roles, movers, days-to-fill, AI/ML and remote share across 21,000+ job boards. Free every Monday.
permalink: /
---
{%- capture nl %}
{% endcapture -%}
{%- capture nl2 %}{{ nl }}{{ nl }}{% endcapture -%}
{%- capture latest_raw %}{% include_relative reports/latest.md %}{% endcapture -%}
{%- assign sections = latest_raw | split: "## " -%}
{%- assign title_line = sections[0] | split: nl | first -%}
{%- assign latest_date = title_line | split: "—" | last | strip -%}
{%- assign coverage_line = sections[0] | remove_first: title_line | strip -%}
{%- assign findings = "" -%}{%- assign charts = "" -%}{%- assign headline = "" -%}
{%- for s in sections -%}
  {%- if s contains "Key findings" and forloop.index0 > 0 and findings == "" -%}{%- assign findings = s | remove_first: "Key findings" -%}
  {%- elsif s contains "This week in charts" and charts == "" -%}{%- assign charts = s | remove_first: "This week in charts" -%}
  {%- elsif s contains "Headline numbers" and headline == "" -%}{%- assign headline = s | remove_first: "Headline numbers" -%}
  {%- endif -%}
{%- endfor -%}
{%- comment -%} Findings come as "- **headline** detail" with an indented "  - *audience*" line; the last paragraph is a coverage note. {%- endcomment -%}
{%- assign items = findings | split: "- **" -%}
{%- assign findings_note = findings | strip | split: nl2 | last | strip -%}
{%- if findings_note contains "- " or findings_note contains "**" -%}{%- assign findings_note = "" -%}{%- endif -%}
{%- assign hero = "" -%}
{%- comment -%} Stat strip from the headline table: value in column 2, change in column 4. {%- endcomment -%}
{%- assign v_companies = "" -%}{%- assign v_open = "" -%}{%- assign d_open = "" -%}{%- assign v_fill = "" -%}{%- assign d_fill = "" -%}{%- assign v_ai = "" -%}{%- assign d_ai = "" -%}{%- assign v_remote = "" -%}{%- assign d_remote = "" -%}
{%- assign hrows = headline | split: nl -%}
{%- for r in hrows -%}
  {%- assign cells = r | split: "|" -%}
  {%- if r contains "| Companies tracked |" -%}{%- assign v_companies = cells[2] | strip -%}
  {%- elsif r contains "| Open roles |" -%}{%- assign v_open = cells[2] | strip -%}{%- assign d_open = cells[4] | strip -%}
  {%- elsif r contains "| Median days-to-fill |" -%}{%- assign v_fill = cells[2] | strip -%}{%- assign d_fill = cells[4] | strip -%}
  {%- elsif r contains "| AI/ML share of open roles |" -%}{%- assign v_ai = cells[2] | strip -%}{%- assign d_ai = cells[4] | strip -%}
  {%- elsif r contains "| Remote roles, share of open roles |" -%}{%- assign v_remote = cells[2] | strip -%}{%- assign d_remote = cells[4] | strip -%}
  {%- endif -%}
{%- endfor -%}

# Where startup hiring is moving this week

{% if items.size > 1 %}
{%- assign first = items[1] | split: nl2 | first -%}
{%- assign hero = first | split: "**" | first %}
<p class="hero">{{ hero }}</p>
{% endif %}
<p class="muted small">Edition of {{ latest_date }}. {{ coverage_line | markdownify | strip_html | strip }} The weekly report is free to quote; the daily data behind it, every company and every role opened or closed, is <a href="{{ '/get-the-data/' | relative_url }}">yours per row, as a feed or through an AI assistant</a>.</p>

{%- if v_open != "" %}
<div class="stats" aria-label="Headline numbers">
<div class="stat"><b>{{ v_open }}</b><span>open roles</span>{% if d_open != "" and d_open != "—" %}<span class="delta">{{ d_open }} vs previous edition</span>{% endif %}</div>
{%- if v_companies != "" %}<div class="stat"><b>{{ v_companies }}</b><span>companies, boards read daily</span></div>{% endif %}
{%- if v_fill != "" and v_fill != "—" %}<div class="stat"><b>{{ v_fill }}</b><span>median days to fill a role</span>{% if d_fill != "" and d_fill != "—" %}<span class="delta">{{ d_fill }}</span>{% endif %}</div>{% endif %}
{%- if v_ai != "" %}<div class="stat"><b>{{ v_ai }}</b><span>of open roles are AI/ML</span>{% if d_ai != "" and d_ai != "—" %}<span class="delta">{{ d_ai }}</span>{% endif %}</div>{% endif %}
{%- if v_remote != "" and v_remote != "—" %}<div class="stat"><b>{{ v_remote }}</b><span>of open roles are remote</span>{% if d_remote != "" and d_remote != "—" %}<span class="delta">{{ d_remote }}</span>{% endif %}</div>{% endif %}
</div>
{%- endif %}

<div class="search" id="company-search" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q">Search a company</label>
<input id="company-q" type="search" autocomplete="off" spellcheck="false" placeholder="Search one of the {{ v_companies | default: site.coverage.companies }} companies: open roles today, change in 30 days, signal">
<ul class="search-results" id="company-results" aria-live="polite"></ul>
</div>
<p class="muted small" id="company-search-note" hidden>Preview tier: one line per company from the latest edition. The roles themselves, the daily history and the opened/closed events are in the <a href="{{ '/get-the-data/' | relative_url }}">feed</a>. A company missing? <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for it</a>.</p>

{%- if site.newsletter_action != "" %}
<div class="signup">
<b>The startup hiring pulse in your inbox, every Monday at 07:00 UTC.</b> Key findings, charts and the movers; no other mail.
<form action="{{ site.newsletter_action }}" method="post" target="_blank">
<input type="email" name="{{ site.newsletter_email_field | default: 'email' }}" placeholder="work e-mail" required>
<button type="submit">Subscribe</button>
<span class="muted small">Prefer a reader? <a href="{{ '/feed.xml' | relative_url }}">Atom feed</a>.</span>
</form>
</div>
{%- endif %}

## What the data says this week

<div class="chips" id="audience-chips" hidden role="group" aria-label="Show the findings for">
<button type="button" data-who="" aria-pressed="true">Everyone</button>
<button type="button" data-who="talent|recruit" aria-pressed="false">Talent teams</button>
<button type="button" data-who="sales|revenue" aria-pressed="false">Sales &amp; revenue</button>
<button type="button" data-who="investor|analyst" aria-pressed="false">Investors &amp; analysts</button>
<button type="button" data-who="employer|compensation" aria-pressed="false">Employer brand</button>
</div>

{% if items.size > 1 %}
<div class="insights">
{%- for item in items offset: 1 %}
{%- assign body = item | split: nl2 | first -%}
{%- assign head = body | split: "**" | first -%}
{%- assign rest = body | remove_first: head | remove_first: "**" -%}
{%- assign who = "" -%}{%- assign detail = rest | strip -%}
{%- if rest contains "- *" -%}{%- assign rp = rest | split: "- *" -%}{%- assign detail = rp[0] | strip -%}{%- assign who = rp[1] | split: "*" | first -%}{%- endif -%}
{%- assign wp = who | split: ": " -%}
<div class="card" data-who="{{ who | downcase | escape }}">
<h3>{{ head | strip }}</h3>
{%- if detail != "" %}<p>{{ detail | markdownify | strip_html }}</p>{% endif %}
{%- if who != "" %}<p class="who">{% if wp.size > 1 %}<b>{{ wp[0] }}:</b> {{ who | remove_first: wp[0] | remove_first: ": " }}{% else %}{{ who }}{% endif %}</p>{% endif %}
</div>
{%- endfor %}
</div>
{% if findings_note != "" %}<p class="muted small">{{ findings_note | markdownify | strip_html }}</p>{% endif %}
{%- else %}
{{ sections[0] | remove_first: title_line | markdownify }}
{%- endif %}

{%- if charts != "" %}
<div class="charts">
{%- assign chart_blocks = charts | split: "![" -%}
{%- for blk in chart_blocks offset: 1 -%}
  {%- assign url = blk | split: "](" | last | split: ")" | first -%}
  {%- assign fname = url | split: "/" | last -%}
  {%- assign rel = "/reports/charts/" | append: fname -%}
  {%- assign on_disk = site.static_files | where: "path", rel | first -%}
  {%- assign caption = blk | split: ")" | last | strip -%}
  {%- if on_disk -%}
  <figure>{% include_relative {{ rel | remove_first: "/" }} %}{% if caption != "" %}<figcaption>{{ caption | markdownify | strip_html }}</figcaption>{% endif %}</figure>
  {%- else -%}
  {{ "![" | append: blk | markdownify }}
  {%- endif -%}
{%- endfor %}
</div>
{%- endif %}
{%- if headline != "" %}
<details><summary>All headline numbers and the change since the previous edition</summary>
{{ headline | markdownify }}
</details>
{%- endif %}
<p><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">How you get the data</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a></p>

## Get the data behind it

<table class="pricing">
<thead><tr><th></th><th>Sales &amp; revenue teams</th><th>Data teams</th><th>Investors &amp; analysts</th></tr></thead>
<tbody>
<tr><td>What you get</td>
<td>Yesterday's signal for every tracked company, one row each: open roles, roles opened and closed, 30-day growth, days-to-fill, a one-word signal; plus every role opened or closed as an event. Filter by vendor, industry, function or signal.</td>
<td>The whole history: daily signals and job events for every company since collection began, with the schema and a free sample to load today.</td>
<td>Daily tracking of the companies you name (a portfolio, a sector, a watch list), SEC Form D funded companies with a live hiring check, and custom cuts of the history.</td></tr>
<tr><td>Delivered as</td>
<td>JSON, CSV or Excel download; REST API with Python and JS clients; schedules to Google Sheets, Slack or a webhook; MCP in Claude, Cursor or Claude Code.</td>
<td>Monthly CSV files, or a Snowflake share refreshed daily.</td>
<td>Same four routes as the feed; custom cuts as CSV or Parquet.</td></tr>
<tr><td>Price</td>
<td><span class="price">$0.01 per company-day</span>; job events $0.004 each.</td>
<td><span class="price">$149 / month</span> or $1,200 / year for the files; <span class="price">$249 / month</span> Snowflake share.</td>
<td><span class="price">$0.025 per company-day</span> on your list; funded leads $0.015 each; custom cuts quoted, often free with attribution for research and press.</td></tr>
<tr><td>Start</td>
<td><a class="btn" href="https://apify.com/agilityy/hiring-signals-feed">Open the feed</a></td>
<td><a class="btn" href="{{ '/for-data-teams/' | relative_url }}">Schema, sample, access</a></td>
<td><a class="btn" href="{{ '/data/' | relative_url }}">Products and prices</a></td></tr>
</tbody>
</table>

<p><a class="btn alt" href="{{ '/samples/daily_signals_sample.csv' | relative_url }}" download>Download a sample CSV: daily signals</a>
<a class="btn alt" href="{{ '/samples/job_events_sample.csv' | relative_url }}" download>Sample CSV: job events</a>
<a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">All six ways to get the data</a></p>

## Why these numbers hold up

- **First-party.** Every company's own job board ({{ site.coverage.vendors }}) is read once a day. A role is counted
  once, from the source, and a closure is observed the day the posting disappears, not inferred from an aggregator.
- **Broad.** {{ site.coverage.companies }} companies since {{ site.coverage.companies_since }}, {{ site.coverage.companies_before }} before that; mostly venture-backed
  technology companies, {{ site.coverage.with_industry }} of them with industry and team size for the segment tables. The exact
  count of the day is in every report.
- **Comparable.** Functions, seniority and the AI/ML flag come from one fixed title taxonomy, so this week's figures
  compare with last week's and with yours.
- **Checked daily.** Fetch rate, day-over-day stability, a careers-page re-count and a re-fetch of closed roles are
  measured every day with alert thresholds. The [methodology]({{ '/methodology/' | relative_url }}) lists them.

## Who it is for

<p class="trust"><span>Launched November 2026, so no customer logos yet. Judge the data itself:</span>
<a href="{{ '/samples/daily_signals_sample.csv' | relative_url }}">the sample</a>
<a href="{{ '/methodology/' | relative_url }}">the method and the daily checks</a>
<a href="https://github.com/agilityy-research/hiring-pulse">the source of every report</a></p>

<div class="grid">
<div class="card"><h3>Talent and recruiting teams</h3>
<p>Which functions are hard to fill and how long roles stay open, by industry and company size. Benchmark your
days-to-fill against companies like yours, and see which competitors are opening or closing teams.</p></div>
<div class="card"><h3>Sales and revenue operations</h3>
<p>A company that just doubled its open roles is buying tools, office space, payroll and insurance. Hiring momentum
per company, refreshed daily, is the earliest public signal of a budget.</p></div>
<div class="card"><h3>Investors and analysts</h3>
<p>Portfolio and sector hiring trends from first-party job-board reads, not aggregator counts: roles opened and
closed, net growth, AI/ML share, remote share, comparable week after week.</p></div>
<div class="card"><h3>Journalists and researchers</h3>
<p>Citable numbers every Monday under CC BY 4.0, with the method published. A custom cut of the history for a story
or a paper is usually free with attribution.</p></div>
</div>

<p class="small muted">Reports are released under CC BY 4.0. Cite as "Agilityy Research, Hiring Pulse, {{ latest_date }}"
with a link to this site. New edition every Monday 07:00 UTC; subscribe to the <a href="{{ '/feed.xml' | relative_url }}">Atom feed</a>.
Source files: <a href="https://github.com/agilityy-research/hiring-pulse">github.com/agilityy-research/hiring-pulse</a>.</p>

<script>
(function () {
  var box = document.getElementById("company-search"), q = document.getElementById("company-q"),
      out = document.getElementById("company-results"), note = document.getElementById("company-search-note");
  if (!box || !q || !out) return;
  box.hidden = false; if (note) note.hidden = false;
  var data = null, loading = null, url = "{{ '/reports/data/companies.json' | relative_url }}";
  function load() {
    if (data || loading) return loading;
    loading = fetch(url, {cache: "force-cache"}).then(function (r) { return r.ok ? r.json() : null; }).then(function (j) {
      data = j && j.companies ? j : {companies: [], windowDays: 30}; return data;
    }).catch(function () { data = {companies: [], windowDays: 30}; return data; });
    return loading;
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]; }); }
  function fmt(n) { return Number(n).toLocaleString("en-US"); }
  function render(term) {
    out.innerHTML = "";
    if (!data || term.length < 2) return;
    var t = term.toLowerCase(), hits = [], rows = data.companies;
    for (var i = 0; i < rows.length && hits.length < 8; i++) { if (String(rows[i][0]).toLowerCase().indexOf(t) !== -1) hits.push(rows[i]); }
    if (!hits.length) { out.innerHTML = '<li><span class="muted">No board with that name among the tracked companies.</span></li>'; return; }
    var d = data.windowDays || 30;
    out.innerHTML = hits.map(function (r) {
      var name = r[0], vendor = r[1], ind = r[2], open = r[3], net = r[4], growth = r[5], sig = r[6], ai = r[7], remote = r[8], fn = r[9];
      var meta = [vendor && vendor.charAt(0).toUpperCase() + vendor.slice(1), ind, fn && ("mostly " + fn)].filter(Boolean).join(" · ");
      var line;
      if (net === null || net === undefined) line = '<span class="muted">' + d + '-day change from the next editions, as its history reaches 14 days</span>';
      else {
        var cls = net > 0 ? "up" : (net < 0 ? "down" : ""), sign = net > 0 ? "+" : "";
        var word = sig === "A" ? "accelerating" : (sig === "C" ? "contracting" : "steady");
        line = '<span class="' + cls + '">' + sign + fmt(net) + " roles in " + d + " days" + (growth === null || growth === undefined ? "" : " (" + (growth > 0 ? "+" : "") + growth + "%)") + "</span> · " + word;
      }
      var extra = [ai != null ? ai + "% AI/ML" : null, remote != null ? remote + "% remote" : null].filter(Boolean).join(" · ");
      return "<li><b>" + esc(name) + "</b><span>" + fmt(open) + " open roles</span>" + line + (meta ? '<span class="muted">' + esc(meta) + "</span>" : "") +
             (extra ? '<span class="muted">' + esc(extra) + "</span>" : "") + ' <a href="{{ '/get-the-data/' | relative_url }}">Which roles? Unlock the feed</a></li>';
    }).join("");
  }
  q.addEventListener("focus", function () { load(); });
  q.addEventListener("input", function () { var v = q.value.trim(); load().then(function () { if (q.value.trim() === v) render(v); }); });
  var chips = document.getElementById("audience-chips"), cards = document.querySelectorAll(".insights .card");
  if (chips && cards.length) {
    chips.hidden = false;
    chips.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      chips.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      var keys = (b.getAttribute("data-who") || "").split("|").filter(Boolean);
      cards.forEach(function (c) {
        var who = (c.getAttribute("data-who") || "").toLowerCase();
        c.classList.toggle("dim", keys.length > 0 && !keys.some(function (k) { return who.indexOf(k) !== -1; }));
      });
    });
  }
})();
</script>
