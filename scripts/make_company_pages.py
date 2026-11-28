#!/usr/bin/env python3
"""Writes one static page per tracked company into the built site, plus the Companies A–Z directory and their sitemap
entries. Runs after `jekyll build`, in the Pages workflow (.github/workflows/pages.yml); the pages are generated at
deploy time and never committed. Standard library only:

    python3 scripts/make_company_pages.py [_site]

Inputs, all in the built site: reports/data/companies.json (one row per company, written by the weekly pipeline),
_data/home.json (the edition's window in days, read from the source tree), and company/_template/index.html, the shell
Jekyll built from company/template-shell.html with @@ markers where the title, description and body go. Every figure on a
page comes from the company's own row; the benchmark line is recomputed from the same file with the formulas the
weekly report uses (AI/ML and remote roles summed from each board's share, the median remote share over boards with
MIN_ROLES or more open roles), so a page never disagrees with the edition it belongs to.

Indexing: a board with fewer than MIN_ROLES open roles and no measured change yet says little, so its page carries
`noindex,follow` and stays out of the sitemap; it is still linked from the directory and reachable.
"""
import hashlib
import html
import json
import os
import re
import statistics
import sys
import time
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_ROLES = 10          # below this, without history, a page is noindex (same floor the report uses for company lists)
MIN_HISTORY_DAYS = 14   # the weekly pipeline measures change only for boards with this much daily history
PER_PAGE = 400          # company rows per directory page
LETTERS = ["0-9"] + [chr(c) for c in range(ord("a"), ord("z") + 1)]


def slug(s: str) -> str:
    """Jekyll's slugify in 'latin' mode: accents stripped, anything but letters and digits becomes one hyphen."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""), quote=True)


def num(n) -> str:
    return f"{n:,}"


def signed(n) -> str:
    return f"{n:+,}"


def pct(x) -> str:
    return "—" if x is None else f"{x:g}%"


def long_date(iso: str) -> str:
    y, m, d = (int(p) for p in iso.split("-"))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{d} {months[m - 1]} {y}"


SIGNAL = {"A": "accelerating", "C": "contracting", "S": "steady"}
VENDOR = {"greenhouse": "Greenhouse", "lever": "Lever", "ashby": "Ashby", "smartrecruiters": "SmartRecruiters", "recruitee": "Recruitee", "personio": "Personio"}


def load(site: Path) -> tuple[list[dict], dict]:
    data = json.loads((site / "reports" / "data" / "companies.json").read_text())
    cols = data["columns"]
    rows = []
    for r in data["companies"]:
        row = dict(zip(cols, r))
        row["company"] = re.sub(r"\s+", " ", str(row["company"])).strip("‎‏﻿ ").strip()
        rows.append(row)
    window = data.get("windowDays")
    home = ROOT / "_data" / "home.json"
    if home.exists():
        h = json.loads(home.read_text())
        if h.get("date") == data["date"] and h.get("windowDays"):
            window = h["windowDays"]  # the span the edition measured (the configured window, capped by the history that exists)
    ctx = {"date": data["date"], "window": window}
    return rows, ctx


def assign_slugs(rows: list[dict]) -> None:
    """Biggest board of a name keeps the plain slug; the others get the vendor, then a number."""
    by_slug = defaultdict(list)
    for r in sorted(rows, key=lambda r: (-r["openRoles"], r["vendor"], r["company"])):
        by_slug[slug(r["company"]) or "company"].append(r)
    taken = set()
    for base, group in by_slug.items():
        for i, r in enumerate(group):
            cands = [base] if i == 0 else [f"{base}-{slug(r['vendor'])}", f"{base}-{i + 1}"]
            s = next((c for c in cands if c not in taken), None)
            n = len(group) + 1
            while s is None or s in taken:
                s = f"{base}-{n}"; n += 1
            taken.add(s)
            r["slug"] = s


def benchmark(rows: list[dict]) -> dict:
    """The same arithmetic as the weekly report's headline table, from the rows themselves."""
    total = sum(r["openRoles"] for r in rows)
    ai = sum(round(r["aiRoleSharePct"] * r["openRoles"] / 100) for r in rows if r["aiRoleSharePct"] is not None)
    remote = sum(round(r["remoteSharePct"] * r["openRoles"] / 100) for r in rows if r["remoteSharePct"] is not None)
    ten = [r["remoteSharePct"] for r in rows if r["openRoles"] >= MIN_ROLES and r["remoteSharePct"] is not None]
    hist = sum(1 for r in rows if r["netChange"] is not None)
    return {"companies": len(rows), "total": total, "aiPct": round(ai / total * 100, 1) if total else None,
            "remotePct": round(remote / total * 100, 1) if total else None,
            "medianRemote": statistics.median(ten) if ten else None, "n10": len(ten), "history": hist}


