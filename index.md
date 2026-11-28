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
{%- comment -%} Extra parses for the home page: accelerating/contracting shares, the function table (share and days-to-fill per
function), and the movers' names (example pills for the lookup). All from the latest edition. {%- endcomment -%}
{%- assign v_accel = "" -%}{%- assign v_contract = "" -%}{%- assign v_history = "" -%}
{%- for r in hrows -%}
  {%- assign cells = r | split: "|" -%}
  {%- if r contains "| Companies accelerating / contracting |" -%}{%- assign ac = cells[2] | split: " / " -%}{%- assign v_accel = ac[0] | strip -%}{%- assign v_contract = ac[1] | strip -%}
  {%- elsif r contains "| Companies with 14+ days of history |" -%}{%- assign v_history = cells[2] | strip -%}
  {%- endif -%}
{%- endfor -%}
{%- assign fn_table = "" -%}
{%- for s in sections -%}{%- assign s_head = s | split: nl | first | strip -%}{%- if s_head == "Open roles by function" and fn_table == "" -%}{%- assign fn_table = s -%}{%- endif -%}{%- endfor -%}
{%- assign fn_shares = "" -%}{%- assign fn_fill = "" -%}
{%- assign fn_rows = fn_table | split: nl -%}
{%- for r in fn_rows -%}
  {%- assign cells = r | split: "|" -%}
  {%- if cells.size > 5 and r contains "%" -%}
    {%- assign fname = cells[1] | strip -%}
    {%- unless fname == "Function" or fname == "Other" -%}
      {%- assign sh_cell = cells[3] | strip | remove: "%" -%}{%- assign fill_cell = cells[5] | strip -%}
      {%- assign fn_shares = fn_shares | append: "|" | append: fname | append: ":" | append: sh_cell -%}
      {%- assign fn_fill = fn_fill | append: "|" | append: fname | append: ":" | append: fill_cell -%}
    {%- endunless -%}
  {%- endif -%}
{%- endfor -%}
{%- assign win_days = "" -%}
{%- if charts contains "net change in open roles over " -%}{%- assign win_days = charts | split: "net change in open roles over " | last | split: " days" | first | strip -%}{%- endif -%}
{%- assign pills = "" | split: "" -%}
{%- assign movers_desc = "" -%}
{%- if charts contains "Largest movers" -%}
  {%- assign movers_desc = charts | split: "Largest movers" | last | split: "](" | first -%}
  {%- assign movers_desc = movers_desc | split: ". " | last -%}
  {%- assign mv = movers_desc | split: "; " -%}
  {%- assign n_up = 0 -%}{%- assign n_down = 0 -%}
  {%- for part in mv -%}
    {%- if part contains " +" and n_up < 2 -%}{%- assign nm = part | split: " +" | first | strip -%}{%- assign pills = pills | push: nm -%}{%- assign n_up = n_up | plus: 1 -%}
    {%- elsif part contains " −" and n_down < 2 -%}{%- assign nm = part | split: " −" | first | strip -%}{%- assign pills = pills | push: nm -%}{%- assign n_down = n_down | plus: 1 -%}
    {%- endif -%}
  {%- endfor -%}
{%- endif -%}
{%- assign mk = site.data.markets -%}
{%- assign mk_ready = false -%}{%- if mk and mk.ready -%}{%- assign mk_ready = true -%}{%- endif -%}
{%- assign usd = nil -%}
{%- if mk_ready -%}{%- assign usd = mk.pay.tables | where: "key", "usd-year" | first -%}{%- unless usd.region == "United States" and usd.ticks -%}{%- assign usd = nil -%}{%- endunless -%}{%- endif -%}
{%- assign ai_agents = nil -%}{%- if mk_ready and mk.skills.ready -%}{%- assign ai_agents = mk.skills.top | where: "name", "AI agents" | first -%}{%- endif -%}

