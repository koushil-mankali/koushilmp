# Style guide

Every file the skill generates follows these conventions so the whole knowledge base reads as one consistent book.

## Voice
- Second person, conversational, confident: "You can build X in an afternoon. That works fine - until it doesn't."
- Explain *why* before *how*. Open with a concrete analogy, then name the concept.
- Speak to the reader's existing knowledge ("As a developer you already understand ...; what you're about to learn is why ...").
- Short paragraphs (1-4 sentences). Bold the key phrase in a sentence, not whole sentences.
- Be candid about trade-offs; end ideas with a decision rule ("Is it worse to give users wrong data or an error?").
- No hype, no filler, no emoji.

## Formatting
- `#` title once; `##` major sections separated by `---`; `###` for sub-concepts.
- Header block under the title, as blockquote lines: `> **Estimated Time:** 1 hour | **Difficulty:** Intermediate` and `> **Prerequisites:** [NN - Topic](../NN-slug/README.md), ...`.
- Use tables for comparisons, catalogues, and decision matrices (e.g. `| Tool | Type | Why |`). Prefer a table over a long bullet list of parallel facts.
- Numbered lists for sequences, bullets for sets, `**"Quoted wrong belief"**` + correction for misconceptions.
- Code blocks always carry a language tag and a short leading comment saying what the snippet demonstrates; follow with 2-4 bullets explaining what it shows.
- Diagram placement: a ```mermaid block immediately followed by its rendered `![Diagram N](./images/diagram-N.svg)`; N restarts at 1 in every chapter.
- Chapters end with `---` then one nav line: `[← Previous: X](../NN-x/README.md) | [Next: Y →](../NN-y/README.md) | [Back to <Section> Index](../README.md)`.
- Folder/file names: zero-padded number + kebab-case slug (`05-cap-theorem`). Section folders likewise (`02-backend`). Always `README.md` inside.

## Section README pattern
1. `# <Section Title>` and a one-sentence blockquote stating who it is for and the promise.
2. `## Why <Section> Matters` - 2-4 paragraphs of motivation, ending with what the reader will be able to do.
3. `## All N Topics` - table `| # | Topic | Description | Time | Difficulty |` with linked titles.
4. `## How to Use This Section` - numbered study method (read, draw diagrams from memory, explain aloud, find it in the wild, practise interview answers).
5. `## Prerequisites` - "You should be comfortable with" list and "You do NOT need to know" list.
6. Final line: `[Start with Topic 1 →](./01-slug/README.md)`.

## Root README pattern
`# <Topic> Knowledge Base` + blockquote tagline -> `## How to Use This Guide` (numbered; include what each topic contains) -> `## Table of Contents` (one `###` per section with link, `(~N hrs)`, one-line description, and `> **N topics** | focus note`) -> `## Summary` table (Section | Topics | Est. Time, with a bold Total row) -> `## Complete Topic List` (numbered list per section).

## Case-study / project chapters
For end-to-end builds, replace the concept layout with: 1 Problem Statement & Requirements, 2 Back-of-the-Envelope Estimation, 3 Interface/API Design, 4 Data Model, 5 High-Level Architecture (diagram), 6 Deep Dive into Core Components, 7 Scaling, 8 Edge Cases & Failures, 9 Monitoring & Alerting, 10 Technology Choices, 11 Interview Tips, then Key Takeaways and Learning Resources. Adapt the headings if "estimation" or "interface" do not apply to the topic.

## Cheatsheet palette
Pair a dark accent with a light tint per section (card fill = tint, card border and number tab = accent; text `#0f172a` title, `#1e293b` summary; page `#f8fafc`; header band = accent):

| Section colour | accent | tint |
|---|---|---|
| blue | `#1e3a8a` | `#dbeafe` |
| orange | `#7c2d12` | `#fed7aa` |
| green | `#14532d` | `#bbf7d0` |
| purple | `#581c87` | `#e9d5ff` |
| sky | `#0c4a6e` | `#bae6fd` |
| red | `#7f1d1d` | `#fecaca` |
| yellow | `#713f12` | `#fef08a` |
| indigo | `#312e81` | `#c7d2fe` |
