---
name: client-intelligence
description: "Build a comprehensive client profile from online research and registry data. Invoke when the user says 'research the client', 'client intelligence', 'run phase 2', 'client profile', 'who is this client', or after INIT phase is complete."
allowed-tools: Read, Write, Glob, WebSearch, Task, AskUserQuestion
version: 1.0.0
---

# Client Intelligence

Build a comprehensive profile of the client's current state. Pure discovery — no analysis, no gap identification, no recommendations. Branches on `build_type` from INIT.

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

Parse `D1-Init.json` notes for client profile information: industry, business model, team size, markets, founding date, description. Populate profile fields from what is available. Leave unknown fields as `null`.

### Step 4N: Registry lookup

1. Determine the **legal entity name**. This is often different from the brand (e.g., hotel "Dubna Skala" operated by "ABC s.r.o."). Check D1-Init.json notes first. If not found, ask the operator.
2. Determine country from `D1-Init.json` → `project.location.primary`.
3. **Slovak company** → WebSearch: `site:finstat.sk "[legal entity name]"`. If match found, fetch the result page.
4. **Other countries** → WebSearch: `site:dnb.com "[legal entity name]"` (or relevant local D&B domain). If match found, fetch.
5. Extract: legal name, registration ID, founded year, legal form, revenue range, employee count, registered address.
6. If no match, note "No business registry data available" and continue.

### Step 5N: Set presence_status

Set `presence_status` to `none`. All web/social/reputation fields remain `null`.

→ Go to **Step 6: Write output**.

---

## Redesign Path

### Step 3R: Website crawl

Use `dispatch-subagent` to dispatch `web-crawler`. Get URL from D1-Init.json notes or ask operator.

1. Crawl homepage. Output instructions: "Return extended summary with key facts. Telegraphic, no prose."
2. From homepage content, identify 3–10 high-value pages (about, services, products, team, portfolio, contact, pricing).
3. Dispatch web-crawler for each high-value page (parallel where possible).
4. Extract: site structure, navigation, messaging, tone of voice, CTA patterns, content presence (frequency, topics).

### Step 4R: Web search + social + reputation

**Web search** — primary language (all queries) + secondary languages (first 2 queries). Natural phrasing per language, not literal translation.

- `"[company name]"`
- `"[company name] [reviews]"` (localized: "recenzie", "Bewertungen", etc.)
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

Same process as Step 4N above. Identical registry lookup regardless of build_type.

### Step 6R: Assess presence_status

- `partial` — some data gathered but significant gaps remain
- `full` — comprehensive data across web, social, reputation, and registry

→ Go to **Step 6: Write output**.

---

## Step 6: Write D2-Client-Intelligence.json

Write `D2-Client-Intelligence.json` to the project root as **minified JSON** (no whitespace).

Use the schema from `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md` § JSON Schema.

All blocks are **always present** regardless of build_type. Fields with no data are `null`. This keeps the schema consistent for all downstream agents.

Extract key findings and strategic signals into the `notes` array.

## Step 7: Write D2-Client-Intelligence.md

Generate from `D2-Client-Intelligence.json` using the template in `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md` § Markdown Template.

The markdown tells a story — the Overview section is a 2–3 sentence narrative paragraph describing who the client is, what they do, and their current situation. Not a data dump.

Sections where all fields are `null` get a one-line note (e.g., "No web presence data — new build") instead of listing null values.

## Step 8: Update project-state.md

Update Phase 2 row: Status → `complete`, Output → `D2-Client-Intelligence.json`, Updated → today's date.

Do not modify any other rows.

Display summary:

```
Client Intelligence complete.

  Client: {client name}
  Build type: {new | redesign}
  Web presence: {summary — e.g., "existing site at domain.com" or "no current site"}
  Phase 2 status: complete

Next step: Run project-research.
```

---

## Rules

<critical>
- **NEVER** skip research for redesign builds — the research-first approach is core
- **NEVER** invent findings or fabricate data points
- **NEVER** write output without completing all prior steps
- **NEVER** modify project-state.md beyond the Phase 2 row
- **ALWAYS** keep all JSON blocks present regardless of build_type (null for missing)
- **ALWAYS** write JSON as minified
- **ALWAYS** generate markdown from JSON, not independently
</critical>

- If web-crawler fails on a page, note the failure and continue with available data
- If WebSearch returns no results, note and continue
- If registry lookup finds nothing, note "No business registry data available" and continue — registry is supplementary
- If fewer than 3 profile fields can be populated, warn operator and ask whether to proceed or provide additional context

## Sub-agents

- `web-crawler` (via dispatch-subagent, model: sonnet) — crawl client website pages (redesign path only)

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/skills/client-intelligence/references/templates.md` — JSON schema, markdown template
