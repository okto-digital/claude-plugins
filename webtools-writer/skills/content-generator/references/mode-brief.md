# Brief Mode

Standalone content generation from a content brief. Generates page content from operator-authored briefs with optional PageOptimizer keyword targets.

---

## Input Requirements

### Content Brief (required)

Check `content/` for files matching `content-brief-*.md`.

- If none exist: offer to create one. "No content briefs found. Create a content brief from the template? This will copy the template to `content/content-brief-{slug}.md` for you to fill in." Ask for the page slug, then copy `references/content-brief-template.md` to `content/content-brief-{slug}.md`.
- If briefs exist: list them and ask the operator which brief to generate content for.

### Brand Voice (optional)

Check `brand/D2-brand-voice-profile.md`.

- If it exists: load silently. Apply voice throughout generation.
- If it does NOT exist: proceed with neutral professional tone. No warning needed in brief mode -- operators may not have a D2 profile.

---

## Brief Parsing

Read the selected brief file and extract:

### Page Metadata

From YAML frontmatter: `page_name`, `slug`, `project`, `status`.

### Page Description

The content under `## Page Description`. This provides context for tone and purpose but is not output directly.

### Content Outline

Each `###` heading under `## Content Outline` becomes a section in the generated content. Parse:

- Section heading text
- Content under each heading (key messages, notes, points to cover)
- FAQ sections: parse `Q:` / `A:` pairs as individual FAQ items

### Keywords

From `## Keywords` subsections: primary, secondary, and variant keywords. These inform word choice but are not tracked with scorecards.

### PageOptimizer Briefs

From `## PageOptimizer Briefs` subsections. Each subsection may contain keyword lines in the format:

```
keyword phrase ( current_count / target_min - target_max )
```
or:
```
keyword phrase ( current_count / target_single )
```

**Parsing rules:**
1. Extract keyword: everything before the opening `(`, trimmed.
2. Extract current count: the number before the `/`.
3. Extract target: if format is `X / Y - Z`, targetMin = Y, targetMax = Z. If format is `X / Y` (no dash), targetMin = Y, targetMax = Y.
4. Skip non-keyword lines: empty lines, HTML comments, header text, and any line not matching the keyword pattern.

If all PageOptimizer sections are empty, generate without keyword targets.

### Additional Context

Raw content under `## Additional Context`. Incorporate relevant information naturally into appropriate sections per the rules in `references/generation-rules.md`.

---

## Status Report

Present before starting generation:

```
Project: [project name or "unspecified"]

Mode: Brief
Source: content/content-brief-[slug].md
Page: [page_name from frontmatter]
Brand voice: [loaded / not found]

Outline sections: [count]
PageOptimizer briefs: [loaded with N keywords / not provided]
Additional context: [present / empty]

Output: content/generated-[slug].md
```

---

## Keyword-Aware Generation

When PageOptimizer briefs are present:

- Use keyword targets as placement guidance during writing.
- Aim for natural inclusion within the target ranges.
- Do NOT produce a keyword scorecard -- that is the content-pageoptimizer skill's job.
- Report a brief keyword summary in the content statistics block (e.g., "Targeted N keywords from PageOptimizer briefs").

When no PageOptimizer briefs are provided:

- Generate content based on the outline and any keywords from the Keywords section.
- Note in statistics: "No PageOptimizer targets applied."

---

## Output Naming

```
content/generated-{slug}.md
```

The `{slug}` comes from the brief's YAML frontmatter `slug` field. See `references/output-format.md` for frontmatter schema.

---

## Downstream Notification

```
Content generated: content/generated-[slug].md
Source: content/content-brief-[slug].md
Word count: [count]

Next steps:
- Run content-pageoptimizer to optimize against PageOptimizer.pro scoring
- Run /export-html to convert to HTML for external tools
```
