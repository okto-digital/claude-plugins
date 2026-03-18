# Concept Section — Functional Requirements

**Code:** C2
**Slug:** Functional
**Output:** `concept/C2-Functional.txt`
**Wave:** 1 (no upstream dependencies)
**Hypothesis:** Core functionality gaps exist that require custom development

## Purpose

Define what the website needs to do. Every functional requirement is traceable to a gap analysis finding, client answer, competitor benchmark, or industry standard.

## Methodology

1. Read the context file.
2. Group requirements by functional area:
   - Core functionality (navigation, search, contact forms)
   - Ecommerce (if applicable)
   - User accounts (if applicable)
   - Booking and scheduling (if applicable)
   - Content management (blog, editorial, media)
   - Analytics and measurement
   - Integrations (CRM, ERP, accounting, email marketing)
   - GDPR and compliance
   - Performance requirements
   - Accessibility requirements
3. Tag each requirement with priority (`must_have`, `should_have`, `nice_to_have`), source, and complexity (`simple`, `moderate`, `complex`).
4. Skip functional areas that don't apply.

**Note:** C2 captures accessibility and GDPR as functional requirements (what's needed, at what priority). Implementation strategy, testing approach, and ongoing governance for these areas are defined in C9-Compliance.

## Output

Follow output guide at `templates/C2-Functional-template.md`.
