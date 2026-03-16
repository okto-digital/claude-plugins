# C7-Project-Roadmap — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C7",
  "slug": "Project-Roadmap",
  "project_roadmap": {
    "launch_scope": {
      "must_have": ["string (MVP items — pages and features)"],
      "should_have": ["string (Phase 2 items)"],
      "out_of_scope": ["string (explicitly excluded)"]
    },
    "phases": [
      {
        "phase": "number",
        "name": "string",
        "deliverables": ["string"],
        "dependencies": ["string | null"],
        "rationale": "string"
      }
    ],
    "success_metrics": [
      {
        "timeframe": "string (launch | 3-month | 6-month | 12-month)",
        "kpis": [
          {
            "metric": "string",
            "target": "string",
            "source": "string (which C-section or G-file drives this)"
          }
        ]
      }
    ],
    "post_launch": {
      "content_governance": "string",
      "maintenance_schedule": "string",
      "growth_roadmap": "string"
    },
    "risks": [
      {
        "risk": "string",
        "impact": "high | medium | low",
        "mitigation": "string",
        "source": "string"
      }
    ]
  },
  "notes": ["string"]
}
```

Write to `concept/C7-Project-Roadmap.json`.

## Markdown Template

Generate `concept/C7-Project-Roadmap.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Project Roadmap

### Launch Scope (MVP)
**Must have:**
- {must_have item}

**Should have (Phase 2):**
- {should_have item}

**Out of scope:**
- {out_of_scope item}

### Phase Breakdown
{for each phase}
**Phase {phase}: {name}**
Deliverables: {deliverables}
Dependencies: {dependencies or "None"}
Rationale: {rationale}
{end for}

### Success Metrics
{for each timeframe}
**{timeframe}:**
| Metric | Target | Source |
|---|---|---|
| {metric} | {target} | {source} |
{end for}

### Post-Launch Plan
- **Content governance:** {content_governance}
- **Maintenance:** {maintenance_schedule}
- **Growth roadmap:** {growth_roadmap}

### Risks
| Risk | Impact | Mitigation | Source |
|---|---|---|---|
| {risk} | {impact} | {mitigation} | {source} |

### Notes
- {note 1}
```
