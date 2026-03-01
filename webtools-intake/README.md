# webtools-intake

Client intake, research, and project brief creation for the webtools website pipeline.

## Overview

This plugin handles the discovery phase of the webtools pipeline. It researches client companies (web search, website crawling, business registry), generates tailored questionnaires, and processes client input in real-time across four modes (PREP, MEETING, REVIEW, BRIEF) with progressive questioning, confidence-scored solutions, and structured project brief output.

**v3.2.0 changes:** PREP now orchestrates research inline -- directly dispatches web-crawler sub-agents and uses WebSearch, eliminating the client-researcher skill (three-level nesting reduced to two). D14 condensed to telegraphic format (12K chars raw, 5.4-6K compressed). Website crawling delegated to webtools-crawler's web-crawler agent. D14 and D1 use the `.raw.md` compression pattern via webtools-init's document-compressor agent.

## Recommended Workflow

```
1. PREP  ->  /webtools-intake-prep [url]
   - If D14 missing: runs inline research phase
     (web search, website crawl via web-crawler, business registry -> D14)
   - If D14 exists: loads it directly
   - Analyzes findings by topic, produces interview guide

2. QUESTIONNAIRE or MEETING  (branching or sequential)
   - /webtools-intake-questionnaire   Generate D11
   - /webtools-intake-meeting         Submarine model, live capture

3. REVIEW + FOLLOW-UP
   - /webtools-intake-review          Summary, inference confirmation, gap report
   - Generates D13 if gaps remain

4. BRIEF
   - /webtools-intake-brief           Compile D1
   - Save D1.raw.md -> compress to D1.md
```

## Components

| Type | Name | Description |
|------|------|-------------|
| Command | `/webtools-intake` | Orientation: show available workflows and current project state |
| Command | `/webtools-intake-prep` | Research client + produce interview guide (auto-researches if no D14) |
| Command | `/webtools-intake-questionnaire` | Generate tailored client intake questionnaire (D11) |
| Command | `/webtools-intake-meeting` | Live meeting companion with submarine mode (MEETING mode) |
| Command | `/webtools-intake-review` | Post-meeting gap analysis and inference review (REVIEW mode) |
| Command | `/webtools-intake-brief` | Generate D1: Project Brief (BRIEF mode) |
| Agent | `brief-generator` | Live meeting companion with 4-mode brief creation workflow |

## Commands

All commands follow the `webtools-{plugin}-{action}` naming convention. See `references/naming-convention.md` for the full convention and rationale.

### /webtools-intake

Show available intake workflows, current project state, and suggested next step. Read-only orientation command.

### /webtools-intake-questionnaire

Generate a tailored client intake questionnaire.

```
/webtools-intake-questionnaire new-build restaurant
/webtools-intake-questionnaire redesign saas
/webtools-intake-questionnaire landing-page
/webtools-intake-questionnaire ecommerce retail
```

**Arguments:**
- `$1` -- Project type (required): `new-build`, `redesign`, `landing-page`, `ecommerce`
- `$2` -- Industry (optional): freeform text for industry-specific questions

**Output:** `brief/D11-client-questionnaire.md`

The questionnaire includes three sections:
- **Section A:** Universal questions (all project types)
- **Section B:** Project-type-specific questions
- **Section C:** Industry-specific questions (only if industry provided)

### /webtools-intake-prep

The primary entry point for meeting preparation. If D14 exists, loads it and produces an interview guide. If D14 does not exist, runs an inline research phase -- directly uses WebSearch for external intelligence and dispatches web-crawler sub-agents for URL crawling (website pages, business registries) -- then synthesizes D14 and produces the interview guide. Also accepts manual data input (inquiry forms, emails, notes) when no URL is available.

```
/webtools-intake-prep https://example.com
/webtools-intake-prep
```

**Arguments:**
- `$1` -- Client website URL (optional). If D14 is missing and no URL provided, PREP will ask for a URL or manual data.

**Flow (D14 missing + URL):** Inline research (WebSearch + web-crawler agents) -> D14 (.raw.md + compressed) -> topic analysis -> interview guide
**Flow (D14 exists):** Load D14 -> topic analysis -> interview guide
**Flow (manual data):** Accept input -> topic analysis -> interview guide

