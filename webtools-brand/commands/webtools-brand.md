---
description: "webtools-brand: Show available brand voice commands and current project state"
allowed-tools: Read, Glob
---

Show available webtools-brand commands, current brand voice status, and suggested next step.

---

## Read Project State

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: skip to the "No Project" output below.
- If it DOES exist: parse the Project Info (client name, project type) and the Document Log.

### 2. Document Status Check

Check existence of each relevant document:
- `brief/D1-project-brief.md` -- required input for brand voice
- `brand/D2-brand-voice-profile.md` -- brand voice output
- `brief/D14-client-research-profile.md` -- research intelligence (voice observations)
- `research/R2-competitor-landscape.md` -- competitor brand profiles
- `research/D15-research-report.md` -- consolidated research report

For each file: report "complete" if it exists, "not found" if it does not.

### 3. Content Folder Check

Glob for `content/*.md` and `content/**/*.md` to count existing content files.

- If files found: report count
- If no files or directory missing: report "empty" or "not found"

### 4. Website URL Check

If D1 was loaded, extract the client website URL from it.

- If found: report the URL
- If not found: report "none"

---

## Display Overview

### With Active Project

```
[BRAND] Webtools Brand -- [client name]

Available commands:
  /webtools-brand                Show this overview
  /webtools-brand-create         Interactive voice creation from scratch (Generate mode)
  /webtools-brand-extract        Auto-extract voice from existing content (Extract mode)

Current state:
  D1 Project Brief:         [complete / not found]
  D2 Brand Voice Profile:   [complete / not found]
  D14 Client Research:      [complete / not found]
  R2 Competitor Landscape:  [complete / not found]
  D15 Research Report:      [complete / not found]
  Content folder:           [X files found / empty / not found]
  Client website URL:       [URL from D1 / none]

Suggested next step: [see logic below]
```

**Next step logic:**

- No D1 -> "Run /webtools-intake first to produce D1 Project Brief."
- D2 exists -> "D2 is complete. Use /webtools-brand-extract to revise or /webtools-brand-create to start fresh."
- No D2, research docs available (D14 or R2 or D15 exists) -> "Research intelligence available. Run /webtools-brand-extract for research-informed extraction."
- No D2, no research docs, website URL from D1 -> "Run /webtools-brand-extract to analyze the client's existing website."
- No D2, no research docs, no website URL -> "Run /webtools-brand-create for interactive voice creation from scratch."

### No Project

If `project-registry.md` does not exist:

```
[BRAND] Webtools Brand

No project found in this directory.

Run /webtools-init to set up a new project first, then return here.

Available commands (after project setup):
  /webtools-brand                Show this overview
  /webtools-brand-create         Interactive voice creation from scratch (Generate mode)
  /webtools-brand-extract        Auto-extract voice from existing content (Extract mode)
```
