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

Return the main content as clean markdown with:
- Heading hierarchy preserved (h1 through h6 as # through ######)
- Bold text as **bold**
- Italic text as *italic*
- Bulleted lists as - items
- Numbered lists as 1. items
- Links as [link text](URL "title") -- include the title attribute if present in the HTML
- Images as ![alt text](image-src "title") -- include both alt and title if present in the HTML
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

Inspect the extracted content for quality:

- Verify headings follow a logical hierarchy (one H1, H2s for sections, etc.)
- Check that links are properly formatted with URLs
- Check that images have alt text
- Remove any remaining navigation artifacts or repeated elements
- Remove any HTML tags that were not converted to markdown
- Fix any broken formatting (unclosed bold, misformatted lists)

### Step 2b: Fallback -- Browser Extraction

If WebFetch fails (403 Forbidden, timeout, empty content, or JS-rendered page), try browser-based extraction before giving up. Many sites block non-browser requests via Cloudflare, WAFs, or bot detection -- a real browser bypasses this.

**Check if browser tools are available** (e.g., `browser_navigate`, `browser_snapshot`). If they are:

1. Navigate to the URL using `browser_navigate`.
2. Wait for the page to fully load (use `browser_wait_for` if needed).
3. Take a snapshot using `browser_snapshot` to get the page content.
4. Extract the main content from the snapshot, applying the same rules as Step 1 (skip header, nav, sidebar, footer; preserve heading hierarchy, formatting, links, images).
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
Links found: [count]
Images found: [count]

---

[extracted markdown content]

---

Review this extraction:
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
