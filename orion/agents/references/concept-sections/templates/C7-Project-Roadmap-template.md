# C7-Project-Roadmap — Output Guide

Write scannable TXT per formatting-rules.md conventions.

## Expected Structure

```
================================================================================
LAUNCH SCOPE
================================================================================

MUST HAVE (Phase 1):
• {page or feature} [src: C1/C2 priority]
• {page or feature} [src: C1/C2 priority]

SHOULD HAVE (Phase 2):
• {page or feature} [src: C1/C2 priority]

OUT OF SCOPE:
• {item} — Reason: {why deferred}

================================================================================
PHASES
================================================================================

PHASE 1 — {name}:
• Deliverables: {pages + features}
• Dependencies: {what must exist first, or "none"}
• Rationale: {why this grouping}

PHASE 2 — {name}:
• Deliverables: {pages + features}
• Dependencies: {what must exist first}
• Rationale: {why this grouping}

PHASE 3 — {name} (if needed):
• Deliverables: {pages + features}
• Dependencies: {what must exist first}
• Rationale: {why this grouping}

================================================================================
SUCCESS METRICS
================================================================================

LAUNCH:
• {KPI}: {target} [src: {evidence}]
• {KPI}: {target} [src: {evidence}]

3 MONTHS:
• {KPI}: {target} [src: {evidence}]

6 MONTHS:
• {KPI}: {target} [src: {evidence}]

12 MONTHS:
• {KPI}: {target} [src: {evidence}]

================================================================================
POST-LAUNCH
================================================================================

Content governance: {who publishes, review cadence}
Maintenance: {updates, backups, security — system from C3, cadence here}
Growth: {what to measure, when to expand}

================================================================================
RISKS
================================================================================

• {risk} — Impact: {high|medium|low} | Mitigation: {approach} [src: {code}]
• {risk} — Impact: {high|medium|low} | Mitigation: {approach} [src: {code}]

================================================================================
NOTES
================================================================================

• {Cross-section observation}
• Must-have items derived from C1/C2 priority tags
• Technical constraints from C3 inform phase sequencing
```

## Field Notes

- Launch scope items must trace to C1 page priorities and C2 requirement priorities
- Must-have items belong in Phase 1 — flag any priority inversion
- Success metrics tied to business goals and C1 traffic potential — don't exceed optimistic estimates
- 2-4 phases typically sufficient
- Post-launch plan: C3 covers update systems, C7 covers schedule and ownership
- Risks sourced from scope constraints, technical complexity, integration dependencies
