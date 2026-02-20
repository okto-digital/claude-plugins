---
name: content-extractor
description: |
  Extract content from a live web page and save it as a well-formatted markdown file. Fetches the page, strips navigation/header/sidebar/footer, and preserves the main content with heading hierarchy, text formatting, links, and images.

  Invoke when the operator asks to "extract page content", "pull content from a URL", "get content from a live page", "scrape page content", or needs to capture existing web page content for revision.
allowed-tools: WebFetch, Read, Write, Edit, Bash, Glob
version: 1.0.0
---

Extract content from a web page or a URL and save it as a clean, well-formatted markdown file in the `content/` directory. The extracted file preserves heading hierarchy, text formatting, links, and images -- but strips site chrome (header, navigation, sidebar, footer).

---

## Lifecycle Startup

Before doing anything else, complete these 4 steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. URL Input

Ask the operator for the URL of the page to extract.

Validate the URL:
- Must start with `http://` or `https://`
- Must be a full page URL (not a PDF, image, or file download)

Check if an extracted file for this URL already exists in `content/` (match by URL slug). If yes, warn and ask whether to overwrite or cancel.

### 4. Status Report

```
Project: [client name]

Extracting content from: [URL]
Output: content/extracted-[slug].md ([new / overwrite])
Extraction method: WebFetch (browser fallback: [available / not available])

Ready to extract.
```

To determine browser fallback availability, check if browser tools (e.g., `browser_navigate`) are accessible in the current session. Report "available" or "not available" accordingly.

---

## Extraction Process

### Step 1: Fetch the Page

Use WebFetch to retrieve the page content. Use the prompt:

```
Extract ONLY the main content area of this page. Skip completely:
- Site header and top navigation bar
- Sidebars (left or right)
- Footer and bottom navigation
- Cookie banners and popups
- Breadcrumbs

IMPORTANT: Include content from ALL expandable/collapsible elements -- FAQs, accordions,
toggles, "read more" sections, tabbed content panels, and any <details>/<summary> elements.
Treat collapsed content as if it were fully expanded. Extract the full text from every
collapsible item, not just the visible summary/heading.

CRITICAL -- YOU MUST preserve these elements. Do NOT strip them out or simplify them:

1. LINKS: Every hyperlink MUST be preserved as [link text](URL "title").
   Keep the full href URL. Include the title attribute in quotes if present.
   Do NOT convert links to plain text. Do NOT omit URLs.

2. IMAGES: Every image MUST be preserved as ![alt text](image-src "title").
   Keep the full src URL. Include alt text AND title attribute if present.
   Do NOT skip images. Do NOT omit alt/title descriptions.

3. TEXT FORMATTING: Bold (**text**), italic (*text*), and all inline
   formatting MUST be preserved exactly.

Return the main content as clean markdown with:
- Heading hierarchy preserved (h1 through h6 as # through ######)
- Bold text as **bold**
- Italic text as *italic*
- Bulleted lists as - items
- Numbered lists as 1. items
- Links as [link text](URL "title") -- MUST include full URL and title if present
- Images as ![alt text](image-src "title") -- MUST include src, alt, and title
- Block quotes as > text
- Tables preserved in markdown table format if present
- Horizontal rules as ---

Do NOT include:
- Navigation menus
- Header/footer content
- Sidebar widgets
- Social media share buttons
- "Related posts" or "You might also like" sections
- Comment sections
- Ad blocks

Also extract from the HTML <head>:
- The <title> tag content (meta title)
- The <meta name="description" content="..."> value (meta description)

Return these two values at the very top, clearly labeled, followed by the extracted markdown content:
META_TITLE: [title tag content]
META_DESCRIPTION: [meta description content]
---
[extracted markdown content]
```

### Step 2: Review Raw Extraction

Inspect the extracted content for quality. **This step is mandatory -- do not skip any check.**

- Verify headings follow a logical hierarchy (one H1, H2s for sections, etc.)
- **LINKS CHECK (critical):** Verify every link has a full URL, not just anchor text. If any links were converted to plain text, re-extract them. Count the links found.
- **IMAGES CHECK (critical):** Verify every image has the src URL and alt text. If images were omitted or reduced to text descriptions, re-extract them. Count the images found.
- **FORMATTING CHECK:** Verify bold, italic, and other inline formatting is preserved. If text appears flattened (no bold/italic), re-extract.
- Remove any remaining navigation artifacts or repeated elements
- Remove any HTML tags that were not converted to markdown
- Fix any broken formatting (unclosed bold, misformatted lists)
- **Check for missing collapsed content:** Look for signs of FAQs, accordions, or expandable sections on the page (e.g., FAQ headings with no answers, numbered items with only titles). If collapsed content appears to be missing, flag it and attempt re-extraction with browser tools if available.

### Step 2b: Fallback -- Browser Extraction

If WebFetch fails (403 Forbidden, timeout, empty content, or JS-rendered page), try browser-based extraction before giving up. Many sites block non-browser requests via Cloudflare, WAFs, or bot detection -- a real browser bypasses this.

**Check if browser tools are available** (e.g., `browser_navigate`, `browser_snapshot`). If they are:

