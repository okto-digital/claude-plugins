# Concept Section — Sitemap

**Code:** C1
**Slug:** Sitemap
**Output:** `concept/C1-Sitemap.json`, `concept/C1-Sitemap.md`
**Wave:** 1 (no upstream dependencies)

## Purpose

Build the full site structure as a nested page tree. Each page is mapped to a persona, keywords, and traffic estimates. The sitemap is the structural backbone of the concept — it defines what pages exist and why.

## Methodology

1. Read the page structure recommendation from content research (R9) as the starting skeleton.
2. Cross-reference with keyword research (R2) to ensure every high-value keyword cluster has a landing page.
3. Check gap analysis domains related to site structure, SEO, and project scope for resolved requirements that imply pages (e.g., "client needs booking page" from gap analysis).
4. For each page, assign:
   - Primary persona (from audience research)
   - Primary keyword + secondary keywords (from keyword research)
   - Combined search volume (sum of all mapped keywords)
   - Traffic estimates at three CTR scenarios:
     - **Conservative** — position 6–10 CTR (~4%), realistic for new/early-stage sites
     - **Realistic** — position 3–5 CTR (~8%), achievable within 6–12 months
     - **Optimistic** — position 1–2 CTR (~20%), peak performance potential
   - Priority: `must_have`, `should_have`, `nice_to_have`
5. Nest pages into a URL hierarchy (parent-child structure reflecting URL paths).
6. Sum traffic across all pages for total site traffic potential.
7. Include utility pages (privacy policy, cookie policy, 404, sitemap) as `must_have` without traffic estimates.

**Traffic note:** Estimates are based on keyword volume data and average organic CTR by position. Actual traffic depends on ranking, content quality, competition, and many other factors. Present as opportunity scale, not guaranteed outcomes.

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
  "code": "C1",
  "slug": "Sitemap",
  "sitemap": {
    "meta": {
      "total_pages": "number",
      "traffic_potential": {
        "conservative_monthly": "number",
        "realistic_monthly": "number",
        "optimistic_monthly": "number"
      }
    },
    "tree": [
      {
        "name": "string",
        "path": "string (URL path, e.g. /shop/caviar/beluga)",
        "type": "string (homepage | landing | product | category | utility | blog | etc.)",
        "priority": "must_have | should_have | nice_to_have",
        "persona": "string | null",
        "primary_keyword": "string | null",
        "secondary_keywords": [],
        "combined_volume": "number | null",
        "traffic_est": {
          "conservative": "number | null",
          "realistic": "number | null",
          "optimistic": "number | null"
        },
        "purpose": "string",
        "children": []
      }
    ]
  },
  "notes": ["string"]
}
```

Write to `concept/C1-Sitemap.json`.

---

## Markdown Template

Generate `concept/C1-Sitemap.md` from the JSON:

```markdown
## Sitemap

**Total traffic potential:** Conservative {conservative_monthly}/mo | Realistic {realistic_monthly}/mo | Optimistic {optimistic_monthly}/mo
**Total pages:** {total_pages}

- **{Page Name}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} ({combined_volume} vol) | Traffic: {c}/{r}/{o} mo
  - **{Child Page}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} ({combined_volume} vol) | Traffic: {c}/{r}/{o} mo
    - **{Grandchild}** `{path}` *({priority})* — Persona: {persona} | KW: {primary_keyword} | Traffic: {c}/{r}/{o} mo

*Traffic: C = conservative / R = realistic / O = optimistic monthly organic visits*
*Estimates based on keyword volume and average organic CTR by position. Figures represent opportunity scale, not guaranteed outcomes.*

### Notes
- {note 1}
```
