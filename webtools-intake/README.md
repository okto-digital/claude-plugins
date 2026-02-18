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

## Documents Produced

| Doc ID | Document | File Path |
|--------|----------|-----------|
| D11 | Client Questionnaire | `brief/D11-client-questionnaire.md` |
| D1 | Project Brief | `brief/D1-project-brief.md` |

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
