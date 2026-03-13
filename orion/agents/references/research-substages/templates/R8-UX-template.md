# R8-UX — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R8",
  "slug": "UX",
  "ux_ui_patterns": {
    "meta": {
      "date_run": "string",
      "primary_persona_device": "string",
      "heuristics_framework": "Nielsen 10 Usability Heuristics"
    },
    "sites": [
      {
        "id": "string",
        "type": "client | competitor | reference",
        "domain": "string",
        "competitor_rank": "number | null",
        "ux": {
          "navigation": {
            "type": "string | null",
            "structure": "string | null",
            "search_present": "boolean | null",
            "notes": "string | null"
          },
          "information_architecture": {
            "above_fold": "string | null",
            "clicks_to_conversion": "number | null",
            "hierarchy_depth": "string | null",
            "notes": "string | null"
          },
          "conversion_patterns": {
            "cta_placement": "string | null",
            "cta_language": "string | null",
            "form_complexity": "simple | moderate | complex | null",
            "friction_points": [],
            "notes": "string | null"
          },
          "mobile_ux": {
            "navigation_type": "string | null",
            "thumb_zone_optimised": "boolean | null",
            "content_prioritisation": "string | null",
            "notes": "string | null"
          },
          "heuristics_violations": [],
          "accessibility_ux": {
            "font_readability": "good | moderate | poor | null",
            "focus_states": "present | absent | partial | null",
            "notes": "string | null"
          }
        },
        "ui": {
          "colours": {
            "primary": [],
            "secondary": [],
            "accent": [],
            "mood": "string | null"
          },
          "typography": {
            "heading_font": "string | null",
            "body_font": "string | null",
            "weight_patterns": "string | null",
            "mood": "string | null"
          },
          "imagery": {
            "type": "stock | original | mixed | null",
            "quality": "high | medium | low | null",
            "mood": "string | null",
            "relevance": "string | null"
          },
          "layout": {
            "density": "dense | balanced | spacious | null",
            "grid_consistency": "consistent | inconsistent | null",
            "whitespace": "generous | moderate | compressed | null"
          },
          "iconography": {
            "style": "string | null",
            "illustration_present": "boolean | null",
            "consistency": "consistent | inconsistent | null"
          },
          "animation": {
            "hover_states": "present | absent | null",
            "scroll_animations": "present | absent | null",
            "quality_signal": "high | medium | low | null"
          },
          "brand_consistency": "consistent | partial | inconsistent | null",
          "notes": "string | null"
        }
      }
    ],
    "gap_analysis": {
      "ux_gaps": [],
      "ui_gaps": [],
      "visual_opportunities": [],
      "ux_opportunities": [],
      "persona_alignment_notes": []
    },
    "notes": [
      "string"
    ]
  }
}
```

**Note on `persona_alignment_notes`:** Agent-written observations connecting UX/UI findings directly to persona expectations from R7-Audience. For example: "Primary persona is mobile-dominant but no competitor has optimised mobile navigation — significant UX opportunity."

Write to `research/R8-UX.json`.

---

## Markdown Template

Generate `research/R8-UX.md` from the JSON:

```markdown
# UX/UI Patterns & Benchmarks — [Client Name]

## Overview
[2-3 sentence narrative summarising the UX/UI landscape — dominant patterns,
where the client stands, key opportunities]

## Site Analysis

### [Client Name] — [domain] *(Client)*

#### Behavioural UX
| Dimension | Finding |
|---|---|
| Navigation type | [type] |
| Clicks to conversion | [number] |
| CTA placement & language | [notes] |
| Form complexity | [simple/moderate/complex] |
| Mobile UX | [notes] |
| Friction points | [points] |
| Heuristics violations | [violations] |
| Accessibility UX | [notes] |

#### Visual UI
| Dimension | Finding |
|---|---|
| Primary colours | [hex values + mood] |
| Typography | [heading font] / [body font] — [mood] |
| Imagery | [type] — [quality] — [mood] |
| Layout density | [dense/balanced/spacious] |
| Whitespace | [generous/moderate/compressed] |
| Iconography | [style] — [consistency] |
| Animation | [quality signal] |
| Brand consistency | [consistent/partial/inconsistent] |

---
*(repeat for each competitor and reference site)*

## Gap Analysis
### UX Gaps
- [gap 1]

### UI / Visual Gaps
- [gap 1]

### Visual Opportunities
- [opportunity 1]

### UX Opportunities
- [opportunity 1]

### Persona Alignment Notes
- [note connecting UX/UI finding to persona expectation]

## Notes
- [note 1]
```
