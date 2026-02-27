# MCP Tool Mapping: SEO Keyword Research

**Purpose:** Lookup table mapping keyword research actions to concrete MCP tool calls for DataForSEO and SE Ranking servers.

**Usage:** Referenced by seo-keyword-research skill during TIER 1 operations. Tool names depend on the server registration name in `.mcp.json` -- use substring matching to handle variations (e.g., match `dataforseo` or `datalabs` in tool names).

---

## Tool Detection

Probe available tools by looking for these substrings in tool names:

| Substring | Server | Priority |
|---|---|---|
| `dataforseo` or `datalabs` | DataForSEO | 1 (preferred) |
| `seo-data-api` or `seranking` or `DATA_` | SE Ranking | 2 |

If both are available, prefer DataForSEO (richer keyword intelligence data including search intent and keyword difficulty in a single call). If neither is found, fall through to TIER 2 (WebSearch) or TIER 3 (estimates).

---

## DataForSEO MCP Server

**Source:** [dataforseo.com/help-center/connect-claude-to-dataforseo-mcp-very-simple-guide](https://dataforseo.com/help-center/connect-claude-to-dataforseo-mcp-very-simple-guide)
**Repository:** `dataforseo/mcp-server-typescript`
**Package:** `dataforseo-mcp-server`

### Configuration

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your_api_login",
        "DATAFORSEO_PASSWORD": "your_api_password",
        "ENABLED_MODULES": "KEYWORDS_DATA,DATAFORSEO_LABS"
      }
    }
  }
}
```

**Required modules for keyword research:** `KEYWORDS_DATA`, `DATAFORSEO_LABS`

### Tools for Keyword Research

#### `keywords-google-ads-search-volume` -- Bulk Search Volume

Primary tool for getting search volume, CPC, and competition for a list of keywords.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `keywords` | string[] | Yes | -- | Array of keywords (max ~700 per request) |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |

**Response fields per keyword:**
- `keyword` -- the keyword
- `search_volume` -- monthly search volume (integer)
- `cpc` -- cost per click (float)
- `competition` -- competition level (0.0-1.0)
- `high_top_of_page_bid`, `low_top_of_page_bid` -- bid range

**Batch limit:** ~700 keywords per request (API-side limit).

#### `datalabs_google_keywords_for_site` -- Keywords for Domain

Discovers keywords relevant to a target domain. Use for seed generation from client and competitor domains.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `target` | string | Yes | -- | Domain name |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |
| `limit` | number | No | 10 | Max results (1-1000) |
| `include_subdomains` | boolean | No | -- | Include subdomain keywords |

**Response fields per keyword:**
- `keyword` -- the keyword
- `keyword_info.search_volume` -- monthly volume
- `keyword_info.cpc` -- cost per click
- `keyword_info.competition` -- competition level
- `keyword_properties.keyword_difficulty` -- KD score (0-100)
- `search_intent_info.main_intent` -- intent classification

#### `datalabs_google_keywords_suggestions` -- Keyword Ideas

Generates keyword suggestions from a seed keyword. Use for keyword expansion.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `keyword` | string | Yes | -- | Seed keyword |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |
| `limit` | number | No | 10 | Max results (1-1000) |

**Response:** Same schema as `keywords_for_site` (includes volume, CPC, KD, intent per keyword).

#### `datalabs_google_related_keywords` -- Related Keywords

Returns "searches related to" keywords. Use for discovering adjacent topics.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `keyword` | string | Yes | -- | Target keyword |
| `depth` | number | No | 1 | Search depth (0-4, higher = more results, more cost) |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |
| `limit` | number | No | 10 | Max results (1-1000) |

**Response:** Same schema as `keywords_for_site`.

#### `datalabs_bulk_keyword_difficulty` -- Bulk KD Scores

Bulk keyword difficulty lookup. Use after collecting keywords to batch-fetch KD scores.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `keywords` | string[] | Yes | -- | Array of keywords (max 1000) |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |

**Response:** `keyword`, `keyword_difficulty` (0-100) per keyword.

#### `datalabs_google_ranked_keywords` -- Domain Ranked Keywords

Returns keywords a domain currently ranks for. Use for competitor keyword analysis.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `target` | string | Yes | -- | Domain or URL |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |
| `limit` | number | No | 10 | Max results (1-1000) |

**Response:** Keywords with ranking positions, volume, and metrics.

#### `datalabs_google_domain_intersections` -- Competitor Keyword Overlap

Finds keywords where two domains both rank. Use for competitor overlap analysis.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `target1` | string | Yes | -- | First domain |
| `target2` | string | Yes | -- | Second domain |
| `location_name` | string | No | "United States" | Full location name |
| `language_code` | string | No | "en" | Language code |
| `limit` | number | No | 10 | Max results (1-1000) |

**Response:** Keywords with volume, KD, intent, plus ranking position and URL for each domain.

### DataForSEO Common Response Schema

Most DATAFORSEO_LABS tools return this consistent shape:

```
keyword: "example keyword"
keyword_info:
  search_volume: 12100
  cpc: 2.45
  competition: 0.67
