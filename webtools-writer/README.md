# webtools-writer

Content generation, optimization, and microcopy for the webtools website pipeline.

## Overview

This plugin produces the written content for the website. It has four skills: a content generator that creates page content from D7 blueprints or standalone content briefs, a content optimizer that rewrites content against PageOptimizer.pro keyword targets, a microcopy generator that produces all UI text elements for the site, and a content extractor that pulls content from live web pages for revision.

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `content-generator` | Generate page content from D7 blueprints or content briefs, one page at a time |
| Skill | `content-pageoptimizer` | Optimize page content against PageOptimizer.pro keyword targets |
| Skill | `microcopy-generator` | Generate all UI text elements for the entire site |
| Skill | `content-extractor` | Extract content from a live web page and save as formatted markdown |
| Command | `/export-html` | Convert content markdown to clean semantic HTML |

## Usage

### Content Generation

Invoke the content-generator skill with the project folder as the working directory. The skill auto-detects available sources and operates in one of two modes:

**Blueprint mode** (D-pipeline):
1. Load D7 blueprint for the selected page (required) and D2 brand voice (required)
2. Ask for content mode: SEO-optimized or clean
3. Generate content section by section following the blueprint
4. Present draft for review and iteration
5. Write to `content/D8-content-{page-slug}.md`

**Brief mode** (standalone):
1. Load a content brief from `content/content-brief-{slug}.md` and D2 brand voice (optional)
2. Parse outline, keywords, and PageOptimizer briefs from the brief
3. Generate content section by section following the outline
4. Present draft for review and iteration
5. Write to `content/generated-{slug}.md`

If neither blueprints nor briefs exist, the skill offers to create a content brief from its built-in template.

Run the skill multiple times to generate content for each page.

### Content Optimization

Invoke the content-pageoptimizer skill with the project folder as the working directory. The skill will:

1. Select source content (`extracted-`, `generated-`, or `pageoptimized-` files)
2. Parse 4 PageOptimizer.pro content brief files (title, H1, subheadings, body)
3. Analyze keyword gaps and present an optimization plan
4. Rewrite content section by section to hit keyword targets
5. Verify all keywords with a scorecard and auto-export to HTML

### Microcopy Generation

Invoke the microcopy-generator skill with the project folder as the working directory. The skill will:

1. Load D4 site architecture, D2 brand voice, and D1 project brief (all required)
2. Identify all UI elements needed based on site structure and project type
3. Generate navigation labels, form text, error messages, CTAs, and all other UI text
4. Present draft for review and iteration
5. Write D9 to `content/D9-microcopy.md`

### Content Extraction

Invoke the content-extractor skill with the project folder as the working directory. The skill will:

1. Ask for the URL of the live page to extract
2. Fetch the page and extract main content only (skips header, nav, sidebar, footer)
3. Format as clean markdown preserving headings, links, images, and text formatting
4. Present extracted content for review and iteration
5. Save to `content/extracted-{url-slug}.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D7 | Page Blueprint | `blueprints/D7-blueprint-{slug}.md` | Required input (content-generator, blueprint mode) |
| D2 | Brand Voice Profile | `brand/D2-brand-voice-profile.md` | Required input (blueprint mode), optional (brief mode, optimizer, microcopy) |
| D4 | Site Architecture | `architecture/D4-site-architecture.md` | Required input (microcopy-generator) |
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input (microcopy-generator) |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Optional input (content-generator) |
| D8 | Page Content | `content/D8-content-{slug}.md` | Output (content-generator, blueprint mode) |
| -- | Generated Content | `content/generated-{slug}.md` | Output (content-generator, brief mode) |
| -- | Content Brief | `content/content-brief-{slug}.md` | Input (content-generator, brief mode) |
| -- | Optimized Content | `content/pageoptimized-{slug}.md` | Output (content-pageoptimizer) |
| D9 | Microcopy | `content/D9-microcopy.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** (this plugin) -- Content generation, optimization, and microcopy
10. **webtools-audit** -- Content quality auditing
