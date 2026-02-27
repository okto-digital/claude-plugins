# Method 1: curl + Local Processing

Preferred extraction method. curl follows redirects transparently, reports the final URL, and fetches raw HTML. Most reliable for redirect detection.

**Requires shell access.** This method works with any shell execution tool -- Bash, Desktop Commander, terminal MCP, or similar. If no shell tool is available, skip to Method 2.

<critical>
**Shell tool priority in cloud environments (Cowork):**
If multiple shell tools are available, prefer tools that execute on the **user's local machine** (e.g., Desktop Commander) over tools that execute on the **cloud VM** (e.g., Bash in Cowork). Cloud VMs use datacenter IPs that get blocked by WAFs (curl exits with code 56 or returns 403). Desktop Commander runs on the user's machine with their residential/office IP, bypassing WAF restrictions.

**If the first curl attempt fails with exit code 56 (connection reset) or HTTP 403, and Desktop Commander is available, retry immediately via Desktop Commander before moving to Method 2.** Do not waste attempts retrying with the same tool.
</critical>

---

## Step 1: Fetch raw HTML

Run via any available shell tool (preferring Desktop Commander over VM Bash in cloud environments):

```bash
curl -sL -w '\n__FINAL_URL__:%{url_effective}\n__HTTP_CODE__:%{http_code}' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -o /tmp/extracted-page.html \
  '[URL]'
```

Check the output:
- `__FINAL_URL__`: Compare with the requested URL. If different, trigger redirect detection (see SKILL.md).
- `__HTTP_CODE__`: If not 200, this method failed -- move to Method 2.
- If the HTML file is empty or under 500 bytes, this method failed -- move to Method 2.

---

## Step 2: Extract meta tags

Run via shell (or read the file directly and extract manually):

```bash
# Extract meta title
grep -oPm1 '(?<=<title>).*?(?=</title>)' /tmp/extracted-page.html

# Extract meta description
grep -oPm1 '<meta[^>]*name=["\x27]description["\x27][^>]*content=["\x27]\K[^"\x27]*' /tmp/extracted-page.html
```

If grep patterns fail (multiline title tags, different quote styles), read the HTML file directly and extract the values manually.

---

## Step 3: Convert HTML to markdown

<critical>
**Check file size before reading.** HTML files from real websites are typically 100-300KB due to inline CSS, JavaScript, cookie consent banners, JSON-LD schema, and other non-content markup. Reading a large HTML file directly will overflow the context window.

**ALWAYS strip non-content elements via shell BEFORE reading the HTML into context.** Run the following Python script (stdlib only, no pip packages needed) via the same shell tool used for curl:

```bash
python3 << 'PYEOF'
import re

with open('/tmp/extracted-page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Remove head section entirely
html = re.sub(r'<head[^>]*>.*?</head>', '', html, flags=re.DOTALL)

# Remove script, style, noscript, svg tags and their contents
for tag in ['script', 'style', 'noscript', 'svg']:
    html = re.sub(rf'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL)

# Remove HTML comments (cookie consent configs, GTM, etc.)
html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

# Remove inline style attributes
html = re.sub(r'\s+style="[^"]*"', '', html)

# Collapse whitespace runs
html = re.sub(r'\n\s*\n', '\n\n', html)

with open('/tmp/extracted-content.html', 'w', encoding='utf-8') as f:
    f.write(html.strip())

import os
original = os.path.getsize('/tmp/extracted-page.html')
stripped = os.path.getsize('/tmp/extracted-content.html')
print(f'Stripped: {original/1024:.0f}KB -> {stripped/1024:.0f}KB ({100-stripped/original*100:.0f}% removed)')
PYEOF
```

Then read `/tmp/extracted-content.html` (not the original) for conversion.

If `python3` is not available, use `python` instead. If neither is available, try `node`:

```bash
node -e "
const fs = require('fs');
let html = fs.readFileSync('/tmp/extracted-page.html', 'utf8');
html = html.replace(/<head[^>]*>[\s\S]*?<\/head>/gi, '');
['script','style','noscript','svg'].forEach(t => {
  html = html.replace(new RegExp('<'+t+'[^>]*>[\\\\s\\\\S]*?</'+t+'>','gi'), '');
});
html = html.replace(/<!--[\s\S]*?-->/g, '');
html = html.replace(/\s+style=\"[^\"]*\"/g, '');
html = html.replace(/\n\s*\n/g, '\n\n');
fs.writeFileSync('/tmp/extracted-content.html', html.trim());
const o = fs.statSync('/tmp/extracted-page.html').size;
const s = fs.statSync('/tmp/extracted-content.html').size;
console.log('Stripped: '+(o/1024|0)+'KB -> '+(s/1024|0)+'KB ('+(100-s/o*100|0)+'% removed)');
"
```
</critical>

After stripping, read `/tmp/extracted-content.html` and convert the main content to markdown.

1. Identify the main content area (see `references/formatting-rules.md` for selectors).
2. Apply all conversion rules from `references/formatting-rules.md`.
3. Verify critical preservation requirements (links, images, formatting, collapsible content).

---

## When this method fails

Move to Method 2 (WebFetch) if:
- No shell tool is available (no Bash, Desktop Commander, or similar)
- `which curl` returns nothing (curl not installed)
- HTTP status code is not 200 (403 Forbidden, 5xx, etc.)
- HTML file is empty or under 500 bytes
- HTML is a Cloudflare/WAF challenge page (look for "cf-browser-verification", "challenge-platform", or similar markers in the HTML)

---

## Limitations

- Cannot execute JavaScript. Pages that render content client-side (SPAs, React/Vue/Angular apps) will return empty or skeleton HTML.
- Cannot bypass aggressive bot protection (Cloudflare with JS challenge, CAPTCHA).
- Cannot interact with the page (no clicking, no expanding collapsed elements via JS -- but `<details>` elements are in the source HTML and can be extracted).
