---
name: content-pageoptimizer
description: |
  Optimize existing page content using keyword targets from PageOptimizer.pro content brief exports. Parses 4 brief files (title, H1, subheadings, body), analyzes keyword gaps, rewrites content to hit targets while maintaining brand voice, and auto-exports to HTML.

  Invoke when the operator asks to "optimize content for SEO", "apply content brief", "run pageoptimizer", "rewrite content for keywords", "apply keyword targets", or needs to optimize page content against PageOptimizer.pro scoring.
allowed-tools: Read, Write, Edit, Glob, Bash(mkdir:*)
version: 1.0.0
---

Optimize existing page content to hit keyword targets from PageOptimizer.pro. Read the source content, parse 4 attached content brief files, apply brand voice, rewrite section by section, verify keyword counts, and auto-export to HTML.

---

## Lifecycle Startup

Before doing anything else, complete these 6 steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Source Content

Ask the operator which content file to optimize. List all `.md` files in `content/` that start with `extracted-` or `pageoptimized-`.

If a `pageoptimized-` version exists alongside an `extracted-` version for the same slug, ask:

```
Found existing optimized version: content/pageoptimized-{slug}.md

(a) Re-optimize -- use the pageoptimized version as source (iterating on previous work)
(b) Fresh start -- use the extracted version as source (discard previous optimization)
```

If only `extracted-` exists, use it as source.

### 4. Brief Files

The operator provides 4 content brief files exported from PageOptimizer.pro. These may be attached directly in the chat or saved to a location the operator specifies.

The 4 required files:
- `ContentBrief_title.txt` -- keyword targets for the `<title>` tag
- `ContentBrief_pageTitle.txt` -- keyword targets for the H1
- `ContentBrief_subHeadings.txt` -- keyword targets for H2-H6 collectively
- `ContentBrief_BodyContent.txt` -- keyword targets for body content

If the files are not yet visible in the conversation, ask the operator to attach them.

Parse each file following the format rules in `references/brief-parsing.md`.

### 5. Brand Voice

Read `brand/D2-brand-voice-profile.md`.

- If it exists: load silently. Use voice attributes, tone, vocabulary, and style throughout all rewrites.
- If it does NOT exist: warn the operator. "Brand voice profile not found. Content may lack voice consistency. Proceed anyway?"

### 6. Status Report

```
Project: [client name]

Source: content/[source filename] ([fresh / re-optimization])
Word count: [current] / [target from brief, if available]

Brief files:
  Title:       [n] keywords parsed
  Page Title:  [n] keywords parsed
  Subheadings: [n] keywords parsed
  Body Content: [n] keywords parsed

Brand voice: [loaded / not found]

Ready to optimize.
```

---

## Phase 1: Analyze

Split the source content into 4 zones:
- **Title**: `meta_title` from YAML frontmatter
- **H1**: the first `#` heading in the markdown body
- **Subheadings**: all `##` through `######` headings (text only)
- **Body**: everything else -- paragraphs, lists, blockquotes, table cells

For each zone, count current occurrences of every keyword from the corresponding brief file. Use the counting rules in `references/keyword-verification.md`.

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
- Maintain brand voice throughout (tone, terminology, style from D2 profile)
- Integrate keywords naturally. If content reads awkwardly, restructure rather than force keywords.

<critical>
Every keyword from ALL 4 briefs must be addressed. Do not silently skip any keyword. If a keyword is genuinely impossible to place naturally, flag it to the operator with an explanation and suggested alternatives.
</critical>

---

## Phase 4: Verify

Count every keyword in the rewritten content and generate a full scorecard. Follow the verification methodology in `references/keyword-verification.md`.

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

If any keywords still miss their target, list them with specific placement suggestions.

If the operator requests changes, iterate: adjust content, re-verify, show updated scorecard. Repeat until approved.

---

## Phase 5: Save and Export

### 1. Build output filename

Derive the slug from the source file:
- `extracted-{slug}.md` becomes `pageoptimized-{slug}.md`
- `pageoptimized-{slug}.md` stays `pageoptimized-{slug}.md` (overwrite)

### 2. Write the optimized markdown

Write to `content/pageoptimized-{slug}.md` with frontmatter:

```yaml
---
document_type: pageoptimized-content
title: "[optimized title]"
meta_title: "[optimized meta title]"
meta_description: "[optimized or preserved meta description]"
source_url: "[preserved from source file]"
final_url: "[preserved from source file]"
optimization_source: "[source .md filename]"
project: "[client name]"
optimized: [today]
created_by: webtools-writer
status: optimized
---
```

### 3. Auto-export to HTML

Convert the optimized markdown to clean semantic HTML following the rules in `references/html-export-rules.md`. Write to `content/pageoptimized-{slug}.html`.

### 4. Verify files

Read both output files back and confirm:
- `.md` file exists, has correct frontmatter, contains optimized content
- `.html` file exists, contains valid HTML tags, no markdown syntax remnants

---

## Lifecycle Completion

### 1. Registry Update

Update `project-registry.md`:
- Add or update a Document Log row: Doc ID = `--`, Document = `PageOptimized: [title]`, File Path = `content/pageoptimized-{slug}.md`, Status = `optimized`, Created = today (or original date if re-optimization), Updated = today, Created By = `webtools-writer`
- Add a row for the HTML export if not already present
- Phase Log: if Content phase has no Started date, set Started to today. Add `webtools-writer` to Plugins Used.

### 2. Downstream Notification

```
Content optimization complete: content/pageoptimized-{slug}.md
HTML export: content/pageoptimized-{slug}.html

Source: content/[source filename]
Word count: [before] -> [after] (target: [target])
Keywords hitting target: [n]/[total] ([percentage]%)

The HTML file is ready for re-scoring in PageOptimizer.pro.
To iterate: re-score in PageOptimizer, export new briefs, and run this skill again.
```

---

## Behavioral Rules

- NEVER skip a keyword silently. Every keyword from all 4 briefs must be surfaced and addressed.
- ALWAYS show the optimization plan before rewriting. Wait for operator approval.
- ALWAYS verify keyword counts after rewriting. Never save without a verified scorecard.
- Maintain brand voice from D2-brand-voice-profile.md throughout all rewrites.
- Integrate keywords naturally. No keyword stuffing. Restructure content if it reads awkwardly.
- Title and H1 should be near-identical (per PageOptimizer guidance).
- Subheading keywords work as a collective group, not individually per subheading.
- New content (sections, paragraphs, subsections) is encouraged to hit word count and keyword targets.
- On re-optimization runs, preserve content where keywords already hit targets. Focus on gaps.
- Do not rewrite the `meta_description` unless the operator explicitly requests it or a brief targets it.
- Do not use emojis in any output.

---

## Reference Files

- `references/brief-parsing.md` -- PageOptimizer brief file format, parsing rules, examples
- `references/keyword-verification.md` -- Keyword counting methodology, case sensitivity, scorecard format
- `references/html-export-rules.md` -- Markdown-to-HTML conversion rules for the auto-export step
