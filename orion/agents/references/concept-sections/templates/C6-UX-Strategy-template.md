# C6-UX-Strategy — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "C6",
  "slug": "UX-Strategy",
  "ux_strategy": {
    "navigation": {
      "primary": "string",
      "mobile": "string",
      "secondary": "string"
    },
    "conversion_funnels": [
      {
        "name": "string",
        "persona": "string",
        "path": "string (entry -> step -> ... -> target action)",
        "rationale": "string"
      }
    ],
    "cta_strategy": [
      {
        "page_type": "string",
        "primary_cta": "string",
        "secondary_cta": "string | null",
        "placement_rationale": "string"
      }
    ],
    "trust_elements": [
      {
        "element": "string",
        "placement": "string",
        "rationale": "string"
      }
    ],
    "mobile_strategy": {
      "approach": "string (mobile-first | responsive)",
      "rationale": "string",
      "content_priority": ["string"],
      "interaction_notes": "string"
    },
    "user_flows": [
      {
        "name": "string",
        "persona": "string",
        "goal": "string",
        "steps": ["string (page: action)"],
        "desired_outcome": "string"
      }
    ]
  },
  "notes": ["string"]
}
```

Write to `concept/C6-UX-Strategy.json`.

## Markdown Template

Generate `concept/C6-UX-Strategy.md` from the JSON:

```markdown
## UX Strategy

### Navigation Model
- **Primary:** {primary}
- **Mobile:** {mobile}
- **Secondary:** {secondary}

### Conversion Funnels
{for each funnel}
**{name}** (Persona: {persona})
Path: {path}
Rationale: {rationale}
{end for}

### CTA Strategy
| Page Type | Primary CTA | Secondary CTA | Rationale |
|---|---|---|---|
| {page_type} | {primary_cta} | {secondary_cta} | {placement_rationale} |

### Trust Elements
| Element | Placement | Rationale |
|---|---|---|
| {element} | {placement} | {rationale} |

### Mobile Strategy
**Approach:** {approach} -- {rationale}
**Content priority (mobile):** {content_priority}
**Interaction notes:** {interaction_notes}

### Key User Flows
{for each flow}
**{name}** (Persona: {persona})
Goal: {goal}
Steps: {steps joined by " -> "}
Outcome: {desired_outcome}
{end for}

### Notes
- {note 1}
```
