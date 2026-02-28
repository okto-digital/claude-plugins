# Method 0: Apify MCP

Highest-priority crawling method. Apify runs headless browsers on their infrastructure, handling JavaScript rendering, WAF bypass, and anti-bot measures. Uses the user's Apify account via MCP integration.

**Requires Apify MCP server configured.** If the tool call fails (tool not found), move to Method 1 (curl).

---

## Tool Names

Two possible configurations exist. Try the invocation below -- if it fails, Apify is not configured.

**Hosted mode** (remote MCP server):
- Server URL: `https://mcp.apify.com`
- Exposes general-purpose tools: `call-actor`, `search-actors`, `get-actor-output`, etc.
- Tool names in Claude Code: `mcp__apify__call-actor`, `mcp__apify__get-actor-output`

**Stdio mode** (local npx):
- Command: `npx @apify/actors-mcp-server --tools apify/website-content-crawler`
- Exposes actor as direct tool (name varies by configuration)
- Tool name example: `mcp__apify__apify-slash-website-content-crawler`

---

## Invocation

### Via `call-actor` (hosted mode)

**Preferred actor:** `apify/website-content-crawler`

```
mcp__apify__call-actor(
  actorId: "apify/website-content-crawler",
  input: {
    "startUrls": [{ "url": "[TARGET_URL]" }],
    "maxCrawlPages": 1,
    "outputFormats": ["markdown"]
  }
)
```

**Fallback actor:** `apify/rag-web-browser`

```
mcp__apify__call-actor(
  actorId: "apify/rag-web-browser",
  input: {
    "startUrls": [{ "url": "[TARGET_URL]" }],
    "maxResults": 1
  }
)
```

### Via direct tool (stdio mode)

Tool name depends on MCP server configuration. Invoke directly with the URL:

```
mcp__apify__apify-slash-website-content-crawler(
  url: "[TARGET_URL]"
)
```

---

## Execution Model

- **Synchronous from MCP client perspective** -- `call-actor` blocks until the actor finishes
- **Real processing time:** 10-60 seconds for a single page (actor spins up browser, renders page, extracts content)
- **Inform operator:** "Calling Apify website-content-crawler... (typically 10-30 seconds)"
- Results returned directly in the response
- If response is truncated, use `get-actor-output` to retrieve full data

---

## Response Handling

The `website-content-crawler` actor returns markdown content directly. Check the response:

1. **Non-empty content:** Proceed with the markdown output. Extract metadata (title, description) from the content if present, or note as unavailable.

2. **Empty or near-empty response:** Some content types return empty strings:
   - XML content (RSS feeds, sitemaps)
   - Non-HTML responses (JSON APIs, PDFs)
   - Pages with aggressive anti-bot that blocks even Apify

   **Detect:** Response body is empty string, whitespace only, or under 100 characters.
   **Action:** Fallback immediately to Method 1 (curl). Do not retry with Apify.

3. **Actor error or timeout:** Apify returns error status.
   **Action:** Fallback to Method 1 (curl).

---

## Configuration

Apify MCP requires `APIFY_TOKEN` environment variable. To enable:

**Hosted mode (.mcp.json):**
```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com?tools=apify/website-content-crawler",
      "env": {
        "APIFY_TOKEN": "your-token-here"
      }
    }
  }
}
```

**Stdio mode (.mcp.json):**
```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server", "--tools", "apify/website-content-crawler"],
      "env": {
        "APIFY_TOKEN": "your-token-here"
      }
    }
  }
}
```

---

## When This Method Fails

Move to Method 1 (curl) if:
- No Apify MCP tools detected at startup
- Actor returns empty/near-empty response (XML, non-HTML content)
- Actor returns error status
- Actor times out
- `APIFY_TOKEN` is not configured or invalid

---

## Limitations

- Requires paid Apify account with API token
- Actor execution costs Apify compute units (minimal for single-page crawls)
- Cannot handle content behind login/authentication (no cookie injection)
- XML and non-HTML content returns empty -- must fallback to curl for these
- Single-page crawl only (maxCrawlPages: 1) -- not for site-wide scraping
