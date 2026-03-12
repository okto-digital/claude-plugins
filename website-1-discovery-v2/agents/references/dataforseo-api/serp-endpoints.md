# DataForSEO REST API — SERP Endpoints

Reference for SERP endpoints: Google organic, YouTube, and location lookups.

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}` (base64 of `login:password`, provided in dispatch prompt)
**Content-Type:** `application/json` for all POST requests

---

## JSON Body Pattern

To avoid shell escaping issues, always write the request body to a temp file first, then reference it in curl:

```
1. Write JSON body to {working_directory}/tmp/dfs-request.json using Write tool
2. Call mcp__mcp-curl__curl_advanced with: -X POST -H "Authorization: Basic {auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json {url}
```

**Reuse the same temp file** for each request — overwrite it before each call.

---

## 1. Locations Lookup

Resolve a country or city name to a DataForSEO `location_code`.

**URL:** `https://api.dataforseo.com/v3/serp/google/locations`
**Method:** GET (no body needed — returns all locations)

**curl example:**
```
mcp__mcp-curl__curl_advanced with args:
-X GET -H "Authorization: Basic {dataforseo_auth}" https://api.dataforseo.com/v3/serp/google/locations
```

**Response fields:**
- `tasks[0].result[]` — array of location objects
- Each: `location_code` (int), `location_name` (string), `country_iso_code` (string)

**Usage:** Filter the result array client-side (in Bash with jq) to find the matching location:
```bash
echo "$response" | jq '[.tasks[0].result[] | select(.location_name == "Slovakia")] | .[0].location_code'
```

**Tip:** Common codes — US: 2840, UK: 2826, Germany: 2276, Slovakia: 2703, Czech Republic: 2203. If you know the code, skip this call.

---

## 2. SERP Organic Live Advanced

Fetch Google organic SERP results for keywords.

**URL:** `https://api.dataforseo.com/v3/serp/google/organic/live/advanced`
**Method:** POST
**Max items per request:** 100 (each item is one keyword + location + language combination)

**Request body schema:**
```json
[
  {
    "keyword": "web design bratislava",
    "location_code": 2703,
    "language_code": "sk",
    "device": "desktop",
    "os": "windows",
    "depth": 10
  }
]
```

**Required fields per item:**
- `keyword` (string) — the search query
- `location_code` (int) — from locations lookup or known code
- `language_code` (string) — e.g., "en", "sk", "cs"

**Optional fields:**
- `device` (string) — "desktop" (default) or "mobile"
- `os` (string) — "windows" (default)
- `depth` (int) — number of results, default 10

**curl example:**
```
Write body to {working_directory}/tmp/dfs-request.json:
[{"keyword":"web design bratislava","location_code":2703,"language_code":"sk","device":"desktop","depth":10}]

mcp__mcp-curl__curl_advanced with args:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/serp/google/organic/live/advanced
```

**Response fields (per task):**
- `tasks[i].result[0].keyword` — queried keyword
- `tasks[i].result[0].spell.type` — spell correction type (if any)
- `tasks[i].result[0].item_types` — array of result types present (e.g., "organic", "featured_snippet", "local_pack")
- `tasks[i].result[0].items[]` — SERP items:
  - `type` — "organic", "featured_snippet", "local_pack", "people_also_ask", etc.
  - `rank_group` — position in SERP
  - `rank_absolute` — absolute position including all types
  - `domain` — result domain
  - `url` — full URL
  - `title` — result title
  - `description` — snippet text

**Batching:** Send up to 100 keyword objects in one request array. Each becomes a separate task in the response.

---

## 3. Search Intent Classification

Classify keywords by search intent (navigational, informational, commercial, transactional).

**URL:** `https://api.dataforseo.com/v3/dataforseo_labs/google/search_intent/live`
**Method:** POST
**Max keywords per request:** 1000

**Request body schema:**
```json
[
  {
    "keywords": ["web design bratislava", "wordpress developer", "tvorba webovych stranok"],
    "language_code": "sk",
    "location_code": 2703
  }
]
```

**Required fields:**
- `keywords` (array of strings) — up to 1000 keywords
- `language_code` (string)
- `location_code` (int)

