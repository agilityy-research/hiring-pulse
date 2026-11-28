---
title: "Startup hiring tracker: open roles, salaries and hiring cuts at 21,000+ companies"
description: >-
  Where startup hiring accelerates and stalls this week: open roles, movers, days-to-fill, AI/ML and remote share across 21,000+ job boards. Free every Monday.
permalink: /
jsonld: dataset
dataset_name: "Hiring Pulse: daily startup hiring data from 21,000+ job boards"
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
{%- assign hm = site.data.home -%}
{%- assign words = "|about as many|half|a third|a quarter|a fifth|a sixth|a seventh|an eighth|a ninth|a tenth" | split: "|" -%}
{%- assign ai_agents = nil -%}{%- if mk_ready and mk.skills.ready -%}{%- assign ai_agents = mk.skills.top | where: "name", "AI agents" | first -%}{%- endif -%}

<section class="band navy hero"><div class="wrap">
<p class="eyebrow">Weekly benchmark · edition of {{ latest_date | date: "%-d %B %Y" }}</p>
<h1>Which startups are hiring, which are cutting, and what they pay</h1>
<p class="hero">Measured every day from the job boards of {{ v_companies | default: site.coverage.companies }} startups and scale-ups. Not job sites, not surveys: the companies' own postings.</p>
<div id="vswrap">
<div class="search hero-search" id="company-search" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q">Look up a company</label>
<input id="company-q" type="search" autocomplete="off" spellcheck="false" placeholder="Look up any of the {{ v_companies | default: site.coverage.companies }} companies">
<ul class="search-results" id="company-results" aria-live="polite"></ul>
</div>
<div class="search hero-search vs2" id="company-search-2" hidden>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
<label class="visually-hidden" for="company-q2">Compare with a second company</label>
<input id="company-q2" type="search" autocomplete="off" spellcheck="false" placeholder="…compared with">
<ul class="search-results" id="company-results-2" aria-live="polite"></ul>
</div>
</div>
<p class="pills" id="company-pills" hidden><span>Open roles, {% if win_days != "" %}{{ win_days }}-day {% endif %}change, AI and remote share. Try</span>{% for nm in pills %}<button type="button" data-q="{{ nm | escape }}">{{ nm }}</button>{% endfor %}{% if pills.size > 1 %}<button type="button" class="vs-btn" data-vs="{{ pills[0] | escape }}|{{ pills[1] | escape }}">Compare {{ pills[0] }} with {{ pills[1] }}</button>{% endif %}</p>
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
<p class="eyebrow">Weekly benchmark · edition of {{ latest_date | date: "%-d %B %Y" }}</p>
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
{%- assign ratio_txt = "" -%}
{%- if v_contract != "" and v_accel != "" -%}
{%- assign c_n = v_contract | remove: "%" | plus: 0.0 -%}{%- assign a_n = v_accel | remove: "%" | plus: 0.0 -%}
{%- if a_n > 0 and c_n > 0 -%}
{%- assign ratio = c_n | divided_by: a_n -%}
{%- if ratio >= 2.2 -%}{%- assign ratio_txt = "More than twice as many startups are cutting (" | append: v_contract | append: ") as growing (" | append: v_accel | append: ")" -%}
{%- elsif ratio >= 1.95 -%}{%- assign ratio_txt = "Twice as many startups are cutting (" | append: v_contract | append: ") as growing (" | append: v_accel | append: ")" -%}
{%- elsif ratio >= 1.6 -%}{%- assign ratio_txt = "Nearly twice as many startups are cutting (" | append: v_contract | append: ") as growing (" | append: v_accel | append: ")" -%}
{%- elsif ratio >= 1.0 -%}{%- assign ratio_txt = "More startups are cutting (" | append: v_contract | append: ") than growing (" | append: v_accel | append: ")" -%}
{%- else -%}{%- assign ratio_txt = "More startups are growing (" | append: v_accel | append: ") than cutting (" | append: v_contract | append: ")" -%}{%- endif -%}
{%- endif -%}{%- endif -%}
<p class="take">{% if ratio_txt != "" %}{{ ratio_txt }}{% if v_history != "" %}, among the {{ v_history }} with 14+ days of history{% endif %}.{% else %}{{ heads[2] | default: "Which companies added and cut the most roles" }}{% endif %}</p>
<p class="sub2">One dot per company with 14+ days of daily history: open roles across, on a log scale; change in open roles{% if win_days != "" %} over {{ win_days }} days{% endif %} up and down. Click a dot for the company, or filter.</p>
<p class="chips" id="scatter-filters" hidden><button type="button" data-f="all" aria-pressed="true">All</button><button type="button" data-f="grow" aria-pressed="false">Growing 20%+</button><button type="button" data-f="ai" aria-pressed="false">AI-heavy, 25%+ AI/ML titles, 10+ roles</button><button type="button" data-f="remote" aria-pressed="false">Fully remote, 10+ roles</button></p>
{%- assign mv_rel = "/reports/charts/" | append: latest_date | append: "-movers.svg" -%}
{%- assign mv_on_disk = site.static_files | where: "path", mv_rel | first -%}
<div class="scroll" id="scatter" data-days="{{ win_days }}">{% if mv_on_disk %}{% include_relative {{ mv_rel | remove_first: "/" }} %}{% endif %}</div>
<ul class="search-results" id="scatter-pick"></ul>
{%- if ratio_txt != "" and heads[2] %}<p class="small"><b>{{ heads[2] }}</b></p>{% endif %}
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
{%- assign eng_share_n = eng_share_s | plus: 0.0 -%}
{%- assign above_txt = "" -%}{%- assign frac_txt = "" -%}{%- assign n_above = 0 -%}
{%- for r in ranked -%}
{%- if r.median > eng.median and n_above < 2 -%}
{%- assign key = "|" | append: r.name | append: ":" -%}
{%- if fn_shares contains key -%}
{%- assign sh_n = fn_shares | split: key | last | split: "|" | first | plus: 0.0 -%}
{%- if sh_n > 0 -%}{%- assign q = eng_share_n | divided_by: sh_n | round -%}{%- else -%}{%- assign q = 99 -%}{%- endif -%}
{%- if q > 10 -%}{%- assign w = "under a tenth" -%}{%- elsif q < 1 -%}{%- assign w = "more" -%}{%- else -%}{%- assign w = words[q] -%}{%- endif -%}
{%- if n_above == 1 -%}{%- assign above_txt = above_txt | append: " and " -%}{%- assign frac_txt = frac_txt | append: " and " -%}{%- endif -%}
{%- assign above_txt = above_txt | append: r.name | append: " (" | append: r.medianText | append: ")" -%}{%- assign frac_txt = frac_txt | append: w -%}
{%- assign n_above = n_above | plus: 1 -%}
{%- endif -%}{%- endif -%}
{%- endfor -%}
<p class="take">{% if n_above > 0 %}{{ above_txt }} advertise{% if n_above == 1 %}s{% endif %} more than Engineering ({{ eng.medianText }}), on {{ frac_txt }} of its openings.{% else %}Engineering is both the largest function ({{ eng_share_s }}% of openings) and the best paid ({{ eng.medianText }} median).{% endif %}</p>
<p class="sub2">Share of this week's {{ v_open }} open roles by function, and the median salary among US postings that publish one.</p>
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
{%- assign rs = nil -%}{%- if hm and hm.remoteSplit and hm.remoteSplit.total > 0 -%}{%- assign rs = hm.remoteSplit -%}{%- endif -%}
{%- assign none_b = nil -%}{%- if rs -%}{%- assign none_b = rs.buckets | where: "key", "none" | first -%}{%- endif -%}
<p class="take">{% if v_remote != "" and none_b %}{{ v_remote }} of open roles are remote, yet {{ none_b.sharePct | round }}% of startups with {{ rs.minOpenRoles }}+ openings offer none.{% else %}{{ heads[5] | default: "Remote roles are concentrated in a minority of companies" }}{% endif %}</p>
<p class="sub2">Startups with {{ rs.minOpenRoles | default: 10 }} or more open roles{% if rs %} ({{ rs.totalT | default: rs.total }} this week){% endif %}, by the share of their roles flagged remote. Fully remote means {{ rs.fullyRemotePct | default: 99.5 }}% or more of them, as in the report.</p>
<ol class="bars split" id="remote-split">{% if rs %}{% for b in rs.buckets %}<li><span class="name">{{ b.label }}</span><span class="track"><span class="fill" style="width:{{ b.sharePct }}%"></span></span><span class="val">{{ b.countT | default: b.count }}<small>{{ b.sharePct | round }}% of {{ rs.totalT | default: rs.total }}</small></span></li>{% endfor %}{% endif %}</ol>
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
<p class="take">{{ c0.label }} leads on volume ({{ c0.rolesT }} open roles){% if pmax %}, {{ pmax.name }} on advertised pay ({{ pmax.medianText }} median){% endif %}{% if hmax %}{% if pmax %} and{% else %},{% endif %} {{ hmax.label }} on hybrid ({{ hmax.modes.hybrid }}%){% endif %}, among the ten largest cities.</p>
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

