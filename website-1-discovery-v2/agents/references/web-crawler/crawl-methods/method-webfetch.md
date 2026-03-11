# Method 2: WebFetch

Fallback when curl is unavailable or blocked. WebFetch is a built-in Claude Code tool that fetches a URL and processes the content through an AI model.

---

## Usage

Use WebFetch with the URL and the following prompt:

```
Extract ONLY the main content area of this page. Skip completely:
- Site header and top navigation bar
- Sidebars (left or right)
- Footer and bottom navigation
- Cookie banners and popups
- Breadcrumbs

IMPORTANT: Include content from ALL expandable/collapsible elements -- FAQs, accordions, toggles, "read more" sections, tabbed content, and <details>/<summary> elements. Treat all collapsed content as fully expanded.

CRITICAL -- You MUST preserve these elements exactly:
1. LINKS as [link text](URL "title") -- keep full URLs, include title attribute if present
2. IMAGES as ![alt text](image-src "title") -- keep full src URL, include alt and title
3. BOLD as **text**, ITALIC as *text* -- do NOT flatten to plain text

Also return:
- Heading hierarchy (h1 through h6 as # through ######)
- Bulleted lists as - items
- Numbered lists as 1. items
- Block quotes as > text
- Tables in markdown table format

Also extract from the HTML <head>:
- The <title> tag content (meta title)
- The <meta name="description"> value (meta description)

Format your response as:
META_TITLE: [title tag value]
META_DESCRIPTION: [meta description value]
FINAL_URL: [the actual URL of the page after any redirects]
---
[extracted markdown content]
```

---

## Redirect Detection

Check the `FINAL_URL` value in the response. If it differs from the requested URL, trigger redirect detection (see SKILL.md).

Note: WebFetch may not always report redirects accurately since the AI model processes the content. Cross-check by examining the page content -- if the H1 or topic doesn't match what was expected, a redirect likely occurred.

---

## When this method fails

Move to Method 3 (Browser Fetch) if:
- HTTP 403 Forbidden (bot protection -- Cloudflare, WAF, Sucuri)
- Timeout or empty response
- Content returned is a challenge page or CAPTCHA
- Content is clearly incomplete (JS-rendered page returned skeleton HTML)

WebFetch runs from cloud/datacenter IPs. If a site blocks datacenter IPs, WebFetch will always fail for that domain -- skip directly to Browser Fetch.

---

## Limitations

- No JavaScript execution. Cannot expand collapsed elements via interaction.
- Blocked by most WAFs and bot detection (Cloudflare, etc.) since it does not present a browser fingerprint.
- AI model may summarize or paraphrase content instead of preserving it verbatim. If the extracted content looks summarized rather than preserved, re-extract with a different method.
- Links and images are sometimes stripped during the AI processing step. Always verify preservation in the Review step.