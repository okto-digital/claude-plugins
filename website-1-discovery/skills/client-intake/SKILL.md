---
name: client-intake
description: "Run client intake research and produce D1 pre-interview document. Invoke when the user asks to research a client, prepare for a client meeting, run intake, generate the D1 document, or start the intake phase of a website project."
allowed-tools: Read, Write, Glob, Bash, WebSearch, Task, AskUserQuestion
version: 2.0.0
---

# Client Intake

Research a client online, dispatch 21 domain-analyst agents in waves of 6 to score 636 checkpoints, and produce D1: a pre-interview document with research findings, domain analysis, gap-targeted questions, and note space.

**Core principle:** Research first, write research context to file, THEN let specialized agents analyze each domain independently.

---

## Process

### Step 1: Load project context

Read `project-state.md`. Extract: client name, URL, project type, language config (primary language, primary market, secondary languages).
If missing, stop: "Run project-init first."

### Step 2: Gather additional input

Ask for anything not in project-state.md: URL (if missing), brief description, industry, additional context (emails, notes, concerns). Proceed once company name and URL are available.

### Step 3: Research

**Web crawling (if URL provided):**
1. Invoke the `dispatch-subagent` skill to dispatch `web-crawler` for the homepage. Output instructions: "Return extended summary with key facts. Telegraphic, no prose."
2. From the homepage content, identify 3-10 high-value pages (eg. about, services, products, team, portfolio, contact, pricing).
3. Dispatch web-crawler for each high-value page (parallel where possible).

**Web search:**

Run in primary language (all queries) + secondary languages (first two queries each). Natural phrasing per language, not literal translation.

- "[company name]" (always, language-neutral)
- "[company name] [reviews]" (e.g., Slovak: "recenzie", German: "Bewertungen")
- "[company name] [industry]"
- "[company name] [news] [current year]"
- "[business type] [location]"

**Competitor discovery:**

Determine business type and location from crawl results. Primary language gets all queries; secondary get top 2.

- "[business type] [location]" (e.g., "hotel Zilina")
- "[business type] [region]" (e.g., "ubytovanie Mala Fatra")
- "[best] [business type] [region] [year]" (e.g., "najlepsie hotely Mala Fatra 2026")

Record competitor names and URLs -- feed into competitive-landscape domain and R2 research.

**Business registry lookup:**
1. Detect company country from research so far (company address, domain TLD, site language).
2. Determine the **legal entity name** -- this is often different from the brand or product name. Look for it in website footer, imprint/legal page, terms of service, or privacy policy. A hotel called "Dubna Skala" may be operated by "ABC s.r.o." -- you need the entity name, not the brand.
3. Look up the company in the appropriate registry using the legal entity name (or company registration ID if found):
   - **Slovak company** -- WebSearch: `site:finstat.sk "[legal entity name]"`. If a match is found, fetch the result page for details.
   - **Other countries** -- WebSearch: `site:dnb.com "[legal entity name]"` (or relevant local D&B domain). If a match is found, fetch the result page for details.
   - If the legal entity name yields no results, try the brand name as fallback -- but the entity name is the primary search term.
4. Extract: legal name, registration ID, founded year, legal form, revenue range, employee count, registered address.
5. If no registry match is found, note "No business registry data available" and continue.

### Step 4: Write research context

Synthesize ALL findings from Step 3 into `intake/research-context.md`. Create the `intake/` directory if it does not exist.

Structure the file:
- **Metadata:** URL, industry, location, business model, project type
- **Key facts:** Name/value pairs for business identity fields
- **Website assessment:** Structure, content quality, tech stack, issues found
- **Competitive context:** Competitors identified, market positioning
- **External intelligence:** News, reviews, social presence, job postings
- **Language context:** Primary language, primary market, which queries were run in which language, whether different-language results differed meaningfully from each other
- **Registry data:** Legal name, ID, legal form, revenue, employees, address (or "No business registry data available")

Checkpoint to operator: "Research found X key facts across Y sources. Written to intake/research-context.md."

### Step 5: Dispatch domain-analyst agents

