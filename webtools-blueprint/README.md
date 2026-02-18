# webtools-blueprint

Page blueprint generation for the webtools website pipeline.

## Overview

This plugin produces D7: Page Blueprint documents -- one per page. The Blueprint Generator agent co-creates page structures section by section through strategic conversation, making decisions about content flow, user psychology, and conversion optimization. It consults a built-in Knowledge Base of proven page type recipes and section patterns.

## Components

| Type | Name | Description |
|------|------|-------------|
| Agent | `blueprint-generator` | Interactive page blueprint creation, one page at a time |
| Reference | `page-type-recipes.md` | Proven section sequences for 10 page types |
| Reference | `section-patterns.md` | Detailed patterns for 19 section types |

## Knowledge Base

The plugin bundles a Knowledge Base in `references/` that the agent consults during blueprint creation:

### Page Type Recipes (10 types)
Homepage, Service page, About page, Portfolio/Case studies, Landing page, Contact page, Blog listing, Product page, Pricing page, Case study (individual)

Each recipe includes recommended section sequence, purpose annotations, typical word counts, conversion strategy notes, and common variations.

### Section Pattern Library (19 patterns)
Hero, Problem/Pain, Solution/Value Proposition, Features/Services, How It Works/Process, Testimonials/Social Proof, Case Study Highlight, Stats/Numbers, FAQ, CTA (Primary), CTA (Secondary), Portfolio Grid, Pricing Table, Contact Form, Blog Preview, Partners/Logos, Comparison Table, Timeline/History, Team

Each pattern includes purpose, when to use, content requirements, visual hints, and common mistakes.

## Usage

Start the blueprint generator agent in a Cowork session with the project folder as the working directory. The agent will:

1. Load D4: Site Architecture and D1: Project Brief (required)
2. Load optional inputs: D2 (brand voice), D3 (SEO), D5 (competitors), D6 (inventory)
3. Present the page list and ask which page to blueprint
4. Recommend a section sequence from the Knowledge Base
5. Walk through each section for operator approval
6. Write D7 to `blueprints/D7-blueprint-{page-slug}.md`
7. Report blueprint coverage vs D4 page list

Run the agent multiple times to blueprint all pages.

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D4 | Site Architecture | `architecture/D4-site-architecture.md` | Required input |
| D2 | Brand Voice Profile | `brand/D2-brand-voice-profile.md` | Optional input |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Optional input |
| D5 | Competitor Analysis | `architecture/D5-competitor-analysis.md` | Optional input |
| D6 | Content Inventory | `architecture/D6-content-inventory.md` | Optional input |
| D7 | Page Blueprint | `blueprints/D7-blueprint-{slug}.md` | Output (one per page) |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** (this plugin) -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
