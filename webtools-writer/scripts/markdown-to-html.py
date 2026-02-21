#!/usr/bin/env python3
"""
markdown-to-html.py -- Convert markdown content with YAML frontmatter to clean semantic HTML.

Follows html-export-rules.md:
- Strip YAML frontmatter, preserve meta_title and meta_description
- Convert all markdown elements to semantic HTML
- Output ONLY content markup (no <html>, <head>, <body> wrapper)
- No CSS, classes, IDs, or styling attributes
- Metadata comment + <title> + <meta> tags at top

Usage:
  markdown-to-html.py INPUT.md OUTPUT.html
  markdown-to-html.py INPUT.md              # writes to INPUT.html (same dir)

Output: JSON summary to stdout.
"""

import sys
import re
import json
import os
from datetime import date
from html import escape as html_escape


# ---------------------------------------------------------------------------
# YAML frontmatter extraction
# ---------------------------------------------------------------------------

def extract_frontmatter(text):
    """Extract and remove YAML frontmatter. Return (meta_dict, body)."""
    meta = {}
    body = text

    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = text[fm_match.end():]

        for key in ("meta_title", "meta_description", "source_url", "title"):
            m = re.search(
                r'^' + re.escape(key) + r':\s*["\']?(.*?)["\']?\s*$',
                fm_text,
                re.MULTILINE,
            )
            if m:
                meta[key] = m.group(1).strip()

        # Also extract source file name from document_type or optimization_source
        src = re.search(r'^optimization_source:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if src:
            meta["optimization_source"] = src.group(1).strip()

    return meta, body


# ---------------------------------------------------------------------------
# Markdown to HTML conversion
# ---------------------------------------------------------------------------

def convert_inline(text):
    """Convert inline markdown to HTML: bold, italic, links, images, code."""
    # Inline code (before other processing to protect contents)
    code_spans = []

    def save_code(m):
        code_spans.append(m.group(1))
        return f"\x00CODE{len(code_spans) - 1}\x00"

    text = re.sub(r'`([^`]+)`', save_code, text)

    # Images: ![alt](src "title") or ![alt](src)
    def img_repl(m):
        alt = html_escape(m.group(1))
        src = html_escape(m.group(2))
        title = m.group(4)
        if title:
            return f'<img src="{src}" alt="{alt}" title="{html_escape(title)}">'
        return f'<img src="{src}" alt="{alt}">'

    text = re.sub(r'!\[([^\]]*)\]\((\S+?)(\s+"([^"]*)")?\)', img_repl, text)

    # Links: [text](url "title") or [text](url)
    def link_repl(m):
        link_text = m.group(1)
        href = html_escape(m.group(2))
        title = m.group(4)
        if title:
            return f'<a href="{href}" title="{html_escape(title)}">{link_text}</a>'
        return f'<a href="{href}">{link_text}</a>'

    text = re.sub(r'\[([^\]]*)\]\((\S+?)(\s+"([^"]*)")?\)', link_repl, text)

    # Bold+italic: ***text*** or ___text___
    text = re.sub(r'\*{3}(.+?)\*{3}', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'_{3}(.+?)_{3}', r'<strong><em>\1</em></strong>', text)

    # Bold: **text** or __text__
    text = re.sub(r'\*{2}(.+?)\*{2}', r'<strong>\1</strong>', text)
    text = re.sub(r'_{2}(.+?)_{2}', r'<strong>\1</strong>', text)

    # Italic: *text* or _text_ (not inside words for underscore)
    text = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'<em>\1</em>', text)

    # Escape bare & in text (not part of HTML entities)
    text = re.sub(r'&(?!amp;|lt;|gt;|quot;|#\d+;|#x[0-9a-fA-F]+;)', '&amp;', text)

    # Restore code spans
    for i, code in enumerate(code_spans):
        text = text.replace(f"\x00CODE{i}\x00", f"<code>{html_escape(code)}</code>")

    return text


