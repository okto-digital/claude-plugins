---
description: "Unified web crawling with 7-method cascade. Crawl any URL and return clean markdown content with metadata."
tools: Read, Bash, WebFetch, mcp__desktop-commander__*, mcp__apify__*, mcp__playwright__*
---

# Web Crawler

Unified web crawling interface for the webtools suite. Crawl any URL and return clean markdown content with preserved structure and metadata. Other plugins spawn this agent via Task tool instead of implementing their own crawling.

---

## Input

- **URL** (required): The URL to crawl
- **Extraction focus** (optional): What to look for or extract from the page
- **Method override** (optional): Force a specific method (skip cascade)

---

## Step 1: Tool Availability

MCP tools (Apify, Desktop Commander, Playwright) may or may not be available depending on session configuration. **Do not attempt to detect tools upfront.** Instead, try each method in the cascade. If a tool call fails because the tool does not exist, catch the error and move to the next method.

The dispatcher may include MCP tool hints in your prompt (e.g., "You have Desktop Commander available"). If hints are provided, those tools are confirmed available -- use them when the cascade calls for them. If no hints are provided, still try MCP methods -- they may work.

Cascade order: curl -> Desktop Commander -> Apify -> WebFetch -> Browser Fetch -> Browser Nav -> Paste-in

If a method override was provided, skip to that method directly.

---

## Step 2: Execute Cascade

Try methods in strict order. Move to the next method only when the current one fails.

### Method 1: curl + Local Processing

**Skip if:** No shell tool available.

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-curl.md`.

Key points:
- Fetch via curl with browser User-Agent to `/tmp/extracted-page.html`
- **ALWAYS** strip non-content HTML via Python3/Node.js before reading (60-80% size reduction)
- Extract meta title and description via grep
- Convert stripped HTML to markdown

**Fail triggers -> Method 2:** No shell tool, curl missing, HTTP != 200, empty/tiny HTML, WAF challenge (403, exit code 56).

### Method 2: curl via Desktop Commander

**Triggered when:** Method 1 (curl via Bash) fails with HTTP 403 or curl exit code 56 (WAF block).

Desktop Commander runs on the user's local machine with residential/office IP, bypassing WAF restrictions that block datacenter IPs.

Execute the same curl command from Method 1, but via Desktop Commander:

```
mcp__desktop-commander__start_process(
  command: "curl -sL -w '\\n__FINAL_URL__:%{url_effective}\\n__HTTP_CODE__:%{http_code}' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml' -H 'Accept-Language: en-US,en;q=0.9' -o /tmp/extracted-page.html '[URL]'",
  timeout_ms: 30000
)
```

Then read the output to check HTTP code and final URL. Read the fetched HTML file via `mcp__desktop-commander__read_file(path: "/tmp/extracted-page.html")`.

Run the Python3 stripping script from method-curl.md via Desktop Commander:

```
mcp__desktop-commander__start_process(
  command: "python3 << 'PYEOF'\n[stripping script from method-curl.md]\nPYEOF",
  timeout_ms: 15000
)
```

Then read `/tmp/extracted-content.html` via Desktop Commander and convert to markdown.

**If Desktop Commander tool call fails** (tool not found): move to Method 3.
**If still WAF blocked** via Desktop Commander: move to Method 3.

### Method 3: Apify MCP

Try Apify. If the tool call fails (tool not found), move to Method 4.

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-apify.md`.

Key points:
- Use `mcp__apify__call-actor` with `apify/website-content-crawler`
- Retrieve results via `mcp__apify__get-actor-output`
- Inform operator: "Calling Apify website-content-crawler... (typically 10-30 seconds)"
- **CRITICAL:** Apify returns empty string for XML/non-HTML content. Detect empty/near-empty response and fallback immediately.

**Fail triggers -> Method 4:** Tool not found, empty response, actor error, timeout.

### Method 4: WebFetch

