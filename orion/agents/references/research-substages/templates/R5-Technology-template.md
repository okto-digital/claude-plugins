# R5-Technology — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "code": "R5",
  "slug": "Technology",
  "technology_performance": {
    "meta": {
      "date_run": "string",
      "wcag_level": "AA",
      "pages_per_site": "number"
    },
    "sites": [
      {
        "id": "string",
        "type": "client | competitor | reference",
        "domain": "string",
        "competitor_rank": "number | null",
        "pages_analysed": [
          {
            "url": "string",
            "page_type": "homepage | conversion | category | secondary",
            "lighthouse": {
              "performance": "number | null",
              "accessibility": "number | null",
              "best_practices": "number | null",
              "seo": "number | null"
            },
            "core_web_vitals": {
              "lcp": "string | null",
              "inp": "string | null",
              "cls": "string | null",
              "ttfb": "string | null"
            }
          }
        ],
        "tech_stack": {
          "cms": "string | null",
          "framework": "string | null",
          "hosting": "string | null",
          "cdn": "string | null",
          "ssl": "boolean | null",
          "analytics": [],
          "marketing_tools": [],
          "other": []
        },
        "wcag": {
          "score": "number | null",
          "level_met": "A | AA | AAA | none | null",
          "critical_violations": [],
          "notes": "string | null"
        },
        "gdpr": {
          "cookie_consent": "present | missing | partial | null",
          "consent_type": "opt-in | opt-out | none | null",
          "privacy_policy": "present | missing | null",
          "tracking_scripts": [],
          "notes": "string | null"
        },
        "notes": "string | null"
      }
    ],
    "gap_analysis": {
      "tech_stack_gaps": [],
      "performance_gaps": [],
      "accessibility_gaps": [],
      "gdpr_gaps": [],
      "opportunities": []
    },
    "notes": [
      "string"
    ]
  }
}
```

Write to `research/R5-Technology.json`.

---

## Markdown Template

Generate `research/R5-Technology.md` from the JSON:

```markdown
# Technology & Performance — [Client Name]

## Overview
[2-3 sentence narrative summarising the technical landscape —
how the client compares technically, most important gaps or opportunities]

## Site Analysis

### [Client Name] — [domain] *(Client)*

#### Pages Analysed
| Page | Type | Perf | Access. | Best Prac. | SEO | LCP | INP | CLS |
|---|---|---|---|---|---|---|---|---|
| [url] | homepage | [score] | [score] | [score] | [score] | [lcp] | [inp] | [cls] |

#### Tech Stack
- **CMS:** [cms] | **Framework:** [framework]
- **Hosting:** [hosting] | **CDN:** [cdn] | **SSL:** [ssl]
- **Analytics:** [analytics]
- **Marketing tools:** [marketing_tools]

#### WCAG Accessibility *(surface scan — AA level)*
- **Score:** [score] | **Level met:** [level_met]
- **Critical violations:** [critical_violations]

#### GDPR *(surface scan — not a legal assessment)*
- **Cookie consent:** [cookie_consent] ([consent_type])
- **Privacy policy:** [privacy_policy]
- **Tracking scripts detected:** [tracking_scripts]

---
*(repeat for each competitor and reference site)*

## Gap Analysis
### Technology Stack Gaps
- [gap 1]

### Performance Gaps
- [gap 1]

### Accessibility Gaps
- [gap 1]

### GDPR Gaps
- [gap 1]

### Opportunities
- [opportunity 1]

## Notes
- [note 1]
```
