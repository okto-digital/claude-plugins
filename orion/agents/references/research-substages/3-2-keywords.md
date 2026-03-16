# Substage 3.2 — Keyword Opportunity

**Code:** R2
**Slug:** Keywords
**Output:** `research/R2-Keywords.json`, `research/R2-Keywords.md`
**Dependencies:** R1-SERP
**Reads from:** `D1-Init.json`, `R1-SERP.json`
**MCP tools:** DataForSEO (required)

---

## Purpose

Take the seed keyword list from R1-SERP and expand, enrich, and analyse it. Add real search volume and keyword difficulty data, identify trend momentum, surface competitor keyword gaps, and produce the final prioritised keyword list organised by page intent. This is the definitive keyword reference for all downstream phases.

---

## Data Sources

From `D1-Init.json`:
- `research_config.search_landscape_max_keywords` — hard cap (default: 100)
- `research_config.research_depth` — `basic` enforces cap, `deep` treats it as guideline
- `project.languages` — primary + additional languages
- `project.location` — primary + additional markets

From `R1-SERP.json`:
- `keywords` — seed keyword list with intent and volume estimates
- `client_rankings` — keywords the client already ranks for (baseline)
- `competitors` — commercial competitor domain list
- `meta.language_location_matrix` — search engine settings per language x location

---

## Methodology

### Step 1: Keyword expansion

Call `dataforseo_labs_google_keyword_ideas` and `dataforseo_labs_google_related_keywords` on the seed keywords from R1-SERP. Run per language x location combination from the matrix.

Deduplicate against existing keywords. **Relevance filter:** drop any expanded keyword that does not describe a service the client actually delivers or a direct query about hiring/booking that service. Keywords about adjacent industries or complementary services the client does not offer are off-topic (e.g., "svadobný darček" for a photographer). Add net-new relevant terms to the candidate list.

### Step 2: Competitor rankings

Call `dataforseo_labs_google_ranked_keywords` on top 3 commercial competitors from R1-SERP. Returns keywords each competitor ranks for, with positions and traffic share.

Cross-reference against R1 keywords + expanded list. Keywords competitors rank for that are absent from the client's list are flagged as gap opportunities.

### Step 3: Domain intersection

Derive keyword overlap from the `dataforseo_labs_google_ranked_keywords` data already obtained in Step 2. Compare keywords across the client domain and each competitor — shared keywords are overlap, keywords only one domain ranks for are unique. No separate API call needed.

### Step 4: Competitor discovery

Call `dataforseo_labs_google_competitors_domain` on the client domain. Surfaces additional competing domains not found in R1 SERP results. Add any net-new commercial competitors to the competitor list.

### Step 5: Difficulty scoring

Extract keyword difficulty from the `dataforseo_labs_google_keyword_ideas` responses obtained in Step 1 — each result includes a difficulty score alongside volume. For any remaining keywords without difficulty data (e.g., from related_keywords), call `dataforseo_labs_google_keyword_ideas` with those keywords as seeds to retrieve difficulty scores.

### Step 6: Trend analysis

Call `kw_data_dfs_trends_explore` on the top 20 keywords by search volume. Classify each as:
- `rising` — growing search interest
- `stable` — consistent search interest
- `declining` — shrinking search interest
- `seasonal` — significant periodic spikes

### Step 7: Prioritisation and capping

Score each keyword:
- High volume + low difficulty + commercial/transactional intent = highest priority
- Rising trend boosts priority; declining trend downgrades regardless of volume
- Informational keywords retained but ranked lower unless content strategy signals need them
- Gap opportunities (competitors rank, client doesn't) get priority boost

Trim to `research_config.search_landscape_max_keywords` (default: 100). Log deprioritised keywords in `notes`.

### Step 8: Keyword clustering

Group the final keyword list into semantic clusters. Each cluster represents one topic that a single page should target.

For each cluster:
- **primary_keyword** — the highest-volume keyword in the cluster (the main target)
- **supporting_keywords** — semantically related keywords that belong on the same page
- **page_type** — suggested page type: `homepage`, `service`, `portfolio`, `location`, `blog`, `landing`, `other`
- **total_volume** — sum of all keyword volumes in the cluster
- **avg_difficulty** — average difficulty across cluster keywords

Use semantic similarity and SERP overlap to group: if two keywords return largely the same top 10 results, they belong in the same cluster. `dataforseo_labs_google_related_keywords` output from Step 1 informs this grouping.

One keyword should appear in only one cluster. If a keyword could fit multiple clusters, assign it to the one with the closest semantic match.

---

## Output

Write output using the templates at `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/templates/R2-Keywords-template.md`.

---

## What passes to the next substage

`research/R2-Keywords.json` — R3 reads the enriched competitor domain list (from R1 SERP appearances + R2 domain intersection + R2 competitor discovery) to build the final competitor profile list. The `keyword_clusters` block feeds into Concept Creation (C1-Sitemap) for hub-and-spoke architecture planning.
