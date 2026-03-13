# Concept Section — Tech Stack Recommendation

**Code:** C3
**Slug:** Tech-Stack
**Output:** `concept/C3-Tech-Stack.json`, `concept/C3-Tech-Stack.md`
**Wave:** 2 (depends on C2-Functional)

## Purpose

Recommend the technology stack based on functional requirements and technical research. Every choice has a rationale tied to project needs, not generic preference.

## Upstream Dependency

**Reads C2-Functional output** to understand what the tech stack must support. Functional requirements determine platform choice — not the other way around.

## Methodology

1. Read C2-Functional output to get the full requirements list.
2. Read technology research (R5) for current tech landscape, performance benchmarks, and WCAG/GDPR context.
3. Read gap analysis domains related to technology: technical-platform, security, performance.
4. For each technology category, recommend a solution:
   - **CMS or framework** — based on content management needs, client capability, industry standards
   - **Hosting approach** — managed, cloud, headless
   - **Key integrations** — payment, booking, CRM, ERP, analytics, email marketing
   - **Performance strategy** — CDN, caching, image optimisation
   - **GDPR compliance approach** — cookie consent platform, data handling
   - **SEO technical foundation** — schema markup, sitemap, robots, canonical strategy
5. Each recommendation includes:
   - Suggested solution
   - Rationale — why this fits the project (tied to functional requirements and research)
   - Alternatives considered
   - Complexity signal
6. Skip categories that don't apply (e.g., no payment gateway for an informational site).

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
  "code": "C3",
  "slug": "Tech-Stack",
  "tech_stack": [
    {
      "category": "string",
      "recommendation": "string",
      "rationale": "string",
      "alternatives": ["string"],
      "complexity": "simple | moderate | complex"
    }
  ],
  "notes": ["string"]
}
```

Write to `concept/C3-Tech-Stack.json`.

---

## Markdown Template

Generate `concept/C3-Tech-Stack.md` from the JSON:

```markdown
## Tech Stack Recommendation

| Category | Recommendation | Rationale | Alternatives | Complexity |
|---|---|---|---|---|
| {category} | {recommendation} | {rationale} | {alternatives} | {complexity} |

### Notes
- {note 1}
```
