# C8-SEO-Strategy — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C8",
  "slug": "SEO-Strategy",
  "seo_strategy": {
    "c1_reference": "string",
    "link_acquisition": {
      "approach": "string",
      "priority_targets": ["string"],
      "domain_types": ["string"],
      "rationale": "string"
    },
    "local_seo": "string | null (GMB, citations, NAP, local content — or null if no physical location)",
    "international_seo": "string | null (hreflang, market adaptation, URL structure — or null if single language)",
    "search_features": [
      {
        "page_type": "string",
        "target_features": ["string"],
        "structured_data": "string",
        "rationale": "string"
      }
    ],
    "monitoring": {
      "rank_tracking_scope": "string",
      "traffic_targets": [
        {
          "timeframe": "string",
          "target": "string"
        }
      ],
      "reporting_cadence": "string",
      "tools": ["string"]
    }
  },
  "notes": ["string"]
}
```

Write to `concept/C8-SEO-Strategy.json`.

## Markdown Template

Generate `concept/C8-SEO-Strategy.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## SEO Strategy

*On-page keyword targeting is defined in C1-Sitemap. SEO-specific monitoring below; project-level KPIs are in C7.*

### Link Acquisition
**Approach:** {approach}
**Priority targets:** {priority_targets}
**Domain types:** {domain_types}
**Rationale:** {rationale}

### Local SEO
{local_seo or "N/A — no physical location."}

### International SEO
{international_seo or "N/A — single language project."}

### Search Feature Optimization
| Page Type | Target Features | Structured Data | Rationale |
|---|---|---|---|
| {page_type} | {target_features} | {structured_data} | {rationale} |

### SEO Monitoring & KPIs
**Rank tracking:** {rank_tracking_scope}
**Reporting:** {reporting_cadence}
**Tools:** {tools}

| Timeframe | Traffic Target |
|---|---|
| {timeframe} | {target} |

### Notes
- {note 1}
```
