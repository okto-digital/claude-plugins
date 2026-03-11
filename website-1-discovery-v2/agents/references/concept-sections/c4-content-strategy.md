# Concept Section — Content Strategy

**Code:** C4
**Slug:** Content-Strategy
**Output:** `concept/C4-Content-Strategy.json`, `concept/C4-Content-Strategy.md`
**Wave:** 2 (depends on C1-Sitemap)

## Purpose

Define how the website communicates — tone of voice, messaging, SEO content plan, and launch priorities. Built on the sitemap (which pages exist) and grounded in audience, keyword, and content research.

## Upstream Dependency

**Reads C1-Sitemap output** to know which pages exist and their keyword mappings. The content strategy must align with the sitemap structure — every primary page needs content direction, and the SEO content plan references sitemap pages by name.

## Methodology

1. Read C1-Sitemap output for the page structure and keyword assignments.
2. Read content research (R9) for brand voice findings and content structure patterns.
3. Read keyword research (R2) for keyword clusters and search intent.
4. Read audience research (R7) for persona preferences and journey stages.
5. Read reputation research (R6) for social tone and communication style signals.
6. Read gap analysis domains related to content: content-strategy, blog, multilingual.
7. Produce:
   - **Tone of voice** — how the site should communicate, with concrete examples (phrases, not just adjectives)
   - **Messaging pillars** — 3–5 core themes mapped to personas
   - **Value proposition** — primary statement for the homepage
   - **SEO content plan:**
     - Primary pages with keyword targets and content notes (reference sitemap pages)
     - Supporting SEO pages with keyword targets and rationale
     - Blog topic clusters with keyword targets
   - **Launch vs post-launch** — what content must be ready at launch vs phased later
   - **Localisation notes** — language and cultural adaptation if secondary languages are active (from D1-Init.json language config)

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
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
    "launch_vs_postlaunch": {
      "launch": ["string"],
      "post_launch": ["string"]
    },
    "localisation_notes": "string | null"
  },
  "notes": ["string"]
}
```

Write to `concept/C4-Content-Strategy.json`.

---

## Markdown Template

Generate `concept/C4-Content-Strategy.md` from the JSON:

```markdown
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

### Launch vs Post-Launch
**At launch:** {launch priorities}
**Post-launch:** {post-launch plan}

### Localisation
{localisation_notes or "N/A — single language project"}

### Notes
- {note 1}
```
