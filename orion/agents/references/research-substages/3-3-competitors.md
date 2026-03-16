# Substage 3.3 — Competitor Landscape

**Code:** R3
**Slug:** Competitors
**Output:** `research/R3-Competitors.json`, `research/R3-Competitors.md`
**Dependencies:** R1-SERP, R2-Keywords
**Reads from:** `D1-Init.json`, `R1-SERP.json`, `R2-Keywords.json`
**MCP tools:** DataForSEO (optional), web-crawler (required), WebSearch (required)

---

## Purpose

Consolidate competitor signals from R1-SERP and R2-Keywords into a finalised competitor list (capped at `research_config.competitors_max`). Build a structured intelligence profile for each — who they are, what they do, how they're doing. The competitor list is locked at the end of this substage. No new competitors are added after R3.

Every subsequent substage uses this finalised list as its reference. The `rank` field determines which competitors receive deeper analysis later.

---

## Data Sources

From `D1-Init.json`:
- `project.languages` — primary + additional languages
- `project.location` — primary + additional markets
- `notes` — client-provided competitor URLs

From `R1-SERP.json`:
- `competitors` — commercial competitor domain list with keyword appearance counts

From `R2-Keywords.json`:
- `gap_analysis.keywords_not_targeted` — domains owning keywords the client doesn't target
- Enriched competitor signals from R2 domain intersection and competitor discovery steps

---

## Methodology

### Step 1: Competitor list consolidation

Merge competitor signals from three sources:
- INIT notes — any competitor URLs provided directly by the operator
- R1-SERP results — commercial domains appearing in organic results
- R2-Keywords gap analysis — domains owning keywords the client doesn't target

Deduplicate. Each domain gets a combined `keyword_appearances` score. Rank by score and trim to `research_config.competitors_max` (default: 5).

### Step 2: Competitor profiling

For each competitor in the locked list, perform a surface intelligence scan:

**Website scrape** — dispatch `web-crawler` sub-agent for each competitor homepage. Extract: structure, messaging, tone of voice, CTAs, content presence.

**Social presence** — use WebSearch to find active social profiles. Note which platforms are active and posting activity level.

**Reputation surface scan** — use WebSearch for Google rating, review count, notable mentions.

**Market and language footprint** — which markets and languages they operate in, based on website language versions and content.

**SERP context** — from R1-SERP data, which language x location combinations they appeared in and how often.

### Step 3: Strengths and weaknesses assessment

Assess each competitor based on visible signals only — no deep analysis. Flag obvious strengths (strong content, clear positioning, high review count) and weaknesses (thin content, poor UX signals, weak social presence, missing markets).

### Step 4: Gap analysis

Compare client against the competitor set as a whole. Each gap is one line: what's weak + why it matters. Do not restate per-competitor findings — synthesise across sites.

- Gaps — what competitors collectively do well that the client doesn't, market/language coverage gaps, positioning angles no one owns
- Opportunities — concrete actions for the client to differentiate

---

## Output

Write output using the templates at `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/templates/R3-Competitors-template.md`.

---

## What passes to the next substage

`research/R3-Competitors.json` — this is the reference file for all substages R4 through R9. Contains the finalised competitor list with ranks, market/language footprints, and baseline profiles. R5-Technology, R6-Reputation use ranks 1–3 (`basic`; all locked competitors when `deep`). R8-UX uses all locked competitors regardless of depth.

**The competitor list is now locked. No new competitors are added after this point.**
