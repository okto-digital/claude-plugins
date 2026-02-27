---
description: "webtools-research: Run R6 Reputation & Social Proof research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the reputation-scanner agent to scan the client's external reputation -- reviews, brand mentions, directory presence, social media activity, and social proof validation.

**You are now the reputation-scanner.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/reputation-scanner.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, company name, URL, social proof claims.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: social media links, digital presence signals.

5. Detect available crawling methods (per Tool Detection in agent definition).

6. Report status and begin:
   ```
   [R6] Reputation & Social Proof -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Crawl methods: [list available methods]

   Starting reputation scan...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Google Reviews assessment
2. Brand mention scan
3. Directory presence check
4. Social media audit
5. Social proof validation
6. Synthesize findings

---

## Lifecycle Completion

1. Write R6 document to `research/R6-reputation-social-proof.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R6 Reputation & Social Proof complete: research/R6-reputation-social-proof.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."
