# C3-Technical-Architecture — Output Guide

Write scannable TXT per formatting-rules.md conventions.

## Expected Structure

```
================================================================================
TECHNICAL ARCHITECTURE SUMMARY
================================================================================

CMS/Framework: {recommendation}
Hosting: {recommendation}
Complexity: {overall assessment}

================================================================================
TECHNOLOGY STACK
================================================================================

CMS/FRAMEWORK:
• Recommendation: {solution}
• Rationale: {tied to C2 requirements} [src: {code}]
• Alternatives considered: {options and why not chosen}
• Complexity: {simple|moderate|complex}

HOSTING:
• Recommendation: {solution}
• Rationale: {tied to requirements} [src: {code}]
• Alternatives considered: {options}
• Complexity: {simple|moderate|complex}

KEY INTEGRATIONS:
• {Integration name}: {solution} [src: {code}] — {complexity}
• {Integration name}: {solution} [src: {code}] — {complexity}

PERFORMANCE STRATEGY:
• CDN: {approach}
• Caching: {approach}
• Image optimisation: {approach}
• Rationale: {tied to requirements} [src: {code}]

GDPR COMPLIANCE APPROACH:
• Cookie consent: {platform/approach}
• Data handling: {approach}
• Rationale: {tied to requirements} [src: {code}]

SEO TECHNICAL FOUNDATION:
• Schema markup: {approach}
• Sitemap: {approach}
• Robots/canonical: {approach}

================================================================================
OPERATIONS
================================================================================

DEPLOYMENT PIPELINE:
• Staging: {approach}
• CI/CD: {approach or "not needed — scale doesn't justify"}
• Version control: {approach}

TESTING APPROACH:
• QA strategy: {approach}
• Browser/device scope: {list}
• Performance testing: {approach}

MONITORING:
• Uptime: {approach}
• Performance tracking: {approach}
• Error logging: {approach}

UPDATE STRATEGY:
• CMS/plugin updates: {cadence}
• Backup verification: {approach}
• Security patches: {approach}

================================================================================
NOTES
================================================================================

• {Cross-section observation}
• Boundary: GDPR implementation here, governance in C9
• Boundary: Testing infrastructure here, accessibility testing in C9
• Boundary: Update systems here, schedule/ownership in C7
```

## Field Notes

- Skip categories that don't apply (e.g., ecommerce integrations for a brochure site)
- Each recommendation needs: solution, rationale tied to C2 requirements, alternatives considered, complexity
- C3 covers technical HOW. C2 covers functional WHAT. C9 covers compliance strategy/governance. C7 covers schedule/ownership
