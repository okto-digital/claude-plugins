---
name: client-researcher
description: "Crawl a client website to produce a D14 Client Research Profile for meeting preparation. Extracts intelligence across 8 categories (business identity, audience signals, website assessment, brand style, digital presence, competitive context) and generates actionable conversation starters."
allowed-tools: Bash, WebFetch, Read, Write, Edit, Glob
version: 1.0.0
---

Crawl a client website and produce a D14 Client Research Profile -- a structured intelligence report that prepares the operator for the intake meeting. Given a URL, discover the site structure, extract intelligence from key pages, and synthesize findings into actionable conversation starters.

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

### 3. Tool Detection

Detect available crawling tools using the same cascade as content-extractor:

- **Shell access:** Check for any shell execution tool (Bash, Desktop Commander, terminal MCP). If available, run `which curl` to verify curl is installed.
- **Browser tools:** Check if browser tools (`browser_navigate`, `browser_evaluate`) are accessible.

Build the available methods list:

| Method | Available when |
|---|---|
| 1. curl | Shell tool available AND curl installed |
| 2. WebFetch | Always available |
| 3. Browser Fetch (fetch API) | Browser tools available |
| 4. Browser Navigation | Browser tools available |
| 5. Manual paste-in | Always available |

### 4. Status Report

```
[CLIENT RESEARCH]

Project: [client name from registry, or "No project -- standalone mode"]

Crawling methods available:
  1. curl + local processing   [available / not available]
  2. WebFetch                  [always available]
  3. Browser Fetch (fetch API) [available / not available]
  4. Browser Navigation        [available / not available]
  5. Manual paste-in           [always available]

Awaiting client URL.
```

---

## Step 1: URL Intake

Ask for the client website URL if not provided as an argument.

Validate the URL:
- Must start with `http://` or `https://`
- Must be a root domain or homepage (not a deep page -- operator provides the main site URL)

Resolve the URL: fetch the homepage with the first available method (curl preferred). Check for redirects. If the URL redirects (e.g., `http://` to `https://`, or `example.com` to `www.example.com`), use the final URL silently. If it redirects to an entirely different domain, warn the operator and ask to confirm.

---

## Step 2: Business Registry Lookup

After resolving the homepage URL, look up the client's business registry entry for financial intelligence.

### 1. Extract company name

From the fetched homepage, extract the company name using the first available source:
- `<meta property="og:site_name">` content
- `<title>` tag (strip suffixes like "| Home", "-- Official Site")
- First visible `<h1>` heading

### 2. Determine entity origin

- If domain TLD is `.sk`, OR the page `<html lang>` attribute starts with `sk`, OR the page content is clearly in Slovak → **Slovak entity** → use finstat.sk
- Otherwise → **international entity** → use dnb.com business directory

### 3. Look up the company

**Slovak entity (finstat.sk):**
Use WebFetch on `https://finstat.sk/databaza?query=[company_name]` to search. From the results page, identify the matching entity and fetch its detail page. Extract: revenue, profit/loss, employee count, legal form, ICO (company ID), founding date, registered address.

**International entity (dnb.com):**
Use WebFetch on `https://www.dnb.com/business-directory.html` search (or the search URL pattern with company name). Extract: company overview, employee count estimate, industry classification, headquarters location, year established.

### 4. Handle ambiguity and failure

- **Multiple results:** Present the top matches to the operator for confirmation before extracting details.
- **No results / blocked / error:** Report to operator and continue without financial data. This step is best-effort, not blocking.

### 5. Present findings

Show results before proceeding to site map discovery:

```
[BUSINESS REGISTRY] finstat.sk

Company: Example s.r.o.
ICO: 12345678
Founded: 2015
Revenue (latest): EUR 1.2M
Employees: 15-25
Legal form: s.r.o.

Proceed with website crawl?
```

For international entities, adapt the format to the available dnb.com fields (company overview, employee estimate, industry, headquarters, year established).

---

## Step 3: Site Map Discovery

Fetch the homepage and extract the navigation structure.

### What to extract

- Primary navigation links (main menu)
- Footer navigation links
- Any secondary/utility navigation
- Sitemap.xml if accessible (try `/sitemap.xml`)

### Present discovered pages

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

---

## Step 4: Page-by-Page Intelligence Extraction

Crawl each confirmed page and extract intelligence. Do NOT extract raw content -- extract structured intelligence per category.

### Crawling method cascade