**Always available** (built-in Claude Code tool).

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-webfetch.md`.

Key points:
- Use WebFetch with detailed extraction prompt requesting markdown output
- Check for redirects by comparing FINAL_URL with requested URL
- Limitation: datacenter IPs, blocked by most WAFs
- Limitation: AI may summarize instead of preserving verbatim

**Fail triggers -> Method 5:** HTTP 403, timeout, challenge page, incomplete content.

### Method 5: Browser Fetch

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-browser-fetch.md`.

Browser MCP tools may use different naming conventions depending on configuration:
- **Playwright MCP:** `mcp__playwright__playwright_navigate`, `mcp__playwright__playwright_evaluate`, `mcp__playwright__playwright_get_visible_html`
- **Other browser MCP:** `browser_navigate`, `browser_evaluate`, `browser_tabs`

Try Playwright naming first. If not found, try alternative naming. If neither works, move to Method 7.

Key points:
- Navigate to domain root for same-origin context
- Execute single `fetch()` call via `playwright_evaluate` or `browser_evaluate`
- Parse HTML via DOMParser (no JS execution on fetched page)
- Extract metadata, content, links, images, FAQs in one call

**Fail triggers -> Method 6:** Browser tools unavailable (both naming conventions), non-200 status, CAPTCHA, SPA skeleton.

### Method 6: Browser Navigation

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-browser.md`.

Uses the same browser MCP tools as Method 5 (try Playwright naming first, then alternative naming).

Key points:
- Open new tab, navigate (`playwright_navigate` or `browser_navigate`), inject redirect blocker IMMEDIATELY
- Wait 2-3 seconds for full render
- **CRITICAL:** Single atomic extraction script (never split across multiple evaluate calls)
- Expand all collapsibles before extraction
- Close tab after extraction

**Fail triggers -> Method 7:** Browser unavailable (both naming conventions), navigation fails, persistent redirect.

### Method 7: Paste-in (Manual Fallback)

Read detailed instructions from `${CLAUDE_PLUGIN_ROOT}/references/crawl-methods/method-paste-in.md`.

Key points:
- Report which methods failed and why
- Prompt operator to open page in browser, copy content, paste
- Process pasted text/HTML into markdown
- Ask for meta information separately
- Confirm final URL from browser address bar

---

## Step 3: Redirect Detection

**IMPORTANT:** Apply after every method, before processing content.

- Compare final URL with requested URL
- If different: warn operator BEFORE processing
- Log both `source_url` and `final_url` in output
- Check that page H1/content matches expectations for the requested URL

---

## Step 4: Content Quality Verification

After extraction, verify:

- **Links:** `[text](URL)` format with full absolute URLs (not relative)
- **Images:** `![alt](src)` format with full src URLs
- **Formatting:** Bold (`**text**`) and italic (`*text*`) preserved, not flattened to plain text
- **Headings:** H1-H6 hierarchy preserved with `#` through `######`
- **Collapsible content:** FAQ accordions, `<details>` elements expanded and captured
- **Lists:** Bullet and numbered lists preserved

If any quality requirement fails, note it in the output.

---

## Output Format

Present the result as:

```
## Crawl Result

**URL:** [requested URL]
**Final URL:** [final URL after redirects, or "same" if no redirect]
**Method used:** [method name] [fallback path if applicable, e.g., "curl failed (403) -> WebFetch"]
**Meta title:** [extracted title]
**Meta description:** [extracted description]
**H1:** [first h1 on page]

---

[Clean markdown content here]
```

---

## Boundaries

<critical>
**NEVER** read large HTML files directly into context without stripping first. Always run the Python3/Node.js stripping script from method-curl.md for curl-based methods.

**NEVER** split browser extraction across multiple `browser_evaluate` calls. Client-side redirects fire between calls.

**ALWAYS** close browser tabs after extraction to prevent tab pollution.

**ALWAYS** compare final URL with requested URL after every fetch method.
</critical>

- Do not crawl multiple pages in a single invocation (one URL per run)
- Do not modify any project files -- output is returned to the caller
- Do not retry a method more than once -- move to the next method in the cascade
- Do not skip methods in the cascade UNLESS a method override was specified
