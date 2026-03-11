# R7-Audience — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R7",
  "slug": "Audience",
  "audience_personas": {
    "meta": {
      "total_segments": "number",
      "total_personas": "number",
      "primary_persona": "string",
      "date_run": "string"
    },
    "segments": [
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "importance": "primary | secondary | tertiary",
        "identified_from": []
      }
    ],
    "personas": [
      {
        "id": "string",
        "segment_id": "string",
        "is_primary": "boolean",
        "name": "string",
        "demographics": {
          "age": "string",
          "location": "string",
          "occupation": "string",
          "income_level": "string | null",
          "lifestyle": "string | null"
        },
        "psychographics": {
          "personality_type": "string | null",
          "values": [],
          "lifestyle_preferences": [],
          "emotional_triggers": [],
          "buying_behaviour": "string | null",
          "brand_perception": "string | null"
        },
        "buying_motivation": {
          "problem_solving": "string | null",
          "emotional_drivers": [],
          "objections": [],
          "decision_process": "string | null",
          "trusted_influences": []
        },
        "digital_behaviour": {
          "search_channels": [],
          "preferred_content": [],
          "device_preference": "mobile | desktop | mixed",
          "active_hours": "string | null"
        },
        "trust_threshold": "high | medium | low",
        "benchmarks": {
          "conversion_rate_est": "string | null",
          "acquisition_channel": "string | null",
          "retention_likelihood": "string | null"
        },
        "keyword_mapping": {
          "awareness": [],
          "consideration": [],
          "decision": []
        },
        "messaging": [
          "string"
        ],
        "psychographics_table": [
          {
            "factor": "string",
            "source": "string",
            "findings": "string",
            "patterns": "string",
            "implications": "string"
          }
        ],
        "journey_map": [
          {
            "stage": "awareness | consideration | decision | retention | advocacy",
            "mindset": "string",
            "where_they_go": [],
            "pain_points": [],
            "content_needed": [],
            "website_implication": "string"
          }
        ]
      }
    ],
    "notes": [
      "string"
    ]
  }
}
```

Write to `research/R7-Audience.json`.

---

## Markdown Template

Generate `research/R7-Audience.md` from the JSON:

```markdown
# Audience & Personas — [Client Name]

## Overview
[2-3 sentence narrative summarising who the audiences are, which persona is primary,
and the most important insight about how they make decisions]

## Audience Segments
| Segment | Description | Importance | Identified From |
|---|---|---|---|
| [name] | [description] | primary/secondary | [sources] |

---

## Persona: [Name] — [Segment]
*Primary design target* (if applicable)

### Demographics
- **Age:** [age] | **Location:** [location]
- **Occupation:** [occupation] | **Income:** [income_level]
- **Lifestyle:** [lifestyle]

### Psychographics
- **Personality:** [personality_type]
- **Values:** [values]
- **Emotional triggers:** [emotional_triggers]
- **Buying behaviour:** [buying_behaviour]

### Buying Motivation
- **Problem solving:** [problem_solving]
- **Objections:** [objections]
- **Decision process:** [decision_process]
- **Trusted influences:** [trusted_influences]

### Digital Behaviour
- **Search channels:** [search_channels]
- **Preferred content:** [preferred_content]
- **Device:** [device_preference]
- **Trust threshold:** [trust_threshold]

### Benchmarks
- **Est. conversion rate:** [conversion_rate_est]
- **Best acquisition channel:** [acquisition_channel]

### Keyword Mapping
| Funnel Stage | Keywords |
|---|---|
| Awareness | [keywords] |
| Consideration | [keywords] |
| Decision | [keywords] |

### Psychographics & Buying Motivation Table
| Factor | Source | Findings | Patterns | Implications |
|---|---|---|---|---|
| [factor] | [source] | [findings] | [patterns] | [implications] |

### Messaging
- "[message 1]"
- "[message 2]"

### User Journey Map
| Stage | Mindset | Where They Go | Pain Points | Content Needed | Website Implication |
|---|---|---|---|---|---|
| Awareness | [mindset] | [channels] | [pain points] | [content] | [implication] |
| Consideration | ... | ... | ... | ... | ... |
| Decision | ... | ... | ... | ... | ... |
| Retention | ... | ... | ... | ... | ... |
| Advocacy | ... | ... | ... | ... | ... |

---

## Notes
- [note 1]
```