**Output:** PREP Report with interview guide. Session state saved to `brief/intake-session.md`.
**Next:** `/webtools-intake-meeting`

### /webtools-intake-meeting

Enter MEETING mode. Live meeting companion using the submarine model -- silent processing, brief acknowledgments (1-4 lines), progressive question disclosure only when asked.

**Inline commands:** `?`, `more`, `next topic`, `status`, `solution [topic]`, `flag [note]`, `pause`, `resume`, `skip [domain]`, `back to [topic]`
**End meeting:** `done` or `wrap up`
**Output:** Ongoing companion. Session state saved to `brief/intake-session.md`.
**Next:** `/webtools-intake-review`

### /webtools-intake-review

Enter REVIEW mode. Post-meeting 3-part review: Meeting Summary, Inference Confirmation (batch Y/N), Gap Report. Optionally generates D13: Client Follow-Up Questionnaire.

**Output:** Review analysis, optional `brief/D13-client-followup.md`. Session state saved to `brief/intake-session.md`.
**Next:** `/webtools-intake-brief`

### /webtools-intake-brief

Enter BRIEF mode. Generate D1: Project Brief from all accumulated data. Checks prerequisites, drafts section-by-section with confidence tags (Solid / Thin / Assumed / Missing), iterates until approved. D1 is saved as `.raw.md` first, then compressed.

**Output:** `brief/D1-project-brief.md` (compressed), `brief/D1-project-brief.raw.md` (original), registry update, downstream notification. Session state saved to `brief/intake-session.md`.

### Session State

Phase commands persist state across conversations via `brief/intake-session.md`. Each phase reads accumulated state from prior phases and writes updated state on completion. This enables workflows that span multiple sessions:

```
Session 1: /webtools-intake-prep [url] -> inline research + state saved (PREP)
Session 2: /webtools-intake-meeting -> loads PREP state, saves MEETING state
Session 3: /webtools-intake-review -> loads all state, saves REVIEW state
Session 4: /webtools-intake-brief -> loads all state, generates D1
```

## Agents

### brief-generator

Live meeting companion that processes client input in real-time and synthesizes it into a comprehensive D1: Project Brief through four structured modes.

Accepts input in any format: meeting notes, questionnaire answers, URLs, bullet points, emails, voice transcriptions, or stream-of-consciousness text. The agent maps all input to domain checkpoints, derives inferences with confidence levels, and tracks coverage across 9 conversation topics.

**Output:** `brief/D1-project-brief.md` (compressed), `brief/D1-project-brief.raw.md` (original), and `brief/D13-client-followup.md`

#### Conversation Topics

Instead of exposing 21 technical domains directly, the agent groups them into 9 conversation topics matching natural meeting flow:

| # | Topic | What It Covers |
|---|---|---|
| 1 | The Business | Identity, offering, competitors, differentiators |
| 2 | The Audience | Who visits, what they need, how they find the business |
| 3 | Goals and Success | Website purpose, KPIs, budget, timeline |
| 4 | The Website Vision | Pages, navigation, content, messaging |
| 5 | Look and Feel | Brand identity, visual style, imagery |
| 6 | Technical Foundation | Platform, hosting, integrations, compliance |
| 7 | Lead Capture and Conversion | Forms, CTAs, lead flows, conversion tracking |
| 8 | Findability | SEO, local search, accessibility |
| 9 | After Launch | Maintenance, content updates, support |

**Conditional extensions** activate when relevant: Online Store, Content Publishing, Multiple Languages, Member Access, Moving From Current Site, Bookings and Appointments.

#### Inference Engine

As information arrives, the agent continuously derives conclusions using codified rules:

| Confidence | Meaning | Action |
|---|---|---|
| HIGH | Near-certainty (universal standard, legal requirement, direct implication) | Auto-include, surface immediately |
| MEDIUM | Reasonable and likely correct (strong convention, multiple indirect signals) | Queue for REVIEW confirmation |
| LOW | Could go either way (single data point, subjective preference) | Generate question for D13 |

Inference types include: universal safe defaults, geographic rules, business model patterns, project type defaults, industry conventions, cross-domain implications, and negative inferences (meaningful absence of information).

#### Domain Validation

The brief-generator validates information against comprehensive domain checklists stored in `references/domains/`. Each domain covers an area of website development expertise with checkpoints tagged by priority (CRITICAL / IMPORTANT / NICE-TO-HAVE).

