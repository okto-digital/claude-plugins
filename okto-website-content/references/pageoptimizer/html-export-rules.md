# HTML Export Rules

After saving the optimized markdown, auto-export to clean semantic HTML. This follows the same rules as the `/webtools-writer-export` command.

---

## Conversion Rules

### Strip YAML Frontmatter

Remove everything between the opening `---` and closing `---` at the top of the file. Preserve `meta_title` and `meta_description` for the output header.

### Markdown to HTML

**Headings:**
- `# text` becomes `<h1>text</h1>`
- `## text` becomes `<h2>text</h2>`
- Through `######` becoming `<h6>`

**Inline formatting:**
- `**bold**` becomes `<strong>bold</strong>`
- `*italic*` becomes `<em>italic</em>`

**Links:**
- `[text](url)` becomes `<a href="url">text</a>`
- `[text](url "title")` becomes `<a href="url" title="title">text</a>`

**Images:**
- `![alt](src)` becomes `<img src="src" alt="alt">`
- `![alt](src "title")` becomes `<img src="src" alt="alt" title="title">`

**Lists:**
- Unordered lists (`- item`) become `<ul><li>item</li></ul>`
- Ordered lists (`1. item`) become `<ol><li>item</li></ol>`
- Nested lists become nested `<ul>` or `<ol>` elements

**Block elements:**
- `> text` becomes `<blockquote><p>text</p></blockquote>`
- Paragraphs (text separated by blank lines) become `<p>text</p>`
- Horizontal rules (`---`) become `<hr>`

**Tables:**
```
| Header | Header |
|--------|--------|
| Cell   | Cell   |
```
Becomes:
```html
<table>
  <thead>
    <tr><th>Header</th><th>Header</th></tr>
  </thead>
  <tbody>
    <tr><td>Cell</td><td>Cell</td></tr>
  </tbody>
</table>
```

---

## Output Rules

<critical>
Do NOT wrap the output in `<html>`, `<head>`, or `<body>` tags. Output ONLY the content markup.

Do NOT add any CSS, classes, IDs, or styling attributes. Clean semantic HTML only.
</critical>

---

## Output File Structure

Write to `content/pageoptimized-{slug}.html` with this structure:

```html
<!--
  Source: [source .md filename]
  Exported: [today's date YYYY-MM-DD]
  Original URL: [source_url from frontmatter, or "n/a" if not present]
  Meta Title: [meta_title from frontmatter, or "n/a" if not present]
  Meta Description: [meta_description from frontmatter, or "n/a" if not present]
-->
<title>[meta_title from frontmatter]</title>
<meta name="description" content="[meta_description from frontmatter]">

[converted HTML content]
```

Omit the `<title>` tag if meta_title is empty or not present. Omit the `<meta>` tag if meta_description is empty or not present.
