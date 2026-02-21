#!/usr/bin/env python3
"""
html-to-markdown.py -- Convert raw HTML page to markdown following formatting-rules.md.

Finds main content area, strips chrome (header/footer/nav/aside), converts all
elements to markdown, resolves relative URLs, extracts metadata. Outputs markdown
file + JSON summary to stdout.

Usage:
  html-to-markdown.py INPUT.html OUTPUT.md [--base-url URL]
  html-to-markdown.py INPUT.html            # writes to INPUT.md (same dir)

Output: JSON summary to stdout with word count, heading/link/image counts, warnings.
"""

import sys
import re
import json
import os
from html.parser import HTMLParser
from html import unescape
from urllib.parse import urljoin


# ---------------------------------------------------------------------------
# HTML Parser
# ---------------------------------------------------------------------------

class HTMLNode:
    """Simple DOM-like node."""
    def __init__(self, tag="", attrs=None):
        self.tag = tag
        self.attrs = dict(attrs) if attrs else {}
        self.children = []
        self.text = ""
        self.tail = ""  # text after this element's closing tag

    def get_attr(self, name, default=""):
        return self.attrs.get(name, default)

    def find_all(self, tag):
        """Find all descendants with given tag."""
        results = []
        for child in self.children:
            if child.tag == tag:
                results.append(child)
            results.extend(child.find_all(tag))
        return results

    def find(self, tag):
        """Find first descendant with given tag."""
        for child in self.children:
            if child.tag == tag:
                return child
            result = child.find(tag)
            if result:
                return result
        return None

    def get_text(self):
        """Get all text content."""
        parts = [self.text or ""]
        for child in self.children:
            parts.append(child.get_text())
            parts.append(child.tail or "")
        return "".join(parts)