<section class="band navy hero"><div class="wrap">
<p class="eyebrow">Weekly edition of {{ latest_date | date: "%-d %B %Y" }}</p>
<h1>Which startups are hiring, which are cutting, and what they pay</h1>
<p class="hero">Measured every day from the job boards of {{ v_companies | default: site.coverage.companies }} startups and scale-ups. Not job sites, not surveys: the companies' own postings.</p>
<div class="search hero-search" id="company-search" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q">Look up a company</label>
<input id="company-q" type="search" autocomplete="off" spellcheck="false" placeholder="Look up any of the {{ v_companies | default: site.coverage.companies }} companies">
<ul class="search-results" id="company-results" aria-live="polite"></ul>
</div>
<p class="pills" id="company-pills" hidden><span>Open roles, {% if win_days != "" %}{{ win_days }}-day {% endif %}change, AI and remote share. Try</span>{% for nm in pills %}<button type="button" data-q="{{ nm | escape }}">{{ nm }}</button>{% endfor %}</p>
<noscript><p class="sub">The company lookup needs JavaScript. <a href="{{ '/reports/latest/' | relative_url }}">This week's report</a> names the biggest movers.</p></noscript>
{%- if v_open != "" %}
<div class="stats" aria-label="Headline numbers">
<div class="stat"><b>{{ v_open }}</b><span>open roles this week</span>{% if d_open != "" and d_open != "—" %}<span class="delta">{{ d_open }} vs previous edition</span>{% endif %}</div>
{%- if v_contract != "" and v_accel != "" %}<div class="stat"><b>{{ v_contract }} <small>vs</small> {{ v_accel }}</b><span>of companies with 14+ days of history are cutting vs growing</span></div>{% elsif v_companies != "" %}<div class="stat"><b>{{ v_companies }}</b><span>companies tracked</span></div>{% endif %}
{%- if v_fill != "" and v_fill != "—" %}<div class="stat"><b>{{ v_fill }}</b><span>median days a role stays open</span>{% if d_fill != "" and d_fill != "—" %}<span class="delta">{{ d_fill }}</span>{% endif %}</div>{% endif %}
{%- if ai_agents %}<div class="stat"><b>{{ ai_agents.sharePct }}%</b><span>of job descriptions name AI agents</span></div>{% elsif v_remote != "" and v_remote != "—" %}<div class="stat"><b>{{ v_remote }}</b><span>of open roles flagged remote</span></div>{% endif %}
</div>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read this week's report</a>
<a class="btn alt" href="#{% if site.beta_signup_action != "" %}beta{% else %}data{% endif %}">Get the daily data{% if site.beta_signup_action != "" %} free{% endif %}</a></div>
</div></section>

<section class="band" id="this-week"><div class="wrap">
<p class="eyebrow">This week · edition of {{ latest_date | date: "%-d %B %Y" }}</p>
<h2>What moved this week, in charts</h2>
{%- comment -%} Finding headlines by position: 0 demand, 1 momentum, 2 movers, 3 time to fill, 4 AI/ML, 5 remote. {%- endcomment -%}
{%- assign heads = "" | split: "" -%}{%- assign whos = "" | split: "" -%}{%- assign details = "" | split: "" -%}
{%- for item in items offset: 1 -%}
  {%- assign body = item | split: nl2 | first -%}
  {%- assign head = body | split: "**" | first | strip -%}
  {%- assign rest = body | remove_first: head | remove_first: "**" -%}
  {%- assign who = "" -%}{%- assign detail = rest | strip -%}
  {%- if rest contains "- *" -%}{%- assign rp = rest | split: "- *" -%}{%- assign detail = rp[0] | strip -%}{%- assign who = rp[1] | split: "*" | first -%}{%- endif -%}
  {%- assign heads = heads | push: head -%}{%- assign whos = whos | push: who -%}{%- assign details = details | push: detail -%}
{%- endfor -%}
<div class="cgrid">

