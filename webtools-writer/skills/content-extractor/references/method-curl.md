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
**Do NOT read raw HTML into context.** HTML files from real websites are typically 100-300KB. Reading them directly wastes context window on non-content markup.

**Use the html-to-markdown script** to convert raw HTML directly to markdown. The script handles: stripping non-content elements (head, script, style, noscript, svg, comments), finding the main content area, removing chrome (header/footer/nav/aside), converting all elements to markdown, and extracting metadata.

```bash
python3 scripts/html-to-markdown.py /tmp/extracted-page.html /tmp/extracted-content.md --base-url '[FINAL_URL]'
```

The script outputs a JSON summary to stdout:
```json
{
  "status": "ok",
  "output": "/tmp/extracted-content.md",
  "word_count": 842,
  "elements": {"headings": 19, "links": 13, "images": 1, "bold": 12, "italic": 0},
  "meta": {"meta_title": "...", "meta_description": "...", "canonical": "...", "og_url": "..."},
  "warnings": []
}
```

Use the JSON summary to verify extraction quality. If `status` is "warning", review the listed issues. Read the markdown file only if you need to review or edit it.

If `python3` is not available, fall back to the inline stripping approach: strip non-content tags via `node`, then read the stripped HTML and convert manually using `references/formatting-rules.md`.
</critical>

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
