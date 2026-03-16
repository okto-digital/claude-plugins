# Content Generation Rules

Shared writing rules for all content generation modes. Apply these consistently regardless of source material (outline, research notes, extracted content, or operator instructions).

---

## Voice Application

- Apply the oktodigital brand voice attributes, tone spectrum, vocabulary guide, and style guidelines from `${CLAUDE_PLUGIN_ROOT}/references/voice-definition.md` throughout all content.
- If voice definition is not loaded, warn the operator: "Voice profile not loaded. Content may lack voice consistency."

---

## Source Outline Adherence

When working from an outline, follow it exactly:
- Do not add sections that are not in the outline.
- Do not remove sections that are in the outline.
- Do not reorder sections from their source order.
- Section headings in the output must match the outline headings (H2/H3 as specified).

---

## Client Input Flagging

Do not invent factual claims. Flag any section where real client input is needed:

```
[NEEDS CLIENT INPUT: This section requires [specific thing needed].
Placeholder content is provided for structure reference only.]
```

Things that always need real client input:
- Testimonials and client quotes
- Statistics, metrics, and numerical claims
- Team member names and bios
- Case study details
- Pricing information
- Specific certifications or awards

---

## Raw Content Incorporation

When the operator provides raw client content (e.g., "here's info about our process" or pasted content):
- Incorporate it naturally into the relevant section.
- Rewrite for voice consistency while preserving factual accuracy.
- Do not flag incorporated raw content as needing client input.

---

## Keyword Integration

When keyword targets are available (from PageOptimizer briefs or keyword research):
- Place keywords naturally in context. Restructure sentences if needed for flow.
- Do not stuff keywords. If a keyword cannot fit naturally, note it rather than forcing it.
- Keyword placement is guidance, not a hard requirement. The Optimize mode handles precise keyword scoring.

When no keyword targets are available:
- Write content without SEO considerations. Keywords can be added in a later optimization pass.

---

## Word Count Tracking

- Track word count per section and total.
- Report word count in the content statistics block.
- Flag significant deviations from target (if a target is specified).

---

## Formatting and Style

- Do not use emojis in any output.
- Use markdown formatting: H2/H3 for sections, bold for emphasis, lists where appropriate.
- Include CTA text if the section calls for a call to action.
- Include alt text suggestions for any referenced images or visuals.
- Add designer/developer notes where content implies specific layout needs.
