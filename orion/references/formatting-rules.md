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
The baseline log is a **signal index**, not a research summary. Only CONFIRMED findings that directly influence website design, development, or scope decisions. If a finding doesn't change what we build, how we build it, or what we propose — it does not belong here. No prose, no paragraphs, no roadmaps, no methodology notes.
</critical>

**Format:**
```
================================================================================
[R1] SERP — research/R1-SERP.txt
================================================================================
- Client ranks for 2 keywords only, zero commercial keywords indexed.
- "komerčná fotografia" greenfield — zero related keywords, jms-studio.sk sole occupant.
```

**Rules:**
- Use `====` divider (80 chars) + `[CODE] TITLE — source/file/path.txt` + `====` divider as section header
- `- ` bullet per finding. One fact per line — if it takes more than one line, split it or you're including too much
- **Only confirmed findings.** No INFERRED, no MISSING, no confidence tags. The baseline log is evidence, not speculation
- No `[src: ...]` tags — the section header identifies the source
- No empty lines between entries within a section
- **Deduplicate:** Read existing baseline-log entries BEFORE appending. If a finding already exists, do NOT re-log it. Only add if you bring new quantification or a materially different angle
- **Append at once:** Accumulate all your entries, then append them in a single batch at the end of your work. Do not append incrementally during processing
- Never edit or delete existing lines — append only