1. Navigate to the URL using `browser_navigate`.
2. Wait for the page to fully load (use `browser_wait_for` if needed).
3. **Expand all collapsible content** before extracting. Use `browser_evaluate` to open every collapsed element:
   ```javascript
   () => {
     // Expand <details> elements
     document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
     // Click accordion triggers (common patterns)
     document.querySelectorAll(
       '[aria-expanded="false"], .accordion-trigger, .faq-question, ' +
       '.collapse-toggle, [data-toggle="collapse"], .expandable:not(.expanded)'
     ).forEach(el => el.click());
     // Expand "read more" buttons
     document.querySelectorAll(
       '.read-more, .show-more, [data-action="expand"], .truncated-toggle'
     ).forEach(el => el.click());
     // Open all tabs to capture tabbed content
     document.querySelectorAll('.tab-trigger, [role="tab"]').forEach(el => el.click());
     return 'expanded';
   }
   ```
   Wait 1-2 seconds after expanding for content to render (`browser_wait_for` with time).
4. Take a snapshot using `browser_snapshot` to get the full page content.
5. Extract the main content from the snapshot, applying the same rules as Step 1 (skip header, nav, sidebar, footer; preserve heading hierarchy, formatting, links, images).
5. Extract meta title and meta description using `browser_evaluate`:
   ```javascript
   () => {
     const title = document.querySelector('title')?.textContent || '';
     const desc = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
     return { meta_title: title, meta_description: desc };
   }
   ```
6. Proceed to Step 3 with the browser-extracted content.

**If browser tools are NOT available**, inform the operator:

```
WebFetch was blocked (likely bot protection: Cloudflare, WAF, or similar).
Browser tools are not available in this session to bypass the restriction.

Options:
(a) Paste the page content directly -- I will format it as markdown
(b) Try a different URL
(c) Cancel

Tip: In a Cowork session with browser MCP enabled, the extraction
can load pages like a real browser and bypass bot protection.
```

### Step 3: Present Extracted Content

Present the cleaned content to the operator:

```
EXTRACTED CONTENT: [page title or URL]

Source: [URL]
Meta title: [extracted meta title, or "not found"]
Meta description: [extracted meta description, or "not found"]
Word count: [count]
Headings found: [count] (H1: [n], H2: [n], H3: [n], ...)
Links preserved: [count] (all with full URLs)
Images preserved: [count] (all with alt text)
Formatting: bold [count], italic [count]

---

[extracted markdown content]

---

Review this extraction:
- Are ALL links present with full URLs? (not converted to plain text)
- Are ALL images present with alt text and src URLs?
- Is bold/italic formatting preserved throughout?
- Is the main content complete? (nothing missing?)
- Was any unwanted content included? (nav, footer, sidebar?)
- Are there formatting issues to fix?
```

Iterate until the operator approves.

---

## File Naming

Convert the URL to a filename slug:

1. Remove the protocol (`https://`, `http://`)
2. Remove trailing slashes
3. Replace `.` in the domain with `-` (e.g., `oktodigital.com` becomes `oktodigital-com`)
4. Replace `/` path separators with `_`
5. If the path is empty (homepage), use `home`

Examples:
- `https://oktodigital.com/services/web-design` --> `extracted-oktodigital-com_services_web-design.md`
- `https://oktodigital.com/about` --> `extracted-oktodigital-com_about.md`
- `https://oktodigital.com/` --> `extracted-oktodigital-com_home.md`
- `https://example.co.uk/work/case-study-1` --> `extracted-example-co-uk_work_case-study-1.md`

Remove query parameters and fragments from the URL before slugifying.

---

## Output Format

Write to `content/extracted-{slug}.md` with YAML frontmatter:

```yaml
---
document_type: extracted-content
title: "[page title or H1 from content]"
meta_title: "[extracted meta title, or empty string if not found]"
meta_description: "[extracted meta description, or empty string if not found]"
source_url: "[original URL]"
project: "[client name]"
extracted: [today]
created_by: webtools-writer
status: extracted
---
```

Then the extracted markdown content exactly as approved by the operator.

---

## Lifecycle Completion

After the operator approves the extraction, complete these 3 steps.

### 1. Save File

Write the file to `content/extracted-{slug}.md` with frontmatter and approved content.

### 2. Registry Update

Update `project-registry.md`:
- Add a row to the Document Log: Doc ID = `--`, Document = `Extracted: [page title]`, File Path = `content/extracted-{slug}.md`, Status = `extracted`, Created = today, Updated = today, Created By = `webtools-writer`
- Phase Log: if Content phase has no Started date, set Started to today. Add `webtools-writer` to Plugins Used.

### 3. Downstream Notification

```
Extracted content saved: content/extracted-[slug].md
Source: [URL]
Word count: [count]

Next steps:
- Edit the extracted file directly for content revisions
- Run content-generator to create new content from a blueprint
- Run /audit (webtools-audit) to check content quality
```

---

## Behavioral Rules

- Extract ONLY main page content. Never include headers, footers, sidebars, or navigation.
- Preserve the original heading hierarchy. Do not flatten or restructure headings.
- Preserve all links with their URLs. Use `[text](url "title")` format when title attributes exist.
- Preserve all images as `![alt](src "title")`. Include alt and title when available in the HTML.
- Do not rewrite, edit, or improve the extracted content. Capture it as-is.
- Do not use emojis in any output.
- If content cannot be extracted cleanly, offer the paste-in fallback. Do not guess or fabricate content.
- File slugs must be deterministic -- the same URL always produces the same filename.
- Remove query parameters (`?`) and fragments (`#`) from URLs before creating the slug.
