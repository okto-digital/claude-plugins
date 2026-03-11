# Domain Output — Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

### Active domain

```json
{
  "code": "string (G-code, e.g. G05)",
  "slug": "string (e.g. Business)",
  "domain": "string (domain-id, e.g. business-context)",
  "status": "ACTIVE",
  "summary": "string (1-2 sentence domain assessment)",
  "counts": {
    "found": "number",
    "partial": "number",
    "gap": "number",
    "na": "number",
    "total": "number",
    "critical_resolved": "number",
    "critical_total": "number"
  },
  "findings": [
    {
      "section": "string (section name from domain file, e.g. Business Identity)",
      "checkpoint": "string (exact wording from domain file)",
      "priority": "CRITICAL | IMPORTANT | NICE-TO-HAVE",
      "status": "FOUND | PARTIAL | GAP | N/A",
      "evidence": "string | null (specific data supporting FOUND or PARTIAL)",
      "reason": "string | null (why N/A, if applicable)"
    }
  ],
  "questions": [
    {
      "checkpoint": "string (exact checkpoint this question addresses)",
      "severity": "CRITICAL | IMPORTANT",
      "question": "string",
      "answer": null
    }
  ],
  "notes": ["string"]
}
```

`critical_resolved` counts FOUND checkpoints that have CRITICAL priority. `critical_total` counts all CRITICAL priority checkpoints.

### Inactive domain

```json
{
  "code": "string (G-code, e.g. G09)",
  "slug": "string (e.g. Ecommerce)",
  "domain": "string (domain-id)",
  "status": "INACTIVE",
  "inactive_reason": "string (one line explaining why domain does not apply)"
}
```

Write to `gap-analysis/{code}-{slug}.json` (e.g., `gap-analysis/G05-Business.json`).

---

## Markdown Template

Generate `gap-analysis/{code}-{slug}.md` from the JSON (e.g., `gap-analysis/G05-Business.md`).

### Active domain

```markdown
## {Domain Name}
**{domain-id}** — {found} FOUND, {partial} PARTIAL, {gap} GAP, {na} N/A | {critical_resolved}/{critical_total} CRITICAL resolved

### {Section Name}
- [FOUND] {checkpoint} — evidence: "{evidence}"
- [PARTIAL] {checkpoint} — evidence: "{partial evidence}"
- [GAP] {checkpoint} [{priority}]
- [N/A] {checkpoint} — reason: {reason}

### Questions
**1. {Question text}** — {checkpoint} [{severity}]
*Answer:* _[to be filled]_

---
```

If there are no questions: `### Questions\nNone — all CRITICAL and IMPORTANT checkpoints resolved.`

### Inactive domain

```markdown
## {Domain Name}
**{domain-id}** — INACTIVE: {inactive_reason}

---
```
