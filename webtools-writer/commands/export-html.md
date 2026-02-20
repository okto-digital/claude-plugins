---
description: Convert content markdown to clean semantic HTML
allowed-tools: Read, Write, Glob, Bash(mkdir:*)
argument-hint: [filename.md]
---

Convert a markdown file from `content/` to clean semantic HTML for PageOptimizer.pro or other HTML-based analysis tools.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

If $1 is provided, verify `content/$1` exists. If the file does not exist, list all `.md` files in `content/` and show an error with the available files.

If $1 is omitted, verify `content/` contains at least one `.md` file.

### 4. Output Preparation

The output filename is the same as the source with `.html` replacing `.md`:
- `extracted-oktodigital-com_services_web-design.md` becomes `extracted-oktodigital-com_services_web-design.html`

Check if the output file already exists in `content/`. If yes, warn the operator:

```
HTML export already exists: content/[name].html (updated: [date])
Overwrite with a fresh export, or cancel?
```

If the operator cancels, stop.

### 5. Status Report

```
Project: [client name]
Source: content/[name].md
Output: content/[name].html ([new / overwrite])

Ready to export.
```

---

## Resolve Source File

If $1 is provided, use `content/$1` as the source file.

If $1 is omitted, list all `.md` files in `content/` and ask the operator to pick one:

```
Markdown files in content/:
  1. extracted-oktodigital-com_services_web-design.md
  2. extracted-oktodigital-com_about.md
  3. ...

Which file to export? (number or filename)
```

---

## Read and Convert

### 1. Read the source file

Read the full contents of the source `.md` file.

### 2. Strip YAML frontmatter

Remove everything between the opening `---` and closing `---` at the top of the file. Preserve the frontmatter values in memory -- the `title`, `source_url`, `meta_title`, and `meta_description` fields are used when writing the HTML file.

### 3. Convert markdown to semantic HTML

Convert the markdown body to clean HTML using these rules:

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

### 4. Output rules

<critical>
Do NOT wrap the output in `<html>`, `<head>`, or `<body>` tags. Output ONLY the content markup. PageOptimizer.pro and similar tools need just the content HTML, not a full document.

Do NOT add any CSS, classes, IDs, or styling attributes. Clean semantic HTML only.
</critical>

---

## Write HTML File

Write the converted HTML to `content/[same-name].html`.

Add a metadata comment at the very top of the file:

```html
<!--
  Source: [source .md filename]
  Exported: [today's date YYYY-MM-DD]
  Original URL: [source_url from frontmatter, or "n/a" if not present]
  Meta Title: [meta_title from frontmatter, or "n/a" if not present]
  Meta Description: [meta_description from frontmatter, or "n/a" if not present]
-->
```

Then the converted HTML content.

---

## Lifecycle Completion

### 1. File Verification

Read the output file back and verify:
- File exists and is non-empty
- Contains valid HTML tags (at least one `<h1>` or `<h2>`)
- Does NOT contain YAML frontmatter remnants
- Does NOT contain markdown syntax (`##`, `**`, `[text](url)`)

### 2. Registry Update

Update `project-registry.md`:
- Add a row to the Document Log: Doc ID = `--`, Document = `HTML Export: [title from frontmatter]`, File Path = `content/[name].html`, Status = `exported`, Created = today, Updated = today, Created By = `webtools-writer`
- Phase Log: if Content phase has no Started date, set Started to today. Add `webtools-writer` to Plugins Used.

### 3. Downstream Notification

```
HTML export complete: content/[name].html
Source: content/[name].md
Size: [file size in KB]

The HTML file contains clean semantic markup ready for
PageOptimizer.pro or other HTML analysis tools.
```
