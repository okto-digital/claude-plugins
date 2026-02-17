---
name: website-ux-component-matcher
description: "Match content to optimal UX components, map to content slots, and provide implementation guidance. Use when selecting UX components for content types, mapping content to component slots, suggesting page layout patterns, or starting website content workflow."
allowed-tools: Read
version: 1.0.0
---

# Website UX Component Matcher

**Purpose:** Match content to optimal UX components, map to content slots, and provide implementation guidance

**Component library:** 82 components across 10 categories. For complete details, see:
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/ux-index-and-patterns.md` -- Quick reference, content type index, page patterns
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/ux-cat-1-5.md` -- Categories 1-5: Navigation, Hero, Content Display, Disclosure, Forms
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/ux-cat-6-10.md` -- Categories 6-10: Media, Feedback, CTA, Social Proof, E-commerce
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/ux-schema-1-5.yaml` -- YAML schema for categories 1-5
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/ux-schema-6-10.yaml` -- YAML schema for categories 6-10 + content type mapping
- `${CLAUDE_PLUGIN_ROOT}/skills/website-ux-component-matcher/resources/sources-keywords.md` -- Source research and keyword data

---

## When to Use This Skill

- Recommend UX components for specific content types
- Map content to component content slots with character limits
- Suggest component pairings for page layouts
- Provide accessibility and mobile guidance
- Select between multiple valid component options

**CRITICAL:** Use this skill FIRST in the website content workflow, before formatting or SEO optimization. You need to know WHAT component pattern to use before deciding HOW to format it.

---

## Quick Reference by Content Type

### Marketing Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Key benefits (3-6) | feature-grid | value-prop-section, bento-grid |
| Single hero message | hero | cta-section |
| Customer logos | logo-cloud | testimonial (with logos) |
| Company metrics | stats-bar | bento-grid, card-grid |
| Social proof quotes | testimonial | review-card, quote-block |

### Navigation Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Main site nav | navbar | mobile-drawer (mobile) |
| Page hierarchy | breadcrumbs | sidebar-nav |
| Long-form TOC | anchor-nav | sidebar-nav (sticky) |
| Section switching | tabs | accordion |
| Many pages | pagination | load-more button |

### Product/Service Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Product features | feature-grid | tabs, accordion |
| Feature comparison | comparison-table | tabs, card-grid |
| Pricing tiers | pricing-table | card-grid |
| Product photos | product-gallery | carousel, image-gallery |
| Product specs | comparison-table | accordion, tabs |

### Educational Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| FAQ | accordion | tabs, anchor-nav |
| How-it-works steps | timeline | feature-grid (numbered) |
| Process explanation | timeline | feature-grid, tabs |
| Documentation | sidebar-nav + anchor-nav | accordion |
| Legal/policy | anchor-nav + accordion | collapsible sections |

### Blog/Article Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Post previews | card-grid | masonry |
| Related articles | card-grid | carousel |
| Author info | avatar + testimonial | card |
| Article TOC | anchor-nav (sticky) | collapsible section |
| Pull quotes | quote-block | testimonial |

### Form Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Simple inquiry | contact-form | modal + contact-form |
| Email capture | newsletter-signup | exit-intent popup |
| Long form | multi-step-form | single-page form + progress |
| Product search | search-bar + filter-controls | sidebar-nav + search |
| Feedback | rating-input + contact-form | modal + rating |

### E-commerce Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Product listing | product-card (grid) | carousel |
| Mini cart | cart-preview (dropdown) | modal, sidebar |
| Checkout summary | checkout-summary (sidebar) | checkout-summary (collapsible) |
| Reviews | review-card (grid) | testimonial, carousel |
| Trust signals | trust-badges | logo-cloud |

### Media Content
| Content | Primary Components | Alternative Components |
|---------|-------------------|----------------------|
| Photo collection | image-gallery + lightbox | masonry + lightbox |
| Video content | video-embed | modal + video-embed |
| Portfolio | masonry | card-grid, bento-grid |
| Before/after | carousel (2 slides) | comparison slider |
| Team photos | card-grid + avatar | testimonial |

---

## Component Selection Process

### Step 1: Analyze Content Characteristics

- What is the content type? (benefits, FAQs, products, navigation, etc.)
- How many items? (1, 2-5, 6-12, 13+)
- Does hierarchy matter? (equal importance vs featured item)
- What's the user goal? (find, compare, understand, take action)
- What's the context? (homepage, product page, documentation, blog)

### Step 2: Identify Candidate Components

From the 82-component library, select 2-3 candidates based on content type match, item count, hierarchy requirements, mobile-first and accessibility considerations. Use Quick Reference tables above.

**Component Categories (82 total):**
1. Navigation & Wayfinding (9)
2. Hero & Landing (5)
3. Content Display (8)
4. Disclosure & Progressive (4)
5. Forms & Input (6)
6. Media & Visual (5)
7. Feedback & Status (5)
8. Call-to-Action (4)
9. Social Proof (3)
10. E-commerce Specific (5)

### Step 3: Evaluate Trade-offs

For each candidate, consider: best-for use cases, avoid-when anti-patterns, available variants, component pairings, mobile adaptation, accessibility requirements. Reference the detailed component files in `resources/`.

### Step 4: Map Content to Slots

For each recommended component, provide:
- Component ID and name
- Content slot mapping with character limits
- Required vs optional fields
- Accessibility notes
- Mobile considerations
- Suggested pairings

**For character limits and slot specifications, see:** `resources/ux-index-and-patterns.md`

### Step 5: Suggest Page Patterns (Optional)

If building full page, reference common patterns:

**Homepage:** announcement-bar (opt) -> navbar -> hero -> logo-cloud -> feature-grid/value-prop -> stats-bar -> testimonial -> cta-section -> footer-nav

**Landing Page:** navbar (minimal) -> hero -> value-prop/feature-grid -> stats-bar -> testimonial -> pricing-table (opt) -> cta-section -> footer-nav (minimal)

**Product/Service:** navbar -> hero (product) -> feature-grid -> comparison-table -> testimonial -> pricing-table -> cta-section -> footer-nav

**Documentation:** navbar -> breadcrumbs -> sidebar-nav (sticky) -> anchor-nav (TOC) -> accordion (FAQ) -> footer-nav

---

## Integration with Other Website Skills

**Recommended Workflow Sequence:**

1. **website-ux-component-matcher** (THIS SKILL) -- Select WHAT component patterns to use
2. **website-content-architect** -- Determine strategic structure (pillar vs hub vs single page)
3. **website-content-formatter** -- Format content for scanners + search bots
4. **website-seo-metadata** -- Generate technical SEO metadata
5. **website-conversion-optimizer** -- Optimize for conversions

---

## Anti-Boring Principle Integration

This skill supports okto-digital's core principle: **"Being boring is a dangerous strategy"**

**How component selection supports anti-boring content:**

1. **Pattern Interrupts:** Recommend unexpected component combinations
   - NOT: hero -> features -> cta (predictable)
   - YES: hero -> stats-bar -> testimonial -> bento-grid -> cta (varied)

2. **Visual Variety:** Mix component types within pages
   - Use bento-grid (asymmetric) instead of always card-grid (symmetric)
   - Combine timelines with feature-grids instead of stacking feature-grids

3. **Unexpected Presentations:** Use surprising content in standard components
   - Case-study-preview with surprising metrics in headlines
   - Feature-grid with contrarian titles

4. **Component Variants:** Choose interesting variants
   - Hero: video-background instead of static image
   - Testimonial: carousel with video instead of static text

**When recommending components, favor:** visual interest, asymmetric layouts, varied component types over repetition.

---

## Reference Files

- `resources/ux-index-and-patterns.md` -- Quick reference, content type index, character limits, page patterns
- `resources/ux-cat-1-5.md` -- Categories 1-5 detailed component specifications
- `resources/ux-cat-6-10.md` -- Categories 6-10 detailed component specifications
- `resources/ux-schema-1-5.yaml` -- YAML schema for categories 1-5
- `resources/ux-schema-6-10.yaml` -- YAML schema for categories 6-10
- `resources/sources-keywords.md` -- Source research and keyword data

---

**Version:** 1.0.0
