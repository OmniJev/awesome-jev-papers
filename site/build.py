#!/usr/bin/env python3
"""Build the Awesome JEV Papers site from README.md into site/dist.

    python3 site/build.py

README.md is the only list. arXiv metadata is cached in site/arxiv.json, star counts and
Hugging Face upvotes are read live and cached for an hour in site/live.json.
"""
import datetime, html, json, os, re, shutil, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "dist")
REPO = "https://github.com/OmniJev/awesome-jev-papers"
SITE = "https://omnijev.github.io/awesome-jev-papers/"
GALLERY = "https://omnijev.github.io/awesome-jev-gallery/"
FONTS = ("DepartureMono-Regular.otf", "PressStart2P-Regular.ttf")
HUES = [("#0ea5e9", "#5cc8f5"), ("#7c5ce6", "#a78bfa"), ("#f59e0b", "#fbbf4d"), ("#e5484d", "#ff7b80"),
        ("#2f80ed", "#6fa8ff"), ("#12a150", "#4fd18b"), ("#8b5e34", "#c9955f"), ("#be2d6e", "#f472b6"),
        ("#12866b", "#4fc0a3")]
ICON = ["################",
        "#..............#",
        "#...mmmmmmm....#",
        "#...m.....mm...#",
        "#...m.oooo.mm..#",
        "#...m.......m..#",
        "#...m.ooooo.m..#",
        "#...m.......m..#",
        "#...m.ooo...m..#",
        "#...mmmmmmmmm..#",
        "#..............#",
        "################",
        "......####......"]
ENTRY = re.compile(r'^- \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\),\s*"(?P<title>.+?)"\.\s*(?P<rest>.*)$')
BADGE = re.compile(r'\[!\[(?P<label>[^\]]*)\]\([^)]*\)\]\((?P<url>[^)\s]+)\)')
ARXIV = re.compile(r'arxiv\.org/(?:abs|pdf)/(?P<id>\d{4}\.\d{4,5})')
A = "{http://www.w3.org/2005/Atom}"
AX = "{http://arxiv.org/schemas/atom}"
UA = "awesome-jev-papers"


def esc(s):
    return html.escape(s or "", quote=True)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def split_head(h):
    lead, _, rest = h.partition(" ")
    return (lead, rest.strip()) if lead and not lead[0].isalnum() else ("", h.strip())


def detex(s, name):
    s = s.replace("\\method", name).replace("\\$", "\0")
    s = re.sub(r"\$?\\times\$?", "\u00d7", s)
    s = re.sub(r"\$?\\sim\$?", "\u223c", s)
    s = re.sub(r"(?<=\w)~(?=\w)", " ", s)
    s = re.sub(r"\\(?:text(?:bf|it|tt|sc|rm)|emph|mathrm)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\$([^$\\]{1,12})\$", r"\1", s)
    for a, b in (("\\%", "%"), ("\\,", " "), ("\\&", "&"), ("\\_", "_"), ("\0", "$")):
        s = s.replace(a, b)
    return s


def logo(animate=False):
    sq = lambda x, y: f"M{x} {y}h1v1h-1z"
    frame = "".join(sq(x, y) for y, r in enumerate(ICON) for x, ch in enumerate(r) if ch == "#")
    cells = [(x, y, ch) for y, r in enumerate(ICON) for x, ch in enumerate(r) if ch in "mo"]
    if animate:
        inner = "".join(f'<rect class="{ch}" x="{x}" y="{y}" width="1" height="1" style="--d:{i}"/>'
                        for i, (x, y, ch) in enumerate(cells))
    else:
        inner = "".join(f'<path class="{k}" d="{"".join(sq(x, y) for x, y, ch in cells if ch == k)}"/>' for k in "mo")
    return (f'<svg class="px" viewBox="0 0 16 13" aria-hidden="true"><path fill="currentColor" d="{frame}"/>'
            f"{inner}</svg>")