<div class="card ccard" id="chart-movers">
<p class="label">Growing against shrinking</p>
<p class="take">{{ heads[2] | default: "Which companies added and cut the most roles" }}</p>
<p class="sub2">One dot per company with 14+ days of daily history{% if v_history != "" %} ({{ v_history }} this week){% endif %}: open roles across, on a log scale; change in open roles{% if win_days != "" %} over {{ win_days }} days{% endif %} up and down. Click a dot for the company.</p>
{%- assign mv_rel = "/reports/charts/" | append: latest_date | append: "-movers.svg" -%}
{%- assign mv_on_disk = site.static_files | where: "path", mv_rel | first -%}
<div class="scroll" id="scatter" data-days="{{ win_days }}">{% if mv_on_disk %}{% include_relative {{ mv_rel | remove_first: "/" }} %}{% endif %}</div>
<ul class="search-results" id="scatter-pick"></ul>
<p class="small"><a href="{{ '/reports/latest/' | relative_url }}#largest-movers">The movers table in the report</a></p>
</div>

{%- if usd and fn_shares != "" %}
{%- assign eng = usd.byFunction | where: "name", "Engineering" | first -%}
{%- assign ranked = usd.byFunction | where_exp: "r", "r.name != 'Other'" | sort: "median" | reverse -%}
{%- assign top_fn = ranked | first -%}
{%- assign max_share = 0.0 -%}{%- assign max_med = 0.0 -%}
{%- for r in ranked -%}{%- if r.median > max_med -%}{%- assign max_med = r.median -%}{%- endif -%}{%- endfor -%}
{%- assign fn_pairs = fn_shares | split: "|" -%}
{%- for p in fn_pairs -%}{%- assign kv = p | split: ":" -%}{%- if kv.size == 2 -%}{%- assign sv = kv[1] | plus: 0.0 -%}{%- if sv > max_share -%}{%- assign max_share = sv -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign eng_share_s = fn_shares | split: "|Engineering:" | last | split: "|" | first -%}
{%- assign top_key = "|" | append: top_fn.name | append: ":" -%}
{%- assign top_share_s = fn_shares | split: top_key | last | split: "|" | first -%}
<div class="card ccard" id="chart-pay-demand">
<p class="label">Volume against pay</p>
<p class="take">{% if top_fn.name != "Engineering" %}{{ top_fn.name }} roles are the best paid at {{ top_fn.medianText }}, yet Engineering has {{ eng_share_s }}% of all openings against {{ top_share_s }}% and pays {{ eng.medianText }}.{% else %}Engineering is both the largest function ({{ eng_share_s }}% of openings) and the best paid ({{ eng.medianText }} median).{% endif %}</p>
<p class="sub2">Share of this week's open roles, and the median salary among US postings that publish one.</p>
<ol class="bars two">
<li class="hd" aria-hidden="true"><span></span><span>Share of openings</span><span>Median US salary</span></li>
{%- for r in ranked -%}
{%- assign key = "|" | append: r.name | append: ":" -%}
{%- if fn_shares contains key -%}
{%- assign sh = fn_shares | split: key | last | split: "|" | first -%}
{%- assign shw = sh | plus: 0.0 | times: 100 | divided_by: max_share -%}
{%- assign mw = r.median | times: 100 | divided_by: max_med -%}
<li><span class="name">{{ r.name }}</span><span class="track2"><span class="fill" style="width:{{ shw }}%"></span><em>{{ sh }}%</em></span><span class="track2 pay"><span class="fill" style="width:{{ mw }}%"></span><em>{{ r.medianText }}</em></span></li>
{%- endif -%}
{%- endfor %}
</ol>
<p class="small"><a href="{{ '/data/salaries/' | relative_url }}">Salary by function, level and city</a></p>
</div>
{%- endif %}

