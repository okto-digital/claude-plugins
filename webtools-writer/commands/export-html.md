---
description: Convert content markdown to clean semantic HTML
allowed-tools: Read, Write, Glob, Bash(mkdir:*), Bash(python3:scripts/*)
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

## Convert and Write

Run the conversion script:

```bash
python3 scripts/markdown-to-html.py content/[source].md content/[output].html
```

The script handles all conversion:
- Strips YAML frontmatter, preserves meta_title and meta_description
- Converts all markdown elements to clean semantic HTML (headings, bold, italic, links, images, lists, tables, blockquotes, horizontal rules)
- Writes the output file with metadata comment, `<title>` and `<meta>` tags at top
- Outputs ONLY content markup (no `<html>/<head>/<body>` wrapper, no CSS/classes/IDs)
- Validates output and reports any issues

The script outputs a JSON summary to stdout:
```json
{
  "status": "ok",
  "output": "content/[name].html",
  "output_size": 12451,
  "elements": {"headings": 30, "paragraphs": 68, "links": 15, "images": 1},
  "meta_title": "...",
  "meta_description": "..."
}
```

Use the JSON summary for the file verification and downstream notification. If `status` is "warning", review and resolve the listed issues before proceeding.

---

## Lifecycle Completion

### 1. File Verification

The script's JSON output includes validation. Check:
- `status` is "ok" (no issues found) or "warning" (review listed issues)
- `elements.headings` > 0 (HTML has heading tags)
- `output_size` > 0 (file is non-empty)

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
