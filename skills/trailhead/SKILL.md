---
name: trailhead
description: Generates a complete, beginner-to-expert learning knowledge base on any technology, tool, framework, language, or concept (e.g. Kubernetes, Kafka, Rust, OAuth, GraphQL, Terraform) in the style of the user's systemdesign repo. Produces a root README with roadmap and time estimates, numbered sections each with its own README index, one folder per topic containing an in-depth chapter README (intro, problem it solves, core concepts, step-by-step internals, code examples, misconceptions, interview tips, takeaways, resources) with Mermaid diagrams rendered to images/diagram-N.svg, plus a one-page SVG cheatsheet per section. Use whenever the user asks for in-depth documentation, a handbook, a study guide, a "zero to expert" roadmap, a learning path, a tutorial series, or a knowledge base on a topic, or says "document X like systemdesign" or "trailhead" - even if they never name the format.
---

# Trailhead

Build a learning knowledge base that takes a reader from zero to expert on one topic. It mirrors the layout of the user's `systemdesign` repo, which they already like, with extra depth added per chapter.

The reader should finish each chapter able to explain *why* the thing exists, not just *what* it is. Everything below serves that.

## Step 0 - Clarify first (the user's global rule)

Before writing anything, ask (AskUserQuestion, 1-4 questions) about what you can't infer: topic and boundaries, audience background (the systemdesign docs assume JavaScript/Node developers - confirm the language/stack for examples), target depth/size (compact ~10 topics vs full 30+), and output location (default: `./<topic-slug>/` in the current directory). Skip questions the request already answers. Then restate the plan in 1-3 sentences.

## Step 1 - Design the roadmap

Research the topic (WebSearch / context7 for current docs when versions or APIs matter - never write version-specific facts from memory). Then split it into numbered **sections** following a difficulty arc, and list topics inside each:

- `00-fundamentals` - vocabulary and mental models; nothing assumed
- `01-core` - the everyday working knowledge (what most people need)
- `02-intermediate` - real-world usage, integration, configuration, patterns
- `03-advanced` - internals, performance, scale, failure modes, security
- `04-expert` - architecture trade-offs, operating in production, edge cases, source-level behaviour
- `05-case-studies` / `projects` - realistic end-to-end builds that combine sections (omit if the topic has none)

Rename sections to fit the topic (a language needs "tooling" and "ecosystem"; a protocol needs "wire format"). Keep a strict dependency order: every topic's prerequisites must appear earlier. Tag each topic with Beginner / Intermediate / Advanced and a time estimate (30 min - 2 hr).

Show the user the section/topic outline and get a go-ahead before generating all chapters; it is cheap to fix now and costly after 30 chapters.

## Step 2 - Scaffold

```
<topic>/
├── README.md                      # root: purpose, how to use, TOC with hours, summary table, full topic list
├── cheatsheet-NN-<section>.svg    # one per section
├── NN-<section>/
│   ├── README.md                  # section index: why it matters, topic table (#, topic, description, time, difficulty), how to use, prerequisites
│   └── NN-<topic-slug>/
│       ├── README.md              # the chapter
│       └── images/diagram-N.svg
└── glossary.md                    # (improvement) every term, one line each, linking to the chapter that teaches it
```

Root and section READMEs follow the patterns in the user's `~/AI/systemdesign/README.md` and `00-fundamentals/README.md`; read one of them if you need the exact feel. Counts and hour totals in the root README must be computed from the real topic list, not guessed.

## Step 3 - Write each chapter

Follow `references/chapter-template.md` exactly for section order and the improvements over the original format (learning objectives, hands-on lab, exercises with answers, "when NOT to use it", failure modes, further reading). Chapters are independent, so for 5+ topics fan them out to parallel subagents, giving each the template path, its topic, prerequisites, neighbours for prev/next links, and the audience/stack. Do not let agents invent links: every relative link must point at a file that exists.

Depth rules that make the docs genuinely in-depth:
- Open with an analogy, then the concrete problem the thing solves. Explain *why* before *how*.
- Show internals step by step (what happens on the wire / in memory / in the scheduler), not only usage.
- Examples must be runnable or clearly marked pseudocode, in the stack the user chose. Verify code you can actually run (run it, or check against current docs).
- Include numbers (limits, latencies, defaults) only when sourced; otherwise say "varies".
- Be honest about trade-offs and misconceptions; a chapter with no downsides is marketing.

## Step 4 - Diagrams

Write diagrams as ```mermaid blocks (3-5 per chapter: architecture, step-by-step flow/sequence, comparison, state/decision). Then render and link them all:

```bash
python3 ~/.claude/skills/trailhead/scripts/render_diagrams.py <chapter>/README.md
```

This writes `images/diagram-N.svg` and inserts `![Diagram N](./images/diagram-N.svg)` after each block (idempotent; needs Node/npx; `--no-render` only fixes the markdown). The Mermaid source stays in the README so diagrams remain editable and still render on GitHub. If rendering fails, fix the Mermaid syntax and rerun; never ship a broken image link.

Cheatsheets: one hand-built SVG per section (1480px wide, dark header band with title and "N concepts - folder: ...", a grid of rounded cards, each with a numbered colour tab, topic title, and a one-line summary), matching the `cheatsheet-*.svg` files in systemdesign. Use a different accent colour per section.

## Step 5 - Verify before reporting done

The user's global rule: after changes, check for bugs and confirm the work does what it should. Concretely:
1. Every relative link in every README resolves to an existing file (script it: regex `\]\((\.[^)]+)\)`, check the path).
2. Every `images/diagram-N.svg` referenced exists and is non-empty; every Mermaid block has a following image.
3. Topic counts and hour totals in the root/section READMEs match the actual folders.
4. Prev/next footer links form an unbroken chain within each section.
5. Spot-check 2-3 chapters for factual accuracy against current official docs.

Report what was generated (sections, topic count, estimated reading time) and anything skipped or unverified. Do not claim completeness you did not check.

## Quality bar

If a chapter could be replaced by the first page of the official docs, it is not in-depth enough. Add internals, failure modes, trade-offs, and a lab. If it is padded with filler that does not teach, cut it.
