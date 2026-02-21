# Blueprint Mode

D-pipeline content generation mode. Generates page content from a completed D7 blueprint.

---

## Input Requirements

### D7: Page Blueprint (required)

Check `blueprints/` for D7 files.

- If no D7 files exist: "No blueprints found. Create page blueprints first using webtools-blueprint."
- If D7 files exist: list them and ask the operator which page to write content for.

### D2: Brand Voice Profile (required)

Check `brand/D2-brand-voice-profile.md`.

- If it exists: load silently. Use voice attributes, tone spectrum, vocabulary guide, and style guidelines throughout content generation.
- If it does NOT exist: warn. "D2: Brand Voice Profile is not available. Content will lack voice consistency. Recommend creating D2 first using webtools-brand. Proceed anyway?"

### Optional Inputs (load silently if present)

- **D3: SEO Keyword Map** at `seo/D3-seo-keyword-map.md` -- keyword targets for the page
- **D12: SEO Content Targets** at `seo/D12-seo-content-targets.md` -- specific keyword targets from external SEO tool
- **D6: Content Inventory** at `architecture/D6-content-inventory.md` -- existing content to incorporate (redesigns)
- **Client-provided raw content** (provided in conversation)

---

## Content Mode Selection

After loading inputs, ask the operator to choose a content mode:

- **SEO-optimized**: Integrate keywords from D3/D12 naturally throughout the content. Track keyword usage and placement.
- **Clean**: Write content without SEO considerations. Keywords can be added later in a revision pass.

If D3 and D12 are both unavailable, default to clean mode and note the limitation.

---

## Outline Extraction

Read the selected D7 blueprint. For each section, extract:

- Section type and purpose
- Content requirements and key messages
- Keyword assignments (if D3/D12 available and SEO mode selected)
- Tone guidance (if D2 available)
- Word count target
- Data requirements (what needs real client input)

---

## Status Report

Present before starting generation:

```
Project: [client name]

Mode: Blueprint
Writing content for: [page name] ([slug])
Blueprint: blueprints/D7-blueprint-[slug].md
Brand voice: [loaded / not found]
SEO keywords: [loaded / not found]
Content inventory: [loaded / not found]

Content mode options:
(a) SEO-optimized -- integrate keywords from D3/D12
(b) Clean -- no SEO integration (keywords added later)

Output: content/D8-content-[slug].md
```

---

## Output Naming

```
content/D8-content-{page-slug}.md
```

The `{page-slug}` must match the slug from D4 and the corresponding D7 exactly. See `references/output-format.md` for frontmatter schema.

---

## Lifecycle Completion Extras

### Cross-Reference Check

After saving, compare D8 files in `content/` against D7 files in `blueprints/`:

```
Content coverage: [X] of [Y] blueprinted pages have content.
Remaining: [list of pages still needing content]
```

### Downstream Notification

```
D8: Content for [page name] is complete.

Run this skill again for the next page, or:
- Run microcopy-generator when all page content is done
- Run /audit (webtools-audit) to check content quality
```
