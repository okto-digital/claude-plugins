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
- `profile` — industry, description, markets
- `website.url` — client domain for position tracking
- `registry` — legal name for brand variant queries

---

## Methodology

### Step 1: Keyword generation

Generate a keyword list based on:
- Client name and brand variants (including legal name if different)
- Services and products identified from INIT notes and client profile
- Location modifiers (city, region, country) per primary and secondary markets
- Language variants per primary and secondary languages

Keywords are generated as combinations with natural phrasing per language — not literal translations.

**Cap rules (when research_depth = basic):**
- Max 5 keywords per service or product
- Max 3 location modifier variants per keyword
- Max 20 keywords per language x location combination
- Hard total cap: `research_config.serp_max_keywords` (default: 50)

**Priority if cap reached:** core service/product keywords first, brand variants second, location modifiers third. Log deprioritised keywords in `notes`.

### Step 2: Language x location matrix

For each language x location combination, determine the correct search engine settings:
- Primary location + primary language → e.g., SK + Slovak → google.sk
- Primary location + secondary language → e.g., SK + English → google.sk in English
- Secondary location + language → e.g., CZ + Czech → google.cz

Map each combination to DataForSEO `location_code` and `language_code` parameters.

### Step 3: SERP execution

For every keyword in the matrix, call `serp_organic_live_advanced` with the correct location_code, language_code, and search engine.

Record per keyword:
- Client domain position (1–10 or `null` if not present)
- All domains appearing in top 10
- Result type (organic, featured snippet, local pack, etc.)
- Top result domain

### Step 4: Intent classification

Call `dataforseo_labs_search_intent` on the full keyword list.

Classify each keyword as:
- `navigational` — looking for specific brand or site
- `informational` — seeking knowledge or answers
- `commercial` — researching before purchase
- `transactional` — ready to act or buy

### Step 5: Volume estimation

Call `kw_data_google_ads_search_volume` on the full keyword list.

Returns estimated monthly search volume per keyword per location. First signal on keyword priority before deeper analysis in 3.2.

### Step 6: Competitor frequency compilation

Count domain appearances across all SERP results. Compile top 10 most frequently appearing domains. Classify each by site type:
- `commercial` — direct competitor selling same product/service
- `directory` — aggregator or listing site
- `media` — editorial, news, blog
- `marketplace` — multi-vendor platform
- `informational` — Wikipedia, how-to, reference

Only `commercial` domains carry forward to 3.3 (Competitor Landscape). All others are noted but not profiled.

### Step 7: Page type suggestions

For each keyword, suggest which page type it likely maps to based on intent and topic: `homepage`, `product_category`, `product_detail`, `service_page`, `blog`, `location_page`, `faq`, `landing_page`. This is a first-pass signal for site structure in Concept Creation.

---

## Output

Write output using the templates at `templates/R1-SERP-template.md`.

---

## What passes to the next substage

`research/R1-SERP.json` — substage 3.2 reads the keyword list as seeds for expansion, and the competitor domain list to cross-reference against keyword-based discovery.
