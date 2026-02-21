#!/usr/bin/env python3
"""
brief-scorer.py -- Parse PageOptimizer.pro brief files and score keyword usage in content.

Usage:
  brief-scorer.py --parse-only TITLE.txt PAGETITLE.txt SUBHEADINGS.txt BODYCONTENT.txt
  brief-scorer.py --score CONTENT.md --briefs TITLE.txt PAGETITLE.txt SUBHEADINGS.txt BODYCONTENT.txt
  brief-scorer.py --score CONTENT.md --briefs-json PARSED.json

Output: JSON to stdout.
"""

import sys
import re
import json
import os


# ---------------------------------------------------------------------------
# Brief parsing
# ---------------------------------------------------------------------------

def parse_brief_file(filepath):
    """Parse a single PageOptimizer.pro brief file into keyword entries.

    Line format (range):  keyword phrase ( current / min - max )
    Line format (single): keyword phrase ( current / target )

    Returns list of dicts: {keyword, current, targetMin, targetMax}
    """
    keywords = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Match: everything before the last parenthesized group with numbers
            # Pattern handles keywords that may contain numbers, slashes, hyphens
            # We anchor on the LAST occurrence of ( digits / digits ) or ( digits / digits - digits )
            m = re.match(
                r'^(.+?)\s*\(\s*(\d+)\s*/\s*(\d+)(?:\s*-\s*(\d+))?\s*\)\s*$',
                line
            )
            if not m:
                # Skip tip text, headers, empty lines
                continue

            keyword = m.group(1).strip()
            current = int(m.group(2))
            target_min = int(m.group(3))
            target_max = int(m.group(4)) if m.group(4) is not None else target_min

            keywords.append({
                "keyword": keyword,
                "current": current,
                "targetMin": target_min,
                "targetMax": target_max,
            })
    return keywords


def parse_all_briefs(title_path, page_title_path, subheadings_path, body_path):
    """Parse all 4 brief files into a structured dict."""
    return {
        "title": parse_brief_file(title_path),
        "pageTitle": parse_brief_file(page_title_path),
        "subHeadings": parse_brief_file(subheadings_path),
        "bodyContent": parse_brief_file(body_path),
    }


# ---------------------------------------------------------------------------
# Content zone extraction
# ---------------------------------------------------------------------------

