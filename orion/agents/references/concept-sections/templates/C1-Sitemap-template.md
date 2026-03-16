# C1-Sitemap — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C1",
  "slug": "Sitemap",
  "sitemap": {
    "meta": {
      "total_pages": "number",
      "traffic_potential": {
        "conservative_monthly": "number",
        "realistic_monthly": "number",
        "optimistic_monthly": "number"
      }
    },
    "tree": [
      {
        "name": "string",
        "path": "string (URL path, e.g. /shop/caviar/beluga)",
        "type": "string (homepage | landing | product | category | utility | blog | etc.)",
        "priority": "must_have | should_have | nice_to_have",
        "persona": "string | null",
        "primary_keyword": "string | null",
        "secondary_keywords": [],
        "combined_volume": "number | null",
        "traffic_est": {
          "conservative": "number | null",
          "realistic": "number | null",
          "optimistic": "number | null"
        },
        "purpose": "string",
        "children": []
      }
    ]
  },
  "notes": ["string"]
}
```

Write to `concept/C1-Sitemap.json`.

## Markdown Template

Generate `concept/C1-Sitemap.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Sitemap

**Total traffic potential:** Conservative {conservative_monthly}/mo | Realistic {realistic_monthly}/mo | Optimistic {optimistic_monthly}/mo
**Total pages:** {total_pages}

- **{Page Name}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} ({combined_volume} vol) | Traffic: {c}/{r}/{o} mo
  - **{Child Page}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} ({combined_volume} vol) | Traffic: {c}/{r}/{o} mo
    - **{Grandchild}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} | Traffic: {c}/{r}/{o} mo

*Traffic: C = conservative / R = realistic / O = optimistic monthly organic visits*
*Estimates based on keyword volume and average organic CTR by position. Figures represent opportunity scale, not guaranteed outcomes.*

### Notes
- {note 1}
```
