---
description: "okto-website-content: Extract a web page into clean markdown"
allowed-tools: Read, Write, Bash, WebFetch, Task
---

Extract a web page into clean markdown with metadata.

## Usage

`/okto-website-content-extract [URL]`

If no URL argument is provided, ask the operator for the URL to extract.

## Instructions

@agents/content-manager.md

Enter Extract mode with the provided URL. Follow the Extract mode process: dispatch the web-crawler sub-agent, write the result to content/extracted-{slug}.md with metadata frontmatter, and offer to audit the extracted content.
