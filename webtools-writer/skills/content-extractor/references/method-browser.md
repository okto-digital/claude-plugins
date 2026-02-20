# Method 3: Browser Extraction

Use browser MCP tools (Playwright or Chrome extension) when WebFetch is blocked by bot protection. The browser loads pages like a real user, bypassing Cloudflare/WAF restrictions and rendering JavaScript content.

---

## Known Pitfalls

<critical>
Before using this method, understand these known issues:

1. **Client-side JavaScript redirects.** Some sites (especially SPAs using Next.js, Nuxt, etc.) redirect via JavaScript AFTER the page loads. The URL briefly shows the correct page, then JS fires a navigation to a different page (e.g., /services/mobile-apps/ loads correctly, then within 1-3 seconds JS redirects to /services/). This makes multi-step extraction unreliable -- the page can redirect BETWEEN your JS calls. The solution is **atomic extraction**: capture everything in a single JS execution.

2. **Stale/cached content.** `get_page_content` and `browser_snapshot` can return content from a PREVIOUS tab or navigation, not the current page. Do NOT rely on them. ALWAYS extract via `browser_evaluate` with direct DOM access.

3. **Tab pollution.** Navigating in an existing tab overwrites its content. Previous extractions leave tabs open that can interfere. ALWAYS open a new tab and close it after extraction.
</critical>

---

## Step-by-Step

### 1. Open a new tab

Use `browser_tabs` with action `"new"`. Do NOT navigate in an existing tab.

### 2. Navigate

Use `browser_navigate` to load the URL in the new tab.

### 3. Inject redirect blocker

**IMMEDIATELY** after navigation, before waiting for full page load, inject a redirect blocker to prevent client-side JS from navigating away:

```javascript
() => {
  // Block SPA-style client-side redirects
  const origPushState = history.pushState;
  const origReplaceState = history.replaceState;
  history.pushState = function(...args) {
    console.log('[BLOCKED] pushState redirect to:', args[2]);
    return;  // silently block
  };
  history.replaceState = function(...args) {
    console.log('[BLOCKED] replaceState redirect to:', args[2]);
    return;  // silently block
  };
  // Block window.location assignments via beforeunload
  window.addEventListener('beforeunload', (e) => {
    e.preventDefault();
    e.returnValue = '';
  });
  // Store original URL for verification
  window.__extractorOriginalUrl = window.location.href;
  return 'redirect blocker injected';
}
```

This blocks the most common client-side redirect mechanisms: `history.pushState()`, `history.replaceState()`, and `window.location` assignments. SPA frameworks (Next.js, Nuxt, React Router) use pushState/replaceState for navigation.

Wait 2-3 seconds after injecting for the page to fully render its content.

### 4. Atomic extraction (single JS call)

<critical>
Do NOT split extraction across multiple `browser_evaluate` calls. Client-side redirects can fire between calls, causing you to capture content from a different page. Extract EVERYTHING in a single execution.
</critical>

Run this single comprehensive extraction script:

