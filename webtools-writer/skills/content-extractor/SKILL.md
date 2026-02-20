---
name: content-extractor
description: |
  Extract content from a live web page and save it as a well-formatted markdown file. Fetches the page, strips navigation/header/sidebar/footer, and preserves the main content with heading hierarchy, text formatting, links, and images.

  Invoke when the operator asks to "extract page content", "pull content from a URL", "get content from a live page", "scrape page content", or needs to capture existing web page content for revision.
allowed-tools: Bash, WebFetch, Read, Write, Edit, Glob
version: 1.1.0
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

Extraction methods available:
  1. curl + local processing  [available / not available]
  2. WebFetch                 [always available]
  3. Browser (MCP)            [available / not available]
  4. Paste-in                 [always available]

Ready to extract.
```

Check availability: run `which curl` via Bash for method 1. Check if browser tools (e.g., `browser_navigate`) are accessible for method 3.

---

## Redirect Detection (applies to ALL methods)

<critical>
ALWAYS verify the final URL after fetching. URLs frequently redirect silently (e.g., /services/website-development/ redirects to /services/). If the final URL differs from the requested URL, STOP and warn the operator BEFORE processing content:

```
REDIRECT DETECTED

Requested URL: [original URL]
Redirected to: [final URL]

The server redirected this URL. The content at the final URL may be
a different page than intended (e.g., a parent/hub page instead of
a specific subpage).

Options:
(a) Extract content from the FINAL URL (update filename to match)
(b) Cancel and investigate the URL
```

NEVER save content under a filename derived from the requested URL when a redirect occurred. The filename MUST always match the actual page that was extracted.
</critical>

---

## Extraction Process

Try methods in this order. Move to the next method only when the current one fails.

### Method 1: curl + Local Processing (preferred)

curl is the most reliable method -- it follows redirects transparently, reports the final URL, and fetches raw HTML without bot detection issues from simple WAFs.

**Step 1a: Fetch raw HTML with curl**

Run via Bash:

```bash
curl -sL -w '\n__FINAL_URL__:%{url_effective}\n__HTTP_CODE__:%{http_code}' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -o /tmp/extracted-page.html \
  '[URL]'
```

Check the output:
- `__FINAL_URL__`: Compare with the requested URL. If different, trigger redirect detection (see above).
- `__HTTP_CODE__`: If not 200, this method failed -- move to Method 2.
- If the HTML file is empty or under 500 bytes, this method failed -- move to Method 2.

**Step 1b: Extract meta tags from raw HTML**

Run via Bash:

```bash
# Extract meta title
grep -oPm1 '(?<=<title>).*?(?=</title>)' /tmp/extracted-page.html

# Extract meta description
grep -oPm1 '<meta[^>]*name=["\x27]description["\x27][^>]*content=["\x27]\K[^"\x27]*' /tmp/extracted-page.html
```

If grep patterns fail, extract them manually from the HTML by reading the file.

**Step 1c: Convert HTML to markdown**

Read `/tmp/extracted-page.html` and convert the main content to markdown. Apply these rules:

- Identify the main content area: look for `<main>`, `<article>`, `<div role="main">`, `<div class="content">`, or the largest content block. Skip `<header>`, `<footer>`, `<nav>`, `<aside>`, and sidebar elements.
- Convert heading tags (h1-h6) to markdown headings (#-######)
- Convert `<strong>`/`<b>` to **bold**
- Convert `<em>`/`<i>` to *italic*
- Convert `<ul>/<li>` to `- items` and `<ol>/<li>` to `1. items`
- Convert `<a href="url" title="t">text</a>` to `[text](url "t")`
- Convert `<img src="url" alt="a" title="t">` to `![a](url "t")`
- Convert `<blockquote>` to `> text`
- Convert `<table>` to markdown tables
- Expand `<details>/<summary>` -- include both summary and hidden content
- Strip all remaining HTML tags after conversion

CRITICAL -- YOU MUST preserve these elements. Do NOT strip them out or simplify them:

1. LINKS: Every `<a>` MUST become `[text](URL "title")`. Keep the full href. Include title if present. Do NOT convert links to plain text. Do NOT omit URLs.
2. IMAGES: Every `<img>` MUST become `![alt](src "title")`. Keep the full src. Include alt AND title if present. Do NOT skip images.
3. TEXT FORMATTING: Bold and italic MUST be preserved. Do NOT flatten to plain text.

Include content from ALL expandable/collapsible elements -- FAQs, accordions, `<details>/<summary>`, tabbed panels. Treat collapsed content as fully expanded.

Proceed to the Review step.

**If curl is not available or returns non-200:** Move to Method 2.

### Method 2: WebFetch

Use WebFetch to retrieve the page content. Use the prompt:

```
Extract ONLY the main content area of this page. Skip completely:
- Site header and top navigation bar
- Sidebars (left or right)
- Footer and bottom navigation
- Cookie banners and popups
- Breadcrumbs

