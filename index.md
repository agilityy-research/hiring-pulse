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
<p class="eyebrow">Weekly edition of {{ latest_date | date: "%-d %B %Y" }}</p>
<h1>Who is hiring, who is cutting, what they pay</h1>
{%- if v_open != "" %}
<p class="hero">{{ v_open }} open roles across {{ v_companies | default: site.coverage.companies }} startups and scale-ups, counted this week from their own job boards.</p>
{%- elsif items.size > 1 %}
{%- assign first = items[1] | split: nl2 | first -%}
{%- assign hero = first | split: "**" | first %}
<p class="hero">{{ hero }}</p>
{%- endif %}
<p class="sub">Read once a day from each company's own job board, never from a job site. Employers with more than 1,000 open roles, staffing agencies and franchises are left out, so the benchmark stays about startups. <a href="{{ '/methodology/' | relative_url }}">How we count</a>.</p>
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read this week's report</a>
<a class="btn alt" href="#{% if site.beta_signup_action != "" %}beta{% else %}data{% endif %}">Get the daily data{% if site.beta_signup_action != "" %} free{% endif %}</a></div>
{%- if v_open != "" %}
<div class="stats" aria-label="Headline numbers">
<div class="stat"><b>{{ v_open }}</b><span>open roles</span>{% if d_open != "" and d_open != "—" %}<span class="delta">{{ d_open }} vs previous edition</span>{% endif %}</div>
{%- if v_companies != "" %}<div class="stat"><b>{{ v_companies }}</b><span>companies tracked</span></div>{% endif %}
{%- if v_fill != "" and v_fill != "—" %}<div class="stat"><b>{{ v_fill }}</b><span>median days a role stays open</span>{% if d_fill != "" and d_fill != "—" %}<span class="delta">{{ d_fill }}</span>{% endif %}</div>{% endif %}
{%- if v_remote != "" and v_remote != "—" %}<div class="stat"><b>{{ v_remote }}</b><span>of open roles flagged remote</span>{% if d_remote != "" and d_remote != "—" %}<span class="delta">{{ d_remote }}</span>{% endif %}</div>{% endif %}
</div>
{%- endif %}
</div></section>

{% include curious-facts.html report_date=latest_date %}

<section class="band tint"><div class="wrap">
<p class="eyebrow">This week</p>
<h2>What the data says this week</h2>
<p class="sub muted">Six findings from the edition of {{ latest_date | date: "%-d %B %Y" }}, each with what it means for your team. The tables behind them are in the full report.</p>
{%- assign labels = "Demand|Momentum|Movers|Time to fill|AI/ML roles|Remote work" | split: "|" -%}
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
<p class="label">{{ labels[forloop.index0] | default: "Finding" }}</p>
<h3>{{ head | strip }}</h3>
{%- if detail != "" %}<p>{{ detail | markdownify | strip_html }}</p>{% endif %}
{%- if who != "" %}{%- assign who_rest = who | remove_first: wp[0] | remove_first: ": " | strip -%}{%- assign who_tag = wp[0] | remove_first: "For " | strip -%}
<p class="who">{% if wp.size > 1 %}<b>{{ who_tag | slice: 0 | upcase }}{{ who_tag | slice: 1, 200 }}</b>{{ who_rest | slice: 0 | upcase }}{{ who_rest | slice: 1, 400 }}{% else %}{{ who }}{% endif %}</p>{% endif %}
</div>
{%- endfor %}
</div>
{% if findings_note != "" %}<p class="muted small" style="margin-top:1rem">{{ findings_note | remove: ", 07:00 UTC" | markdownify | strip_html }}</p>{% endif %}
{%- else %}
{{ sections[0] | remove_first: title_line | markdownify }}
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a></div>
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
<details><summary>All headline numbers, with the change since the previous edition</summary>
{{ headline | split: "Seniority mix of open roles:" | first | markdownify }}
</details>
{%- endif %}
</div></section>
{%- endif %}