<div class="card ccard" id="chart-remote">
<p class="label">Remote, company by company</p>
<p class="take">{{ heads[5] | default: "Remote roles are concentrated in a minority of companies" }}</p>
<p class="sub2">Companies with 10 or more open roles, by the share of their roles flagged remote. Fully remote means 99.5% or more of them, as in the report.</p>
<ol class="bars split" id="remote-split"><li><span class="name muted">Loading…</span></li></ol>
<p class="small"><a href="{{ '/data/cities/#work-mode' | relative_url }}">Remote, hybrid and on-site by city and function</a></p>
</div>

{%- if mk_ready and mk.cities.size > 4 %}
{%- assign c0 = mk.cities[0] -%}
{%- assign hmax = nil -%}{%- assign pmax = nil -%}
{%- for c in mk.cities limit: 10 -%}{%- if c.modes.knownPct >= 40 -%}{%- if hmax == nil or c.modes.hybrid > hmax.modes.hybrid -%}{%- assign hmax = c -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign gbp = mk.pay.tables | where: "key", "gbp-year" | first -%}
{%- assign eur = mk.pay.tables | where: "key", "eur-year" | first -%}
{%- if usd -%}{%- for c in mk.cities limit: 10 -%}{%- assign pc = usd.byCity | where: "name", c.label | first -%}{%- if pc and c.country == "United States" -%}{%- if pmax == nil or pc.median > pmax.median -%}{%- assign pmax = pc -%}{%- endif -%}{%- endif -%}{%- endfor -%}{%- endif -%}
<div class="card ccard" id="chart-cities">
<p class="label">City trade-offs</p>
<p class="take">{{ c0.label }} has the most startup openings{% if hmax or pmax %}; of the ten largest cities, {% endif %}{% if hmax %}{{ hmax.label }} is the most hybrid{% endif %}{% if hmax and pmax %} and {% endif %}{% if pmax %}{{ pmax.name }} advertises the highest median US salary{% endif %}.</p>
<p class="sub2">The ten largest cities: open roles, the remote / hybrid / on-site split of roles that state a work mode, and the median salary among postings that publish one, in that country's currency.</p>
<ol class="bars city">
<li class="hd"><span></span><span>Open roles</span><span></span><span class="mixh">Work mode</span><span>Median pay</span></li>
{%- for c in mk.cities limit: 10 -%}
{%- assign pay = nil -%}
{%- if usd and c.country == "United States" -%}{%- assign pay = usd.byCity | where: "name", c.label | first -%}
{%- elsif gbp and c.country == "United Kingdom" -%}{%- assign pay = gbp.byCity | where: "name", c.label | first -%}
{%- elsif eur -%}{%- assign pay = eur.byCity | where: "name", c.label | first -%}{%- endif -%}
<li><span class="name">{{ c.label }}</span><span class="track"><span class="fill" style="width:{{ c.barPct }}%"></span></span><span class="val">{{ c.rolesT }}</span><span class="mix" title="{{ c.modes.remote }}% remote, {{ c.modes.hybrid }}% hybrid, {{ c.modes.onsite }}% on-site"><i class="r" style="width:{{ c.modes.remote }}%"></i><i class="h" style="width:{{ c.modes.hybrid }}%"></i><i class="o" style="width:{{ c.modes.onsite }}%"></i></span><span class="val pay">{% if pay %}{{ pay.medianText }}{% else %}<span class="muted">—</span>{% endif %}</span></li>
{%- endfor %}
</ol>
<p class="legend"><i class="r"></i>Remote <i class="h"></i>Hybrid <i class="o"></i>On-site</p>
<p class="small"><a href="{{ '/data/cities/' | relative_url }}">All {{ mk.cities.size }} cities</a> · <a href="{{ '/data/salaries/#cities' | relative_url }}">Pay by city and function</a></p>
</div>
{%- endif %}
</div>

