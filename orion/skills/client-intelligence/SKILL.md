---
name: client-intelligence
description: "Build a client profile from online research and registry data. Invoke when the user says 'research the client', 'client intelligence', 'run phase 2', 'client profile', 'who is this client', or after INIT phase is complete."
allowed-tools: Read, Write, Bash, Glob, WebSearch, Task, AskUserQuestion
version: 3.0.0
---

# Client Intelligence

Build a profile of the client's current state through online research. Pure discovery — no analysis, no recommendations.

Read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`. Apply throughout.

## Minimum Scope

Cover at least these domains. You may go beyond them if evidence warrants it.

- Identity & positioning
- Products & services
- Business model
- Target audience
- Market position
- Geographic & language footprint
- Digital presence
- Content & communication
- Reputation & trust
- Social presence
- Commercial performance signals
- Legal & compliance
- Certifications & memberships
- Technology footprint
- Partnerships & ecosystem
- Goals & constraints
- Red flags

## Tooling

Use `build_type` from project.json and the information available to decide which tools apply. A redesign with an existing URL opens up scraping and DataForSEO. A new build without a URL relies on registries, search, and operator input. Use what makes sense — skip what doesn't apply.

### Registries & structured data

For commercial performance, legal, certifications and entity data. Direct lookups by entity name — structured, reliable, low noise.
Determine the **legal entity name** first (often different from brand). Check project.json notes. If not found, ask the operator.
Find the **national business registries** for the client's country. Example for Slovakia: `orsr.sk` (company register), `zrsr.sk` (trade licences), `finstat.sk` (financial data). For international fallback: `dnb.com`.

### DataForSEO endpoints

For digital presence, technology footprint and reputation signals. Use `dispatch-subagent` to dispatch `dataforseo`.

- `/seo dataforseo tech <domain>` — technology stack
- `/seo dataforseo whois <domain>` — domain registration, ownership, age
- `/seo dataforseo onpage <url>` — surface scan of existing site
- `/seo dataforseo top-searches <domain>` — what people search in relation to this domain
- `/seo dataforseo listings <keyword>` — business listings, Google Business profile signals
- `/seo dataforseo ranked <domain>` — current keyword rankings (if site exists)
- `/seo dataforseo backlinks <domain>` — who links to them, from where

### Web scraping & fetching

For identity, positioning, content, communication, social and trust signals. Use `dispatch-subagent` to dispatch `web-crawler`.

- Direct website scrape — homepage, about, services/products, contact, pricing, team, portfolio
- Social platform profiles — LinkedIn, Instagram, Facebook, TikTok, YouTube (public data)
- Google Business profile — rating, review count, category, photos
- Review platforms — Google Reviews, Trustpilot, industry-specific platforms
- Press and media mentions — news search for brand name

### Web search

For reputation, certifications, partnerships, press coverage and anything not found via direct lookup. Search in the client's primary language first, then broader. Combine brand name with domain-specific terms: reviews, certifications, memberships, partnerships, awards, news.

### Human input only

Some domains cannot be fully researched externally:

- Goals & constraints — from INIT notes and gap analysis answers only
- Business model details — partially inferable, confirmed only by client
- Target audience intent — inferable from notes, confirmed in gap analysis

If you need more sources or input data, ask the operator.

---

## Step 1: Load project context

Read `project-state.md`. Verify Phase 1 (INIT) is `complete`. If not, stop: "Run project-init first."
Read `project.json`. Extract: `build_type`, client name, URL, location, languages, notes.
Read `baseline-log.txt`.

If `D2-Client-Intelligence.txt` already exists, warn: "Phase 2 output already exists. Overwrite?" If declined, stop.

## Step 2: Research

Work through the minimum scope domains using the tooling above. Adapt to what's available — a new build with no URL skips scraping and DataForSEO site tools. A redesign uses everything.

Extract **services or products** — every distinct service/product the client offers. This list drives SERP keyword generation in Phase 3.

Flag **red flags** — hidden content, deceptive practices, grey-zone activities, adult/illegal content, cloaked links, keyword stuffing, anything that could pose reputational or legal risk for the agency. Each flag needs: what it is, how severe, where you found it.

## Step 3: Write D2-Client-Intelligence.txt

Free-form TXT — scannable, source-tagged, the agent decides what structure serves this client best. Source-tag every finding per `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` § Source Binding.

Red flags (if any) should be clearly surfaced — these are escalation-level findings that affect whether the agency takes the project.

## Step 4: Append to baseline-log.txt

Read existing entries first — do NOT re-log findings from `[INIT]`. Accumulate all entries, then append in one batch using Bash:

```bash
cat >> baseline-log.txt << 'BASELINE'
================================================================================
[D2] CLIENT INTELLIGENCE — D2-Client-Intelligence.txt
================================================================================
- Finding one.
- Finding two.
BASELINE
```

Follow the baseline-log rules in `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`. Only confirmed findings — no confidence tags, no inferred data.

## Step 5: Debug companion (when enabled)

If `debug` is `true` in project.json: write `tmp/debug/D2-Client-Intelligence-debug.txt` — data sources used, pages crawled, search queries run, no prose.

## Step 6: Update project-state.md

Update Phase 2 row: Status → `complete`, Output → `D2-Client-Intelligence.txt`, Updated → today's date. Do not modify any other rows.

Summarize what was gathered and suggest the next step (project-research).

---

## Rules

<critical>
- **NEVER** invent findings or fabricate data points — if you can't find it, report it as not found
- **NEVER** modify project-state.md beyond the Phase 2 row
</critical>

- If a tool fails or returns no results, note the failure and continue with available data
- If very little data can be gathered, warn operator and ask whether to proceed or provide additional context
- Do not make up information to fill gaps — gaps are valuable signals for downstream phases