def letter_of(r: dict) -> str:
    c = r["slug"][:1]
    return "0-9" if c.isdigit() or not c.isalpha() else c


def page_body(r: dict, ctx: dict, bench: dict, beta: bool) -> tuple[str, str, str, bool]:
    """Returns (title, description, body html, indexable)."""
    name, date, d = r["company"], ctx["date"], ctx["window"]
    date_l = long_date(date)
    vendor = VENDOR.get(r["vendor"], r["vendor"].capitalize() if r["vendor"] else "")
    open_ = r["openRoles"]
    has_flow = r["netChange"] is not None
    thin = open_ < MIN_ROLES and not has_flow
    word = SIGNAL.get(r["signal"], "steady") if has_flow else None
    letter = letter_of(r)

    if has_flow:
        growth = "" if r["growthPct"] is None else f" ({r['growthPct']:+g}%)"
        change_stat = (f'<div class="stat{" up" if r["netChange"] > 0 else (" down" if r["netChange"] < 0 else "")}">'
                       f'<b>{signed(r["netChange"])}</b><span>open roles net over the {d} days to {date_l}{esc(growth)}; hiring {word}</span></div>')
        change_sentence = (f"{esc(name)} is <b>{word}</b>: {num(open_)} open roles on {date_l}, {signed(r['netChange'])}{esc(growth)} against {d} days earlier. "
                           f"Accelerating means open roles up 20% or more over the window with at least 3 roles opened, contracting means down 20% or more, steady is everything in between; "
                           f"{num(bench['history'])} of the {num(bench['companies'])} tracked companies had the {MIN_HISTORY_DAYS}+ days of history the signal needs.")
    else:
        change_stat = (f'<div class="stat"><b>—</b><span>change over {d} days: measured once the board has {MIN_HISTORY_DAYS}+ days of daily history</span></div>')
        change_sentence = (f"Hiring Pulse has fewer than {MIN_HISTORY_DAYS} days of daily history for this board, so its change over the edition's window and its "
                           f"hiring signal are not measured yet. They appear in the first edition after its history reaches {MIN_HISTORY_DAYS} days; "
                           f"{num(bench['history'])} of the {num(bench['companies'])} tracked companies had that history on {date_l}.")

    ai, remote, fn, ind = r["aiRoleSharePct"], r["remoteSharePct"], r["topFunction"], r["industry"]
    stats = (f'<div class="stats">'
             f'<div class="stat"><b>{num(open_)}</b><span>open roles on {date_l}</span></div>'
             f'{change_stat}'
             f'<div class="stat"><b>{esc(pct(ai))}</b><span>AI/ML roles, share of its {num(open_)} open roles</span></div>'
             f'<div class="stat"><b>{esc(pct(remote))}</b><span>remote roles, share of its {num(open_)} open roles</span></div>'
             f'</div>')
    if open_ == 0:
        board_line = f"{esc(name)}'s board listed no open roles on {date_l}; the shares above are therefore not defined."
    else:
        parts = []
        parts.append(f"Most of its open roles are in <b>{esc(fn)}</b>." if fn else "No single largest function is recorded for this board (its titles did not map to one function).")
        if ai is not None:
            parts.append(f"{esc(pct(ai))} of its {num(open_)} open roles are AI/ML roles" + (f" and {esc(pct(remote))} are remote." if remote is not None else "."))
        board_line = " ".join(parts)
    facts = (f'<dl><dt>Job board</dt><dd>{esc(vendor)}</dd>'
             f'<dt>Industry</dt><dd>{esc(ind) if ind else "not recorded for this board"}</dd>'
             f'<dt>Largest function</dt><dd>{esc(fn) if fn else "—"}</dd>'
             f'<dt>Edition</dt><dd>{date_l}; the next weekly edition updates this page</dd></dl>')

    me_ai = pct(ai) if ai is not None else "—"
    me_remote = pct(remote) if remote is not None else "—"
    bench_p = (f"Across all {num(bench['total'])} open roles at the {num(bench['companies'])} companies tracked on {date_l}, "
               f"{bench['aiPct']:g}% are AI/ML roles and {bench['remotePct']:g}% are remote; the median company with {MIN_ROLES}+ open roles "
               f"has {bench['medianRemote']:g}% of its roles remote ({num(bench['n10'])} companies). {esc(name)}: {esc(me_ai)} AI/ML, {esc(me_remote)} remote.")

    track = (f'<p><a class="track" href="#beta" data-company="{esc(name)}">{esc(name)} is in the daily files: get them free by e-mail →</a></p>'
             if beta else f'<p><a class="track" href="/get-the-data/">The daily files behind this page →</a></p>')

    body = (f'<p class="co-crumbs"><a href="/companies/">Companies A–Z</a> › <a href="/companies/{letter}/">{esc(letter.upper())}</a></p>'
            f'<h1>{esc(name)}: open roles and hiring signal</h1>'
            f'<p class="kicker">What {esc(name)}’s public job board ({esc(vendor)}) showed on {date_l}, read daily by Hiring Pulse. '
            f'Every figure counts roles on that board, once each; nothing here is a statement about the company beyond its board.</p>'
            f'{stats}'
            f'<h2>What the board says</h2>'
            f'<p>{change_sentence}</p>'
            f'<p>{board_line}</p>'
            f'{facts}'
            f'<h2>Against the benchmark</h2>'
            f'<p>{bench_p}</p>'
            f'{track}'
            f'<p class="note">Source: {esc(name)}’s job board on {esc(vendor)}, read every day; a role is counted once, from the board itself, and a closure is '
            f'recorded the day the posting disappears. Titles are mapped to functions and the AI/ML flag with one fixed taxonomy '
            f'(<a href="/methodology/">methodology</a>). Weekly editions: <a href="/reports/latest/">this week’s report</a>.</p>')

    title = f"{esc(name)} hiring: {num(open_)} open roles" + (f", {word}" if word else "")
    change_d = (f"{signed(r['netChange'])} over {d} days, {word}" if has_flow else f"change measured after {MIN_HISTORY_DAYS} days of history")
    desc = (f"{name}: {num(open_)} open roles on its {vendor} job board on {date}, {change_d}; {me_ai} AI/ML, {me_remote} remote. "
            f"Read daily by Hiring Pulse.")
    return title, esc(desc), body, not thin


