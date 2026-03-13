# DataForSEO REST API — Backlink Endpoints

Reference for backlink analysis endpoints: profile summaries, link lists, anchor analysis, bulk operations, and intersections.

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

**Target types:** All backlink endpoints accept `target` as domain (`example.com`), subdomain (`blog.example.com`), or URL (`example.com/page`). Bulk endpoints use `targets` (array).

---

## Core Endpoints

### Summary

Backlink profile summary for a domain.

**URL:** `/v3/backlinks/summary/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com"}]
```

**Required:** `target`
**Optional:** `internal_list_limit`, `backlinks_status_type` ("all", "live", "lost")

**Response:** `tasks[0].result[]` — `total_backlinks`, `referring_domains`, `referring_main_domains`, `rank`, `backlinks_nofollow`, `broken_backlinks`

**curl example:**
```
Write body: [{"target":"example.com"}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/backlinks/summary/live
```

---

### Backlinks (detailed list)

Individual backlink list with source URLs and anchor text.

**URL:** `/v3/backlinks/backlinks/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 100, "order_by": ["rank,desc"]}]
```

**Required:** `target`
**Optional:** `limit` (default 100), `offset`, `filters`, `order_by`, `backlinks_status_type`

**Response:** `tasks[0].result[0].items[]` — each with:
- `url_from` — source page URL
- `url_to` — target page URL
- `anchor` — anchor text
- `dofollow` — boolean
- `rank` — page rank score
- `first_seen`, `last_seen` — dates
- `is_new`, `is_lost` — change indicators

---

### Anchors

Anchor text distribution.

**URL:** `/v3/backlinks/anchors/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 100}]
```

**Required:** `target`
**Optional:** `limit`, `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `anchor`, `backlinks`, `referring_domains`, `referring_main_domains`

---

### Referring Domains

Top referring domains.

**URL:** `/v3/backlinks/referring_domains/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 100}]
```

**Required:** `target`
**Optional:** `limit`, `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — each with `domain`, `rank`, `backlinks`, `first_seen`, `lost_date`

---

### Competitors

Domains with similar backlink profiles.

**URL:** `/v3/backlinks/competitors/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 20}]
```

**Required:** `target`
**Optional:** `limit`, `filters`

**Response:** `tasks[0].result[0].items[]` — competing domains with overlap metrics

---

## Intersection Endpoints

### Domain Intersection

Shared referring domains across up to 20 targets.

**URL:** `/v3/backlinks/domain_intersection/live`
**Method:** POST

**Request body:**
```json
[{"targets": {"1": "domain1.com", "2": "domain2.com", "3": "domain3.com"}, "limit": 100}]
```

**Note:** `targets` is an **object** (not array) with numeric string keys.

**Required:** `targets` (object, up to 20 entries)
**Optional:** `limit`, `offset`, `filters`, `order_by`

**Response:** `tasks[0].result[0].items[]` — referring domains shared across targets

---

### Page Intersection

Shared referring pages across targets.

**URL:** `/v3/backlinks/page_intersection/live`
**Method:** POST

**Request body:**
```json
[{"targets": {"1": "domain1.com/page1", "2": "domain2.com/page2"}, "limit": 100}]
```

**Required:** `targets` (object, up to 20 entries)
**Optional:** `limit`, `offset`, `filters`

---

## Time Series Endpoints

### Timeseries Summary

Backlink trends over time.

**URL:** `/v3/backlinks/timeseries_summary/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "date_from": "2025-01-01", "date_to": "2026-03-01"}]
```

**Required:** `target`, `date_from`, `date_to`
**Optional:** `group_range` ("day", "week", "month")

**Response:** `tasks[0].result[0].items[]` — time series with `date`, `new_backlinks`, `lost_backlinks`, `new_referring_domains`

---

### Timeseries New/Lost Summary

Track new and lost backlinks over time.

**URL:** `/v3/backlinks/timeseries_new_lost_summary/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "date_from": "2025-01-01", "date_to": "2026-03-01"}]
```

**Required:** `target`
**Optional:** `date_from`, `date_to`, `group_range`

---

### Referring Networks

Referring network (IP/subnet) analysis.

**URL:** `/v3/backlinks/referring_networks/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 50}]
```

**Required:** `target`
**Optional:** `limit`, `filters`

---

## Domain Pages

### Domain Pages Summary

Summary of pages on a domain with backlink data.

**URL:** `/v3/backlinks/domain_pages_summary/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com"}]
```

**Required:** `target`

---

### Domain Pages (detailed)

List individual pages with their backlink metrics.

**URL:** `/v3/backlinks/domain_pages/live`
**Method:** POST

**Request body:**
```json
[{"target": "example.com", "limit": 100}]
```

**Required:** `target`
**Optional:** `limit`, `offset`, `filters`, `order_by`

---

## Bulk Endpoints

All bulk endpoints accept `targets` as an **array** (max 1000 items).

### Bulk Backlinks

**URL:** `/v3/backlinks/bulk_backlinks/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

**Response:** Per-target backlink count summaries.

---

### Bulk Referring Domains

**URL:** `/v3/backlinks/bulk_referring_domains/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

---

### Bulk Ranks

**URL:** `/v3/backlinks/bulk_ranks/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

**Response:** Per-target domain rank scores.

---

### Bulk Spam Score

**URL:** `/v3/backlinks/bulk_spam_score/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

**Response:** Per-target spam score (0-100).

---

### Bulk New/Lost Backlinks

**URL:** `/v3/backlinks/bulk_new_lost_backlinks/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

---

### Bulk New/Lost Referring Domains

**URL:** `/v3/backlinks/bulk_new_lost_referring_domains/live`

```json
[{"targets": ["domain1.com", "domain2.com"]}]
```

---

### Bulk Pages Summary

**URL:** `/v3/backlinks/bulk_pages_summary/live`

```json
[{"targets": ["domain1.com/page1", "domain2.com/page2"]}]
```

**Max targets:** 1000 URLs.

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
