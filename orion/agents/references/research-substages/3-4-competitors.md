# Substage 3.4 — Competitor Landscape

**Code:** R4
**Slug:** Competitors
**Output:** `research/R4-Competitors.txt`
**Hypothesis:** Competitors have stronger web presence and working conversion paths
**Dependencies:** R2-SERP, R3-Keywords
**Reads from:** `project.json`, `baseline-log.txt`, `research/R2-SERP.txt`, `research/R3-Keywords.txt`
**MCP tools:** DataForSEO (required), web-crawler (required)

---

## Purpose

Consolidate all competitor signals from R2 and R3, select the final competitor roster organised by competitive zones, profile each competitor at the business and SEO authority level, and produce the overlap matrix that every downstream stage references.

**This is a profile-and-lock stage — it answers "who and how big," not "how do they do it." Deep analysis of competitors' technology, reputation, UX, and content belongs in later stages.**

## R2/R3 Carry-Forward

R2 provides: commercial competitor domains with SERP appearance counts, local appearances, scope classification, and domain typing. R3 provides: keyword clusters with competitor rankings per cluster, domain intersection data, gap analysis, page type recommendations. Before calling any API, read both R-files fully and assess what's reusable. Specifically:

- R2's competitor frequency table → direct input to Step 2 selection criteria
- R3's cluster-level competitor rankings → direct input to Step 1 zone definition and Step 5 overlap matrix
- R3's domain intersection data → reuse for overlap matrix instead of re-fetching
- R3's competitor keyword extraction → reuse for authority profile keyword counts

Document what data was carried forward and what required new API calls.

## Minimum Scope

Cover at least these items. You may go beyond them if evidence warrants it.

