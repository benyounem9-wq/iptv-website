# Content & Indexing Audit — bestiptvtoday.com

**Date:** September 6, 2026
**Scope:** Why 35 URLs (32 blog articles + the homepage, `/blog/`, and a stale `http://` crawl of the homepage) sit in Google's "Crawled – currently not indexed" bucket, and what genuinely justified content/internal-linking changes could help — not a request to force indexing.
**Status:** Findings only. No content has been changed yet.

---

## 0. Important timing caveat — read this first

Every one of these 35 URLs was last crawled by Google **between July 13 and August 27, 2026** — all of that **before** the technical fixes (duplicate-URL redirects, canonical tags, internal-link cleanup, `www` fix) shipped on **September 5–6, 2026**. Google has not recrawled a single one of these pages since the technical fixes went live.

That means some unknown share of this "not indexed" list may simply clear up once Google recrawls with the fixed technical signals in place — independent of anything below. This audit does **not** assume that; per your instruction, it looks for genuine content/structure reasons a page might stay un-indexed even after a clean recrawl, and only recommends changes that are justified regardless of the recrawl outcome.

## 1. Headline finding: this is not (mainly) a "thin content" problem — it's a language/authority gap

Word count turned out **not** to predict indexing status. Non-indexed articles average **563 words**, indexed articles average **519 words** — the non-indexed ones are, if anything, slightly longer.

What does predict it, strongly:

| | Total articles | Not indexed | Rate |
|---|---|---|---|
| German-language articles | 22 | 21 | **95%** |
| English-language articles | 39 | 11 | **28%** |

21 of the site's 22 German articles are stuck in "Crawled – currently not indexed." Only 1 German article is indexed. This is the single biggest pattern in the data, and it's almost certainly about **authority and demand signals for German-language content on what is otherwise an English-dominant, UK-focused site** (matches how the business is positioned) rather than a defect in any individual page — that part is Google's call, not something on-page work can force (§6). Two things this audit *can* act on:

- German articles are, on average, **more weakly internally linked** than English ones (2.7 contextual inbound links vs. 4.0) — a fixable structural weakness that compounds the authority gap.
- Several of the *worst* internal near-duplicate pairs on the whole site are German-vs-German (not German-vs-English) — see §2. Cleaning those up removes a plausible confusion signal for Google's German-content crawling of this specific site, on top of whatever the broader authority story is.

No `hreflang` tags exist anywhere on the site, and I'm **not** recommending adding them: `hreflang` is for marking literal translations of the same page, and these German and English articles are (mostly) genuinely different articles on related topics, not translations of each other. Adding `hreflang` here would misrepresent the content and isn't a suggested fix.

## 2. Duplicate/near-duplicate pairs found (beyond the 3 clusters already flagged)

The original audit flagged TiviMate, Firestick, and IBO Player as the highest-overlap clusters. Re-checking all 61 titles/intents against each other surfaced several pairs with **more** overlap than those three, and — tellingly — in every pair below, the weaker/thinner page is in the "not indexed" list, and in three of the four pairs *both* pages are:

| Pair | Language | Both non-indexed? | Overlap |
|---|---|---|---|
| `iptv-app.html` × `beste-iptv-app.html` | German × German | **Yes, both** | Both are literally "best IPTV app(s) comparison" — nearly identical title and intent, same language, same audience |
| `smart-iptv.html` × `smart-iptv-aktivieren.html` | German × German | **Yes, both** | Both cover the "Smart IPTV" app on Samsung/LG; `-aktivieren.html` is also the thinnest page on the entire site (316 words) |
| `iptv-player-windows.html` × `iptv-player-windows-11.html` | German × German | **Yes, both** | Same topic (Windows IPTV players), split only by OS version |
| `iptv-deutschland.html` × `iptv-anbieter.html` | German × German | **Yes, both** | General "everything about IPTV in Germany" vs. "best providers in Germany" — plausibly intentional, but currently under-differentiated |
| `what-is-m3u-iptv.html` × `m3u-playlist-iptv.html` | English × English | Only one (`what-is-m3u-iptv.html`) | Both are generic "what is M3U / M3U guide" explainers |
| `iptv-smarters-pro.html` × `iptv-smarters-pro-apk.html` | German × German | Only one (`-apk.html`) | Same app, split by setup-guide vs. APK-download angle |

