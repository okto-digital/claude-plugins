# R9-Content — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
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
      "voice_gaps": [],
      "content_structure_gaps": [],
      "missing_page_types": [],
      "opportunities": []
    },
    "page_structure_recommendation": {
      "primary_pages": [
        {
          "name": "string",
          "type": "string",
          "priority": "must_have | should_have | nice_to_have",
          "purpose": "string",
          "primary_persona": "string",
          "target_keywords": [],
          "suggested_sections": [],
          "seo_rationale": "string | null"
        }
      ],
      "supporting_pages": [
        {
          "name": "string",
          "type": "string",
          "priority": "must_have | should_have | nice_to_have",
          "purpose": "string",
          "primary_persona": "string",
          "target_keywords": [],
          "suggested_sections": [],
          "seo_rationale": "string | null"
        }
      ]
    },
    "notes": [
      "string"
    ]
  }
}
```

Write to `research/R9-Content.json`.

---

## Markdown Template

Generate `research/R9-Content.md` from the JSON:

```markdown
# Content Landscape & Strategy — [Client Name]

## Overview
[2-3 sentence narrative summarising the content landscape — communication style comparison,
key structural patterns, most important content opportunities]

## Brand Voice Analysis

### [Client Name] — [domain] *(Client)*
| Dimension | Finding |
|---|---|
| Tone | [tone] |
| Language complexity | [simple/moderate/complex] |
| Messaging pillars | [pillars] |
| Value proposition clarity | [clear/moderate/unclear] |
| Emotional vs rational | [balance] |
| CTA style | [style] |
| Localisation quality | [strong/moderate/weak] |
| Content length | [brief/moderate/comprehensive] |
| Storytelling vs features | [balance] |

---
*(repeat for each competitor and reference site)*

## Content Structure Analysis

### Homepage Structure Comparison
| Site | Sections | Depth |
|---|---|---|
| [domain] | [sections] | [depth] |

### Product / Service Page Structure
| Site | Sections | Depth |
|---|---|---|
| [domain] | [sections] | [depth] |

### Supporting Content Patterns
| Site | Blog | FAQ | Schema | Other |
|---|---|---|---|---|
| [domain] | [yes/no] | [yes/no] | [signals] | [other] |

## Gap Analysis
### Voice & Communication Gaps
- [gap 1]

### Content Structure Gaps
- [gap 1]

### Missing Page Types
- [gap 1]

### Opportunities
- [opportunity 1]

---

## Suggested Page Structure

### Primary Pages
- **[Page Name]** *(must have)*
  - Purpose: [purpose]
  - Persona: [persona]
  - Keywords: [keywords]
  - Sections: [section 1], [section 2], [section 3]
  - SEO rationale: [rationale]

### Supporting Pages
- **[Page Name]** *(should have)*
  - Purpose: [purpose]
  - Persona: [persona]
  - Keywords: [keywords]
  - Sections: [section 1], [section 2]
  - SEO rationale: [rationale]

## Notes
- [note 1]
```
