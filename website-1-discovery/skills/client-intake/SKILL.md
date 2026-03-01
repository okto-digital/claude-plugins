---
name: client-intake
description: "Run client intake research and produce D1 pre-interview document. Invoke when the user asks to research a client, prepare for a client meeting, run intake, generate the D1 document, or start the intake phase of a website project."
allowed-tools: Read, Write, Glob, Bash, WebSearch, Task
version: 2.0.0
---

# Client Intake

Research a client online, dispatch 21 domain-analyst agents in parallel to score 636 checkpoints, and produce D1: a pre-interview document with research findings, domain analysis, gap-targeted questions, and note space.

**Core principle:** Research first, write research context to file, THEN let specialized agents analyze each domain independently.

---

## Process

### Step 1: Load project context

Read `project-state.md` from the project working directory. Extract client name, URL, and project type.

If project-state.md does not exist, stop and tell the operator: "Run project-init first to set up the project."

### Step 2: Gather additional input

Ask the operator for context not already in project-state.md:
- Client URL (if missing from state)
- Brief description of the client or project
- Industry (if known)
- Any additional context: emails, inquiry form answers, notes, specific concerns

Proceed once the operator provides at least a company name and URL.

### Step 3: Research

**Web crawling (if URL provided):**
1. Invoke the `dispatch-subagent` skill to dispatch `web-crawler` for the homepage. Output instructions: "Return extended summary with key facts. Telegraphic, no prose."
2. From the homepage content, identify 3-10 high-value pages (eg. about, services, products, team, portfolio, contact, pricing).
3. Dispatch web-crawler for each high-value page (parallel where possible).

**Web search:**
Run 4 WebSearch queries:
- "[company name]"
- "[company name] reviews"
- "[company name] [industry]"
- "[company name] news [current year]"

**Business registry lookup:**
1. Detect company country from research so far (company address, domain TLD, site language).
2. Look up the company in the appropriate registry:
   - **Slovak company** -- WebSearch: `site:finstat.sk [company name]`. If a match is found, fetch the result page for details.
   - **Other countries** -- WebSearch: `site:dnb.com [company name]` (or relevant local D&B domain). If a match is found, fetch the result page for details.
3. Extract: legal name, registration ID, founded year, legal form, revenue range, employee count, registered address.
4. If no registry match is found, note "No business registry data available" and continue.

### Step 4: Write research context

Synthesize ALL findings from Step 3 into `intake/research-context.md`. Create the `intake/` directory if it does not exist.

Structure the file:
- **Metadata:** URL, industry, location, business model, project type
- **Key facts:** Name/value pairs for business identity fields
- **Website assessment:** Structure, content quality, tech stack, issues found
- **Competitive context:** Competitors identified, market positioning
- **External intelligence:** News, reviews, social presence, job postings
- **Registry data:** Legal name, ID, legal form, revenue, employees, address (or "No business registry data available")

Checkpoint to operator: "Research found X key facts across Y sources. Written to intake/research-context.md."

### Step 5: Dispatch domain-analyst agents

Dispatch all 21 domain-analyst agents in parallel via the `dispatch-subagent` skill. All use **sonnet** model.

Each dispatch provides:
- Domain name
- Domain file path: `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/[domain].md`
- Research context path: `intake/research-context.md`
- Conditional flag: `yes` or `no`
- Model: sonet or opus

**15 universal domains** (conditional=no):
business-context, competitive-landscape, target-audience, project-scope, analytics-and-measurement, site-structure, content-strategy, design-and-brand, technical-platform, performance, security-and-compliance, forms-and-lead-capture, seo-and-discoverability, accessibility, post-launch

**6 conditional domains** (conditional=yes):
ecommerce, blog-and-editorial, multilingual, user-accounts, migration-and-redesign, booking-and-scheduling

Dispatch all 21 in a single parallel batch. Collect all returns before proceeding.

### Step 6: Assemble D1

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
- status: complete
- file: intake/D1-pre-interview.md
- updated: today's date

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
- `domain-analyst` -- Analyze one domain's checkpoints against research context (21 instances dispatched in parallel)
