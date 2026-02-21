# Method 3: Browser Fetch

Use the browser's `fetch()` API to retrieve raw HTML from the user's browser. This combines the reliability of curl (raw HTML, no JS execution, clean redirect detection) with the browser's advantage (user's IP address, bypasses WAF/bot protection).

---

## Why this method exists

In cloud environments (e.g., Cowork), curl and WebFetch run from datacenter IPs that get blocked by WAFs (403 Forbidden). Browser MCP tools run in the user's local browser. By using `fetch()` inside the browser, we make an HTTP request from the user's machine -- same IP, same cookies -- but without navigating to the page. This avoids all the tab management, stale content, and client-side redirect problems of full browser navigation.

---

## Prerequisites

- Browser MCP tools must be available (Playwright or Chrome extension)
- `browser_evaluate` must be functional

---

## Step-by-Step

### 1. Open a new tab and establish origin

Open a new tab and navigate to the **domain root** of the target URL. This establishes same-origin context so `fetch()` works without CORS issues.

```
browser_tabs → action: "new"
browser_navigate → https://[domain]/
```

For example, if the target URL is `https://oktodigital.com/services/website-development/`, navigate to `https://oktodigital.com/`.

Wait for the page to load (1-2 seconds is sufficient -- we only need the origin established, not the full page content).

### 2. Fetch the target page via JavaScript

