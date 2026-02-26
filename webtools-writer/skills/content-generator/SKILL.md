---
name: content-generator
description: "Generate page content from a D7 blueprint or a content brief. Fills blueprints with draft content following brand voice and optional SEO/PageOptimizer keyword targets. Works one page at a time."
allowed-tools: Read, Write, Edit, Glob, Bash(mkdir:*)
version: 2.0.0
---

Generate page content for the webtools website pipeline. Detect the available source (D7 blueprint or content brief), load the outline and brand voice, generate content section by section, and save the output.

---

## Lifecycle Startup

Before doing anything else, complete these steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Mode Detection

Scan for available source types:
- Check `blueprints/` for D7 files (blueprint mode)
- Check `content/` for `content-brief-*.md` files (brief mode)

**If both found:** Ask the operator which mode to use -- blueprint or brief. List available files for each.

**If only blueprints found:** Enter blueprint mode. Follow `references/mode-blueprint.md` for input loading, content mode selection, and outline extraction.

**If only briefs found:** Enter brief mode. Follow `references/mode-brief.md` for brief parsing and outline extraction.

**If neither found:** Offer to create a content brief from the template. Ask for the page slug, then copy `references/content-brief-template.md` to `content/content-brief-{slug}.md`. Inform the operator to fill it in and re-run the skill.

### 4. Brand Voice

Load `brand/D2-brand-voice-profile.md` if present. Handling differs by mode -- see the active mode reference file for details.

### 5. Status Report

Present the mode-specific status report as defined in the active mode reference file. Wait for the operator to confirm before proceeding.

---

## Content Generation Process

### Step 1: Load Outline

Extract the content outline from the mode-specific source:
- **Blueprint mode:** Extract sections, requirements, and word count targets from D7. See `references/mode-blueprint.md`.
- **Brief mode:** Parse sections, FAQ items, keywords, and additional context from the brief. See `references/mode-brief.md`.

### Step 2: Generate Section by Section

For each section in the source outline order, generate content following the rules in `references/generation-rules.md`:

- Apply brand voice (D2 if loaded, neutral professional if not)
- Include section heading, body content, CTA text, alt text suggestions, and designer/developer notes as applicable
- Flag sections needing real client input with `[NEEDS CLIENT INPUT]` markers
- Incorporate raw content or additional context naturally
- Integrate keywords when targets are available (guidance, not scoring)

### Step 3: Present Draft

Present the complete page content to the operator with content statistics: total word count, flagged sections, and keyword summary.

### Step 4: Review and Iterate

Ask the operator:
- Does the tone match the brand voice?
- Are there sections that need more or less detail?
- Any specific messaging to adjust?
- Should any placeholder content be replaced with real client content?

Iterate until the operator approves.

---

## Save and Lifecycle Completion

### 1. Write Output

Write the approved content following the file naming and frontmatter rules in `references/output-format.md`:
- **Blueprint mode:** `content/D8-content-{page-slug}.md`
- **Brief mode:** `content/generated-{slug}.md`

Check for existing files before writing. Warn and ask before overwriting.

### 2. Registry Update

Update `project-registry.md`:
- Add or update a Document Log row for this page with appropriate status and metadata.
- Phase Log: if Content phase has no Started date, set Started to today. Add `webtools-writer` to Plugins Used.

### 3. Mode-Specific Completion

Follow the active mode reference file for additional completion steps:
- **Blueprint mode:** Cross-reference check and downstream notification per `references/mode-blueprint.md`.
- **Brief mode:** Downstream notification per `references/mode-brief.md`.

---

## Behavioral Rules

- Follow the source outline exactly. Do not add, remove, or reorder sections.
- Follow the brand voice consistently. If D2 is loaded, apply its guidelines throughout.
- Flag all sections needing real client input. Do not invent testimonials, statistics, names, or case study details.
- Track word count per section and total. Flag significant deviations from targets.
- Do not use emojis in any output.
- Full writing rules: `references/generation-rules.md`.

---

## Reference Files

- `references/mode-blueprint.md` -- D-pipeline mode: D7 input validation, D8 naming, cross-references, SEO mode selection
- `references/mode-brief.md` -- Brief mode: template parsing, keyword extraction, outline interpretation, output naming
- `references/content-brief-template.md` -- Template for operators to fill in with page description, outline, keywords, and briefs
- `references/output-format.md` -- Shared output structure and mode-specific frontmatter schemas
- `references/generation-rules.md` -- Shared writing rules: voice, flagging, keyword integration, formatting
