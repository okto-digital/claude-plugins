---
name: brand-voice-research-transformer
description: "Transform generic research, articles, and competitor content into unique okto-digital content using SPECIFIC, POINTED questions. Use when converting external research into brand-aligned content, adapting competitor content, or creating unique perspectives from industry articles."
allowed-tools: Read, Edit, AskUserQuestion
version: 1.0.0
---

# Brand Voice Research Transformer

**Purpose:** Transform research, articles, and competitor content into uniquely okto-digital content

**CRITICAL:** This skill uses SPECIFIC, POINTED questions - NEVER vague ones

**When to Use:**
- User provides research article for transformation
- Transforming competitor content
- Adapting generic industry content
- Converting external insights to okto-digital perspective

**Brand Voice Reference:** `${CLAUDE_PLUGIN_ROOT}/docs/brand-voice-definition.md`

---

## Why Pointed Questions Matter

**The Problem with Vague Questions:**
- "How do you do this differently?" -> Produces vague answers
- "What makes you unique?" -> Generic claims
- "What's your approach?" -> Abstract descriptions

**The Power of Pointed Questions:**
- "This article recommends React Native. What do YOU use and why?" -> Specific tool + reasoning
- "Walk me through YOUR exact steps." -> Concrete process
- "Give me a recent client example." -> Real situation

**Result:** Content that's genuinely unique to okto-digital, not just reworded research.

---

## Process

### 1. Read & Analyze Source Material

- Read research article, blog post, or competitor content thoroughly
- Identify key concepts, recommendations, and claims
- Note generic statements that need okto-digital specifics
- Highlight areas where okto-digital perspective would differ

### 2. Ask SPECIFIC, POINTED Questions

**CRITICAL:** Use pointed questions from templates -- NEVER ask vague questions.

Select appropriate question type based on content. Five categories of templates are available:
- **A. Technical Content** -- tool/technology recommendations, technical approaches
- **B. Process Content** -- process steps, workflows
- **C. Case Study/Example** -- client situations, problem-solution patterns
- **D. Recommendation/Advice** -- best practices, strategic decisions
- **E. Industry Trends** -- trends, predictions

**Full question templates with pointed/vague examples:** `${CLAUDE_PLUGIN_ROOT}/skills/brand-voice-research-transformer/resources/question-templates.md`

### 3. Transform Content

**With answers to pointed questions, transform research into unique okto-digital content:**

**Incorporate:**
+ Specific okto-digital processes and tools
+ Real client examples (anonymized appropriately)
+ Actual timelines and outcomes
+ Genuine learnings from projects
+ okto-digital's unique perspective on recommendations
+ Technical details specific to how okto-digital works

**Avoid:**
- Simply rewording the research
- Keeping generic examples
- Abstract claims without specifics
- Corporate language (use okto-digital voice)

**Apply Brand Voice:**
- Formality: Casual (baseline) + channel adjustment
- Tone: Reliable, Genuine, Curious
- Language: Plain, concrete, no buzzwords
- Readability: 9th-10th grade
- Archetype: Creator + Everyman + Sage + Jester moments

### 4. Verify Uniqueness

**Before finalizing, check:**

+ **Is it genuinely okto-digital?**
  - Uses specific okto-digital tools/processes
  - Includes real client situations
  - Reflects actual experience

+ **Is it NOT just reworded research?**
  - Different examples (not generic ones from article)
  - okto-digital perspective (not just paraphrased author view)
  - Specific details (not abstract claims)

+ **Does it sound authentic?**
  - Genuine voice (Reliable, Genuine, Curious)
  - Down-to-earth language (Everyman)
  - Knowledge-sharing tone (Sage)
  - Subtle wit if appropriate (Jester moments)

### 5. Log Transformation Insights

**Use brand-voice-logger skill if:**
- Certain pointed questions were exceptionally effective
- Research revealed new content area needing voice guidance
- Transformation pattern worth documenting
- User feedback indicates content is uniquely okto-digital

---

## Quality Checklist

Transformed content must meet:

+ **Uniqueness:**
  - Specific okto-digital processes (not generic research)
  - Real client examples (not article's examples)
  - Actual tools and approaches okto-digital uses
  - Genuine okto-digital perspective

+ **Voice Compliance:**
  - Casual formality
  - Reliable, Genuine, Curious tone
  - Plain language (no buzzwords)
  - Readability: 9th-10th grade
  - Archetype balance

+ **Pointed Questions Used:**
  - Never vague questions
  - Always specific, concrete
  - Extract unique details

---

## Common Mistakes to Avoid

**MISTAKE 1: Vague Questions**
- "How do you do this differently?"
+ "This recommends React. What do YOU use and why?"

**MISTAKE 2: Just Rewording**
- Taking research and changing words but keeping examples
+ Extract okto-digital examples through pointed questions

**MISTAKE 3: Abstract Answers**
- Accepting "We have a unique approach" as answer
+ Push for specifics: "Walk me through exact steps from recent project"

**MISTAKE 4: Skipping Follow-ups**
- One question per topic
+ Drill down: "Tell me more about [specific detail]"

**MISTAKE 5: Generic Voice**
- Transforming content but losing okto-digital voice
+ Apply casual tone, genuine language, down-to-earth examples

---

## Reference Files

- `resources/question-templates.md` -- Full question templates (A-E) with pointed/vague examples, plus example transformation walkthrough

---

**Version:** 1.0.0
