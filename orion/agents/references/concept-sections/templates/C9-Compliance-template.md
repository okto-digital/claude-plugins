# C9-Compliance — Output Guide

Write scannable TXT per formatting-rules.md conventions.

## Expected Structure

```
================================================================================
COMPLIANCE SUMMARY
================================================================================

WCAG target: {A|AA|AAA}
Legal jurisdiction: {country/region}
Industry-specific: {regulations or "none"}

================================================================================
WCAG COMPLIANCE
================================================================================

Target level: {A|AA|AAA}
Rationale: {why this level} [src: {code}]
Legal drivers:
• {driver 1}
• {driver 2}

================================================================================
ACCESSIBILITY IMPLEMENTATION
================================================================================

DESIGN PHASE:
• {requirement — contrast, focus states, typography, etc.}
• {requirement}

DEVELOPMENT PHASE:
• {requirement — semantic HTML, ARIA, keyboard nav, etc.}
• {requirement}

CONTENT PHASE:
• {requirement — alt text, headings, link text, plain language, etc.}
• {requirement}

================================================================================
TESTING STRATEGY
================================================================================

Automated tools: {tool list}
Manual checklist: {key checks}
Screen reader scope: {which readers, which pages}
Device matrix: {browsers and devices}
Frequency: {during dev, pre-launch, post-launch cadence}

================================================================================
LEGAL COMPLIANCE
================================================================================

GDPR approach: {consent, data processing, policies} [src: {code}]
Cookie consent: {platform/approach}
Terms and policies: {what's needed}
Jurisdiction notes: {country-specific requirements}

================================================================================
INDUSTRY-SPECIFIC REQUIREMENTS
================================================================================

{If applicable:}
• {Regulation} ({applicability}):
  └─ {requirement}
  └─ {requirement}

{If none: "No industry-specific compliance requirements identified"}

================================================================================
ONGOING COMPLIANCE
================================================================================

Audit cadence: {frequency and approach}
Governance: {remediation process, training, documentation}

================================================================================
NOTES
================================================================================

• {Cross-section observation}
• Boundary: C2 captures WHAT compliance is required, C9 defines HOW
• Boundary: C3 covers compliance TOOLING, C9 covers STRATEGY and GOVERNANCE
```

## Field Notes

- C2 captures accessibility/GDPR as functional requirements (what's needed). C9 defines implementation strategy, testing, governance
- C3 covers technical implementation (which consent platform). C9 covers compliance strategy
- WCAG AA is typical default — justify if different
- Industry-specific section is conditional — only include applicable regulations
- Testing strategy browser/device scope should be consistent with C3 testing approach
