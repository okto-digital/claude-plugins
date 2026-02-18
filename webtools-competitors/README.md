# webtools-competitors

Competitor and reference site analysis for the webtools website pipeline.

## Overview

This plugin produces D5: Competitor Analysis -- a structured document with page inventories, section patterns, messaging themes, and cross-site insights. It analyzes 3-5 competitor or reference websites to identify common patterns, gaps, and differentiation opportunities.

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `competitor-analyzer` | Structured competitor site analysis with cross-site pattern detection |

## Usage

Invoke the competitor-analyzer skill in a Cowork session with the project folder as the working directory. The skill will:

1. Load D1: Project Brief (required)
2. Confirm competitor URLs (required, from D1 or operator)
3. Analyze each site: page inventory, section structure, messaging, CTAs
4. Identify cross-site patterns, gaps, and opportunities
5. Write D5 to `architecture/D5-competitor-analysis.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D5 | Competitor Analysis | `architecture/D5-competitor-analysis.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** (this plugin) -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
