---
name: seo-keyword-research
description: "Conduct structured SEO keyword research for a website project. Takes business context from D1, analyzes competitor keyword usage via MCP SEO tools or web research, and produces organized keyword clusters with page mapping, search intent classification, and priority ranking. Produces D3: SEO Keyword Map. Invoke when the user asks to research keywords, build a keyword map, create D3, run SEO keyword analysis, or map keywords to pages."
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
version: 1.1.0
---

Conduct SEO keyword research for the webtools website creation pipeline. Produce D3: SEO Keyword Map -- a structured document mapping keyword opportunities to pages with volume data, difficulty assessments, and intent classifications.

---

## Lifecycle Startup

Before doing anything else, complete these steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

**Required inputs:**
- D1: Project Brief at `brief/D1-project-brief.md`
  - If it does NOT exist: warn the operator. "D1: Project Brief is not available. SEO research without business context produces generic results. It should be created using webtools-intake. You can: (a) Switch to create it first, or (b) Proceed with manual context."
  - If it exists but status is not `complete`: warn. "D1: Project Brief exists but status is [status]. Proceeding with current version."
  - If it exists and status is `complete`: load it silently. Extract: business description, services/products, target audience, competitors, geographic focus, client website URL.

**Optional inputs (load silently if present):**
- Competitor URLs (from D1 or provided in conversation)
- Target location/market (from D1 or provided in conversation)
- Existing Google Search Console or Analytics data (CSV, provided in conversation)
- Manual seed keywords (provided in conversation)
- R1: SERP Landscape at `research/R1-serp-landscape.md`
- R5: Content Strategy at `research/R5-content-strategy.md`
- D15: Research Report at `research/D15-research-report.md`

### 4. Output Preparation

Check if `seo/D3-seo-keyword-map.md` already exists. If yes, warn the operator and ask whether to overwrite or cancel.

### 5. Tool Detection

Probe for SEO data MCP tools. Check available tool names for these substrings:

| Substring Match | Server | Priority |
|---|---|---|
| `dataforseo` or `datalabs` | DataForSEO | 1 (preferred) |
| `seo-data-api` or `seranking` or `DATA_` | SE Ranking | 2 |

Set the active data tier based on what is available:
- **TIER 1 (MCP)**: DataForSEO or SE Ranking tools detected. Actual volume, KD, CPC data.
- **TIER 2 (WebSearch)**: No MCP tools, but WebSearch is available. Signal-based estimates.
- **TIER 3 (Estimates)**: No MCP tools and no WebSearch. Industry knowledge Low/Medium/High.

Consult `${PLUGIN_ROOT}/references/mcp-tool-mapping.md` for exact tool names, parameters, and batch strategies when using TIER 1.

### 6. Research Intelligence

Load research documents if available (skip silently if absent):
- **R1** (`research/R1-serp-landscape.md`): Extract SERP-observed keywords, competitor keyword patterns, difficulty signals from SERP composition.
- **R5** (`research/R5-content-strategy.md`): Extract content gap terms, audience language patterns, topic cluster suggestions.
- **D15** (`research/D15-research-report.md`): Extract strategic focus areas for priority alignment, market positioning themes.

Record which documents were loaded and what key inputs were extracted.

### 7. Status Report

```
Project: [client name]
D1 Project Brief: [loaded / not found / in-progress]
Competitor URLs: [list or "none found"]
Geographic focus: [location or "not specified"]
Data tier: [TIER 1 (DataForSEO) / TIER 1 (SE Ranking) / TIER 2 (WebSearch) / TIER 3 (Estimates)]
Research intelligence: [R1 loaded, R5 loaded, D15 loaded / none available]
Output: seo/D3-seo-keyword-map.md ([new / overwrite])

Ready to begin keyword research.
```

---

## Gather Research Inputs

After startup, prompt the operator for any missing context:

1. **Primary services/products to target** -- what does the client want to be found for?
2. **Geographic focus** -- local, regional, national, or international?
3. **Priority keywords** -- any keywords the client already knows they want to target?
4. **Competitor URLs** -- if not already in D1, ask for 3-5 competitor sites to analyze

---

## Research Methodology

Follow these steps to produce the keyword map. Each step describes behavior per data tier. TIER 3 is the baseline; higher tiers add data sources on top.

### Step 1: Seed Generation

Generate an initial list of seed keywords from all available sources:

**All tiers (baseline):**
- Core service/product terms from D1 and operator input
- Industry-specific terminology
- Location-modified terms (if local/regional)
- Problem/solution terms (what does the audience search for?)
- Competitor brand-adjacent terms

**Research-enhanced (when R1/R5 loaded):**
- SERP-observed keywords from R1 (terms appearing in top results for core queries)
- Content gap terms from R5 (topics where competitors have content but client does not)
- Audience language patterns from R5 (how the target audience phrases searches)

