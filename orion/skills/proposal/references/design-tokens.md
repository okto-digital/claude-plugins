# oktodigital Design Tokens

CSS custom properties and brand elements for the HTML proposal template. Source: oktodigital brand guide.

## Core Palette

```css
:root {
  /* Brand */
  --c-primary:        #FF003D;   /* Brand red -- accent only, never large fills */
  --c-dark:           #1a2332;   /* Primary headings, dark sections, title page bg */
  --c-text:           #606F7E;   /* Body text */
  --c-text-light:     #9AA7B2;   /* Secondary text, footer text, meta lines */
  --c-bg:             #FFFFFF;   /* Primary background */
  --c-bg-light:       #F2F5F8;   /* Alternating section background, table headers */
  --c-bg-alt:         #f0f0f0;   /* Canvas / page wrapper */
  --c-border:         #DFE5EB;   /* Borders, dividers, table lines */
  --c-primary-tint:   rgba(255, 0, 61, 0.10);  /* Accent highlight bg */

  /* Functional accent colors (mapped to service phases) */
  --c-green:          #4DEDB1;   /* Plan phase */
  --c-green-bg:       rgba(77, 237, 177, 0.15);
  --c-yellow:         #EDDF4C;   /* Build phase */
  --c-yellow-bg:      rgba(237, 223, 76, 0.15);
  --c-pink:           #FF8EA9;   /* Care phase */
  --c-pink-bg:        rgba(255, 142, 169, 0.15);
  --c-purple:         #B199F9;   /* Grow phase */
  --c-purple-bg:      rgba(177, 153, 249, 0.15);

  /* Legacy alias (templates may reference --c-red) */
  --c-red:            var(--c-pink);
  --c-red-bg:         var(--c-pink-bg);
}
```

### Functional color mapping

| Color | Variable | Phase | Proposal usage |
|---|---|---|---|
| Green | `--c-green` | Plan | Traffic numbers, frontend/analytics modules, must_have badges |
| Yellow | `--c-yellow` | Build | Design/content/SEO modules, should_have badges, operator notices |
| Pink | `--c-pink` | Care | Backend/ecommerce/integration modules |
| Purple | `--c-purple` | Grow | Strategy/migration modules, nice_to_have badges |

## Typography

```css
:root {
  --font:             "Safiro", "Inter", sans-serif;
  --fs-base:          18px;
  --fs-sm:            14px;
  --fs-xs:            12px;
  --fs-lg:            22px;
  --fs-xl:            28px;
  --fs-h1:            48px;
  --fs-h2:            32px;
  --fs-h3:            24px;
  --fs-display:       64px;    /* Bracket numbers (stacked) */
  --fs-stat:          56px;    /* Stat block numbers */
  --lh-base:          1.5;
  --lh-heading:       1.2;
  --fw-normal:        400;
  --fw-semibold:      600;
  --fw-extrabold:     800;
}
```

### Fonts

Primary: Safiro (loaded from oktodigital.com woff2)
Fallback: Inter (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
```

Safiro is loaded via `@font-face` in the template CSS. If unavailable, Inter renders seamlessly.

## Layout

```css
:root {
  --max-width:        900px;
  --section-py:       80px;
  --container-px:     48px;
  --shadow:           0 5px 15px rgba(0, 0, 0, 0.15);

  /* Spacing scale */
  --sp-xs:            4px;
  --sp-sm:            8px;
  --sp-md:            16px;
  --sp-lg:            24px;
  --sp-xl:            40px;
  --sp-2xl:           64px;
}
```

**Sharp corners (0px radius)** -- The brand uses 0px border-radius on all elements. No radius variables are defined. Do not add rounded corners to any element.

## Brand Elements

### Bracket numbers `{ 01 }`

Typographic signature used throughout the brand. Three variants:

| Variant | Class | Size | Usage |
|---|---|---|---|
| Inline | `.bracket-num--inline` | 14px | Section labels next to headings |
| Stacked | `.bracket-num--stacked` | 64px | Large display numbers |
| Watermark | `.bracket-num--watermark` | 200px | Faded background decoration |

Color variants: `--green`, `--yellow`, `--pink`, `--purple`. The `::before` and `::after` pseudo-elements add the `{ }` brackets automatically.

### Corner accents

Colored L-shaped bracket on content blocks, always top-left. Applied via `.corner-accent` class on a positioned parent. The `::before` pseudo-element draws the L-shape (24x24px, 3px border).

Color variants: `--green`, `--yellow`, `--pink`, `--purple`, `--primary`.

### Grid motif

Subtle dot-grid texture for dark sections. Applied via `.grid-motif` class. Uses `radial-gradient` with 6% white opacity dots on a 24px grid.

### Dividers

| Type | Class | Description |
|---|---|---|
| Standard | `.divider` | 1px border-color line |
| Accent | `.divider--accent` | 3px red, 60px wide |
| Four-color strip | `.divider--four-color` | 4px gradient: green-yellow-pink-purple |
| Numbered | `.divider--numbered` | `{ 03 }` centered between lines |

### Stat blocks

Large colored numbers with small labels. Use `.stat-grid` for layout and `.stat-block` for each item. Number colors: `.stat-number--green/yellow/pink/purple`.

### Icons

All icons are inline SVG with these properties:
- Geometric, line-based (not filled)
- 2px stroke weight
- Square linecap, miter join (sharp corners)
- Default size: 32x32px (`.icon--lg` for 48x48px)

## Usage in Proposal

### Module category colors

| Category | Border color | Background |
|---|---|---|
| strategy | `--c-purple` | `--c-purple-bg` |
| design | `--c-yellow` | `--c-yellow-bg` |
| content, seo | `--c-yellow` | `--c-yellow-bg` |
| frontend | `--c-green` | `--c-green-bg` |
| backend, ecommerce, integration | `--c-pink` | `--c-pink-bg` |
| migration, multilingual | `--c-purple` | `--c-purple-bg` |
| analytics, post-launch | `--c-green` | `--c-green-bg` |

### Priority badges

| Priority | Color | Background |
|---|---|---|
| must_have | `--c-green` | `--c-green-bg` |
| should_have | `--c-yellow` | `--c-yellow-bg` |
| nice_to_have | `--c-purple` | `--c-purple-bg` |

### Section backgrounds

Alternate between white and light. Use dark for title page and high-impact sections.

| Background | Variable | Usage |
|---|---|---|
| White | `--c-bg` | Odd sections |
| Light | `--c-bg-light` | Even sections |
| Dark | `--c-dark` | Title page, optional accent sections |
