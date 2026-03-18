# Substage 3.2 — Keyword Opportunity

**Code:** R2
**Slug:** Keywords
**Output:** `research/R2-Keywords.txt`
**Hypothesis:** Untapped keyword opportunities exist in the client's service categories
**Dependencies:** R1-SERP
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`
**MCP tools:** DataForSEO (required)

---

## Purpose

Take the seed keyword list from R1-SERP and expand, enrich, and analyse it. Add real search volume and keyword difficulty data, identify trend momentum, surface competitor keyword gaps, and produce the final prioritised keyword list organised by page intent. This is the definitive keyword reference for all downstream phases.

---

## Data Sources

From `project.json`: research config (search_landscape_max_keywords, research_depth), languages, location.
From `baseline-log.txt`: mission, all prior findings including R1 highlights.
From `research/R1-SERP.txt`: seed keywords, client rankings, competitor domains, language x location matrix.

---

## Methodology

### Step 1: Keyword expansion

Cast a wide net, then keep only the traffic-driving, service-relevant, location-relevant winners.

Even in small markets (e.g., Slovakia), there are always keywords that drive real traffic — the job is to find them. Low absolute volume is fine if the keyword is high-intent and service-relevant. Zero volume is not — drop it.

Call `dataforseo_labs_google_keyword_ideas` and `dataforseo_labs_google_related_keywords` on the seed keywords from R1-SERP. Set `limit: 200` per call to ensure broad expansion. Run per language x location combination from the matrix.

**Multi-seed batching:** Do not pass all seeds in a single call — batch by semantic group (e.g., one call per service/product cluster of related seeds). This produces more diverse results than one large batch.

Deduplicate against existing keywords. **Relevance filter** (apply in this order):
1. **Service match** — keyword must describe a service the client actually delivers or a direct query about hiring/booking that service. Off-topic keywords about adjacent industries or services the client does not offer are dropped (e.g., "svadobný darček" for a photographer).
2. **Traffic potential** — keyword must have non-zero search volume. Prioritise keywords that actually drive clicks and traffic over vanity terms.
3. **Location relevance** — for local/regional businesses, prioritise keywords with location intent or that match the client's service area.

### Step 2: Competitor rankings

Call `dataforseo_labs_google_ranked_keywords` on top 3 commercial competitors from R1-SERP. Returns keywords each competitor ranks for, with positions and traffic share.

Cross-reference against R1 keywords + expanded list. Keywords competitors rank for that are absent from the client's list are flagged as gap opportunities. **Tag source correctly:** keywords from R1 seeds = `seed`, from keyword_ideas/related_keywords = `expanded`, from competitor ranking gaps = `gap_opportunity`.

### Step 3: Domain intersection

Derive keyword overlap from the `dataforseo_labs_google_ranked_keywords` data already obtained in Step 2. Compare keywords across the client domain and each competitor — shared keywords are overlap, keywords only one domain ranks for are unique. No separate API call needed.

### Step 4: Competitor discovery

Call `dataforseo_labs_google_competitors_domain` on the client domain. Surfaces additional competing domains not found in R1 SERP results. Add any net-new commercial competitors to the competitor list.

### Step 5: Difficulty scoring

Extract keyword difficulty from the `dataforseo_labs_google_keyword_ideas` responses obtained in Step 1 — each result includes a difficulty score alongside volume. For any remaining keywords without difficulty data (e.g., from related_keywords), call `dataforseo_labs_google_keyword_ideas` with those keywords as seeds to retrieve difficulty scores.

### Step 6: Trend analysis

Call `kw_data_dfs_trends_explore` on the top 30 keywords by search volume. Classify each as:
- `rising` — growing search interest
- `stable` — consistent search interest
- `declining` — shrinking search interest
- `seasonal` — significant periodic spikes

### Step 7: Split verified vs unverified

After volume enrichment, split keywords into two buckets:

- **Verified** — keywords with `volume > 0` (confirmed traffic). These are the main output.
- **Unverified** — keywords where DataForSEO returned `null` volume. Null means no ads data — not necessarily zero searches, but unproven. These go to a separate `unverified_candidates` section.

Keep unverified keywords separate from verified ones. Pick the best candidates by service relevance and intent strength, group by service area, and note how they might be validated (paid social test, content experiment, etc.).

### Step 8: Prioritisation and capping

Score **verified keywords only**. The goal is to surface keywords that will **drive real traffic to the client's website**:
- High volume + low difficulty + commercial/transactional intent = highest priority
- Service-specific + location-modified keywords rank above generic terms, even at lower volume
- Rising trend boosts priority; declining trend downgrades regardless of volume
- Gap opportunities (competitors rank, client doesn't) get priority boost — these are proven traffic drivers
- Informational keywords retained but ranked lower unless content strategy signals need them

Respect `research_config.search_landscape_max_keywords` as the cap. The final list should represent the best traffic opportunities for the client's services in their market.

### Step 9: Keyword clustering

Group the **verified keyword list** into semantic clusters. Each cluster represents one topic that a single page should target.

Each cluster should identify the primary keyword (highest volume), supporting keywords, suggested page type, and aggregate metrics (volume, difficulty). Drop clusters where zero keywords have verified volume.

Use semantic similarity and SERP overlap to group: if two keywords return largely the same top 10 results, they belong in the same cluster. `dataforseo_labs_google_related_keywords` output from Step 1 informs this grouping. One keyword per cluster.

---

## Output

Write `research/R2-Keywords.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R2]`.

R3 will read your output for: enriched competitor domain list (R1 SERP appearances + R2 domain intersection + R2 competitor discovery), keyword clusters for site architecture planning.
