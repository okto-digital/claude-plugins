# R4-Market — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R4",
  "slug": "Market",
  "industry_market_context": {
    "meta": {
      "industry": "string",
      "date_run": "string",
      "sources": [
        {"url": "string", "title": "string", "type": "local | global", "relevance": "string"}
      ],
      "search_matrix": {
        "local": {"language": "string", "location": "string", "search_engine": "string"},
        "global": {"language": "en", "location": "global", "search_engine": "google.com"}
      }
    },
    "current_state": {
      "market_maturity": "established | growing | emerging",
      "market_dynamics": "string | null",
      "regulatory_considerations": [],
      "seasonal_patterns": "string | null"
    },
    "customer_behaviour": {
      "discovery_patterns": "string | null",
      "buying_journey": "string | null",
      "common_questions": [],
      "content_formats": [],
      "device_preferences": "string | null"
    },
    "website_expectations": {
      "standard_functionality": [],
      "trust_signals": [],
      "ia_patterns": "string | null",
      "conversion_patterns": "string | null"
    },
    "payment_patterns": {
      "local_methods": [],
      "emerging_behaviours": []
    },
    "trends": {
      "current": [],
      "innovations": [],
      "future": [],
      "local_vs_global_gap": "string | null"
    },
    "website_implications": [
      "string"
    ],
    "notes": [
      "string"
    ]
  }
}
```

**Note on `website_implications`:** Most important field for downstream phases. Agent-written statements connecting market findings to website decisions — e.g. "Mobile-first design is critical — 78% of searches in this category are on mobile in SK." Concept Creation reads this directly.

**Note on `local_vs_global_gap`:** What global markets are doing that the local market hasn't adopted yet. Consistent source of differentiation opportunities for the proposal.

Write to `research/R4-Market.json`.

---

## Markdown Template

Generate `research/R4-Market.md` from the JSON:

```markdown
# Industry & Market Context — [Client Name]

## Overview
[2-3 sentence narrative summarising the most important industry findings
and what they mean for the website project]

## Search Sources
| Source | Type | Relevance |
|---|---|---|
| [title] ([url]) | local / global | [relevance note] |

## Current Market State
- **Maturity:** [market_maturity]
- **Dynamics:** [market_dynamics]
- **Regulatory considerations:** [list]
- **Seasonal patterns:** [seasonal_patterns]

## Customer Behaviour
- **Discovery patterns:** [discovery_patterns]
- **Buying journey:** [buying_journey]
- **Common questions:** [list]
- **Preferred content formats:** [list]
- **Device preferences:** [device_preferences]

## Website Expectations
- **Standard functionality:** [list]
- **Trust signals:** [list]
- **IA patterns:** [ia_patterns]
- **Conversion patterns:** [conversion_patterns]

## Payment Patterns
- **Local methods:** [list]
- **Emerging behaviours:** [list]

## Trends
### Current
- [trend 1]

### Innovations
- [innovation 1]

### Future Direction
- [future trend 1]

### Local vs Global Gap
[local_vs_global_gap]

## Website Implications
- [implication 1]
- [implication 2]

## Notes
- [note 1]
```
