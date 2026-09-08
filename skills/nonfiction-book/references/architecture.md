# Book architecture

Readers experience nonfiction as a sequence of answers, discoveries, or
capabilities — not a warehouse of information. Design the sequence.

## The fat outline

An effective chapter outline contains far more than titles. For each chapter,
specify:

- The reader's question entering the chapter.
- The chapter's central claim or skill.
- Why that claim matters now.
- Key evidence and sources (claim-ledger row ids).
- A story, case study, scene, or running example — a specific person or decision,
  not a generic example.
- The framework, process, or explanation.
- The likely objection or misconception, and its answer.
- The practical takeaway.
- What the reader understands or can do by the end.

A useful chapter is usually built from five ingredients: **ideas / frameworks,
stories or case studies, reasoning, proof points (data and citations), and
actionable guidance.** Planning these before drafting stops chapters becoming
either dry information dumps or unsupported anecdotes.

## Every chapter earns its place

For every chapter, complete:

> After reading this chapter, the reader will understand or be able to ______.

If the answer is vague — "know more about the topic" — the chapter lacks a
function. Give it one or cut it.

Each chapter must have a **distinct job**. Chapters that restate a point in
slightly different language should be merged. A clean structure usually follows
one pattern:

| Structure | Best for | Progression |
|---|---|---|
| Problem → solution | practical books | diagnose → principles → method → implementation |
| Beginner → advanced | skill-building | foundations → practice → edge cases → mastery |
| Past → present → future | history and ideas | origins → turning points → current implications |
| Myth → evidence → action | corrective books | common belief → what evidence shows → what to do |
| Case study → principle | business and applied | story → lesson → tool → next case |
| Journey / chronology | narrative nonfiction | inciting event → escalation → resolution → meaning |

Pick the governing pattern deliberately and flag chapters that fight it.

## Ordering concepts with tsort

A nonfiction book is a dependency-ordered sequence of concepts, exactly like a
formula tree or a theorem tree. Use [`tsort`](../../tsort/SKILL.md):

1. List each concept / term the book defines and each chapter that first uses it.
2. Write one edge `A B` for every "A must be understood before B".
3. `tsort` the edges. A cycle means two concepts each depend on the other —
   resolve by splitting one, introducing a minimal early version, or merging.
4. The linear order is the constraint the chapter sequence must not violate: no
   term used before the chapter that introduces it.

## The through-line

A reader should always know why the next chapter follows this one. At the end of
each chapter, write a transition sentence that creates forward motion:

> Understanding the diagnosis is necessary, but it does not tell you how to
> choose among competing remedies; the next chapter provides that decision rule.

Small practice, large effect on cohesion.
