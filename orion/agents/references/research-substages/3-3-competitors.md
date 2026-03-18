# Substage 3.3 — Competitor Landscape

**Code:** R3
**Slug:** Competitors
**Output:** `research/R3-Competitors.txt`
**Hypothesis:** Competitors have stronger web presence and working conversion paths
**Dependencies:** R1-SERP, R2-Keywords
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`, `research/R2-Keywords.txt`
**MCP tools:** DataForSEO (optional), web-crawler (required), WebSearch (required)

---

## Purpose

Consolidate competitor signals from R1-SERP and R2-Keywords into a finalised competitor list (capped at `research_config.competitors_max`). Build a structured intelligence profile for each — who they are, what they do, how they're doing. The competitor list is locked at the end of this substage. No new competitors are added after R3.

Every subsequent substage uses this finalised list as its reference. The `rank` field determines which competitors receive deeper analysis later.

---

## Data Sources

From `project.json`: languages, location, notes (client-provided competitor URLs).
From `baseline-log.txt`: mission, all prior findings including R1 and R2 highlights.
From `research/R1-SERP.txt`: commercial competitor domains from organic results, keyword appearance counts, scope.
From `research/R2-Keywords.txt`: domains owning keywords the client doesn't target, enriched competitor signals from domain intersection and competitor discovery.

---

## Methodology

### Step 1: Competitor list consolidation

Merge competitor signals from three sources:
- INIT notes — any competitor URLs provided directly by the operator
- R1-SERP results — commercial domains appearing in organic results
- R2-Keywords gap analysis — domains owning keywords the client doesn't target

Deduplicate. Rank by relevance, not raw frequency:
- **Local competitors first** — domains with `scope: local` or `scope: both` from R1 are the client's direct market rivals. Weight `local_appearances` higher than general `keyword_appearances`.
- **Favour local representation** — a national directory appearing in 20 keywords is less relevant than a local business appearing in 3 location keywords.
- **Break ties by keyword gap ownership** — competitors from R2 gap analysis (domains owning keywords the client doesn't target) get a boost.

Trim to `research_config.competitors_max` (default: 5).

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

Compare client against the competitor set as a whole. Synthesise across sites — don't restate per-competitor findings. Surface gaps (what competitors do well that the client doesn't), coverage gaps (markets, languages), and differentiation opportunities.

---

## Output

Write `research/R3-Competitors.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R3]`.

This is the reference file for all substages R4 through R9. R5-Technology, R6-Reputation use ranks 1–3 (`basic`; all locked competitors when `deep`). R8-UX uses all locked competitors regardless of depth.

**The competitor list is now locked. No new competitors are added after this point.**
