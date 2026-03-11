# Client Intelligence — Templates

## JSON Schema

All blocks are always present regardless of `build_type`. Fields with no available data are `null`.

```json
{
  "client_intelligence": {
    "meta": {
      "build_type": "new | redesign",
      "presence_status": "none | partial | full",
      "business_entity": "string | null"
    },
    "profile": {
      "description": "string | null",
      "industry": "string | null",
      "founded": "string | null",
      "size": "string | null",
      "team": "string | null",
      "markets": []
    },
    "website": {
      "url": "string | null",
      "structure": "string | null",
      "messaging": "string | null",
      "tone_of_voice": "string | null",
      "cta_patterns": "string | null",
      "content_presence": "string | null"
    },
    "social": {
      "platforms": [],
      "activity": "string | null",
      "engagement": "string | null",
      "top_content": "string | null"
    },
    "reputation": {
      "google_rating": "string | null",
      "review_platforms": [],
      "press_coverage": [],
      "awards_certifications": []
    },
    "financials": {
      "source": "string | null",
      "status": "string | null",
      "notes": "string | null"
    },
    "registry": {
      "registered_name": "string | null",
      "legal_form": "string | null",
      "registration_date": "string | null",
      "address": "string | null",
      "owners": []
    },
    "notes": [
      "string",
      "string"
    ]
  }
}
```

### presence_status values

- `none` — No external data available (typical for new builds). Almost all fields are `null`.
- `partial` — Some discovery was possible but significant gaps remain.
- `full` — Comprehensive data gathered across web, social, reputation, and registry.

Downstream agents use this to calibrate data confidence.

---

## Markdown Template

Generate `D2-Client-Intelligence.md` from the JSON. The Overview is a narrative paragraph, not field values. Sections with all-null fields get a one-line note instead of listing nulls.

```markdown
# Client Intelligence — [client name]

## Overview
[2-3 sentence narrative paragraph describing who the client is,
what they do, and their current market position or situation]

## Profile
- **Industry:** [industry]
- **Founded:** [founded]
- **Size:** [size]
- **Markets:** [markets]
- **Business entity:** [business_entity]

## Web Presence
- **URL:** [url]
- **Structure:** [structure]
- **Messaging:** [messaging]
- **Tone of voice:** [tone_of_voice]
- **CTAs:** [cta_patterns]
- **Content:** [content_presence]

## Social Presence
- **Active platforms:** [platforms]
- **Activity:** [activity]
- **Engagement:** [engagement]

## Reputation
- **Google rating:** [google_rating]
- **Review platforms:** [review_platforms]
- **Press coverage:** [press_coverage]
- **Awards/certifications:** [awards_certifications]

## Financials
- **Source:** [source]
- **Status:** [status]
- **Notes:** [financials.notes]

## Registry
- **Registered name:** [registered_name]
- **Legal form:** [legal_form]
- **Registration date:** [registration_date]
- **Address:** [address]
- **Owners:** [owners]

## Key Findings
[Flags, concerns, or important observations that should influence project direction]

## Notes
- [note 1]
- [note 2]
```

### Null-section handling

When all fields in a section are `null`, replace the field list with a single line:

- Web Presence → "No web presence data — new build."
- Social Presence → "No social media data available."
- Reputation → "No reputation data available."
- Financials → "No financial data available."
- Registry → "No business registry data available."
