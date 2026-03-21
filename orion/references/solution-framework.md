# Solution Framework

A thinking method for agents that propose, not collect. The decision framework (`${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md`) governs research agents — collectors and filters. This file governs solution agents — synthesizers and decision makers.

Research agents fail by collecting wrong things or inventing sources. Solution agents fail by **connecting wrong dots** — selective reading, premature conclusion, false synthesis, proposing what's familiar rather than what's right. The enemy is not noise. It is **false coherence**.

## The Boundary

The research tells you what IS. The solution proposes what SHOULD BE. Never confuse the two. A solution agent that presents recommendations as findings produces proposals that are wrong in ways very hard to catch.

## Input Quality Check

Before synthesizing — assess what you're working with:
- How many CONFIRMED findings vs INFERRED?
- Are there unresolved contradictions between substages or domains?
- Is any critical field MISSING that would change the recommendation?

If critical gaps exist — flag before proceeding. Do not paper over them.

## ICIP Sequence

Four questions, asked in order. Do not skip to PROPOSE.

**INTERPRET** — What does the combined research actually show — not per substage, but as a whole picture? What is the dominant pattern? State it in one sentence before proposing anything.

**CHALLENGE** — What in the research contradicts or complicates that pattern? Name it explicitly. Do not smooth it over.

**INVERT** — What would guarantee failure for this client's goals? What must the solution absolutely prevent? (Munger: instead of asking "what should we build?" ask "what would make this project fail?" Then eliminate those conditions first.)

**PROPOSE** — What is the simplest solution that addresses the confirmed findings, eliminates the failure conditions, and is honest about what's INFERRED?

## Divergent Before Convergent

Solution agents have two distinct jobs that must never happen simultaneously:

- **Divergent** — what are all the possible interpretations of this data?
- **Convergent** — which interpretation is best supported by evidence?

Most agents skip divergent and go straight to convergent — they produce the first plausible solution, not the best one. The ICIP sequence forces both: INTERPRET and CHALLENGE are divergent. INVERT and PROPOSE are convergent.

## Solution Filters

Adapted from the research filters. Applied to every recommendation:

**1. Decision** — Does this recommendation change scope, price, or approach? If removing it changes nothing downstream, it shouldn't exist.

**2. Evidence** — Which CONFIRMED finding justifies this? Every major recommendation must trace back to at least one CONFIRMED finding. INFERRED findings can inform — never justify alone. MISSING findings flag risk.

**3. Simplicity** — Is there a simpler version that achieves the same outcome? Between two solutions that equally address the findings, prefer the simpler one. Solution agents tend toward complexity because complexity signals effort. Simplicity is the goal.

**4. Honesty** — Is any part of this built on INFERRED or MISSING data? Label it. Do not present uncertain recommendations with the same confidence as evidence-backed ones.

## First Principles

Do not derive solutions from what's conventional in this space. Derive them from what the research actually shows. The baseline exists for anomaly detection — not for solution generation. What competitors do is evidence, not prescription.

## Null Hypothesis

Before committing to a recommendation, try to disprove it:
- What evidence in the research contradicts this?
- What would have to be true for this NOT to be the right approach?

If you cannot find a counter-argument, you either haven't looked hard enough or the solution is genuinely strong.

## Escalation

Escalate immediately if:
- A recommendation contradicts the client's stated goal
- Two confirmed findings point to opposite solutions
- The simplest viable solution exceeds a reasonable scope for this project type

## What Not To Do

- Do not skip INTERPRET and jump straight to PROPOSE
- Do not build a solution on the findings you understood best instead of the findings that matter most
- Do not smooth over contradictions — name them
- Do not add complexity to signal thoroughness
- Do not treat competitor patterns as requirements — they are evidence
- Do not present INFERRED recommendations as if they were CONFIRMED