class SimpleHTMLParser(HTMLParser):
    """Parse HTML into a tree of HTMLNode objects."""

    # Self-closing tags
    VOID_ELEMENTS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    # Tags to skip entirely (including content)
    SKIP_TAGS = {"script", "style", "noscript", "svg", "template"}

    def __init__(self):
        super().__init__()
        self.root = HTMLNode("root")
        self.stack = [self.root]
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.skip_depth > 0:
            if tag not in self.VOID_ELEMENTS:
                self.skip_depth += 1
            return
        if tag in self.SKIP_TAGS:
            self.skip_depth = 1
            return

        node = HTMLNode(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID_ELEMENTS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.skip_depth > 0:
            self.skip_depth -= 1
            return
        if tag in self.VOID_ELEMENTS:
            return
        # Pop stack back to matching tag
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                return

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        if self.stack[-1].children:
            # Append as tail of last child
            self.stack[-1].children[-1].tail += data
        else:
            self.stack[-1].text += data

    def handle_comment(self, data):
        pass  # Skip comments

    def handle_entityref(self, name):
        self.handle_data(unescape(f"&{name};"))

    def handle_charref(self, name):
        self.handle_data(unescape(f"&#{name};"))


def parse_html(html_text):
    """Parse HTML string into node tree."""
    parser = SimpleHTMLParser()
    parser.feed(html_text)
    return parser.root


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------

def extract_metadata(root):
    """Extract title, meta description, canonical URL, og:url from HTML head."""
    meta = {}

    # Find <head>
    head = root.find("head")
    if not head:
        return meta

    # <title>
    title_el = head.find("title")
    if title_el:
        meta["meta_title"] = title_el.get_text().strip()

    # <meta> tags
    for node in head.find_all("meta"):
        name = node.get_attr("name", "").lower()
        prop = node.get_attr("property", "").lower()
        content = node.get_attr("content", "")

        if name == "description":
            meta["meta_description"] = content
        elif prop == "og:url":
            meta["og_url"] = content

    # <link rel="canonical">
    for node in head.find_all("link"):
        if node.get_attr("rel", "").lower() == "canonical":
            meta["canonical"] = node.get_attr("href", "")

    return meta


# ---------------------------------------------------------------------------
# Content area finding
# ---------------------------------------------------------------------------

# Chrome elements to remove
CHROME_TAGS = {"header", "footer", "nav", "aside"}
CHROME_CLASSES_EXACT = {
    "sidebar", "nav", "header", "footer", "cookie-banner", "breadcrumb",
    "cookie", "popup", "modal", "share", "related", "comments",
    "advertisement", "newsletter", "social", "widget", "menu",
}
# These require exact class/id match (not substring) to avoid false positives
CHROME_CLASSES_WORD = {
    "ad",  # "ad" as substring matches "heading", "loading", etc.
}

def has_chrome_class(node):
    """Check if node has a class or id suggesting it's chrome."""
    classes = node.get_attr("class", "").lower().split()
    node_id = node.get_attr("id", "").lower()

    for cls in classes:
        # Exact match for short ambiguous keywords
        if cls in CHROME_CLASSES_WORD:
            return True
        # Substring match for longer keywords
        for chrome in CHROME_CLASSES_EXACT:
            if chrome in cls:
                return True

    # Check ID with same logic
    if node_id in CHROME_CLASSES_WORD:
        return True
    for chrome in CHROME_CLASSES_EXACT:
        if chrome in node_id:
            return True
    return False


def find_content_area(root):
    """Find the main content area using priority selectors."""
    body = root.find("body")
    if not body:
        body = root

    # Priority 1: <main>
    main = body.find("main")
    if main:
        return main

    # Priority 2: <article>
    article = body.find("article")
    if article:
        return article

    # Priority 3: [role="main"]
    for node in _walk(body):
        if node.get_attr("role", "").lower() == "main":
            return node

    # Priority 4: Common content class/id selectors
    for node in _walk(body):
        classes = node.get_attr("class", "").lower().split()
        node_id = node.get_attr("id", "").lower()
        for target in ("content", "page-content", "main-content", "entry-content"):
            if target in classes or target == node_id:
                return node

    # Fallback: body itself
    return body


def _walk(node):
    """Walk all descendants."""
    for child in node.children:
        yield child
        yield from _walk(child)


def strip_chrome(node):
    """Remove chrome elements from content area (in-place)."""
    node.children = [
        child for child in node.children
        if child.tag not in CHROME_TAGS and not has_chrome_class(child)
    ]
    for child in node.children:
        strip_chrome(child)


# ---------------------------------------------------------------------------
# HTML to Markdown conversion
# ---------------------------------------------------------------------------

def node_to_markdown(node, base_url="", depth=0):
    """Convert an HTML node tree to markdown string."""
    parts = []
    _convert_children(node, parts, base_url, depth)
    return _clean_markdown("\n".join(parts))


def _convert_children(node, parts, base_url, depth):
    """Process a node's text and children."""
    # Handle direct text
    if node.text and node.text.strip():
        text = _normalize_ws(node.text)
        if text.strip():
            parts.append(text.strip())

    for child in node.children:
        md = _convert_node(child, base_url, depth)
        if md is not None:
            parts.append(md)
        # Handle tail text
        if child.tail and child.tail.strip():
            text = _normalize_ws(child.tail)
            if text.strip():
                parts.append(text.strip())


def _convert_node(node, base_url, depth):
    """Convert a single node to markdown."""
    tag = node.tag

    # Headings
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        text = _inline_text(node, base_url)
        if text.strip():
            return f"\n\n{'#' * level} {text.strip()}"
        return None

    # Paragraphs
    if tag == "p":
        text = _inline_text(node, base_url)
        if text.strip():
            return f"\n\n{text.strip()}"
        return None

    # Bold
    if tag in ("strong", "b"):
        text = _inline_text(node, base_url)
        if text.strip():
            return f"**{text.strip()}**"
        return None

    # Italic
    if tag in ("em", "i"):
        text = _inline_text(node, base_url)
        if text.strip():
            return f"*{text.strip()}*"
        return None

    # Code
    if tag == "code":
        text = node.get_text().strip()
        if text:
            return f"`{text}`"
        return None

    # Links
    if tag == "a":
        href = node.get_attr("href", "")
        if base_url and href and not href.startswith(("http://", "https://", "#", "mailto:")):
            href = urljoin(base_url, href)
        text = _inline_text(node, base_url)
        title = node.get_attr("title", "")
        if text.strip():
            if title:
                return f'[{text.strip()}]({href} "{title}")'
            return f"[{text.strip()}]({href})"
        return None

    # Images
    if tag == "img":
        src = node.get_attr("src", "")
        if base_url and src and not src.startswith(("http://", "https://", "data:")):
            src = urljoin(base_url, src)
        alt = node.get_attr("alt", "")
        title = node.get_attr("title", "")
        if title:
            return f'\n\n![{alt}]({src} "{title}")'
        return f"\n\n![{alt}]({src})"

    # Lists
    if tag in ("ul", "ol"):
        items = []
        for i, child in enumerate(node.children):
            if child.tag == "li":
                text = _inline_text(child, base_url)
                if text.strip():
                    if tag == "ol":
                        items.append(f"{i + 1}. {text.strip()}")
                    else:
                        items.append(f"- {text.strip()}")
        if items:
            return "\n\n" + "\n".join(items)
        return None

    # Blockquotes
    if tag == "blockquote":
        text = _inline_text(node, base_url)
        if text.strip():
            lines = text.strip().split("\n")
            return "\n\n" + "\n".join(f"> {line}" for line in lines)
        return None

    # Tables
    if tag == "table":
        return "\n\n" + _convert_table(node, base_url)

    # Horizontal rule
    if tag == "hr":
        return "\n\n---"

    # Line break
    if tag == "br":
        return "\n"

    # Details/summary (collapsible content -- expand fully)
    if tag == "details":
        parts = []
        for child in node.children:
            if child.tag == "summary":
                text = _inline_text(child, base_url)
                if text.strip():
                    parts.append(f"\n\n### {text.strip()}")
            else:
                md = _convert_node(child, base_url, depth)
                if md:
                    parts.append(md)
        return "".join(parts) if parts else None

    # Figure
    if tag == "figure":
        parts = []
        _convert_children(node, parts, base_url, depth + 1)
        return "\n".join(parts) if parts else None

    # Figcaption
    if tag == "figcaption":
        text = _inline_text(node, base_url)
        if text.strip():
            return f"\n\n*{text.strip()}*"
        return None

    # Div, section, span, etc. -- recurse into children
    if tag in ("div", "section", "span", "main", "article", "aside",
               "figure", "figcaption", "dl", "dt", "dd", "small",
               "mark", "abbr", "time", "address", "pre"):
        parts = []
        _convert_children(node, parts, base_url, depth + 1)
        if parts:
            return "\n".join(parts)
        return None

    # Default: recurse
    parts = []
    _convert_children(node, parts, base_url, depth + 1)
    if parts:
        return "\n".join(parts)
    return None


def _inline_text(node, base_url):
    """Get inline content of a node, converting inline elements."""
    parts = []
    if node.text:
        parts.append(_normalize_ws(node.text))

    for child in node.children:
        tag = child.tag

        if tag in ("strong", "b"):
            text = _inline_text(child, base_url)
            if text.strip():
                parts.append(f"**{text.strip()}**")

        elif tag in ("em", "i"):
            text = _inline_text(child, base_url)
            if text.strip():
                parts.append(f"*{text.strip()}*")

        elif tag == "code":
            text = child.get_text().strip()
            if text:
                parts.append(f"`{text}`")

        elif tag == "a":
            href = child.get_attr("href", "")
            if base_url and href and not href.startswith(("http://", "https://", "#", "mailto:")):
                href = urljoin(base_url, href)
            text = _inline_text(child, base_url)
            title = child.get_attr("title", "")
            if text.strip():
                if title:
                    parts.append(f'[{text.strip()}]({href} "{title}")')
                else:
                    parts.append(f"[{text.strip()}]({href})")

        elif tag == "img":
            src = child.get_attr("src", "")
            if base_url and src and not src.startswith(("http://", "https://", "data:")):
                src = urljoin(base_url, src)
            alt = child.get_attr("alt", "")
            parts.append(f"![{alt}]({src})")

        elif tag == "br":
            parts.append("\n")

        elif tag in ("span", "mark", "abbr", "time", "small", "sub", "sup"):
            parts.append(_inline_text(child, base_url))

        else:
            # Unknown inline element -- just get text
            parts.append(_inline_text(child, base_url))

        if child.tail:
            parts.append(_normalize_ws(child.tail))

    return "".join(parts)


def _convert_table(node, base_url):
    """Convert table node to markdown table."""
    rows = []
    thead = node.find("thead")
    tbody = node.find("tbody")

    if thead:
        for tr in thead.find_all("tr"):
            cells = []
            for child in tr.children:
                if child.tag in ("th", "td"):
                    cells.append(_inline_text(child, base_url).strip())
            if cells:
                rows.append(cells)

    # Add separator after header
    if rows:
        rows.insert(1, ["---"] * len(rows[0]))

    if tbody:
        for tr in tbody.find_all("tr"):
            cells = []
            for child in tr.children:
                if child.tag in ("th", "td"):
                    cells.append(_inline_text(child, base_url).strip())
            if cells:
                rows.append(cells)
    else:
        # No thead/tbody -- all rows from direct tr children
        for tr in node.find_all("tr"):
            cells = []
            for child in tr.children:
                if child.tag in ("th", "td"):
                    cells.append(_inline_text(child, base_url).strip())
            if cells:
                rows.append(cells)
        # Insert separator after first row if none exists
        if len(rows) > 1 and rows[1] != ["---"] * len(rows[0]):
            rows.insert(1, ["---"] * len(rows[0]))

    lines = []
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def _normalize_ws(text):
    """Normalize whitespace in text."""
    return re.sub(r'\s+', ' ', text)


def _clean_markdown(md):
    """Clean up generated markdown."""
    # Remove excess blank lines (max 2 consecutive newlines)
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Remove leading/trailing whitespace
    md = md.strip()
    # Ensure single newline at end
    return md + "\n"


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_markdown(md, base_url=""):
    """Validate markdown output for common issues."""
    warnings = []

    # Check for remaining HTML tags
    remaining_tags = re.findall(r'<(?!/?(?:br|hr)\s*/?>)[a-zA-Z][^>]*>', md)
    if remaining_tags:
        unique_tags = set(re.match(r'</?(\w+)', t).group(1) for t in remaining_tags if re.match(r'</?(\w+)', t))
        warnings.append(f"Remaining HTML tags: {', '.join(sorted(unique_tags))}")

    # Check heading hierarchy
    headings = re.findall(r'^(#{1,6})\s', md, re.MULTILINE)
    if headings:
        levels = [len(h) for h in headings]
        if levels[0] != 1:
            warnings.append(f"First heading is H{levels[0]}, expected H1")
        for i in range(1, len(levels)):
            if levels[i] > levels[i-1] + 1:
                warnings.append(f"Heading jump from H{levels[i-1]} to H{levels[i]}")
                break

    return warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]

    if not args or len(args) > 4:
        print("Usage:", file=sys.stderr)
        print("  html-to-markdown.py INPUT.html OUTPUT.md [--base-url URL]", file=sys.stderr)
        print("  html-to-markdown.py INPUT.html  (writes to INPUT.md)", file=sys.stderr)
        sys.exit(1)

    input_path = args[0]
    output_path = None
    base_url = ""

    # Parse remaining args
    i = 1
    while i < len(args):
        if args[i] == "--base-url" and i + 1 < len(args):
            base_url = args[i + 1]
            i += 2
        elif output_path is None:
            output_path = args[i]
            i += 1
        else:
            i += 1

    if output_path is None:
        output_path = re.sub(r'\.html?$', '.md', input_path)
        if output_path == input_path:
            output_path = input_path + ".md"

    # Read input
    with open(input_path, "r", encoding="utf-8", errors="replace") as f:
        html_text = f.read()

    # Parse HTML
    root = parse_html(html_text)

    # Extract metadata
    meta = extract_metadata(root)

    # Find content area
    content = find_content_area(root)

    # Strip chrome from content area
    strip_chrome(content)

    # Convert to markdown
    markdown = node_to_markdown(content, base_url)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    # Validate
    warnings = validate_markdown(markdown, base_url)

    # Count elements
    headings = re.findall(r'^#{1,6}\s', markdown, re.MULTILINE)
    links = re.findall(r'\[([^\]]+)\]\(', markdown)
    images = re.findall(r'!\[([^\]]*)\]\(', markdown)
    word_count = len(markdown.split())
    bold_count = len(re.findall(r'\*\*[^*]+\*\*', markdown))
    italic_count = len(re.findall(r'(?<!\*)\*(?!\*)[^*]+\*(?!\*)', markdown))

    result = {
        "status": "ok" if not warnings else "warning",
        "input": input_path,
        "output": output_path,
        "output_size": len(markdown),
        "word_count": word_count,
        "elements": {
            "headings": len(headings),
            "links": len(links),
            "images": len(images),
            "bold": bold_count,
            "italic": italic_count,
        },
        "meta": meta if meta else None,
    }
    if warnings:
        result["warnings"] = warnings

    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