For comparison, the three previously-flagged clusters check out about as well as the last report concluded:

- **IBO Player** (`ibo-player.html`, `iboplayer-setup.html`) — both indexed, low risk, no change needed.
- **TiviMate** (5 pages) — 4 of 5 indexed; only `tivimate-premium-apk.html` (the APK-download page) is stuck. Consistent with a broader pattern below.
- **Firestick** (3 pages) — only the German general guide (`iptv-firestick.html`) is stuck; the two English pages are indexed. Reads as part of the language pattern in §1 more than genuine duplication.

**A second, separate pattern:** every "APK download" page on the site — `iptv-apk.html`, `iptv-smarters-pro-apk.html`, `tivimate-premium-apk.html` — is in the not-indexed list. These are the thinnest, most commodity-shaped pages on the site (mostly "here's the download link and install steps," a pattern that exists on thousands of other sites). That's a content-value gap independent of the duplicate-pair issue above.

## 3. Orphaned pages

13 non-indexed articles have **zero contextual inbound links** from other articles — the only thing linking to them is the `/blog/` index card. Full list is in the table (§5), flagged as "near-orphan." Some of these (e.g. `iptv-turk.html`, `xciptv.html`, `iptv-rtl.html`) don't have an overlap problem — they're simply not woven into the site's internal-linking structure, which is a legitimate, safe thing to fix with a couple of contextual links each.

## 4. Titles/meta — minor, not indexing-blocking

A handful of titles run 70–83 characters (e.g. `iptv-test.html` at 83, `iptvnator.html` at 80, `public-iptv-playlist.html` at 80) and will likely get truncated in the search snippet. This is a CTR/appearance issue, not an indexing blocker, so it's listed for awareness but not prioritized above the structural issues.

## 5. Full table — all 35 non-indexed URLs

The homepage (`/`), `/blog/`, and a stale `http://bestiptvtoday.com/` crawl (pre-dating the `www`/redirect fixes) make up 3 of the 35 and aren't "content" in the sense this audit covers — they should simply be picked up cleanly on Google's next recrawl now that the technical fixes are live. The other 32 are blog articles, detailed below.