Try methods in priority order. Move to the next only when the current one fails. Follow the same patterns as content-extractor:

1. **curl** (preferred) -- fetch raw HTML, strip non-content elements via python3/node, then read the cleaned HTML. See `references/crawl-methods.md` for the full curl workflow including HTML stripping.
2. **WebFetch** -- use when curl is unavailable or blocked (403/WAF).
3. **Browser Fetch** -- use when WebFetch is blocked. Runs `fetch()` in the user's browser.
4. **Browser Navigation** -- use when Browser Fetch fails (JS-rendered pages).
5. **Manual paste-in** -- last resort. Ask the operator to paste page content.

<critical>
When curl fails with HTTP 403 or exit code 56, and Desktop Commander is available, retry via Desktop Commander before moving to Method 2. Desktop Commander runs on the user's machine (residential IP), bypassing WAF restrictions that block datacenter IPs.

When WebFetch returns 403 for a site behind WAF/bot protection, skip directly to Method 3 (Browser Fetch). Do not retry WebFetch -- if the site blocks datacenter IPs, WebFetch will always fail for that domain.
</critical>

### What to extract per page

For each page, extract intelligence observations (not raw content). Organize observations by the 6 intelligence sections in `references/d14-template.md` (sections 2-7). Not every page yields intelligence for every section. Extract what is present and move on.

### Progress tracking

After each page, show a brief progress line:

```
[3/12] /services -- 8 observations (Business Identity: 3, Market Signals: 2, Brand: 3)
```

If a page fails to load after exhausting the method cascade, log it and continue:

```
[5/12] /case-studies -- FAILED (all methods exhausted). Skipping.
```

---

## Step 5: Synthesis and Report

After crawling all pages, synthesize the collected intelligence into the D14 report structure.

### D14 structure

Follow the template in `references/d14-template.md` for the full 8-section structure and frontmatter schema. Sections 2-7 compile intelligence by category. Section 8 is analytical synthesis.

<critical>
Section 8 (Conversation Starters) is the highest-value output of this skill. It is NOT a summary of the other sections. It is analytical synthesis: key observations, inferred pain points, unanswered questions, and contradictions noticed. Write each starter as an actionable meeting prompt the operator can say or ask. Example: "Your case studies page mentions 50+ projects but only shows 3 -- worth asking if there are more we can showcase."
</critical>

### Present summary

After generating D14, present a completion summary showing pages analyzed, observation count per section, the output file path, and an offer to expand sections or re-crawl pages.

---

## Step 6: Lifecycle Completion

### 1. Save file

Write the D14 report to `brief/D14-client-research-profile.md` with frontmatter per `references/d14-template.md`.

### 2. Registry update (if project exists)

Update `project-registry.md`:
- Add or update a Document Log row: Doc ID = `D14`, Document = `Client Research Profile`, File Path = `brief/D14-client-research-profile.md`, Status = `complete`, Created = today, Updated = today, Created By = `webtools-intake`
- Phase Log: if Intake phase has no Started date, set Started to today. Add `webtools-intake` to Plugins Used.

### 3. Next step suggestion

If project exists:
```
Next step: /webtools-intake-prep to prepare the interview guide using D14 findings.
```

If no project:
```
D14 saved to brief/D14-client-research-profile.md

No project registry found. To integrate this into the webtools pipeline:
  1. Run /webtools-init to create a project
  2. Run /webtools-intake-prep to prepare the interview guide using D14 findings
```

---

## Behavioral Rules

- Extract intelligence, not raw content. Every observation must be an analytical finding, not a copy-paste.
- Crawling scope is the client website plus business registry lookups (finstat.sk for Slovak entities, dnb.com for international). Do not search LinkedIn, social media, or other external sources.
- Do not fabricate intelligence. If a section has no findings, state "No indicators found on the crawled pages."
- Do not rewrite or improve the client's content. Report what exists as-is.
- Do not use emojis in any output.
- File slugs and URLs must be deterministic -- same URL always produces the same output path.
- Redirect detection: if a page redirects to a different URL than requested, note the redirect and extract from the final URL.
- Respect the operator's page selection. Do not crawl pages the operator excluded.

---

## Reference Files

- `references/d14-template.md` -- D14 report template with frontmatter schema, section structure, and mapping to PREP conversation topics
- `references/crawl-methods.md` -- Detailed crawling method cascade: curl workflow (including HTML stripping scripts), WebFetch prompts, browser fetch, browser navigation, and manual paste-in fallback