{%- if fn_fill != "" or hm.aiLeaders %}
<div class="cgrid" style="margin-top:1.2rem">
{%- if fn_fill != "" %}
{%- assign fill_pairs = fn_fill | split: "|" -%}
{%- assign f_max = nil -%}{%- assign f_min = nil -%}{%- assign f_top = 0.0 -%}
{%- for pr in fill_pairs -%}{%- assign kv = pr | split: ":" -%}{%- if kv.size == 2 and kv[1] != "—" -%}{%- assign fv = kv[1] | plus: 0.0 -%}
{%- if fv > f_top -%}{%- assign f_top = fv -%}{%- assign f_max = kv -%}{%- endif -%}
{%- if f_min == nil -%}{%- assign f_min = kv -%}{%- else -%}{%- assign mn = f_min[1] | plus: 0.0 -%}{%- if fv < mn -%}{%- assign f_min = kv -%}{%- endif -%}{%- endif -%}
{%- endif -%}{%- endfor -%}
<div class="card ccard" id="chart-fill">
<p class="label">Hiring bottlenecks</p>
{%- if f_max and f_min -%}{%- assign mx = f_max[1] | plus: 0.0 -%}{%- assign mn = f_min[1] | plus: 0.0 -%}{%- assign times = mx | divided_by: mn | times: 10 | round | divided_by: 10.0 -%}
<p class="take">{{ f_max[0] }} roles stay open {{ f_max[1] }} days, {{ f_min[0] }} roles {{ f_min[1] }}: {{ times }} times as long{% if v_fill != "" %}, around a median of {{ v_fill }} for all roles{% endif %}.</p>
{%- else -%}<p class="take">{{ heads[3] | default: "How long roles stay open, by function" }}</p>{%- endif %}
<p class="sub2">Median days a posting stayed up before it closed, by function, among roles that closed in the window at companies with 14+ days of history. Functions with too few closures are left out.</p>
<ol class="bars fill">
{%- assign sorted_fill = "" | split: "" -%}
{%- for pr in fill_pairs -%}{%- assign kv = pr | split: ":" -%}{%- if kv.size == 2 and kv[1] != "—" -%}{%- assign padded = kv[1] | plus: 1000.0 | append: ":" | append: kv[0] -%}{%- assign sorted_fill = sorted_fill | push: padded -%}{%- endif -%}{%- endfor -%}
{%- assign sorted_fill = sorted_fill | sort | reverse -%}
{%- for item in sorted_fill -%}{%- assign kv = item | split: ":" -%}{%- assign fv = kv[0] | plus: 0.0 | minus: 1000.0 -%}{%- assign fw = fv | times: 100 | divided_by: f_top -%}
<li><span class="name">{{ kv[1] }}</span><span class="track"><span class="fill" style="width:{{ fw }}%"></span></span><span class="val">{{ fv | round: 1 | replace: ".0", "" }}<small>days</small></span></li>
{%- endfor %}
</ol>
<p class="small"><a href="{{ '/reports/latest/' | relative_url }}#open-roles-by-function">Days-to-fill by function in the report</a></p>
</div>
{%- endif %}
{%- if hm.aiLeaders and hm.aiLeaders.rows.size > 0 %}
<div class="card ccard" id="chart-ai">
<p class="label">AI-native boards</p>
<p class="take">{{ heads[4] | default: "Where AI/ML roles are most of the hiring" }}</p>
<p class="sub2">Boards with {{ hm.aiLeaders.minOpenRoles }} or more open roles and the highest share of AI/ML titles{% if v_ai != "" %}, against {{ v_ai }} of all open roles{% endif %}.</p>
<ol class="bars leaders">
{%- for r in hm.aiLeaders.rows limit: 5 %}
<li><span class="name">{{ r.company }}<small>{{ r.openRolesT | default: r.openRoles }} open{% if r.industry != "" %} · {{ r.industry }}{% endif %}</small></span><span class="track"><span class="fill" style="width:{{ r.aiSharePct }}%"></span></span><span class="val">{{ r.aiSharePct }}%<small>AI/ML</small></span></li>
{%- endfor %}
{%- if v_ai != "" %}<li class="base"><span class="name">All open roles</span><span class="track"><span class="fill" style="width:{{ v_ai | remove: "%" }}%"></span></span><span class="val">{{ v_ai }}<small>AI/ML</small></span></li>{% endif %}
</ol>
<p class="small"><a href="{{ '/reports/latest/' | relative_url }}">The AI/ML finding in the report</a></p>
</div>
{%- endif %}
</div>
{%- endif %}
<div class="actions"><a class="btn" href="{{ '/reports/latest/' | relative_url }}">Read the full report</a>
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Every edition</a>
<a class="btn alt" href="{{ '/reports/trends/' | relative_url }}">Week by week</a>
<a class="btn alt" href="{{ '/lists/' | relative_url }}">Startup lists</a></div>
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
<p class="sub muted">Behind every number on this page is one line per company per day. Until {{ site.beta_end | date: "%-d %B %Y" }}, every company's files arrive free by e-mail each morning, with the companies that added and cut the most roles. Free for the whole public beta; we will write before it ends.</p>
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
<p><b>Journalists and researchers</b> quote the Monday numbers under CC BY 4.0; a cut of the history for a story or a paper is usually free: <a href="mailto:data@agilityy.com?subject=Hiring%20Pulse%20data%20request">ask us</a>.</p>
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
<a class="btn alt" href="{{ '/reports/' | relative_url }}">Browse every edition</a></div>
</div></section>

