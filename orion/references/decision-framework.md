# Decision Framework

A thinking method, not a template. This defines HOW to decide what matters. Formatting rules (`${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`) define HOW to write it down.

## Mission

Your job is not to fill templates. Your job is to make downstream decisions easier.

Every line of output should pass this test: "If I deleted this line, would the next phase produce a worse result?" If no, the line shouldn't exist.

The mission reframes facts. Without it, "dual lightbox plugins installed" is a technical observation. With it, it becomes "technical debt = cleanup item in proposal scope." Same fact, completely different utility. The mission turns researchers into proposal builders.

## Four Filters

Apply in order to every piece of information you encounter:

**1. Decision Relevance** — "Would this change what we propose, price, ask, or recommend?" YES = capture. NO = drop.

**2. Anomaly Detection** — "Is this different from what you'd expect?" Anomalies are high-value: missing things that should exist, things that exist but shouldn't, quantities unusually high or low. Expected findings can be dropped — the consumer already assumes the baseline.

**3. Quantification** — "Can you put a number on it?" Numbers over adjectives. Always. Ranges when exact numbers aren't available. "Zero" and "none" are numbers.

**4. Self-Containment** — "Can someone understand this line without reading anything else?" One fact per line. Each line stands alone. If it needs context, add the context inline.

## Hypothesis

When your task has a testable assumption, start with it. Verify, quantify, report.

When a hypothesis is wrong, that's often the most valuable finding. Capture three things:
- **Status** — CONFIRMED / PARTIALLY CONFIRMED / CHALLENGED / INVALIDATED
- **Challenged by** — the specific evidence (one line, self-contained, quantified)
- **Implication** — how this changes the downstream decision

The implication matters more than the fact. A challenged hypothesis without an implication is just a note. With an implication, it's a course correction.

## Baseline Awareness

Read `baseline-log.txt` before starting any work. It contains key findings from all preceding agents — the cumulative knowledge of what THIS project looks like.

The baseline defines "typical" so you know what's worth noting (deviations) and what's noise (expected). A photographer having a portfolio page is expected — don't note. Zero CTAs and 4 clicks to contact is an anomaly — note it.

Two baselines compound:
- **Static** — what's typical for this project type (provided by substage definitions)
- **Cumulative** — what prior agents found about THIS project (in baseline-log.txt)

By later phases, the agent reads a substantial cumulative log (see `formatting-rules.md` § Output Budgets for entry caps) and starts from a precise, evidence-backed model — not from "typical portfolio redesign."

## Stopping Rule

Done when you can answer the decision question, not when you've checked everything. If you've verified the hypothesis and captured the anomalies, stop. More research after the decision question is answered = noise.

## Proposal Impact Section

Every R-file must end with a `PROPOSAL IMPACT` section: a specific list of what this stage's findings would add, change, or remove from the proposal. Not "key takeaways" — concrete proposal consequences.

Each entry answers: "Because we found X, the proposal should Y." If a finding doesn't appear in this section, it's context for other researchers, not a proposal driver.

This is Filter 1 applied at the output level. If a stage produces 40 findings but only 6 change the proposal, the proposal impact section has 6 entries. The rest stay in the body for downstream stages to reference but don't carry forward to Concept Creation.

## Escalation

If you find something that changes the project framing — not just your current task — surface it immediately. Don't bury it as an anomaly.

Examples: the local market has no websites (questions whether a website proposal is right), the client is legally prohibited from collecting leads (invalidates conversion-focused mission), 90% of the target audience uses RFPs not websites (changes the sales channel assumption).

## What Not To Do

- Do not note things that are true of every project of this type
- Do not write scripts to process your own output
- Do not ignore evidence that challenges the hypothesis
- Do not include findings without a source tag (in output files) or phase tag (in baseline-log)
- Do not fill gaps with plausible guesses — report MISSING
- Do not generate more findings than pass the four filters — if you have 30+, you're not filtering hard enough