{%- assign mk = site.data.markets -%}
{%- if mk and mk.ready %}
{%- assign mkpay = mk.pay.tables | where: "key", "usd-year" | first -%}
<section class="band tint" id="explore"><div class="wrap">
<p class="eyebrow">Explore the data</p>
<h2>Where startups hire, what they pay, what they ask for</h2>
<p class="sub muted">Every open role placed in its city, with its work mode, the salary its posting publishes and the skills its description names, as read on {{ mk.dateText }}.</p>
<div class="dgrid three">
<div class="panel"><h3><a href="{{ '/data/cities/' | relative_url }}">Hiring by city</a></h3><p class="muted">Open roles, {{ mk.coverage.cityPct }}% of roles name a city</p>
<ol class="bars">{% for c in mk.cities limit: 6 %}<li><span class="name">{{ c.label }}</span><span class="track"><span class="fill" style="width:{{ c.barPct }}%"></span></span><span class="val">{{ c.rolesT }}</span></li>{% endfor %}</ol>
<p class="small"><a href="{{ '/data/cities/' | relative_url }}">All {{ mk.cities.size }} cities, by function and work mode</a></p></div>
{%- if mkpay and mkpay.ticks and mkpay.region == "United States" and mkpay.byFunction.size > 1 %}
<div class="panel"><h3><a href="{{ '/data/salaries/' | relative_url }}">Salaries</a></h3><p class="muted">Median salary offered, US roles; bar: typical range</p>
<ol class="bars pay">{% for r in mkpay.byFunction limit: 6 %}{% if r.lowPct %}<li title="{{ r.name }}: median {{ r.medianText }}, typical range {{ r.medianMinText }} to {{ r.medianMaxText }}, top 10% reach {{ r.topP90Text }}; {{ r.nT }} roles"><span class="name">{{ r.name }}</span><span class="range"><span class="band" style="left:{{ r.lowPct }}%;width:{{ r.widthPct }}%"></span><span class="med" style="left:{{ r.medPct }}%"></span></span><span class="val">{{ r.medianText }}</span></li>{% endif %}{% endfor %}</ol>
<p class="small"><a href="{{ '/data/salaries/' | relative_url }}">Salary by level and city</a></p></div>
{%- endif %}
{%- if mk.skills.ready %}
<div class="panel"><h3><a href="{{ '/data/skills/' | relative_url }}">Skills in demand</a></h3><p class="muted">Share of job descriptions naming each</p>
<ol class="bars">{% for k in mk.skills.top limit: 6 %}<li><span class="name">{{ k.name }}</span><span class="track"><span class="fill" style="width:{{ k.barPct }}%"></span></span><span class="val">{{ k.sharePct }}%</span></li>{% endfor %}</ol>
<p class="small"><a href="{{ '/data/skills/' | relative_url }}">Top skills by function</a></p></div>
{%- else %}
<div class="panel"><h3><a href="{{ '/data/cities/#work-mode' | relative_url }}">How roles are offered</a></h3><p class="muted">Among roles that state a work mode</p>
{%- assign wm = mk.workMode.overall %}
<ol class="bars"><li><span class="name">Remote</span><span class="track"><span class="fill" style="width:{{ wm.remote }}%"></span></span><span class="val">{{ wm.remote }}%</span></li><li><span class="name">Hybrid</span><span class="track"><span class="fill" style="width:{{ wm.hybrid }}%"></span></span><span class="val">{{ wm.hybrid }}%</span></li><li><span class="name">On-site</span><span class="track"><span class="fill" style="width:{{ wm.onsite }}%"></span></span><span class="val">{{ wm.onsite }}%</span></li></ol>
<p class="small">Skills from the job descriptions join here once nine in ten descriptions have been read ({{ mk.skills.coveragePct }}% so far).</p></div>
{%- endif %}
</div>
</div></section>
{%- endif %}

<section class="band" id="lookup"><div class="wrap">
<p class="eyebrow">Try the data</p>
<h2>Look up any company in the benchmark</h2>
<p class="sub muted">Its open roles this week, the share of AI/ML and remote roles, and the recent change once it has two weeks of history.</p>
<div class="search" id="company-search" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q">Search a company</label>
<input id="company-q" type="search" autocomplete="off" spellcheck="false" placeholder="Type a company name, e.g. Fivetran">
<ul class="search-results" id="company-results" aria-live="polite"></ul>
</div>
<p class="muted small" id="company-search-note" hidden>One line per company, from this week's edition. The roles themselves and the day-by-day history are in the <a href="#data">daily data</a>. Not finding a company? <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Request it</a>.</p>
<noscript><p class="muted small">The search needs JavaScript; the same preview rows are in <a href="{{ '/reports/data/companies.json' | relative_url }}">reports/data/companies.json</a>.</p></noscript>
</div></section>

