# R2-Keywords — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R2",
  "slug": "Keywords",
  "search_landscape": {
    "meta": {
      "total_keywords": "number",
      "cap_applied": "number",
      "date_run": "string",
      "competitors_analysed": []
    },
    "keywords": [
      {
        "keyword": "string",
        "language": "string",
        "location": "string",
        "intent": "navigational | informational | commercial | transactional",
        "volume": "number | null",
        "difficulty": "number | null",
        "trend": "rising | stable | declining | seasonal | null",
        "priority": "high | medium | low",
        "page_group": "string",
        "source": "seed | expanded | gap_opportunity",
        "gap_competitor": "string | null"
      }
    ],
    "gap_analysis": {
      "keywords_not_targeted": [
        {
          "keyword": "string",
          "owned_by": "string",
          "volume": "number | null",
          "difficulty": "number | null",
          "opportunity": "string"
        }
      ],
      "summary": "string"
    },
    "page_groups": {
      "homepage": [],
      "product_category": [],
      "product_detail": [],
      "service_page": [],
      "location_page": [],
      "blog": [],
      "other": []
    },
    "notes": [
      "string"
    ]
  }
}
```

Write to `research/R2-Keywords.json`.

---

## Markdown Template

Generate `research/R2-Keywords.md` from the JSON:

```markdown
# Keyword Opportunity — [Client Name]

## Overview
[2-3 sentence summary of the keyword landscape — total opportunity size,
competitive difficulty level, key gaps identified, and top page groups by volume]

## Keyword Table
| Keyword | Intent | Volume | Difficulty | Trend | Priority | Page Group | Source |
|---|---|---|---|---|---|---|---|
| [keyword] | [intent] | [vol] | [kd] | [trend] | [priority] | [group] | [source] |

## Keyword Gap Analysis
### Keywords competitors rank for that we are not targeting
| Keyword | Owned By | Volume | Difficulty | Opportunity |
|---|---|---|---|---|
| [keyword] | [competitor] | [vol] | [kd] | [opportunity note] |

### Summary
[Agent-written paragraph summarising gap findings and what they mean for the project]

## Keywords by Page Group
### Homepage
- [keyword] — vol: [x], kd: [x], intent: [intent]

### Product / Service Pages
- [keyword] — vol: [x], kd: [x], intent: [intent]

### Blog / Content
- [keyword] — vol: [x], kd: [x], intent: [intent]

## Notes
- [note 1]
- [note 2]
```
