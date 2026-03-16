# PageOptimizer 5-Phase Workflow

Rules for the Optimize mode. Follows the PageOptimizer.pro keyword optimization methodology.

---

## Overview

The operator scores a page in PageOptimizer.pro, exports 4 content brief files, and provides them to the plugin. The plugin runs 5 phases: Analyze, Plan, Rewrite, Verify, Save+Export.

---

## Brief Files

The 4 required files exported from PageOptimizer.pro:
- `ContentBrief_title.txt` -- keyword targets for the `<title>` tag
- `ContentBrief_pageTitle.txt` -- keyword targets for the H1
- `ContentBrief_subHeadings.txt` -- keyword targets for H2-H6 collectively
- `ContentBrief_BodyContent.txt` -- keyword targets for body content

Parse each file following the format rules in `${CLAUDE_PLUGIN_ROOT}/references/pageoptimizer/brief-parsing.md`.

---

## Phase 1: Analyze

Split the source content into 4 zones:
- **Title**: `meta_title` from YAML frontmatter
- **H1**: the first `#` heading in the markdown body
- **Subheadings**: all `##` through `######` headings (text only)
- **Body**: everything else -- paragraphs, lists, blockquotes, table cells

For each zone, count current occurrences of every keyword from the corresponding brief file. Use the counting rules in `${CLAUDE_PLUGIN_ROOT}/references/pageoptimizer/keyword-verification.md`.

Present a gap summary:

```
ANALYSIS: [page name]

Title:       [n] keywords -- [x] in range, [y] below target, [z] at zero
Page Title:  [n] keywords -- [x] in range, [y] below target, [z] at zero
Subheadings: [n] keywords -- [x] in range, [y] below target, [z] at zero
Body Content: [n] keywords -- [x] in range, [y] below target, [z] at zero

Word count: [current] words (target: [target])
```

---

## Phase 2: Plan

<critical>
ALWAYS show the plan to the operator and wait for approval before rewriting. Never start rewriting without explicit approval.
</critical>

### Title + H1

Handle together. Per PageOptimizer guidance, the search engine title and H1 should be as identical as possible.

- List all keyword targets from both title and pageTitle briefs
- Propose 2-3 title/H1 options that incorporate the highest-priority terms
- Show which keywords each option covers

### Subheadings

Subheading keywords work as a **collective group** -- the goal is to distribute keywords across all subheadings so the section as a whole hits the target range.

- Group keywords by natural clusters (shared root phrases)
- Propose new or revised subheadings that absorb keyword clusters
- Show which keywords each proposed subheading covers
- Mark which subheadings are existing (revised) vs new

### Body Content

- Identify keyword clusters that need new sections or extended paragraphs
- Estimate word count increase needed to reach target
- Propose new sections/topics that naturally absorb keyword clusters
- Show keyword distribution plan: which keywords go into which sections

Present the full plan and wait for the operator to approve, adjust, or request changes.

---

## Phase 3: Rewrite

Execute the approved plan section by section.

**Title + H1:** Write the chosen title and H1. Update `meta_title` in frontmatter and the `#` heading in the body.

**Subheadings:** Revise existing and add new subheadings per plan.

**Body content:** Rewrite and extend section by section:
- Preserve existing content structure where keywords already hit targets
- Extend sections that need more keyword coverage
- Add new sections as planned
- Maintain brand voice throughout (from voice-definition.md)
- Integrate keywords naturally. If content reads awkwardly, restructure rather than force keywords.

<critical>
Every keyword from ALL 4 briefs must be addressed. Do not silently skip any keyword. If a keyword is genuinely impossible to place naturally, flag it to the operator with an explanation and suggested alternatives.
</critical>

---

## Phase 4: Verify

Count every keyword in the rewritten content and generate a full scorecard. Follow the verification methodology in `${CLAUDE_PLUGIN_ROOT}/references/pageoptimizer/keyword-verification.md`.

Present the scorecard:

```
KEYWORD SCORECARD: [page name]

TITLE ([x]/[total] in target range)
  keyword              before  after  target   status
  -------              ------  -----  ------   ------
  example keyword         0      1    1        MAXED
  another keyword         0      1    0-1      MAXED
  third keyword           0      0    0-1      MISS
  ...

PAGE TITLE ([x]/[total] in target range)
  ...

SUBHEADINGS ([x]/[total] in target range)
  ...

BODY CONTENT ([x]/[total] in target range)
  ...

OVERALL
  Word count: [before] -> [after] (target: [target])
  Keywords hitting target: [n]/[total] ([percentage]%)
```

**Status labels:**
- **MAXED** -- count equals max of target range (no room to add more)
- **HIT** -- count within target range but below max
- **PARTIAL** -- count improved but still below target min
- **MISS** -- count unchanged at zero or below target
- **OVER** -- count exceeds max of target range

If any keywords still miss their target, list them with specific placement suggestions.

If the operator requests changes, iterate: adjust content, re-verify, show updated scorecard. Repeat until approved.

---

## Phase 5: Save and Export

### 1. Build output filename

Derive the slug from the source file:
- `extracted-{slug}.md` becomes `optimized-{slug}.md`
- `draft-{slug}.md` becomes `optimized-{slug}.md`
- `optimized-{slug}.md` stays `optimized-{slug}.md` (overwrite)

### 2. Write the optimized markdown

Write to `content/optimized-{slug}.md` with frontmatter:

```yaml
---
document_type: optimized-content
title: "[optimized title]"
meta_title: "[optimized meta title]"
meta_description: "[optimized or preserved meta description]"
source_url: "[preserved from source file]"
optimization_source: "[source .md filename]"
optimized: [today]
status: optimized
---
```

### 3. Export to HTML

Convert the optimized markdown to clean semantic HTML following the rules in `${CLAUDE_PLUGIN_ROOT}/references/pageoptimizer/html-export-rules.md`. Write to `content/export-{slug}.html`.

### 4. Completion report

```
Content optimization complete: content/optimized-{slug}.md
HTML export: content/export-{slug}.html

Source: content/[source filename]
Word count: [before] -> [after] (target: [target])
Keywords hitting target: [n]/[total] ([percentage]%)

The HTML file is ready for re-scoring in PageOptimizer.pro.
To iterate: re-score in PageOptimizer, export new briefs, and run Optimize mode again.
```

---

## Behavioral Rules

- NEVER skip a keyword silently. Every keyword from all 4 briefs must be surfaced and addressed.
- ALWAYS show the optimization plan before rewriting. Wait for operator approval.
- ALWAYS verify keyword counts after rewriting. Never save without a verified scorecard.
- Maintain brand voice throughout all rewrites.
- Integrate keywords naturally. No keyword stuffing. Restructure content if it reads awkwardly.
- Title and H1 should be near-identical (per PageOptimizer guidance).
- Subheading keywords work as a collective group, not individually per subheading.
- New content (sections, paragraphs, subsections) is encouraged to hit word count and keyword targets.
- On re-optimization runs, preserve content where keywords already hit targets. Focus on gaps.
- Do not rewrite the `meta_description` unless the operator explicitly requests it or a brief targets it.
- Do not use emojis in any output.