<section class="band tint"><div class="wrap">
<p class="eyebrow">Readers</p>
<h2>Who uses it, and for what</h2>
<div class="grid four">
<div class="card"><h3>Sales and revenue teams</h3><p class="muted small">The companies adding open roles fastest, named every morning with the roles they added. A team that is hiring is a team with budget: reach it first.</p></div>
<div class="card"><h3>Talent and recruiting teams</h3><p class="muted small">How long roles stay open by function, industry and company size, and which competitors are opening or closing teams.</p></div>
<div class="card"><h3>Investors and analysts</h3><p class="muted small">Portfolio and sector hiring from each company's own job board: roles opened and closed, net growth, AI/ML share and remote share, week after week.</p></div>
<div class="card"><h3>Journalists and researchers</h3><p class="muted small">Citable numbers every Monday under CC BY 4.0, with the method published. A cut of the history for a story or a paper is usually free with attribution: <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">ask us</a>.</p></div>
</div>
</div></section>

<section class="band" id="data"><div class="wrap">
<p class="eyebrow">The data behind the report</p>
{%- if site.beta_signup_action != "" %}
<h2>The report is free. During the beta, so is the daily data.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day: open roles, roles opened and closed, and whether it is growing or cutting. Until {{ site.beta_end | date: "%-d %B %Y" }}, every company's files arrive free by e-mail each morning. After that they will be $99 a month, and you decide then.</p>
{% include beta-signup.html %}
{%- elsif site.stripe_payment_link != "" %}
<h2>The report is free. The daily data is $99 a month.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day: open roles, roles opened and closed, and whether it is growing or cutting. Hiring Pulse Daily sends you all of it every morning: every company, the latest day plus the 30 before, cancel any time.</p>
<div class="actions"><a class="btn" href="{{ site.stripe_payment_link }}">Subscribe, $99 a month</a></div>
{%- else %}
<h2>The report is free. Ask us for the data behind it.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day: open roles, roles opened and closed, and whether it is growing or cutting. Tell us which companies and days you need and what for, and we will send a cut.</p>
{%- endif %}
<div class="actions"><a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">What you get</a>
<a class="btn alt" href="{{ '/samples/daily_signals_sample.csv' | relative_url }}" download>Free sample file</a></div>
<p class="muted small">Need the whole history in your own systems, or a cut for a story or a paper? <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">Ask us</a>.</p>
</div></section>

<section class="band tint"><div class="wrap">
<p class="eyebrow">Method</p>
<h2>Why these numbers hold up</h2>
<div class="facts">
<div class="card"><h3>Straight from the source</h3><p>Each company's own job board, read once a day; never a job site that copies listings. A role is counted once, and counts as closed the day its posting comes down.</p></div>
<div class="card"><h3>Broad</h3><p>{{ site.coverage.companies }} companies, found by scanning the public boards of six hiring systems: mostly venture-backed technology companies. Large employers, staffing agencies and franchises stay in the daily data but out of the benchmark.</p></div>
<div class="card"><h3>Comparable</h3><p>Every role is sorted by its title into a function, a seniority level and AI/ML or not, with the same rules every week. When a rule changes, the report says so and does not compare the figures it affects.</p></div>
<div class="card"><h3>Checked daily</h3><p>How many boards answered, how much the totals moved, whether a sample of boards matches its careers page, whether closed roles are really gone. <a href="{{ '/methodology/' | relative_url }}">The methodology</a> lists each check and its alert threshold.</p></div>
</div>
</div></section>

<section class="band navy"><div class="wrap">
<p class="eyebrow">Stay current</p>
<h2>A new edition every Monday</h2>
<p class="sub muted">Out before the US workday starts. Free to read and to quote under CC BY 4.0: cite as "Agilityy Research, Hiring Pulse, {{ latest_date | date: "%-d %B %Y" }}" with a link to this site.</p>
{%- if site.newsletter_action != "" %}
<div class="signup">
<b>Get it in your inbox.</b> Key findings, charts and the movers; no other mail.
<form action="{{ site.newsletter_action }}" method="post" target="_blank">
<input type="email" name="{{ site.newsletter_email_field | default: 'email' }}" placeholder="work e-mail" required>
<button type="submit">Subscribe</button>
</form>
</div>
{%- endif %}
{%- if site.beta_signup_action != "" %}
<p class="muted">The data behind it is free by e-mail during the beta: <a href="#beta">get every company's daily files</a>.</p>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/feed.xml' | relative_url }}">Follow in a feed reader</a>
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
             (extra ? '<span class="muted">' + esc(extra) + "</span>" : "") + '</li>';
    }).join("");
  }
  q.addEventListener("focus", function () { load(); });
  q.addEventListener("input", function () { var v = q.value.trim(); load().then(function () { if (q.value.trim() === v) render(v); }); });
})();
</script>
