---
name: brand-voice-logger
description: "Append feedback entries to voice-feedback.md for Brand Voice Architect review. Use when encountering voice violations, edge cases, new content types, platform additions, success patterns, or research transformation insights."
allowed-tools: Read, Edit
version: 1.0.0
---

# Brand Voice Logger

**Purpose:** Append structured feedback entries to voice-feedback.md

**When to Use:**
- Voice violations (user requests that break rules)
- Modification requests (adjustments beyond current guidance)
- New content types (no existing voice guidance)
- Platform additions (new channels/social networks)
- Edge cases (unclear or conflicting situations)
- Success patterns (exceptionally effective content)
- Research transformation insights

---

## Usage

Invoke this skill whenever you encounter situations requiring voice framework updates.

---

## Entry Format

When logging, use the Edit tool to append the following format to the project's `voice-feedback.md` file:

```markdown
## YYYY-MM-DD HH:MM | [Category]
**Type:** [Specific type description]
**Context:** [What happened]
**Issue:** [What guidance is missing or conflicting]
**Resolution:** [How you handled it]
**For Architect:** [What voice update would help]
```

**Categories:**
- Voice Violation
- Modification Request
- New Content Type
- Platform Addition
- Edge Case
- Success Pattern
- Research Transformation

**Timestamp:** Use the current date and time in `YYYY-MM-DD HH:MM` format.

**File location:** The `voice-feedback.md` file should exist in the project root. If it does not exist, create it with a `# Voice Feedback Log` heading before appending.

---

## Input Fields

All fields are required:

| Field | Description |
|---|---|
| category | One of the 7 categories listed above |
| type | Specific type description (e.g., "Buzzword request") |
| context | What happened that triggered the log |
| issue | What guidance is missing or conflicting |
| resolution | How you handled the situation |
| for_architect | What voice update would help |

---

## Examples

### Voice Violation Example

```markdown
## 2025-11-15 14:30 | Voice Violation
**Type:** Buzzword request
**Context:** User wanted "leverage synergy" in investor pitch
**Issue:** Violates language style rules (buzzwords prohibited)
**Resolution:** Used "work together effectively" instead
**For Architect:** Consider investor communication channel rules - may need specific guidance for pitch decks
```

### New Content Type Example

```markdown
## 2025-11-15 16:45 | New Content Type
**Type:** Podcast script
**Context:** Creating audio content for okto-digital podcast
**Issue:** No audio-specific voice guidance in current framework
**Resolution:** Applied conversational casual tone, shorter sentences for speech
**For Architect:** Add audio content guidelines (podcast, video voiceover, webinar scripts)
```

### Success Pattern Example

```markdown
## 2025-11-15 18:00 | Success Pattern
**Type:** Blog post structure
**Context:** Discovery process explanation blog post
**Issue:** N/A - This worked exceptionally well
**Resolution:** Used concrete client example, step-by-step breakdown, genuine transparent tone
**For Architect:** Template this structure for other service explanation content
```

---

**Version:** 1.0.0
