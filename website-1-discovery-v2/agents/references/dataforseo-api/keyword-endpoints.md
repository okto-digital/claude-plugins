# DataForSEO REST API — Keyword Endpoints

Reference for keyword research endpoints: Labs keyword tools and Keywords Data (volume, trends).

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

---

## DataForSEO Labs — Keyword Research

### Keyword Ideas

Generate keyword ideas from seed keywords.

**URL:** `/v3/dataforseo_labs/google/keyword_ideas/live`
**Method:** POST
**Max keywords:** 200 per request

**Request body:**
```json
[{"keywords": ["web design", "website creation"], "location_code": 2703, "language_code": "sk", "limit": 50}]
```

**Required:** `keywords` (array), `location_code` or `location_name`
**Optional:** `language_code`, `limit` (default 100), `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `keyword`, `search_volume`, `cpc`, `competition`, `keyword_difficulty`, `monthly_searches[]`

---

### Keyword Suggestions

Keyword suggestions from a single seed.

**URL:** `/v3/dataforseo_labs/google/keyword_suggestions/live`
**Method:** POST

**Request body:**
```json
[{"keyword": "web design", "location_code": 2703, "language_code": "sk", "limit": 50}]
```

**Required:** `keyword` (string)
**Optional:** `location_code`, `language_code`, `limit`, `filters`, `order_by`

**Response:** Same structure as Keyword Ideas.

---

### Related Keywords

Semantically related keywords.

**URL:** `/v3/dataforseo_labs/google/related_keywords/live`
**Method:** POST

**Request body:**
```json
[{"keyword": "web design", "location_code": 2703, "language_code": "sk", "limit": 50}]
```

**Required:** `keyword` (string), `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `limit`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `keyword_data` (volume, CPC, difficulty) and `related_keywords[]`

---

### Bulk Keyword Difficulty

Keyword difficulty scores for a batch.

**URL:** `/v3/dataforseo_labs/google/bulk_keyword_difficulty/live`
**Method:** POST

**Request body:**
```json
[{"keywords": ["web design bratislava", "wordpress developer"], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keywords` (array), `location_code`, `language_code`

**Response:** `tasks[0].result[0].items[]` — each with `keyword`, `keyword_difficulty` (0-100)

---

### Search Intent

Classify keywords by intent. (Also documented in serp-endpoints.md for R1-SERP.)

**URL:** `/v3/dataforseo_labs/google/search_intent/live`
**Method:** POST
**Max keywords:** 1000

**Request body:**
```json
[{"keywords": ["web design bratislava", "how to build a website"], "language_code": "sk", "location_code": 2703}]
```

**Required:** `keywords` (array), `language_code`
**Optional:** `location_code`

**Response:** `tasks[0].result[0].items[]` — each with `keyword`, `keyword_intent` object, `secondary_keyword_intents`

**Intent values:** `informational`, `navigational`, `commercial`, `transactional`

---

### Keyword Overview

Quick metrics overview for a keyword batch.

**URL:** `/v3/dataforseo_labs/google/keyword_overview/live`
**Method:** POST
**Max keywords:** 700

**Request body:**
```json
[{"keywords": ["web design", "seo agency"], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keywords` (array), `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[]` — each with `keyword`, `search_volume`, `cpc`, `competition`, `keyword_difficulty`, `monthly_searches[]`

---

### Historical Keyword Data

Historical keyword metrics over time.

**URL:** `/v3/dataforseo_labs/google/historical_keyword_data/live`
**Method:** POST
**Max keywords:** 700

**Request body:**
```json
[{"keywords": ["web design"], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keywords` (array), `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[]` — each with `keyword`, `monthly_searches[]` with historical data points

---

## Keywords Data — Volume & Trends

### Search Volume (Google Ads)

Monthly volume, CPC, and competition. (Also documented in serp-endpoints.md for R1-SERP.)

**URL:** `/v3/keywords_data/google_ads/search_volume/live`
**Method:** POST
**Max keywords:** 1000

**Request body:**
```json
[{"keywords": ["web design bratislava", "wordpress developer"], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keywords` (array), `location_code`, `language_code`
**Optional:** `date_from`, `date_to` (YYYY-MM-DD), `sort_by`

**Response:** `tasks[0].result[]` — each with `keyword`, `search_volume`, `cpc`, `competition`, `competition_level`, `monthly_searches[]`

---

### Google Trends Explore

Google Trends interest over time.

**URL:** `/v3/keywords_data/google_trends/explore/live`
**Method:** POST
**Max keywords:** 5 per request

**Request body:**
```json
[{"keywords": ["web design", "ux design"], "location_code": 2703, "date_from": "2025-01-01", "date_to": "2026-03-01"}]
```

**Required:** `keywords` (array, max 5)
**Optional:** `location_code`, `language_code`, `date_from`, `date_to`, `type` ("web_search", "image_search", "news_search", "youtube_search")

**Response:** `tasks[0].result[]` — time series with `date`, `values[]` per keyword

---

### DataForSEO Trends Explore

DFS proprietary trends data (more granular than Google Trends).

**URL:** `/v3/keywords_data/dataforseo_trends/explore/live`
**Method:** POST
**Max keywords:** 5

**Request body:**
```json
[{"keywords": ["web design"], "location_code": 2703}]
```

**Required:** `keywords` (array, max 5)
**Optional:** `location_code`, `date_from`, `date_to`, `type`

**Response:** Same structure as Google Trends.

---

### DataForSEO Trends Demography

Demographic data for keyword interest.

**URL:** `/v3/keywords_data/dataforseo_trends/demography/live`
**Method:** POST
**Max keywords:** 5

**Request body:**
```json
[{"keywords": ["web design"], "location_code": 2703}]
```

**Required:** `keywords` (array, max 5)
**Optional:** `location_code`, `location_name`

**Response:** `tasks[0].result[]` — demographic breakdowns (age, gender distributions)

---

### DataForSEO Trends Subregion Interests

Regional interest data for keywords.

**URL:** `/v3/keywords_data/dataforseo_trends/subregion_interests/live`
**Method:** POST
**Max keywords:** 5

**Request body:**
```json
[{"keywords": ["web design"], "location_code": 2703}]
```

**Required:** `keywords` (array, max 5)
**Optional:** `location_code`, `location_name`

**Response:** `tasks[0].result[]` — subregion interest scores

---

### Location Lookups (Keywords Data)

**URL:** `/v3/keywords_data/google_ads/locations`
**Method:** GET

Filter by country: `/v3/keywords_data/google_ads/locations/{country_iso}`

---

### Google Trends Categories

**URL:** `/v3/keywords_data/google_trends/categories`
**Method:** GET

Returns full category tree for use in Trends requests.

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
