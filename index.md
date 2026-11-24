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

<section class="band navy hero"><div class="wrap">
<p class="eyebrow">Weekly startup hiring benchmarks · Edition {{ latest_date }}</p>
<h1>Where startup hiring is moving this week</h1>
{%- if v_open != "" %}
<p class="hero">{{ v_open }} open roles at {{ v_companies | default: site.coverage.companies }} startups, counted from their own job boards every day.</p>
{%- elsif items.size > 1 %}
{%- assign first = items[1] | split: nl2 | first -%}
{%- assign hero = first | split: "**" | first %}
<p class="hero">{{ hero }}</p>
{%- endif %}
<p class="sub muted">Free report every Monday. The daily data behind it is for sale.</p>
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read this week's report</a>
<a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">How to buy</a></div>
{%- if v_open != "" %}
<div class="stats" aria-label="Headline numbers">
<div class="stat"><b>{{ v_open }}</b><span>open roles</span>{% if d_open != "" and d_open != "—" %}<span class="delta">{{ d_open }} vs previous edition</span>{% endif %}</div>
{%- if v_companies != "" %}<div class="stat"><b>{{ v_companies }}</b><span>companies, boards read daily</span></div>{% endif %}
{%- if v_fill != "" and v_fill != "—" %}<div class="stat"><b>{{ v_fill }}</b><span>median days a role stays posted</span>{% if d_fill != "" and d_fill != "—" %}<span class="delta">{{ d_fill }}</span>{% endif %}</div>{% endif %}
{%- if v_ai != "" %}<div class="stat"><b>{{ v_ai }}</b><span>of open roles are AI/ML</span>{% if d_ai != "" and d_ai != "—" %}<span class="delta">{{ d_ai }}</span>{% endif %}</div>{% endif %}
{%- if v_remote != "" and v_remote != "—" %}<div class="stat"><b>{{ v_remote }}</b><span>of open roles are remote</span>{% if d_remote != "" and d_remote != "—" %}<span class="delta">{{ d_remote }}</span>{% endif %}</div>{% endif %}
</div>
{%- endif %}
</div></section>

<section class="band" id="lookup"><div class="wrap">
<p class="eyebrow">Try the data</p>
<h2>Look up any of the {{ v_companies | default: site.coverage.companies }} companies</h2>
<div class="search" id="company-search" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q">Search a company</label>
<input id="company-q" type="search" autocomplete="off" spellcheck="false" placeholder="Type a company name, e.g. Fivetran">
<ul class="search-results" id="company-results" aria-live="polite"></ul>
</div>
<p class="muted small" id="company-search-note" hidden>One line per company from this week's edition. The roles, the daily history and every opened or closed event are in the <a href="{{ '/get-the-data/' | relative_url }}">feed</a>. Company missing? <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask for it</a>.</p>
<noscript><p class="muted small">The search needs JavaScript; the same preview rows are in <a href="{{ '/reports/data/companies.json' | relative_url }}">reports/data/companies.json</a>.</p></noscript>
</div></section>

<section class="band tint"><div class="wrap">
<p class="eyebrow">Key findings</p>
<h2>What the data says this week</h2>
<div class="chips" id="audience-chips" hidden role="group" aria-label="Show the findings for">
<button type="button" data-who="" aria-pressed="true">Everyone</button>
<button type="button" data-who="talent|recruit" aria-pressed="false">Talent teams</button>
<button type="button" data-who="sales|revenue" aria-pressed="false">Sales &amp; revenue</button>
<button type="button" data-who="investor|analyst" aria-pressed="false">Investors &amp; analysts</button>
<button type="button" data-who="employer|compensation" aria-pressed="false">Employer brand</button>
</div>
{%- if items.size > 1 %}
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
{%- if who != "" %}{%- assign who_rest = who | remove_first: wp[0] | remove_first: ": " | strip -%}{%- assign who_tag = wp[0] | remove_first: "For " | strip -%}
<p class="who">{% if wp.size > 1 %}<b>{{ who_tag | slice: 0 | upcase }}{{ who_tag | slice: 1, 200 }}</b>{{ who_rest | slice: 0 | upcase }}{{ who_rest | slice: 1, 400 }}{% else %}{{ who }}{% endif %}</p>{% endif %}
</div>
{%- endfor %}
</div>
{% if findings_note != "" %}<p class="muted small" style="margin-top:1rem">{{ findings_note | markdownify | strip_html }}</p>{% endif %}
{%- else %}
{{ sections[0] | remove_first: title_line | markdownify }}
{%- endif %}
</div></section>

{%- if charts != "" %}
<section class="band"><div class="wrap">
<p class="eyebrow">Charts</p>
<h2>This week in charts</h2>
<div class="charts">
{%- assign chart_blocks = charts | split: "![" -%}
{%- for blk in chart_blocks offset: 1 -%}
  {%- assign url = blk | split: "](" | last | split: ")" | first -%}
  {%- assign fname = url | split: "/" | last -%}
  {%- assign rel = "/reports/charts/" | append: fname -%}
  {%- assign on_disk = site.static_files | where: "path", rel | first -%}
  {%- assign caption = blk | split: ")" | last | strip -%}
  {%- if on_disk -%}
  <figure><div class="scroll">{% include_relative {{ rel | remove_first: "/" }} %}</div>{% if caption != "" %}<figcaption>{{ caption | markdownify | strip_html | strip }}</figcaption>{% endif %}</figure>
  {%- else -%}
  <figure>{{ "![" | append: blk | markdownify }}</figure>
  {%- endif -%}
{%- endfor %}
</div>
{%- if headline != "" %}
<details><summary>All headline numbers and the change since the previous edition</summary>
{{ headline | markdownify }}
</details>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a></div>
</div></section>
{%- endif %}