```javascript
() => {
  // --- URL & METADATA ---
  const currentUrl = window.location.href;
  const metaTitle = document.querySelector('title')?.textContent?.trim() || '';
  const h1 = document.querySelector('h1')?.textContent?.trim() || '';
  const metaDesc = document.querySelector('meta[name="description"]')?.getAttribute('content') || '';
  const canonical = document.querySelector('link[rel="canonical"]')?.href || '';
  const ogUrl = document.querySelector('meta[property="og:url"]')?.getAttribute('content') || '';

  // --- EXPAND COLLAPSIBLES ---
  document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
  document.querySelectorAll(
    '[aria-expanded="false"], .accordion-trigger, .faq-question, ' +
    '.collapse-toggle, [data-toggle="collapse"], .expandable:not(.expanded)'
  ).forEach(el => { try { el.click(); } catch(e) {} });
  document.querySelectorAll(
    '.read-more, .show-more, [data-action="expand"], .truncated-toggle'
  ).forEach(el => { try { el.click(); } catch(e) {} });

  // --- FIND MAIN CONTENT ---
  const main = document.querySelector('main, article, [role="main"], .content, .page-content, #content')
    || document.querySelector('body');
  const clone = main.cloneNode(true);

  // Remove chrome elements
  clone.querySelectorAll(
    'header, footer, nav, aside, .sidebar, .nav, .header, .footer, ' +
    '.cookie-banner, .breadcrumb, .share-buttons, .related-posts, ' +
    '.comments, .ad, .advertisement, script, style, noscript'
  ).forEach(el => el.remove());

  // --- EXTRACT LINKS ---
  const links = [];
  clone.querySelectorAll('a[href]').forEach(a => {
    const href = a.href || a.getAttribute('href') || '';
    const text = a.textContent?.trim() || '';
    const title = a.getAttribute('title') || '';
    if (text && href && !href.startsWith('javascript:')) {
      links.push({ text, href, title });
    }
  });

  // --- EXTRACT IMAGES ---
  const images = [];
  clone.querySelectorAll('img[src]').forEach(img => {
    images.push({
      src: img.src || img.getAttribute('src') || '',
      alt: img.getAttribute('alt') || '',
      title: img.getAttribute('title') || ''
    });
  });

  // --- EXTRACT FAQ / ACCORDION Q&A ---
  const faqs = [];
  // Common FAQ patterns: dt/dd, question/answer pairs, details/summary
  clone.querySelectorAll('details').forEach(d => {
    const q = d.querySelector('summary')?.textContent?.trim() || '';
    const a = d.querySelector('summary')?.nextElementSibling?.textContent?.trim()
      || d.textContent?.replace(q, '')?.trim() || '';
    if (q) faqs.push({ question: q, answer: a });
  });
  // Also check aria-based accordions
  clone.querySelectorAll('[aria-expanded]').forEach(trigger => {
    const q = trigger.textContent?.trim() || '';
    const targetId = trigger.getAttribute('aria-controls');
    const panel = targetId ? document.getElementById(targetId) : trigger.nextElementSibling;
    const a = panel?.textContent?.trim() || '';
    if (q && a && q !== a) faqs.push({ question: q, answer: a });
  });

  // --- EXTRACT HTML CONTENT ---
  const html = clone.innerHTML;

  // --- EXTRACT BOLD TEXT (for verification) ---
  const boldCount = (clone.querySelectorAll('strong, b') || []).length;
  const italicCount = (clone.querySelectorAll('em, i') || []).length;

  return {
    url: currentUrl,
    original_url: window.__extractorOriginalUrl || currentUrl,
    meta_title: metaTitle,
    meta_description: metaDesc,
    h1: h1,
    canonical: canonical,
    og_url: ogUrl,
    html: html,
    links: links,
    images: images,
    faqs: faqs,
    stats: {
      link_count: links.length,
      image_count: images.length,
      faq_count: faqs.length,
      bold_count: boldCount,
      italic_count: italicCount
    }
  };
}
```

This returns a single JSON object with everything needed for the extraction.

### 5. Validate the extraction result

Check the returned data:

- **Redirect check:** Compare `url` and `original_url`. If they differ, the redirect blocker failed or a different redirect mechanism was used. Compare `canonical` and `og_url` with the requested URL. Check that the `h1` matches expectations for the requested page, not a parent/hub page.
- **Content check:** Verify `html` contains substantial content (not empty or just navigation). The `h1` should match the expected page title.
- **Links/images check:** Verify `links` array contains page-specific links (not just global nav links). Verify `images` array has expected images.
- **FAQ check:** If the page has visible FAQs/accordions, verify `faqs` captured them with both questions and answers.

If the `h1` or content clearly belongs to a different page (e.g., a services hub instead of a specific service page), the extraction captured the wrong content. Re-navigate and retry, or trigger redirect detection (see SKILL.md).

### 6. Convert to markdown

Using the `html` from the extraction result, convert to markdown following `references/formatting-rules.md`. Supplement with the structured data:

- Use `links` array to verify all links made it into the markdown with full URLs.
- Use `images` array to verify all images made it in with alt text and src.
- Use `faqs` array to verify FAQ content is complete (questions AND answers).
- Use `stats` to report counts in the presentation step.

### 7. Close the tab

Close the tab after extraction using `browser_tabs` with action `"close"` to prevent tab pollution for future extractions.

### 8. Proceed

Proceed to the Review step in SKILL.md.

---

## If the redirect blocker doesn't work

Some redirects use mechanisms the blocker can't catch (e.g., `window.location.href = ...` assignments, meta refresh tags, or server-side redirects after AJAX calls). If extraction still captures the wrong page after injecting the blocker:

1. **Retry with immediate extraction.** Skip the redirect blocker. Navigate and run the atomic extraction script immediately (within 1 second of navigation), racing the redirect.
2. **Try multiple rapid attempts.** Navigate, extract immediately, check the H1. If wrong, navigate again and extract faster.
3. **If the page consistently redirects**, it may genuinely redirect (not a separate page). Inform the operator and trigger redirect detection (see SKILL.md).

---

## When this method fails

Move to Method 4 (Paste-in) if:
- Browser tools are not available in this session
- Navigation fails or times out
- Redirect cannot be resolved after 3 attempts
- Content extraction returns empty or garbled HTML

---

## Limitations

- Depends on browser MCP being configured in the session.
- Tab management can be unreliable across MCP implementations (Playwright vs Chrome extension).
- Redirect blocker cannot catch ALL redirect mechanisms (direct `window.location` assignment in some environments).
- Large pages may exceed `browser_evaluate` return size limits -- if content is truncated, extract in two calls: first half and second half of the DOM.
