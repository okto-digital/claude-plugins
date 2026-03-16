# C3-Technical-Architecture — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C3",
  "slug": "Technical-Architecture",
  "tech_stack": [
    {
      "category": "string",
      "recommendation": "string",
      "rationale": "string",
      "alternatives": ["string"],
      "complexity": "simple | moderate | complex"
    }
  ],
  "notes": ["string"]
}
```

Write to `concept/C3-Technical-Architecture.json`.

## Markdown Template

Generate `concept/C3-Technical-Architecture.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Technical Architecture

| Category | Recommendation | Rationale | Alternatives | Complexity |
|---|---|---|---|---|
| {category} | {recommendation} | {rationale} | {alternatives} | {complexity} |

### Notes
- {note 1}
```
