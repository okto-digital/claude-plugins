# Method 1: curl + Local Processing

Preferred extraction method. curl follows redirects transparently, reports the final URL, and fetches raw HTML. Most reliable for redirect detection.

---

## Step 1: Fetch raw HTML

Run via Bash:

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

Run via Bash:

```bash
# Extract meta title
grep -oPm1 '(?<=<title>).*?(?=</title>)' /tmp/extracted-page.html

# Extract meta description
grep -oPm1 '<meta[^>]*name=["\x27]description["\x27][^>]*content=["\x27]\K[^"\x27]*' /tmp/extracted-page.html
```

If grep patterns fail (multiline title tags, different quote styles), read the HTML file directly and extract the values manually.

---

## Step 3: Convert HTML to markdown

Read `/tmp/extracted-page.html` and convert the main content to markdown.

1. Identify the main content area (see `references/formatting-rules.md` for selectors).
2. Apply all conversion rules from `references/formatting-rules.md`.
3. Verify critical preservation requirements (links, images, formatting, collapsible content).

---

## When this method fails

Move to Method 2 (WebFetch) if:
- `which curl` returns nothing (curl not installed)
- HTTP status code is not 200 (403 Forbidden, 5xx, etc.)
- HTML file is empty or under 500 bytes
- HTML is a Cloudflare/WAF challenge page (look for "cf-browser-verification", "challenge-platform", or similar markers in the HTML)

---

## Limitations

- Cannot execute JavaScript. Pages that render content client-side (SPAs, React/Vue/Angular apps) will return empty or skeleton HTML.
- Cannot bypass aggressive bot protection (Cloudflare with JS challenge, CAPTCHA).
- Cannot interact with the page (no clicking, no expanding collapsed elements via JS -- but `<details>` elements are in the source HTML and can be extracted).
