# R1-SERP — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — 10-20 telegraphic findings that would change what we propose, how we price it, or what we ask the client"],
  "code": "R1",
  "slug": "SERP",
  "serp_research": {
    "meta": {
      "language_location_matrix": [
        {"language": "string", "location": "string", "search_engine": "string", "location_code": "number", "language_code": "string"}
      ],
      "total_keywords": "number",
      "cap_applied": "number",
      "date_run": "string"
    },
    "client_rankings": [
      {
        "keyword": "string",
        "position": "number",
        "url": "string",
        "traffic_share": "number | null"
      }
    ],
    "keywords": [
      {
        "keyword": "string",
        "language": "string",
        "location": "string",
        "intent": "navigational | informational | commercial | transactional",
        "volume_est": "number | null",
        "client_position": "number | null",
        "top_result": "string",
        "page_type_suggestion": "string"
      }
    ],
    "competitors": [
      {
        "domain": "string",
        "site_type": "commercial | directory | media | marketplace | informational",
        "keyword_appearances": "number",
        "languages_detected": [],
        "notes": "string | null"
      }
    ],
    "notes": [
      "string"
    ]
  }
}
```

Write to `research/R1-SERP.json`.

---

## Markdown Template

Generate `research/R1-SERP.md` from the JSON:

```markdown
# SERP Research — {Client Name}

## TLDR

{bulleted list from tldr array — one line per finding, telegraphic}

---

## Overview
{2-3 sentence summary: how competitive the SERP landscape is, whether the client
appears, dominant site types in results}

## Language & Location Matrix
| Language | Location | Search Engine |
|---|---|---|
| {language} | {location} | {search_engine} |

## Client Current Rankings
| Keyword | Position | URL | Traffic Share |
|---|---|---|---|
| {keyword} | {position} | {url} | {traffic_share} |

## Keyword Results
| Keyword | Lang | Location | Intent | Volume | Client Pos | Top Result | Page Suggestion |
|---|---|---|---|---|---|---|---|
| {keyword} | {lang} | {loc} | {intent} | {vol} | {pos / —} | {domain} | {page_type} |

## Top Competitor Domains
| Domain | Site Type | Appearances | Languages | Notes |
|---|---|---|---|---|
| {domain} | {type} | {count} | {langs} | {notes} |

## Notes
- {note 1}
- {note 2}
```