- Competitive zones — defined by service category × market (location + language), derived from R3's keyword clusters. Each zone groups the clusters where a distinct set of competitors emerges
- Competitor roster — deduplicated list of all unique commercial competitor domains across all zones. Maximum 15 unique competitors. Each domain typed and tagged with which zones it appears in
- Business profile per competitor — company name, positioning statement, services offered (mapped against client's services), markets served, apparent company size, unique selling proposition, pricing signals, primary CTA. From homepage + about page + services pages only
- SEO authority profile per competitor — domain rank, total ranked keywords, estimated organic traffic, keyword position distribution (top 3/10/20/50), backlink summary (total backlinks, referring domains), top 5-10 performing pages by traffic
- Competitive overlap matrix per zone — keyword clusters × competitors showing positions. Highlights convergence (proven demand) and whitespace (uncontested clusters)
- Tier classification per zone — each competitor classified as direct threat (high overlap, similar services, comparable authority), aspirational benchmark (much stronger, learning target), or niche competitor (lower authority, dominant in specific cluster)
- Multi-zone threats — competitors appearing in 3+ zones flagged separately as primary strategic threats regardless of per-zone tier

## Data Sources

From `project.json`: languages, locations, notes (client-provided competitor URLs), research config (competitors_max).
From `baseline-log.txt`: mission, services/products, all prior findings including R2 and R3 highlights.
From `research/R2-SERP.txt`: commercial competitor domains with appearance counts, local appearances, scope, domain typing.
From `research/R3-Keywords.txt`: keyword clusters with competitor rankings, domain intersection data, gap analysis, page type recommendations, service mappings.

---

## Methodology — Processing Sequence

Six steps. Steps 1-2 define who to analyse. Steps 3-4 profile each competitor. Steps 5-6 build the cross-reference outputs.

**Crawl cache:** Before dispatching web-crawler for any competitor URL, check `tmp/competitors/{domain-slug}/` for an existing snapshot. If a `.txt` file exists for that page, read from cache instead of re-crawling. After crawling any new page, save the extracted content to `tmp/competitors/{domain-slug}/{page-slug}.txt`. This avoids redundant crawls — pages cached by earlier stages are reused.

**Step 1 — Define competitive zones:** A zone is the intersection of service category × market (location + language). Zones are not invented — they emerge from R3's cluster data. Each keyword cluster already has a service mapping, location, and language from R3. Group clusters by service × market to define zones. Rank zones by combined cluster volume from R3. Zones in the bottom quartile by volume may be deprioritised — flagged but not given full competitor analysis.

**Step 2 — Select competitors per zone:** Input: all commercial domains from R2 (SERP frequency) and R3 (keyword gap, cluster SERP composition). Only domains typed as `commercial` in R2 are eligible. Select top 3-5 per zone by: keyword overlap (how many zone clusters does this competitor rank for), SERP frequency (R2 appearances for this zone's keywords), service overlap (does the competitor actually offer the same services), comparable scale (favour competitors of similar or slightly higher authority over massive multinationals). Compile the full roster — all unique competitors across all zones. Cap at 15 unique domains. If the zone map produces more, drop the weakest single-zone competitors that don't add unique insight. Also produce the zone map showing which competitors appear in which zones. Multi-zone competitors (3+ zones) are typically the most important — they're the client's truest direct threats.

**Step 3 — Business profile per competitor:** Done once per unique competitor in the roster. Dispatch web-crawler sub-agent for each competitor's homepage, about page, and services pages. Extract: company name, positioning statement (hero section or meta description), services offered (mapped against client's services — flag overlap and gaps), markets served (locations, languages, verticals), apparent company size (team page signals, years in business), unique selling proposition (what they lead with), pricing signals (visible prices, "request a quote", package tiers, or "not public"), primary CTA (what action the website pushes). This is lightweight scraping — homepage + about + services only. If a page beyond these three is needed, it belongs in a later stage.

**Step 4 — SEO authority profile per competitor:** Done once per unique competitor. Pull from DataForSEO: domain rank/authority score, total ranked keywords in target market, estimated monthly organic traffic, keyword position distribution (how many in top 3/10/20/50), backlink summary (total backlinks, referring domains — not a full audit, just the authority gap picture), top 5-10 pages by estimated traffic (reveals content strategy shape without a full content analysis). Reuse R3's ranked_keywords and domain intersection data where available — the main new calls are domain rank overview, relevant pages, and backlink summary.

**Step 5 — Competitive overlap matrix:** The key output. Per zone: build a table of keyword clusters × competitors showing positions. From R3's cluster data and Step 4 rankings. Highlight: convergence points (multiple competitors rank for the same cluster = proven demand, client must be there), single-competitor clusters (niche strength or unique positioning angle), zero-competitor clusters (whitespace opportunities already flagged in R3). This matrix directly feeds the proposal's competitive positioning argument.

**Step 6 — Tier classification:** Done per zone, not globally. Same competitor may be classified differently across zones. Direct threat: high keyword overlap, similar services, comparable or stronger authority. Aspirational benchmark: much stronger authority, broader market, but overlapping on key clusters — study for best practices, don't set unrealistic expectations. Niche competitor: lower authority overall but dominant in a specific cluster — quick wins for the proposal. Flag multi-zone competitors (3+ zones) separately as primary strategic threats regardless of per-zone tier.

---

## Scope Boundaries

**What R4 does:** Define zones, select roster, profile business + SEO authority, build overlap matrix, classify tiers.

**What R4 does NOT do:**
- Crawl competitor sites for tech stack → R8-Technology
- Analyse reviews or social proof → R7-Reputation
- Evaluate design patterns, navigation, conversion flows → R9-UX
- Perform deep content audits or topical coverage analysis → R10-Content
- Build audience personas → R6-Audience

**Boundary rule:** If it requires visiting the competitor's website page-by-page beyond homepage, about page, and services pages, it belongs in a later stage.

---

## Tooling

**DataForSEO — authority profiling:**
- Domain rank overview — authority score, traffic estimate, keyword counts per competitor. One call per competitor.
- Bulk traffic estimation — traffic estimates for all competitors in one call.
- Relevant pages — top performing pages per competitor. One call per competitor.
- Backlink summary — total backlinks, referring domains. One call per competitor.
- Ranked keywords — position distribution per competitor. Reuse from R3 where available.
- Domain intersection — keyword overlap. Reuse from R3 where available.

**Web-crawler — business profiling:**
- Dispatch per competitor for homepage + about + services pages. Lightweight scrape for business profile data points.

**Estimated API calls per project:** 15-30 new calls depending on roster size. Steps 5-6 primarily reuse data from R2 and R3.

---

## Output

Write `research/R4-Competitors.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R4]`.

**The competitor list is now locked. No new competitors are added after this point.**

This is the reference file for all substages R5 through R10. Later stages use the roster, zone map, and tier classifications to scope their own analysis.

**What R4 feeds downstream:**
- Locked competitor roster + zone map → R5-Market, R6-Audience, R7-Reputation, R8-Technology, R9-UX, R10-Content
- SEO authority profiles → R8-Technology (benchmark), Concept Creation (realistic targets)
- Overlap matrix → Concept Creation sitemap (which clusters must have pages), Proposal (competitive positioning argument)
- Tier classifications → Concept Creation (priority ordering), Proposal (competitive narrative)
- Top performing pages per competitor → R10-Content (content strategy shape)
- Business profiles → R9-UX (context for navigation/CTA analysis), Proposal (competitive landscape section)
