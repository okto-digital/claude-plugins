# webtools-intake

Client intake and project brief creation for the webtools website pipeline.

## Overview

This plugin handles the discovery phase of the webtools pipeline. The brief-generator agent acts as a **live meeting companion** -- running during client meetings, processing input in real-time, suggesting questions progressively, and proposing solutions with confidence levels. It operates across four explicit modes: PREP, MEETING, REVIEW, and BRIEF.

Operators navigate the intake workflow through **phase commands** -- each command enters a specific mode of the brief-generator agent, carries forward state from prior phases, and suggests the next step on completion.

## Components

| Type | Name | Description |
|------|------|-------------|
| Command | `/webtools-intake` | Orientation: show available workflows and current project state |
| Command | `/webtools-intake-questionnaire` | Generate tailored client intake questionnaire (D11) |
| Command | `/webtools-intake-prep` | Analyze pre-existing data, produce interview guide (PREP mode) |
| Command | `/webtools-intake-meeting` | Live meeting companion with submarine mode (MEETING mode) |
| Command | `/webtools-intake-review` | Post-meeting gap analysis and inference review (REVIEW mode) |
| Command | `/webtools-intake-brief` | Generate D1: Project Brief (BRIEF mode) |
| Agent | `brief-generator` | Live meeting companion with 4-mode brief creation workflow |

## Workflow

```
PREP  -->  MEETING  -->  REVIEW  -->  BRIEF
```

### 1. PREP Mode (before meeting)

Load any available client data (external inquiry form answers, prior correspondence) and score it against all domain checklists. The agent produces a PREP Report: what is already covered, remaining CRITICAL gaps, and a recommended conversation flow with time estimates.

```
Operator: /webtools-intake-prep
Operator: [pastes inquiry form answers]
Agent: PREP Report with interview guide
Agent: Suggests /webtools-intake-meeting
```

### 2. MEETING Mode (during meeting)

The agent runs as a "submarine" -- processing every message silently, surfacing only when valuable. The operator types meeting notes in real time. The agent acknowledges briefly (1-4 lines), maps input to domain checkpoints, and updates coverage tracking.

Questions are disclosed progressively: **3 at a time**, only when the operator asks. The agent never dumps all gaps at once.

```
Operator: Client wants an online store, ~200 products, B2B model
Agent: [1-line ack] + [proactive: E-commerce, B2B inferences activated]
Operator: ?
Agent: [3 prioritized questions for the active topic]
```

**Operator commands in MEETING mode:**

| Command | Action |
|---------|--------|
| `?` or `suggest` | Show next 3 suggested questions for the active topic |
| `more` | Show 3 more questions (continues the queue) |
| `next topic` | Suggest the next conversation topic with CRITICAL count and time estimate |
| `status` | Show coverage dashboard with topic progress bars |
| `solution [topic]` | Show proposed solutions and inferences for a topic |
| `flag [note]` | Save a note for REVIEW mode (contradiction, concern, special request) |
| `skip [domain]` | Mark a conditional domain as not applicable |
| `back to [topic]` | Switch suggestion context to a different topic |
| `pause` | Stop all proactive communication (silent processing continues) |
| `resume` | Resume proactive alerts and show catch-up summary |
| `done` / `wrap up` | End meeting, save state, suggest `/webtools-intake-review` |

### 3. REVIEW Mode (after meeting)

Three-part review with the operator:

1. **Meeting Summary** -- Topics covered, key decisions, data points captured
2. **Inference Confirmation** -- HIGH/MEDIUM/LOW inferences grouped for batch review
3. **Gap Report** -- Remaining CRITICAL and IMPORTANT items with resolution options

The agent then generates **D13: Client Follow-Up Questionnaire** for any unresolved gaps.

### 4. BRIEF Mode (document generation)

Compile all sources (inquiry form + meeting data + confirmed inferences + D13 answers) into a complete D1: Project Brief. Each section carries a confidence tag (Solid / Thin / Assumed / Missing). Iterate with the operator until approved.

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

Enter PREP mode. Analyze pre-existing client data (inquiry forms, D11 answers, notes, URLs), score against domain checkpoints, run inference engine, and produce a PREP Report with an interview guide.

**Input:** Any format -- inquiry form answers, D11 responses, meeting notes, emails, URLs.
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

Enter BRIEF mode. Generate D1: Project Brief from all accumulated data. Checks prerequisites, drafts section-by-section with confidence tags (Solid / Thin / Assumed / Missing), iterates until approved.

**Output:** `brief/D1-project-brief.md`, registry update, downstream notification. Session state saved to `brief/intake-session.md`.

### Session State

Phase commands persist state across conversations via `brief/intake-session.md`. Each phase reads accumulated state from prior phases and writes updated state on completion. This enables workflows that span multiple sessions:

```
Session 1: /webtools-intake-prep -> state saved
Session 2: /webtools-intake-meeting -> loads PREP state, saves MEETING state
Session 3: /webtools-intake-review -> loads all state, saves REVIEW state
Session 4: /webtools-intake-brief -> loads all state, generates D1
```

## Agents

### brief-generator

Live meeting companion that processes client input in real-time and synthesizes it into a comprehensive D1: Project Brief through four structured modes.

Accepts input in any format: meeting notes, questionnaire answers, URLs, bullet points, emails, voice transcriptions, or stream-of-consciousness text. The agent maps all input to domain checkpoints, derives inferences with confidence levels, and tracks coverage across 9 conversation topics.

**Output:** `brief/D1-project-brief.md` and `brief/D13-client-followup.md`

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
| D11 | Client Questionnaire | `brief/D11-client-questionnaire.md` | `/webtools-intake-questionnaire` command |
| D13 | Client Follow-Up Questionnaire | `brief/D13-client-followup.md` | `brief-generator` (REVIEW mode) |
| D1 | Project Brief | `brief/D1-project-brief.md` | `brief-generator` (BRIEF mode) |

D13 is always generated after the meeting (even for minimal gaps) to maintain a consistent project paper trail. It contains only CRITICAL and IMPORTANT gaps, written in client-friendly language, grouped by conversation topic. Each question includes meeting context and suggested answers where possible.

## Reference Files

### Conversation and Inference References

| File | Purpose |
|---|---|
| `references/topic-mapping.md` | Maps 21 domains to 9 conversation topics, default flow order, conditional extensions |
| `references/inference-rules.md` | Codified inference patterns with trigger conditions, confidence levels, covered checkpoints |
| `references/d13-template.md` | D13 format spec, question formatting rules, client-friendly language principles |
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
