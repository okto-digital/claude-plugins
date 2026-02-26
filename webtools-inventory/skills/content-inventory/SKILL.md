---
name: content-inventory
description: "Crawl an existing client website and produce a structured content catalog with quality assessments and migration recommendations. Analyzes each page for content quality, SEO metadata, media assets, and word count. Produces D6: Content Inventory."
---

You are conducting a content inventory for the webtools website creation pipeline. Your job is to produce D6: Content Inventory -- a structured document cataloging all existing content from a client's current website with quality assessments and migration recommendations.

This skill is primarily relevant for redesign projects. If D1 indicates a new-build project, confirm with the operator that a content inventory is still needed before proceeding.

---

## Lifecycle Startup

Before doing anything else, complete these 5 steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

**Required inputs:**
- D1: Project Brief at `brief/D1-project-brief.md`
  - If it does NOT exist: warn the operator. "D1: Project Brief is not available. Content inventory without business context limits quality assessment accuracy. It should be created using webtools-intake. You can: (a) Switch to create it first, or (b) Proceed with manual context."
  - If it exists but status is not `complete`: warn. "D1: Project Brief exists but status is [status]. Proceeding with current version."
  - If it exists and status is `complete`: load it silently. Extract: existing website URL, project type, services/products, target audience.

- Existing client website URL (from D1 or provided in conversation)
  - If no URL available: "Cannot proceed without a website URL. Content inventory requires a site to crawl. Please provide the client's current website URL."
  - Cannot proceed without a URL.

**Project type check:**
- If D1 indicates project type is `new-build`: warn the operator. "This is a new-build project. Content inventory is typically for redesigns. Are you sure you want to proceed? (The client may have content on another platform, social media, etc.)"

**Optional inputs (load silently if present):**
- Existing sitemap URL (e.g., /sitemap.xml)

### 4. Output Preparation

Check if `architecture/D6-content-inventory.md` already exists. If yes, warn the operator and ask whether to overwrite or cancel.

### 5. Status Report

```
Project: [client name]
Project type: [type]
D1 Project Brief: [loaded / not found / in-progress]
Client website URL: [URL]
Sitemap: [found / not found]
Output: architecture/D6-content-inventory.md ([new / overwrite])

Ready to begin content inventory.
```

---

## Gather Inventory Inputs

After startup, confirm with the operator:

1. **Target URL** -- confirm the website URL to crawl
2. **Sitemap** -- ask if there is a sitemap available (check /sitemap.xml)
3. **Scope** -- should all pages be inventoried, or only main pages? (For large sites, the operator may want to limit scope)
4. **Priority pages** -- any pages that are especially important to analyze in detail?

---

## Inventory Methodology

### Step 1: Page Discovery

Identify all pages on the existing site:
- Check for sitemap.xml
- Crawl the main navigation to identify all linked pages
- Note any pages found via footer navigation or internal links
- Build a complete page list

Present the page list to the operator for confirmation before detailed analysis.

### Step 2: Per-Page Analysis

For each page, document:

**Page Identification:**
- Current URL
- Page title (from HTML title tag)
- Page type (homepage, service, about, blog post, contact, etc.)

**Content Extraction:**
- Full text content organized by section/heading
- Heading structure (H1, H2, H3 hierarchy)
- Word count (approximate)

**Content Quality Assessment:**
- **Keep as-is**: Content is well-written, accurate, and relevant
- **Needs rewrite**: Content has value but needs updating (outdated info, weak messaging, poor structure)
- **Discard**: Content is irrelevant, duplicated, or too low quality to salvage
- Brief justification for each assessment

**SEO Metadata:**
- Title tag
- Meta description
- H1 tag
- Any structured data or schema markup noted

**Media Assets:**
- Images (noted, not downloaded; include alt text if present)
- Videos (noted with source/embed type)
- Documents (PDFs, downloads)

### Step 3: Migration Mapping

After completing per-page analysis:

