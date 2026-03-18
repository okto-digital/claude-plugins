# Concept Section — UX Strategy

**Code:** C6
**Slug:** UX-Strategy
**Output:** `concept/C6-UX-Strategy.txt`
**Wave:** 2 (depends on C1-Sitemap)
**Hypothesis:** Conversion paths are missing or broken in current site UX

## Purpose

Define how users move through the site: navigation patterns, conversion funnels, CTA placement, trust signals, and mobile strategy. This is the behavioural layer — C1 defines what pages exist, C6 defines how users flow between them.

## Upstream Dependency

**Reads C1-Sitemap output** for the page tree and page count. Navigation model scales to sitemap complexity. User flows reference specific pages from C1.

## Methodology

1. Read the context file.
2. Produce:
   - **Navigation model** — primary structure, mobile approach, secondary/utility nav. Scale to C1 page count.
   - **Conversion funnels** — 2-3 paths per persona from entry to target action. Name the pages involved and the rationale for each path.
   - **CTA strategy** — primary and secondary CTA per page type. Placement rationale.
   - **Trust elements** — which signals where (testimonials, badges, guarantees, case studies) with rationale per persona.
   - **Mobile strategy** — mobile-first vs responsive rationale. Content priority order for mobile. Touch target considerations.
   - **Key user flows** — 2-3 page sequences with persona mapping. Goal, entry, steps, outcome. Reference C1 pages by name.

## Output

Follow output guide at `templates/C6-UX-Strategy-template.md`.
