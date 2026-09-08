# Editorial production: the five passes

Professional-quality books are made during revision. Use **separate passes** so
each read has one defined purpose. Do not spend days polishing a paragraph in a
chapter that a later pass may remove.

## Pass 1 — Developmental revision (author-owned)

Highest-level questions first:

- Is the book's central promise clear and consistently fulfilled?
- Does the structure build logically?
- Does every chapter have a distinct purpose?
- Are important reader questions answered in the right order?
- Does the book need more story, evidence, explanation, or practical
  application?
- Are there chapters to cut, combine, move, or expand?
- Does the conclusion synthesize rather than merely repeat?

Agent deliverables: the **chapter-function table** (each chapter's
`reader_can_now` and its job vs its neighbours), the **promise-vs-delivery map**
(every promise element → the chapter that delivers it; flag undelivered promises
and major content outside the promise), the **repetition report** (claims
restated without added evidence, nuance, or application).

## Pass 2 — Argument and evidence

Audit every meaningful assertion:

- What exactly is being claimed?
- What is the best source?
- Does the source support the precise wording?
- Is the evidence current enough?
- Is the claim too broad?
- What would a skeptical, informed reader say?
- Are limitations disclosed?
- Are quotations exact, attributed, and contextualized?

Run [`citation-check`](../../citation-check/SKILL.md) over flagged ledger rows.
For technical, historical, scientific, health, legal, or financial topics,
recruit a qualified **subject-matter expert** to review accuracy. An editor
improves expression; a domain expert checks substance — these are different
people doing different jobs.

## Pass 3 — Reader usability

Especially important for practical nonfiction.

- Are concepts introduced before they are used? (Check against the `tsort`
  order.)
- Are instructions actionable?
- Is every term defined in plain language, consistent with the style sheet?
- Are examples representative of real reader circumstances?
- Are tools, templates, checklists, figures, and summaries easy to find?
- Can a reader skim a chapter and still grasp its main value?

Use [`visualization-design`](../../visualization-design/SKILL.md) for any figure,
table, or diagram — first decide whether it earns its place (does it reduce
confusion the prose cannot?), then build it with graphical integrity and
accessibility. Sidebars, end-of-chapter summaries, checklists, sample scripts,
and worked examples are added only when they genuinely reduce confusion.

## Pass 4 — Line edit (author-owned voice)

Now improve sentences, paragraphs, rhythm, and voice:

- Cut throat-clearing openings.
- Replace abstractions with concrete nouns and active verbs.
- Break long, overloaded sentences.
- Remove redundant modifiers and repeated ideas.
- Vary sentence length intentionally.
- Ensure pronouns have clear referents.
- Keep terminology consistent (against the style sheet's `terms`).
- Make headings informative rather than clever-but-ambiguous.

Apply [`simple-technical-english`](../../simple-technical-english/SKILL.md)
**only to genuinely instructional passages** — checklists, procedures, step lists,
how-to sequences. Do **not** apply it to narrative or argument: controlled
English removes nuance that those modes need.

## Pass 5 — Copyedit and proofread

**Copyedit:** grammar, punctuation, spelling, consistency, citations,
capitalization, dates, terminology, cross-references, tables, formatting —
against the style sheet. Use [`ed`](../../ed/SKILL.md) for minimal, reviewable
line edits to structured front and back matter.

**Proofread:** the final inspection **after layout**. New errors appear when a
manuscript is typeset or converted to ebook formats — bad line breaks, dropped
words, broken cross-references, mis-numbered figures. This is a separate pass on
the typeset files, not the manuscript.

## Outside readers

Different feedback at different moments:

| Reviewer | Best time | Evaluates |
|---|---|---|
| Ideal readers | after a substantial draft | relevance, clarity, usefulness, interest, confusion |
| Subject-matter expert | during evidence revision (Pass 2) | accuracy, nuance, missing context, misleading claims |
| Developmental editor | after a complete draft | structure, premise, pacing, reader journey, chapter function |
| Line / copy editor | after developmental issues are resolved | style, clarity, consistency, grammar, citations |
| Proofreader | after final formatting | typos, page-level errors, headings, tables, captions, references |

### Beta-reader questions

Give focused questions, not "what did you think?":

- Where did you lose interest or become confused?
- What did you expect the book to cover but not find?
- Which claim felt least credible, and why?
- What did you underline, save, or want to apply?
- Which chapter could you skip without losing the book's value?
- What would you tell a friend this book is about?
- Did the book fulfill the promise you expected from its title and introduction?

**Feedback is data, not a vote.** If three readers stumble at the same point,
investigate the manuscript. If one reader dislikes the premise itself, do not
automatically rebuild the book around that preference.