**curl example:**
```
Write body to {working_directory}/tmp/dfs-request.json:
[{"keywords":["web design bratislava","wordpress developer"],"language_code":"sk","location_code":2703}]

mcp__mcp-curl__curl_advanced with args:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/dataforseo_labs/google/search_intent/live
```

**Response fields:**
- `tasks[0].result[0].items[]`:
  - `keyword` — the keyword
  - `keyword_intent` — object with intent labels
  - `secondary_keyword_intents` — additional intents if mixed

**Intent values:** `informational`, `navigational`, `commercial`, `transactional`

---

## 4. Search Volume (Google Ads)

Get monthly search volume, CPC, and competition data for keywords.

**URL:** `https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live`
**Method:** POST
**Max keywords per request:** 1000

**Request body schema:**
```json
[
  {
    "keywords": ["web design bratislava", "wordpress developer"],
    "location_code": 2703,
    "language_code": "sk",
    "date_from": "2025-03-01",
    "date_to": "2026-03-01"
  }
]
```

**Required fields:**
- `keywords` (array of strings) — up to 1000 keywords
- `location_code` (int)
- `language_code` (string)

**Optional fields:**
- `date_from`, `date_to` (string, YYYY-MM-DD) — period for volume data. Omit for latest available.
- `sort_by` (string) — "relevance" (default) or "search_volume"

**curl example:**
```
Write body to {working_directory}/tmp/dfs-request.json:
[{"keywords":["web design bratislava","wordpress developer"],"location_code":2703,"language_code":"sk"}]

mcp__mcp-curl__curl_advanced with args:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live
```

**Response fields:**
- `tasks[0].result[]`:
  - `keyword` — the keyword
  - `search_volume` — average monthly searches (int)
  - `competition` — competition level (float 0-1)
  - `competition_level` — "LOW", "MEDIUM", "HIGH"
  - `cpc` — cost per click (float, USD)
  - `monthly_searches[]` — array of {year, month, search_volume} for trend data

---

## 5. YouTube Organic SERP

YouTube search results for keywords.

**URL:** `https://api.dataforseo.com/v3/serp/youtube/organic/live/advanced`
**Method:** POST
**Max items per request:** 100

**Request body:**
```json
[{"keyword": "web design tutorial", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keyword`, `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `depth` (default 20)

**Response:** `tasks[i].result[0].items[]` — each with:
- `title` — video title
- `url` — video URL
- `channel_name` — channel name
- `views_count` — view count
- `timestamp` — upload date
- `description` — video description

---

## 6. YouTube Video Info

Metadata for a specific YouTube video.

**URL:** `https://api.dataforseo.com/v3/serp/youtube/video_info/live/advanced`
**Method:** POST

**Request body:**
```json
[{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}]
```

**Required:** `video_id`, `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — title, channel, views, likes, description, publish date

---

## 7. YouTube Video Comments

Top comments on a YouTube video.

**URL:** `https://api.dataforseo.com/v3/serp/youtube/video_comments/live/advanced`
**Method:** POST

**Request body:**
```json
[{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}]
```

**Required:** `video_id`, `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — comments with engagement metrics

---

## 8. YouTube Video Subtitles

Video subtitles/transcript.

**URL:** `https://api.dataforseo.com/v3/serp/youtube/video_subtitles/live/advanced`
**Method:** POST

**Request body:**
```json
[{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}]
```

**Required:** `video_id`, `location_code` or `location_name`, `language_code` or `language_name`

**Response:** `tasks[0].result[0].items[]` — subtitle text segments

---

## Error Handling

All responses include a `status_code` and `status_message` per task:
- `20000` — Success
- `40000` — Bad request (check parameters)
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error

Check `tasks[i].status_code` for each task in the response. If a task fails, note the error and continue with other tasks.

---

## Rate Limits

- No explicit rate limit per second, but large batches are preferred over many small requests
- SERP Organic: max 100 items per request
- Search Intent: max 1000 keywords per request
- Search Volume: max 1000 keywords per request
- Locations: returns full list (~100k items), cache locally if needed
