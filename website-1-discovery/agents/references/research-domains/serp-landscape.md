# Domain: SERP & Search Landscape

**Document ID:** R1
**Output filename:** R1-serp-landscape.md
**Topic:** "SERP & Search Landscape"
**Wave:** 1
**Cross-topic inputs:** none

---

## Tools

**Required:** WebSearch, WebFetch
**Optional MCP:** `mcp__dataforseo__serp_organic_live_advanced` (live SERP data with ranking positions, SERP features), `mcp__dataforseo__serp_locations` (location-specific SERP results)
**Crawling:** web-crawler dispatch for 2-3 top-ranking pages in Step 3 (content format sampling)

**IMPORTANT:** This is BREADTH research (landscape mapping), not DEPTH research (keyword targeting). Map the battlefield -- do not plan the attack.

---

## Methodology

### Step 1: Derive Search Queries

Extract 5-10 core service keywords from D1:
- Primary service terms (what the client sells/does)
- Industry category terms (how the market describes this type of business)
- Problem/solution terms (what customers search when they need this service)

**If D1 indicates local/regional business**, create location-modified variants:
- "[service] [city]"
- "[service] near [city]"
- "[industry] [region]"

Add 2-3 "People Also Ask" discovery queries:
- "how to choose [service]"
- "best [service] for [use case]"
- "[service] vs [alternative]"

**IMPORTANT:** List all planned queries before executing. Target 8-15 total queries (5-10 core + 2-5 local if applicable).

### Step 2: SERP Analysis

Run each query via WebSearch (or DataForSEO `serp_organic_live_advanced` if available for richer data). For each query, record:

- **Top 5 ranking domains** -- who appears, domain authority signals (brand vs niche site vs directory)
- **SERP features present** -- featured snippets, local pack, knowledge panel, People Also Ask, image pack, video carousel, shopping results, site links
- **Content types that rank** -- service pages, long-form guides, comparison articles, directories, tools, video, FAQ pages
- **Search intent signals** -- informational (guides, how-to), transactional (pricing, booking), navigational (brand searches), commercial investigation (comparisons, reviews)

Track cross-query patterns:
- Domains appearing in 3+ queries = dominant players (feed to R2)
- SERP features appearing consistently = content format opportunities
- Intent clustering = what the audience primarily wants

### Step 3: Content Format Sampling

For 2-3 top-ranking pages from core queries, dispatch web-crawler to observe:
- Content length (approximate word count)
- Page structure (sections, headings, media usage)
- Internal linking patterns
- Trust signals present (author bio, citations, certifications)

**IMPORTANT:** This is surface-level observation, not full content extraction. Spend no more than 5 minutes per page. If crawl fails for a URL, skip it -- this step is optional.

### Step 4: Local SEO Assessment

**Conditional -- only if D1 indicates local/regional business.**

Run location-specific searches (use DataForSEO `serp_locations` if available for location-accurate results):
- "[service] [city]" -- observe local pack (map results)
- "[service] near [city]" -- observe local pack variation
- "[industry] [city]" -- observe directory presence

Record for each local query:
- Local pack present? (yes/no, how many results)
- Review counts visible in SERP (range across competitors)
- Google Business Profile quality signals (photos, posts, Q&A visible)
- Map pack vs organic result overlap (same businesses or different?)

### Step 5: Synthesize

**Detailed Findings sub-sections:**
- Dominant Players (who ranks consistently across queries)
- SERP Feature Landscape (what features appear and for which query types)
- Content Format Winners (what content types rank, with evidence)
- Search Intent Distribution (informational vs transactional vs commercial split)
- Local Search Landscape (if applicable -- local pack, GBP signals, review landscape)
- Content Gaps (queries with weak results or no clear winner)
