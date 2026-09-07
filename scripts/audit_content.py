#!/usr/bin/env python3
"""
Content/indexing audit for bestiptvtoday.com.
Reads every page from sitemap.xml's on-disk sources (index.html, blog/index.html,
blog/*.html), extracts title/meta description/word count/H2s/canonical/outbound
internal links, and builds a reverse link graph (who links to each page).
Outputs JSON to stdout.
"""
import json
import os
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://bestiptvtoday.com"

def rel_path_to_url(rel):
    if rel == "index.html":
        return SITE + "/"
    if rel == "blog/index.html":
        return SITE + "/blog/"
    return SITE + "/" + rel

def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()

def word_count(soup):
    # remove script/style/nav/footer for a rough "content" word count too
    body = soup.body or soup
    text = body.get_text(separator=" ", strip=True)
    words = re.findall(r"[A-Za-zÀ-ÿ0-9']+", text)
    return len(words)

def analyze(rel):
    html = load(rel)
    soup = BeautifulSoup(html, "html.parser")
    url = rel_path_to_url(rel)

    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else None

    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc_tag.get("content", "").strip() if meta_desc_tag else None

    canonical_tag = soup.find("link", attrs={"rel": "canonical"})
    canonical = canonical_tag.get("href") if canonical_tag else None

    robots_tag = soup.find("meta", attrs={"name": "robots"})
    robots_content = robots_tag.get("content", "") if robots_tag else ""
    noindex = "noindex" in robots_content.lower()

    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2s = [h.get_text(strip=True) for h in soup.find_all("h2")]
    h3_count = len(soup.find_all("h3"))

    wc = word_count(soup)

    # outbound internal links (same-origin, dedup, excluding nav/footer would need markup knowledge;
    # keep all <a> but tag whether they are inside <nav>/<footer>/<header> for context)
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute = urljoin(url, href)
        parsed = urlparse(absolute)
        if parsed.netloc not in ("bestiptvtoday.com", "www.bestiptvtoday.com", ""):
            continue
        clean = absolute.split("#")[0]
        if not clean.startswith(SITE):
            continue
        in_structural = False
        p = a
        for _ in range(6):
            p = p.parent
            if p is None:
                break
            if getattr(p, "name", None) in ("nav", "footer", "header"):
                in_structural = True
                break
        links.append({"href": clean, "text": a.get_text(strip=True)[:60], "structural": in_structural})

    # has FAQ section heuristic
    has_faq = bool(re.search(r"\bFAQ\b|frequently asked questions", html, re.IGNORECASE))

    return {
        "rel": rel,
        "url": url,
        "title": title,
        "title_len": len(title) if title else 0,
        "meta_desc": meta_desc,
        "meta_desc_len": len(meta_desc) if meta_desc else 0,
        "canonical": canonical,
        "noindex": noindex,
        "h1": h1s,
        "h2": h2s,
        "h2_count": len(h2s),
        "h3_count": h3_count,
        "word_count": wc,
        "has_faq": has_faq,
        "outbound_links": links,
    }

def main():
    rels = ["index.html", "blog/index.html"]
    blog_dir = os.path.join(ROOT, "blog")
    for f in sorted(os.listdir(blog_dir)):
        if f.endswith(".html") and f != "index.html":
            rels.append("blog/" + f)

    pages = {}
    for rel in rels:
        pages[rel] = analyze(rel)

    # reverse link graph: url -> list of (rel, text) that link to it, contextual (non-structural) only
    url_to_rel = {p["url"]: rel for rel, p in pages.items()}
    inbound_contextual = {rel: [] for rel in pages}
    inbound_any = {rel: [] for rel in pages}
    for rel, p in pages.items():
        seen_targets = set()
        for link in p["outbound_links"]:
            target_url = link["href"]
            target_rel = url_to_rel.get(target_url)
            if not target_rel or target_rel == rel:
                continue
            inbound_any[target_rel].append(rel)
            if not link["structural"]:
                key = (rel, target_rel)
                if key not in seen_targets:
                    inbound_contextual[target_rel].append({"from": rel, "text": link["text"]})
                    seen_targets.add(key)

    for rel, p in pages.items():
        p["inbound_contextual_count"] = len(inbound_contextual[rel])
        p["inbound_contextual_from"] = inbound_contextual[rel]
        p["inbound_any_count"] = len(set(inbound_any[rel]))

    print(json.dumps(pages, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
