# Concept Section — Functional Requirements

**Code:** C2
**Slug:** Functional
**Output:** `concept/C2-Functional.json`, `concept/C2-Functional.md`
**Wave:** 1 (no upstream dependencies)

## Purpose

Define what the website needs to do. Every functional requirement is traceable to a gap analysis finding, client answer, competitor benchmark, or industry standard.

## Methodology

1. Read gap analysis domains related to functionality: forms, ecommerce, booking, analytics, security, accessibility, performance, user accounts.
2. Read competitor research (R3) for functionality gaps and industry baselines.
3. Read market research (R4) for industry-standard features and expectations.
4. Group requirements by functional area:
   - Core functionality (navigation, search, contact forms)
   - Ecommerce (if applicable — catalogue, cart, checkout, payment, integrations)
   - User accounts (if applicable — registration, login, B2B pricing, order history)
   - Booking and scheduling (if applicable)
   - Content management (blog, editorial, media)
   - Analytics and measurement (GA4, GTM, conversion tracking)
   - Integrations (CRM, ERP, accounting, email marketing)
   - GDPR and compliance (cookie consent, privacy controls)
   - Performance requirements (Core Web Vitals targets)
   - Accessibility requirements (WCAG AA compliance)
5. Tag each requirement with:
   - Priority: `must_have`, `should_have`, `nice_to_have`
   - Source: which finding or client answer drives this
   - Complexity: `simple`, `moderate`, `complex`
6. Skip functional areas that don't apply to this project (e.g., no ecommerce section for a portfolio site).

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
  "code": "C2",
  "slug": "Functional",
  "functional_requirements": [
    {
      "area": "string",
      "requirement": "string",
      "priority": "must_have | should_have | nice_to_have",
      "source": "string (e.g. 'G10-Forms: contact form checkpoint', 'R3-Competitors: competitor X has booking')",
      "complexity": "simple | moderate | complex"
    }
  ],
  "notes": ["string"]
}
```

Write to `concept/C2-Functional.json`.

---

## Markdown Template

Generate `concept/C2-Functional.md` from the JSON:

```markdown
## Functional Requirements

### Must Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Should Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Nice to Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Notes
- {note 1}
```
