# Domain Output — Templates

Write all JSON as **minified single line** (no whitespace, no indentation).

## JSON Schema — Findings

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
    "critical_resolved": "number (FOUND checkpoints with CRITICAL priority)",
    "critical_total": "number (all CRITICAL priority checkpoints)",
    "questions_generated": "number (questions written to separate question file)",
    "questions_resolved": "number (answers applied from D4-Answers.json, 0 initially)"
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
  "notes": ["string"]
}
```

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

Write to `gap-analysis/{code}-{slug}.json`.

---

## JSON Schema — Questions

Per-domain question file. Write to `gap-analysis/questions/{code}-{slug}-questions.json`.
Only written for active domains with CRITICAL or IMPORTANT gaps/partials.

```json
[
  {
    "id": "string ({G-code}-Q{nn}, unique across all domains, sequential starting Q01)",
    "domain": "string (domain-id)",
    "checkpoint": "string (exact checkpoint wording from domain file)",
    "severity": "CRITICAL | IMPORTANT",
    "question": "string (business-first framing, under 3 sentences)",
    "context": "string (one line of evidence from research that grounds the question)",
    "options": [
      { "id": "na", "label": "Not applicable" },
      { "id": "a1", "label": "string (most likely answer — agent-suggested)" },
      { "id": "a2", "label": "string (second option — agent-suggested)" },
      { "id": "a3", "label": "string (third option — agent-suggested)" },
      { "id": "other", "label": "Other", "freetext": true }
    ],
    "selected": null,
    "freetext_response": null
  }
]
```

Always exactly 5 options per question. `selected` and `freetext_response` are always null (filled by operator).

---

## Markdown Template — Findings

Generate `gap-analysis/{code}-{slug}.md` from the JSON.

### Active domain

```markdown
## {Domain Name}
**{domain-id}** — {found} FOUND, {partial} PARTIAL, {gap} GAP, {na} N/A | {critical_resolved}/{critical_total} CRITICAL resolved | {questions_generated} questions

### {Section Name}
- [FOUND] {checkpoint} — evidence: "{evidence}"
- [PARTIAL] {checkpoint} — evidence: "{partial evidence}"
- [GAP] {checkpoint} [{priority}]
- [N/A] {checkpoint} — reason: {reason}

---
```

### Inactive domain

```markdown
## {Domain Name}
**{domain-id}** — INACTIVE: {inactive_reason}

---
```

---

## D4-Answers Schema

Answer template generated from D4-Questions.json at the end of gap analysis. Operator fills `answer` field.

```json
[
  {
    "id": "string ({G-code}-Q{nn})",
    "domain": "string (domain-id)",
    "checkpoint": "string (exact checkpoint wording)",
    "answer": "string | \"N/A\" | null"
  }
]
```

**Answer values:**
- `"text"` — finding becomes FOUND, evidence = answer text
- `"N/A"` — finding becomes N/A, reason = "Not applicable (client)"
- `null` — skip (unanswered, finding stays as GAP/PARTIAL)
