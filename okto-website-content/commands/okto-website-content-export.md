---
description: "okto-website-content: Export content markdown to production HTML"
allowed-tools: Read, Write, Glob
---

Convert a content markdown file to production HTML.

## Usage

`/okto-website-content-export [content-file]`

If no content file argument is provided, list available content .md files in content/ and ask the operator which to export.

## Instructions

@agents/content-manager.md

Enter Export mode. Convert the specified markdown file to clean semantic HTML following the export rules. Output is content-only (no html/head/body wrapper tags). Write to content/export-{slug}.html.