def convert_markdown_to_html(body):
    """Convert markdown body (no frontmatter) to semantic HTML."""
    lines = body.split("\n")
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Empty line
        if not stripped:
            i += 1
            continue

        # Heading
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            level = len(heading_match.group(1))
            text = convert_inline(heading_match.group(2))
            html_parts.append(f"<h{level}>{text}</h{level}>")
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^[-*_]{3,}\s*$', stripped):
            html_parts.append("<hr>")
            i += 1
            continue

        # Table
        if "|" in stripped and i + 1 < len(lines) and re.match(r'^\|[-\s|:]+\|$', lines[i + 1].strip()):
            table_lines = []
            while i < len(lines) and "|" in lines[i].strip():
                table_lines.append(lines[i].strip())
                i += 1
            html_parts.append(convert_table(table_lines))
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r'^>\s?', '', lines[i].strip()))
                i += 1
            bq_text = " ".join(bq_lines)
            html_parts.append(f"<blockquote><p>{convert_inline(bq_text)}</p></blockquote>")
            continue

        # Unordered list
        if re.match(r'^[-*+]\s+', stripped):
            html_parts.append(convert_list(lines, i, ordered=False))
            # Advance past list
            while i < len(lines) and (re.match(r'^(\s*)[-*+]\s+', lines[i]) or (lines[i].strip() == '' and i + 1 < len(lines) and re.match(r'^(\s*)[-*+]\s+', lines[i + 1]))):
                i += 1
            continue

        # Ordered list
        if re.match(r'^\d+\.\s+', stripped):
            html_parts.append(convert_list(lines, i, ordered=True))
            while i < len(lines) and (re.match(r'^(\s*)\d+\.\s+', lines[i]) or (lines[i].strip() == '' and i + 1 < len(lines) and re.match(r'^(\s*)\d+\.\s+', lines[i + 1]))):
                i += 1
            continue

        # Standalone image on its own line (no <p> wrapper)
        img_match = re.match(r'^!\[([^\]]*)\]\((\S+?)(\s+"([^"]*)")?\)$', stripped)
        if img_match:
            alt = html_escape(img_match.group(1))
            src = html_escape(img_match.group(2))
            title = img_match.group(4)
            if title:
                html_parts.append(f'<img src="{src}" alt="{alt}" title="{html_escape(title)}">')
            else:
                html_parts.append(f'<img src="{src}" alt="{alt}">')
            i += 1
            continue

        # Paragraph (collect consecutive non-empty, non-special lines)
        para_lines = []
        while i < len(lines):
            s = lines[i].strip()
            if not s:
                i += 1
                break
            # Check if next line is a special element
            if re.match(r'^#{1,6}\s+', s):
                break
            if re.match(r'^[-*_]{3,}\s*$', s):
                break
            if re.match(r'^[-*+]\s+', s) and not para_lines:
                break
            if re.match(r'^\d+\.\s+', s) and not para_lines:
                break
            if s.startswith(">") and not para_lines:
                break
            if "|" in s and i + 1 < len(lines) and re.match(r'^\|[-\s|:]+\|$', lines[i + 1].strip()) and not para_lines:
                break
            para_lines.append(s)
            i += 1

        if para_lines:
            para_text = " ".join(para_lines)
            html_parts.append(f"<p>{convert_inline(para_text)}</p>")

    return "\n".join(html_parts)


def convert_table(table_lines):
    """Convert markdown table lines to HTML table."""
    if len(table_lines) < 2:
        return ""

    def parse_row(line):
        cells = line.strip().strip("|").split("|")
        return [c.strip() for c in cells]

    header_cells = parse_row(table_lines[0])
    # Skip separator line (table_lines[1])
    body_rows = [parse_row(line) for line in table_lines[2:] if not re.match(r'^\|[-\s|:]+\|$', line.strip())]

    parts = ["<table>", "  <thead>"]
    header_html = "<th>" + "</th><th>".join(convert_inline(c) for c in header_cells) + "</th>"
    parts.append(f"    <tr>{header_html}</tr>")
    parts.extend(["  </thead>", "  <tbody>"])

    for row in body_rows:
        row_html = "<td>" + "</td><td>".join(convert_inline(c) for c in row) + "</td>"
        parts.append(f"    <tr>{row_html}</tr>")

    parts.extend(["  </tbody>", "</table>"])
    return "\n".join(parts)


