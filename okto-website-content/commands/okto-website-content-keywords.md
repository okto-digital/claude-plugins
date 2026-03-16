---
description: "okto-website-content: Run keyword research via DataForSEO"
allowed-tools: Read, Write, Task
---

Run keyword research using DataForSEO MCP tools.

## Usage

`/okto-website-content-keywords [seed-keywords...]`

Examples:
- `/okto-website-content-keywords web design services`
- `/okto-website-content-keywords "SEO audit" "technical SEO"`

If no seed keywords are provided, ask the operator for the keywords to research.

## Instructions

@agents/content-manager.md

Enter Research mode focused on keyword research. Dispatch the dataforseo sub-agent with the provided seed keywords. Request keyword ideas, search volume, keyword difficulty, and search intent classification. Present the results in a structured table and save to content/research-{topic-slug}.md.
