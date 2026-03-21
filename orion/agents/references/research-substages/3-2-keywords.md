# Substage 3.2 — Keyword Research & Opportunity Analysis

**Code:** R2
**Slug:** Keywords
**Output:** `research/R2-Keywords.txt`
**Hypothesis:** Untapped keyword opportunities exist in the client's service categories
**Dependencies:** R1-SERP
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`
**MCP tools:** DataForSEO (required)

---

## Purpose

Expand R1's seed keywords into the full keyword landscape, cluster them into page-level targets based on SERP overlap, score each cluster by feasibility and value, and produce a prioritised list of page recommendations that feeds directly into Concept Creation.

**R1 mapped the battlefield. R2 plans the attack — which positions to take, in what order, and why.**

## R1 Carry-Forward

R1 already provides seed keywords with volume, intent, client positions, competitor domains, and SERP composition. Before calling any API, read R1-SERP.txt fully and assess what's already available. Skip or reduce any step where R1 data is sufficient. Specifically:

- If R1 includes client rankings per keyword → use as baseline instead of re-fetching in Step 0
- If R1 volume and intent data covers the seed list → skip re-enrichment for those keywords
- If R1 competitor list is already typed and ranked → use directly in Step 1A without re-fetching

The agent decides what to skip based on R1 completeness. Document skipped steps and reasoning in the output.

## Minimum Scope

Cover at least these items. You may go beyond them if evidence warrants it.

- Client keyword baseline — what the client currently ranks for (position, URL, volume), or confirmation of zero presence for new builds
- Keyword discovery from three streams — competitor gap extraction, seed expansion via DataForSEO, agent-generated semantic candidates validated against real volume
- Deduplication and enrichment — every keyword carries: volume, difficulty, CPC, intent, source stream, client position (or null)
- Opportunity classification per keyword — NOT_TARGETED (no ranking), UNDERPERFORMING (pos 11+), COMPETITIVE (top 10 but below best competitor), OWNED (top 3 and above competitors)
- Keyword clusters — keywords grouped by SERP overlap into page-level targets. Each cluster = one page on the future website
- Cluster enrichment — per cluster: primary keyword, cluster volume, average difficulty, dominant intent, opportunity classification, SERP composition (who ranks, what features appear)
- Opportunity scoring — Keyword Opportunity Score (KOS) per cluster using the weighted formula below
- Page type recommendation — each cluster mapped to: core service page, supporting content, local variation, comparison page, or aspirational target
- Competitor anchor — at least one commercial competitor must rank top 10 for a cluster to be classified as actionable. Clusters with only Wikipedia/directories/forums = UNPROVEN
- Verified vs unverified split — keywords with confirmed volume separate from null-volume candidates

## Data Sources

From `project.json`: research config (search_landscape_max_keywords, research_depth), languages, locations, site_type (new vs redesign).
From `baseline-log.txt`: mission, services/products, client URL, all prior findings including R1 highlights.
From `research/R1-SERP.txt`: seed keywords with volume/intent/position, competitor domains (top 10 typed), language x location matrix, SERP composition patterns.

---

## Methodology — Processing Sequence

Seven steps. Each builds on the previous. The agent may compress or skip steps where R1 data already covers the need.

**Step 0 — Client keyword baseline:** Establish what the client already ranks for before discovering new opportunities. Run ranked keywords on the client domain per language x location combination. For new builds (site_type = "new"), this returns minimal or no data — all discovered keywords default to NOT_TARGETED. Skip if R1 already includes comprehensive client rankings.

**Step 1 — Keyword discovery (three streams):** Three independent sources, merged into one deduplicated list.

- **Stream A — Competitor gap extraction:** Pull ranked keywords for top 5 commercial competitors from R1. Identify keywords where competitors rank top 20 and client does not (or ranks below 20). These are highest-signal opportunities — proven demand in the client's exact market. Use domain intersection where available.
- **Stream B — Seed expansion:** Expand R1 seed keywords into long-tail variants. Three passes in order: full-text expansion (keywords containing the seed phrase), related-keyword depth crawl (2 levels of "searches related to"), category-based relevance search (same product/service category, may not contain seed phrase). Batch by semantic group — one call per service/product cluster, not one massive call.
- **Stream C — Agent-generated semantic candidates:** Generate keyword candidates from reasoning about the client's business: service × location modifiers, service × audience segments, service × problem/solution framing, service × comparison modifiers, industry terminology variations. All agent-generated keywords must be validated against DataForSEO for volume and difficulty before inclusion.

**Step 2 — Deduplication and enrichment:** Merge all streams. Remove exact duplicates. Ensure every keyword carries: keyword, volume, difficulty, CPC, competition level, intent, source stream, client position (from Step 0 or null). Tag source correctly: `seed` (from R1), `expanded` (from Stream B), `gap_opportunity` (from Stream A), `agent_generated` (from Stream C). Fill missing data points via bulk intent classification and bulk difficulty scoring.

**Step 3 — Opportunity classification:** Using the client baseline from Step 0, classify each keyword: NOT_TARGETED (no ranking), UNDERPERFORMING (pos 11+), COMPETITIVE (top 10 but below best competitor), OWNED (top 3 and above — not an opportunity, skip). For new builds, all keywords = NOT_TARGETED.

**Step 4 — Clustering (two-pass):** Group keywords that Google treats as the same search intent. Each cluster = one page.

- **Pass 1 — Core keyword grouping (fast, free):** Group by the `core_keyword` property that DataForSEO returns with every keyword response. Handles singular/plural, word order, minor phrasing differences. No extra API calls. Result: initial cluster draft, ~70-80% accuracy.
- **Pass 2 — SERP overlap validation (accurate, costs API calls):** For the top 30-50 highest-value clusters from Pass 1 (ranked by combined volume), run SERP queries and compare top 10 organic URLs between keyword pairs. Threshold: 3+ shared URLs in top 10 = same cluster. 0-2 shared = split. Two clusters from Pass 1 showing high mutual overlap = merge.

Why two passes: full SERP-based clustering for 500 keywords = 500 API calls + O(n²) comparisons. Two-pass limits expensive SERP calls to the clusters that will actually become pages.

**Step 5 — Cluster enrichment:** Each validated cluster gets: primary keyword (highest volume), cluster intent (majority vote — flag mixed-intent clusters for potential split), cluster volume (sum of all keyword volumes), average difficulty, opportunity classification (majority of keywords: NEW_PAGE / OPTIMIZE / COMPETE), SERP composition (which competitors rank + average position, whether directories/Wikipedia/forums dominate, which SERP features appear).

**Step 6 — Scoring and page type recommendation:** Score each cluster using KOS (see formula below). Then map to page type: core service/product pages (commercial/transactional, aligned with client services), supporting content (informational, builds topical authority), local/regional variations (same topic, location-specific), comparison/alternative pages ("[service] vs [alternative]", high conversion), aspirational targets (high-value but fierce competition — flag as requiring pillar-page strategy).

**Step 7 — Capping and split:** Respect `research_config.search_landscape_max_keywords` as the verified keyword cap. Split output into verified (volume > 0) and unverified (null volume). Unverified go to a separate section — group by service area, note validation suggestions (paid social test, content experiment).

---

## Opportunity Scoring — KOS Formula

```
KOS = (V × 0.15) + (I × 0.20) + (D × 0.20) + (G × 0.20) + (F × 0.25)
```

| Factor | Weight | Measures | Scoring |
|---|---|---|---|
| V — Volume | 15% | Combined cluster search volume | Normalised against other clusters |
| I — Intent | 20% | Commercial/transactional alignment | Transactional 1.0, Commercial 0.8, Informational 0.4, Navigational 0.1 |
| D — Difficulty | 20% | Inverse competitive difficulty | 0-30 = 1.0, 31-50 = 0.7, 51-70 = 0.4, 71-100 = 0.1 |
| G — Gap | 20% | Competitor presence where client is absent | 3+ competitors rank, client doesn't = 1.0. Fewer or client present = lower |
| F — Feasibility | 25% | How quickly results can be achieved | OPTIMIZE 1.0, COMPETE 0.7, NEW_PAGE low-diff 0.5, NEW_PAGE high-diff 0.2 |

**Feasibility gets highest weight (25%)** — this is a website proposal. Clients need achievable results. A keyword with amazing volume is worthless if it requires 18 months of link building.

**Volume gets lowest weight (15%)** — high-volume keywords are often high-difficulty and informational. Chasing volume leads to proposals full of blog post recommendations instead of revenue-driving service pages.

---

## Tooling

**DataForSEO — primary tool:**
- Ranked keywords per domain — client baseline (Step 0) and competitor keyword extraction (Step 1A). Returns keywords, positions, URLs, volume, difficulty, intent.
- Domain intersection — gap identification between client and competitors (Step 1A).
- Keyword suggestions, related keywords, keyword ideas — seed expansion streams (Step 1B). Each returns volume, difficulty, and core_keyword clustering signal.
- Keyword overview (bulk) — validate agent-generated candidates, up to 700 per call (Step 1C).
- Search intent (bulk) — classify intent for up to 1,000 keywords per call (Step 2).
- Bulk keyword difficulty — difficulty for up to 1,000 keywords per call (Step 2).
- SERP organic results — top 10 URLs per keyword for cluster validation (Step 4, Pass 2).

**Estimated API calls per project:** 30-80 depending on keyword volume and competitor count. Main cost driver is Step 4 SERP validation — limit to top 30-50 clusters.

---

## Output

Write `research/R2-Keywords.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R2]`.

**What R2 feeds downstream:**
- Keyword clusters with page type recommendations → Concept Creation sitemap (C1)
- Enriched competitor domain list (R1 appearances + R2 domain intersection + R2 competitor discovery) → R3-Competitors
- Opportunity scores → Concept Creation prioritisation (C7-Roadmap)
- Intent classification per cluster → Concept Creation page type mapping (C1)
- Gap analysis → R3-Competitors (which competitors own which clusters)
- Verified vs unverified split → R9-Content (content experiment candidates)
