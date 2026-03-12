# DataForSEO REST API — Content & Business Data Endpoints

Reference for content analysis (search, summary, phrase trends) and business data (business listings).

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

---

## Content Analysis

### Content Search

Search for online content by topic — returns articles, pages with quality and sentiment scores.

**URL:** `/v3/content_analysis/search/live`
**Method:** POST

**Request body:**
```json
[{"keyword": "web design trends", "search_mode": "as_is", "limit": 20}]
```

**Required:** `keyword`
**Optional:** `search_mode` ("as_is", "url"), `limit`, `offset`, `filters`, `order_by`, `page_type` ("ecommerce", "news", "blogs", "message-boards", "organization"), `internal_list_limit`

**Response:** `tasks[0].result[0].items[]` — each with:
- `url` — content URL
- `domain` — source domain
- `title` — page title
- `main_domain_rank` — domain authority score
- `page_types` — array of content types
- `content_quality_score` — quality score (0-100)
- `sentiment_connotations` — positive, negative, neutral scores
- `text_category` — content category
- `date_published` — publication date

**curl example:**
```
Write body: [{"keyword":"web design trends","limit":20}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/content_analysis/search/live
```

---

### Content Summary

Aggregated content quality analysis for a topic.

**URL:** `/v3/content_analysis/summary/live`
**Method:** POST

**Request body:**
```json
[{"keyword": "web design"}]
```

**Required:** `keyword`
**Optional:** `page_type`, `internal_list_limit`, `search_mode`

**Response:** `tasks[0].result[0]`:
- `total_count` — total content items found
- `sentiment_connotations` — aggregate sentiment distribution
- `connotation_types` — positive/negative/neutral breakdown
- `text_categories` — content category distribution
- `page_types` — content type distribution
- `top_domains` — most frequent source domains

---

### Phrase Trends

Track phrase/topic trends over time.

**URL:** `/v3/content_analysis/phrase_trends/live`
**Method:** POST

**Request body:**
```json
[{"keyword": "web design", "date_from": "2025-01-01", "date_to": "2026-03-01"}]
```

**Required:** `keyword`, `date_from`
**Optional:** `date_to`, `page_type`, `search_mode`

**Response:** `tasks[0].result[0].items[]` — time series with:
- `date` — period date
- `top_domains` — most active domains in period
- `sentiment_connotations` — sentiment distribution for period
- `connotation_types` — positive/negative/neutral for period

---

## Business Data

### Business Listings Search

Search for business listings by keyword and/or location.

**URL:** `/v3/business_data/business_listings/search/live`
**Method:** POST

**Request body:**
```json
[{"categories": ["Web Design"], "location_coordinate": {"latitude": 48.1486, "longitude": 17.1077, "radius": 50000}, "limit": 20}]
```

**Required:** None strictly required — but must include at least one scoping parameter to get useful results
**Scoping parameters:** `categories` (array), `title` (business name), `location_coordinate` (object with `latitude`, `longitude`, `radius` in meters), `filters`
**Optional:** `limit`, `offset`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with:
- `title` — business name
- `category` — primary category
- `additional_categories` — secondary categories
- `address` — full address string
- `address_info` — structured (city, region, zip, country)
- `phone` — phone number
- `domain` — website domain
- `url` — website URL
- `rating` — aggregate rating (object with `value`, `votes_count`)
- `total_photos` — photo count
- `is_claimed` — whether listing is claimed

**curl example:**
```
Write body: [{"categories":["Web Design"],"location_coordinate":{"latitude":48.1486,"longitude":17.1077,"radius":50000},"limit":20}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/business_data/business_listings/search/live
```

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
