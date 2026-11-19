# Chapter template

Voice and formatting rules are in `style-guide.md`. Sections marked (+) add depth beyond a basic overview. For end-to-end case-study chapters use the case-study layout in the style guide instead. Use `---` between major sections.

```markdown
# <Topic Title>

> **Estimated Time:** <30 min - 2 hr> | **Difficulty:** <Beginner|Intermediate|Advanced>
> **Prerequisites:** [NN - Topic](../NN-slug/README.md), ...   (or "None")

---

## What You'll Learn (+)
3-5 verifiable outcomes: "By the end you can ... ".

## Introduction
A concrete analogy from everyday life (e.g. a database consistency chapter might use two bank branches sharing accounts), then 1-2 sentences naming the concept.

## The Problem It Solves
What breaks without it. Bullet the mistakes people make when they don't understand it.

## Core Concepts
One `###` per concept. Definition -> why it matters -> small example. Mermaid diagram + rendered image where a picture beats prose.

## How It Works (Step by Step)
Numbered walk-through of the internals (request lifecycle, algorithm, protocol exchange). Sequence/flow diagram.

## Hands-On Example
Runnable code in the user's chosen stack with expected output. Explain each non-obvious line. Mark pseudocode as pseudocode.

## Real-World Examples / In Practice
A table of named tools, products, or configurations (`| Name | Category | Why |`) followed by a bold **Important nuance** paragraph, then a "Practical meaning for <audience> developers" subsection with code and 2-4 explanatory bullets.

## Trade-offs and When NOT to Use It (+)
Costs, limits, alternatives, decision table.

## Failure Modes and Debugging (+)
What goes wrong in production, symptoms, how to diagnose, how to fix.

## Common Misconceptions
`**"Quoted wrong belief"**` followed by the correction.

## Choosing <A> vs <B> for Your Situation
Numbered questions, each with 2 bullets mapping an answer to a choice. Include only when the topic involves a real decision.

## Interview Tips
What interviewers ask, the nuance that separates good answers, a sample answer structure.

## Exercises (+)
3-5 practice problems, easy -> hard, with collapsed answers (`<details><summary>Answer</summary>`).

## Key Takeaways
5-8 bullets, bold the key phrase in each.

## Learning Resources
### YouTube (Search Terms)  /  ### Books & Courses  /  ### Articles
Prefer search terms and titles over URLs unless the URL is verified.

---

[← Previous: X](../NN-x/README.md) | [Next: Y →](../NN-y/README.md) | [Back to <Section> Index](../README.md)
```

Length: 250-450 lines. Keep the first and last topic of a section's prev/next footer pointing sensibly (first has no Previous; last points to the next section's index).