keyword_properties:
  keyword_difficulty: 45
search_intent_info:
  main_intent: "informational"
```

### DataForSEO Rate Limits

No server-side rate limit configuration. Limits enforced by DataForSEO API based on account plan (credit-based system). Each call costs credits depending on endpoint and parameters.

---

## SE Ranking MCP Server

**Source:** [seranking.com/api/integrations/mcp](https://seranking.com/api/integrations/mcp/)
**Repository:** `seranking/seo-data-api-mcp-server`

### Configuration

```json
{
  "mcpServers": {
    "seo-data-api-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "DATA_API_TOKEN",
        "se-ranking/seo-data-api-mcp-server"
      ],
      "env": {
        "DATA_API_TOKEN": "<your-api-token>"
      }
    }
  }
}
```

**Token retrieval:** https://online.seranking.com/admin.api.dashboard.html

### Tool Naming Convention

SE Ranking tools are prefixed `DATA_` for Data API tools. When registered as `seo-data-api-mcp`, the full Claude Code tool name is `mcp__seo-data-api-mcp__DATA_exportKeywords`.

### Tools for Keyword Research

#### `DATA_exportKeywords` -- Bulk Keyword Metrics

Primary tool for batch keyword volume, CPC, difficulty, and competition lookup.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | string | Yes | -- | Alpha-2 country code (e.g., "us", "gb") |
| `keywords` | string[] | Yes | -- | Array of keywords (max 5,000) |
| `sort` | string | No | "cpc" | Sort by: volume, cpc, difficulty, competition |
| `cols` | string | No | all | Comma-separated: keyword, volume, cpc, competition, difficulty, history_trend |

**Response fields per keyword:**
- `keyword` -- the keyword
- `volume` -- monthly search volume (integer)
- `cpc` -- cost per click (float)
- `competition` -- competition level (0.0-1.0)
- `difficulty` -- keyword difficulty (0-100)
- `history_trend` -- object with 12 months of volume history

**Batch limit:** 5,000 keywords per call.

#### `DATA_getRelatedKeywords` -- Semantically Related Keywords

Returns topically related keywords based on shared SERP URLs.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | string | Yes | -- | Alpha-2 country code |
| `keyword` | string | Yes | -- | Seed keyword |
| `limit` | integer | No | 100 | Max results (1-1000) |
| `filter_volume_from` | integer | No | -- | Min monthly volume |
| `filter_difficulty_from` | integer | No | -- | Min difficulty |
| `filter_difficulty_to` | integer | No | -- | Max difficulty |
| `filter_intents` | string | No | -- | Comma-separated: I, N, T, C, L |

**Response fields per keyword:**
- `keyword`, `volume`, `cpc`, `difficulty`, `competition`
- `intents` -- array of intent codes: I(nformational), N(avigational), T(ransactional), C(ommercial), L(ocal)
- `serp_features` -- array of SERP feature codes
- `relevance` -- topical relevance score

#### `DATA_getSimilarKeywords` -- Synonyms and Close Variations

Same parameters and response as `getRelatedKeywords`. Returns synonyms and different phrasings with same intent.

#### `DATA_getLongTailKeywords` -- Long-tail Variations

Same parameters and response as `getRelatedKeywords`. Returns longer-form keyword variations.

#### `DATA_getKeywordQuestions` -- Question Keywords

Same parameters and response as `getRelatedKeywords`. Returns question-phrased keywords.

#### `DATA_getDomainKeywords` -- Domain Organic Keywords

Returns keywords a domain ranks for organically.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | string | Yes | -- | Alpha-2 country code |
| `domain` | string | Yes | -- | Domain to analyze |
| `type` | string | No | "organic" | "organic" or "adv" (paid) |
| `limit` | integer | No | 100 | Results per page (1-1000) |
| `filter_volume_from` | integer | No | -- | Min monthly volume |
| `filter_intents` | string | No | -- | Comma-separated intent codes |

**Response:** Keywords with position, URL, volume, traffic, CPC, competition, KEI.

#### `DATA_getDomainCompetitors` -- Organic Competitors

Returns competitor domains based on keyword overlap.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | string | Yes | -- | Alpha-2 country code |
| `domain` | string | Yes | -- | Domain to find competitors for |
| `type` | string | No | "organic" | "organic" or "adv" |

#### `DATA_getDomainKeywordsComparison` -- Keyword Overlap Comparison

Compares keyword rankings between two domains.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source` | string | Yes | -- | Alpha-2 country code |
| `domain` | string | Yes | -- | Primary domain |
| `compare` | string | Yes | -- | Competitor domain |
| `diff` | string | No | "0" | "0" = common keywords, "1" = unique to primary |
| `limit` | integer | No | 100 | Results per page (1-1000) |

