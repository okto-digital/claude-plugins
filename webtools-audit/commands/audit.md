---
description: Audit content quality against SEO, readability, and brand voice standards
allowed-tools: Read, Write, Glob, Grep
argument-hint: [all | page-slug]
---

Evaluate generated content against SEO targets, readability standards, brand voice consistency, and heading structure. Produces D10: Content Audit Report.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: report "No project found. Run /webtools-init first." and stop.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

**Required inputs:**
- At least one D8 (Page Content) file in `content/`
  - If no D8 files exist: "No content documents found in content/. Create page content first using webtools-writer." Stop.

- D3: SEO Keyword Map at `seo/D3-seo-keyword-map.md`
  - If it does NOT exist: warn. "D3: SEO Keyword Map not found. SEO evaluation will be limited."
  - If it exists: load it silently.

**Optional inputs (load silently if present):**
- D12: SEO Content Targets at `seo/D12-seo-content-targets.md` -- specific keyword targets from external tool
- D2: Brand Voice Profile at `brand/D2-brand-voice-profile.md` -- for voice consistency checks
- D5: Competitor Analysis at `architecture/D5-competitor-analysis.md` -- for competitive benchmarking
- D4: Site Architecture at `architecture/D4-site-architecture.md` -- for internal linking checks
- D7: Page Blueprints in `blueprints/` -- for blueprint compliance checks

### 4. Output Preparation

Check if `audit/D10-content-audit-report.md` already exists. If yes, warn:

```
D10: Content Audit Report already exists (status: [status], updated: [date]).
Overwrite with a new audit, or cancel?
```

If the operator cancels, stop.

### 5. Status Report

```
Project: [client name]

Inputs loaded:
  D8 Content pages: [list files found]
  D3 SEO Keywords:  [loaded / not found]
  D12 SEO Targets:  [loaded / not found]
  D2 Brand Voice:   [loaded / not found]
  D4 Architecture:  [loaded / not found]
  D7 Blueprints:    [X files found]

Audit scope: [all / specific page]
Output: audit/D10-content-audit-report.md
```

---

## Validate Arguments

Parse the command argument:

- **`all`** (or no argument): Audit all D8 content documents found in `content/`.
- **`[page-slug]`**: Audit only `content/D8-content-{page-slug}.md`. If the file does not exist, report the error and list available D8 files.

---

## Audit Methodology

### Per-Page Audit

For each D8 document being audited, evaluate:

**1. SEO Analysis (if D3 or D12 available)**

- **Keyword coverage**: For each assigned keyword (from D3 page mapping), check if it appears in:
  - Title tag
  - Meta description
  - H1 heading
  - H2 headings
  - Body text
- **Keyword density**: Is each keyword used enough but not over-stuffed?
- **Missing keywords**: Keywords assigned but not used anywhere
- **Title tag assessment**: Length (50-60 characters), keyword placement, clarity
- **Meta description assessment**: Length (150-160 characters), keyword presence, call to action

Score: [Good / Needs Work / Poor] with specific findings.

**2. Heading Structure**

- Is there exactly one H1?
- Do H2s logically organize the content?
- Is the heading hierarchy correct (no skipping levels)?
- Do headings include relevant keywords where natural?

Score: [Good / Needs Work / Poor] with specific findings.

**3. Readability Analysis**

- **Average sentence length**: Flag sentences over 25 words
- **Paragraph length**: Flag paragraphs over 5 sentences
- **Vocabulary level**: Appropriate for target audience?
- **Passive voice**: Flag excessive passive constructions
- **Flesch-Kincaid approximation**: Estimate reading level

Score: [Good / Needs Work / Poor] with specific findings.

**4. Brand Voice Consistency (if D2 available)**

- Does the content match D2 tone spectrum positioning?
- Are D2 vocabulary preferences followed (words to use/avoid)?
- Is sentence style consistent with D2 guidelines?
- Are there sections that deviate from the established voice?

Score: [Good / Needs Work / Poor] with specific findings.

**5. Blueprint Compliance (if D7 available)**

- Does each section match the D7 blueprint structure?
- Are all required key messages present?
- Does word count match D7 targets (within 20%)?
- Are data requirements flagged appropriately?

Score: [Good / Needs Work / Poor] with specific findings.

**6. Internal Linking (if D4 available)**

- Are recommended internal links present?
- Are links contextually placed?
- Are there orphan references (links to pages that do not exist in D4)?

Score: [Good / Needs Work / Poor] with specific findings.

**7. Improvement Suggestions**

For each section of the page, provide specific, actionable improvement suggestions:
- What to change
- Why it matters
- Example of improved text (if applicable)

### Cross-Page Analysis (when auditing all)

When auditing all pages, also evaluate:

**Keyword cannibalization**: Are multiple pages targeting the same primary keyword?

**Content consistency**: Is messaging aligned across pages? Are value propositions consistent?

**Missing content**: Are there blueprinted sections that are inadequately filled or still have placeholder content?

**Coverage**: Do all pages from D4 have corresponding D8 content?

---

## Write D10

Write the audit report to `audit/D10-content-audit-report.md`.

### YAML Frontmatter

```yaml
---
document_id: D10
title: "Content Audit Report"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-audit
status: complete
dependencies:
  - D8: /content/D8-content-*.md
  - D3: /seo/D3-seo-keyword-map.md
---
```

Include D12, D2, D4, D5, D7 in dependencies if they were loaded and used.

### Report Structure

```markdown
# Content Audit Report: [Client Name]

## Audit Summary

Audit date: [today]
Pages audited: [count]
Audit scope: [all / specific page]

### Overall Scores

| Category | Score | Details |
|----------|-------|---------|
| SEO | [Good/Needs Work/Poor] | [brief summary] |
| Heading Structure | [Good/Needs Work/Poor] | [brief summary] |
| Readability | [Good/Needs Work/Poor] | [brief summary] |
| Brand Voice | [Good/Needs Work/Poor] | [brief summary] |
| Blueprint Compliance | [Good/Needs Work/Poor] | [brief summary] |
| Internal Linking | [Good/Needs Work/Poor] | [brief summary] |

## Per-Page Audit

### [Page Name] (D8-content-{slug}.md)

[Full audit results for each category]
[Improvement suggestions per section]

## Cross-Page Analysis

[Keyword cannibalization findings]
[Content consistency findings]
[Missing content findings]
[Coverage report]

## Priority Improvements

1. [Highest priority improvement with page and section]
2. [Second priority improvement]
3. [Third priority improvement]
...
```

---

## Lifecycle Completion

### 1. File Naming Validation

Verify the output file is named `D10-content-audit-report.md` and is located in `audit/`.

### 2. Registry Update

Update `project-registry.md`:
- Set D10 row: Status = `complete`, File Path = `audit/D10-content-audit-report.md`, Created = today, Updated = today, Created By = `webtools-audit`
- Phase Log: if Audit phase has no Started date, set Started to today and set Completed to today. Add `webtools-audit` to Plugins Used.

### 3. Cross-Reference Check

Skip. D10 is a single-instance document.

### 4. Downstream Notification

```
D10: Content Audit Report is complete.

Review the findings and iterate on D8 content as needed.
Re-run /audit after making changes to verify improvements.

If all scores are Good, the content phase is complete.
Run /webtools-health for a final project integrity check.
```
