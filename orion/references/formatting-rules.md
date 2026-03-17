# Formatting Rules

How to format output. The decision framework (`decision-framework.md`) defines how to think. This file defines how to write.

## Source Binding

Every finding must reference where it came from. No source = drop the finding.

**In R-files, D-files, G-files, C-files:** Tag with `[src: category]` — categories: `tool`, `document`, `registry`, `operator`, `url`, `other`.

**Confidence** — end every finding with one of:
- CONFIRMED — found directly in source, verifiable
- INFERRED — deduced from available evidence
- MISSING — looked for, not found (the absence IS the finding)

Findings that affect scope or pricing need 2 independent sources for CONFIRMED. Single source = INFERRED. An agent that reports MISSING is more valuable than one that invents a plausible number.

## Scannable Formatting (R-files, D-files, G-files, C-files)

Output files should be **scannable** — a reader skimming the file finds what they need in seconds.

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

**Conventions:**
- `====` divider (80 chars) before each major section
- ALL CAPS for section headers
- `Key: Value` for metadata and facts
- `•` for unordered lists, numbered for ordered
- `→` for URLs, links, references
- `└─` for hierarchy/tree structure
- `✓` / `✗` for presence checks
- `PRIORITY N — Label:` for grouped items
- No markdown — pure TXT that renders identically everywhere

## Baseline Log

<critical>
The baseline log is a **signal index**, not a research summary. Only key findings that change downstream decisions. Telegraphic one-liners. No prose, no paragraphs, no roadmaps, no methodology notes.
</critical>

**Format:**
```
--- [R1] SERP ---
[R1] Client ranks for 2 keywords only, zero commercial keywords indexed. CONFIRMED
[R1] "komerčná fotografia" greenfield — zero related keywords, jms-studio.sk sole occupant. CONFIRMED
```

**Rules:**
- Start with a `--- [CODE] TITLE ---` header before your entries
- Tag every line with your phase code: `[INIT]`, `[D2]`, `[R1]`–`[R9]`, `[D4]`, etc.
- One fact per line. If it takes more than one line, split it or you're including too much
- No `[src: ...]` tags — the phase code IS the source reference
- No empty lines between your entries
- End each line with CONFIRMED, INFERRED, or MISSING
- **Deduplicate:** Read existing baseline-log entries BEFORE appending. If a finding already exists, do NOT re-log it. Only add if you bring new quantification or a materially different angle
- **Append at once:** Accumulate all your entries, then append them in a single batch at the end of your work. Do not append incrementally during processing
- Do NOT invent tags. The only valid confidence markers are CONFIRMED, INFERRED, MISSING. Do not use CRITICAL DECISION POINT or other ad-hoc labels
- Never edit or delete existing lines — append only
