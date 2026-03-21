# Substage 3.0 — Client Website Inventory

**Code:** R0
**Slug:** Inventory
**Output:** `research/R0-Inventory.txt`
**Hypothesis:** The client's site structure does not reflect the full range of services they offer
**Dependencies:** none (first substage)
**Reads from:** `project.json`, `baseline-log.txt`
**MCP tools:** DataForSEO (optional), web-crawler (required)
**Skip condition:** If `project.json → site_type = "new"` (no existing website), skip entirely. All downstream stages handle the new-build case by defaulting to empty client baselines.

---

## Purpose

Crawl the client's existing website to produce a complete page inventory with basic on-page data. This is not an analysis or audit — it is a factual baseline that every subsequent research substage references. It answers "what exists right now" so that no downstream stage has to guess or re-discover this information.

**This substage produces no recommendations, no gap analysis, no quality judgments. It is a neutral inventory. Interpretation happens in later stages.**

## Minimum Scope

Cover at least these items. You may go beyond them if evidence warrants it.

- Full page inventory — every publicly accessible HTML page with: URL, URL depth (clicks from homepage), language version, page type classification (homepage, service, product, category, about, contact, blog post, blog listing, case study, portfolio item, FAQ, legal/policy, landing page, other)
- Meta information per page — meta title (text + char count), meta description (text + char count), canonical URL (self-referencing or pointing elsewhere), robots directive (index/noindex, follow/nofollow)
- Heading structure per page — H1 text (flag if missing, duplicate, or multiple), H2 list (reveals content structure at a glance), heading hierarchy health (logical H1→H2→H3 or broken)
- Content signals per page (lightweight) — approximate word count (body text, excluding nav/footer), image count, video presence (yes/no), structured data/schema markup (type if present), internal links count, incoming internal links count
- Page status — HTTP status code, in sitemap.xml (yes/no), in main navigation (yes/no)
- Site structure summary — page count by type, language coverage and translation gaps (multi-language), depth distribution, orphan pages (zero incoming internal links), deeply buried pages (4+ clicks), navigation coverage (nav vs link-only vs sitemap-only)
- On-page health flags — missing meta titles, missing meta descriptions, missing/duplicate H1s, broken heading hierarchy, very thin content (<100 words), noindex on pages that probably shouldn't be, duplicate meta titles across pages. Flagged only, not analysed
- Service/product page mapping — each service/product from baseline-log.txt mapped to its dedicated page (or noted as missing/partial), with URL, H1, word count, and navigation status

## Data Sources

From `project.json`: site type, languages, locations.
From `baseline-log.txt`: mission, client URL, services/products list from D2.

---

## Methodology — Processing Sequence

Four steps. Step 1 discovers all pages. Step 2 extracts per-page data. Step 3 compiles the structural overview. Step 4 maps services to pages.

**Step 1 — Full site crawl:** Before crawling, check the site root for sitemap files: `/sitemap.xml`, `/sitemap_index.xml`, `/sitemap.xml.gz`, and any sitemap references in `/robots.txt`. If a sitemap exists, fetch and parse it first to get the full URL list — faster and more reliable than crawl-only discovery for sites with clean sitemaps. Then crawl from the homepage following all internal links to catch pages not in the sitemap.

Crawl boundaries: internal links only (no external domains), respect robots.txt, capture all HTML pages (log PDFs/images/non-HTML but don't analyse), crawl all language versions for multi-language sites (flag language per page), maximum depth 5 levels (pages beyond flagged as deeply buried).

**Step 2 — Per-page data extraction:** For every discovered page, extract: URL and depth, language version, page type classification (agent classifies based on URL pattern, content, and position in site hierarchy), meta title and description (text + char count), canonical URL, robots directive, H1 text (flag anomalies), H2 list, heading hierarchy assessment, approximate word count, image count, video presence, structured data type, internal links out, internal links in, HTTP status, sitemap presence, navigation presence.

Use on-page analysis tools where available for efficient bulk extraction. Fallback: dispatch web-crawler per page for sites where bulk crawl tools are unavailable.

**Step 3 — Site structure summary:** From per-page data, compile: total page count and breakdown by type, language coverage with translation gaps (pages in one language but not another), depth distribution (pages per level), orphan pages (exist but nothing links to them), deeply buried pages (4+ clicks from homepage), navigation coverage (nav pages vs link-only vs sitemap-only), common on-page issues flagged (missing meta, missing H1, broken hierarchy, thin content, suspicious noindex, duplicate titles).

**Step 4 — Service/product page mapping:** For each service/product identified in baseline-log.txt (from D2), check whether the site has a dedicated page. Produce the mapping: service name → dedicated page (yes/no/partial) → URL → H1 → word count → in main nav. This immediately reveals: services with no page (content gap R2 will find keywords for), services with thin pages (optimisation opportunity), services not in navigation (visibility gap).

---

## Tooling

**Web-crawler — primary tool:**
- Full site crawl from homepage. Follow internal links, extract page-level data. Dispatch for sitemap.xml discovery and parsing.

**DataForSEO — bulk extraction (optional):**
- On-page instant analysis for bulk per-page data extraction (meta, headings, word count, structured data, internal links). More efficient than per-page crawling for larger sites.

---

## Output

Write `research/R0-Inventory.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R0]`.

**What R0 feeds downstream:**
- Service/product mapping → R1-SERP (informs keyword generation — knows which services have pages vs which don't)
- Full page inventory with URLs → R2-Keywords (Step 0 cross-references ranked_keywords against actual pages — NOT_TARGETED means no page exists, UNDERPERFORMING means page exists but ranks poorly)
- Service/product mapping → R3-Competitors (competitor service overlap grounded in what client actually has pages for)
- Page type breakdown → R4-Market (knows whether client has functionality pages the market expects)
- Site structure → R5-Audience (can the primary persona actually find what they need)
- Trust signal pages → R6-Reputation (knows whether case study, testimonial, about/team pages exist)
- Page list + depth data → R7-Technology (selects subpages for Lighthouse analysis intelligently)
- Full structure + navigation → R8-UX (evaluates IA against actual page set, not assumptions)
- Full inventory with meta/H1s/word counts/headings → R9-Content (complete baseline for content analysis, cluster-to-content map references real client URLs)
- Page disposition signals (thin, orphan, missing) → Concept Creation (plans migration — which pages to keep, rewrite, merge, redirect, or drop)
