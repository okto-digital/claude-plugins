# webtools-audit

Content quality auditing for the webtools website pipeline.

## Overview

This plugin evaluates generated content against SEO targets, readability standards, brand voice consistency, heading structure, and blueprint compliance. It produces D10: Content Audit Report with per-page scores and specific improvement suggestions.

## Components

| Type | Name | Description |
|------|------|-------------|
| Command | `/audit` | Audit content quality for all pages or a specific page |

## Usage

```
/audit all           # Audit all D8 content documents
/audit homepage      # Audit only the homepage content
/audit about         # Audit only the about page content
```

**Arguments:**
- `$1` -- Scope: `all` (default) or a specific page slug

The audit evaluates 6 dimensions per page:
1. **SEO** -- Keyword coverage, density, title/meta assessment
2. **Heading structure** -- H1/H2/H3 hierarchy
3. **Readability** -- Sentence length, paragraph length, vocabulary level
4. **Brand voice** -- Consistency with D2 voice profile
5. **Blueprint compliance** -- Content matches D7 blueprint structure
6. **Internal linking** -- Recommended links present

When auditing all pages, also performs cross-page analysis: keyword cannibalization, content consistency, and missing content gaps.

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D8 | Page Content | `content/D8-content-{slug}.md` | Required input (at least one) |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Required input |
| D12 | SEO Content Targets | `seo/D12-seo-content-targets.md` | Optional input |
| D2 | Brand Voice Profile | `brand/D2-brand-voice-profile.md` | Optional input |
| D4 | Site Architecture | `architecture/D4-site-architecture.md` | Optional input |
| D7 | Page Blueprints | `blueprints/D7-blueprint-{slug}.md` | Optional input |
| D5 | Competitor Analysis | `architecture/D5-competitor-analysis.md` | Optional input |
| D10 | Content Audit Report | `audit/D10-content-audit-report.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** (this plugin) -- Content quality auditing