IMPORTANT: Include content from ALL expandable/collapsible elements.

CRITICAL -- Preserve ALL of these exactly:
1. LINKS as [link text](URL "title") -- keep full URLs, include title attribute
2. IMAGES as ![alt text](image-src "title") -- keep full src, include alt and title
3. BOLD as **text**, ITALIC as *text** -- do NOT flatten formatting

Also return heading hierarchy (h1-h6), bullets, numbered lists, blockquotes, tables.

Also extract from the HTML <head>:
- The <title> tag content
- The <meta name="description"> value

Format:
META_TITLE: [value]
META_DESCRIPTION: [value]
FINAL_URL: [the actual URL after any redirects]
---
[markdown content]
```

Check the FINAL_URL in the response. If it differs from the requested URL, trigger redirect detection.

**If WebFetch fails (403, timeout, empty):** Move to Method 3.

### Method 3: Browser Extraction

Use browser MCP tools if available. **This method requires extra care -- known pitfalls below.**

<critical>
Known issues with browser extraction:
- `get_page_content` and `browser_snapshot` can return STALE/CACHED content from a previous tab or navigation. Do NOT rely on them alone.
- Some sites use CLIENT-SIDE JavaScript redirects that fire AFTER page load. The URL briefly shows the correct page, then JavaScript redirects to a different page (e.g., /services/website-development/ loads, then JS redirects to /services/). Server-side redirect detection (curl, HTTP headers) will NOT catch these.
- ALWAYS extract content via `browser_evaluate` with direct DOM access. This reads the LIVE DOM at the moment of execution, not cached content.
</critical>

1. **Open a NEW tab** using `browser_tabs` with action "new". Do NOT navigate in an existing tab.
2. Navigate to the URL in the new tab using `browser_navigate`.
3. Wait for the page to fully load (2-3 seconds).
4. **IMMEDIATELY verify URL and extract metadata in a single call** -- do this fast, before any client-side redirect fires:
   ```javascript
   () => {
     const url = window.location.href;
     const title = document.querySelector('title')?.textContent || '';
     const h1 = document.querySelector('h1')?.textContent || '';
     const desc = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
     const canonical = document.querySelector('link[rel="canonical"]')?.href || '';
     const ogUrl = document.querySelector('meta[property="og:url"]')?.getAttribute('content') || '';
     return { current_url: url, meta_title: title, h1: h1, meta_description: desc, canonical: canonical, og_url: ogUrl };
   }
   ```
   Compare `current_url`, `canonical`, and `og_url` with the requested URL. If ANY differ, a redirect has occurred -- trigger redirect detection.
5. **Expand all collapsible content:**
   ```javascript
   () => {
     document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
     document.querySelectorAll(
       '[aria-expanded="false"], .accordion-trigger, .faq-question, ' +
       '.collapse-toggle, [data-toggle="collapse"], .expandable:not(.expanded)'
     ).forEach(el => el.click());
     document.querySelectorAll(
       '.read-more, .show-more, [data-action="expand"], .truncated-toggle'
     ).forEach(el => el.click());
     document.querySelectorAll('.tab-trigger, [role="tab"]').forEach(el => el.click());
     return 'expanded';
   }
   ```
   Wait 1-2 seconds after expanding for content to render.
6. **Extract content via JavaScript DOM access** -- do NOT use `get_page_content` or `browser_snapshot` as primary source, they can return stale data. Use `browser_evaluate` to read the live DOM directly:
   ```javascript
   () => {
     // Find main content container
     const main = document.querySelector('main, article, [role="main"], .content, .page-content, #content')
       || document.querySelector('body');
     // Clone to avoid modifying the page
     const clone = main.cloneNode(true);
     // Remove chrome elements from clone
     clone.querySelectorAll('header, footer, nav, aside, .sidebar, .nav, .header, .footer, .cookie-banner, .breadcrumb').forEach(el => el.remove());
     return clone.innerHTML;
   }
   ```
   Then convert the returned HTML to markdown following the same rules as Method 1 Step 1c.
7. **Re-verify URL after extraction** -- check `window.location.href` again. If the URL changed during extraction (client-side redirect fired), the content may be from the wrong page. Compare the H1 from step 4 with the H1 in the extracted content. If they don't match, the page redirected mid-extraction -- warn the operator.
8. **Close the tab** after extraction to avoid tab pollution in future extractions.
9. Proceed to the Review step.

**If browser tools are NOT available:** Move to Method 4.

### Method 4: Paste-in Fallback

If all automated methods fail, ask the operator to provide the content manually:

```
All automated extraction methods failed for this URL.

