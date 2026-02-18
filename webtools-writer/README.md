# webtools-writer

Content and microcopy generation for the webtools website pipeline.

## Overview

This plugin produces the written content for the website. It has two skills: a content generator that fills page blueprints with draft content following brand voice, and a microcopy generator that produces all UI text elements for the site.

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `content-generator` | Generate page content from D7 blueprints, one page at a time |
| Skill | `microcopy-generator` | Generate all UI text elements for the entire site |

## Usage

### Content Generation

Invoke the content-generator skill with the project folder as the working directory. The skill will:

1. Load D7 blueprint for the selected page (required) and D2 brand voice (required)
2. Ask for content mode: SEO-optimized or clean
3. Generate content section by section following the blueprint
4. Present draft for review and iteration
5. Write D8 to `content/D8-content-{page-slug}.md`

Run the skill multiple times to generate content for each page.

### Microcopy Generation

Invoke the microcopy-generator skill with the project folder as the working directory. The skill will:

1. Load D4 site architecture, D2 brand voice, and D1 project brief (all required)
2. Identify all UI elements needed based on site structure and project type
3. Generate navigation labels, form text, error messages, CTAs, and all other UI text
4. Present draft for review and iteration
5. Write D9 to `content/D9-microcopy.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D7 | Page Blueprint | `blueprints/D7-blueprint-{slug}.md` | Required input (content-generator) |
| D2 | Brand Voice Profile | `brand/D2-brand-voice-profile.md` | Required input (both skills) |
| D4 | Site Architecture | `architecture/D4-site-architecture.md` | Required input (microcopy-generator) |
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input (microcopy-generator) |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Optional input (content-generator) |
| D8 | Page Content | `content/D8-content-{slug}.md` | Output (one per page) |
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
9. **webtools-writer** (this plugin) -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