{%- if heads.size > 1 %}
<h3 class="sub-h">And in the rest of the edition</h3>
{%- assign labels = "Demand|Momentum|Movers|Time to fill|AI/ML roles|Remote work" | split: "|" -%}
<div class="insights compact">
{%- for head in heads -%}
{%- assign i = forloop.index0 -%}
{%- unless i == 2 or i == 5 -%}
{%- assign who = whos[i] -%}{%- assign wp = who | split: ": " -%}
<div class="card">
<p class="label">{{ labels[i] | default: "Finding" }}</p>
<h3>{{ head }}</h3>
{%- if details[i] != "" %}<p>{{ details[i] | markdownify | strip_html }}</p>{% endif %}
{%- if who != "" %}{%- assign who_rest = who | remove_first: wp[0] | remove_first: ": " | strip -%}{%- assign who_tag = wp[0] | remove_first: "For " | strip -%}
<p class="who">{% if wp.size > 1 %}<b>{{ who_tag | slice: 0 | upcase }}{{ who_tag | slice: 1, 200 }}</b>{{ who_rest | slice: 0 | upcase }}{{ who_rest | slice: 1, 400 }}{% else %}{{ who }}{% endif %}</p>{% endif %}
</div>
{%- endunless -%}
{%- endfor %}
</div>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a>
<a class="btn alt" href="{{ '/reports/trends/' | relative_url }}">Week by week</a></div>
</div></section>

{% include curious-facts.html report_date=latest_date %}

<section class="band" id="explore"><div class="wrap">
<p class="eyebrow">Go deeper</p>
<h2>Salaries, cities, skills, and every company's daily numbers</h2>
<div class="hub four">
<a class="card hub-card" href="{{ '/data/salaries/' | relative_url }}">
<span class="k">Salaries</span>
{%- if usd and usd.all.medianMaxText %}<b class="n">{{ usd.all.medianText }}</b><p>Median yearly salary offered across {{ usd.all.nT }} distinct US roles that publish one; one in ten tops out at {{ usd.all.topP90Text }} or more.</p>{% else %}<p>The salary ranges startups publish, by function, level and city.</p>{% endif %}
<span class="more">By function, level and city</span></a>
<a class="card hub-card" href="{{ '/data/cities/' | relative_url }}">
<span class="k">Hiring by city</span>
{%- if mk_ready and mk.cities.size > 0 %}<b class="n">{{ mk.cities[0].rolesT }}</b><p>Open startup roles in {{ mk.cities[0].label }}, the largest market, at {{ mk.cities[0].companiesT }} companies.</p>{% else %}<p>Where startups hire, and how.</p>{% endif %}
<span class="more">Top cities, roles and work mode</span></a>
<a class="card hub-card" href="{{ '/data/skills/' | relative_url }}">
<span class="k">Skills in demand</span>
{%- if mk_ready and mk.skills.ready and mk.skills.top.size > 0 %}{%- assign sql = mk.skills.top | where: "name", "SQL" | first -%}<b class="n">{{ mk.skills.top[0].sharePct }}%</b><p>of job descriptions name {{ mk.skills.top[0].name }}, the most requested skill.{% if ai_agents and sql %} AI agents are already at {{ ai_agents.sharePct }}%{% if ai_agents.sharePct >= sql.sharePct %}, level with SQL{% else %}, against SQL's {{ sql.sharePct }}%{% endif %}.{% endif %}</p>{% elsif mk_ready %}<b class="n">{{ mk.skills.coveragePct }}%</b><p>of job descriptions read so far. The ranking appears once nine in ten have been read.</p>{% else %}<p>The tools, languages and certifications job descriptions ask for.</p>{% endif %}
<span class="more">Tools, languages and certifications</span></a>
<a class="card hub-card" href="{{ '/get-the-data/' | relative_url }}{% if site.beta_signup_action != "" %}#beta{% endif %}">
<span class="k">The daily data</span>
<b class="n">{{ v_companies | default: site.coverage.companies }}</b><p>companies, one line each, every day: open roles, roles opened and closed, growing or cutting.{% if site.beta_signup_action != "" %} Free by e-mail until {{ site.beta_end | date: "%-d %B %Y" }}.{% endif %}</p>
<span class="more">{% if site.beta_signup_action != "" %}Sign up free{% else %}What you get{% endif %}</span></a>
</div>
</div></section>