Method 1 (curl): [reason -- not available / HTTP error / blocked]
Method 2 (WebFetch): [reason -- 403 / timeout / empty]
Method 3 (Browser): [reason -- not available / redirect / error]

To proceed, open the page in your browser and either:
(a) Select all main content on the page, copy, and paste it here
(b) Use browser View Source, copy the HTML, and paste it here
(c) Try a different URL
(d) Cancel

I will format whatever you paste into clean markdown.
```

When the operator pastes content, apply the same formatting rules (headings, links, images, bold/italic) and proceed to the Review step. Ask the operator for the meta title and meta description separately if not included in the paste.

---

## Review (applies to ALL methods)

Inspect the extracted content for quality. **This step is mandatory -- do not skip any check.**

- **REDIRECT CHECK (critical):** Confirm the content matches the intended page. Check the H1 and first paragraph -- do they match what the operator expects for this URL? If the content looks like a different page, STOP and warn.
- Verify headings follow a logical hierarchy (one H1, H2s for sections, etc.)
- **LINKS CHECK (critical):** Verify every link has a full URL, not just anchor text. If any links were converted to plain text, re-extract them. Count the links found.
- **IMAGES CHECK (critical):** Verify every image has the src URL and alt text. If images were omitted or reduced to text descriptions, re-extract them. Count the images found.
- **FORMATTING CHECK:** Verify bold, italic, and other inline formatting is preserved. If text appears flattened (no bold/italic), re-extract.
- Remove any remaining navigation artifacts or repeated elements
- Remove any HTML tags that were not converted to markdown
- Fix any broken formatting (unclosed bold, misformatted lists)
- **Check for missing collapsed content:** Look for signs of FAQs, accordions, or expandable sections (e.g., FAQ headings with no answers). If collapsed content appears missing, flag it and attempt re-extraction with a different method if possible.

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
source_url: "[original URL as requested by operator]"
final_url: "[actual URL after redirects -- same as source_url if no redirect]"
extraction_method: "[curl / webfetch / browser / paste-in]"
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
- File slugs MUST be derived from the FINAL URL (after redirects), never the requested URL if they differ.
- Remove query parameters (`?`) and fragments (`#`) from URLs before creating the slug.
- NEVER save content without verifying the final URL matches the requested URL. Redirect detection is not optional.
