# R6-Reputation — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R6",
  "slug": "Reputation",
  "reputation_social": {
    "meta": {
      "date_run": "string",
      "social_limitation": "Analysis limited to publicly visible data. Audience demographics and ad spend require paid platform tools.",
      "max_posts_per_platform": 5,
      "review_samples_per_sentiment": 4
    },
    "sites": [
      {
        "id": "string",
        "type": "client | competitor | reference",
        "domain": "string",
        "competitor_rank": "number | null",
        "reviews": [
          {
            "platform": "string",
            "url": "string | null",
            "overall_rating": "number | null",
            "total_count": "number | null",
            "intensity": "active | moderate | sparse | null",
            "samples": {
              "positive": [
                {"text": "string", "rating": "number | null", "date": "string | null"}
              ],
              "medium": [
                {"text": "string", "rating": "number | null", "date": "string | null"}
              ],
              "negative": [
                {"text": "string", "rating": "number | null", "date": "string | null"}
              ]
            },
            "response_behaviour": {
              "responds": "boolean | null",
              "speed": "fast | moderate | slow | null",
              "tone": "string | null"
            }
          }
        ],
        "social": [
          {
            "platform": "string",
            "url": "string | null",
            "followers": "number | null",
            "verified": "boolean | null",
            "frequency": "active | moderate | dormant | null",
            "tone_of_voice": "string | null",
            "content_types": [],
            "posts_sampled": [
              {
                "type": "string",
                "topic": "string",
                "likes": "number | null",
                "comments": "number | null",
                "notes": "string | null"
              }
            ]
          }
        ],
        "website_trust_signals": {
          "case_studies": {
            "present": "boolean",
            "count": "number | null",
            "format": "string | null"
          },
          "testimonials": {
            "present": "boolean",
            "count": "number | null",
            "placement": "string | null",
            "format": "string | null"
          },
          "other_signals": []
        },
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

**Note on `gap_analysis`:** Each gap is a single concise line — what's missing + why it matters. Do not restate per-site findings. The detail lives in the `sites` array; the gap analysis synthesises across sites. Max 5 opportunities.

Write to `research/R6-Reputation.json`.

---

## Markdown Template

Generate `research/R6-Reputation.md` from the JSON:

```markdown
# Reputation & Social Proof — {Client Name}

## Overview
{2-3 sentence narrative summarising the trust landscape — how the client compares
to competitors on reputation and social, most important gaps or opportunities}

## Site Analysis

### {Client Name} — {domain} *(Client)*

#### Reviews
| Platform | Rating | Count | Intensity | Responds? |
|---|---|---|---|---|
| {platform} | {rating} | {count} | {intensity} | {yes/no} |

**Positive review samples:**
- "{review text}" — {rating} ({date})

**Medium review samples:**
- "{review text}" — {rating} ({date})

**Negative review samples:**
- "{review text}" — {rating} ({date})

#### Social Presence
| Platform | Followers | Verified | Frequency | Tone |
|---|---|---|---|---|
| {platform} | {count} | {yes/no} | {frequency} | {tone} |

**Sampled posts:**
- {type} — {topic} | {likes} likes, {comments} comments

#### Website Trust Signals
- **Case studies:** {present/absent} — {count}, {format}
- **Testimonials:** {present/absent} — {count}, {placement}, {format}
- **Other signals:** {other_signals}

---
*(repeat for each competitor and reference site)*

## Gap Analysis

### Gaps
- {gap — what's weak + why it matters}

### Opportunities
- {opportunity — what to do + expected impact}

## Notes
- {note 1}
```
