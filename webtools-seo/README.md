# webtools-seo

SEO keyword research for the webtools website pipeline.

## Overview

This plugin produces D3: SEO Keyword Map -- a structured document mapping keyword opportunities to pages with volume estimates, difficulty assessments, and intent classifications. It follows a structured methodology: seed generation, expansion, competitor analysis, clustering, and page mapping.

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `seo-keyword-research` | Structured keyword research with clustering and page mapping |

## Usage

Invoke the seo-keyword-research skill in a Cowork session with the project folder as the working directory. The skill will:

1. Load D1: Project Brief (required)
2. Gather research inputs (services, geographic focus, seed keywords, competitor URLs)
3. Generate and expand keyword seeds
4. Analyze competitor keyword usage
5. Cluster keywords by topic and intent
6. Map clusters to target pages
7. Write D3 to `seo/D3-seo-keyword-map.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** (this plugin) -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
