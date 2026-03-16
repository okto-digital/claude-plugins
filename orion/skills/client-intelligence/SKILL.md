---
name: client-intelligence
description: "Build a comprehensive client profile from online research and registry data. Invoke when the user says 'research the client', 'client intelligence', 'run phase 2', 'client profile', 'who is this client', or after INIT phase is complete."
allowed-tools: Read, Write, Glob, WebSearch, Task, AskUserQuestion
version: 1.0.0
---

# Client Intelligence

## Mission

Build a comprehensive profile of the client's current state by filling the template in `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md`. The template is the source of truth for structure and fields.

Your job is to research and extract data that is:
- **Correct and verifiable** -- backed by numbers, statistics, and sources where possible
- **Concise but complete** -- no filler, but no gaps in what's available
- **Relevant to website discovery** -- every data point should inform website design, content strategy, or conversion optimization. Filter out noise that doesn't serve this purpose.

Pure discovery -- no analysis, no gap identification, no recommendations. Branches on `build_type` from INIT.

---

## Step 1: Load project context

Read `D1-Init.json`. Extract: `build_type`, client name, location, languages, notes.
If missing, stop: "Run project-init first."

Read `project-state.md`. Verify Phase 1 (INIT) is `complete`. If not, stop.

If `D2-Client-Intelligence.json` already exists, warn: "Phase 2 output already exists. Overwrite?" Use AskUserQuestion. If declined, stop.

## Step 2: Branch on build_type

- `new` → **New Build Path** (Steps 3N–5N)
- `redesign` → **Redesign Path** (Steps 3R–6R)

---

## New Build Path

### Step 3N: Extract from INIT notes

Parse `D1-Init.json` notes for client profile information: industry, business model, team size, markets, founding date, description, **services or products**. Populate fields from what is available. Leave unknown fields as `null`.

### Step 4N: Registry lookup

Run the **Registry Lookup** (see below).

### Step 5N: Set presence_status

Set `presence_status` to `none`. All web/social/reputation fields remain `null`.

→ Go to **Step 7: Write output**.

---

## Redesign Path

### Step 3R: Website crawl

Use `dispatch-subagent` to dispatch `web-crawler`. Get URL from D1-Init.json notes or ask operator.

1. Crawl homepage. Output instructions: "Return extended summary with key facts. Telegraphic, no prose."
2. From homepage content, identify 3–10 high-value pages (about, services, products, team, portfolio, contact, pricing).
3. Dispatch web-crawler for each high-value page (parallel where possible).
4. Extract: site structure, navigation, messaging, tone of voice, CTA patterns, content presence.
5. Extract **services or products** -- identify every distinct service/product the client offers. This list is critical for SERP keyword generation in the research stage.
6. Flag **dark patterns or red flags** -- hidden content (hidden divs, display:none text), deceptive practices, grey-zone activities, adult/illegal content, cloaked links, or anything that could pose reputational or legal risk for the agency taking on this client.

### Step 4R: Web search + social + reputation

**Web search** — primary language (all queries) + secondary languages (first 2 queries). Localize naturally.

- `"[company name]"`
- `"[company name] [reviews]"`
- `"[company name] [industry]"`
- `"[company name] [news] [current year]"`

**Social media discovery:**
- Identify active platforms from website links and search results
- Assess: posting frequency, consistency, engagement quality, sentiment
- Note which platforms are active vs dormant

**Reputation:**
- Google Business profile and rating
- Industry-specific review platforms
- Press coverage, interviews, podcast appearances
- Awards and certifications

### Step 5R: Registry lookup

Run the **Registry Lookup** (see below).

### Step 6R: Assess presence_status

- `partial` — some data gathered but significant gaps remain
- `full` — comprehensive data across web, social, reputation, and registry

→ Go to **Step 7: Write output**.

---

## Registry Lookup

Used by both paths (Step 4N and Step 5R).

1. Determine the **legal entity name** (often different from brand). Check D1-Init.json notes first. If not found, ask the operator.
2. Determine country from `D1-Init.json` → `project.location.primary`.
3. **Slovak company** → WebSearch: `site:finstat.sk "[legal entity name]"`. Fetch if match found.
4. **Other countries** → WebSearch: `site:dnb.com "[legal entity name]"`. Fetch if match found.
5. Extract: legal name, registration ID, founded year, legal form, revenue range, employee count, registered address.
6. If no match, note "No business registry data available" and continue.

---

## Step 7: Write D2-Client-Intelligence.json

Write `D2-Client-Intelligence.json` to the project root as **a single line** — no newlines, no indentation, no spaces after colons or commas.

Use the schema from `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md` § JSON Schema.

All blocks are always present regardless of build_type. Fields with no data are `null`.

## Step 8: Write D2-Client-Intelligence.md

Generate from `D2-Client-Intelligence.json` using the markdown template in `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md`.

## Step 9: Debug companion (when enabled)

If `research_config.debug` is `true` in D1-Init.json: write `tmp/debug/D2-Client-Intelligence-debug.txt` — telegraphic bullet points, key facts only, data sources used, no prose, no template structure.

## Step 10: Update project-state.md

Update Phase 2 row: Status → `complete`, Output → `D2-Client-Intelligence.json`, Updated → today's date.

Do not modify any other rows.

Summarize what was gathered and suggest the next step (project-research).

---

## Rules

<critical>
- **NEVER** skip research for redesign builds — the research-first approach is core
- **NEVER** invent findings or fabricate data points
- **NEVER** write output without completing all prior steps
- **NEVER** modify project-state.md beyond the Phase 2 row
- **ALWAYS** keep all JSON blocks present regardless of build_type (null for missing)
- **ALWAYS** write JSON as a single line (no newlines, no indentation)
- **ALWAYS** generate markdown from JSON, not independently
</critical>

- If web-crawler fails on a page, note the failure and continue with available data
- If WebSearch returns no results, note and continue
- If registry lookup finds nothing, note "No business registry data available" and continue — registry is supplementary
- If fewer than 3 profile fields can be populated, warn operator and ask whether to proceed or provide additional context