def jsonld(r: dict, ctx: dict, url: str, site: str) -> str:
    name = r["company"]
    ds = {"@context": "https://schema.org", "@type": "Dataset", "name": f"Open roles on {name}'s job board",
          "description": f"Daily readings of {name}'s public job board by Hiring Pulse: open roles, change over the edition's window, AI/ML and remote share.",
          "url": url, "creator": {"@id": f"{site}#organization"}, "publisher": {"@id": f"{site}#organization"},
          "temporalCoverage": ctx["date"], "inLanguage": "en", "isAccessibleForFree": True,
          "license": "https://creativecommons.org/licenses/by/4.0/",
          "variableMeasured": ["open roles", "net change in open roles", "AI/ML role share", "remote role share", "largest function"],
          "isPartOf": {"@type": "Dataset", "name": "Hiring Pulse: daily startup hiring data", "url": site}}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Companies A–Z", "item": f"{site}companies/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}
    return ("<script type=\"application/ld+json\">" + json.dumps(ds, ensure_ascii=False) + "</script>"
            "<script type=\"application/ld+json\">" + json.dumps(bc, ensure_ascii=False) + "</script>")


class Shell:
    """The built template page, with its stylesheet moved to one shared file so each company page stays small."""

    def __init__(self, site: Path):
        tpl = site / "company" / "_template" / "index.html"
        s = tpl.read_text()
        m = re.search(r"<style>(.*?)</style>", s, re.S)
        if not m:
            sys.exit("template: no <style> block found")
        css = m.group(1)
        digest = hashlib.sha1(css.encode()).hexdigest()[:10]
        css_path = f"/assets/site-{digest}.css"
        (site / "assets").mkdir(exist_ok=True)
        (site / css_path.lstrip("/")).write_text(css)
        s = s[:m.start()] + f'<link rel="stylesheet" href="{css_path}">' + s[m.end():]
        s = s.replace('<meta name="robots" content="noindex">', "")  # the template's own noindex; set per page below
        self.robots = '<meta name="robots" content="index,follow,max-image-preview:large">'
        if self.robots not in s or "@@BODY@@" not in s or "@@TITLE@@" not in s:
            sys.exit("template: markers missing (robots meta, @@TITLE@@ or @@BODY@@)")
        m = re.search(r'<link rel="canonical" href="(https?://[^/"]+/)company/_template/">', s)
        if not m:
            sys.exit("template: canonical URL not found")
        self.site = m.group(1)
        self.beta = 'id="beta"' in s
        self.use_input = re.search(r'<input type="text" name="[^"]+"', s)
        self.html = s

    def render(self, url_path: str, title: str, desc: str, body: str, indexable: bool, head_extra: str = "", track: str = "") -> str:
        s = self.html.replace("/company/_template/", url_path).replace("@@TITLE@@", title).replace("@@DESC@@", desc)
        if not indexable:
            s = s.replace(self.robots, '<meta name="robots" content="noindex,follow">')
        s = s.replace("@@BODY@@", body + head_extra)
        if track and self.use_input:
            tag = self.use_input.group(0)
            s = s.replace(tag, f'{tag} value="Track {esc(track)}"', 1)
        return s


