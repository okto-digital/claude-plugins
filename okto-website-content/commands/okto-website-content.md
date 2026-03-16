---
description: "okto-website-content: Show available modes, commands, and content status"
allowed-tools: Read, Glob
---

Show the okto-website-content plugin overview: available modes, commands, and current content status.

## Instructions

Display the following overview:

---

[CONTENT] okto-website-content -- Content Manager

Modes (conversational -- infer from context):
  Extract          Crawl a URL into markdown (dispatches web-crawler)
  Audit            Assess content quality, voice alignment, SEO signals
  Opportunity      Identify content gaps and new page ideas
  Research         Deep-dive a topic (web search + optional DataForSEO)
  Outline          Structure a page before writing
  EEAT Interview   Extract unique expertise via pointed questions
  Write            Draft content in oktodigital voice
  Optimize         Rewrite for PageOptimizer keyword targets (5 phases)
  Export           Convert markdown to production HTML

Commands:
  /okto-website-content              Show this overview
  /okto-website-content-extract      Quick extract: URL to markdown
  /okto-website-content-optimize     Quick optimize: content + PO briefs
  /okto-website-content-export       Quick export: markdown to HTML
  /okto-website-content-keywords     Run keyword research via DataForSEO

---

Then scan the content/ directory (if it exists) and list existing content files grouped by type (extracted, research, outline, draft, optimized, export). Show file count per type.

If no content/ directory exists, show: "No content directory yet. Start by extracting a page or writing content."

Suggest a next step based on what exists:
- No files: "Try: paste a URL to extract, or ask to write content for a page"
- Only extracted: "Try: audit the extracted content, or start an outline"
- Has outlines but no drafts: "Try: write a draft from your outline"
- Has drafts but no optimized: "Try: optimize with PageOptimizer briefs"
