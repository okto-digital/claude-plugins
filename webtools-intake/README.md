# webtools-intake

Client intake and project brief creation for the webtools website pipeline.

## Overview

This plugin handles the discovery phase of the webtools pipeline. It provides two tools: a questionnaire generator for structured client intake, and a conversational agent for synthesizing raw client input into a structured project brief.

## Components

| Type | Name | Description |
|------|------|-------------|
| Command | `/questionnaire` | Generate tailored client intake questionnaire based on project type and industry |
| Agent | `brief-generator` | Conversational brief creation from raw client input |

## Workflow

1. Run `/questionnaire [project-type] [industry]` to generate D11: Client Questionnaire
2. Conduct the client interview using the generated questions
3. Start the Brief Generator agent with the client's answers (and any other raw input)
4. Iterate with the agent until D1: Project Brief is approved

## Commands

### /questionnaire

Generate a tailored client intake questionnaire.

```
/questionnaire new-build restaurant
/questionnaire redesign saas
/questionnaire landing-page
/questionnaire ecommerce retail
```

**Arguments:**
- `$1` -- Project type (required): `new-build`, `redesign`, `landing-page`, `ecommerce`
- `$2` -- Industry (optional): freeform text for industry-specific questions

**Output:** `brief/D11-client-questionnaire.md`

The questionnaire includes three sections:
- **Section A:** Universal questions (all project types)
- **Section B:** Project-type-specific questions
- **Section C:** Industry-specific questions (only if industry provided)

## Agents

### brief-generator

Takes raw, unstructured client information and synthesizes it into a comprehensive D1: Project Brief through iterative dialogue.

Accepts input in any format: meeting notes, questionnaire answers, URLs, bullet points, emails, or stream-of-consciousness text. The agent identifies gaps, asks targeted clarifying questions, and presents a draft for review.

**Output:** `brief/D1-project-brief.md`

#### Domain Validation

The brief-generator validates extracted information against comprehensive domain checklists stored in `references/domains/`. Each domain covers an area of website development expertise with checkpoints tagged by priority (CRITICAL / IMPORTANT / NICE-TO-HAVE).

The agent reads all domain files dynamically, scores the input against every checkpoint, and produces a structured gap report. Questions to fill gaps follow priority order (CRITICAL first) and use an Option A / Option B format to reduce cognitive load.

- **15 universal domains** -- always evaluated regardless of project type
- **6 conditional domains** -- evaluated only when relevant (e.g., e-commerce, multilingual)

## Documents Produced

| Doc ID | Document | File Path |
|--------|----------|-----------|
| D11 | Client Questionnaire | `brief/D11-client-questionnaire.md` |
| D1 | Project Brief | `brief/D1-project-brief.md` |

## Reference Files

Domain checklists used by the brief-generator for gap analysis. Located in `references/domains/`.

### Universal Domains (always evaluated)

| # | File | Focus |
|---|---|---|
| 1 | `business-context.md` | Business identity, goals, value proposition, market position |
| 2 | `target-audience.md` | Primary/secondary personas, needs, behavior, decision journey |
| 3 | `competitive-landscape.md` | Named competitors, strengths/gaps, differentiation strategy |
| 4 | `content-strategy.md` | Existing content, content creation plan, messaging hierarchy |
| 5 | `site-structure.md` | Page inventory, navigation model, information architecture, user flows |
| 6 | `design-and-brand.md` | Brand identity status, visual style, imagery, typography |
| 7 | `seo-and-discoverability.md` | Keyword strategy, technical SEO, URL structure, local SEO |
| 8 | `technical-platform.md` | CMS/platform, hosting, infrastructure, integrations |
| 9 | `performance.md` | Page speed targets, Core Web Vitals, optimization |
| 10 | `accessibility.md` | WCAG compliance, assistive technology, inclusive design |
| 11 | `analytics-and-measurement.md` | Tracking setup, KPIs, conversion events, reporting |
| 12 | `security-and-compliance.md` | SSL, GDPR/CCPA, cookie consent, regulations |
| 13 | `forms-and-lead-capture.md` | Contact forms, CTAs, lead flow, CRM integration |
| 14 | `project-scope.md` | Timeline, budget, milestones, phasing, approvals |
| 15 | `post-launch.md` | Maintenance, content updates, hosting, support |

### Conditional Domains (evaluated when applicable)

| # | File | Applies When |
|---|---|---|
| 16 | `ecommerce.md` | Products or services sold online |
| 17 | `blog-and-editorial.md` | Regular content publishing planned |
| 18 | `multilingual.md` | Multiple languages needed |
| 19 | `user-accounts.md` | Login, membership, or gated content |
| 20 | `migration-and-redesign.md` | Existing site to migrate from |
| 21 | `booking-and-scheduling.md` | Appointment or reservation functionality |

## Part of the Webtools Suite

This plugin is part of the webtools website creation pipeline:

1. **webtools-init** -- Project setup and management
2. **webtools-intake** (this plugin) -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
