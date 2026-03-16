# R3-Competitors — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — 10-20 telegraphic findings that would change what we propose, how we price it, or what we ask the client"],
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
      "gaps": [],
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

**Note on `gap_analysis`:** One line per item. `gaps` covers client-vs-competitor differences, market gaps, and positioning gaps together — no separate subsections. `opportunities` = concrete actions + expected impact. Do not restate per-competitor findings.

Write to `research/R3-Competitors.json`.

---

## Markdown Template

Generate `research/R3-Competitors.md` from the JSON:

```markdown
# Competitor Landscape — {Client Name}

## TLDR

{bulleted list from tldr array — one line per finding, telegraphic}

---

## Overview
{2-3 sentence narrative summarising the competitive landscape — how many strong
competitors exist, how mature the market looks, and the most important finding}

## Competitor Profiles

### {Rank}. {Competitor Name} — {domain}
**Positioning:** {positioning}
**Markets:** {primary} + {other} | **Languages:** {languages_detected}
**SERP Presence:** {serp_context summary}

| Dimension | Finding |
|---|---|
| Website structure | {structure} |
| Messaging | {messaging} |
| Tone of voice | {tone_of_voice} |
| CTAs | {cta_patterns} |
| Content | {content_presence} |
| Social activity | {activity} |
| Google rating | {google_rating} ({review_count} reviews) |

**Strengths:** {strengths}
**Weaknesses:** {weaknesses}

---

## Gap Analysis

### Gaps
- {gap — what's weak + why it matters}

### Opportunities
- {opportunity — what to do + expected impact}

## Notes
- {note 1}
```