def strip_yaml_frontmatter(text):
    """Remove YAML frontmatter and return (frontmatter_dict, body).

    Extracts meta_title and meta_description from frontmatter.
    """
    meta = {}
    body = text

    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = text[fm_match.end():]

        # Extract meta_title
        mt = re.search(r'^meta_title:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if mt:
            meta["meta_title"] = mt.group(1).strip()

        # Extract meta_description
        md = re.search(r'^meta_description:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if md:
            meta["meta_description"] = md.group(1).strip()

    return meta, body


def extract_zones(content_text):
    """Split markdown content into 4 zones for keyword counting.

    Returns dict with keys: title, pageTitle, subHeadings, bodyContent
    Each value is the text of that zone (plain text, markdown syntax stripped).
    """
    meta, body = strip_yaml_frontmatter(content_text)

    # Zone 1: Title (meta_title from frontmatter)
    title_text = meta.get("meta_title", "")

    # Zone 2: Page Title (H1 -- first line starting with single #)
    page_title_text = ""
    h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if h1_match:
        page_title_text = h1_match.group(1).strip()

    # Zone 3: Subheadings (all H2-H6 text combined)
    subheadings_parts = []
    for m in re.finditer(r'^#{2,6}\s+(.+)$', body, re.MULTILINE):
        subheadings_parts.append(m.group(1).strip())
    subheadings_text = " ".join(subheadings_parts)

    # Zone 4: Body text (everything that is NOT a heading, NOT frontmatter, NOT markdown syntax)
    body_lines = []
    for line in body.split("\n"):
        stripped = line.strip()
        # Skip headings (any level)
        if re.match(r'^#{1,6}\s+', stripped):
            continue
        # Skip empty lines
        if not stripped:
            continue
        # Skip table separator lines
        if re.match(r'^\|[-\s|:]+\|$', stripped):
            continue
        body_lines.append(stripped)

    body_text = "\n".join(body_lines)

    return {
        "title": title_text,
        "pageTitle": page_title_text,
        "subHeadings": subheadings_text,
        "bodyContent": body_text,
    }


def clean_zone_text(text):
    """Strip markdown syntax from zone text for keyword counting.

    Removes: markdown link syntax (keeps text), image syntax (keeps alt),
    bold/italic markers, YAML-like lines, URL targets, inline code backticks.
    """
    # Remove image references: ![alt](url) -> alt
    text = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # Remove links: [text](url) -> text  (exclude URL from counting)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # Remove bare URLs (http/https)
    text = re.sub(r'https?://\S+', '', text)
    # Remove bold/italic markers
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'_{1,3}', '', text)
    # Remove inline code backticks
    text = re.sub(r'`[^`]*`', '', text)
    # Remove table pipes
    text = re.sub(r'\|', ' ', text)
    # Remove markdown list markers
    text = re.sub(r'^[\s]*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[\s]*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Remove blockquote markers
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove horizontal rules (standalone --- or ***)
    text = re.sub(r'^[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)

    return text


# ---------------------------------------------------------------------------
# Keyword counting
# ---------------------------------------------------------------------------

def count_keyword(keyword, text):
    """Count occurrences of keyword in text.

    Rules:
    - Case-insensitive
    - Whole word boundaries (hyphenated forms count)
    - Contiguous phrase matching only
    """
    # Escape regex special chars in keyword
    escaped = re.escape(keyword)

    # Word boundary: allow hyphen as word-internal character
    # Use \b but also allow hyphen boundaries
    # Pattern: word boundary, then the keyword, then word boundary
    # For multi-word keywords, spaces in the keyword match literal spaces
    pattern = r'(?<![a-zA-Z0-9-])' + escaped + r'(?![a-zA-Z0-9-])'

    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)


def compute_status(count, target_min, target_max):
    """Determine keyword status based on count vs targets."""
    if target_max == 0 and target_min == 0:
        if count == 0:
            return "HIT"  # 0/0 target, 0 count = fine
        else:
            return "OVER"
    if count == 0:
        return "MISS"
    if count > target_max:
        return "OVER"
    if count == target_max:
        return "MAXED"
    if count >= target_min:
        return "HIT"
    # count > 0 but < target_min
    return "PARTIAL"


def score_section(keywords, zone_text):
    """Score all keywords in a section against the zone text.

    Returns dict with keyword results and section summary.
    """
    cleaned = clean_zone_text(zone_text)
    results = []
    counts = {"total": len(keywords), "maxed": 0, "hit": 0, "partial": 0, "miss": 0, "over": 0}

    for kw in keywords:
        count = count_keyword(kw["keyword"], cleaned)
        status = compute_status(count, kw["targetMin"], kw["targetMax"])
        counts[status.lower()] += 1
        results.append({
            "keyword": kw["keyword"],
            "count": count,
            "targetMin": kw["targetMin"],
            "targetMax": kw["targetMax"],
            "status": status,
        })

    return {
        "total": counts["total"],
        "maxed": counts["maxed"],
        "hit": counts["hit"],
        "partial": counts["partial"],
        "miss": counts["miss"],
        "over": counts["over"],
        "keywords": results,
    }


def count_words(text):
    """Count words in markdown body text (excluding frontmatter)."""
    _, body = strip_yaml_frontmatter(text)
    # Remove markdown syntax for clean word count
    cleaned = clean_zone_text(body)
    words = cleaned.split()
    return len(words)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage:", file=sys.stderr)
        print("  brief-scorer.py --parse-only T.txt PT.txt SH.txt BC.txt", file=sys.stderr)
        print("  brief-scorer.py --score CONTENT.md --briefs T.txt PT.txt SH.txt BC.txt", file=sys.stderr)
        print("  brief-scorer.py --score CONTENT.md --briefs-json PARSED.json", file=sys.stderr)
        sys.exit(1)

    if args[0] == "--parse-only":
        if len(args) != 5:
            print("Error: --parse-only requires exactly 4 brief file paths", file=sys.stderr)
            sys.exit(1)
        briefs = parse_all_briefs(args[1], args[2], args[3], args[4])
        json.dump(briefs, sys.stdout, indent=2)
        print()
        sys.exit(0)

    if args[0] == "--score":
        if len(args) < 2:
            print("Error: --score requires a content file path", file=sys.stderr)
            sys.exit(1)

        content_path = args[1]

        # Load content
        with open(content_path, "r", encoding="utf-8") as f:
            content_text = f.read()

        # Load briefs
        briefs = None
        if len(args) >= 4 and args[2] == "--briefs":
            if len(args) != 7:
                print("Error: --briefs requires exactly 4 brief file paths", file=sys.stderr)
                sys.exit(1)
            briefs = parse_all_briefs(args[3], args[4], args[5], args[6])
        elif len(args) >= 4 and args[2] == "--briefs-json":
            with open(args[3], "r", encoding="utf-8") as f:
                briefs = json.load(f)
        else:
            print("Error: --score requires --briefs or --briefs-json", file=sys.stderr)
            sys.exit(1)

        # Extract zones
        zones = extract_zones(content_text)

        # Score each section
        result = {}
        total_kw = 0
        total_maxed = 0
        total_hit = 0
        total_partial = 0
        total_miss = 0
        total_over = 0

        for section in ["title", "pageTitle", "subHeadings", "bodyContent"]:
            scored = score_section(briefs[section], zones[section])
            result[section] = scored
            total_kw += scored["total"]
            total_maxed += scored["maxed"]
            total_hit += scored["hit"]
            total_partial += scored["partial"]
            total_miss += scored["miss"]
            total_over += scored["over"]

        maxed_or_hit = total_maxed + total_hit
        pct = round((maxed_or_hit / total_kw * 100), 1) if total_kw > 0 else 0.0

        result["summary"] = {
            "total_keywords": total_kw,
            "maxed": total_maxed,
            "hit": total_hit,
            "partial": total_partial,
            "miss": total_miss,
            "over": total_over,
            "maxed_or_hit_pct": pct,
        }
        result["word_count"] = count_words(content_text)

        json.dump(result, sys.stdout, indent=2)
        print()
        sys.exit(0)

    print(f"Error: Unknown flag '{args[0]}'", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
