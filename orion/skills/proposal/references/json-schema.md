# D6-Proposal -- JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

## Schema

```json
{
  "proposal": {
    "title_page": {
      "project_title": "string",
      "client_name": "string",
      "prepared_by": "string",
      "date": "string",
      "version": "string"
    },
    "executive_summary": {
      "headline": "string",
      "project_overview": "string",
      "opportunity_statement": "string",
      "traffic_potential": {
        "conservative_monthly": "number",
        "realistic_monthly": "number",
        "optimistic_monthly": "number"
      }
    },
    "problem_statement": {
      "current_situation": "string",
      "pain_points": ["string"],
      "key_challenges": ["string"],
      "evidence": [
        {
          "domain": "string (e.g. Search & SEO, Competitive Landscape, Technology)",
          "findings": [
            {
              "text": "string",
              "metric": "string | null"
            }
          ]
        }
      ]
    },
    "proposed_solution": {
      "strategy_overview": "string",
      "methodology": "string",
      "desired_outcome": "string",
      "concept_highlights": {
        "positioning": "string",
        "visual_direction": "string",
        "tone_of_voice": "string",
        "ux_approach": "string",
        "seo_approach": "string",
        "compliance_approach": "string"
      }
    },
    "scope_of_work": {
      "modules": [
        {
          "id": "string",
          "name": "string",
          "category": "strategy | design | frontend | backend | ecommerce | integration | content | seo | migration | multilingual | analytics | post-launch",
          "description": "string",
          "inclusions": ["string"],
          "hours_est": "number",
          "complexity": "simple | moderate | complex",
          "dependencies": ["string (module id)"],
          "phase": "launch | post-launch",
          "priority": "must_have | should_have | nice_to_have",
          "selected": "boolean"
        }
      ],
      "sitemap_summary": {
        "page_count": "number",
        "traffic_potential": {
          "conservative_monthly": "number",
          "realistic_monthly": "number",
          "optimistic_monthly": "number"
        },
        "page_tree": [
          {
            "name": "string",
            "path": "string",
            "traffic_conservative": "number",
            "traffic_realistic": "number",
            "children": ["recursive"]
          }
        ]
      }
    },
    "timeline": {
      "phases": [
        {
          "phase": "number",
          "name": "string",
          "description": "string",
          "duration": "string",
          "modules_included": ["string (module id)"]
        }
      ],
      "total_duration": "string",
      "milestones": [
        {
          "name": "string",
          "date_offset": "string",
          "description": "string"
        }
      ]
    },
    "investment": {
      "breakdown": [
        {
          "module_id": "string",
          "module_name": "string",
          "category": "string",
          "hours": "number"
        }
      ],
      "total_hours": "number",
      "pricing_note": "string"
    },
    "about_us": {
      "company_intro": "string",
      "team_highlights": ["string"],
      "case_studies": ["string"],
      "note": "placeholder"
    },
    "conclusion": {
      "call_to_action": "string",
      "next_steps": ["string"],
      "acceptance": {
        "client_name_field": "string",
        "date_field": "string",
        "signature_field": "string"
      }
    },
    "notes": ["string"]
  }
}
```

Write to `D6-Proposal.json`.

## Field Notes

### title_page

`client_name` and `project_title` populated from `project.json` fields `project.client` and `project.name`. `prepared_by` defaults to "oktodigital". `date` is the generation date. `version` starts at "1.0".

### executive_summary

Written last (Step 9 in SKILL.md). Synthesises all other sections into a concise overview. `headline` is a single sentence -- the project's positioning statement.

### problem_statement

Replaces the v1.0.0 `research_findings[]` array. Research data is now contextualised as evidence supporting the problem narrative.

- `current_situation` -- 2-3 sentences describing where the client is today
- `pain_points` -- specific business problems the website should solve
- `key_challenges` -- obstacles or constraints (technical, market, competitive)
- `evidence` -- grouped by research domain, max 3-5 findings per domain

### proposed_solution

Synthesised from D5 concept TLDRs: C4 (content strategy), C5 (visual), C6 (UX), C8 (SEO), C9 (compliance). Replaces the v1.0.0 "Website Concept" section with a narrative framing.

- `concept_highlights` -- one-sentence summaries per dimension, client-friendly language. `compliance_approach` covers WCAG level, GDPR, and any industry-specific regulations from C9.

### scope_of_work

Combines v1.0.0 top-level `modules[]` and the sitemap section into a single scope block.

- `modules` -- schema unchanged from v1.0.0
- `sitemap_summary.page_tree` -- recursive structure, arbitrary depth. Each node has `name`, `path`, traffic estimates, and optional `children[]`

### timeline

Enhanced from v1.0.0 with explicit `total_duration` and optional `milestones[]`.

- `milestones` -- key dates beyond phase boundaries (e.g., "Content freeze", "UAT start"). Omit if not applicable.

### investment

Restructured from v1.0.0. `breakdown` now includes `category` for grouped display. Only `selected: true` modules appear in `breakdown`.

- `pricing_note` -- always "To be completed by operator". Agent NEVER generates pricing, rates, or payment terms.

### about_us

Always present with `note: "placeholder"`. The agent generates a skeleton structure; the operator fills actual content.

- `company_intro` -- placeholder: "About [company name]..."
- `team_highlights` -- empty array or generic placeholders
- `case_studies` -- empty array or generic placeholders

### conclusion

Replaces v1.0.0 `next_steps[]`. Adds a call-to-action paragraph and acceptance/signature block.

- `acceptance` fields contain empty strings. Rendered as blank signature lines in markdown and input fields in HTML.

## Removed from v1.0.0

| v1.0.0 Field | Status | New Location |
|---|---|---|
| `meta` | Replaced | `title_page` |
| `research_findings[]` | Absorbed | `problem_statement.evidence` |
| Top-level `modules[]` | Moved | `scope_of_work.modules` |
| Top-level sitemap section | Moved | `scope_of_work.sitemap_summary` |
| `next_steps[]` | Moved | `conclusion.next_steps` |
| `investment.modules_selected` | Removed | Derived from `breakdown` |
