# DataForSEO REST API — On-Page & Domain Analytics Endpoints

Reference for on-page analysis (instant pages, content parsing, Lighthouse) and domain analytics (technology detection, WHOIS).

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

---

## On-Page Analysis

### Instant Pages

Quick page analysis — status codes, meta tags, content size, timing, broken links.

**URL:** `/v3/on_page/instant_pages`
**Method:** POST
**Max tasks per request:** 20 (max 5 identical domains)

**Note:** No `/live` suffix on this endpoint.

**Request body:**
```json
[{"url": "https://example.com/page", "enable_javascript": true}]
```

**Required:** `url` (absolute URL with protocol)
**Optional:** `enable_javascript` (boolean, default false), `custom_user_agent`

**Response:** `tasks[0].result[]` — each with:
- `status_code` — HTTP status
- `meta` — title, description, robots, canonical
- `page_timing` — connection, download, rendering times
- `onpage_score` — overall page quality score (0-100)
- `total_dom_size` — page size in bytes
- `broken_resources` — count of broken links/images
- `duplicate_title`, `duplicate_description` — boolean flags

**curl example:**
```
Write body: [{"url":"https://example.com","enable_javascript":true}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/on_page/instant_pages
```

---

### Content Parsing

Extract and parse page content — plain text, word count, structure.

**URL:** `/v3/on_page/content_parsing/live`
**Method:** POST

**Request body:**
```json
[{"url": "https://example.com/page"}]
```

**Required:** `url`
**Optional:** `enable_javascript`

**Response:** `tasks[0].result[0].items[]` — each with:
- `page_content` — extracted plain text content
- `page_content_plain_text` — cleaned text
- `page_content_meta` — word_count, character_count, sentence_count
- `page_content_structure` — headings hierarchy

---

### Lighthouse

Full Lighthouse audit — performance, accessibility, best practices, SEO, Core Web Vitals.

**URL:** `/v3/on_page/lighthouse/live/json`
**Method:** POST

**Note:** Path includes `/json` suffix for JSON response format.

**Request body:**
```json
[{"url": "https://example.com", "for_mobile": false, "categories": ["performance", "accessibility", "best-practices", "seo"]}]
```

**Required:** `url` (absolute URL with protocol)
**Optional:** `for_mobile` (boolean, default false), `categories` (array — "performance", "accessibility", "best-practices", "seo"), `audits` (array of specific audit names)

**Response:** `tasks[0].result[0]`:
- `categories` — scores per category (0-1 scale, multiply by 100):
  - `performance.score`, `accessibility.score`, `best-practices.score`, `seo.score`
- `audits` — individual audit results with scores and details
- Core Web Vitals in audits: `largest-contentful-paint`, `first-contentful-paint`, `cumulative-layout-shift`, `total-blocking-time`, `speed-index`

---

## Domain Analytics

### Technology Detection

Detect technology stack (CMS, frameworks, analytics, CDN, etc.).

**URL:** `/v3/domain_analytics/technologies/domain_technologies/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com"}]
```

**Required:** `target` (domain name without protocol)

**Response:** `tasks[0].result[0].items[]` — each with:
- `technology` — name (e.g., "WordPress", "Google Analytics")
- `category` — type (e.g., "CMS", "Analytics", "CDN", "JavaScript framework")
- `version` — detected version (if available)

**curl example:**
```
Write body: [{"target":"example.com"}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/domain_analytics/technologies/domain_technologies/live
```

---

### WHOIS Overview

Domain registration and WHOIS data.

**URL:** `/v3/domain_analytics/whois/overview/live`
**Method:** POST

**Request body:**
```json
[{"filters": ["domain", "=", "example.com"], "limit": 1}]
```

**Note:** This endpoint uses `filters` to query specific domains, not a `target` parameter.

**Required:** None strictly required — use `filters` to scope
**Optional:** `filters` (array), `limit`, `offset`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with:
- `domain` — domain name
- `registrar` — registrar name
- `create_datetime` — registration date
- `expiration_datetime` — expiry date
- `updated_datetime` — last update
- `name_servers` — array of nameservers

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
