# Method 5: Paste-in Fallback

Manual content extraction when all automated methods fail. The operator provides the content directly.

---

## When to use

Use this method when:
- Method 1 (curl): not available, HTTP error, or WAF blocked
- Method 2 (WebFetch): 403 Forbidden, timeout, or empty response
- Method 3 (Browser Fetch): not available, fetch blocked, or incomplete content
- Method 4 (Browser Navigation): not available, redirect loop, or stale content issues

---

## Prompt the operator

```
All automated extraction methods failed for this URL.

Method 1 (curl): [reason -- not available / HTTP [code] / WAF challenge page]
Method 2 (WebFetch): [reason -- 403 / timeout / empty / summarized content]
Method 3 (Browser Fetch): [reason -- not available / fetch blocked / incomplete content]
Method 4 (Browser Navigation): [reason -- not available / redirect loop / stale content]

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

Apply formatting rules from `references/formatting-rules.md` where possible:
- Identify heading hierarchy from text patterns (lines that look like section headers)
- Preserve any markdown formatting already present
- URLs that appear as plain text: attempt to reconstruct as links if context suggests they were links

### If operator pastes HTML

Convert to markdown using the full rules in `references/formatting-rules.md`:
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
