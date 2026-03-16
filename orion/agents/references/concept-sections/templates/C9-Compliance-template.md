# C9-Compliance — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C9",
  "slug": "Compliance",
  "compliance": {
    "wcag": {
      "target_level": "string (A | AA | AAA)",
      "rationale": "string",
      "legal_drivers": ["string"]
    },
    "accessibility_implementation": {
      "design_phase": ["string"],
      "development_phase": ["string"],
      "content_phase": ["string"]
    },
    "testing_strategy": {
      "automated_tools": ["string"],
      "manual_checklist": ["string"],
      "screen_reader_scope": "string",
      "device_matrix": ["string"],
      "frequency": "string"
    },
    "legal_compliance": {
      "gdpr_approach": "string",
      "cookie_consent": "string",
      "terms_and_policies": "string",
      "jurisdiction_notes": "string"
    },
    "industry_specific": [
      {
        "regulation": "string",
        "applicability": "string",
        "requirements": ["string"]
      }
    ],
    "ongoing_compliance": {
      "audit_cadence": "string",
      "governance_approach": "string"
    }
  },
  "notes": ["string"]
}
```

Write to `concept/C9-Compliance.json`.

## Markdown Template

Generate `concept/C9-Compliance.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Compliance

### WCAG Compliance
**Target level:** {target_level}
**Rationale:** {rationale}
**Legal drivers:** {legal_drivers}

### Accessibility Implementation

**Design phase:**
- {design_phase item}

**Development phase:**
- {development_phase item}

**Content phase:**
- {content_phase item}

### Testing Strategy
**Automated tools:** {automated_tools}
**Manual checklist:** {manual_checklist}
**Screen reader scope:** {screen_reader_scope}
**Device matrix:** {device_matrix}
**Frequency:** {frequency}

### Legal Compliance
- **GDPR approach:** {gdpr_approach}
- **Cookie consent:** {cookie_consent}
- **Terms & policies:** {terms_and_policies}
- **Jurisdiction:** {jurisdiction_notes}

### Industry-Specific Requirements
{for each regulation}
**{regulation}** ({applicability})
- {requirement}
{end for}

### Ongoing Compliance
- **Audit cadence:** {audit_cadence}
- **Governance:** {governance_approach}

### Notes
- {note 1}
```