Dispatch all 21 domain-analyst agents via `dispatch-subagent`. Model: **sonnet**. Max 6 concurrent -- dispatch in waves, wait for each wave before the next.

- **Wave 1:** business-context, competitive-landscape, target-audience, project-scope, analytics-and-measurement, site-structure
- **Wave 2:** content-strategy, design-and-brand, technical-platform, performance, security-and-compliance, forms-and-lead-capture
- **Wave 3:** seo-and-discoverability, accessibility, post-launch, ecommerce (cond.), blog-and-editorial (cond.), multilingual (cond.)
- **Wave 4:** user-accounts (cond.), migration-and-redesign (cond.), booking-and-scheduling (cond.)

Each dispatch: domain name, domain file path (`${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/[domain].md`), research context path (`intake/research-context.md`), conditional flag (`yes`/`no`), model: sonnet.

15 universal domains (conditional=no), 6 conditional domains (conditional=yes): ecommerce, blog-and-editorial, multilingual, user-accounts, migration-and-redesign, booking-and-scheduling.

### Step 6: Assemble D1

If `intake/D1-pre-interview.md` already exists, warn: "D1 already exists. Overwrite?" Use AskUserQuestion. If declined, stop.

Read `${CLAUDE_PLUGIN_ROOT}/references/d1-template.md`.

Assemble the document:
- **Section 1 (Research Findings):** From `intake/research-context.md`
- **Section 2 (Domain Analysis):** From 21 domain-analyst returns, grouped by the fixed headers in the template:
  - About the Business: business-context, competitive-landscape, target-audience
  - Project Parameters: project-scope, analytics-and-measurement
  - Website Structure and Content: site-structure, content-strategy
  - Design and Brand: design-and-brand
  - Technical: technical-platform, performance, security-and-compliance
  - Conversion and Growth: forms-and-lead-capture, seo-and-discoverability, accessibility
  - After Launch: post-launch
  - Additional Areas: conditional domains (ACTIVE get full sections, INACTIVE get one-line notes)

Write to `intake/D1-pre-interview.md`.

### Step 7: Update state

Read project-state.md. Update the D1 row:
- status: research-complete
- file: intake/D1-pre-interview.md
- updated: today's date

**D1 states:**
- `research-complete` -- research + gap analysis done, interview not yet conducted
- `interview-complete` -- operator filled in client answers (update via project-init Update Mode)

Downstream skills check this distinction: project-research warns if only `research-complete`, project-brief warns if proposal will lack client priorities.

Write the updated project-state.md. Do not modify any other rows.

---

## Rules

<critical>
- **NEVER** skip research (Step 3) and go straight to domain analysis -- the research-first approach is the core value of this skill
- **NEVER** invent research findings or fabricate data points
- **NEVER** write D1 without completing all prior steps
- **NEVER** modify project-state.md beyond the D1 row
- **NEVER** run without project-state.md -- require project-init first
- **NEVER** read the domain content files, leave this to the dispatched domain-analyst
</critical>

- If web-crawler fails on a page, note the failure and continue with available data -- do not block the entire process
- If WebSearch returns no useful results for a query, note it and continue
- If business registry lookup returns no match, note it and continue -- registry data is supplementary, not required
- If fewer than 5 key facts are gathered from research, warn the operator that D1 will have limited coverage and ask whether to proceed or provide additional context
- If a domain-analyst agent fails, note which domain was affected and continue assembling D1 with available results

---

## Reference Files

All shared references are at the plugin root:

- `${CLAUDE_PLUGIN_ROOT}/references/d1-template.md` -- D1 output template (2-section structure)
- `${CLAUDE_PLUGIN_ROOT}/references/domain-quick-ref.md` -- Compact checkpoint index (21 domains, 636 checkpoints)
- `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/*.md` -- 21 domain checkpoint files (read by domain-analyst agents, not by this skill directly)

Sub-agents dispatched by this skill (via dispatch-subagent):

- `web-crawler` -- Crawl client website pages
- `domain-analyst` -- Analyze one domain's checkpoints against research context (21 instances, dispatched in waves of 6)