Use `browser_evaluate` to run a single `fetch()` call that retrieves the raw HTML and extracts everything:

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

  // --- CONVERT DOM TO MARKDOWN (inline, no intermediate HTML in context) ---
  function domToMd(el) {
    let md = '';
    for (const node of el.childNodes) {
      if (node.nodeType === 3) { // text
        md += node.textContent;
      } else if (node.nodeType === 1) { // element
        const tag = node.tagName.toLowerCase();
        if (['script','style','noscript','svg','template'].includes(tag)) continue;
        const hMatch = tag.match(/^h([1-6])$/);
        if (hMatch) {
          md += '\n\n' + '#'.repeat(+hMatch[1]) + ' ' + inlineMd(node) + '\n';
        } else if (tag === 'p') {
          md += '\n\n' + inlineMd(node) + '\n';
        } else if (tag === 'ul' || tag === 'ol') {
          md += '\n\n' + listMd(node, tag === 'ol') + '\n';
        } else if (tag === 'blockquote') {
          md += '\n\n' + inlineMd(node).split('\n').map(l => '> ' + l).join('\n') + '\n';
        } else if (tag === 'table') {
          md += '\n\n' + tableMd(node) + '\n';
        } else if (tag === 'hr') {
          md += '\n\n---\n';
        } else if (tag === 'br') {
          md += '\n';
        } else if (tag === 'img') {
          const src = node.src || node.getAttribute('src') || '';
          const alt = node.getAttribute('alt') || '';
          md += '\n\n![' + alt + '](' + src + ')\n';
        } else if (tag === 'details') {
          const sum = node.querySelector('summary');
          if (sum) md += '\n\n### ' + sum.textContent.trim() + '\n';
          for (const ch of node.childNodes) {
            if (ch !== sum && ch.nodeType === 1) md += '\n\n' + inlineMd(ch) + '\n';
          }
        } else {
          md += domToMd(node);
        }
      }
    }
    return md;
  }
  function inlineMd(el) {
    let out = '';
    for (const n of el.childNodes) {
      if (n.nodeType === 3) { out += n.textContent; continue; }
      if (n.nodeType !== 1) continue;
      const t = n.tagName.toLowerCase();
      if (t === 'strong' || t === 'b') out += '**' + inlineMd(n) + '**';
      else if (t === 'em' || t === 'i') out += '*' + inlineMd(n) + '*';
      else if (t === 'code') out += '`' + n.textContent + '`';
      else if (t === 'a') {
        const href = n.href || n.getAttribute('href') || '';
        const text = inlineMd(n);
        const title = n.getAttribute('title');
        if (text.trim() && href) {
          out += title ? '[' + text.trim() + '](' + href + ' "' + title + '")' : '[' + text.trim() + '](' + href + ')';
        }
      } else if (t === 'img') {
        out += '![' + (n.getAttribute('alt')||'') + '](' + (n.src||n.getAttribute('src')||'') + ')';
      } else if (t === 'br') { out += '\n'; }
      else { out += inlineMd(n); }
    }
    return out;
  }
  function listMd(el, ordered) {
    const items = [];
    let idx = 1;
    for (const li of el.children) {
      if (li.tagName.toLowerCase() === 'li') {
        items.push((ordered ? (idx++) + '. ' : '- ') + inlineMd(li).trim());
      }
    }
    return items.join('\n');
  }
  function tableMd(el) {
    const rows = [];
    el.querySelectorAll('tr').forEach(tr => {
      const cells = [];
      tr.querySelectorAll('th, td').forEach(c => cells.push(inlineMd(c).trim()));
      rows.push('| ' + cells.join(' | ') + ' |');
    });
    if (rows.length > 1) rows.splice(1, 0, '|' + rows[0].split('|').slice(1,-1).map(()=>'---|').join(''));
    return rows.join('\n');
  }

  const markdown = domToMd(clone).replace(/\n{3,}/g, '\n\n').trim();
  const boldCount = (clone.querySelectorAll('strong, b') || []).length;
  const italicCount = (clone.querySelectorAll('em, i') || []).length;
  const wordCount = markdown.split(/\s+/).filter(Boolean).length;

  return {
    status: status,
    redirected: redirected,
    final_url: finalUrl,
    meta_title: metaTitle,
    meta_description: metaDesc,
    h1: h1,
    canonical: canonical,
    og_url: ogUrl,
    markdown: markdown,
    links: links,
    images: images,
    faqs: faqs,
    stats: {
      word_count: wordCount,
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

- **HTTP status:** Must be 200. If 403/404/5xx, this method failed -- move to Method 4 (Browser Navigation).
- **Redirect check:** If `redirected` is `true`, compare `final_url` with the requested URL. Trigger redirect detection (see SKILL.md).
- **Content check:** Verify `html` contains substantial content (not empty or just navigation). The `h1` should match the expected page.
- **Links/images check:** Verify `links` and `images` arrays have entries.

### 4. Use the markdown output

The extraction script now returns `markdown` directly (DOM-to-markdown conversion runs in the browser). There is no `html` field -- the DOM is converted to markdown inline, saving the agent from reading raw HTML into context.

Review the `markdown` field and verify quality using the structured data:

- Use `links` array to verify all links made it into the markdown with full URLs.
- Use `images` array to verify all images made it in with alt text and src.
- Use `faqs` array to verify FAQ content is complete (questions AND answers).
- Use `stats` to report counts (including `word_count`) in the presentation step.
- If the markdown quality is poor (missing sections, broken formatting), write it to the output file and review/fix manually rather than re-extracting.

### 5. Close the tab

Close the tab using `browser_tabs` with action `"close"`.

### 6. Proceed

Proceed to the Review step in SKILL.md.

---

## When this method fails

Move to Method 4 (Browser Navigation) if:
- `fetch()` returns non-200 status
- Response is empty, a challenge page, or CAPTCHA HTML
- Content is clearly incomplete (some sites block fetch but allow full page loads)
- The page requires JavaScript rendering to produce content (SPAs that return skeleton HTML)

Move to Method 5 (Paste-in) if Browser Navigation also fails.

---

## Limitations

- **No JavaScript execution on the fetched page.** The HTML is parsed via `DOMParser`, not rendered. Collapsed elements (`<details>`) are in the HTML source and extractable, but content injected by client-side JS after page load will be missing.
- **Same-origin only.** Must navigate to the target domain first to avoid CORS errors.
- **Depends on browser MCP** being configured in the session.
- **Large pages** may exceed `browser_evaluate` return size limits. If content is truncated, extract metadata and content in two separate fetch+parse calls.
