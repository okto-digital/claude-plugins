# Formatting Rules

Shared HTML-to-markdown conversion rules used by all extraction methods. Read this file before converting any HTML content to markdown.

---

## Content Area Identification

Identify the main content area from the HTML. Look for these elements in order:
- `<main>`
- `<article>`
- `<div role="main">`
- `<div class="content">` or `<div class="page-content">` or `<div id="content">`
- Largest content block inside `<body>`

**Skip entirely:**
- `<header>`, `<footer>`, `<nav>`, `<aside>`
- Elements with classes: `.sidebar`, `.nav`, `.header`, `.footer`, `.cookie-banner`, `.breadcrumb`
- Cookie banners, popups, modals
- Social media share buttons, "Related posts" sections, comment sections, ad blocks

---

## Element Conversion Rules

### Headings

Convert heading tags to markdown headings preserving the hierarchy:
- `<h1>` --> `#`
- `<h2>` --> `##`
- `<h3>` --> `###`
- `<h4>` --> `####`
- `<h5>` --> `#####`
- `<h6>` --> `######`

### Text Formatting

- `<strong>` or `<b>` --> `**bold text**`
- `<em>` or `<i>` --> `*italic text*`
- `<code>` --> `` `inline code` ``
- `<pre><code>` --> fenced code block with language if specified

### Lists

- `<ul>` with `<li>` --> `- item` (bulleted list)
- `<ol>` with `<li>` --> `1. item` (numbered list)
- Nested lists: indent with 2 spaces per level

### Links

- `<a href="url">text</a>` --> `[text](url)`
- `<a href="url" title="t">text</a>` --> `[text](url "t")`
- Keep the full href URL (absolute preferred). Do not shorten or omit URLs.
- If href is relative, convert to absolute using the page's base URL.

### Images

- `<img src="url" alt="a">` --> `![a](url)`
- `<img src="url" alt="a" title="t">` --> `![a](url "t")`
- Keep the full src URL. Do not omit image references.
- If src is relative, convert to absolute using the page's base URL.

### Block Quotes

- `<blockquote>` --> `> text`
- Nested blockquotes: `> > text`

### Tables

Convert `<table>` to markdown table format:
```
| Header 1 | Header 2 |
|---|---|
| Cell 1 | Cell 2 |
```

### Horizontal Rules

- `<hr>` --> `---`

### Collapsible / Expandable Content

- `<details>` / `<summary>` --> Include BOTH the summary text and the hidden content as regular markdown. Do not hide or collapse content.
- Accordions, FAQ toggles, "read more" sections --> Treat as fully expanded. Extract all hidden content.
- Tabbed panels --> Extract content from ALL tabs, not just the active one.

---

## Critical Preservation Requirements

These elements MUST be preserved in the markdown output. Failing to preserve them is a failed extraction.

1. **LINKS:** Every `<a>` tag MUST become `[text](URL "title")`. Keep the full href URL. Include the title attribute in quotes if present. Do NOT convert links to plain text. Do NOT omit URLs. Do NOT strip link destinations.

2. **IMAGES:** Every `<img>` tag MUST become `![alt](src "title")`. Keep the full src URL. Include alt text AND title attribute if present. Do NOT skip images. Do NOT replace images with text descriptions.

3. **TEXT FORMATTING:** All `<strong>`/`<b>` MUST become `**bold**`. All `<em>`/`<i>` MUST become `*italic*`. Do NOT flatten formatted text to plain text.

4. **COLLAPSIBLE CONTENT:** ALL expandable elements (FAQs, accordions, details/summary, tabs) MUST be included fully expanded. Do NOT extract only the visible/summary content.

---

## Cleanup

After conversion:
- Strip all remaining HTML tags that were not converted
- Remove empty lines caused by removed elements (but keep intentional paragraph breaks)
- Fix broken formatting: unclosed bold/italic markers, misformatted lists, orphaned link syntax
- Ensure consistent spacing between sections (one blank line between paragraphs, two before headings)
