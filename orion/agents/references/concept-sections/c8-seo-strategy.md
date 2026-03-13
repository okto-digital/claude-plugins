# Concept Section — SEO Strategy

**Code:** C8
**Slug:** SEO-Strategy
**Output:** `concept/C8-SEO-Strategy.json`, `concept/C8-SEO-Strategy.md`
**Wave:** 3 (depends on C1-Sitemap)

## Purpose

Define the SEO strategy beyond what C1 (keyword-page mapping) and C3 (technical SEO foundation) already cover. Addresses link acquisition, local/international SEO, search feature targeting, and monitoring. References C1 as the keyword foundation without duplicating it. SEO-specific measurement lives here; project-level KPIs are in C7.

## Upstream Dependency

**Reads C1-Sitemap output** for the keyword-page mapping. C8 builds the off-page and advanced on-page strategy on top of C1.

## Methodology

1. Read the context file. Check D1-Init for location data (local SEO) and language config (international SEO).
2. Produce:
   - **Link acquisition strategy** — approach, priority targets, domain types. Pragmatic — scaled to client resources.
   - **Local SEO** (if D1 has physical location) — GMB, citations, NAP consistency, local content. Set to null if not applicable.
   - **International SEO** (if D1 has multiple languages) — hreflang, market adaptation, content priority, URL structure. Set to null if not applicable.
   - **Search feature optimization** — which SERP features to target per page type. Include structured data recommendations tied to C1 page types.
   - **SEO monitoring and KPIs** — rank tracking scope, traffic targets by timeframe (tied to C1 estimates), reporting cadence, tools.
   - **C1 reference** — note that on-page keyword targeting is in C1 (not duplicated here).

## Output

Write output using the templates at `templates/C8-SEO-Strategy-template.md`.