**Response:** keyword, volume, cpc, competition, position (both domains), URL (both domains).

### SE Ranking Intent Codes

| Code | Intent |
|---|---|
| `I` | Informational |
| `N` | Navigational |
| `T` | Transactional |
| `C` | Commercial |
| `L` | Local |

### SE Ranking Rate Limits

| API Type | Limit |
|---|---|
| Data API | **10 requests/second** |
| Project API | **5 requests/second** |

HTTP 429 returned when exceeded. Implement delays between batches accordingly.

---

## Action-to-Tool Mapping

Quick reference for which tool to call for each research action:

| Action | DataForSEO Tool | SE Ranking Tool |
|---|---|---|
| Seeds from domain | `datalabs_google_keywords_for_site` | `DATA_getDomainKeywords` |
| Keyword ideas/expansion | `datalabs_google_keywords_suggestions` | `DATA_getRelatedKeywords` |
| Related keywords | `datalabs_google_related_keywords` | `DATA_getSimilarKeywords` |
| Long-tail variations | `datalabs_google_keywords_suggestions` (filtered) | `DATA_getLongTailKeywords` |
| Question keywords | `datalabs_google_keywords_suggestions` (filtered) | `DATA_getKeywordQuestions` |
| Bulk volume + KD | `keywords-google-ads-search-volume` + `datalabs_bulk_keyword_difficulty` | `DATA_exportKeywords` |
| Competitor keywords | `datalabs_google_ranked_keywords` | `DATA_getDomainKeywords` |
| Competitor overlap | `datalabs_google_domain_intersections` | `DATA_getDomainKeywordsComparison` |
| Competitor discovery | `datalabs_google_domain_competitors` | `DATA_getDomainCompetitors` |

### Batch Strategy

**DataForSEO:**
1. Use `keywords_for_site` for client + each competitor (limit: 100-200 each)
2. Use `keywords_suggestions` for top 5-10 seeds (limit: 50-100 each)
3. Collect all unique keywords, then batch `search_volume` (up to 700/call) + `bulk_keyword_difficulty` (up to 1000/call)

**SE Ranking:**
1. Use `getDomainKeywords` for client + each competitor (limit: 200 each)
2. Use `getRelatedKeywords` + `getLongTailKeywords` + `getKeywordQuestions` for top seeds
3. Collect all unique keywords, then batch `exportKeywords` (up to 5000/call -- includes volume, KD, CPC in one call)
4. Respect 10 req/sec rate limit -- add 100ms delay between calls

---

## WebSearch Fallback (TIER 2)

When no MCP tools are available, use WebSearch for signal-based estimation:

| Signal | Method | Indicates |
|---|---|---|
| Search result count | WebSearch `"keyword"` -- note total results | Rough popularity indicator |
| Ad density | WebSearch `keyword` -- count sponsored results | Commercial value (CPC proxy) |
| SERP richness | WebSearch `keyword` -- check for featured snippets, PAA, knowledge panels | Competition/difficulty proxy |
| Autocomplete depth | WebSearch `keyword a`, `keyword b`... -- count suggestions | Search demand indicator |
| PAA questions | WebSearch `keyword` -- extract "People Also Ask" | Long-tail expansion source |

**Estimation methodology:**
- Volume: Cross-reference result count + autocomplete depth + PAA presence
  - High (>5K/mo est.): >100M results, rich autocomplete, multiple PAA
  - Medium (~1K-5K/mo est.): 10M-100M results, some autocomplete
  - Low (<1K/mo est.): <10M results, sparse autocomplete
- Difficulty: Based on result quality + SERP features
  - High: Major brands dominate, rich SERP features, knowledge panel
  - Medium: Mix of authority and niche sites
  - Low: Few authority sites, sparse SERP features
- Format as "Medium (~1,000-3,000/mo est.)" to distinguish from TIER 1 actuals
