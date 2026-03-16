# C2-Functional — Output Templates

Write JSON as **minified** (no whitespace, no indentation).

## JSON Schema

```json
{
  "tldr": ["string — max 15 telegraphic decision items, scope/solution/quantitative"],
  "code": "C2",
  "slug": "Functional",
  "functional_requirements": [
    {
      "area": "string",
      "requirement": "string",
      "priority": "must_have | should_have | nice_to_have",
      "source": "string (e.g. 'G10-Forms: contact form checkpoint', 'R3-Competitors: competitor X has booking')",
      "complexity": "simple | moderate | complex"
    }
  ],
  "notes": ["string"]
}
```

Write to `concept/C2-Functional.json`.

## Markdown Template

Generate `concept/C2-Functional.md` from the JSON:

```markdown
## TLDR
- {tldr item 1}
- {tldr item 2}

## Functional Requirements

### Must Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Should Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Nice to Have
| Requirement | Area | Source | Complexity |
|---|---|---|---|
| {requirement} | {area} | {source} | {complexity} |

### Notes
- {note 1}
```
