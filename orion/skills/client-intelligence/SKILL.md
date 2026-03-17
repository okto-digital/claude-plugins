---
name: client-intelligence
description: "Build a client profile from online research and registry data. Invoke when the user says 'research the client', 'client intelligence', 'run phase 2', 'client profile', 'who is this client', or after INIT phase is complete."
allowed-tools: Read, Write, Glob, WebSearch, Task, AskUserQuestion
version: 2.0.0
---

# Client Intelligence

Build a profile of the client's current state through online research. Pure discovery — no analysis, no recommendations. Branches on `build_type` from project.json.

Read `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` and apply it throughout.

---

## Step 1: Load project context

Read `project-state.md`. Verify Phase 1 (INIT) is `complete`. If not, stop: "Run project-init first."
Read `project.json`. Extract: `build_type`, client name, URL, location, languages, notes.
Read `baseline-log.txt`.

If `D2-Client-Intelligence.txt` already exists, warn: "Phase 2 output already exists. Overwrite?" If declined, stop.

## Step 2: Branch on build_type

- `new` → **New Build Path** (Steps 3N–4N)
- `redesign` → **Redesign Path** (Steps 3R–5R)

---

## New Build Path

### Step 3N: Extract from INIT notes + registry lookup

Parse project.json notes for client profile information. Then run the **Registry Lookup** (see below). For new builds, this is the primary data source — there's no website to crawl.

### Step 4N: Write output

→ Go to **Step 6: Write D2-Client-Intelligence.txt**.

---

## Redesign Path

### Step 3R: Website crawl

Use `dispatch-subagent` to dispatch `web-crawler`. Get URL from project.json.

1. Crawl homepage. Output instructions: "Return extended summary with key facts. Telegraphic, no prose."
2. From homepage content, identify 3-10 high-value pages (about, services, products, team, portfolio, contact, pricing).
3. Dispatch web-crawler for each high-value page (parallel where possible).
4. From crawled pages, extract what passes the four filters — focus on what changes downstream decisions about scope, positioning, or approach.
5. Extract **services or products** — every distinct service/product the client offers. This list drives SERP keyword generation in Phase 3.
6. Flag **red flags** — hidden content, deceptive practices, grey-zone activities, adult/illegal content, cloaked links, keyword stuffing, anything that could pose reputational or legal risk for the agency. Each flag needs: what it is, how severe, where you found it.

### Step 4R: Web search + social + reputation

**Web search** — primary language (all queries) + secondary languages (first 2 queries). Localize naturally.

- `"[company name]"`
- `"[company name] [reviews]"`
- `"[company name] [industry]"`
- `"[company name] [news] [current year]"`

**Social media:** Identify active platforms from website links and search results. Note activity level, engagement quality, sentiment.

**Reputation:** Google Business profile, industry review platforms, press coverage, awards and certifications.

### Step 5R: Registry lookup

Run the **Registry Lookup** (see below).

→ Go to **Step 6: Write D2-Client-Intelligence.txt**.

---

## Registry Lookup

Used by both paths.

1. Determine the **legal entity name** (often different from brand). Check project.json notes first. If not found, ask the operator.
2. Determine country from project.json → `project.location.primary`.
3. **Slovak company** → WebSearch: `site:finstat.sk "[legal entity name]"`. Fetch if match found.
4. **Other countries** → WebSearch: `site:dnb.com "[legal entity name]"`. Fetch if match found.
5. Extract: legal name, registration ID, founded year, legal form, revenue range, employee count, registered address.
6. If no match, note "No business registry data available" and continue.

---

## Step 6: Write D2-Client-Intelligence.txt

Free-form TXT. Apply the decision framework — four filters, source binding, telegraphic style. The agent decides what structure serves this client best.

Source-tag everything: `[src: tool]` for crawled/searched data, `[src: registry]` for business registry, `[src: operator]` for notes, `[src: url]` for specific pages.

Red flags (if any) should be clearly surfaced — these are escalation-level findings that affect whether the agency takes the project.

## Step 7: Write baseline-log.txt

Append key findings tagged with `[D2]`. Apply the four filters — only findings that change what downstream agents need to know.

## Step 8: Debug companion (when enabled)

If `research_config.debug` is `true` in project.json: write `tmp/debug/D2-Client-Intelligence-debug.txt` — data sources used, pages crawled, search queries run, no prose.

## Step 9: Update project-state.md

Update Phase 2 row: Status → `complete`, Output → `D2-Client-Intelligence.txt`, Updated → today's date. Do not modify any other rows.

Summarize what was gathered and suggest the next step (project-research).

---

## Rules

<critical>
- **NEVER** skip research for redesign builds — the research-first approach is core
- **NEVER** invent findings or fabricate data points — report MISSING, don't guess
- **NEVER** modify project-state.md beyond the Phase 2 row
</critical>

- If web-crawler fails on a page, note the failure and continue with available data
- If WebSearch returns no results, note and continue
- If registry lookup finds nothing, note and continue — registry is supplementary
- If very little data can be gathered, warn operator and ask whether to proceed or provide additional context

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` — shared decision framework
