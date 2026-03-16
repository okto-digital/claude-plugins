# R9-Content — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — 10-20 telegraphic findings that would change what we propose, how we price it, or what we ask the client"],
  "code": "R9",
  "slug": "Content",
  "content_landscape": {
    "meta": {
      "date_run": "string"
    },
    "sites": [
      {
        "id": "string",
        "type": "client | competitor | reference",
        "domain": "string",
        "competitor_rank": "number | null",
        "brand_voice": {
          "tone": "string | null",
          "language_complexity": "simple | moderate | complex | null",
          "messaging_pillars": [],
          "value_proposition_clarity": "clear | moderate | unclear | null",
          "emotional_vs_rational": "emotional | balanced | rational | null",
          "cta_style": "string | null",
          "localisation_quality": "strong | moderate | weak | null",
          "person_voice": "first | second | third | mixed | null",
          "headline_pattern": "string | null",
          "content_length": "brief | moderate | comprehensive | null",
          "storytelling_vs_features": "storytelling | balanced | features | null"
        },
        "content_structure": {
          "homepage": {
            "sections": [],
            "depth": "string | null"
          },
          "product_service_pages": {
            "sections": [],
            "depth": "string | null"
          },
          "supporting_pages": [],
          "blog_present": "boolean | null",
          "faq_present": "boolean | null",
          "schema_signals": []
        },
        "notes": "string | null"
      }
    ],
    "gap_analysis": {
      "gaps": [],
      "opportunities": []
    }
  }
}
```

**Note on `gap_analysis`:** One line per item. `gaps` covers voice, content structure, and missing page types together — no separate subsections. `opportunities` = what to do + expected impact. Do not restate per-site findings.

Write to `research/R9-Content.json`.

---

## Markdown Template

Generate `research/R9-Content.md` from the JSON:

```markdown
# Content Landscape & Strategy — {Client Name}

## TLDR

{bulleted list from tldr array — one line per finding, telegraphic}

---

## Overview
{2-3 sentence narrative summarising the content landscape — communication style comparison,
key structural patterns, most important content opportunities}

## Brand Voice Analysis

### {Client Name} — {domain} *(Client)*
| Dimension | Finding |
|---|---|
| Tone | {tone} |
| Language complexity | {simple/moderate/complex} |
| Messaging pillars | {pillars} |
| Value proposition clarity | {clear/moderate/unclear} |
| Emotional vs rational | {balance} |
| CTA style | {style} |
| Localisation quality | {strong/moderate/weak} |
| Content length | {brief/moderate/comprehensive} |
| Storytelling vs features | {balance} |

---
*(repeat for each competitor and reference site)*

## Content Structure Analysis

### Homepage Structure Comparison
| Site | Sections | Depth |
|---|---|---|
| {domain} | {sections} | {depth} |

### Product / Service Page Structure
| Site | Sections | Depth |
|---|---|---|
| {domain} | {sections} | {depth} |

### Supporting Content Patterns
| Site | Blog | FAQ | Schema | Other |
|---|---|---|---|---|
| {domain} | {yes/no} | {yes/no} | {signals} | {other} |

## Gap Analysis

### Gaps
- {gap — what's weak + why it matters}

### Opportunities
- {opportunity — what to do + expected impact}
```