| URL | Intent/keyword | Title | Words | Similar/overlapping pages | Inbound contextual links | Content concerns | Recommended action | Priority |
|---|---|---|---|---|---|---|---|---|
| /blog/iptv-player-windows-11.html | IPTV player, Windows 11 | Bester IPTV Player Windows 11 – Top 5 Apps 2026 | 551 | iptv-player-windows.html | 1 | near-orphan, overlap | Differentiate from iptv-player-windows.html (make this one Windows-11-specific: new OS features/quirks only) + cross-link both ways | High |
| /blog/iptv-app-smart-tv.html | best IPTV app, Smart TV | Best IPTV App for Smart TV 2025: Samsung, LG & More | 461 | iptv-app.html, beste-iptv-app.html | 3 | overlap | Keep device-specific angle (Smart TV), add 1-2 contextual links to/from the general app-comparison pages with clear differentiation text | Medium |
| /blog/iptv-extreme.html | IPTV Extreme Pro | IPTV Extreme Pro: Test & Einrichtung 2024 | 450 | - | 1 | near-orphan | Add 1-2 contextual inbound links from a related app-review page; otherwise low-touch | Low |
| /blog/iptv-web-player.html | IPTV web player (browser) | IPTV Web Player – IPTV direkt im Browser 2026 | 417 | - | 1 | thin, near-orphan | Expand slightly + add contextual inbound link; low priority | Low |
| /blog/dazn-vs-iptv.html | DAZN vs IPTV | DAZN vs IPTV 2024: Was ist besser für Sportfans? | 547 | - | 2 | none major | No content issue found; likely just awaiting recrawl | Low |
| /blog/iptv-smarters-pro-apk.html | IPTV Smarters Pro APK | IPTV Smarters Pro APK Download 2026 – Anleitung & Setup | 611 | iptv-smarters-pro.html, iptv-apk.html | 1 | near-orphan, overlap | Add unique value beyond download steps (safety/legality note, version differences) + link to/from iptv-smarters-pro.html with clear differentiation | High |
| /blog/iptvnator.html | IPTVnator player | IPTVNator: Kostenloser IPTV Player für Windows, Mac & Linux 2024 | 551 | - | 3 | none major | No major issue; monitor after recrawl | Low |
| /blog/m3u-iptv.html | M3U playlist, what is it | M3U IPTV Playlist: Was ist das & wie nutzt du sie? 2024 | 617 | what-is-m3u-iptv.html, m3u-playlist-iptv.html | 5 | overlap | This is the German original; keep as-is, just ensure it cross-links to the English pages as "related" not duplicate | Medium |
| /blog/tivimate-premium-apk.html | TiviMate Premium APK | TiviMate Premium APK Guide: Download & Install 2025 | 522 | tivimate.html, tivimate-setup.html, tivimate-premium-features.html | 2 | overlap | Add unique value (what Premium unlocks vs free, pricing caveats) not covered by tivimate-premium-features.html; link between them with distinct angles | High |
| /blog/what-is-m3u-iptv.html | what is M3U IPTV (beginner) | What is M3U IPTV? Beginner's Guide 2025 | 568 | m3u-playlist-iptv.html, m3u-iptv.html | 4 | overlap | Sharpen this one to a pure beginner-explainer angle, leave practical/technical steps to m3u-playlist-iptv.html, cross-link | High |
| /blog/public-iptv-playlist.html | free public M3U playlists | Kostenlose IPTV Playlists 2024: Public M3U Listen & ihre Grenzen | 610 | m3u-iptv.html, what-is-m3u-iptv.html | 1 | near-orphan, overlap | Distinct intent (free/public lists + legal risk) is legitimate; just add contextual inbound links from the M3U explainer pages | Medium |
| /blog/ss-iptv-tutorial.html | SS IPTV app, Samsung setup | SS IPTV Tutorial: Full Setup Guide for Samsung Smart TV 2025 | 500 | smart-iptv.html, smartiptv-activation-guide.html | 5 | overlap | Different app (SS IPTV vs "Smart IPTV") but same device/intent cluster; add clarifying cross-links so Google/users don't conflate the two apps | Medium |
| /blog/net-iptv.html | NET IPTV, LG Smart TV | NET IPTV für LG Smart TV: Test & Einrichtung 2024 | 646 | - | 3 | none major | No major issue; monitor after recrawl | Low |
| /blog/flix-iptv.html | Flix IPTV, Samsung/LG | Flix IPTV: Test & Einrichtung für Samsung & LG 2024 | 607 | - | 2 | none major | No major issue; monitor after recrawl | Low |
| /blog/iptv-player-windows.html | IPTV player, Windows/PC | IPTV Player Windows 2024: Die besten Programme für PC | 581 | iptv-player-windows-11.html | 2 | overlap | Keep as the general/legacy-Windows pillar; add an explicit "if you're on Windows 11 see our dedicated guide" link | High |
| /blog/iptv-deutschland.html | IPTV Deutschland, general overview | IPTV Deutschland 2024: Alles was du wissen musst | 671 | iptv-anbieter.html | 1 | near-orphan, overlap | Keep as the broad intro/pillar page; add clear internal link to iptv-anbieter.html for "best providers" instead of re-covering that ground here | High |
| /blog/iptv-anbieter.html | beste IPTV Anbieter, Deutschland | Beste IPTV Anbieter 2024: Großer Vergleich für Deutschland | 530 | iptv-deutschland.html | 6 | overlap | Keep as the dedicated "providers comparison" page; make the differentiation from iptv-deutschland.html explicit in the intro | High |
| /blog/iptv-app.html | beste IPTV Apps, all devices | Beste IPTV Apps 2024: Großer Vergleich für alle Geräte | 540 | beste-iptv-app.html, iptv-app-smart-tv.html | 6 | overlap | Highest-overlap pair with beste-iptv-app.html (near-identical German title+intent). Reposition this as the broad "all devices" comparison; push app-specific depth to the other two | High |
| /blog/beste-iptv-app.html | beste IPTV App, Deutschland | Beste IPTV App Deutschland 2026 – Top Apps im Vergleich | 428 | iptv-app.html, iptv-app-smart-tv.html | 1 | thin, near-orphan, overlap | Thinnest, most orphaned, most duplicated page in this cluster. Sharpen unique angle or expand with genuinely new content; add internal links | High |
| /blog/iptv-one.html | IPTV One, review | IPTV One – Review, Setup & Erfahrungen 2026 | 401 | - | 1 | thin, near-orphan | Thin + orphaned; add 1-2 contextual inbound links; low priority otherwise | Low |
| /blog/iptv-smarters-pro.html | IPTV Smarters Pro, setup | IPTV Smarters Pro: Vollständige Einrichtungsanleitung 2024 | 824 | iptv-smarters-pro-apk.html | 9 | overlap | Already the stronger/longer page — just ensure it links to the APK page for "where to download" rather than duplicating that content | Medium |
| /blog/iptv-apk.html | IPTV APK download, Android | IPTV APK Download 2026 – Beste IPTV Apps für Android | 380 | iptv-smarters-pro-apk.html, tivimate-premium-apk.html | 1 | thin, near-orphan, overlap | Reposition as an overview/comparison of APK options linking to the specific app pages, rather than a third similar download page | High |
| /blog/smart-iptv-aktivieren.html | Smart IPTV aktivieren (DE) | Smart IPTV aktivieren – Samsung & LG Smart TV Anleitung 2026 | 316 | smart-iptv.html, smartiptv-activation-guide.html | 1 | thin, near-orphan, overlap | Thinnest page on the site. Either substantially expand with unique activation-code/troubleshooting detail, or scope it down to "activation steps only" with a link to the full guide | High |
| /blog/iptv-turk.html | türkisches IPTV, Anbieter | Türkisches IPTV 2026 – Beste türkische IPTV Anbieter | 449 | - | 1 | thin, near-orphan | Thin + orphaned; add contextual inbound link; low priority otherwise | Low |
| /blog/xciptv.html | XCIPTV player | XC IPTV Player – Setup & Review 2026 | 569 | - | 1 | near-orphan | Orphaned; add 1 contextual inbound link; low priority otherwise | Low |
| /blog/iptv-fussball.html | IPTV Bundesliga/Fußball | IPTV Fußball: Bundesliga & Champions League live streamen 2024 | 701 | - | 2 | none major | No major issue; monitor after recrawl | Low |
| /blog/iptv-rtl.html | IPTV RTL/RTL2/Vox | IPTV RTL Live Stream 2026: RTL, RTL2 & Vox kostenlos schauen | 587 | - | 1 | near-orphan | Orphaned; add 1 contextual inbound link; low priority otherwise | Low |
| /blog/smart-iptv.html | Smart IPTV App, Samsung/LG (DE) | Smart IPTV App für Samsung & LG Smart TV einrichten 2024 | 592 | smart-iptv-aktivieren.html, smartiptv-activation-guide.html | 3 | overlap | Stronger/longer of the two German pages; keep as the primary guide and link to -aktivieren.html only for the narrow "activation code" step | High |
| /blog/iptv-firestick.html | IPTV auf Firestick (DE) | IPTV auf Firestick einrichten 2024: Vollständige Anleitung | 632 | fire-tv-stick-iptv.html, install-tivimate-firestick.html | 6 | overlap | Different language from its English sibling (lower risk) but same device; add a clear cross-link | Medium |
| /blog/iptv-test.html | IPTV kostenlos testen | IPTV kostenlos testen 2024: So bekommst du einen Gratis-Testaccount | 594 | iptv-kaufen.html, iptv-legal.html | 6 | overlap | Legitimate distinct intent (free trial) in a natural 3-page decision cluster; strengthen cross-links between all three | Medium |
| /blog/iptv-legal.html | ist IPTV legal, Deutschland | Ist IPTV legal in Deutschland? Die Wahrheit 2024 | 651 | iptv-kaufen.html, iptv-test.html | 4 | overlap | Legitimate distinct intent (legality); strengthen cross-links within the decision cluster | Medium |
| /blog/iptv-kaufen.html | IPTV kaufen, Leitfaden | IPTV kaufen 2024: Der ultimative Leitfaden für Deutschland | 907 | iptv-legal.html, iptv-test.html | 6 | overlap | Legitimate distinct intent (buying guide), already the longest/best-linked of the three; strengthen cross-links | Medium |

