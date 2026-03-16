# C5-Visual — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C5",
  "slug": "Visual",
  "visual_direction": {
    "positioning_mood": "string",
    "colour_direction": "string",
    "typography_direction": "string",
    "imagery_direction": "string",
    "layout_direction": "string",
    "recognisability": "string",
    "references": [
      {
        "url": "string",
        "what_to_take": "string"
      }
    ]
  },
  "notes": ["string"]
}
```

Write to `concept/C5-Visual.json`.

## Markdown Template

Generate `concept/C5-Visual.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Visual Direction

- **Positioning & mood:** {positioning_mood}
- **Colour direction:** {colour_direction}
- **Typography direction:** {typography_direction}
- **Imagery direction:** {imagery_direction}
- **Layout direction:** {layout_direction}
- **Recognisability:** {recognisability}

### Reference Examples
| URL | What to take from it |
|---|---|
| {url} | {what_to_take} |

### Notes
- {note 1}
```