def directory_pages(rows: list[dict], ctx: dict, bench: dict, shell: Shell, site: Path) -> list[str]:
    date_l = long_date(ctx["date"])
    groups = defaultdict(list)
    for r in rows:
        groups[letter_of(r)].append(r)
    for g in groups.values():
        g.sort(key=lambda r: (r["slug"], r["company"]))
    urls = []

    def letter_nav(current: str) -> str:
        items = []
        for L in LETTERS:
            n = len(groups.get(L, []))
            if not n:
                continue
            cls = ' class="on"' if L == current else ""
            items.append(f'<a{cls} href="/companies/{L}/">{L.upper()}<small>{num(n)}</small></a>')
        return '<nav class="dir-letters" aria-label="Companies by first letter">' + "".join(items) + "</nav>"

    intro = (f'<p class="co-crumbs"><a href="/">Hiring Pulse</a> › Companies A–Z</p><h1>Companies A–Z</h1>'
             f'<p class="kicker">Every company job board Hiring Pulse read for the edition of {date_l}: {num(bench["companies"])} boards, {num(bench["total"])} open roles between them. '
             f'One page per company with its open roles, the change over the edition’s window once it has {MIN_HISTORY_DAYS}+ days of daily history ({num(bench["history"])} boards had it), '
             f'and its AI/ML and remote share. Boards are listed by name; the number under each letter is how many start with it.</p>')
    biggest = sorted(rows, key=lambda r: -r["openRoles"])[:25]
    big_rows = "".join(f'<tr><td><a href="/company/{r["slug"]}/">{esc(r["company"])}</a></td><td class="n">{num(r["openRoles"])}</td>'
                       f'<td class="n">{signed(r["netChange"]) if r["netChange"] is not None else "—"}</td><td>{esc(VENDOR.get(r["vendor"], r["vendor"]))}</td></tr>' for r in biggest)
    index_body = (intro + letter_nav("") +
                  f'<h2>The 25 largest boards on {date_l}</h2>'
                  f'<table class="dir"><thead><tr><th>Company</th><th class="n">Open roles</th><th class="n">Change, {ctx["window"]} days</th><th>Job board</th></tr></thead><tbody>{big_rows}</tbody></table>'
                  f'<p class="note">Change is the net change in open roles over the {ctx["window"]} days to {date_l}; — means the board has under {MIN_HISTORY_DAYS} days of daily history. '
                  f'Looking for one company? The <a href="/#company-q">lookup on the home page</a> finds any tracked board as you type.</p>')
    out = site / "companies" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(shell.render("/companies/", "Companies A–Z: every job board Hiring Pulse tracks",
                                esc(f"The directory of every company job board Hiring Pulse reads daily, A to Z: {num(bench['companies'])} boards on {ctx['date']}, one page per company with open roles, change, AI/ML and remote share."),
                                index_body, True))
    urls.append("/companies/")

    for L in LETTERS:
        g = groups.get(L)
        if not g:
            continue
        pages = [g[i:i + PER_PAGE] for i in range(0, len(g), PER_PAGE)]
        for pi, chunk in enumerate(pages, start=1):
            path = f"/companies/{L}/" if pi == 1 else f"/companies/{L}/{pi}/"
            pager = ""
            if len(pages) > 1:
                links = []
                for k in range(1, len(pages) + 1):
                    href = f"/companies/{L}/" if k == 1 else f"/companies/{L}/{k}/"
                    links.append(f"<b>{k}</b>" if k == pi else f'<a href="{href}">{k}</a>')
                pager = f'<nav class="dir-pages" aria-label="Pages">' + "".join(links) + "</nav>"
            trs = "".join(f'<tr><td><a href="/company/{r["slug"]}/">{esc(r["company"])}</a></td><td class="n">{num(r["openRoles"])}</td>'
                          f'<td class="n">{signed(r["netChange"]) if r["netChange"] is not None else "—"}</td><td>{esc(VENDOR.get(r["vendor"], r["vendor"]))}</td></tr>' for r in chunk)
            label = "0–9" if L == "0-9" else L.upper()
            body = (f'<p class="co-crumbs"><a href="/companies/">Companies A–Z</a> › {label}</p>'
                    f'<h1>Companies: {label}</h1>'
                    f'<p class="kicker">{num(len(g))} tracked job boards whose name starts with {label}, edition of {date_l}'
                    + (f"; page {pi} of {len(pages)}, {num(len(chunk))} boards" if len(pages) > 1 else "") + ".</p>"
                    + letter_nav(L) + pager +
                    f'<table class="dir"><thead><tr><th>Company</th><th class="n">Open roles</th><th class="n">Change, {ctx["window"]} days</th><th>Job board</th></tr></thead><tbody>{trs}</tbody></table>'
                    + pager +
                    f'<p class="note">Open roles as read on {date_l}. Change is the net change in open roles over the {ctx["window"]} days to that date; — means the board has under {MIN_HISTORY_DAYS} days of daily history.</p>')
            title = f"Companies starting with {label}" + (f", page {pi}" if len(pages) > 1 else "") + ": open roles and change"
            desc = esc(f"{num(len(g))} company job boards starting with {label}, as Hiring Pulse read them on {ctx['date']}: open roles and the change over {ctx['window']} days, one page per company.")
            out = site / path.strip("/") / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(shell.render(path, title, desc, body, True))
            urls.append(path)
    return urls


