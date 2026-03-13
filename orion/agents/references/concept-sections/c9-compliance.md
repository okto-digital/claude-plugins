# Concept Section — Compliance

**Code:** C9
**Slug:** Compliance
**Output:** `concept/C9-Compliance.json`, `concept/C9-Compliance.md`
**Wave:** 3 (depends on C2-Functional)

## Purpose

Define the accessibility and legal compliance strategy: WCAG target, implementation approach, testing, legal requirements, and ongoing governance. C2 captures *that* compliance is required; C9 defines *how* to achieve and maintain it. C3 covers compliance *tooling*; C9 covers compliance *strategy and governance*.

## Upstream Dependency

**Reads C2-Functional output** for accessibility and GDPR requirements already captured. C9 expands these into implementation strategy, testing, and governance.

## Methodology

1. Read the context file. Check D1-Init for industry, location (jurisdiction), and target markets.
2. Produce:
   - **WCAG compliance level** — target level (A, AA, AAA) with rationale. AA is typical; justify if different.
   - **Accessibility implementation approach** — what to address in each phase: design (contrast, focus states, typography), development (semantic HTML, ARIA, keyboard nav), content (alt text, headings, link text, plain language).
   - **Testing strategy** — automated tools, manual checklist, screen reader scope, device matrix, frequency (during dev, pre-launch, post-launch).
   - **Legal compliance** — GDPR approach (consent, data processing, policies), cookie consent, terms/policies, jurisdiction-specific requirements.
   - **Industry-specific requirements** — only what applies: EAA 2025, ADA, sector-specific (HIPAA, PCI-DSS, etc.).
   - **Ongoing compliance** — audit cadence and governance approach (remediation, training, documentation).

## Output

Write output using the templates at `templates/C9-Compliance-template.md`.
