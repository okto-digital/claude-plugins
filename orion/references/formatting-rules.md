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
[R2] SERP — research/R2-SERP.txt
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
- **Max ~15 entries per section.** If you have more, you are logging detail, not signals. Combine related findings or drop the least impactful

**Anti-patterns — bloated vs telegraphic:**

Bad (methodology contamination, too much context):
```
- After analyzing the competitor landscape using DataForSEO backlink analysis and manual SERP review, we found that the top 3 competitors have domain authority scores of 45, 52, and 38 respectively, which suggests a moderately competitive niche where the client's current DA of 12 will require significant link-building investment to achieve first-page rankings for primary commercial keywords.
```

Good (one fact, one line, actionable):
```
- Client DA 12 vs top 3 competitors 38-52 — link building required for commercial keywords.
```

Bad (cross-reference bloat):
```
- As noted in the technology audit section and confirmed by the content analysis, the client's WordPress installation is running version 5.8.2 which is significantly outdated and poses both security vulnerabilities (3 known CVEs) and performance issues that were also flagged in the UX benchmark analysis.
```

Good:
```
- WordPress 5.8.2 — 3 known CVEs, security upgrade mandatory before launch.
```

## Proposal Impact Section

Every R-file must end with a `PROPOSAL IMPACT` section. This is the decision framework's Filter 1 applied at the output level — only findings that change the proposal.

```
================================================================================
PROPOSAL IMPACT
================================================================================

• Because {finding}, the proposal should {consequence}.
• Because {finding}, the proposal should {consequence}.
```

**Rules:**
- Each entry follows "Because X, the proposal should Y" — cause and consequence
- Only entries that change scope, price, or approach. If a finding doesn't appear here, it's context for other researchers, not a proposal driver
- No more than 10 entries. If you have more, you're not filtering hard enough
- CONFIRMED findings only. INFERRED may appear with explicit label

---

## Output Budgets

<critical>
Every output file has a character budget. Exceeding it means you are including methodology, cross-references, or granularity that downstream agents do not need. Cut content — do not compress prose into denser prose.
</critical>

**Budgets by file type:**

| File Type | Target | Hard Max | Notes |
|---|---|---|---|
| R-files (research) | 15,000 chars | 50,000 chars | Findings + evidence, not methodology |
| C-files (concept) | 20,000 chars | 50,000 chars | Recommendations + rationale, not research recap |
| D2 (client intelligence) | 10,000 chars | 30,000 chars | Facts about the client, not analysis |
| baseline-log (per section) | ~15 entries | ~30 entries | ~100 chars per entry average |

These are defaults. The `output_format` field in project.json can override:
- `concise` — target budgets apply (default)
- `detailed` — hard max budgets apply, target is relaxed to hard max

**What to cut first** (priority order):

1. **Methodology** — how you found it, which tools you used, your analytical process. The reader needs findings, not your workflow
2. **Cross-references** — "as noted in R3 and confirmed by D2". The baseline-log handles cross-phase context. Each file stands alone
3. **Scoring explanations** — "this scores 7/10 because...". State the score and the implication, drop the rubric
4. **Duplicate phrasings** — same finding stated differently in summary and detail sections. State it once
5. **Context available in baseline-log** — if a finding is already in baseline-log, the R/C-file needs the detail behind it, not a restatement of the same fact

**Self-check before writing:** If your output exceeds target, re-read every section and ask: "Does this change what we build, how we build it, or what we propose?" If no — cut it.
