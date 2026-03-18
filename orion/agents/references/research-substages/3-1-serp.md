# Substage 3.1 — SERP Research

**Code:** R1
**Slug:** SERP
**Output:** `research/R1-SERP.txt`
**Hypothesis:** Client is invisible in local search for core services
**Dependencies:** none (first substage)
**Reads from:** `project.json`, `baseline-log.txt`
**MCP tools:** DataForSEO (required)

---

## Purpose

Establish the initial keyword set, check current SERP positions for the client, classify search intent, estimate volumes, and compile the first competitor signal list from recurring SERP domains. This is the foundation that substages 3.2 and 3.3 build on.

**This is BREADTH research (landscape mapping), not DEPTH research (keyword targeting). Map the battlefield — do not plan the attack.**

---

## Data Sources

From `project.json`: site type, goal, languages, location, research config (serp_max_keywords, research_depth), notes.
From `baseline-log.txt`: mission, client profile, services/products, client URL, any prior findings.

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

For each service/product from `baseline-log.txt` (captured during D2 Client Intelligence):
- Generate phrasing variants: noun forms, adjective forms, verb forms, common synonyms (e.g., "svadobný fotograf", "svadobná fotografia", "fotografovanie svadby", "fotenie svadby"). Natural phrasing per language — not literal translations.
- Combine high-priority variants with location modifiers (city, region, country).

Add brand-related seeds: client name and brand variants, INIT notes (competitor hints, operator keyword suggestions).

Build a substantial seed list before any API call. A single generic word (e.g., "fotograf") is never sufficient — it returns irrelevant results.

**2b. Call `dataforseo_labs_google_keyword_ideas`** with the full seed list. Set `limit: 100` per call to ensure broad coverage. Run per language x location combination from the matrix.

**Relevance guardrail:** Every keyword must describe a service the client actually delivers or a direct query about hiring/booking that service. Keywords about adjacent industries, complementary services the client does not offer, or generic topic words (e.g., "svadobný darček" for a photographer, "kameraman" if client does not offer video) are off-topic. Drop off-topic keywords before applying caps.

Respect `research_config.serp_max_keywords` as the total cap. When trimming, prioritise core service/product keywords over brand variants over location modifiers. Log deprioritised keywords in `notes`.

### Step 3: Client current rankings

Call `dataforseo_labs_google_ranked_keywords` on the client domain. Returns keywords the client already ranks for, with positions and traffic share.

**Flag shady/off-brand keywords.** If the client ranks for keywords unrelated to their services — adult content, grey-zone terms, keyword-stuffed phrases — do NOT merge them into the seed list. Log them separately with a warning. This informs the operator and prevents shady keywords from contaminating downstream research.

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

**7c. Merge and rank.** Combine both lists. Track total keyword appearances, local appearances, and scope (local, national, both). A domain with 3 local appearances is more relevant than one with 10 national appearances — the client competes with local businesses first.

**7d. Compile top competitors.** Favour local representation. Classify each by site type — commercial, directory, media, marketplace, informational. Only `commercial` domains carry forward to R2 and R3. All others are noted but not profiled.

### Step 8: Page type suggestions

For each keyword, suggest which page type it likely maps to based on intent and topic (e.g., homepage, service page, blog, location page, landing page, etc.).

---

## Output

Write `research/R1-SERP.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R1]`.

R2 will read your output for: seed keywords, client current rankings, competitor domain list.
