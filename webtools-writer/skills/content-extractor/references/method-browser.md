# Method 3: Browser Extraction

Use browser MCP tools (Playwright or Chrome extension) when WebFetch is blocked by bot protection. The browser loads pages like a real user, bypassing Cloudflare/WAF restrictions and rendering JavaScript content.

---

## Known Pitfalls

<critical>
Before using this method, understand these known issues:

1. **Stale/cached content.** `get_page_content` and `browser_snapshot` can return content from a PREVIOUS tab or navigation, not the current page. Do NOT rely on them as the primary content source.

2. **Client-side JavaScript redirects.** Some sites redirect via JavaScript AFTER the page loads. The URL briefly shows the correct page, then JS changes it to a different page (e.g., /services/website-development/ loads correctly, then JS redirects to /services/). Server-side redirect detection (curl, HTTP headers) will NOT catch these. You MUST verify the URL via JavaScript at the moment of extraction.

3. **Tab pollution.** Navigating in an existing tab overwrites its content. Previous extractions leave tabs open that can interfere. ALWAYS open a new tab and close it after extraction.

4. **ALWAYS extract via `browser_evaluate` with direct DOM access.** This reads the LIVE DOM at the exact moment of execution, not cached or stale content.
</critical>

---

## Step-by-Step

### 1. Open a new tab

Use `browser_tabs` with action `"new"`. Do NOT navigate in an existing tab.

### 2. Navigate

Use `browser_navigate` to load the URL in the new tab. Wait for the page to fully load (2-3 seconds).

### 3. Verify URL and extract metadata (do this IMMEDIATELY)

Run a single `browser_evaluate` call right after page load -- before any client-side redirect has time to fire:

```javascript
() => {
  const url = window.location.href;
  const title = document.querySelector('title')?.textContent || '';
  const h1 = document.querySelector('h1')?.textContent || '';
  const desc = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
  const canonical = document.querySelector('link[rel="canonical"]')?.href || '';
  const ogUrl = document.querySelector('meta[property="og:url"]')?.getAttribute('content') || '';
  return { current_url: url, meta_title: title, h1: h1, meta_description: desc, canonical: canonical, og_url: ogUrl };
}
```

**Redirect check:** Compare `current_url`, `canonical`, and `og_url` with the requested URL. If ANY differ, a redirect has occurred. Also compare the `meta_title` and `h1` with what is expected for this page. Trigger redirect detection if mismatched (see SKILL.md).

### 4. Expand all collapsible content

```javascript
() => {
  // Expand <details> elements
  document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
  // Click accordion triggers (common patterns)
  document.querySelectorAll(
    '[aria-expanded="false"], .accordion-trigger, .faq-question, ' +
    '.collapse-toggle, [data-toggle="collapse"], .expandable:not(.expanded)'
  ).forEach(el => el.click());
  // Expand "read more" buttons
  document.querySelectorAll(
    '.read-more, .show-more, [data-action="expand"], .truncated-toggle'
  ).forEach(el => el.click());
  // Open all tabs to capture tabbed content
  document.querySelectorAll('.tab-trigger, [role="tab"]').forEach(el => el.click());
  return 'expanded';
}
```

Wait 1-2 seconds after expanding for content to render.

### 5. Extract content via live DOM

Do NOT use `get_page_content` or `browser_snapshot` as the primary source. Use `browser_evaluate` to read the live DOM:

```javascript
() => {
  // Find main content container
  const main = document.querySelector('main, article, [role="main"], .content, .page-content, #content')
    || document.querySelector('body');
  // Clone to avoid modifying the page
  const clone = main.cloneNode(true);
  // Remove chrome elements from clone
  clone.querySelectorAll(
    'header, footer, nav, aside, .sidebar, .nav, .header, .footer, ' +
    '.cookie-banner, .breadcrumb, .share-buttons, .related-posts, ' +
    '.comments, .ad, .advertisement'
  ).forEach(el => el.remove());
  return clone.innerHTML;
}
```

Then convert the returned HTML to markdown using the rules in `references/formatting-rules.md`.

### 6. Re-verify URL after extraction

Check `window.location.href` one more time via `browser_evaluate`. If the URL changed during extraction (client-side redirect fired mid-process), the content may be from the wrong page. Compare the H1 captured in step 3 with the H1 in the extracted content. If they don't match, warn the operator.

### 7. Close the tab

Close the tab after extraction using `browser_tabs` with action `"close"` to prevent tab pollution for future extractions.

### 8. Convert and proceed

Convert the extracted HTML to markdown using `references/formatting-rules.md`. Proceed to the Review step in SKILL.md.

---

## When this method fails

Move to Method 4 (Paste-in) if:
- Browser tools are not available in this session
- Navigation fails or times out
- Redirect cannot be resolved (page keeps redirecting)
- Content extraction returns empty or garbled HTML

---

## Limitations

- Depends on browser MCP being configured in the session.
- Tab management can be unreliable across MCP implementations (Playwright vs Chrome extension).
- Client-side redirects may fire faster than the extraction script, requiring multiple attempts.
- Large pages may exceed `browser_evaluate` return size limits.
