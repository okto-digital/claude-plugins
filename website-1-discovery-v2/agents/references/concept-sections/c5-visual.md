# Concept Section — Visual Direction

**Code:** C5
**Slug:** Visual
**Output:** `concept/C5-Visual.json`, `concept/C5-Visual.md`
**Wave:** 1 (no upstream dependencies)

## Purpose

Define the visual direction for the website — not a design brief, but a direction document. Grounded in UX/UI research, persona expectations, and brand positioning from gap analysis. Gives the designer a clear starting point with evidence-based rationale.

## Methodology

1. Read UX/UI research (R8) for competitor visual patterns, colour schemes, typography, layout density, and persona alignment notes.
2. Read audience research (R7) for persona expectations, trust thresholds, and device preferences.
3. Read reputation research (R6) for brand and social signals.
4. Read gap analysis domains related to design: design-and-brand.
5. Produce direction (not specifications) for each dimension:
   - **Positioning and mood** — how the brand should feel visually (premium, technical, warm, bold, minimal, etc.), grounded in persona expectations and market positioning
   - **Colour direction** — mood and reference points, not exact palette. Reference competitor analysis from R8
   - **Typography direction** — style and feel (modern vs traditional, technical vs humanist), not specific fonts
   - **Imagery direction** — style (original vs stock), quality level, subject matter, mood. Reference persona expectations
   - **Layout and density** — spacious vs dense, based on persona trust threshold and industry patterns
   - **Recognisability** — what specific visual choices would make this brand distinctly identifiable, grounded in competitor differentiation gaps
   - **Reference examples** — specific pages or sites from research that demonstrate the recommended direction, with what to take from each

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
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

---

## Markdown Template

Generate `concept/C5-Visual.md` from the JSON:

```markdown
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
