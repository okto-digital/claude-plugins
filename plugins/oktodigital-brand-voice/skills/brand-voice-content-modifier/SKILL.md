---
name: brand-voice-content-modifier
description: "Transform existing content to align with okto-digital brand voice. Use when modifying external content, repurposing competitor content, updating old content, or adjusting tone and formality for different channels."
allowed-tools: Read, Edit, AskUserQuestion
version: 1.0.0
---

# Brand Voice Content Modifier

**Purpose:** Modify existing content to fit okto-digital brand voice

**When to Use:**
- User provides existing content that needs voice alignment
- Repurposing competitor/generic content
- Updating old content to current voice standards
- Adjusting content from other sources

**Brand Voice Reference:** `${CLAUDE_PLUGIN_ROOT}/docs/brand-voice-definition.md`

---

## Process

### 1. Analyze Existing Content

**Read and identify:**
- Current tone and formality level
- Voice misalignments (buzzwords, jargon, wrong formality)
- Core message and key facts to preserve
- Structural issues (readability, flow)

### 2. Ask Contextual Questions

**MANDATORY if not clear:**
- "Where will the modified version be used?" (channel/platform)
- "What's the purpose?" (inform, convert, educate)
- "Who's the audience?" (decision-maker level, technical knowledge)
- "Any specific points you want emphasized or de-emphasized?"

### 3. Apply Brand Voice Framework

**Adjust systematically:**

**Formality:**
- Target: Casual (baseline) + channel adjustment
- Complete sentences (not fragments, unless social media)
- Conversational but professional
- Contractions allowed ("we're", "you'll")

**Language Style:**
- Replace buzzwords with plain language
- Remove jargon (or define if necessary)
- Use concrete over abstract
- Active voice preferred
- No ableist language

**Tone:**
- Reliable: Clear, consistent, trustworthy
- Genuine: Authentic, transparent, no fluff
- Curious: Question-driven, exploratory, thoughtful

**Readability:**
- Target: 9th-10th grade reading level
- Shorter sentences for clarity
- Break up long paragraphs
- Clear structure

**Archetype Balance:**
- Creator (50%): Innovation, quality emphasis
- Everyman (30%): Down-to-earth, approachable
- Sage (20%): Knowledge sharing, thoughtful
- Jester moments (15-20%): Subtle wit if appropriate

### 4. Preserve Core Message

**DO NOT change:**
- Key facts and data
- Core arguments
- Essential information
- Client commitments or promises

**DO change:**
- Wording and phrasing
- Tone and style
- Structure and flow
- Examples (if generic, make okto-digital specific)

### 5. Log Modification Patterns

**Use brand-voice-logger skill if:**
- User requested changes that violate voice
- Modification reveals edge case
- Pattern emerges (recurring modification type)
- Success: Modified content performs exceptionally well

---

## Example Modifications

### Example 1: Buzzword Removal

**Original:**
"We leverage cutting-edge technologies to synergize cross-functional paradigms and deliver best-in-class solutions that drive value-add outcomes for our stakeholders."

**Modified (okto-digital voice):**
"We use modern tools and clear processes to build software that solves real problems for your business."

**Changes:**
- "leverage" -> "use"
- "cutting-edge technologies" -> "modern tools"
- "synergize cross-functional paradigms" -> "clear processes"
- "best-in-class solutions" -> "software"
- "drive value-add outcomes" -> "solves real problems"
- "stakeholders" -> "your business"

---

### Example 2: Formality Adjustment

**Original (too formal):**
"Organizations seeking to implement comprehensive digital transformation initiatives require strategic partnerships with vendors possessing extensive technical expertise."

**Modified (casual, okto-digital voice):**
"If you're planning a digital transformation, you'll need a partner who really knows the technical side."

**Changes:**
- "Organizations seeking to implement" -> "If you're planning"
- "comprehensive digital transformation initiatives" -> "a digital transformation"
- "require strategic partnerships" -> "you'll need a partner"
- "vendors possessing extensive technical expertise" -> "who really knows the technical side"
- Conversational tone with contractions

---

### Example 3: Adding Genuine Voice

**Original (generic):**
"Our team of experienced professionals delivers quality results."

**Modified (genuine, okto-digital voice):**
"We're a small team of developers who care about building software that actually works for you. No fluff, just solid code and honest communication."

**Changes:**
- Generic -> Specific ("small team of developers")
- Corporate -> Genuine ("care about", "actually works")
- Added transparency ("No fluff, just solid code")
- Down-to-earth tone (Everyman archetype)

---

### Example 4: Channel Adjustment (Social Media)

**Original (website copy):**
"The discovery phase is a critical component of our development process. We conduct comprehensive stakeholder interviews and requirement analysis to ensure project success."

**Modified (LinkedIn post - very casual):**
"Discovery phase = project foundation.

We talk to everyone involved, figure out what you actually need (not just what you think you need), and map it out before writing a single line of code.

Skipping this? That's how projects go sideways."

**Changes:**
- Casual -> Very Casual (social media)
- Sentence fragments OK for social
- Conversational punctuation
- Direct, punchy
- Subtle Jester moment ("That's how projects go sideways")

---

## Quality Checklist

Modified content must meet:

+ **Voice Compliance:**
  - Core attributes present (Reliable, Genuine, Curious)
  - Appropriate formality (Casual + channel)
  - No buzzwords or jargon
  - Readability: 9th-10th grade

+ **Message Preservation:**
  - Core message intact
  - Key facts unchanged
  - Essential information retained

+ **Channel Appropriateness:**
  - Tone matches channel
  - Length appropriate
  - Format suitable

+ **Okto-Digital Authenticity:**
  - Sounds genuinely okto-digital
  - Specific where possible (not generic)
  - Archetype balance present

---

## Common Modification Patterns

### Pattern: Corporate -> Casual

**Replace:**
- "utilize" -> "use"
- "facilitate" -> "help" or "make easier"
- "implement" -> "build" or "set up"
- "leverage" -> "use"
- "stakeholders" -> "your team" or "your business"
- "solutions" -> "software" or specific term
- "best-in-class" -> remove or "effective"
- "synergy" -> "work together"

### Pattern: Formal -> Conversational

**Adjust:**
- Remove passive voice -> Active voice
- Long sentences -> Shorter, clearer
- Complex vocabulary -> Plain language
- No contractions -> Use contractions
- Third person -> Second person ("you")

### Pattern: Generic -> Specific

**Add:**
- Concrete examples over abstract claims
- Real scenarios (anonymized if needed)
- Specific tools/processes okto-digital uses
- Actual client situations

### Pattern: Fluff -> Genuine

**Remove:**
- Empty claims ("world-class", "innovative leader")
- Unnecessary adjectives
- Marketing speak
- Corporate jargon

**Add:**
- Honest statements
- Transparent explanations
- Real value propositions
- Down-to-earth language

---

**Version:** 1.0.0
