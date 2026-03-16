# Brief File Parsing Rules

PageOptimizer.pro exports 4 content brief files. Each file targets a different section of the page.

---

## File Mapping

| File | Target Section | Scope |
|---|---|---|
| `ContentBrief_title.txt` | `<title>` tag | The meta title / search engine title |
| `ContentBrief_pageTitle.txt` | H1 | The visible page title (single H1) |
| `ContentBrief_subHeadings.txt` | H2-H6 | All subheadings collectively |
| `ContentBrief_BodyContent.txt` | Body text | Paragraphs, lists, tables -- everything except headings |

---

## Line Format

Each keyword line follows one of two formats:

**Range target:**
```
keyword phrase ( current_count / target_min - target_max )
```

**Single target:**
```
keyword phrase ( current_count / target_single )
```

### Examples

```
mobile app development company ( 0 / 1 )
development ( 0 / 1 - 2 )
mobile ( 1 / 0 - 2 )
mobile app development ( 0 / 0 - 1 )
app development company ( 0 / 0 - 1 )
mobile app development agency ( 0 / 0 - 1 )
```

### Parsing Rules

1. **Extract keyword**: Everything before the opening `(`, trimmed.
2. **Extract current count**: The number before the `/`.
3. **Extract target**:
   - If format is `X / Y - Z`: targetMin = Y, targetMax = Z.
   - If format is `X / Y` (no dash): targetMin = Y, targetMax = Y.
4. **Skip non-keyword lines**: Ignore empty lines, header text, tip paragraphs, and any line that does not match the `keyword ( N / N )` or `keyword ( N / N - N )` pattern.

### Edge Cases

- Keywords with numbers: `24/7 support ( 0 / 1 )` -- the keyword is `24/7 support`. The `/` inside the keyword is distinguishable because it is not inside parentheses.
- Keywords with hyphens: `mobile-friendly ( 0 / 1 )` -- preserve the hyphen as part of the keyword.
- Target includes zero: `some keyword ( 0 / 0 - 1 )` means the keyword should be used 1 time. The 0 in the range means PageOptimizer won't penalize for skipping it, but including it improves the score. Always aim for targetMax (1 in this case). Do NOT treat this as optional.
- Current exceeds target max: `overused term ( 5 / 1 - 2 )` means the keyword is OVER-represented. Flag it but do not remove content -- just avoid adding more.

---

## Tips Text

Each brief file may include tip text from PageOptimizer.pro at the top. These provide guidance specific to the section:

**Title tips** (summary): Use important terms in suggested range. Select the ones you like. Title and H1 should be as identical as possible.

**Page Title tips** (summary): Same as title tips. Only one H1 on the page.

**Subheadings tips** (summary): Distribute keywords across all subheadings. The goal is the section as a whole hitting the target range, not individual subheadings.

**Body Content tips** (summary): Use terms to optimize main content. Write content first, then edit for terms. Answer reader questions about the target keyword.

These tips are embedded in the skill's Phase 2 planning logic. Parse and discard them from the keyword list -- they are not keyword lines.

---

## Data Structure

After parsing, each brief should be represented as:

```
Section: title | pageTitle | subHeadings | bodyContent
Keywords: [
  { keyword: "mobile app development company", current: 0, targetMin: 1, targetMax: 1 },
  { keyword: "development", current: 0, targetMin: 1, targetMax: 2 },
  { keyword: "mobile", current: 1, targetMin: 0, targetMax: 2 },
  ...
]
```