**TIER 1 addition:**
- Call `keywords_for_site` (DataForSEO) or `getDomainKeywords` (SE Ranking) for the client domain and each competitor domain (limit: 100-200 each). Merge API-discovered seeds with manual seeds.

Annotate each seed with its source (D1, operator, R1, R5, MCP). Present the seed list to the operator for review. Add any missing seeds they suggest.

### Step 2: Keyword Expansion

For each seed keyword, generate related terms:

**TIER 3 (baseline):**
- Long-tail variations
- Question-based queries ("how to", "what is", "best")
- Comparison queries ("[service] vs [alternative]")
- Location variations (if applicable)
- Intent-specific variations (informational, commercial, transactional)

**TIER 2 addition:**
- WebSearch `[seed] related searches` -- extract autocomplete patterns
- WebSearch `[seed]` -- extract "People Also Ask" questions as long-tail candidates

**TIER 1 addition:**
- Call `keywords_suggestions` / `related_keywords` (DataForSEO) or `getRelatedKeywords` / `getLongTailKeywords` / `getKeywordQuestions` (SE Ranking) for the top 5-10 seeds (limit: 50-100 each).
- Merge API expansions with manual expansions, deduplicate.

### Step 3: Competitor Keyword Analysis

If competitor URLs are available:

**TIER 2/3 (baseline):**
- Fetch competitor sites via WebFetch and analyze page titles, headings, meta descriptions
- Note content topics and themes
- Identify keyword gaps (terms competitors target that the client does not)
- Identify opportunities (terms competitors miss)

**TIER 1 addition:**
- Call `ranked_keywords` (DataForSEO) or `getDomainKeywords` (SE Ranking) for each competitor domain (limit: 200 each) to get their actual organic keyword portfolio.
- Call `domain_intersections` (DataForSEO) or `getDomainKeywordsComparison` (SE Ranking) to find keyword overlap between client and each competitor.
- Use API data for gap/opportunity analysis instead of manual site inspection.

### Step 4: Keyword Clustering

Group the expanded keyword list into clusters:
- Each cluster represents a topic or theme
- Assign a primary keyword to each cluster (highest relevance and opportunity)
- Include 3-8 supporting keywords per cluster
- Classify each cluster by search intent:
  - **Informational**: Learning, researching ("what is", "how to", "guide")
  - **Commercial**: Comparing, evaluating ("best", "vs", "review", "top")
  - **Transactional**: Ready to act ("buy", "hire", "get quote", "pricing")
  - **Navigational**: Looking for specific brand/site

When TIER 1 data includes intent classification (DataForSEO `main_intent` or SE Ranking `intents`), use API intent data as primary signal. Override only when context clearly contradicts.

### Step 5: Volume and Difficulty Assessment

**TIER 3 (baseline):**
- **Search volume**: Low / Medium / High (with approximate monthly ranges)
- **Difficulty**: Low / Medium / High (based on competition level)
- **Opportunity score**: Priority ranking combining volume, difficulty, and business relevance
- Note: "Estimates are based on industry knowledge, competitor analysis, and search pattern understanding."

**TIER 2 (WebSearch signals):**
- Cross-reference search result count, autocomplete depth, SERP richness, and PAA presence per `references/mcp-tool-mapping.md` TIER 2 methodology.
- Format volume as "Medium (~1,000-3,000/mo est.)" to distinguish from actual data.
- Difficulty based on SERP composition (brand dominance, featured snippets, ad density).

**TIER 1 (MCP actual data):**
- **DataForSEO**: Batch all unique keywords through `keywords-google-ads-search-volume` (up to 700/call) for volume + CPC. Then batch through `datalabs_bulk_keyword_difficulty` (up to 1000/call) for KD scores.
- **SE Ranking**: Batch all unique keywords through `DATA_exportKeywords` (up to 5000/call) -- returns volume, CPC, difficulty, competition in a single call.
- Record actual monthly volume (integer), KD score (0-100), CPC (float).
- Before making TIER 1 calls, estimate the total call count and inform the operator.

Add a **Source** column to all keyword tables indicating where the data came from (MCP actual / WebSearch estimate / Industry estimate).

### Step 6: Page Mapping

Map each keyword cluster to a suggested target page:
- Match clusters to pages likely in the site architecture
- Identify clusters that need dedicated pages
- Flag clusters that might share a page
- Note when a cluster maps to a page type (e.g., "service page" or "blog post") rather than a specific page

---

## D3 Output Structure

The final D3: SEO Keyword Map MUST contain these sections:

### Research Summary
- Business context (from D1)
- Geographic focus
- Total keywords identified
- Number of clusters
- Data tier used and methodology notes
- Research intelligence used (list R1, R5, D15 if loaded)
- Data source (MCP server name, or "WebSearch signals", or "Industry estimates")

### Keyword Clusters

