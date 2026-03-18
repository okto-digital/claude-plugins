# C2-Functional — Output Guide

Write scannable TXT per formatting-rules.md conventions.

## Expected Structure

```
================================================================================
FUNCTIONAL REQUIREMENTS SUMMARY
================================================================================

Total requirements: {number}
Must have: {number} | Should have: {number} | Nice to have: {number}
Complexity: Simple {n} | Moderate {n} | Complex {n}

================================================================================
MUST HAVE
================================================================================

{Area}:
• {requirement} [src: {R/G/D2 code}] — {complexity}. CONFIRMED
• {requirement} [src: {R/G/D2 code}] — {complexity}. CONFIRMED

{Area}:
• {requirement} [src: {R/G/D2 code}] — {complexity}. CONFIRMED

================================================================================
SHOULD HAVE
================================================================================

{Area}:
• {requirement} [src: {R/G/D2 code}] — {complexity}. {CONFIRMED|INFERRED}

================================================================================
NICE TO HAVE
================================================================================

{Area}:
• {requirement} [src: {R/G/D2 code}] — {complexity}. INFERRED

================================================================================
NOTES
================================================================================

• {Cross-section observation}
```

## Field Notes

- Group by priority tier first, then by functional area within each tier
- Functional areas include: Core functionality, Ecommerce, User accounts, Booking/scheduling, Content management, Analytics, Integrations, GDPR/compliance, Performance, Accessibility
- Skip areas that don't apply
- Every requirement needs: source reference, complexity signal (simple/moderate/complex), confidence tag
- C2 captures WHAT is needed. C3 covers HOW (technology). C9 covers compliance STRATEGY
