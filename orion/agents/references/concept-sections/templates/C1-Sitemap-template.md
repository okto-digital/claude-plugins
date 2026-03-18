# C1-Sitemap — Output Guide

Write scannable TXT per formatting-rules.md conventions.

## Expected Structure

```
================================================================================
SITEMAP SUMMARY
================================================================================

Total pages: {number}
Must have: {number} | Should have: {number} | Nice to have: {number}
Traffic potential: Conservative {n}/mo | Realistic {n}/mo | Optimistic {n}/mo

================================================================================
PAGE TREE
================================================================================

MUST HAVE:
• {Page Name} /{path} — Persona: {who} | KW: {keyword} ({vol}) | Traffic: {c}/{r}/{o}
  └─ {Child Page} /{path} — Persona: {who} | KW: {keyword} ({vol}) | Traffic: {c}/{r}/{o}
    └─ {Grandchild} /{path} — Persona: {who} | KW: {keyword} ({vol}) | Traffic: {c}/{r}/{o}

SHOULD HAVE:
• {Page Name} /{path} — Persona: {who} | KW: {keyword} ({vol}) | Traffic: {c}/{r}/{o}

NICE TO HAVE:
• {Page Name} /{path} — Persona: {who} | KW: {keyword} ({vol}) | Traffic: {c}/{r}/{o}

UTILITY PAGES:
• Privacy Policy /privacy — must_have, no traffic estimate
• Cookie Policy /cookies — must_have, no traffic estimate
• 404 /404 — must_have, no traffic estimate
• Sitemap /sitemap — must_have, no traffic estimate

================================================================================
NOTES
================================================================================

• {Cross-section observation or methodology note}
• Traffic: C = conservative (pos 6-10, ~4% CTR) / R = realistic (pos 3-5, ~8%) / O = optimistic (pos 1-2, ~20%)
• Estimates represent opportunity scale, not guaranteed outcomes
```

## Field Notes

- Group pages by priority tier (MUST HAVE, SHOULD HAVE, NICE TO HAVE)
- Preserve URL hierarchy using `└─` tree notation
- Every non-utility page needs: persona, primary keyword, combined volume, traffic estimate at three tiers
- Utility pages (privacy, cookie, 404, sitemap) are always must_have with no traffic estimates
- Source references: tag keyword sources with `[src: R2]`, page additions with `[src: D4]`, etc.