def favicon():
    col = {"#": "#1e1e1e", "m": "#ff5c1a", "o": "#ffa66b"}
    paths = "".join(
        f'<path fill="{c}" d="{"".join(f"M{x} {y + 1}h1v1h-1z" for y, r in enumerate(ICON) for x, ch in enumerate(r) if ch == k)}"/>'
        for k, c in col.items())
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
            f'<rect width="16" height="16" fill="#fefefe"/>{paths}</svg>')


def parse_readme():
    lines = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read().splitlines()
    chips = {}
    for ln in lines:
        if ln.count(" · ") >= 3 and not ln.startswith(("#", "-", "!", "[")):
            for part in ln.split(" · "):
                lead, rest = split_head(part.strip())
                if lead:
                    chips[lead] = rest
            break
    tabs, leaves, papers = [], [], []
    top = cur = None
    for ln in lines:
        if ln.startswith("## ") or ln.startswith("### "):
            lead, name = split_head(ln.split(" ", 1)[1])
            node = {"name": name, "desc": "", "n": 0}
            if ln.startswith("## "):
                node.update(key=slug(name), chip=chips.get(lead, name), subs=[])
                top = cur = node
                tabs.append(node)
            elif top:
                node.update(key=slug(top["name"] + " " + name), parent=top["key"])
                top["subs"].append(node)
                cur = node
            continue
        if cur is None:
            continue
        m = ENTRY.match(ln)
        if m:
            leaf = cur
            if not any(l is leaf for l in leaves):
                leaves.append(leaf)
            aid = ARXIV.search(m["url"])
            p = {"name": m["name"].strip(), "title": m["title"].strip(), "url": m["url"],
                 "id": aid["id"] if aid else None, "sec": leaf["key"], "tab": top["key"],
                 "order": len(papers), "code": [], "model": None, "site": None, "daily": None}
            for b in BADGE.finditer(m["rest"]):
                label, url = b["label"].lower(), b["url"]
                if "github.com/" in url and ("code" in label or "github" in label):
                    p["code"].append({"url": url, "repo": "/".join(url.split("github.com/")[1].split("/")[:2])})
                elif "huggingface.co/papers/" in url:
                    p["daily"] = {"url": url}
                elif "model" in label or "huggingface.co/" in url:
                    p["model"] = url
                elif "website" in label or "site" in label or "page" in label:
                    p["site"] = url
            papers.append(p)
            leaf["n"] += 1
            if leaf is not top:
                top["n"] += 1
        elif ln.strip() and not cur["desc"] and not cur["n"] and not ln.startswith(("-", ">", "<", "!", "[", "|", "`", "#")):
            cur["desc"] = ln.strip()
    tabs = [t for t in tabs if t["n"]]
    for i, t in enumerate(tabs):
        t["hue"] = HUES[i % len(HUES)]
        for s in t["subs"]:
            s["hue"] = t["hue"]
    for l in leaves:
        if "parent" in l:
            l["parent_name"] = next(t["name"] for t in tabs if t["key"] == l["parent"])
    return tabs, leaves, papers


def get(url, timeout=30, accept=None):
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
    h = {"User-Agent": UA}
    if accept:
        h["Accept"] = accept
    if tok and "api.github.com" in url:
        h["Authorization"] = "Bearer " + tok
    return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout).read()