Each domain file includes a **"What to look for"** reasoning summary -- 5 conceptual themes that give the agent analytical context beyond the individual checkpoints. These describe what the agent should be thinking about (e.g., "Whether the client's design expectations match their budget") rather than repeating specific questions.

- **15 universal domains** -- always evaluated regardless of project type
- **6 conditional domains** -- evaluated only when relevant (e.g., e-commerce, multilingual)

#### Open Reasoning

The domain checklists are a floor, not a ceiling. When the conversation reveals topics no checkpoint covers -- a complex approval workflow, an unusual integration, industry-specific nuances -- the agent generates new questions beyond the checklists.

Open-reasoning questions follow the same formulation rules as checkpoint questions and are tagged `[OPEN]` in suggestion batches so the operator can distinguish them from checklist-driven questions. At most 1 open-reasoning question appears per suggestion batch of 3. In REVIEW mode, all open-reasoning data points are listed in a separate "Additional Findings" section.

#### Voice Transcription (future extension)

The agent accommodates Whisper or similar voice-to-text integration. Transcribed messages are prefixed with `[T]` to distinguish client speech from operator instructions. No structural changes are needed -- the existing input pipeline handles high-frequency transcription chunks.

## Documents Produced

| Doc ID | Document | File Path | Generated By |
|--------|----------|-----------|--------------|
| D14 | Client Research Profile | `brief/D14-client-research-profile.md` (.raw.md + compressed) | `/webtools-intake-prep` (inline research phase) |
| D11 | Client Questionnaire | `brief/D11-client-questionnaire.md` | `/webtools-intake-questionnaire` command |
| D13 | Client Follow-Up Questionnaire | `brief/D13-client-followup.md` | `brief-generator` (REVIEW mode) |
| D1 | Project Brief | `brief/D1-project-brief.md` (.raw.md + compressed) | `brief-generator` (BRIEF mode) |

D14 and D1 use the `.raw.md` compression pattern: the original is saved as `.raw.md`, then compressed via webtools-init's document-compressor agent to the standard `.md` path. Downstream tools consume the compressed version.

D13 is always generated after the meeting (even for minimal gaps) to maintain a consistent project paper trail. It contains only CRITICAL and IMPORTANT gaps, written in client-friendly language, grouped by conversation topic. Each question includes meeting context and suggested answers where possible.

## Dependencies

- **webtools-crawler** -- Required for web-crawler agent (website crawling). Invoked via the Task tool from PREP's inline research phase.
- **webtools-init** -- Required for document-compressor agent (D14/D1 compression). Invoked via the Task tool from PREP and BRIEF mode.

## Reference Files

### Conversation and Inference References

| File | Purpose |
|---|---|
| `references/topic-mapping.md` | Maps 21 domains to 9 conversation topics, default flow order, conditional extensions |
| `references/inference-rules.md` | Codified inference patterns with trigger conditions, confidence levels, covered checkpoints |
| `references/d13-template.md` | D13 format spec, question formatting rules, client-friendly language principles |
| `references/d14-template.md` | D14 format spec with 9 sections including External Intelligence (used by PREP inline research) |
| `references/questioning-strategy.md` | Question formulation rules and QBQ awareness |
| `references/naming-convention.md` | `webtools-{plugin}-{action}` command naming convention for the suite |

### Domain Checklists

Located in `references/domains/`. Used by the brief-generator for gap analysis and checkpoint scoring.

#### Universal Domains (always evaluated)

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

#### Conditional Domains (evaluated when applicable)

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

1. **webtools-init** -- Project setup, management, and utility agents (document-compressor)
1b. **webtools-crawler** -- Unified web crawling with 7-method cascade
2. **webtools-intake** (this plugin) -- Client research, questionnaire, and brief generation
3. **webtools-research** -- Multi-topic research with parallel agent dispatch
4. **webtools-brand** -- Brand voice profiling
5. **webtools-seo** -- SEO keyword research
6. **webtools-competitors** -- Competitor site analysis
7. **webtools-inventory** -- Content inventory and migration
8. **webtools-architecture** -- Site structure planning
9. **webtools-blueprint** -- Page blueprint generation
10. **webtools-writer** -- Content and microcopy generation
11. **webtools-audit** -- Content quality auditing
