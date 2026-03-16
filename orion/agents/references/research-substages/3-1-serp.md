# Substage 3.1 — SERP Research

**Code:** R1
**Slug:** SERP
**Output:** `research/R1-SERP.json`, `research/R1-SERP.md`
**Dependencies:** none (first substage)
**Reads from:** `D1-Init.json`, `D2-Client-Intelligence.json`
**MCP tools:** DataForSEO (required)

---

## Purpose

Establish the initial keyword set, check current SERP positions for the client, classify search intent, estimate volumes, and compile the first competitor signal list from recurring SERP domains. This is the foundation that substages 3.2 and 3.3 build on.

**This is BREADTH research (landscape mapping), not DEPTH research (keyword targeting). Map the battlefield — do not plan the attack.**

---

## Data Sources

From `D1-Init.json`:
- `project.site_type`, `project.goal` — what the client offers
- `project.languages` — primary + additional languages
- `project.location` — primary + additional markets
- `research_config.serp_max_keywords` — hard cap (default: 50)
- `research_config.research_depth` — `basic` enforces cap, `deep` treats it as guideline
- `notes` — competitor hints, SEO keyword suggestions from operator

From `D2-Client-Intelligence.json`:
- `services_or_products` — primary source for keyword generation
- `profile` — industry, description, markets
- `website.url` — client domain for position tracking
- `registry` — legal name for brand variant queries

---

## Methodology

### Step 1: Language x location matrix

For each language x location combination, determine the correct search engine settings:
- Primary location + primary language → e.g., SK + Slovak → google.sk
- Primary location + secondary language → e.g., SK + English → google.sk in English
- Secondary location + language → e.g., CZ + Czech → google.cz

Map each combination to DataForSEO `location_code` and `language_code` parameters.

### Step 2: Keyword generation

**2a. Build seed list BEFORE calling the API.** Do not pass a single generic word — construct a full seed list first:

For each service/product from `D2.services_or_products`:
- Generate 3–5 phrasing variants: noun forms, adjective forms, verb forms, common synonyms (e.g., "svadobný fotograf", "svadobná fotografia", "fotografovanie svadby", "fotenie svadby"). Natural phrasing per language — not literal translations.
- Combine high-priority variants with location modifiers (city, region, country).

Add brand-related seeds:
- Client name and brand variants (including legal name if different)
- INIT notes (competitor hints, operator keyword suggestions)

The seed list should contain **15–30 seed phrases** before any API call. A single generic word (e.g., "fotograf") is never sufficient — it returns irrelevant results.

**2b. Call `dataforseo_labs_google_keyword_ideas`** with the full seed list. Set `limit: 100` per call to ensure broad coverage. Run per language x location combination from the matrix.

**Relevance guardrail:** Every keyword must describe a service the client actually delivers or a direct query about hiring/booking that service. Keywords about adjacent industries, complementary services the client does not offer, or generic topic words (e.g., "svadobný darček" for a photographer, "kameraman" if client does not offer video) are off-topic. Drop off-topic keywords before applying caps.

**Cap rules (when research_depth = basic):**
- Max 10 keywords per service or product
- Max 3 location modifier variants per keyword
- Max 30 keywords per language x location combination
- Hard total cap: `research_config.serp_max_keywords` (default: 50)

**Priority if cap reached:** core service/product keywords first, brand variants second, location modifiers third. Log deprioritised keywords in `notes`.

### Step 3: Client current rankings

Call `dataforseo_labs_google_ranked_keywords` on the client domain. Returns keywords the client already ranks for, with positions and traffic share.

**Flag shady/off-brand keywords.** If the client ranks for keywords unrelated to their services — adult content, grey-zone terms, keyword-stuffed phrases, or anything that doesn't match D2's services_or_products — do NOT merge them into the seed list. Instead, log them separately in `notes` with a warning (e.g., "Client ranks for 'akty fotografia' — off-brand, possible keyword stuffing on current site. Excluded from seeds."). This informs the operator and prevents shady keywords from contaminating downstream research.

Merge only relevant net-new keywords into the keyword list. Mark existing keywords with client position data.

### Step 4: SERP check

For every keyword in the list, call `serp_organic_live_advanced` with the correct location_code, language_code, and search engine.

Record per keyword:
- Client domain position (1–10 or `null` if not present)
- All domains appearing in top 10
- Top result domain

### Step 5: Intent classification

Classify each keyword as: `navigational`, `informational`, `commercial`, `transactional`.

**Primary method:** Use SERP features from Step 4 to infer intent — shopping ads and product carousels signal `transactional`, local packs and map results signal `commercial`, featured snippets and PAA boxes signal `informational`, brand sitelinks signal `navigational`. When a keyword has mixed signals, classify by the dominant SERP feature type.

**Fallback:** If intent remains ambiguous after SERP analysis, classify from keyword structure — brand terms → `navigational`, question words → `informational`, price/buy/order modifiers → `transactional`, service + location → `commercial`.

### Step 6: Volume estimation

Call `kw_data_google_ads_search_volume` on the full keyword list. Returns estimated monthly search volume per keyword per location.

### Step 7: Competitor frequency compilation

Count domain appearances across all SERP results **with location weighting**:

**7a. Primary location competitors.** Filter SERP results to keywords containing the client's primary location (city, region). Compile domains appearing in these location-specific SERPs — these are the client's **direct local competitors**. Even if a domain appears only 2-3 times, if those appearances are all in location keywords matching the client's service area, it's a real competitor.

**7b. General competitors.** Count domain appearances across all remaining (non-location) SERP results for broader market competitors.

**7c. Merge and rank.** Combine both lists. Each competitor gets:
- `keyword_appearances` — total count across all SERPs
- `local_appearances` — count in location-specific SERPs only
- `scope` — `local` (appears mainly in client's location keywords), `national` (appears across broad keywords), `both`

A domain with 3 local appearances is more relevant than one with 10 national appearances — the client competes with local businesses first.

**7d. Compile top 10** (always 10 — `competitors_max` in research_config applies to R3 detailed profiling, not R1 frequency counting). Ensure at least 3 local competitors are included if available. Classify each by site type:
- `commercial` — direct competitor selling same product/service
- `directory` — aggregator or listing site
- `media` — editorial, news, blog
- `marketplace` — multi-vendor platform
- `informational` — Wikipedia, how-to, reference

Only `commercial` domains carry forward to R2 and R3. All others are noted but not profiled.

### Step 8: Page type suggestions

For each keyword, suggest which page type it likely maps to based on intent and topic: `homepage`, `product_category`, `product_detail`, `service_page`, `blog`, `location_page`, `faq`, `landing_page`.

---

## Output

Write output using the templates at `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/templates/R1-SERP-template.md`.

---

## What passes to the next substage

`research/R1-SERP.json` — R2 reads: seed keywords for expansion, client current rankings as baseline, competitor domain list for gap analysis.
