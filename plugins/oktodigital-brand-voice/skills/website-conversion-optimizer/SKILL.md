---
name: website-conversion-optimizer
description: "Conversion optimization including CTA placement, voice-compliant CTA wording, readability optimization, and conversion vs SEO balance. Use when adding CTAs, optimizing for conversions, analyzing readability, or balancing conversion with SEO goals."
allowed-tools: Read
version: 1.0.0
---

# Website Conversion Optimizer

**Purpose:** Conversion optimization including CTA placement, voice-compliant CTA wording, readability optimization, and conversion vs SEO balance

**For comprehensive conversion strategies, see:** `${CLAUDE_PLUGIN_ROOT}/skills/website-conversion-optimizer/resources/conversion-optimization-guide.md`

---

## Skill Overview

This skill optimizes content for conversions while maintaining SEO value. It provides CTA placement strategy, brand voice-compliant CTA wording, readability optimization (Flesch-Kincaid), and guidance on balancing conversion focus with SEO requirements.

**Core Functions:**
- CTA placement strategy (primary, secondary, tertiary)
- CTA wording library (voice-compliant examples)
- Readability optimization (Flesch-Kincaid scoring)
- Conversion vs SEO balance recommendations
- Trust signal placement

---

## CTA Placement Strategy

### By Page Type

**Landing Pages:**
- 1 primary CTA above fold (317% conversion increase)
- Single CTA focus (266% increase vs multiple CTAs)
- Repeat same CTA 2-3 times down page

**Service Pages:**
- 1 primary CTA above fold
- 2-3 secondary CTAs mid-content
- 1 tertiary CTA at end
- Total: 3-5 CTAs

**Blog Posts (Long-form 2,000+ words):**
- 1 CTA after introduction
- 1 CTA every 600-800 words
- 1 strong CTA at end
- Total: 3-4 CTAs

**Product Pages:**
- 1 primary "Buy Now" above fold
- 1 softer CTA mid-content ("Learn More")
- 1 primary CTA at end
- Total: 3 CTAs

### CTA Positioning

**Primary CTA (Above Fold):**
- Hero section, right side or center
- Prominent contrasting color
- Large button (min 48x48px tap target)

**Secondary CTAs (Mid-Content):**
- After value delivery/benefits section
- Every 600-800 words in long content
- Softer approach (informational, not pushy)

**Tertiary CTA (End of Content):**
- Strong call to action, reinforces primary CTA

**Mobile:** Sticky CTA button (bottom of screen), click-to-call for local services, min 48x48px tap targets

---

## Voice-Compliant CTA Wording

**Brand Voice Attributes:** Reliable (40%), Genuine (35%), Curious (25%), Casual formality, NO buzzwords/jargon/hype

**Strong CTAs (Decision Stage):** Action-oriented, direct, benefit-focused
- Examples: "Schedule Your Discovery Call", "Get Your Custom Quote", "Start Your Project Today", "Book Free Consultation", "Download Complete Guide", "See Pricing & Plans"

**Soft CTAs (Awareness/Consideration Stage):** Informational, non-threatening
- Examples: "See How It Works", "Explore Our Process", "Read Customer Stories", "View Case Studies", "Check Out Examples", "See What's Possible"

**Rules:**
- DO: Use action verbs, be specific, include benefit, keep casual but professional, be genuine
- DON'T: Use weak verbs ("Submit", "Click Here"), buzzwords ("Leverage", "Synergy"), hype, or generic CTAs ("Contact Us" without context)

---

## Readability Optimization

**Brand Voice Target:** 9th-10th grade reading level (Flesch Reading Ease 60-70)

| Audience | Target Grade Level | Flesch Reading Ease |
|----------|-------------------|---------------------|
| General | 9th-10th grade | 60-70 |
| Professional/B2B | 10th-12th grade | 50-60 |
| Technical | 11th-13th grade | 40-50 |

**Key simplification techniques:**
1. Break long sentences (one idea per sentence)
2. Replace complex words ("use" not "utilize", "help" not "facilitate")
3. Use active voice
4. Remove unnecessary filler words
5. Short paragraphs (2-3 sentences max)

**For Flesch-Kincaid formula, common readability issues, and tools, see:** `resources/conversion-optimization-guide.md`

---

## Conversion vs SEO Balance

**Page Structure for Dual Goals:**
- **Above Fold:** CONVERSION focus -- value prop, hero image, primary CTA, social proof
- **Mid-Content:** SEO focus -- comprehensive information, keyword coverage, depth
- **Final Section:** CONVERSION focus -- summary, final CTA, trust signals

**Prioritize Conversion:** Landing pages, product pages, pricing pages, contact pages (high-intent traffic)
**Prioritize SEO:** Blog posts, pillar pages, how-to guides (top-of-funnel traffic)
**Balance Both:** Strong conversion above fold, SEO-rich mid-page, conversion reinforcement at end

---

## Decision Framework

**Question 1:** What is primary page goal?
- Conversion -> Prioritize CTAs, above-fold value prop, short content
- Rankings -> Prioritize depth, comprehensive coverage, SEO

**Question 2:** What is traffic source?
- Paid ads -> Landing page structure (conversion focus)
- Organic search -> Blog structure (SEO + conversion balance)
- Direct/referral -> Service page structure (trust + conversion)

**Question 3:** What is user intent?
- Informational -> Long content, soft CTAs
- Commercial -> Medium content, moderate CTAs
- Transactional -> Short content, strong CTAs

---

## Output Format

```yaml
# CONVERSION OPTIMIZATION RECOMMENDATIONS

## CTA Strategy
primaryCTA:
  text: "[Voice-compliant CTA]"
  placement: "Above fold, hero section"
  style: "Large button, contrasting color"

secondaryCTAs:
  - text: "[Softer CTA]"
    placement: "After benefits section"

tertiaryCTA:
  text: "[Strong reinforcement CTA]"
  placement: "End of content"

## Readability
currentLevel: "[Grade level]"
targetLevel: "9th-10th grade"
fleschScore: [score]
recommendations:
  - "[Simplification suggestion]"

## Conversion vs SEO Balance
pageGoal: "conversion" | "rankings" | "balanced"
aboveFold: "Conversion-focused value prop + CTA"
midContent: "SEO-rich comprehensive coverage"
endSection: "Conversion reinforcement"

## Trust Signals
testimonials: [2-4]
clientLogos: "[Placement recommendation]"
statistics: "[Which stats to highlight]"

## Quality Checks
- [ ] Primary CTA above fold
- [ ] Secondary CTAs every 600-800 words
- [ ] Readability 9th-10th grade
- [ ] Voice-compliant CTA wording
- [ ] Trust signals present
```

---

## Reference Files

- `resources/conversion-optimization-guide.md` -- CTA research data, Flesch-Kincaid formula, trust signal types, internal linking strategy, detailed examples

---

**Version:** 1.0.0
