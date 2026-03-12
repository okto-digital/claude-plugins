# DataForSEO REST API — Prompt Recipes

Pre-built instruction sequences that replicate the DataForSEO MCP server's 21 ready-made prompts as direct HTTP API call chains. Each recipe specifies which endpoints to call, in what order, and how to format the output.

**Usage:** When the `dataforseo-api` agent receives a task matching one of these recipes, follow the endpoint sequence and output format described here. All endpoints use the standard auth and temp-file patterns from the other reference files in this directory.

**Auth:** `Authorization: Basic {dataforseo_auth}`
**Temp file:** Write JSON body to `{working_directory}/tmp/dfs-request.json` before each call.

---

## SERP Recipes (3)

### Recipe S1: Local SEO Comparison Across Two Markets

**Purpose:** Compare top 10 Google organic results for a keyword in two different locations. Reveals which domains dominate each local market.

**Parameters:** `keyword`, `language_code`, `location_1` (name or code), `location_2` (name or code)

**Endpoint sequence:**

1. **Resolve locations** (if names given) — `GET /v3/serp/google/locations` (see serp-endpoints.md #1)
2. **SERP for location 1** — `POST /v3/serp/google/organic/live/advanced`
   ```json
   [{"keyword": "{keyword}", "location_code": {loc1_code}, "language_code": "{language_code}", "depth": 10}]
   ```
3. **SERP for location 2** — same endpoint, swap `location_code` to `{loc2_code}`

**Output format:** Unified comparison table:

```
| Rank | Location 1 Domain | Location 1 Title | Location 2 Domain | Location 2 Title |
|------|-------------------|------------------|-------------------|------------------|
| 1    | example.com       | Title...         | other.com         | Title...         |
```

Highlight domains that appear in both locations. Note any featured snippets, local packs, or other SERP features present.

---

### Recipe S2: Branded Search Visibility Monitor

**Purpose:** Check if a domain appears in top 3 organic results or SERP features for its brand keyword. Identify competitors occupying brand SERP real estate.

**Parameters:** `domain`, `location_code`, `language_code`

**Endpoint sequence:**

1. **SERP organic** — `POST /v3/serp/google/organic/live/advanced`
   ```json
   [{"keyword": "{domain brand name}", "location_code": {code}, "language_code": "{lang}", "depth": 10}]
   ```

**Output format:**
- Domain position (1-10 or "not found")
- SERP features present (`item_types` array): featured_snippet, local_pack, knowledge_panel, people_also_ask
- Competitor domains occupying SERP features
- Alert if domain is NOT in top 3 for its own brand

---

### Recipe S3: Domain Visibility Report with Historical Trends

**Purpose:** Generate a visibility snapshot showing current domain rank, traffic, and how it changed over time.

**Parameters:** `domain`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Current rank** — `POST /v3/dataforseo_labs/google/domain_rank_overview/live`
   ```json
   [{"target": "{domain}", "location_code": {code}, "language_code": "{lang}"}]
   ```
2. **Historical rank** — `POST /v3/dataforseo_labs/google/historical_rank_overview/live`
   ```json
   [{"target": "{domain}", "location_code": {code}, "language_code": "{lang}"}]
   ```

**Output format:**
- Current: domain rank, organic traffic estimate, total ranked keywords, top 3/10/100 distribution
- Trend: month-over-month changes in traffic and keyword count (last 12 months)
- Highlight peaks and drops with possible causes

---

## Backlinks Recipes (5)

### Recipe B1: Strongest Backlinks for Authority Building

**Purpose:** Find the highest-authority backlinks pointing to a domain. Useful for understanding which links drive the most authority.

**Parameters:** `domain`

**Endpoint sequence:**

1. **Backlink list** — `POST /v3/backlinks/backlinks/live`
   ```json
   [{"target": "{domain}", "limit": 50, "order_by": ["rank,desc"], "backlinks_status_type": "live"}]
   ```

**Output format:** Top 10 highest-authority backlinks grouped by referring domain:

```
| Referring Domain | Page Rank | Anchor Text | Target Page | Type | First Seen |
|------------------|-----------|-------------|-------------|------|------------|
```

---

### Recipe B2: Blog Content Earning Most Backlinks

**Purpose:** Identify which blog posts earn the most backlinks. Informs content strategy — replicate what works.

**Parameters:** `domain`

**Endpoint sequence:**

1. **Domain pages** — `POST /v3/backlinks/domain_pages/live`
   ```json
   [{"target": "{domain}", "limit": 100, "order_by": ["backlinks,desc"], "filters": ["url_from", "like", "/blog"]}]
   ```

**Note:** Filter pattern may need adjustment based on blog URL structure (`/blog/`, `/articles/`, `/news/`). Try without filter first if blog path is unknown.

**Output format:** Top 5 blog posts by backlink count:

```
| URL | Backlinks | Referring Domains | Top Anchor Texts |
|-----|-----------|-------------------|------------------|
```

---

### Recipe B3: Competitor Link Opportunities

**Purpose:** Find domains that link to two competitors but NOT to your domain. Prime outreach targets.

**Parameters:** `my_domain`, `competitor_1`, `competitor_2`

**Endpoint sequence:**

1. **Domain intersection** — `POST /v3/backlinks/domain_intersection/live`
   ```json
   [{"targets": {"1": "{competitor_1}", "2": "{competitor_2}", "3": "{my_domain}"}, "limit": 100, "order_by": ["rank,desc"]}]
   ```

**Post-processing:** Filter results to domains that link to targets 1 and 2 but NOT target 3.

**Output format:** Top 15 outreach targets:

```
| Referring Domain | Domain Rank | Links to Competitor 1 | Links to Competitor 2 | Category |
|------------------|-------------|----------------------|----------------------|----------|
```

---

### Recipe B4: Broken Pages Wasting Link Equity

**Purpose:** Find pages on your domain that have backlinks but return 404 or redirect. These waste link equity that could be reclaimed.

**Parameters:** `domain`, `min_backlinks` (default 5)

**Endpoint sequence:**

1. **Domain pages** — `POST /v3/backlinks/domain_pages/live`
   ```json
   [{"target": "{domain}", "limit": 100, "order_by": ["backlinks,desc"]}]
   ```

**Post-processing:** Filter to pages with `status_code` != 200 (404, 301, 302) and backlinks >= `min_backlinks`.

**Output format:**

```
| URL | Status Code | Backlinks | Referring Domains | Action |
|-----|-------------|-----------|-------------------|--------|
```

Action: "Restore" (404), "Update redirect target" (301/302 to wrong page), "OK" (301 to correct page).

---

### Recipe B5: Backlink Gap Benchmark vs Competitor

**Purpose:** Compare your backlink profile against a competitor. Find domains linking only to the competitor.

**Parameters:** `my_domain`, `competitor`

**Endpoint sequence:**

1. **Summary — your domain** — `POST /v3/backlinks/summary/live`
   ```json
   [{"target": "{my_domain}"}]
   ```
2. **Summary — competitor** — same endpoint with `"{competitor}"`
3. **Domain intersection** — `POST /v3/backlinks/domain_intersection/live`
   ```json
   [{"targets": {"1": "{competitor}", "2": "{my_domain}"}, "limit": 100, "order_by": ["rank,desc"]}]
   ```

**Post-processing:** From intersection, filter to domains linking to target 1 (competitor) but NOT target 2 (you).

**Output format:**
- Side-by-side profile comparison (total backlinks, referring domains, domain rank)
- Top 10 competitor-exclusive linking domains with rank and link count

---

## DataForSEO Labs Recipes (8)

### Recipe L1: Decision-Stage Keywords

**Purpose:** Find "vs", "alternative", "best", "compare" keywords for a product. Targets users in the decision/purchase stage.

**Parameters:** `product`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Keyword ideas** — `POST /v3/dataforseo_labs/google/keyword_ideas/live`
   ```json
   [{"keywords": ["{product} vs", "{product} alternative", "best {product}", "{product} compare", "{product} review"], "location_code": {code}, "language_code": "{lang}", "limit": 100}]
   ```
2. **Intent classification** — `POST /v3/dataforseo_labs/google/search_intent/live`
   ```json
   [{"keywords": [{extracted keywords from step 1}], "language_code": "{lang}", "location_code": {code}}]
   ```

**Post-processing:** Filter to commercial and transactional intent. Sort by search volume descending.

**Output format:** Top 20 decision-stage keywords:

```
| Keyword | Volume | CPC | Intent | Difficulty | Suggested Page Type |
|---------|--------|-----|--------|------------|---------------------|
```

---

### Recipe L2: Question-Based Article Ideas

**Purpose:** Find question keywords (what, why, how) with decent volume. Each becomes an article topic.

**Parameters:** `topic`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Keyword ideas** — `POST /v3/dataforseo_labs/google/keyword_ideas/live`
   ```json
   [{"keywords": ["what is {topic}", "how to {topic}", "why {topic}", "{topic} guide", "{topic} tips"], "location_code": {code}, "language_code": "{lang}", "limit": 100}]
   ```
2. **Intent classification** — `POST /v3/dataforseo_labs/google/search_intent/live`
   ```json
   [{"keywords": [{extracted keywords}], "language_code": "{lang}", "location_code": {code}}]
   ```

**Post-processing:** Filter to informational intent and volume >= 300. Generate a suggested article headline for each.

**Output format:** Top 20 article ideas:

```
| Keyword | Volume | Difficulty | Intent | Suggested Headline |
|---------|--------|------------|--------|-------------------|
```

---

### Recipe L3: High-Converting Paid Campaign Terms

**Purpose:** Find commercial/transactional keywords with high CPC (buyer readiness signal) for paid campaigns.

**Parameters:** `product`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Keyword ideas** — `POST /v3/dataforseo_labs/google/keyword_ideas/live`
   ```json
   [{"keywords": ["{product}", "buy {product}", "{product} price", "{product} service", "{product} near me"], "location_code": {code}, "language_code": "{lang}", "limit": 100}]
   ```
2. **Intent classification** — `POST /v3/dataforseo_labs/google/search_intent/live`
   ```json
   [{"keywords": [{extracted keywords}], "language_code": "{lang}", "location_code": {code}}]
   ```

**Post-processing:** Filter to CPC >= $2, volume >= 1000, commercial or transactional intent.

**Output format:** Top 20 high-converting terms:

```
| Keyword | Volume | CPC | Competition | Intent | Landing Page Angle |
|---------|--------|-----|-------------|--------|-------------------|
```

---

### Recipe L4: Keyword Cluster for Content Architecture

**Purpose:** Build a keyword cluster around a topic, grouped by intent. Informs site structure and internal linking.

**Parameters:** `keyword`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Related keywords** — `POST /v3/dataforseo_labs/google/related_keywords/live`
   ```json
   [{"keyword": "{keyword}", "location_code": {code}, "language_code": "{lang}", "limit": 50}]
   ```
2. **Keyword ideas** — `POST /v3/dataforseo_labs/google/keyword_ideas/live`
   ```json
   [{"keywords": ["{keyword}"], "location_code": {code}, "language_code": "{lang}", "limit": 50}]
   ```
3. **Difficulty** — `POST /v3/dataforseo_labs/google/bulk_keyword_difficulty/live`
   ```json
   [{"keywords": [{merged unique keywords from steps 1+2}], "location_code": {code}, "language_code": "{lang}"}]
   ```
4. **Intent** — `POST /v3/dataforseo_labs/google/search_intent/live`
   ```json
   [{"keywords": [{same merged list}], "language_code": "{lang}", "location_code": {code}}]
   ```

**Output format:** 20-term cluster grouped by intent:

```
## Informational
| Keyword | Volume | Difficulty | SERP Features |

## Commercial
| Keyword | Volume | Difficulty | SERP Features |

## Transactional
| Keyword | Volume | Difficulty | SERP Features |

## Internal Linking Map
- Pillar: {main keyword} → links to all cluster pages
- Cluster pages link back to pillar and to related intent pages
```

---

### Recipe L5: Competitor Keyword Comparison

**Purpose:** Compare two domains by keyword overlap and unique keywords. Reveals content gaps and competitive advantages.

**Parameters:** `site_1`, `site_2`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Domain rank — site 1** — `POST /v3/dataforseo_labs/google/domain_rank_overview/live`
   ```json
   [{"target": "{site_1}", "location_code": {code}, "language_code": "{lang}"}]
   ```
2. **Domain rank — site 2** — same endpoint with `"{site_2}"`
3. **Domain intersection** — `POST /v3/dataforseo_labs/google/domain_intersection/live`
   ```json
   [{"target1": "{site_1}", "target2": "{site_2}", "location_code": {code}, "language_code": "{lang}", "limit": 100}]
   ```

**Output format:**
- Side-by-side: domain rank, organic traffic, keyword count, top 3/10/100 distribution
- Shared keywords (top 20 by volume) with position for each domain
- Keywords unique to each domain (top 10 each)

---

### Recipe L6: Low-Competition Informational Content

**Purpose:** Find informational keywords with low competition and decent volume. Easy wins for blog/content strategy.

**Parameters:** `topic`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Keyword ideas** — `POST /v3/dataforseo_labs/google/keyword_ideas/live`
   ```json
   [{"keywords": ["{topic}", "{topic} guide", "{topic} explained", "{topic} tutorial"], "location_code": {code}, "language_code": "{lang}", "limit": 100}]
   ```
2. **Difficulty** — `POST /v3/dataforseo_labs/google/bulk_keyword_difficulty/live`
   ```json
   [{"keywords": [{extracted keywords}], "location_code": {code}, "language_code": "{lang}"}]
   ```
3. **Intent** — `POST /v3/dataforseo_labs/google/search_intent/live`
   ```json
   [{"keywords": [{same keywords}], "language_code": "{lang}", "location_code": {code}}]
   ```

**Post-processing:** Filter to informational intent, difficulty < 40, volume >= 500.

**Output format:** Top 20 easy-win topics:

```
| Keyword | Volume | Difficulty | CPC | Blog Topic Suggestion |
|---------|--------|------------|-----|----------------------|
```

---

### Recipe L7: Long-Term SEO Performance Tracker

**Purpose:** Show how a domain's visibility changed over 12 months. Identify seasonal trends and ranking shifts.

**Parameters:** `domain`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Historical rank overview** — `POST /v3/dataforseo_labs/google/historical_rank_overview/live`
   ```json
   [{"target": "{domain}", "location_code": {code}, "language_code": "{lang}"}]
   ```

**Output format:** Monthly trend table (last 12 months):

```
| Month | Organic Traffic | Keywords (Top 3) | Keywords (Top 10) | Keywords (Top 100) | Change |
|-------|-----------------|-------------------|--------------------|--------------------|--------|
```

Highlight: peak months, significant drops, seasonal patterns.

---

### Recipe L8: Monthly Traffic Trend Comparison vs Competitor

**Purpose:** Compare monthly organic traffic and ranking distribution between your domain and a competitor.

**Parameters:** `domain`, `competitor_domain`, `location_code`, `language_code`

**Endpoint sequence:**

1. **Your domain rank** — `POST /v3/dataforseo_labs/google/domain_rank_overview/live`
   ```json
   [{"target": "{domain}", "location_code": {code}, "language_code": "{lang}"}]
   ```
2. **Competitor domain rank** — same endpoint with `"{competitor_domain}"`

**Output format:**
- Side-by-side: organic traffic, keyword count, top 10 visibility percentage
- Traffic trend comparison if historical data available
- Competitive gap analysis: where competitor leads and where you lead

---

## On-Page Recipes (5)

### Recipe O1: Technical Crawlability Audit

**Purpose:** Check a page for technical issues affecting crawlability and ranking: robots directives, noindex, broken resources.

**Parameters:** `url`

**Endpoint sequence:**

1. **Instant pages** — `POST /v3/on_page/instant_pages`
   ```json
   [{"url": "{url}", "enable_javascript": true}]
   ```

**Output format:**
- HTTP status code
- Robots directives (index/noindex, follow/nofollow)
- Canonical URL (and whether it matches)
- Broken resources count
- Page timing (connection, download, rendering)
- onpage_score (0-100)

Flag: any status != 200, noindex present, canonical mismatch, broken resources > 0.

---

### Recipe O2: Meta Tag Audit

**Purpose:** Detect missing or duplicate meta titles and descriptions that hurt SEO.

**Parameters:** `url`

**Endpoint sequence:**

1. **Instant pages** — `POST /v3/on_page/instant_pages`
   ```json
   [{"url": "{url}", "enable_javascript": true}]
   ```

**Output format:**
- Title: present/missing, length, duplicate flag
- Meta description: present/missing, length, duplicate flag
- H1: present/missing, count (should be exactly 1), content
- Open Graph tags: present/missing
- Structured data: present/missing

Flag: missing title, missing description, title > 60 chars, description > 160 chars, multiple H1 tags, duplicate flags.

---

### Recipe O3: Speed and Mobile Compatibility Check

**Purpose:** Analyze page load time and Core Web Vitals. Identify speed bottlenecks.

**Parameters:** `url`

**Endpoint sequence:**

1. **Lighthouse (desktop)** — `POST /v3/on_page/lighthouse/live/json`
   ```json
   [{"url": "{url}", "for_mobile": false, "categories": ["performance", "seo"]}]
   ```
2. **Lighthouse (mobile)** — `POST /v3/on_page/lighthouse/live/json`
   ```json
   [{"url": "{url}", "for_mobile": true, "categories": ["performance", "seo"]}]
   ```

**Output format:**

```
| Metric              | Desktop | Mobile | Target |
|---------------------|---------|--------|--------|
| Performance Score   |         |        | > 90   |
| SEO Score           |         |        | > 90   |
| LCP                 |         |        | < 2.5s |
| FCP                 |         |        | < 1.8s |
| CLS                 |         |        | < 0.1  |
| TBT                 |         |        | < 200ms|
| Speed Index         |         |        | < 3.4s |
```

Flag any metric in red zone. List top 3 improvement opportunities from audit details.

---

### Recipe O4: Internal Linking and Crawl Depth Audit

**Purpose:** Evaluate internal link structure and crawl depth. Pages buried too deep get less link equity and crawl frequency.

**Parameters:** `url`

**Endpoint sequence:**

1. **Instant pages** — `POST /v3/on_page/instant_pages`
   ```json
   [{"url": "{url}", "enable_javascript": true}]
   ```

**Output format:**
- Internal links count (outgoing)
- External links count
- Crawl depth (clicks from homepage)
- Link equity distribution assessment

Flag: crawl depth > 3, fewer than 3 internal links, high external-to-internal ratio.

**Note:** Full internal linking analysis requires crawling multiple pages. This recipe audits a single page. For site-wide analysis, run this recipe on 10-20 key pages and aggregate.

---

### Recipe O5: Keyword Optimization and Content Gap Analysis

**Purpose:** Evaluate how well a page is optimized for a target keyword. Check keyword presence across title, meta, headings, and body.

**Parameters:** `url`, `keyword`

**Endpoint sequence:**

1. **Instant pages** — `POST /v3/on_page/instant_pages`
   ```json
   [{"url": "{url}", "enable_javascript": true}]
   ```
2. **Content parsing** — `POST /v3/on_page/content_parsing/live`
   ```json
   [{"url": "{url}"}]
   ```

**Output format:**

```
| Element          | Keyword Present? | Content                     |
|------------------|------------------|-----------------------------|
| Title            | Yes/No           | "Actual title text"         |
| Meta Description | Yes/No           | "Actual description text"   |
| H1               | Yes/No           | "Actual H1 text"            |
| H2-H6            | X of Y contain   | List matching headings      |
| Body Content     | X occurrences    | Keyword density percentage  |
| URL              | Yes/No           | Actual URL slug             |
```

- Word count and content length assessment
- Keyword density (target: 1-2%)
- Missing optimization opportunities
- Content gap: topics the keyword implies that the page doesn't cover

---

## Recipe Index

Quick lookup by use case:

| Code | Recipe | Endpoints Used | Primary Use Case |
|------|--------|----------------|------------------|
| S1 | Local SEO Comparison | SERP Organic (x2) | Market comparison |
| S2 | Branded Search Monitor | SERP Organic | Brand protection |
| S3 | Domain Visibility Report | Domain Rank + Historical Rank | Visibility tracking |
| B1 | Strongest Backlinks | Backlinks List | Authority analysis |
| B2 | Blog Content Links | Domain Pages | Content strategy |
| B3 | Competitor Link Opportunities | Domain Intersection | Link building |
| B4 | Broken Pages Wasting Links | Domain Pages | Link reclamation |
| B5 | Backlink Gap vs Competitor | Summary (x2) + Intersection | Competitive analysis |
| L1 | Decision-Stage Keywords | Keyword Ideas + Intent | Conversion keywords |
| L2 | Question-Based Articles | Keyword Ideas + Intent | Content planning |
| L3 | High-Converting Paid Terms | Keyword Ideas + Intent | PPC campaigns |
| L4 | Keyword Cluster | Related + Ideas + Difficulty + Intent | Site architecture |
| L5 | Competitor Keyword Comparison | Domain Rank (x2) + Intersection | Competitive analysis |
| L6 | Low-Competition Content | Ideas + Difficulty + Intent | Quick wins |
| L7 | SEO Performance Tracker | Historical Rank | Trend analysis |
| L8 | Traffic Trend vs Competitor | Domain Rank (x2) | Competitive tracking |
| O1 | Technical Crawlability | Instant Pages | Technical SEO |
| O2 | Meta Tag Audit | Instant Pages | On-page SEO |
| O3 | Speed & Mobile Check | Lighthouse (x2) | Performance |
| O4 | Internal Linking Audit | Instant Pages | Site structure |
| O5 | Keyword Optimization | Instant Pages + Content Parsing | Content optimization |