<section class="band tint" id="data"><div class="wrap">
<p class="eyebrow">The data behind the report</p>
{%- if site.beta_signup_action != "" %}
<h2>The report is free. During the beta, so is the daily data.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day. Until {{ site.beta_end | date: "%-d %B %Y" }}, every company's files arrive free by e-mail each morning, with the companies that added and cut the most roles. After that they will be $99 a month, and you decide then.</p>
{% include beta-signup.html %}
{%- elsif site.stripe_payment_link != "" %}
<h2>The report is free. The daily data is $99 a month.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day: open roles, roles opened and closed, and whether it is growing or cutting. Hiring Pulse Daily sends you all of it every morning: every company, the latest day plus the 30 before, cancel any time.</p>
<div class="actions"><a class="btn" href="{{ site.stripe_payment_link }}">Subscribe, $99 a month</a></div>
{%- else %}
<h2>The report is free. Ask us for the data behind it.</h2>
<p class="sub muted">Behind every number on this page is one line per company per day: open roles, roles opened and closed, and whether it is growing or cutting. Tell us which companies and days you need and what for, and we will send a cut.</p>
{%- endif %}
<div class="uses">
<p><b>Sales and revenue teams</b> see which companies are adding roles fastest, named every morning: a team that is hiring has budget.</p>
<p><b>Talent teams</b> benchmark how long roles stay open by function, industry and company size, and watch competitors open or close teams.</p>
<p><b>Investors and analysts</b> read portfolio and sector hiring from each company's own board, week after week.</p>
<p><b>Journalists and researchers</b> quote the Monday numbers under CC BY 4.0; a cut of the history for a story or a paper is usually free: <a href="https://github.com/agilityy-research/hiring-pulse/issues/new?template=data-access-request.yml">ask us</a>.</p>
</div>
<div class="actions"><a class="btn alt" href="{{ '/get-the-data/' | relative_url }}">What you get</a>
<a class="btn alt" href="{{ '/samples/daily_signals_sample.csv' | relative_url }}" download>Free sample file</a>
<a class="btn alt" href="{{ '/for-data-teams/' | relative_url }}">For data teams</a></div>
</div></section>

<section class="band navy"><div class="wrap">
<p class="eyebrow">Every Monday</p>
<h2>A new edition before the US workday starts</h2>
<p class="sub muted">Free to read and to quote under CC BY 4.0: cite as "Agilityy Research, Hiring Pulse, {{ latest_date | date: "%-d %B %Y" }}" with a link to this site.</p>
<p class="sub muted">Why the numbers hold up: each company's own job board, read once a day; a role counted once and closed the day its posting comes down; the same title rules every week; four quality checks every morning. <a href="{{ '/methodology/' | relative_url }}">The methodology</a> has every definition and threshold.</p>
{%- if site.newsletter_action != "" %}
<div class="signup">
<b>Get it in your inbox.</b> Key findings, charts and the movers; no other mail.
<form action="{{ site.newsletter_action }}" method="post" target="_blank">
<input type="email" name="{{ site.newsletter_email_field | default: 'email' }}" placeholder="work e-mail" required>
<button type="submit">Subscribe</button>
</form>
</div>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/feed.xml' | relative_url }}">Follow in a feed reader</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Browse every edition</a>
<a class="btn alt" href="https://github.com/agilityy-research/hiring-pulse">Source on GitHub</a></div>
</div></section>

