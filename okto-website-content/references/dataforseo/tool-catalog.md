# DataForSEO -- Tool Catalog

Reference of available MCP tools for the dataforseo sub-agent. Only tools relevant to website content management are listed.

---

## SERP Analysis

### serp_organic_live_advanced
Google/Bing/Yahoo organic SERP results.
- **Params:** keyword, location_code (2840), language_code (en), device (desktop), depth (100), se (google|bing|yahoo)
- **Output:** Rank, URL, title, description, domain, featured snippets, People Also Ask

### serp_locations
Location code lookups for SERP queries.

---

## Keyword Research

### dataforseo_labs_google_keyword_ideas
Generate keyword ideas from seed.
- **Params:** keywords (array), location_code (2840), language_code (en), limit (50)
- **Output:** Keyword, search volume, CPC, competition, difficulty, trend

### dataforseo_labs_google_related_keywords
Semantically related keywords.
- **Params:** keyword, location_code, language_code, limit

### kw_data_google_ads_search_volume
Search volume for keyword list.
- **Params:** keywords (array), location_code, language_code
- **Output:** Monthly search volume, CPC, competition, monthly trend

### dataforseo_labs_bulk_keyword_difficulty
Keyword difficulty scores.
- **Params:** keywords (array), location_code, language_code
- **Output:** Difficulty score 0-100 (Easy/Medium/Hard/Very Hard)

### dataforseo_labs_search_intent
Search intent classification.
- **Params:** keywords (array), location_code, language_code
- **Output:** Intent type (informational/navigational/commercial/transactional), confidence

### kw_data_dfs_trends_explore
DFS proprietary trends data.
- **Params:** keywords (array), location_code, language_code

### kw_data_google_ads_locations
Location lookups for keyword data.

---

## Domain & Competitor Analysis

### dataforseo_labs_google_competitors_domain
Identify competing domains.
- **Params:** target (domain), location_code, language_code
- **Output:** Competitor domains, keyword overlap %, estimated traffic, domain rank

### dataforseo_labs_google_domain_rank_overview
Domain rank and metrics.
- **Params:** target (domain), location_code, language_code
- **Output:** Domain rank, organic traffic, keywords count

### dataforseo_labs_google_ranked_keywords
Keywords a domain ranks for.
- **Params:** target (domain), location_code, language_code, limit (100)
- **Output:** Keyword, position, URL, search volume, traffic share, SERP features

### dataforseo_labs_google_relevant_pages
Top-performing pages on a domain.
- **Params:** target (domain), location_code, language_code

### dataforseo_labs_google_domain_intersection
Shared keywords across 2-20 domains.
- **Params:** targets (array of domains)
- **Output:** Shared keywords with positions per domain

### dataforseo_labs_bulk_traffic_estimation
Organic traffic estimation for domains.
- **Params:** targets (array of domains)
- **Output:** Estimated organic traffic, traffic cost, top keywords

---

## Technical / On-Page

### on_page_instant_pages
Quick page analysis.
- **Params:** url
- **Output:** Status codes, meta tags, content size, page timing, broken links

### on_page_content_parsing
Extract and parse page content.
- **Params:** url
- **Output:** Plain text, word count, structure

### on_page_lighthouse
Full Lighthouse audit.
- **Params:** url
- **Output:** Performance, accessibility, best practices, SEO scores, Core Web Vitals

### domain_analytics_technologies_domain_technologies
Technology stack detection.
- **Params:** target (domain)
- **Output:** Technology name, version, category (CMS, analytics, CDN, framework)

---

## Content & Business Data

### content_analysis_search
Search for content by topic.
- **Params:** keyword
- **Output:** Content matches with quality scores, sentiment

### business_data_business_listings_search
Business listings search.
- **Params:** keyword, location (optional)
- **Output:** Business name, category, address, phone, domain, rating, review count
