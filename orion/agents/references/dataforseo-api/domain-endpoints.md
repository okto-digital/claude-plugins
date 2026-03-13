# DataForSEO REST API — Domain & Competitor Endpoints

Reference for domain analysis and competitor intelligence endpoints (DataForSEO Labs).

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

---

## Competitors Domain

Identify competing domains based on keyword overlap.

**URL:** `/v3/dataforseo_labs/google/competitors_domain/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk", "limit": 20}]
```

**Required:** `target` (domain), `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `limit`, `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with:
- `domain` — competitor domain
- `avg_position` — average SERP position
- `sum_position` — total position sum
- `intersections` — keyword overlap count
- `full_domain_metrics[]` — organic traffic, keywords count, estimated cost

**curl example:**
```
Write body: [{"target":"example.com","location_code":2703,"language_code":"sk","limit":20}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/dataforseo_labs/google/competitors_domain/live
```

---

## Domain Rank Overview

Domain rank and high-level metrics.

**URL:** `/v3/dataforseo_labs/google/domain_rank_overview/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (domain)
**Optional:** `location_code`, `language_code`

**Response:** `tasks[0].result[]` — each with `target`, `domain_rank`, `organic_etv` (estimated traffic value), `organic_count` (ranked keywords), `organic_is_new`, `organic_is_up`, `organic_is_down`, `organic_is_lost`

---

## Ranked Keywords

Keywords a domain ranks for.

**URL:** `/v3/dataforseo_labs/google/ranked_keywords/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk", "limit": 100}]
```

**Required:** `target` (domain or URL)
**Optional:** `location_code`, `language_code`, `limit`, `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with:
- `keyword_data` — keyword, volume, CPC, difficulty
- `ranked_serp_element` — position, URL, type, is_featured_snippet
- `se_type` — search engine

---

## Relevant Pages

Top-performing pages on a domain.

**URL:** `/v3/dataforseo_labs/google/relevant_pages/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk", "limit": 20}]
```

**Required:** `target` (domain)
**Optional:** `location_code`, `language_code`, `limit`, `filters`

**Response:** `tasks[0].result[0].items[]` — each with `page_address`, `metrics` (organic traffic, keywords count)

---

## Domain Intersection

Shared keywords across 2-20 domains.

**URL:** `/v3/dataforseo_labs/google/domain_intersection/live`
**Method:** POST

**Request body:**
```json
[{"target1": "domain1.com", "target2": "domain2.com", "location_code": 2703, "language_code": "sk", "limit": 100}]
```

**Required:** `target1`, `target2`, `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `target3` through `target20`, `limit`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `keyword_data` and per-domain position/URL info

---

## Bulk Traffic Estimation

Organic traffic estimation for multiple domains.

**URL:** `/v3/dataforseo_labs/google/bulk_traffic_estimation/live`
**Method:** POST
**Max targets:** 1000

**Request body:**
```json
[{"targets": ["domain1.com", "domain2.com", "domain3.com"]}]
```

**Required:** `targets` (array of domains/URLs, max 1000)

**Response:** `tasks[0].result[]` — each with `target`, `organic_etv`, `organic_count`, `organic_is_new`

---

## Subdomains

Subdomains with ranking data.

**URL:** `/v3/dataforseo_labs/google/subdomains/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (domain)
**Optional:** `location_code`, `language_code`, `limit`, `filters`

**Response:** `tasks[0].result[0].items[]` — each with `target` (subdomain), `metrics` (ranked keywords, traffic)

---

## Top Searches

Top-searched keywords in a location.

**URL:** `/v3/dataforseo_labs/google/top_searches/live`
**Method:** POST

**Request body:**
```json
[{"location_code": 2703, "language_code": "sk", "limit": 50}]
```

**Required:** `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `limit`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `keyword`, `search_volume`, `keyword_difficulty`

---

## Keywords for Site

Keywords a site ranks for (alternative to ranked_keywords).

**URL:** `/v3/dataforseo_labs/google/keywords_for_site/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk", "limit": 100}]
```

**Required:** `target` (domain), `location_code` or `location_name`
**Optional:** `language_code`, `limit`, `filters`

**Response:** `tasks[0].result[0].items[]` — keyword data with volume, difficulty, CPC

---

## Page Intersection

Shared keywords at page level across up to 20 pages.

**URL:** `/v3/dataforseo_labs/google/page_intersection/live`
**Method:** POST

**Request body:**
```json
[{"pages": {"1": "domain1.com/page1", "2": "domain2.com/page2"}, "location_code": 2703, "language_code": "sk"}]
```

**Required:** `pages` (object, up to 20 URL entries), `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — shared keywords with per-page positions

---

## Historical SERPs

Historical SERP results for a keyword over time.

**URL:** `/v3/dataforseo_labs/google/historical_serps/live`
**Method:** POST

**Note:** URL path uses `historical_serps` (plural).

**Request body:**
```json
[{"keyword": "web design bratislava", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keyword`, `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — SERP snapshots with dates and position data

---

## SERP Competitors

Competitors for a specific SERP.

**URL:** `/v3/dataforseo_labs/google/serp_competitors/live`
**Method:** POST

**Request body:**
```json
[{"keywords": ["web design bratislava"], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keywords` (array), `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — domains appearing in SERP with frequency/position data

---

## Historical Rank Overview

Historical domain rank data over time.

**URL:** `/v3/dataforseo_labs/google/historical_rank_overview/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (domain), `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[]` — time series of domain rank, traffic estimates, keyword counts

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
