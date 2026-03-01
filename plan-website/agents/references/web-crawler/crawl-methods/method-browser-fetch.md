# Method 4: Chrome Control Fetch

Use the browser's `fetch()` API to retrieve raw HTML from the user's browser via Chrome Control MCP (`mcp__Control_Chrome__*`). This combines the reliability of curl (raw HTML, no JS execution, clean redirect detection) with the browser's advantage (user's IP address, bypasses WAF/bot protection).

---

## Why this method exists

In cloud environments (e.g., Cowork), curl and WebFetch run from datacenter IPs that get blocked by WAFs (403 Forbidden). Chrome Control MCP tools run in the user's local browser. By using `fetch()` inside the browser, we make an HTTP request from the user's machine -- same IP, same cookies -- but without navigating to the page. This avoids all the tab management, stale content, and client-side redirect problems of full browser navigation.

---

## Prerequisites

- Chrome Control MCP tools must be available (`mcp__Control_Chrome__*`)
- `mcp__Control_Chrome__execute_javascript` must be functional

---

## Step-by-Step

### 1. Open URL and establish origin

Open the **domain root** of the target URL in the browser. This establishes same-origin context so `fetch()` works without CORS issues.

```
mcp__Control_Chrome__open_url(url: "https://[domain]/")
```

For example, if the target URL is `https://oktodigital.com/services/website-development/`, open `https://oktodigital.com/`.

Wait for the page to load (1-2 seconds is sufficient -- we only need the origin established, not the full page content).

### 2. Fetch the target page via JavaScript

Use `mcp__Control_Chrome__execute_javascript` to run a single `fetch()` call that retrieves the raw HTML and extracts everything:

```javascript
async () => {
  const targetPath = '/services/website-development/';
  const response = await fetch(targetPath, {
    method: 'GET',
    credentials: 'same-origin',
    headers: {
      'Accept': 'text/html,application/xhtml+xml'
    }
  });

  const finalUrl = response.url;
  const redirected = response.redirected;
  const status = response.status;
  const html = await response.text();

  // Parse the HTML
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');

  // --- METADATA ---
  const metaTitle = doc.querySelector('title')?.textContent?.trim() || '';
  const h1 = doc.querySelector('h1')?.textContent?.trim() || '';
  const metaDesc = doc.querySelector('meta[name="description"]')?.getAttribute('content') || '';
  const canonical = doc.querySelector('link[rel="canonical"]')?.getAttribute('href') || '';
  const ogUrl = doc.querySelector('meta[property="og:url"]')?.getAttribute('content') || '';

  // --- FIND MAIN CONTENT ---
  const main = doc.querySelector('main, article, [role="main"], .content, .page-content, #content')
    || doc.querySelector('body');
  const clone = main.cloneNode(true);

  // Remove chrome elements
  clone.querySelectorAll(
    'header, footer, nav, aside, .sidebar, .nav, .header, .footer, ' +
    '.cookie-banner, .breadcrumb, .share-buttons, .related-posts, ' +
    '.comments, .ad, .advertisement, script, style, noscript'
  ).forEach(el => el.remove());

  // --- EXTRACT LINKS ---
  const baseUrl = new URL(finalUrl);
  const links = [];
  clone.querySelectorAll('a[href]').forEach(a => {
    const rawHref = a.getAttribute('href') || '';
    let href = rawHref;
    try { href = new URL(rawHref, baseUrl).href; } catch(e) {}
    const text = a.textContent?.trim() || '';
    const title = a.getAttribute('title') || '';
    if (text && href && !href.startsWith('javascript:')) {
      links.push({ text, href, title });
    }
  });

  // --- EXTRACT IMAGES ---
  const images = [];
  clone.querySelectorAll('img[src]').forEach(img => {
    const rawSrc = img.getAttribute('src') || '';
    let src = rawSrc;
    try { src = new URL(rawSrc, baseUrl).href; } catch(e) {}
    images.push({
      src: src,
      alt: img.getAttribute('alt') || '',
      title: img.getAttribute('title') || ''
    });
  });

  // --- EXTRACT FAQ / ACCORDION Q&A ---
  const faqs = [];
  clone.querySelectorAll('details').forEach(d => {
    const q = d.querySelector('summary')?.textContent?.trim() || '';
    const a = d.querySelector('summary')?.nextElementSibling?.textContent?.trim()
      || d.textContent?.replace(q, '')?.trim() || '';
    if (q) faqs.push({ question: q, answer: a });
  });

  // --- CONTENT HTML ---
  const contentHtml = clone.innerHTML;
  const boldCount = (clone.querySelectorAll('strong, b') || []).length;
  const italicCount = (clone.querySelectorAll('em, i') || []).length;

  return {
    status: status,
    redirected: redirected,
    final_url: finalUrl,
    meta_title: metaTitle,
    meta_description: metaDesc,
    h1: h1,
    canonical: canonical,
    og_url: ogUrl,
    html: contentHtml,
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

**IMPORTANT:** Replace `targetPath` with the actual path of the page being extracted. Use a relative path (e.g., `/services/website-development/`) since we are same-origin.

### 3. Validate the result

Check the returned data:

- **HTTP status:** Must be 200. If 403/404/5xx, this method failed -- move to Method 5 (Chrome Automation Navigation).
- **Redirect check:** If `redirected` is `true`, compare `final_url` with the requested URL. Trigger redirect detection (see SKILL.md).
- **Content check:** Verify `html` contains substantial content (not empty or just navigation). The `h1` should match the expected page.
- **Links/images check:** Verify `links` and `images` arrays have entries.

### 4. Convert to markdown

Using the `html` from the extraction result, convert to markdown following `references/formatting-rules.md`. Supplement with the structured data:

- Use `links` array to verify all links made it into the markdown with full URLs.
- Use `images` array to verify all images made it in with alt text and src.
- Use `faqs` array to verify FAQ content is complete (questions AND answers).
- Use `stats` to report counts in the presentation step.

### 5. Close the tab

Close the tab using `mcp__Control_Chrome__close_tab`.

### 6. Proceed

Proceed to the Review step in SKILL.md.

---

## When this method fails

Move to Method 5 (Chrome Automation Navigation) if:
- `fetch()` returns non-200 status
- Response is empty, a challenge page, or CAPTCHA HTML
- Content is clearly incomplete (some sites block fetch but allow full page loads)
- The page requires JavaScript rendering to produce content (SPAs that return skeleton HTML)

Move to Method 7 (Paste-in) if Chrome Automation Navigation also fails.

---

## Limitations

- **No JavaScript execution on the fetched page.** The HTML is parsed via `DOMParser`, not rendered. Collapsed elements (`<details>`) are in the HTML source and extractable, but content injected by client-side JS after page load will be missing.
- **Same-origin only.** Must open the target domain first to avoid CORS errors.
- **Depends on Chrome Control MCP** (`mcp__Control_Chrome__*`) being configured in the session.
- **Large pages** may exceed `execute_javascript` return size limits. If content is truncated, extract metadata and content in two separate fetch+parse calls.