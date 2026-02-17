# oktodigital-brand-voice

Brand voice content generation plugin for Claude Code. Creates content aligned with okto-digital's 15-dimension voice framework (Reliable, Genuine, Curious) across all channels and formats.

## Installation

```bash
/plugin install oktodigital-brand-voice@oktodigital
```

Restart Claude Code after installing.

## Project Setup

Create these directories in your project root:

```bash
mkdir -p ingest/ output/
touch voice-feedback.md
```

| Directory/File | Purpose |
|---|---|
| `ingest/` | Place research articles and competitor content for transformation |
| `output/` | Auto-saved long-form content (>300 words) |
| `voice-feedback.md` | Automatic voice compliance log |

## What's Included

### Agent

**brand-voice-generator** -- Content creation specialist with three core workflows:
1. **Content Generation** -- Original content with contextual discovery
2. **Content Modification** -- Transform existing content to fit brand voice
3. **Research Transformation** -- Convert generic research into unique okto-digital content using pointed questions

### Skills (9)

| Skill | Purpose |
|---|---|
| brand-voice-logger | Log voice violations, edge cases, and success patterns |
| brand-voice-content-modifier | Transform existing content to match brand voice |
| brand-voice-research-transformer | Convert research into unique okto-digital content |
| brand-voice-dash-cleaner | Auto-correct improper dash and em-dash usage |
| website-ux-component-matcher | Match content to optimal UX components (82-component library) |
| website-seo-metadata | Technical SEO metadata optimization |
| website-content-formatter | Format content for dual audiences (scanners + search bots) |
| website-content-architect | Content architecture decisions (pillar, hub-and-spoke, single page) |
| website-conversion-optimizer | CTA placement, readability, conversion vs SEO balance |

### Documentation

- **brand-voice-definition.md** -- Complete 15-dimension voice framework (977 lines)
- Each website skill includes its own `resources/` directory with detailed reference docs

### Hooks

- **dash-cleaner** -- Automatically corrects dash and em-dash usage after every Write/Edit on `.md` files

---

## Workflows

### 1. Content Generation (From Scratch)

Provide context and the agent generates brand-aligned content.

```
User: Write a blog post about our discovery process

Agent: I'm assuming this is for the website blog. Is that correct?
       What specific aspects should I emphasize?
       Who's the primary audience?
       What's the goal?

User: Yes, website blog. Focus on why discovery prevents failures.
      Audience is business owners. Goal is educate + build trust.

Agent: [Generates blog post with brand voice compliance]
       [Auto-saves to output/ if >300 words]

       Do you need a shorter version? A/B variants? Social media posts?
```

**Quick mode:** Provide all context upfront to skip questions:
```
User: Quick LinkedIn post about our new case study - e-commerce client, 18% conversion increase
Agent: [Generates immediately from provided context]
```

### 2. Content Modification (Existing Content)

Transform content you already have into okto-digital's voice.

```
User: Can you modify this to sound like okto-digital?
      "Our enterprise-grade solutions leverage cutting-edge technologies..."

Agent: Where will this be used? What's the purpose?

User: Website homepage, above the fold

Agent: "We build custom software that solves real business problems.
       No buzzwords, no fluff - just solid code and honest communication."

       Changes: removed jargon, added Genuine attribute, casual tone
```

### 3. Research Transformation (Unique Content)

Convert generic research into genuinely unique okto-digital content.

```bash
# Add research to ingest/
cp ~/research/article.md ingest/
```

```
User: Transform ingest/article.md into an okto-digital blog post

Agent: [Reads article, then asks POINTED questions]
       Q1: Article recommends 2-week sprints. What does okto-digital use?
           Tell me about a recent project where sprint length mattered.
       Q2: They recommend CI/CD from day 1. Do you phase it in instead?

User: [Provides specific answers with real examples]

Agent: [Generates unique content using okto-digital specifics]
       [Saves to output/blog-title-2025-11-15.md]
```

The key: agent asks **specific, pointed questions** (never vague like "what makes you unique?") to extract real okto-digital details.

## Website Content Workflow

When generating website content, skills are consulted in sequence:

1. **UX Component Matcher** -- Select WHAT components to use
2. **Content Architect** -- Determine structure and length
3. **Content Formatter** -- Apply formatting within components
4. **SEO Metadata** -- Generate metadata package
5. **Conversion Optimizer** -- Add CTAs and optimize conversions

## Post-Generation Options

After every generation, the agent offers:
- **Length variants** -- shorter, longer, or multiple lengths
- **A/B variants** -- different hooks, emphasis, or tone
- **Channel adaptations** -- blog to social posts, service page to email
- **Format adaptations** -- article to slides, blog to video script

## Brand Voice Quick Reference

- **Core Attributes:** Reliable (40%), Genuine (35%), Curious (25%)
- **Archetype Mix:** Creator (50%), Everyman (30%), Sage (20%), Jester moments (15-20%)
- **Formality:** Casual baseline (adjusts by channel)
- **Readability:** 9th-10th grade (Flesch-Kincaid 60-70)
- **Prohibitions:** No buzzwords, no jargon, no ableist language

## Channel Tone Adjustment

| Channel | Formality | Fragments OK | Example |
|---|---|---|---|
| Website | Casual | No | "We start every project with discovery because it's the foundation for success." |
| Social Media | Very Casual | Yes | "Discovery phase? Game changer. Here's why." |
| Documentation | Moderate | No | "The discovery phase establishes project foundations through systematic research." |
| Crisis Comms | Moderate | No | "We identified the issue at 2pm and implemented a fix by 3:15pm." |

## File Management

**Auto-save:** Content >300 words saves to `output/` as `{type}-{slug}-{YYYY-MM-DD}.md`

**Quality checks before save:**
1. Boring Detector -- flags generic openings, corporate jargon, predictable structures
2. Dash Cleaner -- auto-corrects improper dash/em-dash usage (runs as hook on all .md writes)

**Feedback log:** Conflicts, violations, and success patterns auto-log to `voice-feedback.md`

## Tips for Best Results

1. **Provide context upfront** -- content type, channel, audience, goal = less back-and-forth
2. **Answer pointed questions specifically** -- "We use 1-week sprints for projects <3 months" beats "we're flexible"
3. **Use ingest/ for research** -- don't paste long articles in chat
4. **Request variants proactively** -- "also create LinkedIn and Twitter posts" while context is loaded
5. **Iterate on output** -- "make the hook stronger" or "simplify paragraph 4" refines without regenerating

## Troubleshooting

| Problem | Solution |
|---|---|
| Agent asks too many questions | Provide more context upfront, or prefix with "Quick:" |
| Content doesn't sound okto-digital | Use research transformation workflow with specific answers |
| Content too formal/casual | Specify channel clearly; agent auto-adjusts formality |
| Skills not loading | Run `/plugin list`, reinstall if missing, restart Claude Code |
| Auto-save not working | Check content is >300 words and `output/` directory exists |

## Version

1.0.0
