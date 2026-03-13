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
        "cluster": "string",
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
    "keyword_clusters": [
      {
        "cluster_name": "string",
        "primary_keyword": "string",
        "supporting_keywords": ["string"],
        "page_type": "homepage | service | portfolio | location | blog | landing | other",
        "total_volume": "number",
        "avg_difficulty": "number"
      }
    ],
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
# Keyword Opportunity — {Client Name}

## Overview
{2-3 sentence summary: total opportunity size, competitive difficulty level,
key gaps identified, top page groups by volume}

## Keyword Table
| Keyword | Intent | Volume | Difficulty | Trend | Priority | Cluster | Source |
|---|---|---|---|---|---|---|---|
| {keyword} | {intent} | {vol} | {kd} | {trend} | {priority} | {cluster} | {source} |

## Keyword Gap Analysis
### Keywords competitors rank for that we are not targeting
| Keyword | Owned By | Volume | Difficulty | Opportunity |
|---|---|---|---|---|
| {keyword} | {competitor} | {vol} | {kd} | {opportunity note} |

### Summary
{Agent-written paragraph summarising gap findings and what they mean for the project}

## Keyword Clusters
### {cluster_name} ({page_type})
**Primary:** {primary_keyword} (vol: {x}, kd: {x})
**Supporting:** {keyword 1}, {keyword 2}, ...
**Total volume:** {total_volume} | **Avg difficulty:** {avg_difficulty}

## Notes
- {note 1}
- {note 2}
```
