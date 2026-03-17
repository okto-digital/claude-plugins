# Formatting Rules

Output files (R-files, D-files, G-files, C-files) should be **scannable** — a reader skimming the file finds what they need in seconds.

## Conventions

```
================================================================================
SECTION TITLE IN CAPS
================================================================================

Key: Value
Another Key: Longer value with detail

• Bullet point for unordered items
• Another bullet point

1. Numbered item
   → https://example.com/link
2. Second item
   └─ Sub-item (tree structure)
   └─ Another sub-item

✓ Present/confirmed item
✗ Missing/absent item

PRIORITY 1 — Critical:
• Item one
• Item two

PRIORITY 2 — Important:
• Item three
```

## Rules

- `====` divider (80 chars) before each major section
- ALL CAPS for section headers
- `Key: Value` for metadata and facts
- `•` for unordered lists, numbered for ordered
- `→` for URLs, links, references
- `└─` for hierarchy/tree structure
- `✓` / `✗` for presence checks
- `PRIORITY N — Label:` for grouped items
- No markdown — pure TXT that renders identically everywhere

## Exemptions

**baseline-log.txt** stays flat — no dividers, no formatting. See the Baseline Log section in `decision-framework.md`.