def extend_sitemap(site: Path, urls: list[str], date: str, origin: str) -> int:
    sm = site / "sitemap.xml"
    if not sm.exists():
        return 0
    s = sm.read_text()
    extra = "".join(f"<url><loc>{origin.rstrip('/')}{html.escape(u)}</loc><lastmod>{date}</lastmod></url>\n" for u in urls)
    s = s.replace("</urlset>", extra + "</urlset>")
    sm.write_text(s)
    return len(urls)


def main() -> int:
    t0 = time.time()
    site = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "_site"
    rows, ctx = load(site)
    assign_slugs(rows)
    bench = benchmark(rows)
    shell = Shell(site)
    origin = shell.site
    indexable = 0
    sitemap_urls = []
    for r in rows:
        path = f"/company/{r['slug']}/"
        url = origin.rstrip("/") + path
        title, desc, body, ok = page_body(r, ctx, bench, shell.beta)
        out = site / "company" / r["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(shell.render(path, title, desc, body, ok, jsonld(r, ctx, url, origin), track=r["company"]))
        if ok:
            indexable += 1
            sitemap_urls.append(path)
    dir_urls = directory_pages(rows, ctx, bench, shell, site)
    (site / "company" / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/companies/"><title>Companies A–Z</title>'
        '<link rel="canonical" href="' + origin + 'companies/"><p>Moved: <a href="/companies/">Companies A–Z</a>.</p>')
    added = extend_sitemap(site, sitemap_urls + dir_urls, ctx["date"], origin)
    tpl = site / "company" / "_template"
    for f in tpl.glob("*"):
        f.unlink()
    tpl.rmdir()
    size = sum(f.stat().st_size for f in (site / "company").rglob("*.html")) + sum(f.stat().st_size for f in (site / "companies").rglob("*.html"))
    secs = time.time() - t0
    report = (f"company pages: {len(rows):,} written ({indexable:,} indexable, {len(rows) - indexable:,} noindex: under {MIN_ROLES} open roles and no history), "
              f"{len(dir_urls):,} directory pages, {added:,} sitemap entries added, {size / 1e6:.0f} MB of HTML, {secs:.1f}s. "
              f"Edition {ctx['date']}, window {ctx['window']} days; benchmark: {bench['total']:,} open roles, {bench['aiPct']}% AI/ML, "
              f"{bench['remotePct']}% remote, median remote share {bench['medianRemote']}% over {bench['n10']:,} boards with {MIN_ROLES}+ roles, {bench['history']:,} with history.")
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as fh:
            fh.write(report + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
