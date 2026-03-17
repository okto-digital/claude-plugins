# Decision Framework

Your job is not to fill templates. Your job is to make downstream decisions easier.
Every line of output should pass this test: "If I deleted this line, would the next phase produce a worse result?" If no, the line shouldn't exist.

## Four Filters

Apply in order to every piece of information you encounter:

**1. Decision Relevance** — "Would this change what we propose, price, ask, or recommend?" YES = capture. NO = drop.

**2. Anomaly Detection** — "Is this different from what you'd expect?" Anomalies are high-value: missing things that should exist, things that exist but shouldn't, quantities unusually high or low. Expected findings can be dropped — the consumer already assumes the baseline.

**3. Quantification** — "Can you put a number on it?" Numbers over adjectives. Always. Ranges when exact numbers aren't available. "Zero" and "none" are numbers.

**4. Self-Containment** — "Can someone understand this line without reading anything else?" One fact per line. Each line stands alone. If it needs context, add the context inline.

## Source Binding

Every finding must reference where it came from. No source = drop the finding.

**In R-files, D-files, G-files, C-files:** Tag with `[src: category]` — categories: `tool`, `document`, `registry`, `operator`, `url`, `other`.

**In baseline-log.txt:** Do NOT use `[src: ...]` tags. The source is the phase tag itself — `[R1]`, `[D2]`, `[G05]`, `[C3]`. The reader knows where to look for detail.

**Confidence** — end every finding with one of:
- CONFIRMED — found directly in source, verifiable
- INFERRED — deduced from available evidence
- MISSING — looked for, not found (the absence IS the finding)

Findings that affect scope or pricing need 2 independent sources for CONFIRMED. Single source = INFERRED. An agent that reports MISSING is more valuable than one that invents a plausible number.

## Hypothesis

When your task has a testable assumption, start with it. Verify, quantify, report. When a hypothesis is wrong, that's often the most valuable finding — capture what challenged it and what it means for downstream decisions. The implication matters more than the fact.

## Escalation

If you find something that changes the project framing — not just your current task — surface it immediately. Don't bury it as an anomaly.

## Output Style

TXT, not JSON. Telegraphic — no prose, no filler, no hedging. Self-contained. Source-tagged (in output files). Scannable formatting per `formatting-rules.md`.

## Baseline Log

<critical>
The baseline log is a **signal index**, not a research summary. Only key findings that change downstream decisions. Telegraphic one-liners. No prose, no paragraphs, no roadmaps, no methodology notes.
</critical>

**Format:**
```
--- [R1] SERP ---
[R1] Client ranks for 2 keywords only, zero commercial keywords indexed. CONFIRMED
[R1] "komerčná fotografia" greenfield — zero related keywords, jms-studio.sk sole occupant. CONFIRMED
```

**Rules:**
- Start with a `--- [CODE] TITLE ---` header before your entries
- Tag every line with your phase code: `[INIT]`, `[D2]`, `[R1]`–`[R9]`, `[D4]`, etc.
- One fact per line. If it takes more than one line, split it or you're including too much
- No `[src: ...]` tags — the phase code IS the source reference
- No empty lines between your entries
- End each line with CONFIRMED, INFERRED, or MISSING
- **Deduplicate:** Read existing baseline-log entries BEFORE appending. If a finding already exists, do NOT re-log it. Only add if you bring new quantification or a materially different angle
- **Append at once:** Accumulate all your entries, then append them in a single batch at the end of your work. Do not append incrementally during processing
- Do NOT invent tags. The only valid confidence markers are CONFIRMED, INFERRED, MISSING. Do not use CRITICAL DECISION POINT or other ad-hoc labels
- Never edit or delete existing lines — append only

## What Not To Do

- Do not note things that are true of every project of this type
- Do not write scripts to process your own output
- Do not ignore evidence that challenges the hypothesis
- Do not include findings without a source tag (in output files) or phase tag (in baseline-log)
- Do not fill gaps with plausible guesses — report MISSING
