# Method 7: Paste-in Fallback

Manual content extraction when all automated methods fail. The operator provides the content directly.

---

## When to use

Use this method when all automated methods (1–6) have failed:
- Methods 1–2 (curl via mcp-curl / Bash): not available, HTTP error, or WAF blocked
- Method 3 (Apify): not available, empty response, actor error, or timeout
- Method 4 (Chrome Control Fetch): not available, fetch blocked, or incomplete content
- Method 5 (Chrome Automation Navigation): not available, redirect loop, or stale content
- Method 6 (WebFetch): 403 Forbidden, timeout, empty, or summarized content

---

## Prompt the operator

```
All automated extraction methods failed for this URL.

Methods 1-2 (curl): [reason -- not available / HTTP [code] / WAF challenge page]
Method 3 (Apify): [reason -- not available / empty response / actor error / timeout]
Method 4 (Chrome Control Fetch): [reason -- not available / fetch blocked / incomplete content]
Method 5 (Chrome Automation Nav): [reason -- not available / redirect loop / stale content]
Method 6 (WebFetch): [reason -- 403 / timeout / empty / summarized content]

To proceed, open the page in your browser and either:
(a) Select all main content on the page, copy, and paste it here
(b) Use browser View Source (Ctrl+U / Cmd+U), copy the HTML, and paste it here
(c) Try a different URL
(d) Cancel

I will format whatever you paste into clean markdown.
```

---

## Processing pasted content

### If operator pastes plain text

Apply formatting rules from `${CLAUDE_PLUGIN_ROOT}/agents/references/web-crawler/formatting-rules.md` where possible:
- Identify heading hierarchy from text patterns (lines that look like section headers)
- Preserve any markdown formatting already present
- URLs that appear as plain text: attempt to reconstruct as links if context suggests they were links

### If operator pastes HTML

Convert to markdown using the full rules in `${CLAUDE_PLUGIN_ROOT}/agents/references/web-crawler/formatting-rules.md`:
- Identify main content area
- Convert all elements (headings, links, images, bold, italic, lists, tables)
- Strip remaining HTML tags

### Meta title and description

Ask the operator separately:

```
I also need the page's meta information. You can find this in View Source:

1. Meta title: Look for <title>...</title> in the <head> section
2. Meta description: Look for <meta name="description" content="...">

If you can't find them, I'll leave them empty in the output.
```

---

## Redirect verification

Since the operator is viewing the page in their own browser, ask them to confirm the URL:

```
Please confirm: what URL is shown in your browser's address bar?
(This helps detect any redirects that may have occurred.)
```

Compare the reported URL with the originally requested URL. If different, apply redirect detection (see SKILL.md).

---

## Proceed

After formatting the pasted content, proceed to the Review step in SKILL.md.