def convert_list(lines, start_idx, ordered=False):
    """Convert markdown list starting at start_idx to HTML."""
    tag = "ol" if ordered else "ul"
    pattern = r'^\d+\.\s+(.*)$' if ordered else r'^[-*+]\s+(.*)$'

    items = []
    i = start_idx

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            # Check if list continues after blank line
            if i + 1 < len(lines):
                next_stripped = lines[i + 1].strip()
                if ordered and re.match(r'^\d+\.\s+', next_stripped):
                    i += 1
                    continue
                elif not ordered and re.match(r'^[-*+]\s+', next_stripped):
                    i += 1
                    continue
            break

        m = re.match(pattern, stripped)
        if m:
            items.append(m.group(1))
            i += 1
        else:
            # Could be continuation of previous item or end of list
            break

    parts = [f"<{tag}>"]
    for item in items:
        parts.append(f"<li>{convert_inline(item)}</li>")
    parts.append(f"</{tag}>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_html(html_content, source_md):
    """Validate HTML output for common issues."""
    issues = []

    # Check for markdown remnants
    if re.search(r'(?<!\w)#{1,6}\s+\w', html_content):
        issues.append("Possible markdown heading remnants found")
    if re.search(r'(?<!\w)\*{2}\w', html_content):
        issues.append("Possible markdown bold remnants found")
    if re.search(r'(?<!\w)\[.+?\]\(.+?\)', html_content):
        issues.append("Possible markdown link remnants found")

    # Check HTML tags are present
    if "<h" not in html_content and "#" in source_md:
        issues.append("No HTML heading tags but source had headings")
    if "<p>" not in html_content:
        issues.append("No paragraph tags found")
    if "<a " not in html_content and "[" in source_md and "](" in source_md:
        issues.append("No anchor tags but source had links")

    # Check for YAML remnants
    if "---\n" in html_content[:100]:
        issues.append("YAML frontmatter remnants at start of output")

    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]

    if not args or len(args) > 2:
        print("Usage:", file=sys.stderr)
        print("  markdown-to-html.py INPUT.md OUTPUT.html", file=sys.stderr)
        print("  markdown-to-html.py INPUT.md  (writes to INPUT.html)", file=sys.stderr)
        sys.exit(1)

    input_path = args[0]
    if len(args) == 2:
        output_path = args[1]
    else:
        output_path = re.sub(r'\.md$', '.html', input_path)
        if output_path == input_path:
            output_path = input_path + ".html"

    # Read input
    with open(input_path, "r", encoding="utf-8") as f:
        source = f.read()

    # Extract frontmatter
    meta, body = extract_frontmatter(source)

    # Get source filename for metadata comment
    source_filename = os.path.basename(input_path)
    source_url = meta.get("source_url", "n/a")
    meta_title = meta.get("meta_title", "")
    meta_description = meta.get("meta_description", "")
    export_date = date.today().isoformat()

    # Convert
    html_content = convert_markdown_to_html(body)

    # Build output
    output_parts = []

    # Metadata comment
    output_parts.append(f"""<!--
  Source: {source_filename}
  Exported: {export_date}
  Original URL: {source_url}
  Meta Title: {meta_title or 'n/a'}
  Meta Description: {meta_description or 'n/a'}
-->""")

    # Title tag
    if meta_title:
        output_parts.append(f"<title>{html_escape(meta_title)}</title>")

    # Meta description tag (don't escape apostrophes inside double-quoted attributes)
    if meta_description:
        safe_desc = meta_description.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        output_parts.append(f'<meta name="description" content="{safe_desc}">')

    # Blank line before content
    output_parts.append("")
    output_parts.append(html_content)

    final_output = "\n".join(output_parts) + "\n"

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    # Validate
    issues = validate_html(html_content, source)

    # Count elements for summary
    h_count = len(re.findall(r'<h[1-6]', html_content))
    p_count = len(re.findall(r'<p>', html_content))
    a_count = len(re.findall(r'<a ', html_content))
    img_count = len(re.findall(r'<img ', html_content))
    list_count = len(re.findall(r'<[ou]l>', html_content))
    table_count = len(re.findall(r'<table>', html_content))

    result = {
        "status": "ok" if not issues else "warning",
        "input": input_path,
        "output": output_path,
        "output_size": len(final_output),
        "elements": {
            "headings": h_count,
            "paragraphs": p_count,
            "links": a_count,
            "images": img_count,
            "lists": list_count,
            "tables": table_count,
        },
        "meta_title": meta_title or None,
        "meta_description": meta_description[:80] + "..." if len(meta_description) > 80 else meta_description or None,
    }
    if issues:
        result["issues"] = issues

    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