<section class="band tint" id="data"><div class="wrap">
<p class="eyebrow">Get the data behind it</p>
<h2>Three ways to buy</h2>
<div class="plans">
<div class="card plan"><div class="for">Sales &amp; revenue teams</div><p class="price">$0.01</p><p class="per">per company and day · job events $0.004 each</p>
<ul><li>Yesterday's signal for every tracked company: open roles, opened and closed, 30-day growth, days-to-fill, a one-word signal.</li><li>Every role opened or closed as an event, with title, function, location and URL.</li><li>JSON, CSV or Excel download; REST API; schedules to Google Sheets, Slack or a webhook; MCP in Claude or Cursor.</li></ul>
<a class="btn" href="https://apify.com/agilityy/hiring-signals-feed">Open the feed</a></div>
<div class="card plan"><div class="for">Data teams</div><p class="price">$149 <span class="per" style="display:inline;font-size:1rem">/ month</span></p><p class="per">or $1,200 a year for the files · Snowflake share $249 / month</p>
<ul><li>The whole history: daily signals and job events for every company since collection began.</li><li>Monthly CSV files, or a Snowflake share refreshed daily.</li><li>Published schema and a free sample to load today.</li></ul>
<a class="btn" href="{{ '/for-data-teams/' | relative_url }}">Schema, sample, access</a></div>
<div class="card plan"><div class="for">Investors &amp; analysts</div><p class="price">$0.025</p><p class="per">per company and day on your own list · funded leads $0.015 each</p>
<ul><li>Daily tracking of the companies you name: a portfolio, a sector, a watch list.</li><li>SEC Form D funded companies with a live hiring check.</li><li>Custom cuts of the history, often free with attribution for research and press.</li></ul>
<a class="btn" href="{{ '/data/' | relative_url }}">Products and prices</a></div>
</div>
<div class="actions"><a class="btn alt" href="{{ '/samples/daily_signals_sample.csv' | relative_url }}" download>Download a sample CSV: daily signals</a>
<a class="btn alt" href="{{ '/samples/job_events_sample.csv' | relative_url }}" download>Sample CSV: job events</a>
<a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">How to buy: all six routes</a></div>
</div></section>

<section class="band"><div class="wrap">
<p class="eyebrow">Method</p>
<h2>Why these numbers hold up</h2>
<div class="facts">
<div class="card"><h3>First-party</h3><p>Every company's own job board ({{ site.coverage.vendors }}) is read once a day. A role is counted once, from the source; a closure is observed the day the posting disappears.</p></div>
<div class="card"><h3>Broad</h3><p>{{ site.coverage.companies }} companies, mostly venture-backed technology companies; {{ site.coverage.with_industry }} of them with industry and team size for the segment tables. The exact count of the day is in every report.</p></div>
<div class="card"><h3>Comparable</h3><p>Functions, seniority and the AI/ML flag come from one fixed title taxonomy, so this week's figures compare with last week's and with yours.</p></div>
<div class="card"><h3>Checked daily</h3><p>Fetch rate, day-over-day stability, a careers-page re-count and a re-fetch of closed roles are measured every day with alert thresholds. <a href="{{ '/methodology/' | relative_url }}">The methodology</a> lists them.</p></div>
</div>
<p class="muted small" style="margin-top:1rem">Launched November 2026, so no customer logos yet. Judge the data itself: <a href="{{ '/samples/daily_signals_sample.csv' | relative_url }}">the sample</a>, <a href="{{ '/methodology/' | relative_url }}">the method</a>, <a href="https://github.com/agilityy-research/hiring-pulse">the source of every report</a>.</p>
</div></section>

<section class="band tint"><div class="wrap">
<p class="eyebrow">Readers</p>
<h2>Who uses it, and for what</h2>
<div class="grid four">
<div class="card"><h3>Talent and recruiting teams</h3><p class="muted small">Which functions are hard to fill and how long roles stay open, by industry and company size; which competitors are opening or closing teams.</p></div>
<div class="card"><h3>Sales and revenue operations</h3><p class="muted small">A company that just doubled its open roles is buying tools, office space, payroll and insurance. Hiring momentum per company is the earliest public budget signal.</p></div>
<div class="card"><h3>Investors and analysts</h3><p class="muted small">Portfolio and sector hiring trends from first-party reads, not aggregator counts: roles opened and closed, net growth, AI/ML share, remote share, week after week.</p></div>
<div class="card"><h3>Journalists and researchers</h3><p class="muted small">Citable numbers every Monday under CC BY 4.0, with the method published. A custom cut of the history for a story or a paper is usually free with attribution.</p></div>
</div>
</div></section>

<section class="band navy"><div class="wrap">
<p class="eyebrow">Stay current</p>
<h2>A new edition every Monday at 07:00 UTC</h2>
<p class="sub muted">Free to quote under CC BY 4.0: cite as "Agilityy Research, Hiring Pulse, {{ latest_date }}" with a link to this site.</p>
{%- if site.newsletter_action != "" %}
<div class="signup">
<b>Get it in your inbox.</b> Key findings, charts and the movers; no other mail.
<form action="{{ site.newsletter_action }}" method="post" target="_blank">
<input type="email" name="{{ site.newsletter_email_field | default: 'email' }}" placeholder="work e-mail" required>
<button type="submit">Subscribe</button>
</form>
</div>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/feed.xml' | relative_url }}">Subscribe with the Atom feed</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Browse every edition</a>
<a class="btn alt" href="https://github.com/agilityy-research/hiring-pulse">Source on GitHub</a></div>
</div></section>

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