def arxiv_meta(ids):
    path = os.path.join(HERE, "arxiv.json")
    cache = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    need = [i for i in ids if i not in cache]
    for k in range(0, len(need), 20):
        batch = need[k:k + 20]
        q = urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": len(batch)})
        try:
            root = ET.fromstring(get("https://export.arxiv.org/api/query?" + q, timeout=60))
        except Exception as ex:
            print(f"  arXiv {batch[0]}..: {ex}")
            continue
        for e in root.findall(A + "entry"):
            m = ARXIV.search(e.findtext(A + "id") or "")
            if not m:
                continue
            cat = e.find(AX + "primary_category")
            cache[m["id"]] = {
                "authors": [a.findtext(A + "name").strip() for a in e.findall(A + "author")],
                "date": (e.findtext(A + "published") or "")[:10],
                "abstract": " ".join((e.findtext(A + "summary") or "").split()),
                "cat": cat.get("term") if cat is not None else ""}
        if k + 20 < len(need):
            time.sleep(3)
    json.dump(dict(sorted(cache.items())), open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    missing = [i for i in ids if i not in cache]
    print(f"arXiv: {len(need) - len(missing)} fetched, {len(ids) - len(need)} cached, {len(missing)} missing")
    return cache


def live(keys, max_age=3600):
    path = os.path.join(HERE, "live.json")
    cache = json.load(open(path)) if os.path.exists(path) else {}
    now, out, fetched = time.time(), {}, 0
    for key in keys:
        c = cache.get(key)
        if c and now - c["t"] < max_age:
            out[key] = c["v"]
            continue
        kind, ref = key.split(":", 1)
        try:
            if kind == "gh":
                v = json.loads(get(f"https://api.github.com/repos/{ref}", accept="application/vnd.github+json"))["stargazers_count"]
            else:
                v = json.loads(get(f"https://huggingface.co/api/papers/{ref}")).get("upvotes", 0)
            cache[key] = {"v": v, "t": now}
            out[key] = v
            fetched += 1
        except Exception as ex:
            print(f"  {key}: {ex}")
            out[key] = c["v"] if c else None
    json.dump(cache, open(path, "w"), indent=1)
    print(f"stars and upvotes: {fetched} fetched, {len(keys) - fetched} from cache")
    return out


def build():
    tabs, leaves, papers = parse_readme()
    meta = arxiv_meta([p["id"] for p in papers if p["id"]])
    keys = sorted({"gh:" + c["repo"] for p in papers for c in p["code"]} |
                  {"hf:" + p["id"] for p in papers if p["daily"] and p["id"]})
    counts = live(keys)
    for p in papers:
        p.update(meta.get(p["id"]) or {"authors": [], "date": "", "abstract": "", "cat": ""})
        p["abstract"] = detex(p["abstract"], p["name"])
        for c in p["code"]:
            c["stars"] = counts.get("gh:" + c["repo"])
        if p["daily"]:
            p["daily"]["up"] = counts.get("hf:" + p["id"])

    found = next((t for t in tabs if t["key"] == "foundations"), None)
    total = len(papers)
    n_found = found["n"] if found else 0
    n_code = sum(bool(p["code"]) for p in papers)
    n_daily = sum(bool(p["daily"]) for p in papers)
    built = datetime.datetime.now(datetime.timezone.utc)
    tagline = "Research papers on Jev, TypeSafe's System One model, and the open models built in its shape."

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    for f in ("papers.css", "papers.js", "og.png"):
        shutil.copy(os.path.join(HERE, f), os.path.join(OUT, "assets", f))
    shutil.copytree(os.path.join(HERE, "fonts"), os.path.join(OUT, "assets", "fonts"))
    open(os.path.join(OUT, "assets", "favicon.svg"), "w").write(favicon())
    with open(os.path.join(OUT, "assets", "papers.css"), "a", encoding="utf-8") as f:
        f.write("\n:root{" + "".join(f"--s-{t['key']}:{t['hue'][0]};" for t in tabs) + "}"
                "\n:root[data-theme=\"dark\"]{" + "".join(f"--s-{t['key']}:{t['hue'][1]};" for t in tabs) + "}\n")

    data = {"built": built.isoformat(timespec="minutes"),
            "tabs": [{k: t[k] for k in ("key", "name", "chip", "desc", "n")} for t in tabs],
            "leaves": [{"key": l["key"], "name": l["name"], "desc": l["desc"], "n": l["n"],
                        "tab": l.get("parent", l["key"]), "parent": l.get("parent_name")} for l in leaves],
            "papers": papers}
    pills = (f'<button type="button" data-tab="" aria-pressed="true">All <b>{total}</b></button>' + "".join(
        f'<button type="button" data-tab="{t["key"]}" aria-pressed="false" style="--sc:var(--s-{t["key"]})"><i></i>{esc(t["chip"])} <b>{t["n"]}</b></button>'
        for t in tabs))
    sorts = "".join(f'<button type="button" data-sort="{k}" aria-pressed="false">{k}</button>'
                    for k in ("sections", "newest", "stars", "upvotes"))
    meta_line = (f"{total} papers, {total - n_found} of them on Jev and {n_found} from the work before it."
                 if found else f"{total} papers.")
    body = f"""<header class="top">
  <a class="brand" href="{SITE}">{logo()}<span class="w">JEV Papers</span></a>
  <nav><a href="{REPO}#readme" target="_blank" rel="noopener">README</a><a href="{GALLERY}" target="_blank" rel="noopener">Gallery</a><button id="theme" type="button" aria-label="Switch colour theme">Dark</button><a class="hot" href="{REPO}" target="_blank" rel="noopener">GitHub</a></nav>
</header>
<section class="wrap banner">
  <div class="logo">{logo(animate=True)}</div>
  <div>
    <span class="tag">awesome</span>
    <h1>JEV Papers</h1>
    <p class="sub" id="sub">{esc(tagline)}</p>
    <p class="meta">{esc(meta_line)} Press <b>/</b> to search titles, authors and abstracts.</p>
  </div>
</section>
<div class="wrap controls">
  <div class="tabs" id="pills">{pills}</div>
  <div class="tools">
    <label class="search"><span>find</span><input type="search" id="q" placeholder="press /" aria-label="Search"></label>
    <div class="grp"><span>sort</span><div class="tabs" id="sort">{sorts}</div></div>
    <div class="grp cols"><span>per row</span><button id="colDec" type="button" aria-label="Fewer per row">-</button><b id="colN">3</b><button id="colInc" type="button" aria-label="More per row">+</button></div>
    <span class="count" id="count"></span>
  </div>
</div>
<main class="wrap"><div id="grid"></div><div class="empty" id="empty" hidden>Nothing matches.</div></main>
<dialog id="abs" aria-labelledby="absName"></dialog>
<footer>
  <div class="foot-in">
    <div class="foot-logo">{logo()}</div>
    <div class="fwin">
      <div class="win-t"><span class="t">awesome-jev-papers.txt</span></div>
      <div class="win-b">{total} papers, {n_code} with code and {n_daily} on Hugging Face Daily Papers.<br>Projects, models and benchmarks live in the <a href="{GALLERY}">Awesome JEV gallery</a>.<br>Curated at <a href="{REPO}">OmniJev/awesome-jev-papers</a>, CC BY 4.0.<br>Stars and upvotes read on {built:%d %B %Y}, {built:%H:%M} UTC.</div>
    </div>
  </div>
</footer>
<script id="data" type="application/json">{json.dumps(data, ensure_ascii=False).replace("</", "<\\/")}</script>"""

    desc = f"{total} research papers on Jev, TypeSafe's System One model, and the open models built in its shape, with abstracts, code and models."
    ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Awesome JEV Papers",
                     "description": desc, "url": SITE})
    preload = "\n".join(f'<link rel="preload" href="assets/fonts/{f}" as="font" type="font/{f.rsplit(".", 1)[1]}" crossorigin>'
                        for f in FONTS)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome JEV Papers</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:title" content="Awesome JEV Papers">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}assets/og.png">
<meta name="theme-color" content="#1e1e1e">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{preload}
<link rel="stylesheet" href="assets/papers.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{body}
<script src="assets/papers.js"></script>
</body>
</html>
"""
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{SITE}</loc><lastmod>{built:%Y-%m-%d}</lastmod><changefreq>daily</changefreq></url>\n"
        "</urlset>\n")
    print(f"{OUT}/index.html: {total} papers in {len(tabs)} tabs, {len(leaves)} sections")


if __name__ == "__main__":
    build()
