---
name: client-researcher
description: "Research a client company and produce a D14 Client Research Profile for meeting preparation. Combines web search intelligence, website crawling (via webtools-init web-crawler), and business registry lookups to build a comprehensive profile across 9 categories. Saves as .raw.md and compresses via document-compressor."
allowed-tools: WebSearch, Read, Write, Edit, Glob, Task
version: 2.0.0
---

Research a client company and produce a D14 Client Research Profile -- a structured intelligence report that prepares the operator for the intake meeting. Given a URL (required) and optional context, gather intelligence from web search, website crawling, and business registry lookups, then synthesize findings into actionable conversation starters.

---

## Lifecycle Startup

Before doing anything else, complete these steps in order. This skill works with OR without an existing webtools project.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- **If it exists:** Parse Project Info and Document Log. Check if D14 already exists in the Document Log.
  - If D14 exists and has status `complete`: warn the operator that a D14 already exists. Ask whether to overwrite or cancel.
  - If D14 exists with other status: note it and proceed (will overwrite the draft).
- **If it does NOT exist:** Continue without project context. After producing D14, suggest running `/webtools-init` to create a project and persist the document properly.

### 2. Directory Validation

Check if `brief/` directory exists. Create it if missing. D14 is saved here regardless of whether a project exists.

### 3. Status Report

```
[CLIENT RESEARCH]

Project: [client name from registry, or "No project -- standalone mode"]

Awaiting client URL (required). You may also provide context about what to look for.
```

---

## Step 1: URL and Context Intake

Ask for the client website URL if not provided as an argument. Accept optional context from the operator about what to focus on (e.g., "look for their pricing model", "they are a B2B SaaS company", "focus on their service offering").

Validate the URL:
- Must start with `http://` or `https://`
- Must be a root domain or homepage (not a deep page -- operator provides the main site URL)

---

## Step 2: Web Search -- External Intelligence

Use WebSearch to find the client by company name. Extract the company name from the URL domain (e.g., `acme.com` -> "Acme"). If ambiguous, crawl the homepage first (Step 3) to get the company name from `<title>` or `<meta og:site_name>`, then return to complete this step.

Run these searches:

1. **General presence:** `"[company name]"` -- overall web footprint
2. **Reputation signals:** `"[company name]" reviews` -- Google Business, Trustpilot, Clutch, G2, etc.
3. **News and professional presence:** `"[company name]" news` OR `site:linkedin.com "[company name]"` -- press mentions, LinkedIn profile
4. **Hiring signals:** `"[company name]" jobs` OR `site:linkedin.com/jobs "[company name]"` -- open positions revealing growth areas, tech stack, strategic priorities

### What to extract

From the search results directly (do NOT crawl every result URL -- extract what WebSearch returns):

- **Recent news and press:** Notable mentions, awards, partnerships, funding (with dates and sources)
- **Online reputation:** Review site ratings and recurring themes
- **Social presence:** Active platforms, follower ranges if visible
- **Job postings:** Open positions that reveal growth areas, tech stack, or strategic priorities
- **Industry context:** Market position signals from third-party sources (rankings, directories, awards)

### Present findings

Show a summary of external intelligence gathered before proceeding:

```
[WEB SEARCH] [company name]

Searches completed: 4
Notable findings:
  - [key finding 1]
  - [key finding 2]
  - ...

Proceed with website crawl?
```

---

## Step 3: Website Crawl -- Via Web-Crawler Agent

Delegate all website crawling to the webtools-init web-crawler agent via the Task tool. The web-crawler handles the full method cascade (Apify, curl, WebFetch, browser, etc.) internally.

### 3a. Crawl homepage

Dispatch a Task to the web-crawler agent for the homepage URL:

```
Task(subagent_type="general-purpose", prompt="You are the web-crawler agent. Crawl this URL and return clean markdown content with metadata: [URL]

Read and follow the agent definition at: ${CLAUDE_PLUGIN_ROOT}/../webtools-init/agents/web-crawler.md

Return the full cleaned content with metadata headers.")
```

From the homepage content:
- Extract the company name (for web search if not yet done)
- Discover primary navigation links (main menu)
- Discover footer navigation links
- Check for sitemap.xml (try `[domain]/sitemap.xml` via a separate Task)

### 3b. Present discovered pages

Show the operator a numbered list of discovered pages. Recommend 5-15 pages based on intelligence value:

- **High value (always recommend):** Homepage, About, Services/Products, Contact, Case Studies/Portfolio
- **Medium value (recommend if present):** Team, Industries, Testimonials, Blog listing, Pricing
- **Low value (skip unless requested):** Privacy Policy, Terms, Cookie Policy, individual blog posts, login pages

Let the operator confirm or adjust the selection before proceeding.

```
[SITE MAP] example.com -- 23 pages discovered

Recommended for analysis (12 pages):
  [x]  1. / (Homepage)
  [x]  2. /about
  [x]  3. /services
  ...

Skipped (low intelligence value):
  [ ] 13. /privacy-policy
  ...

Confirm this selection, or adjust (add/remove page numbers).
```

### 3c. Crawl confirmed pages

Dispatch one Task per confirmed page to the web-crawler agent. Run multiple Tasks in parallel where possible for efficiency.

For each returned page content, extract intelligence observations organized by the intelligence sections in `references/d14-template.md` (sections 3-8). Not every page yields intelligence for every section. Extract what is present and move on.

### Progress tracking

After each page completes, show a brief progress line:

```
[3/12] /services -- 8 observations (Business Identity: 3, Market Signals: 2, Brand: 3)
```

If a page crawl fails (web-crawler returns error), log it and continue:

```
[5/12] /case-studies -- FAILED (web-crawler could not retrieve). Skipping.
```

---

## Step 4: Business Registry Lookup

After web search and website crawl, look up the client's business registry entry for financial intelligence.

### 1. Extract company name

Use the company name already extracted from the homepage in Step 3a.

### 2. Determine entity origin

- If domain TLD is `.sk`, OR the page `<html lang>` attribute starts with `sk`, OR the page content is clearly in Slovak -> **Slovak entity** -> use finstat.sk
- Otherwise -> **international entity** -> use dnb.com business directory

### 3. Look up the company

**Slovak entity (finstat.sk):**
Dispatch a Task to the web-crawler agent for `https://finstat.sk/databaza?query=[company_name]`. From the returned content, identify the matching entity. If a detail page URL is found, dispatch another web-crawler Task for the detail page. Extract: revenue, profit/loss, employee count, legal form, ICO (company ID), founding date, registered address.

**International entity (dnb.com):**
Dispatch a Task to the web-crawler agent for `https://www.dnb.com/business-directory.html` search (or the search URL pattern with company name). Extract from the returned content: company overview, employee count estimate, industry classification, headquarters location, year established.

### 4. Handle ambiguity and failure

- **Multiple results:** Present the top matches to the operator for confirmation before extracting details.
- **No results / blocked / error:** Report to operator and continue without financial data. This step is best-effort, not blocking.

### 5. Present findings

Show results before proceeding to synthesis:

```
[BUSINESS REGISTRY] finstat.sk

Company: Example s.r.o.
ICO: 12345678
Founded: 2015
Revenue (latest): EUR 1.2M
Employees: 15-25
Legal form: s.r.o.

Proceeding to synthesis.
```

For international entities, adapt the format to the available dnb.com fields (company overview, employee estimate, industry, headquarters, year established).

---

## Step 5: Synthesis and Report

After all three intelligence sources are gathered (web search, website crawl, business registry), synthesize into the D14 report structure.

### D14 structure

Follow the template in `references/d14-template.md` for the full 9-section structure and frontmatter schema. Section 1 is the executive summary, section 1b covers external intelligence from web search, sections 3-8 compile website intelligence by category, and section 9 is analytical synthesis.

<critical>
Section 9 (Conversation Starters) is the highest-value output of this skill. It is NOT a summary of the other sections. It is analytical synthesis: key observations, inferred pain points, unanswered questions, and contradictions noticed. Write each starter as an actionable meeting prompt the operator can say or ask. Example: "Your case studies page shows 3 projects, but the homepage says '50+ completed.' Are there more projects we can showcase on the new site?"
</critical>

### Present summary

After generating D14, present a completion summary showing:
- Sources used (web search findings count, pages analyzed, registry status)
- Observation count per section
- The output file path
- An offer to expand sections or re-crawl pages

---

## Step 6: Save and Compress

### 1. Write raw file

Write the D14 report to `brief/D14-client-research-profile.raw.md` with frontmatter per `references/d14-template.md`.

### 2. Compress

Invoke the document-compressor agent via Task tool to produce the compressed version:

```
Task(subagent_type="general-purpose", prompt="You are the document-compressor agent. Compress this document to reduce token consumption while preserving all substantive information.

Read and follow the agent definition at: ${CLAUDE_PLUGIN_ROOT}/../webtools-init/agents/document-compressor.md

Document to compress: brief/D14-client-research-profile.raw.md
Output path: brief/D14-client-research-profile.md

The .raw.md file already exists. Compress it to the standard path.")
```

### 3. Registry update (if project exists)

Update `project-registry.md`:
- Add or update a Document Log row: Doc ID = `D14`, Document = `Client Research Profile`, File Path = `brief/D14-client-research-profile.md`, Status = `complete`, Created = today, Updated = today, Created By = `webtools-intake`
- Phase Log: if Intake phase has no Started date, set Started to today. Add `webtools-intake` to Plugins Used.

### 4. Next step suggestion

If project exists:
```
D14 saved to brief/D14-client-research-profile.md (compressed)
Raw version: brief/D14-client-research-profile.raw.md

Next step: /webtools-intake-research to auto-continue into PREP mode,
  or /webtools-intake-prep to prepare the interview guide manually.
```

If no project:
```
D14 saved to brief/D14-client-research-profile.md (compressed)
Raw version: brief/D14-client-research-profile.raw.md

No project registry found. To integrate this into the webtools pipeline:
  1. Run /webtools-init to create a project
  2. Run /webtools-intake-research to auto-continue into PREP mode
```

---

## Behavioral Rules

- Extract intelligence, not raw content. Every observation must be an analytical finding, not a copy-paste.
- Web search extracts intelligence from search result snippets. Do not crawl every search result URL -- use what WebSearch returns.
- Website crawling is delegated to the webtools-init web-crawler agent via Task tool. Do NOT implement your own crawl cascade.
- Business registry lookups (finstat.sk for Slovak entities, dnb.com for international) are delegated to the web-crawler agent via Task tool, same as website crawling.
- Do not fabricate intelligence. If a section has no findings, state "No indicators found from the sources analyzed."
- Do not rewrite or improve the client's content. Report what exists as-is.
- Do not use emojis in any output.
- File slugs and URLs must be deterministic -- same URL always produces the same output path.
- Redirect detection: if a page redirects to a different URL than requested, note the redirect and extract from the final URL.
- Respect the operator's page selection. Do not crawl pages the operator excluded.
- Always save to `.raw.md` first, then compress. Never write directly to the standard path.

---

## Reference Files

- `references/d14-template.md` -- D14 report template with frontmatter schema, section structure, and mapping to PREP conversation topics