For each cluster, present as a table:

```
#### Cluster: [Cluster Name]
Intent: [Informational / Commercial / Transactional / Navigational]
Suggested page: [page name or type]
Priority: [High / Medium / Low]

| Keyword | Volume | Difficulty | CPC | Source | Notes |
|---------|--------|------------|-----|--------|-------|
| primary keyword | 2,400 | 35 | $2.10 | MCP | Primary target |
| supporting keyword 1 | Medium (~1K-3K est.) | Low | -- | WebSearch | Long-tail |
| supporting keyword 2 | Low | Low | -- | Estimate | Question-based |
```

TIER 1 volume is an integer. TIER 2 volume uses "Level (~range est.)" format. TIER 3 volume is Low/Medium/High only.

### Page-Keyword Matrix

| Page | Primary Keyword | Secondary Keywords | Intent |
|------|-----------------|-------------------|--------|
| Homepage | [keyword] | [keywords] | Mixed |
| [Service page] | [keyword] | [keywords] | Transactional |

### Competitor Keyword Overlap

If competitor analysis was performed:
- Keywords all competitors target (table stakes)
- Keywords only some competitors target (opportunities)
- Keywords no competitor targets (gaps)

### Priority Recommendations

1. **Quick wins**: Low difficulty, decent volume, high business relevance
2. **Strategic targets**: Higher difficulty but important for business
3. **Long-term plays**: High difficulty, high volume targets to build toward
4. **Content opportunities**: Informational keywords that support blog/resource content

When research intelligence is loaded, align priorities with D15 strategic focus areas.

### Data Source Notes

- Data tier: [TIER 1 / TIER 2 / TIER 3]
- Source: [DataForSEO / SE Ranking / WebSearch / Industry estimates]
- Date: [research date]
- Keywords with actual data: [count] / Keywords with estimated data: [count]
- If mixed tiers: note which clusters have actual vs estimated data

---

## Review Process

Present the complete D3 draft to the operator. Ask:
- Do the clusters make sense for the business?
- Are there missing keyword areas?
- Is the page mapping aligned with the planned site structure?
- Are the priorities correct?

Iterate based on feedback.

---

## Lifecycle Completion

After the operator approves the keyword map, complete these 4 steps.

### 1. File Naming Validation

Write to `seo/D3-seo-keyword-map.md` with YAML frontmatter:

```yaml
---
document_id: D3
title: "SEO Keyword Map"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-seo
status: complete
data_tier: "[TIER 1 (DataForSEO) / TIER 1 (SE Ranking) / TIER 2 / TIER 3]"
data_source: "[DataForSEO / SE Ranking / WebSearch / Industry estimates]"
dependencies:
  - D1: /brief/D1-project-brief.md
  # Include only those that were actually loaded:
  - R1: /research/R1-serp-landscape.md
  - R5: /research/R5-content-strategy.md
  - D15: /research/D15-research-report.md
---
```

### 2. Registry Update

Update `project-registry.md`:
- Set D3 row: Status = `complete`, File Path = `seo/D3-seo-keyword-map.md`, Created = today, Updated = today, Created By = `webtools-seo`
- Phase Log: if Research phase has no Started date, set Started to today. Add `webtools-seo` to Plugins Used.

### 3. Cross-Reference Check

Skip. D3 is a single-instance document.

### 4. Downstream Notification

```
D3: SEO Keyword Map is complete.
Data tier: [tier used]

Downstream documents that use D3:
- D4: Site Architecture (keyword-informed page structure) -> webtools-architecture
- D7: Page Blueprints (keyword targets per section)       -> webtools-blueprint
- D8: Page Content (SEO-optimized writing)                -> webtools-writer
- D10: Content Audit (SEO compliance checks)              -> webtools-audit
```

---

## Behavioral Rules

- Do NOT fabricate search volume numbers. TIER 1: use actual API data. TIER 2: provide signal-based estimates with methodology. TIER 3: provide Low/Medium/High ranges and note the limitation.
- Do NOT claim keyword rankings. This skill identifies opportunities, not current positions.
- If no competitor URLs are available, skip competitor keyword analysis and note the limitation.
- Keep the tone professional and efficient.
- Do not use emojis in any output.
- Flag when a keyword recommendation conflicts with the business goals from D1.
- Batch MCP API calls where the API supports it. Consult `references/mcp-tool-mapping.md` for batch limits per tool.
- Respect SE Ranking 10 req/sec rate limit -- add delays between sequential calls.
- Never mix data tiers in a single table without explicit Source column notation.
- Before TIER 1 API calls, estimate the total call count and inform the operator (API calls cost credits).
- Cite research document sources (R1, R5, D15) in D3 output when their data influenced seeds or priorities.
- If an MCP call fails mid-research, fall back gracefully to the next available tier. Annotate which keywords have actual vs estimated data in the Source column.
