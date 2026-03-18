# Concept Section — Project Roadmap

**Code:** C7
**Slug:** Project-Roadmap
**Output:** `concept/C7-Project-Roadmap.txt`
**Wave:** 3 (depends on C1-Sitemap, C2-Functional, C3-Technical-Architecture)
**Hypothesis:** Full scope exceeds a single launch — phased delivery is necessary

## Purpose

Define the phased delivery plan: what launches first, what follows, and what success looks like. Turns the sitemap, functional requirements, and technical architecture into an actionable timeline with clear scope boundaries and measurable targets.

## Upstream Dependencies

- **Reads C1-Sitemap** for page priorities (must_have, should_have, nice_to_have) and traffic potential targets.
- **Reads C2-Functional** for requirement priorities and complexity signals.
- **Reads C3-Technical-Architecture** for technical constraints and infrastructure sequencing.

## Methodology

1. Read the context file.
2. Produce:
   - **Launch scope** — explicit lists of must_have (= MVP / Phase 1), should_have (= Phase 2), and out-of-scope items. Derived from C1/C2 priority tags and G15 scope constraints. Resolves any priority conflicts between C1 pages and C2 requirements.
   - **Phase breakdown** — 2-4 delivery phases, each with: name, deliverables (pages + features), dependencies on prior phases, and rationale for the grouping. Phase 1 = minimum viable launch. Subsequent phases add value incrementally.
   - **Success metrics** — KPIs per timeframe (launch, 3-month, 6-month, 12-month). Tied to business goals from G02 and traffic potential from C1. Include: traffic targets, conversion targets, performance baselines, and content milestones.
   - **Post-launch plan** — content governance (who publishes, review cadence), maintenance schedule (updates, backups, security), growth roadmap (what to measure and when to expand). Grounded in G14 findings.
   - **Risks** — key delivery risks with impact assessment and mitigations. Sources: G15 scope risks, C3 technical complexity, C2 integration dependencies.

## Output

Follow output guide at `templates/C7-Project-Roadmap-template.md`.
