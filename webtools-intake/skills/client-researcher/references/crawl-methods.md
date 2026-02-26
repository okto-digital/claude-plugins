# Crawl Methods Cascade

Detailed instructions for each crawling method. Try methods in priority order. Move to the next only when the current one fails.

---

## Method 1: curl + Local Processing (Preferred)

Requires shell access (Bash, Desktop Commander, terminal MCP, or similar) and curl installed.

### Fetch page

```bash
curl -sL -w '\n__FINAL_URL__:%{url_effective}\n__HTTP_CODE__:%{http_code}' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -o /tmp/research-page.html \
  '[URL]'
```

Check the output:
- `__FINAL_URL__`: Compare with requested URL. Note redirects.
- `__HTTP_CODE__`: If not 200, this method failed -- move to Method 2.
- If HTML file is empty or under 500 bytes, this method failed.

### Strip non-content elements

<critical>
HTML files from real websites are typically 100-300KB. ALWAYS strip non-content elements via shell BEFORE reading into context.
</critical>

```bash
python3 << 'PYEOF'
import re

with open('/tmp/research-page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Remove head section entirely
html = re.sub(r'<head[^>]*>.*?</head>', '', html, flags=re.DOTALL)

# Remove script, style, noscript, svg tags and their contents
for tag in ['script', 'style', 'noscript', 'svg']:
    html = re.sub(rf'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL)

# Remove HTML comments
html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

# Remove inline style attributes
html = re.sub(r'\s+style="[^"]*"', '', html)

# Collapse whitespace runs
html = re.sub(r'\n\s*\n', '\n\n', html)

with open('/tmp/research-content.html', 'w', encoding='utf-8') as f:
    f.write(html.strip())

import os
original = os.path.getsize('/tmp/research-page.html')
stripped = os.path.getsize('/tmp/research-content.html')
print(f'Stripped: {original/1024:.0f}KB -> {stripped/1024:.0f}KB ({100-stripped/original*100:.0f}% removed)')
PYEOF
```

If `python3` is not available, use `python`. If neither, use `node`:

```bash
node -e "
const fs = require('fs');
let html = fs.readFileSync('/tmp/research-page.html', 'utf8');
html = html.replace(/<head[^>]*>[\s\S]*?<\/head>/gi, '');
['script','style','noscript','svg'].forEach(t => {
  html = html.replace(new RegExp('<'+t+'[^>]*>[\\\\s\\\\S]*?</'+t+'>','gi'), '');
});
html = html.replace(/<!--[\s\S]*?-->/g, '');
html = html.replace(/\s+style=\\\"[^\\\"]*\\\"/g, '');
html = html.replace(/\n\s*\n/g, '\n\n');
fs.writeFileSync('/tmp/research-content.html', html.trim());
const o = fs.statSync('/tmp/research-page.html').size;
const s = fs.statSync('/tmp/research-content.html').size;
console.log('Stripped: '+(o/1024|0)+'KB -> '+(s/1024|0)+'KB ('+(100-s/o*100|0)+'% removed)');
"
```

Then read `/tmp/research-content.html` (not the original) for intelligence extraction.

### Extract meta tags

```bash
# Meta title
grep -oPm1 '(?<=<title>).*?(?=</title>)' /tmp/research-page.html

# Meta description
grep -oPm1 '<meta[^>]*name=["\x27]description["\x27][^>]*content=["\x27]\K[^"\x27]*' /tmp/research-page.html

# Meta generator (CMS detection)
grep -oPm1 '<meta[^>]*name=["\x27]generator["\x27][^>]*content=["\x27]\K[^"\x27]*' /tmp/research-page.html
```

If grep patterns fail (multiline tags, different quote styles), read the HTML directly and extract manually.

### When this method fails

Move to Method 2 if:
- No shell tool available
- curl not installed
- HTTP status not 200 (403, 5xx, etc.)
- HTML empty or under 500 bytes
- HTML is a WAF challenge page (look for "cf-browser-verification", "challenge-platform")

<critical>
Shell tool priority in cloud environments (Cowork): prefer tools that execute on the user's local machine (Desktop Commander) over cloud VM tools (Bash in Cowork). Cloud VMs use datacenter IPs blocked by WAFs. If curl fails with exit code 56 or HTTP 403, and Desktop Commander is available, retry via Desktop Commander before moving to Method 2.
</critical>

---

## Method 2: WebFetch

Use when curl is unavailable or blocked. WebFetch runs from cloud servers and is blocked by most WAF-protected sites.

Call WebFetch with the page URL and a prompt tailored to intelligence extraction:

```
Prompt: "Extract the main content of this page. Include: all headings and their hierarchy, all body text, all links with their URLs, all image alt text descriptions, any meta information visible on the page, navigation menu items, footer content, and any structured data. Preserve the content structure."
```

Read the WebFetch response and extract intelligence observations.

### When this method fails

Move to Method 3 if:
- WebFetch returns 403 or access denied
- Response is a WAF challenge or CAPTCHA page
- Content is empty or clearly truncated

<critical>
If the target site is behind WAF/bot protection and WebFetch returns 403, skip directly to Method 3 (Browser Fetch). Do not retry WebFetch -- it will always fail for that domain.
</critical>

---

## Method 3: Browser Fetch (fetch API)

Use when WebFetch is blocked. Runs `fetch()` in the user's browser, which uses their residential IP.

Requires browser tools to be available (`browser_evaluate` or equivalent).

Execute in the browser console:

```javascript
fetch('[URL]')
  .then(r => r.text())
  .then(html => {
    // Return a truncated version to avoid context overflow
    const stripped = html
      .replace(/<head[^>]*>[\s\S]*?<\/head>/gi, '')
      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
      .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
      .replace(/<noscript[^>]*>[\s\S]*?<\/noscript>/gi, '')
      .replace(/<!--[\s\S]*?-->/g, '');
    return stripped.substring(0, 50000);
  });
```

### When this method fails

Move to Method 4 if:
- Browser tools not available
- fetch() blocked by CORS
- Page requires JavaScript rendering (SPA)

---

## Method 4: Browser Navigation

Use when Browser Fetch fails. Full page load in the user's browser.

1. Navigate to the URL using browser navigation tools
2. Wait for page load to complete
3. Extract the page content via browser evaluation:

```javascript
document.documentElement.outerHTML.substring(0, 50000);
```

Or use a browser snapshot tool if available.

### When this method fails

Move to Method 5 if:
- Browser tools not available
- Page fails to load
- Content is behind authentication

---

## Method 5: Manual Paste-in (Last Resort)

When all automated methods fail for a specific page:

```
[PAGE FETCH FAILED] /example-page

All automated methods failed for this URL.

Options:
(a) Open the page in your browser, select all content (Cmd+A / Ctrl+A),
    copy it, and paste it here. I will extract intelligence from the pasted text.
(b) Skip this page and continue with the remaining pages.
```

If the operator pastes content, extract intelligence from the pasted text. Pasted content will lack HTML structure, so focus on text-based intelligence (business claims, service descriptions, audience signals) rather than technical indicators (meta tags, schema markup).

---

## Multi-Page Crawling Efficiency

When crawling multiple pages with curl:
- Reuse the same temp file (`/tmp/research-page.html`) for each page -- overwrite between pages
- Run the strip + read cycle for each page individually
- Do not attempt to batch-download all pages at once
- Track which method succeeded for each page (useful for the progress report)

If curl works for the first page but fails for a subsequent page on the same domain, retry once before falling back. Intermittent failures happen.
