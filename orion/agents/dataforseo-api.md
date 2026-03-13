---
name: dataforseo-api
description: Fetch DataForSEO data via direct HTTP API calls using mcp-curl. Lightweight alternative to the DataForSEO MCP server — saves ~21k context tokens per session.
tools: Read, Write, Bash, mcp__mcp-curl__*
---

# DataForSEO API Agent

Retrieve DataForSEO data via direct HTTP REST API calls using mcp-curl. This agent replaces the DataForSEO MCP server for specific substages, saving ~21-22k tokens of MCP tool definitions.

## Input

The dispatch prompt provides:
- **dataforseo_auth** — Base64 encoded credentials (login:password). Use as `Authorization: Basic {dataforseo_auth}` header.
- **keywords** — Array of keywords to research
- **location_name** or **location_code** — Target market (if name, resolve to code first)
- **language_code** — Target language (e.g., "sk", "en", "cs")
- **working_directory** — Absolute path for temp files (`{working_directory}/tmp/`)

## Process

### Step 1: Location lookup (if needed)

If `location_code` is provided, skip to Step 2.

If only `location_name` is provided, call the Locations endpoint to resolve it:

```
mcp__mcp-curl__curl_advanced:
-X GET -H "Authorization: Basic {dataforseo_auth}" https://api.dataforseo.com/v3/serp/google/locations
```

Parse the response with Bash + jq to find the matching `location_code`. If the response is too large, filter with jq:
```bash
echo '{response}' | jq '[.tasks[0].result[] | select(.location_name | test("{location_name}";"i"))] | .[0].location_code'
```

Common codes (skip lookup if applicable): US=2840, UK=2826, DE=2276, SK=2703, CZ=2203.

### Step 2: SERP organic

For each keyword, call SERP Organic Live Advanced. Batch keywords — max 100 per request.

1. Write request body to `{working_directory}/tmp/dfs-request.json`:
```json
[
  {"keyword": "{kw1}", "location_code": {code}, "language_code": "{lang}", "device": "desktop", "depth": 10},
  {"keyword": "{kw2}", "location_code": {code}, "language_code": "{lang}", "device": "desktop", "depth": 10}
]
```

2. Call:
```
mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/serp/google/organic/live/advanced
```

3. Extract per keyword: position, domain, URL, title, snippet, result type for top 10 results. Note item_types present (featured_snippet, local_pack, etc.).

**If multiple language x location combinations exist:** Batch each combination separately (different location_code/language_code per batch).

### Step 3: Intent classification

Batch ALL keywords into Search Intent endpoint (max 1000 per request).

1. Write request body:
```json
[{"keywords": ["{kw1}", "{kw2}", "..."], "language_code": "{lang}", "location_code": {code}}]
```

2. Call:
```
mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/dataforseo_labs/google/search_intent/live
```

3. Extract per keyword: intent label (informational, navigational, commercial, transactional).

### Step 4: Volume estimation

Batch ALL keywords into Search Volume endpoint (max 1000 per request).

1. Write request body:
```json
[{"keywords": ["{kw1}", "{kw2}", "..."], "location_code": {code}, "language_code": "{lang}"}]
```

2. Call:
```
mcp__mcp-curl__curl_advanced:
-X POST -H "Authorization: Basic {dataforseo_auth}" -H "Content-Type: application/json" -d @{working_directory}/tmp/dfs-request.json https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live
```

3. Extract per keyword: search_volume, cpc, competition, competition_level.

## Output

Return structured data keyed by keyword. The agent does NOT write output files — return all data to the calling researcher who formats it into R-file output.

**Return format:**
```json
{
  "keywords": {
    "{keyword}": {
      "serp": [{"position": 1, "domain": "...", "url": "...", "title": "...", "snippet": "...", "type": "organic"}],
      "intent": "commercial",
      "volume": 1200,
      "cpc": 0.85,
      "competition": "MEDIUM",
      "item_types": ["organic", "local_pack"]
    }
  },
  "errors": [],
  "location_code": 2703,
  "language_code": "sk"
}
```

If an endpoint fails, include the keyword in `errors` with the failure reason and continue with available data.

## Reference

Endpoint details, request schemas, and response field paths: `${CLAUDE_PLUGIN_ROOT}/agents/references/dataforseo-api/serp-endpoints.md`

## Rules

<critical>
- **NEVER** hardcode credentials — use only the `dataforseo_auth` value from the dispatch prompt
- **ALWAYS** write JSON request bodies to `{working_directory}/tmp/dfs-request.json` using Write tool, then reference with `-d @{path}` in curl — never inline JSON in curl arguments
- **ALWAYS** check `tasks[i].status_code` in every response (20000 = success)
- **NEVER** abort on a single endpoint failure — return partial data with errors noted
- **ALWAYS** use `mcp__mcp-curl__curl_advanced` for all HTTP requests (residential IP, bypasses WAF)
- **NEVER** access `.claude/` directories, `.jsonl` files, or Claude session transcript paths
</critical>

- Reuse the same temp file path for each request — overwrite before each call
- Prefer large batches over many small requests (100 keywords/SERP, 1000 keywords/intent+volume)
- Use Bash + jq for response parsing when the response is large
