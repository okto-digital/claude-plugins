# DataForSEO REST API — AI Optimization Endpoints

Reference for AI visibility endpoints: ChatGPT scraper and LLM mentions analysis.

**Base URL:** `https://api.dataforseo.com`
**Auth:** `Authorization: Basic {dataforseo_auth}`
**Content-Type:** `application/json` for all POST requests
**JSON body pattern:** Write to `{working_directory}/tmp/dfs-request.json`, reference with `-d @{path}`

---

## ChatGPT Scraper

Scrape ChatGPT web search responses for a query — see which domains/URLs ChatGPT cites.

**URL:** `/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced`
**Method:** POST

**Request body:**
```json
[{"keyword": "best web design agencies bratislava", "location_code": 2703, "language_code": "sk"}]
```

**Required:** `keyword`, `location_code` or `location_name`, `language_code` or `language_name`
**Optional:** `depth` (number of results)

**Response:** `tasks[0].result[0].items[]` — each with:
- `type` — response element type
- `text` — ChatGPT response text
- `references[]` — cited URLs with:
  - `url` — source URL
  - `domain` — source domain
  - `title` — reference title
  - `snippet` — reference snippet

**curl example:**
```
Write body: [{"keyword":"best web design agencies bratislava","location_code":2703,"language_code":"sk"}]

mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced
```

---

## LLM Mentions — Search

Search for brand/keyword mentions across LLM responses.

**URL:** `/v3/ai_optimization/llm_mentions/search/live`
**Method:** POST

**Request body:**
```json
[{"target": [{"domain": "example.com"}], "location_code": 2703, "language_code": "sk", "limit": 20}]
```

**Required:** `target` (array of entities, max 10)
**Entity format:** Each entity is an object with either:
- `domain` (string, max 63 chars) — track domain mentions
- `keyword` (string, max 250 chars) — track keyword mentions

**Optional:** `location_code` (default 2840), `language_code` (default "en"), `platform` ("google" for AI Overview, "chat_gpt" for ChatGPT), `limit`, `offset`, `filters`

**Response:** `tasks[0].result[0].items[]` — each with:
- `keyword` — query that triggered the mention
- `url` — URL cited in LLM response
- `domain` — domain mentioned
- `position` — position in LLM response
- `platform` — which LLM platform
- `date` — when the mention was recorded

---

## LLM Mentions — Top Domains

Top cited domains for a topic across LLMs.

**URL:** `/v3/ai_optimization/llm_mentions/top_domains/live`
**Method:** POST

**Request body:**
```json
[{"target": [{"keyword": "web design"}], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (array of entities, max 10)
**Optional:** `location_code`, `language_code`, `platform`, `limit`

**Response:** `tasks[0].result[0].items[]` — each with `domain`, `mention_count`, `percentage`, `platform`

---

## LLM Mentions — Top Pages

Top cited pages for a topic across LLMs.

**URL:** `/v3/ai_optimization/llm_mentions/top_pages/live`
**Method:** POST

**Request body:**
```json
[{"target": [{"keyword": "web design bratislava"}], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (array of entities, max 10)
**Optional:** `location_code`, `language_code`, `platform`, `limit`

**Response:** `tasks[0].result[0].items[]` — each with `url`, `domain`, `mention_count`, `percentage`

---

## LLM Mentions — Aggregated Metrics

Aggregate LLM mention metrics — overall visibility across LLMs.

**URL:** `/v3/ai_optimization/llm_mentions/aggregated_metrics/live`
**Method:** POST

**Request body:**
```json
[{"target": [{"domain": "example.com"}], "location_code": 2703, "language_code": "sk"}]
```

**Required:** `target` (array of entities, max 10)
**Optional:** `location_code`, `language_code`, `platform`

**Response:** `tasks[0].result[0]`:
- `total_mentions` — total mention count
- `total_keywords` — keywords triggering mentions
- `platforms` — per-platform breakdown
- `trends` — mention trends over time

---

## Shared Notes

- **Default platform:** "google" (Google AI Overview). Set `"platform": "chat_gpt"` for ChatGPT results.
- **Default location:** 2840 (United States). Always specify if targeting non-US markets.
- **target structure:** Array of entity objects — can mix `domain` and `keyword` entities in the same request (max 10 total).

---

## Error Handling

All responses include `status_code` per task:
- `20000` — Success
- `40000` — Bad request
- `40100` — Authentication failed
- `40200` — Insufficient credits
- `50000` — Internal server error