## 6. What this audit is *not* claiming

- It is not claiming that fixing any of the above guarantees indexing. Google's own authority/demand model for German-language content on this site (§1) is outside anything on-page work can control.
- It is not claiming word count is the problem — it demonstrably isn't (§1).
- It is not recommending `hreflang` (§1), merges, redirects, noindex, or deletions anywhere.

## 7. The 5–10 highest-impact pages to touch first

Picked for the combination of (a) real overlap with a sibling page, (b) both/weaker member currently non-indexed, and (c) a concrete, safe, non-destructive fix available:

1. **`beste-iptv-app.html` + `iptv-app.html`** — the site's clearest same-language duplicate pair; both non-indexed.
2. **`smart-iptv-aktivieren.html` + `smart-iptv.html`** — second-clearest duplicate pair; `-aktivieren.html` is also the thinnest page on the site; both non-indexed.
3. **`iptv-player-windows-11.html` + `iptv-player-windows.html`** — same topic split only by OS version; both non-indexed.
4. **`iptv-anbieter.html` + `iptv-deutschland.html`** — biggest German pillar pair; both non-indexed, needs explicit differentiation.
5. **`what-is-m3u-iptv.html`** (+ light-touch note added to `m3u-playlist-iptv.html`) — the one same-language English overlap pair.
6. **`iptv-apk.html`, `iptv-smarters-pro-apk.html`, `tivimate-premium-apk.html`** — the sitewide "thin APK download page" pattern, all three non-indexed.

That's 10 pages across 6 logical groups. All changes below are: sharper intros/differentiation, added FAQ or unique-value sections where genuinely useful, and new contextual internal links — never merges, deletions, redirects, or noindex, and never touching the site's existing language or factual claims.

## 8. Explicitly recommended NOT to touch

- IBO Player cluster (`ibo-player.html`, `iboplayer-setup.html`) — already well-differentiated and both indexed.
- TiviMate cluster's 4 already-indexed pages (`tivimate.html`, `tivimate-setup.html`, `tivimate-premium-features.html`, `install-tivimate-firestick.html`) — working as intended.
- The IPTV kaufen/legal/test decision cluster's core content — intent is legitimate and distinct; only the cross-linking needs strengthening, not the articles themselves.
- Any merge of German and English near-pairs into one page — that would eliminate legitimate language-targeted content, not fix a duplication problem.
- Adding `hreflang` — would misrepresent unrelated articles as translations of each other.
- Mass-rewriting all 61 articles, or any article not listed above — not justified by this data.
