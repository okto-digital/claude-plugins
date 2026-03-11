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
- `keywords` — full seed keyword list with intent and volume estimates
- `competitors` — commercial competitor domain list with keyword appearance counts
- `meta.language_location_matrix` — search engine settings per language x location

---

## Methodology

### Step 1: Keyword expansion

Call `dataforseo_labs_keyword_suggestions` on the seed keyword list from R1-SERP. Run per language x location combination from the matrix.

Deduplicate against existing keywords. Add net-new terms to the candidate list.

### Step 2: Volume and difficulty enrichment

Call `kw_data_google_ads_search_volume` on the full expanded keyword list. Returns accurate monthly search volume per keyword per location.

Call `dataforseo_labs_keyword_difficulty` on the full expanded keyword list. Returns keyword difficulty score (0–100) indicating how hard it is to rank organically.

### Step 3: Trend analysis

Call `dataforseo_labs_google_trends` on the top 20 keywords by search volume only. Classify each as:
- `rising` — growing search interest
- `stable` — consistent search interest
- `declining` — shrinking search interest
- `seasonal` — significant periodic spikes

Trend status influences keyword priority — a high-volume declining keyword is deprioritised versus a lower-volume rising one.

### Step 4: Competitor keyword gap analysis

Call `dataforseo_labs_competitors_domain` on the client domain (if exists) and top 3 commercial competitors from R1-SERP.

Call `dataforseo_labs_ranked_keywords` on top 3 commercial competitors. Cross-reference against current keyword list to identify uncovered opportunities.

Produce a gap list — keywords competitors rank for that are not in the client keyword set — flagged as opportunities.

### Step 5: Prioritisation and capping

Score each keyword:
- High volume + low difficulty + commercial or transactional intent = highest priority
- Informational keywords retained but ranked lower unless content strategy signals need them
- Declining trend keywords downgraded regardless of volume

Trim to `research_config.search_landscape_max_keywords` (default: 100). Log deprioritised keywords in `notes`.

### Step 6: Page intent grouping

Organise the final keyword list into page intent groups based on `page_type_suggestion` from R1-SERP and refined intent signals:
- `homepage`
- `product_category`
- `product_detail`
- `service_page`
- `location_page`
- `blog`
- `other`

---

## Output

Write output using the templates at `templates/R2-Keywords-template.md`.

---

## What passes to the next substage

`research/R2-Keywords.json` — substage 3.3 reads the commercial competitor domain list (enriched from both R1 and R2) to build the final competitor list (capped at `competitors_max`). The `page_groups` block feeds into Concept Creation for site structure planning.
