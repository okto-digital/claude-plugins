# C4-Content-Strategy — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C4",
  "slug": "Content-Strategy",
  "content_strategy": {
    "tone_of_voice": "string",
    "tone_examples": ["string"],
    "messaging_pillars": [
      {
        "pillar": "string",
        "description": "string",
        "persona": "string"
      }
    ],
    "value_proposition": "string",
    "seo_content_plan": {
      "primary_pages": [
        {
          "page": "string (matches sitemap page name)",
          "keyword_target": "string",
          "content_notes": "string"
        }
      ],
      "supporting_pages": [
        {
          "page": "string",
          "keyword_target": "string",
          "seo_rationale": "string"
        }
      ],
      "blog_clusters": [
        {
          "cluster": "string",
          "topics": ["string"],
          "keyword_targets": ["string"]
        }
      ]
    },
    "localisation_notes": "string | null"
  },
  "notes": ["string"]
}
```

Write to `concept/C4-Content-Strategy.json`.

## Markdown Template

Generate `concept/C4-Content-Strategy.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Content Strategy

### Tone of Voice
{tone_of_voice}

**Examples:**
- "{example 1}"
- "{example 2}"

### Messaging Pillars
| Pillar | Description | Persona |
|---|---|---|
| {pillar} | {description} | {persona} |

### Value Proposition
> {value_proposition}

### SEO Content Plan

#### Primary Pages
| Page | Keyword Target | Content Notes |
|---|---|---|
| {page} | {keyword_target} | {content_notes} |

#### Supporting SEO Pages
| Page | Keyword Target | SEO Rationale |
|---|---|---|
| {page} | {keyword_target} | {seo_rationale} |

#### Blog Clusters
- **{cluster}** — {keyword_targets}
  - {topic 1}
  - {topic 2}

### Localisation
{localisation_notes or "N/A — single language project"}

### Notes
- {note 1}
```
