# webtools-architecture

Site architecture planning for the webtools website pipeline.

## Overview

This plugin produces D4: Site Architecture -- the document that defines the complete site structure, navigation, URL slugs, user journeys, and internal linking strategy. D4 is the naming authority: all downstream D7 (blueprint) and D8 (content) files use page slugs defined here.

## Components

| Type | Name | Description |
|------|------|-------------|
| Agent | `architecture-planner` | Conversational site structure planning |

## Usage

Start the architecture planner agent in a Cowork session with the project folder as the working directory. The agent will:

1. Load D1: Project Brief (required)
2. Load optional research: D3 (SEO), D5 (competitors), D6 (content inventory)
3. Walk through architecture decisions: pages, hierarchy, slugs, navigation, user journeys
4. Confirm each decision with the operator
5. Write D4 to `architecture/D4-site-architecture.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Optional input |
| D5 | Competitor Analysis | `architecture/D5-competitor-analysis.md` | Optional input |
| D6 | Content Inventory | `architecture/D6-content-inventory.md` | Optional input |
| D4 | Site Architecture | `architecture/D4-site-architecture.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** (this plugin) -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