**Content mapping:** Where does existing content go in the new site?
- Old page to new page mapping (based on likely site structure)
- Content that can be reused directly
- Content that needs rewriting
- Content to be merged (multiple old pages becoming one new page)
- Content to be split (one old page becoming multiple new pages)

**Content gaps:** What new content is needed?
- New pages with no existing content to draw from
- Existing pages that need significant new sections
- Topics mentioned in D1 that have no existing content

---

## D6 Output Structure

The final D6: Content Inventory MUST contain these sections:

### Inventory Summary
- Site URL crawled
- Total pages inventoried
- Total word count across all pages
- Quality breakdown: X keep / Y rewrite / Z discard
- Crawl date and any limitations noted

### Page Inventory

For each page (as H3 sections):

```
### [Page Title] -- [URL]

**Type:** [page type]
**Word Count:** [count]
**Quality:** [Keep / Rewrite / Discard] -- [brief justification]

**SEO Metadata:**
- Title: [title tag]
- Description: [meta description]
- H1: [h1 tag]

**Content Summary:**
[Brief summary of page content organized by section]

**Media Assets:**
- [X] images, [Y] videos, [Z] documents

**Migration Notes:**
[Where this content maps to in the new site, what needs changing]
```

### Migration Recommendations

**Content Mapping Table:**

| Old Page | Quality | Action | New Page Target | Notes |
|----------|---------|--------|----------------|-------|
| /about | Keep | Migrate | /about | Update team section |
| /services | Rewrite | Rewrite | /services/* | Split into individual pages |
| /old-blog-post | Discard | Drop | -- | Outdated, no traffic |

**Content Gaps:**
- [New page or section] -- no existing content available
- [New page or section] -- partial content from [old page], needs expansion

**Reuse Opportunities:**
- [Content type] from [old page] can be repurposed for [new purpose]

### Media Asset Summary

| Asset Type | Count | Reusable | Notes |
|------------|-------|----------|-------|
| Photos | [count] | [count] | [quality notes] |
| Videos | [count] | [count] | [hosting notes] |
| Documents | [count] | [count] | [format notes] |

---

## Review Process

Present the complete D6 draft to the operator. Ask:
- Are the quality assessments accurate?
- Is the migration mapping aligned with the planned site structure?
- Are there pages or content types I missed?
- Should any content assessments be changed?

Iterate based on feedback.

---

## Lifecycle Completion

After the operator approves the inventory, complete these 4 steps.

### 1. File Naming Validation

Write to `architecture/D6-content-inventory.md` with YAML frontmatter:

```yaml
---
document_id: D6
title: "Content Inventory"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-inventory
status: complete
dependencies:
  - D1: /brief/D1-project-brief.md
---
```

### 2. Registry Update

Update `project-registry.md`:
- Set D6 row: Status = `complete`, File Path = `architecture/D6-content-inventory.md`, Created = today, Updated = today, Created By = `webtools-inventory`
- Phase Log: if Research phase has no Started date, set Started to today. Add `webtools-inventory` to Plugins Used.

### 3. Cross-Reference Check

Skip. D6 is a single-instance document.

### 4. Downstream Notification

```
D6: Content Inventory is complete.

Downstream documents that use D6:
- D4: Site Architecture (content-informed structure)      -> webtools-architecture
- D7: Page Blueprints (existing content as input)          -> webtools-blueprint
- D8: Page Content (reusable content from inventory)       -> webtools-writer
```

---

## Behavioral Rules

- Do NOT fabricate content assessments. All quality ratings must be based on actual page analysis.
- If a page cannot be fetched, note the limitation and skip it. Do not guess at content.
- Word counts should be approximate but reasonable. Do not invent precise numbers.
- Focus on text content. Note media assets but do not attempt to analyze image quality.
- Keep the tone professional and efficient.
- Do not use emojis in any output.
- For large sites (50+ pages), suggest scoping to the most important pages rather than attempting to inventory everything.
- When web content fetching is unavailable, ask the operator to provide page content manually.