<script>
(function () {
  var box = document.getElementById("company-search"), q = document.getElementById("company-q"),
      out = document.getElementById("company-results"), pills = document.getElementById("company-pills"),
      box2 = document.getElementById("company-search-2"), q2 = document.getElementById("company-q2"),
      out2 = document.getElementById("company-results-2"), wrap = document.getElementById("vswrap"), vs = false;
  if (!box || !q || !out) return;
  box.hidden = false; if (pills) pills.hidden = false;
  var data = null, loading = null, url = "{{ '/reports/data/companies.json' | relative_url }}", betaOn = {% if site.beta_signup_action != "" %}true{% else %}false{% endif %};
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest("a.track"); if (!a) return;
    var use = document.querySelector('#beta input[name="{{ site.beta_use_field | default: 'fields[use_case]' }}"]'), mail = document.querySelector('#beta input[type=email]');
    if (use && !use.value.trim()) use.value = "Track " + a.getAttribute("data-company");
    if (mail) setTimeout(function () { mail.focus({preventScroll: true}); }, 400);
  });
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
    var track = betaOn ? '<a class="track" href="#beta" data-company="' + esc(name) + '">' + esc(name) + " is in the daily files: get them free by e-mail \u2192</a>" : "";
    return "<li><b>" + esc(name) + "</b><span>" + fmt(open) + " open roles</span>" + line + (meta ? '<span class="muted">' + esc(meta) + "</span>" : "") +
           (extra ? '<span class="muted">' + esc(extra) + "</span>" : "") + track + '</li>';
  }
  function render(term, target) {
    target = target || out; target.innerHTML = "";
    if (!data || term.length < 2) return;
    var t = term.toLowerCase(), hits = [], rows = data.companies, exact = null;
    for (var i = 0; i < rows.length && hits.length < 8; i++) {
      var nm = String(rows[i][0]).toLowerCase();
      if (nm === t && !exact) exact = rows[i];
      if (nm.indexOf(t) !== -1) hits.push(rows[i]);
    }
    if (!hits.length) { target.innerHTML = '<li><span class="muted">No board with that name among the tracked companies.</span></li>'; return; }
    if (vs) hits = [exact || hits[0]];  // compare mode: one card per side
    target.innerHTML = hits.map(rowHtml).join("");
  }
  function setVs(on) {
    vs = on; if (!box2 || !wrap) return;
    box2.hidden = !on; wrap.classList.toggle("on", on);
    var b = pills && pills.querySelector(".vs-btn"); if (b) b.textContent = on ? "Single lookup" : b.getAttribute("data-label");
    load().then(function () { render(q.value.trim()); if (on) render(q2.value.trim(), out2); else out2.innerHTML = ""; });
  }
  q.addEventListener("focus", function () { load(); });
  q.addEventListener("input", function () { var v = q.value.trim(); load().then(function () { if (q.value.trim() === v) render(v); }); });
  if (q2) q2.addEventListener("input", function () { var v = q2.value.trim(); load().then(function () { if (q2.value.trim() === v) render(v, out2); }); });
  if (pills) pills.addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    if (b.classList.contains("vs-btn")) {
      if (!b.getAttribute("data-label")) b.setAttribute("data-label", b.textContent);
      if (!vs) { var pair = (b.getAttribute("data-vs") || "|").split("|"); q.value = pair[0]; if (q2) q2.value = pair[1]; }
      setVs(!vs); return;
    }
    if (!b.getAttribute("data-q")) return;
    var target = vs && q.value.trim() && !q2.value.trim() ? q2 : q;
    target.value = b.getAttribute("data-q"); target.focus(); load().then(function () { render(target.value.trim(), target === q2 ? out2 : out); });
  });

  // Copy the card as text, or save an SVG chart as a PNG with the site's stamp.
  function stamp() { var e = document.querySelector(".hero .eyebrow"); return "hiring.agilityy.com · " + (e ? e.textContent.replace(/^.*·\s*/, "") : ""); }
  function tools() {
    var canCopyImg = !!(navigator.clipboard && window.ClipboardItem);
    document.querySelectorAll(".ccard, .card.fact").forEach(function (card, i) {
      if (!card.id) card.id = "fact-" + (i + 1);
      var bar = document.createElement("p"); bar.className = "tools";
      bar.innerHTML = '<button type="button" data-act="img">' + (canCopyImg ? "Copy image" : "Save image") + '</button><button type="button" data-act="copy">Copy text</button>';
      var anchor = card.querySelector("p.small:last-of-type, a.more"); card.insertBefore(bar, anchor || null);
      bar.addEventListener("click", function (ev) {
        var b = ev.target.closest("button"); if (!b) return;
        if (b.getAttribute("data-act") === "copy") {
          var clone = card.cloneNode(true); clone.querySelectorAll(".tools, .search-results, .chips, svg").forEach(function (n) { n.remove(); });
          var text = clone.innerText.replace(/\n{3,}/g, "\n\n").trim() + "\n\nSource: " + location.origin + location.pathname + "#" + card.id + " (" + stamp() + ")";
          (navigator.clipboard ? navigator.clipboard.writeText(text) : Promise.reject()).then(function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy text"; }, 1500); }, function () { window.prompt("Copy this text", text); });
        } else {
          b.textContent = "Drawing…";
          cardImage(card).then(function (canvas) {
            return new Promise(function (res) { canvas.toBlob(res, "image/png"); });
          }).then(function (blob) {
            if (canCopyImg) return navigator.clipboard.write([new ClipboardItem({"image/png": blob})]).then(function () { b.textContent = "Copied"; });
            var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "hiring-pulse-" + card.id + ".png"; a.click(); b.textContent = "Saved";
          }).catch(function () { b.textContent = "Could not copy"; }).then(function () { setTimeout(function () { b.textContent = canCopyImg ? "Copy image" : "Save image"; }, 1800); });
        }
      });
    });
  }
  // Draw a card onto a canvas without any library: its text lines, its bars and swatches, and any SVG chart, each at the
  // position it has on screen, then the site's stamp. Buttons, filters, result lists and links are left out.
  function cardImage(card) {
    var k = 2, pad = 16, root = card.getBoundingClientRect(), W = Math.ceil(root.width), H = Math.ceil(root.height) + 26;
    var c = document.createElement("canvas"); c.width = W * k; c.height = H * k;
    var g = c.getContext("2d"); g.scale(k, k);
    var cs0 = getComputedStyle(card), bg = cs0.backgroundColor;
    if (!bg || bg === "rgba(0, 0, 0, 0)") bg = getComputedStyle(document.body).backgroundColor;
    g.fillStyle = bg; g.fillRect(0, 0, W, H);
    var skip = function (el) { return el.closest(".tools, .chips, .search-results, button, a.more, p.small, noscript, .visually-hidden") || getComputedStyle(el).display === "none"; };
    var pending = [], maxY = 0;
    card.querySelectorAll("*").forEach(function (el) {
      if (skip(el)) return;
      var r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
      var x = r.left - root.left, y = r.top - root.top, cs = getComputedStyle(el);
      if (!el.closest("svg") && y + r.height > maxY) maxY = y + r.height;
      if (el.matches("svg.hp")) {
        pending.push(svgImage(el).then(function (img) { g.drawImage(img, x, y, r.width, r.height); }));
        return;
      }
      if (el.closest("svg")) return;
      if (el.matches(".fill, .mix i, .legend i, .band, .med")) {
        var bgc = cs.backgroundColor; if (bgc && bgc !== "rgba(0, 0, 0, 0)") { g.fillStyle = bgc; g.globalAlpha = +cs.opacity || 1; roundRect(g, x, y, r.width, r.height, Math.min(4, r.height / 2)); g.globalAlpha = 1; }
      }
      if (cs.borderBottomWidth !== "0px" && cs.borderBottomStyle !== "none" && el.matches("li, li.hd")) { g.fillStyle = cs.borderBottomColor; g.fillRect(x, y + r.height - 1, r.width, 1); }
    });
    var walker = document.createTreeWalker(card, NodeFilter.SHOW_TEXT), node;
    while ((node = walker.nextNode())) {
      var text = node.nodeValue.replace(/\s+/g, " "); if (!text.trim()) continue;
      var el = node.parentElement; if (skip(el) || el.closest("svg")) continue;
      var cs = getComputedStyle(el), range = document.createRange(); range.selectNodeContents(node);
      var rects = Array.prototype.slice.call(range.getClientRects()).filter(function (q) { return q.width > 0; }); if (!rects.length) continue;
      g.font = cs.fontStyle + " " + cs.fontWeight + " " + cs.fontSize + " " + cs.fontFamily; g.fillStyle = cs.color; g.textBaseline = "middle";
      var clip = el.closest(".name") || el; var cr = clip.getBoundingClientRect();
      g.save(); g.beginPath(); g.rect(cr.left - root.left - 1, cr.top - root.top - 1, cr.width + 2, cr.height + 2); g.clip();
      if (rects.length === 1) { g.textAlign = cs.textAlign === "right" ? "right" : "left"; g.fillText(text.trim(), (cs.textAlign === "right" ? rects[0].right : rects[0].left) - root.left, rects[0].top - root.top + rects[0].height / 2); }
      else {  // wrapped text: refill each line box with as many words as fit
        var words = text.trim().split(" "), li = 0, line = "";
        g.textAlign = "left";
        words.forEach(function (w) {
          var t2 = line ? line + " " + w : w;
          if (g.measureText(t2).width > rects[Math.min(li, rects.length - 1)].width + 2 && line) { g.fillText(line, rects[Math.min(li, rects.length - 1)].left - root.left, rects[Math.min(li, rects.length - 1)].top - root.top + rects[Math.min(li, rects.length - 1)].height / 2); li++; line = w; }
          else line = t2;
        });
        if (line) { var q = rects[Math.min(li, rects.length - 1)]; g.fillText(line, q.left - root.left, q.top - root.top + q.height / 2); }
      }
      g.restore();
    }
    return Promise.all(pending).then(function () {  // crop to the content, then the stamp
      var H2 = Math.min(H, Math.ceil(maxY) + pad + 26), out = document.createElement("canvas"); out.width = W * k; out.height = H2 * k;
      var g2 = out.getContext("2d"); g2.scale(k, k); g2.fillStyle = bg; g2.fillRect(0, 0, W, H2); g2.drawImage(c, 0, 0, W * k, H2 * k, 0, 0, W, H2);
      g2.font = "500 12px -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"; g2.fillStyle = getComputedStyle(document.body).color; g2.globalAlpha = .7; g2.textAlign = "right"; g2.textBaseline = "middle";
      g2.fillText(stamp(), W - pad, H2 - 13); g2.globalAlpha = 1; return out;
    });
  }
  function roundRect(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); g.fill(); }
  function svgImage(svg) {
    var props = ["fill", "stroke", "stroke-width", "opacity", "font-size", "font-family", "font-weight", "text-anchor"];
    var clone = svg.cloneNode(true), src = svg.querySelectorAll("*"), dst = clone.querySelectorAll("*");
    for (var i = 0; i < src.length; i++) { var cs = getComputedStyle(src[i]); props.forEach(function (pn) { var v = cs.getPropertyValue(pn); if (v) dst[i].style.setProperty(pn, v); }); }
    clone.querySelectorAll("title").forEach(function (t) { t.remove(); });
    var r = svg.getBoundingClientRect(); clone.setAttribute("width", Math.round(r.width)); clone.setAttribute("height", Math.round(r.height)); clone.removeAttribute("class");
    var url = URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(clone)], {type: "image/svg+xml;charset=utf-8"}));
    return new Promise(function (res, rej) { var img = new Image(); img.onload = function () { URL.revokeObjectURL(url); res(img); }; img.onerror = rej; img.src = url; });
  }
  window.hpCardImage = cardImage;

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
    var filters = document.getElementById("scatter-filters");
    if (!filters) return;
    var tests = {all: function () { return true; }, grow: function (r) { return r[5] >= 20; }, ai: function (r) { return r[3] >= 10 && r[7] != null && r[7] >= 25; }, remote: function (r) { return r[3] >= 10 && r[8] != null && r[8] >= 99.5; }};
    filters.querySelectorAll("button").forEach(function (b) { var n = rows.filter(tests[b.getAttribute("data-f")]).length; b.textContent += " (" + fmt(n) + ")"; });
    filters.hidden = false;
    filters.addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-f]"); if (!b) return;
      var f = b.getAttribute("data-f"), t = tests[f];
      filters.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      host.querySelectorAll("circle[data-i]").forEach(function (c) { c.classList.toggle("dim", !t(rows[+c.getAttribute("data-i")])); });
      if (!pick) return;
      if (f === "all") { pick.innerHTML = ""; return; }
      var sel = rows.filter(t).sort(function (a, b2) { return b2[4] - a[4]; });
      pick.innerHTML = sel.length ? sel.slice(0, 8).map(rowHtml).join("") : '<li><span class="muted">No company matches this week.</span></li>';
    });
  }

  // Remote, company by company: companies with 10+ open roles by the share of their roles flagged remote.
  function remoteSplit() {
    var host = document.getElementById("remote-split"); if (!host || host.children.length) return;
    var ten = data.companies.filter(function (r) { return r[3] >= 10 && r[8] !== null && r[8] !== undefined; });
    if (!ten.length) { host.innerHTML = ""; return; }
    var b = [["No remote roles", 0], ["Under half remote", 0], ["Half or more remote", 0], ["Fully remote", 0]];
    ten.forEach(function (r) { var v = r[8]; b[v <= 0 ? 0 : v < 50 ? 1 : v < 99.5 ? 2 : 3][1]++; });
    host.innerHTML = b.map(function (x) { var pct = x[1] / ten.length * 100; return '<li><span class="name">' + x[0] + '</span><span class="track"><span class="fill" style="width:' + pct.toFixed(1) + '%"></span></span><span class="val">' + fmt(x[1]) + '<small>' + Math.round(pct) + '% of ' + fmt(ten.length) + '</small></span></li>'; }).join("");
  }
  load().then(function () { try { scatter(); } catch (e) {} try { remoteSplit(); } catch (e) {} try { tools(); } catch (e) {} });
})();
</script>
