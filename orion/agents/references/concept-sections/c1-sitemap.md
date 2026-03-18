# Concept Section — Sitemap

**Code:** C1
**Slug:** Sitemap
**Output:** `concept/C1-Sitemap.txt`
**Wave:** 1 (no upstream dependencies)
**Hypothesis:** The site needs more pages than the client expects, driven by keyword opportunities

## Purpose

Build the full site structure as a nested page tree. Each page is mapped to a persona, keywords, and traffic estimates. The sitemap is the structural backbone of the concept — it defines what pages exist and why.

## Methodology

1. Read the context file.
2. Use R9 page structure as the starting skeleton.
3. Cross-reference with R2 keywords — ensure every high-value cluster has a landing page.
4. Check gap analysis findings for resolved requirements that imply pages (e.g., "client needs booking page").
5. For each page, assign:
   - Primary persona
   - Primary keyword + secondary keywords
   - Combined search volume (sum of mapped keywords)
   - Traffic estimates at three CTR scenarios:
     - **Conservative** — position 6-10 CTR (~4%)
     - **Realistic** — position 3-5 CTR (~8%)
     - **Optimistic** — position 1-2 CTR (~20%)
   - Priority: `must_have`, `should_have`, `nice_to_have`
6. Nest pages into a URL hierarchy.
7. Sum traffic for total site traffic potential.
8. Include utility pages (privacy, cookie, 404, sitemap) as `must_have` without traffic estimates.

**Traffic note:** Estimates are opportunity scale, not guaranteed outcomes. Actual traffic depends on ranking, content quality, and competition.

## Output

Follow output guide at `templates/C1-Sitemap-template.md`.
