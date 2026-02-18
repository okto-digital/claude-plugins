# webtools-brand

Brand voice profiling for the webtools website pipeline.

## Overview

This plugin creates D2: Brand Voice Profile -- a comprehensive document that defines how the brand communicates across 15 voice dimensions with archetype profiling, channel adaptation, and anti-boring standards. Every piece of website content follows this profile.

It operates in two modes depending on whether the client has existing content to analyze.

## Components

| Type | Name | Description |
|------|------|-------------|
| Agent | `brand-voice-creator` | Interactive brand voice extraction or generation across 15 dimensions |

## What the D2 Includes

The D2: Brand Voice Profile produced by this plugin contains 9 sections:

| Section | Content |
|---------|---------|
| Voice Foundation | 5 scored dimensions: core attributes, formality, language style, perspective, emotional quality |
| Brand Archetype Profile | Primary + secondary + accent archetypes with percentages and voice implications |
| Vocabulary & Expression | Power words, banned phrases, filler words, industry terminology, sentence style, punctuation personality |
| Storytelling & Rhetoric | Narrative frameworks, rhetorical device preferences, pacing and rhythm scores |
| Channel Tone Adaptation | How voice shifts across website, blog, social, email, docs, and crisis communication |
| Anti-Boring Standards | Boring detector criteria, banned cliches, required freshness elements per content type |
| Sample Content | Voice demonstrated across multiple contexts with anti-boring elements |
| Do's and Don'ts | Concrete behavioral examples with counterexamples, minimum 8-10 each |
| Application & Measurement | Page-type adaptation, voice consistency scoring criteria for D10 audit use |

## Modes

### Extract Mode
For clients with existing content (websites, marketing materials, social media). The agent analyzes content to score voice across all 15 dimensions, identifies brand archetypes from content patterns, and presents findings for validation.

### Generate Mode
For new brands or clients without existing content. The agent co-creates a voice through archetype identification, dimension-by-dimension exploration using POINTED questions, and iterative sample content generation.

The agent detects the appropriate mode from available inputs but always confirms with the operator.

## Methodology

### 15-Dimension Voice Framework
Every voice profile scores the brand across 15 dimensions organized into four layers:
- **Foundation** (1-5): Core attributes, formality, language style, perspective, emotional quality
- **Expression** (6-8): Pacing, storytelling approach, rhetorical devices
- **Context** (9-12): Channel adaptation, cultural adaptation, inclusivity, crisis handling
- **Strategic** (13-15): Content principles, market positioning, voice evolution

### Brand Archetypes
12 archetypes (Creator, Everyman, Sage, Explorer, Hero, Caregiver, Jester, Ruler, Magician, Rebel, Lover, Innocent) identified as a weighted mix that shapes voice decisions across all dimensions.

### POINTED Questions
Targeted extraction questions that produce specific, actionable insights instead of generic platitudes. Organized by dimension with variants for Extract and Generate modes.

### Anti-Boring Standards
Built-in boring detector that checks for generic openings, corporate buzzwords, predictable structures, and requires freshness elements in all content.

## Reference Files

| File | Purpose |
|------|---------|
| `references/voice-dimensions-framework.md` | Full 15-dimension framework with scoring scales and scorecard template |
| `references/brand-archetypes.md` | 12 archetypes with voice characteristics, combinations, and dimension mapping |
| `references/extraction-questions.md` | POINTED questions organized by dimension (~80 questions) |
| `references/channel-adaptation-template.md` | Channel tone mapping template with shift notation |

## Usage

Start the brand voice creator agent in a Cowork session with the project folder as the working directory. The agent will:

1. Load D1: Project Brief (required)
2. Detect whether Extract or Generate mode is appropriate
3. Walk through the voice creation process interactively across all 15 dimensions
4. Identify brand archetype mix
5. Define channel adaptation map
6. Apply anti-boring standards to all sample content
7. Present a draft D2 for review and iteration
8. Write the approved profile to `brand/D2-brand-voice-profile.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| D2 | Brand Voice Profile | `brand/D2-brand-voice-profile.md` | Output |

## Part of the Webtools Suite

This plugin is part of the webtools website creation pipeline:

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** (this plugin) -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing
