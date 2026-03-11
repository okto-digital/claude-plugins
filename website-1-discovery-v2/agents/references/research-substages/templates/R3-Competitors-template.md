# R3-Competitors — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R3",
  "slug": "Competitors",
  "competitor_landscape": {
    "meta": {
      "total_competitors": "number",
      "sources": ["init_notes", "R1-SERP", "R2-Keywords"],
      "date_run": "string",
      "language_location_matrix": [
        {"language": "string", "location": "string", "search_engine": "string"}
      ]
    },
    "competitors": [
      {
        "rank": "number",
        "domain": "string",
        "name": "string | null",
        "site_type": "commercial",
        "keyword_appearances": "number",
        "markets": {
          "primary": "string | null",
          "other": [],
          "languages_detected": [],
          "serp_context": [
            {"language": "string", "location": "string", "appearances": "number"}
          ]
        },
        "profile": {
          "description": "string | null",
          "industry": "string | null",
          "founded": "string | null",
          "size": "string | null",
          "positioning": "string | null"
        },
        "website": {
          "url": "string",
          "structure": "string | null",
          "messaging": "string | null",
          "tone_of_voice": "string | null",
          "cta_patterns": "string | null",
          "content_presence": "string | null"
        },
        "social": {
          "platforms": [],
          "activity": "string | null"
        },
        "reputation": {
          "google_rating": "string | null",
          "review_count": "string | null",
          "notable_mentions": []
        },
        "strengths": [],
        "weaknesses": [],
        "notes": "string | null"
      }
    ],
    "gap_analysis": {
      "client_vs_competitors": "string",
      "market_gaps": [],
      "positioning_gaps": [],
      "opportunities": []
    },
    "notes": [
      "string"
    ]
  }
}
```

**Note on `rank`:** Rank 1 is the most frequently appearing commercial competitor across all language x location SERP matrices. Ranks 1–3 receive deeper analysis in substages R5-Technology, R6-Reputation and R9-Content. All locked competitors are included in R8-UX.

**Note on `positioning`:** A single agent-written sentence summarising the competitor's apparent value proposition. This is the most used field in Proposal generation.

Write to `research/R3-Competitors.json`.

---

## Markdown Template

Generate `research/R3-Competitors.md` from the JSON:

```markdown
# Competitor Landscape — [Client Name]

## Overview
[2-3 sentence narrative summarising the competitive landscape — how many strong
competitors exist, how mature the market looks, and the most important finding]

## Competitor Profiles

### [Rank]. [Competitor Name] — [domain]
**Positioning:** [positioning]
**Markets:** [primary] + [other] | **Languages:** [languages_detected]
**SERP Presence:** [serp_context summary]

| Dimension | Finding |
|---|---|
| Website structure | [structure] |
| Messaging | [messaging] |
| Tone of voice | [tone_of_voice] |
| CTAs | [cta_patterns] |
| Content | [content_presence] |
| Social activity | [activity] |
| Google rating | [google_rating] ([review_count] reviews) |

**Strengths:** [strengths]
**Weaknesses:** [weaknesses]

---

## Gap Analysis

### Client vs Competitor Set
[agent-written paragraph comparing client against competitors as a whole]

### Market Gaps
- [gap 1]

### Positioning Gaps
- [gap 1]

### Opportunities
- [opportunity 1]

## Notes
- [note 1]
```