<script>
(function () {
  var box = document.getElementById("company-search"), q = document.getElementById("company-q"),
      out = document.getElementById("company-results"), pills = document.getElementById("company-pills");
  if (!box || !q || !out) return;
  box.hidden = false; if (pills) pills.hidden = false;
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
  var pageDays = +((document.getElementById("scatter") || {getAttribute: function () { return 0; }}).getAttribute("data-days")) || 0;
  function rowHtml(r) {
    var d = pageDays || data.windowDays || 30;
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
  }
  function render(term) {
    out.innerHTML = "";
    if (!data || term.length < 2) return;
    var t = term.toLowerCase(), hits = [], rows = data.companies;
    for (var i = 0; i < rows.length && hits.length < 8; i++) { if (String(rows[i][0]).toLowerCase().indexOf(t) !== -1) hits.push(rows[i]); }
    if (!hits.length) { out.innerHTML = '<li><span class="muted">No board with that name among the tracked companies.</span></li>'; return; }
    out.innerHTML = hits.map(rowHtml).join("");
  }
  q.addEventListener("focus", function () { load(); });
  q.addEventListener("input", function () { var v = q.value.trim(); load().then(function () { if (q.value.trim() === v) render(v); }); });
  if (pills) pills.addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-q]"); if (!b) return;
    q.value = b.getAttribute("data-q"); q.focus(); load().then(function () { render(q.value.trim()); });
  });

  // Growing against shrinking: every company with enough history, open roles across (log scale), change up and down.
  function scatter() {
    var host = document.getElementById("scatter"), pick = document.getElementById("scatter-pick");
    if (!host) return;
    var d = +host.getAttribute("data-days") || data.windowDays || 30;
    var hist = data.companies.filter(function (r) { return r[4] !== null && r[4] !== undefined; });
    var rows = hist.filter(function (r) { return r[5] !== null && r[5] !== undefined && r[3] > 0; }), gone = hist.length - rows.length;
    if (rows.length < 20) return;
    var W = 720, H = 380, L = 52, R = 18, T = 26, B = 44, lim = 100;
    var xs = rows.map(function (r) { return r[3]; }), xmin = Math.max(1, Math.min.apply(null, xs)), xmax = Math.max.apply(null, xs);
    var lx0 = Math.log10(xmin), lx1 = Math.log10(xmax);
    var ymax = 0; rows.forEach(function (r) { ymax = Math.max(ymax, Math.min(lim, Math.abs(r[5]))); }); ymax = Math.max(20, Math.ceil(ymax / 10) * 10);
    var clipped = rows.filter(function (r) { return Math.abs(r[5]) > lim; }).length;
    function X(v) { return L + (Math.log10(v) - lx0) / (lx1 - lx0 || 1) * (W - L - R); }
    function Y(v) { v = Math.max(-lim, Math.min(lim, v)); return T + (ymax - v) / (2 * ymax) * (H - T - B); }
    var s = '<svg class="hp sc" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Companies by open roles and ' + d + '-day change">';
    var ticks = [1, 3, 10, 30, 100, 300, 1000, 3000].filter(function (v) { return v >= xmin && v <= xmax; });
    ticks.forEach(function (v) { s += '<line x1="' + X(v) + '" x2="' + X(v) + '" y1="' + T + '" y2="' + (H - B) + '" class="g"/><text x="' + X(v) + '" y="' + (H - B + 16) + '" text-anchor="middle" class="m s">' + fmt(v) + '</text>'; });
    for (var yv = -ymax; yv <= ymax; yv += ymax / 2) { s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + Y(yv) + '" y2="' + Y(yv) + '" class="g' + (yv === 0 ? ' z' : '') + '"/><text x="' + (L - 6) + '" y="' + (Y(yv) + 4) + '" text-anchor="end" class="m s">' + (yv > 0 ? "+" : "") + yv + '%</text>'; }
    s += '<text x="' + ((L + W - R) / 2) + '" y="' + (H - 6) + '" text-anchor="middle" class="m c">Open roles today (log scale)</text>';
    s += '<text x="12" y="' + ((T + H - B) / 2) + '" text-anchor="middle" class="m c" transform="rotate(-90 12 ' + ((T + H - B) / 2) + ')">Change in open roles, ' + d + ' days</text>';
    var byNet = rows.slice().sort(function (a, b) { return b[4] - a[4]; });
    var label = {}; byNet.slice(0, 3).concat(byNet.slice(-3)).forEach(function (r) { label[r[0]] = true; });
    rows.forEach(function (r, i) {
      var cls = r[6] === "A" ? "p" : (r[6] === "C" ? "n" : "s");
      s += '<circle class="d ' + cls + '" data-i="' + i + '" cx="' + X(r[3]).toFixed(1) + '" cy="' + Y(r[5]).toFixed(1) + '" r="4.2"><title>' + esc(r[0]) + ': ' + fmt(r[3]) + ' open, ' + (r[4] > 0 ? '+' : '') + fmt(r[4]) + ' (' + (r[5] > 0 ? '+' : '') + r[5] + '%) in ' + d + ' days</title></circle>';
    });
    var k = 0;
    var placed = [];
    rows.forEach(function (r) {
      if (!label[r[0]]) return;
      var x = X(r[3]), y = Y(r[5]), left = x > W * 0.6, ty = y - 7;
      for (var tries = 0; tries < 6; tries++) { var clash = placed.some(function (q) { return Math.abs(q[1] - ty) < 12 && Math.abs(q[0] - x) < 110; }); if (!clash) break; ty += 13; }
      placed.push([x, ty]);
      s += '<text class="t c" x="' + (left ? x - 7 : x + 7) + '" y="' + ty.toFixed(1) + '" text-anchor="' + (left ? 'end' : 'start') + '">' + esc(r[0]) + '</text>';
    });
    s += '</svg>';
    host.innerHTML = s;
    var note = document.createElement("p"); note.className = "legend";
    note.innerHTML = '<span><i class="p"></i>Accelerating</span><span><i class="n"></i>Contracting</span><span><i class="sdot"></i>Steady or flat</span><span class="all">' + fmt(rows.length) + ' of ' + fmt(hist.length) + ' companies drawn' + (gone ? '; ' + gone + ' with no open roles left today cannot sit on a log scale' : '') + (clipped ? '; ' + clipped + ' beyond ±' + lim + '% drawn at the edge' : '') + '.</span>';
    host.parentNode.insertBefore(note, host.nextSibling);
    host.addEventListener("click", function (ev) { var c = ev.target.closest("circle[data-i]"); if (!c || !pick) return; pick.innerHTML = rowHtml(rows[+c.getAttribute("data-i")]); });
  }

  // Remote, company by company: companies with 10+ open roles by the share of their roles flagged remote.
  function remoteSplit() {
    var host = document.getElementById("remote-split"); if (!host) return;
    var ten = data.companies.filter(function (r) { return r[3] >= 10 && r[8] !== null && r[8] !== undefined; });
    if (!ten.length) { host.innerHTML = ""; return; }
    var b = [["No remote roles", 0], ["Under half remote", 0], ["Half or more remote", 0], ["Fully remote", 0]];
    ten.forEach(function (r) { var v = r[8]; b[v <= 0 ? 0 : v < 50 ? 1 : v < 99.5 ? 2 : 3][1]++; });
    host.innerHTML = b.map(function (x) { var pct = x[1] / ten.length * 100; return '<li><span class="name">' + x[0] + '</span><span class="track"><span class="fill" style="width:' + pct.toFixed(1) + '%"></span></span><span class="val">' + fmt(x[1]) + '<small>' + Math.round(pct) + '% of ' + fmt(ten.length) + '</small></span></li>'; }).join("");
  }
  load().then(function () { try { scatter(); } catch (e) {} try { remoteSplit(); } catch (e) {} });
})();
</script>
