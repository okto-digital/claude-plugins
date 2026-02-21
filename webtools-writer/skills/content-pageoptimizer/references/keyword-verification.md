# Keyword Verification Methodology

Rules for counting keyword occurrences and generating the verification scorecard.

---

## Counting Rules

### Case Sensitivity

Keyword matching is **case-insensitive**. "Mobile App Development" matches "mobile app development" and "MOBILE APP DEVELOPMENT".

### Word Boundaries

Match whole words only. "app" should NOT match "application" or "appy". Use word boundary detection:
- Space, punctuation, or start/end of text around the keyword
- Hyphenated forms count: "mobile-friendly" matches "mobile-friendly"

### Phrase Matching

Multi-word keywords match as a contiguous phrase. "mobile app development" matches only when those three words appear consecutively (with optional punctuation between them). It does NOT match "mobile and app development" or "mobile applications development".

### Overlapping Keywords

Keywords may overlap. For example:
- "mobile app development" (3 words)
- "mobile app development company" (4 words)
- "app development" (2 words)

Each keyword is counted independently. A single occurrence of "mobile app development company" counts as:
- 1 occurrence of "mobile app development company"
- 1 occurrence of "mobile app development"
- 1 occurrence of "app development company"
- 1 occurrence of "app development"

### Section Boundaries

Count keywords ONLY within their designated section:
- **Title keywords**: count only in the meta_title value from frontmatter
- **Page Title keywords**: count only in the H1 text (the `#` heading)
- **Subheading keywords**: count only in H2-H6 heading text (all combined into one pool)
- **Body keywords**: count only in body text (paragraphs, lists, blockquotes, table cells). Exclude all headings (H1-H6) from body count.

### What NOT to count

- Text inside YAML frontmatter (except meta_title for the Title section)
- Markdown syntax characters (`#`, `*`, `-`, `[`, `]`, etc.)
- URLs in link targets `[text](url)` -- count the link text, not the URL
- Image alt text counts as body content
- HTML tags if any remain

---

## Scorecard Format

### Optimization Target

<critical>
ALWAYS aim for targetMax for every keyword. The target range is NOT a "minimum acceptable" -- it is the scoring zone. Higher within the range is better.

A keyword with target `0-1` means "use this keyword 1 time." It does NOT mean "optional." The 0 in the range means PageOptimizer won't penalize you for skipping it, but including it improves your score. The agent must attempt to place every keyword at its targetMax.

A keyword with target `1-2` means "aim for 2 uses." Hitting 1 is acceptable but 2 is the goal.

There are NO optional keywords. Every keyword in the brief is an opportunity to improve the page score. Treat them all as targets.
</critical>

### Per-Keyword Status

| Status | Condition |
|---|---|
| MAXED | `current == targetMax` (ideal -- keyword at maximum target) |
| HIT | `current >= targetMin AND current <= targetMax AND current > 0` |
| PARTIAL | `current > 0 AND current < targetMin` |
| MISS | `current == 0 AND targetMax > 0` (keyword not used at all despite having a target) |
| OVER | `current > targetMax` |

Note: There is no OPTIONAL status. Even `0-1` targets should be pursued. A keyword at 0 with target `0-1` has status MISS -- it is an opportunity the agent should try to fill.

### Section Summary

For each section, report:
- Total keywords
- Keywords with status MAXED (at maximum target -- ideal)
- Keywords with status HIT (in range but below max)
- Keywords with status PARTIAL (some usage but below minimum)
- Keywords with status MISS (not used at all)
- Keywords with status OVER (exceeds target -- do not add more)

### Overall Summary

- Total keywords across all sections
- Percentage at MAXED or HIT
- Word count: before, after, target
- Verdict: PASS (>90% at MAXED/HIT), NEEDS WORK (70-90%), SIGNIFICANT GAPS (<70%)

---

## Re-Optimization Counting

On re-optimization runs, the "before" column in the scorecard reflects the state of the `pageoptimized-` file at the start of this run, NOT the original extracted content. The briefs attached by the operator already reflect current counts from PageOptimizer.pro's latest scoring.

Verify that your own keyword counts approximately match the brief's "current" numbers. Small discrepancies are normal (PageOptimizer may count slightly differently). Large discrepancies (off by more than 2) suggest a parsing or section boundary issue -- investigate before proceeding.
