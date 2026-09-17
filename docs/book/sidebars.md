# Sidebars — what the standard caught while the book was being built

A running record of moments where **the method this book describes, applied to
the book's own construction, caught something that reading had not.** Each is a
candidate for a `#sidebar[...]` in a chapter; some are cut in, most are not yet.

Why keep it. The book argues that a check you have not seen fail is not a check,
and that the valuable result is the one that disagrees with you. Building the
book produced a stream of exactly those, against the author. They are the
cheapest evidence the book has — no fixture to run, no agent to spawn, it simply
happened — and they were previously recorded only in commit messages, which is
where this corpus keeps things it later cannot find.

**The bar for an entry.** A tool or practice from the corpus reported something
false or missing that a careful person had already read past. Not "a check
passed". Not "I noticed a typo". The check has to have been the one that caught
it.

Two directions, both counted:

- **inward** — a corpus practice caught a defect in the book's own toolchain.
- **outward** — writing the book caught a defect in the corpus.

| # | date | direction | the practice | what it caught | commit | in the book |
|---|---|---|---|---|---|---|
| 1 | 09-14→17 | outward | the claim ledger | the corpus's one external citation had drifted from its source, in four places | `a92cc8f` | I.2, II.3 |
| 2 | 09-17 | outward | drafting II.6 against its skill | `directed-verification`'s self-correction count held two false positives, one of them the skill's own release commit | `8097530` | II.6 |
| 3 | 09-17 | outward | drafting II.7 against its skill | two stale statements in `skill-authoring`; its proposed harness-first check is silent for 17 of 21 skills | `b3ad6e6` | II.7 |
| 4 | 09-17 | outward | a book tool promoted to a corpus gate | the changelog §3b contract had decayed where nothing checked it — six entries fixed | `b08e99e` | — |
| 5 | 09-17 | outward | generating Part V | 14 OPEN backlog items were filed under `## Done`, including every `claim-fixture` item | `da03635` | V (candidate) |
| 6 | 09-17 | inward | the mutation test | `typstlib`'s self-test passed 10/10 with `*` removed from the escape set — every star in the suite sat inside a matched pair | `da03635` | II.2 (**cut in**) |
| 7 | 09-17 | inward | the mutation test | a changelog entry styled `**MAJOR.** **Headline.**` was leaking literal `\*\*` into Part IV; the page read plausibly either way | `da03635` | II.3 (candidate) |
| 8 | 09-17 | inward | the no-mutation control | the fixture copied `docs/book` but not `docs/`, so 13 mutations "passed" for the wrong reason | `845ea24` | II.2 (**cut in**) |
| 9 | 09-17 | inward | the no-mutation control | `gen-facts.py` shelled out to `git` unconditionally and could not run outside a checkout — where the harness runs it | `c503a9c` | II.2 (**cut in**) |
| 10 | 09-17 | inward | reading the PDF, not the exit code | Markdown links printed raw; a tutorial's install instructions printed as what it teaches | `cb4c2aa`, `845ea24` | III intro (candidate) |
| 11 | 09-17 | inward | the drift check (`nonfiction-book` Pass 1) | two of its own findings were wrong and were withdrawn on checking — the audit's own negative result | `1bb3797` | V (candidate) |

## The one that keeps recurring

Entries 8 and 9 are the same defect twice, a day apart, and neither was in the
subject under test. Both were in the **fixture**, and in both cases every
mutation would have reported "caught" while proving nothing. Only the
no-mutation control — the case that asserts an *unmutated* copy still passes —
distinguished a gate that works from a fixture that is broken.

That is `test-writing` behaviour 6 (*run your new check against code you believe
is correct*) landing on the book's own harness, and it is the strongest single
piece of evidence in this file, because the control was added as an afterthought
and has since earned its place twice.

## Entries 2 and 3 are the uncomfortable ones

Both are the book finding its own supporting skill weaker than claimed, in the
chapter written to showcase it. Neither was found by running the skill's
harness; both were found by *writing the chapter* — i.e. by having to state the
claim precisely enough for a reader.

That is a real and slightly awkward finding about the corpus: **drafting prose
for an outside reader is a verification technique**, and it is not one the
standard names. It belongs in the backlog as a candidate behaviour, not merely
in a sidebar.

## Rules for cutting one into a chapter

- A sidebar is not a practice. A practice is what the reader should do; a
  sidebar is what happened when the author did it. Do not let a sidebar end with
  advice — the advice already has a chapter.
- One per chapter at most. They are asides; a chapter that needs two is a
  chapter whose argument is missing something.
- It must survive the rewrite pass in the author's voice. These are currently
  written in the drafting agent's, like the chapters around them.
- Keep the failure, not the fix. The interesting half is that a careful reader
  had already been past it.
