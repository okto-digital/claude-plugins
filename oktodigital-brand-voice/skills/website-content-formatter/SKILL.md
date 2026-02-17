---
name: website-content-formatter
description: "Content formatting optimization for dual audiences (human scanners + search bots) including headline hierarchy, progressive disclosure, TLDR summaries, Featured Snippets, and visual structure. Use when formatting content for scanners, optimizing headline hierarchy, creating TLDR summaries, or targeting Featured Snippets."
allowed-tools: Read
version: 1.0.0
---

# Website Content Formatter

**Purpose:** Content formatting optimization for dual audiences (human scanners + search bots)

**For comprehensive formatting guidelines, see:** `${CLAUDE_PLUGIN_ROOT}/skills/website-content-formatter/resources/formatting-best-practices.md`

---

## Skill Overview

This skill provides content formatting recommendations that serve both user experience (scannability, readability) and SEO (search bot understanding, Featured Snippet eligibility).

**What this skill does:**
- Optimize headline hierarchy (H1/H2/H3 structure)
- Create TLDR/executive summaries
- Recommend progressive disclosure (accordions, tabs, collapsible sections)
- Format content for Featured Snippets (paragraph, list, table formats)
- Design table of contents for long content
- Apply F-pattern and Z-pattern formatting
- Optimize white space and visual hierarchy

**What this skill does NOT do:**
- Write content (only formats existing content)
- Handle SEO metadata (use website-seo-metadata)
- Make architecture decisions (use website-content-architect)
- Optimize CTAs or conversion elements (use website-conversion-optimizer)
- Select UX component patterns (use website-ux-component-matcher)

---

## Integration with Website Skills Workflow

1. **website-ux-component-matcher** -- Select WHAT component patterns to use
2. **website-content-architect** -- Determine page structure
3. **website-content-formatter** (THIS SKILL) -- Apply formatting within selected components
4. **website-seo-metadata** -- Generate technical SEO metadata
5. **website-conversion-optimizer** -- Optimize for conversions

---

## Core Formatting Rules

### 1. Headline Hierarchy

**H1:** ONE per page (from frontmatter `title` field). Never use H1 in Markdown body.

**H2:** 5-10 per page. Every major topic section. Include primary keyword in first H2. Never skip levels (H1 -> H2, not H1 -> H3).

**H3:** Nested under H2 only. 2-5 per H2 section.

**H4-H6:** Avoid deeper than H4.

**Heading length:** 6 words ideal, 8 max, 40 chars for mobile.

**Keyword integration:** Primary keyword in first H2, secondary keywords in subsequent H2s, natural placement.

### 2. TLDR Summary

**Placement:** After introduction, before main content.

**Structure:** 3-5 bullet points, 100-200 total words, 15-30 words per bullet. Include primary and secondary keywords. Answer "What will I learn/get?"

**Alternative names by audience:** "Key Takeaways" (broadest appeal), "TLDR" (tech-savvy), "Executive Summary" (B2B), "At a Glance" (visual).

**Featured Snippet optimization:** Use bulleted/numbered lists, concise bullets, front-load with answer/benefit, target keyword in first bullet.

### 3. Progressive Disclosure

**Critical Rule:** Content MUST exist in HTML DOM even when hidden. CSS-only hiding is SEO-safe; JavaScript-only rendering is NOT.

**SEO-Safe methods:**
- **Accordions** -- FAQ sections, technical specs, supplementary info. Use `<details>`/`<summary>`.
- **Tabs** -- Related content by category. All tab content must be in DOM.
- **Expandable sections** -- Long quotes, optional deep-dives. CSS-hidden, not JS-loaded.
- **FAQ Schema + collapsible** -- Official Google recommendation. Eligible for rich snippets.

**MUST stay visible:** Primary value proposition, main content, first 2-3 paragraphs, H2/H3 headlines, primary CTAs.
**CAN be hidden:** FAQ answers, technical specs, long code examples, supplementary explanations.

### 4. Featured Snippet Optimization

**Paragraph snippets (40-60 words):** Answer question in first paragraph below H2. Be concise and direct.

**List snippets (3-10 items):** Bulleted or numbered. Start with action verb for numbered lists. Bold key terms.

**Table snippets:** Clear column headers, 2-5 columns, 3-10 rows, concise cells.

**Placement:** Early in article (first 2-3 sections), immediately after H2 question, within first 500 words.

### 5. Table of Contents

**Include when:** Content >1,500 words, 6+ H2 sections, complex/technical topics, comprehensive guides.
**Skip when:** Content <1,000 words, <5 sections, linear narrative.
**Structure:** H2 headings only (H3 optional for 3,000+ words). Collapsible on mobile.

### 6. Text Structure

**Paragraphs:** 2-3 sentences, 40-60 words. Single-sentence paragraphs for emphasis (use sparingly).

**Scanning patterns:**
- **F-pattern** (most pages): Front-load key information in first sentence of each paragraph.
- **Z-pattern** (landing pages): Place key info at diagonal scanning points.

### 7. Visual Hierarchy

**Spacing:** 50-60px between H2 sections, 30-40px between H3, 15-20px between paragraphs. Increase 20-30% on mobile.

**Size:** H1 32-40px, H2 28-32px, H3 22-26px, Body 16-18px.

**Weight:** H1/H2 Bold (700), H3/H4 Semi-bold (600), Body Regular (400).

---

## Formatting Checklists by Content Type

### Blog Post
- [ ] One H1 (from frontmatter)
- [ ] 5-10 H2 sections with primary keyword in first H2
- [ ] TLDR after introduction (3-5 bullets)
- [ ] Paragraphs: 2-3 sentences
- [ ] TOC (if >1,500 words)
- [ ] Featured Snippet optimization (first H2)
- [ ] FAQ section (if applicable, with schema)
- [ ] Proper heading hierarchy (no skipped levels)

### Service Page
- [ ] Value proposition in first 100 words
- [ ] 5-8 H2 sections
- [ ] TLDR or "At a Glance" summary
- [ ] Bullets for features/benefits
- [ ] FAQ section with accordion (+ schema)
- [ ] Progressive disclosure for technical specs

### Landing Page
- [ ] Minimal H2s (3-5 sections)
- [ ] Large, bold headlines
- [ ] Short paragraphs (1-2 sentences)
- [ ] Bullet lists for benefits
- [ ] No TOC (single-page flow)
- [ ] Z-pattern layout, ample white space

---

## Output Format

```yaml
# CONTENT FORMATTING RECOMMENDATIONS

## Headline Structure
headlineHierarchy:
  h1: "[Page title from frontmatter]"
  h2Count: [number]
  h2Headings:
    - "[H2 heading with keyword]"
  issues: [list any heading hierarchy problems]

## TLDR Summary
tldr:
  placement: "After introduction"
  format: "bulleted-list"
  bulletPoints:
    - "[Key takeaway 1]"
  wordCount: [count]

## Progressive Disclosure
progressiveDisclosure:
  recommended:
    - section: "FAQ"
      method: "accordion"
      schema: "FAQ schema"

## Featured Snippet Optimization
featuredSnippet:
  targetQuestion: "[Question in H2]"
  format: "paragraph" | "list" | "table"
  optimizedAnswer: "[40-60 word answer]"

## Quality Checks
- [ ] No H1 in content body
- [ ] Heading levels don't skip
- [ ] 5-10 H2s present
- [ ] TLDR included (if >1,000 words)
- [ ] Paragraphs <= 3 sentences
```

---

## Reference Files

- `resources/formatting-best-practices.md` -- Google's official position on hidden content, heading hierarchy research data, accessibility impact, detailed examples

---

**Version:** 1.0.0
