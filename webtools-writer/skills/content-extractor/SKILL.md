---
name: content-extractor
description: "Extract content from a live web page and save it as a well-formatted markdown file. Fetches the page, strips navigation/header/sidebar/footer, and preserves the main content with heading hierarchy, text formatting, links, and images."
allowed-tools: Bash, WebFetch, Read, Write, Edit, Glob
version: 2.2.0
---

Extract content from a live web page and save it as a clean, well-formatted markdown file in the `content/` directory. The extracted file preserves heading hierarchy, text formatting, links, and images -- but strips site chrome (header, navigation, sidebar, footer).

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
  1. curl + local processing   [available / not available]
  2. WebFetch                  [always available]
  3. Browser Fetch (fetch API) [available / not available]
  4. Browser Navigation        [available / not available]
  5. Paste-in                  [always available]

Ready to extract.
```

**Tool detection (shell-agnostic):** Do not assume a specific shell tool. Check for ANY available shell execution tool -- Bash, Desktop Commander, terminal MCP, or similar. If any shell tool is available, run `which curl` to verify curl is installed. If no shell tool exists (e.g., cloud-only Cowork session without Desktop Commander), method 1 is unavailable. **In cloud environments (Cowork), prefer Desktop Commander over VM Bash** -- Desktop Commander runs on the user's machine (residential IP, bypasses WAFs), while VM Bash runs from datacenter IPs (blocked by most WAFs).

**Browser tool detection:** Check if browser tools (e.g., `browser_navigate`, `browser_evaluate`) are accessible. If available, methods 3 and 4 are available.

---

## Redirect Detection

<critical>
ALWAYS verify the final URL after fetching. URLs frequently redirect silently (e.g., /services/website-development/ redirects to /services/). Some redirects are server-side (HTTP 301/302), others are CLIENT-SIDE JavaScript redirects that fire AFTER page load.

If the final URL differs from the requested URL, STOP and warn the operator BEFORE processing content:

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

Try methods in this order. Move to the next method only when the current one fails. Each method has detailed instructions in its reference file.

| Priority | Method | When to use | Reference |
|---|---|---|---|
| 1 | curl + local processing | Preferred. Requires shell access (Bash, Desktop Commander, etc.). Most reliable for redirect detection. | `references/method-curl.md` |
| 2 | WebFetch | No shell available, or curl blocked. Runs from cloud servers -- blocked by most WAFs. | `references/method-webfetch.md` |
| 3 | Browser Fetch | WebFetch blocked (403/WAF). Uses `fetch()` API inside the user's browser -- gets raw HTML from user's IP without page navigation. | `references/method-browser-fetch.md` |
| 4 | Browser Navigation | Browser Fetch failed (page requires JS rendering, or fetch blocked). Full page load with redirect blocker. | `references/method-browser.md` |
| 5 | Paste-in | All automated methods failed. | `references/method-paste-in.md` |

<critical>
**Method selection shortcut for cloud environments (Cowork without shell access):**
When curl is unavailable and the target site is behind WAF/bot protection (WebFetch returns 403), skip directly to Method 3 (Browser Fetch). Do NOT spend time retrying WebFetch -- if the site blocks datacenter IPs, WebFetch will always fail for that domain.
</critical>

Read the reference file for the method you are about to use. All methods share the same formatting rules defined in `references/formatting-rules.md` -- read it before converting any HTML to markdown.

After successful extraction with any method, proceed to the Review step below.

---

## Review and Save (applies to ALL methods)

Inspect the extracted content for quality before saving. **This step is mandatory -- do not skip any check.** Perform all checks internally without presenting the full content to the operator.

- **REDIRECT CHECK (critical):** Confirm the content matches the intended page. Check the H1 and first paragraph -- do they match what the operator expects for this URL? If the content looks like a different page, STOP and warn.
- Verify headings follow a logical hierarchy (one H1, H2s for sections, etc.)
- **LINKS CHECK (critical):** Verify every link has a full URL, not just anchor text. If any links were converted to plain text, re-extract them.
- **IMAGES CHECK (critical):** Verify every image has the src URL and alt text. If images were omitted or reduced to text descriptions, re-extract them.
- **FORMATTING CHECK:** Verify bold, italic, and other inline formatting is preserved. If text appears flattened (no bold/italic), re-extract.
- Remove any remaining navigation artifacts or repeated elements
- Remove any HTML tags that were not converted to markdown
- Fix any broken formatting (unclosed bold, misformatted lists)
- **Check for missing collapsed content:** Look for signs of FAQs, accordions, or expandable sections (e.g., FAQ headings with no answers). If collapsed content appears missing, flag it and attempt re-extraction with a different method if possible.

<critical>
Save the file immediately after passing quality checks. Do NOT present the full extracted content in the chat. Do NOT ask for operator approval before saving. The operator will review the file directly via the file link.
</critical>

After saving (see File Naming, Output Format, and Lifecycle Completion below), present a brief summary with the file path:

```
Extracted: content/extracted-[slug].md

Source: [URL]
Method: [curl / webfetch / browser-fetch / browser-nav / paste-in]
Title: [page title or H1]
Word count: [count]
Headings: [count] (H1: [n], H2: [n], H3: [n], ...)
Links: [count]
Images: [count]

Review the file and let me know if anything needs to be re-extracted.
```

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

Remove query parameters and fragments from the URL before slugifying. File slugs MUST be derived from the FINAL URL (after redirects), never the requested URL if they differ.

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
extraction_method: "[curl / webfetch / browser-fetch / browser-nav / paste-in]"
project: "[client name]"
extracted: [today]
created_by: webtools-writer
status: extracted
---
```

Then the extracted markdown content.

---

## Lifecycle Completion

Complete these 3 steps immediately after passing quality checks.

### 1. Save File

Write the file to `content/extracted-{slug}.md` with frontmatter and extracted content.

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
- NEVER save content without verifying the final URL matches the requested URL. Redirect detection is not optional.

---

## Reference Files

- `references/formatting-rules.md` -- Shared HTML-to-markdown conversion rules, element preservation requirements
- `references/method-curl.md` -- curl + local HTML processing (preferred method, requires shell access)
- `references/method-webfetch.md` -- WebFetch extraction with prompt template (cloud servers, blocked by WAFs)
- `references/method-browser-fetch.md` -- Browser fetch() API extraction (user's IP, raw HTML, no page navigation)
- `references/method-browser.md` -- Full browser page load with redirect blocker (last resort for JS-rendered pages)
- `references/method-paste-in.md` -- Manual paste-in fallback workflow
