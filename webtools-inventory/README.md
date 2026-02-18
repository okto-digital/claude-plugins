# webtools-inventory

Content inventory and migration analysis for the webtools website pipeline.

## Overview

This plugin produces D6: Content Inventory -- a structured document cataloging all existing content from a client's current website with quality assessments and migration recommendations. It crawls the existing site page by page, extracts content, assesses quality, and maps old content to the new site structure.

This plugin is primarily relevant for redesign projects. For new-build projects, it can still be used if the client has content on an existing platform.

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `content-inventory` | Structured site crawl with content quality assessment and migration mapping |

## Usage

Invoke the content-inventory skill in a Cowork session with the project folder as the working directory. The skill will:

1. Load D1: Project Brief (required)
2. Confirm existing website URL (required)
3. Discover all pages (sitemap or crawl)
4. Analyze each page: content, quality, SEO metadata, media assets
5. Produce migration recommendations
6. Write D6 to `architecture/D6-content-inventory.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D6 | Content Inventory | `architecture/D6-content-inventory.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** (this plugin) -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
