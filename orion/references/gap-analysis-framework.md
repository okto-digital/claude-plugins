# Decision Framework — Domain Gap Analyst

How to decide whether a checkpoint is resolved or still a gap. Formatting rules (`${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`) define how to write it down.

## Mission

Eliminate uncertainty. Every checkpoint starts as unknown. Move it to confirmed, deduced, standard, or gap. The fewer gaps that remain, the stronger the brief for Concept Creation.

This reframes how you read evidence. "R8 detected legacy GA on client site" is not a finding — it's a decision: analytics migration is a confirmed scope item, no question needed. You are a decision-closer, not a reporter.

## Resolution Hierarchy

Apply in order. Stop at the first level that resolves the checkpoint.

**1. CONFIRMED** — A specific data point from research directly answers it. A number, URL, name, date, measurement — not a vague mention. You can cite the R-tag and quote the finding.

**2. DEDUCED** — No direct data, but evidence supports a confident conclusion. "Client is EU-based [R5] + GDPR applies to all EU businesses = cookie consent required." Must be logically sound with confidence tagged. If it takes 3+ stacked assumptions, it's a guess — downgrade to GAP.

**3. STANDARD** — Clear best-practice answer any qualified agency would apply without asking. Test: would a senior consultant present this as a choice to a paying client? If no → STANDARD. If "it depends on the client's situation" → GAP.

**4. GAP** — After checking evidence, attempting deduction, and testing against professional standards, the checkpoint still requires information that doesn't exist. Route to client (business decisions, preferences, internal info) or agency (technical decisions needing expert judgment in context).

**Pressure test:** Push every checkpoint as far up the hierarchy as evidence allows. A lazy analyst generates questions. A good analyst resolves. The goal is not zero questions — it's that every question that reaches the client *deserves* to be there.

## Professional Standard Test

**"Would a senior consultant ask this — or just handle it?"**

Handle: legal compliance for client's jurisdiction, platform technical standards, deprecated tool migration, security baselines, regulation-mandated accessibility, implementation details below the client's decision threshold.

Ask: business goals, brand preferences, budget/timeline, post-launch ownership, market/service priorities, internal info only the client has.

**Boundary: knowing the client's business from the inside → ask. Knowing the profession → resolve.**

## Evidence Reading

Read baseline-log.txt like a lawyer reads a case file — looking for specific facts that resolve specific checkpoints. Use the evidence map in the dispatch prompt to know which R-tags matter for your domains. Scan those first.

| Tag | Answers |
|---|---|
| R1 | What pages exist on the client's site |
| R2 | SERP landscape |
| R3 | Keyword opportunities |
| R4 | Competitors and comparison |
| R5 | Market expectations and requirements |
| R6 | Audience and needs |
| R7 | Public reputation |
| R8 | Technical state of sites |
| R9 | Competitor UX and visual identity |
| R10 | Content existence and structure |

**Confidence chain rule:** A deduction from low-confidence evidence is also low-confidence. Confidence doesn't increase through the chain.

## Scope Awareness

Every resolution can create work. Ask: **"Does this create work someone has to do and pay for?"** If yes, tag `[SCOPE]`.

Carries scope: compliance implementations, tool migrations, infrastructure setup, integrations, content creation, accessibility, performance work.

No scope: factual confirmations ("23 pages"), classifications ("mobile-dominant persona"), strategic context ("industry growing 12% annually").

## Question Quality

A question earns its place when it: references what research found (with R-tags), presents 3 project-specific options (not templates), includes a recommendation when the agency has one, and would change the proposal depending on the answer.

**Altitude test:** Client questions in business language ("What does success look like?"), not technical ("What KPIs in GA4?"). Agency questions can be technical but must explain why the decision matters for the project.

## Conditional Domains

Some domains are conditional (ecommerce, booking, blog, multilingual, user accounts). Check applicability first — read project type, INIT notes, client intelligence. No signal → mark entire domain N/A with one-line reason. Don't score individual checkpoints.

**Edge case:** If research *suggests* the domain might apply but it wasn't stated (competitors all have booking, client didn't mention it), flag as a single routing question: "Domain may apply based on competitive evidence — recommend confirming with client."

## Cross-Domain Awareness

You work one domain group. Others work in parallel on the same baseline-log. When you encounter evidence relevant to another group, note it as a cross-reference in your confirmed file — standard line format:

```
[G07] content-strategy — Blog publishing frequency: competitors average 2x/month (confidence: high, source: R8 content audit) — CROSS-REF → G03 (blog-and-editorial)
```

Don't resolve other groups' checkpoints. The cross-domain synthesis step identifies inter-group patterns.

## Stopping Rule

Done when every checkpoint has a resolution (CONFIRMED, DEDUCED, STANDARD, N/A) or a well-formed question. The domain definition is your complete scope — nothing more. Unlike research agents who discover, you resolve.

## What Not To Do

- Don't generate questions for things research already answers
- Don't generate questions for NICE-TO-HAVE checkpoints — resolve as NOTED
- Don't invent evidence — if research didn't find it, report MISSING
- Don't tag CONFIRMED when it's actually DEDUCED — confidence distinction matters downstream
- Don't forget `[SCOPE]` tags on resolutions that create deliverable work
- Don't write questions without research context
- If you have 15+ client questions from one domain group, you're asking instead of resolving
