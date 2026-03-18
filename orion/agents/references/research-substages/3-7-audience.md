# Substage 3.7 — Audience & Personas

**Code:** R7
**Slug:** Audience
**Output:** `research/R7-Audience.txt`
**Hypothesis:** Target audience has specific device preferences and trust thresholds that affect UX decisions
**Dependencies:** R1-SERP, R2-Keywords, R3-Competitors, R4-Market
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`, `research/R2-Keywords.txt`, `research/R3-Competitors.txt`, `research/R4-Market.txt`
**MCP tools:** none (synthesis only — no new data collection)

---

## Purpose

The only fully synthesised substage in the research phase — performs no new scraping or API calls. Distils everything gathered across R1–R4 into structured human profiles. Every layout decision, content choice, and feature recommendation in later phases should be traceable back to a persona defined here.

Keep the persona count tight — one per distinct audience segment. Fewer well-researched personas beat many shallow ones.

---

## Data Sources

From `project.json`: goal, site type, notes (audience signals from operator).
From `baseline-log.txt`: mission, client profile, all prior findings including D2, R1–R4 highlights.
From `research/R1-SERP.txt`: intent patterns, search behaviour signals.
From `research/R2-Keywords.txt`: keyword gap and audience segment signals, semantic keyword clusters with page type mapping.
From `research/R3-Competitors.txt`: competitor audience targeting signals, positioning, messaging.
From `research/R4-Market.txt`: customer behaviour, website expectations, payment patterns, gap analysis opportunities.

---

## Methodology

### Step 1: Audience segment definition

Before building personas, define distinct audience segments based on all available research. Segments come from the data (INIT notes, competitor targeting, search intent, market research) — personas are built from segments, not the other way around.

### Step 2: Persona construction

For each segment, construct a concise persona profile. Areas to cover: demographics, psychographics and buying motivation, digital behaviour and device preferences, trust threshold, keyword mapping across funnel stages (from R2-Keywords), and messaging angles. Flag one persona as the primary design target.

Be concise — short phrases, not paragraphs. The persona should be a decision tool for downstream agents, not a character study.

### Step 3: User journey map per persona

Map the journey from awareness through advocacy. The most important output per stage is the **website implication** — what does the site need to do at this stage to move this persona forward? This translates persona behaviour directly into page and content requirements.

---

## Output

Write `research/R7-Audience.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R7]`.

Concept Creation reads personas, journey map website implications and keyword mapping for site structure and content planning. R8-UX and R9-Content use persona device preferences and trust thresholds to contextualise their findings.
