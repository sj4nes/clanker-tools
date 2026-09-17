# Drift check — the built book against the plan

**Date:** 2026-09-17, at `845ea24` (93 pages, six parts).
**Method:** the `nonfiction-book` skill's Pass 1 (developmental) — the
chapter-function table, the promise-vs-delivery map, and the repetition report —
run against the planning artifacts rather than against taste.

**Compared:** [`positioning-brief.md`](positioning-brief.md) (the constitution),
[`outline/fat-outline.md`](outline/fat-outline.md),
[`outline/GAPS.md`](outline/GAPS.md), [`claim-ledger.md`](claim-ledger.md) and
[`comps-table.md`](comps-table.md), against `book.typ` and `parts/`.

Run because six parts now exist and the last three were built in one day, two of
them from a conversation rather than from the outline. The brief says that when
it and a draft disagree the disagreement is *surfaced, not quietly resolved*;
nothing had checked that since Part III.

| | |
|---|---|
| Parts I–III vs the outline | **no drift** — chapter for chapter, titles near-verbatim |
| The four promised outcomes | **all four delivered**, one chapter each |
| The two drafting warnings | **both honored** |
| Mode-mixing mitigation | **met by a different mechanism than planned** — ratify or revert |
| Findings raised | **5** — 1, 2, 3 and 5 resolved 2026-09-17; **4** resolved by the corpus-count registry |
| Findings withdrawn on checking | **2** |

---

## What holds

**Parts I–III match the outline chapter for chapter.** Nine authored chapters,
titles near-verbatim from the fat outline, in the planned order. The dependency
rule the outline set (`tools/check-intro-order.py`, no term used before it is
introduced) still passes over the drafts.

**The four promised outcomes are each delivered by a chapter.** The brief's
`what_outcome` names four things the reader can do afterwards:

| promised outcome | delivered in |
|---|---|
| name the default behaviour a skill displaces | II.1 — Name the default you displace |
| build a harness that has been SEEN to fail | II.2 — Build a harness that can fail |
| measure whether that default is real | II.4 — Measure the premise before you build on it |
| direct an agent to do that work, including disproving you | II.6 — Work with the agent, not at it |

**Both explicit drafting warnings were honored.** These are the two places the
plan left a trap for the drafter, and both held:

- The brief required the unread-comps limitation to travel with any claim about
  the shelf. `parts/01-pile/01-asset.typ` carries it in the footnote, phrased as
  a characterisation of the genre — *"This characterises how the genre presents
  itself, not what any one book contains"* — not an assertion about titles.
- The outline's ⚠ on II.3 said Kreinin's remark must not appear as an observed
  default, and proposed using it openly as the corpus's own unmeasured premise.
  `parts/02-standard/03-oracle.typ` takes exactly that move: *"That default has
  never been measured… The claim that it displaces something agents actually do
  is, for now, a premise."* The ledger's single `blocking` row (C-I-17) is
  blocking only *"for any sentence stating it as observed"*, and no sentence does.

**The GAPS.md gaps are reflected honestly.** Both built gaps are drafted (II.7
from `skill-authoring`, II.6 from `directed-verification`, the latter still
reported weak by its own table), and the unbuilt third, `source-authority`,
appears in II.3 as an open problem rather than being quietly dropped.

---

## Drift, worst first

### 1. Part VI sits outside the constitution — RESOLVED 2026-09-17

The brief's `will_not_cover` list excludes **"The domain content of the corpus's
knowledge capsules."** Part VI's 24 generated entries are that content: what
each tutorial teaches is electrolysis, buffer pH, Bolzano–Weierstrass. The
reader those entries serve — someone who wants to learn chemistry — is not the
brief's reader, who is auditing a corpus of agent skills.

The part's **argument** is in scope and is some of the book's strongest
material: a check that can fail and a lesson that teaches are the same event, so
the tutorials were cut *from* the harnesses rather than written beside them.
That belongs to the standard. The catalogue wrapped around it does not.

It also pushes the book further toward reference mode, which the brief lists as a
secondary mode and whose over-use it already flags as the mode-mixing risk.

This was added from a conversation without checking the brief — the quiet
resolution the brief forbids — so it is recorded here rather than defended.

**Resolved: the brief was amended** (option 1), recorded under "Amendments" in
[`positioning-brief.md`](positioning-brief.md) with the reasoning and the cost.
A `secondary_promise` now covers reuse of verified material, and the exclusion
narrowed from the capsules' *content* to *developing* that content. Part VI is
unchanged. The appendix option stays available if a developmental pass finds the
close weakened.

The options as they stood:

+ **Amend the brief** — add a second promise clause about reuse of verified
  material, and narrow the exclusion to *undeveloped* capsule content.
  Recommended: the reuse argument is real value, but the constitution should
  change deliberately rather than be outvoted by a part that already exists.
+ **Keep the framing chapter, demote the catalogue** to an appendix, leaving
  Part V as the book's close.
+ **Record an explicit exception**, as the brief already does for reader
  interviews.

### 2. The running example stops at Part II — RESOLVED 2026-09-17

The outline specified one real skill *"followed through the whole book"*, with
`test-writing` as the candidate. Counted across the authored chapters:

| Part | mentions of `test-writing` |
|---|---|
| I (2 chapters) | 3 |
| II (7 chapters) | 13 |
| **III, IV, V, VI (authored chapters)** | **0** |

Part III audits capsules, so its absence there is natural; Parts IV–VI never
return to it. The through-line the outline promised is not kept.

**Resolved 2026-09-17** in `04-catalogue/00-howtoread.typ`, which was the better
of the two homes: that chapter tells the reader to find the entry nearest their
own skill, and the running example has an entry. The new section reads
`test-writing`'s entry through the four fields and lands on the uncomfortable
result — its *displaces* field reports that the counts are stated in prose
rather than reported, in the skill the standard names as the worked example of
that very rule. Written without restating any count, so it cannot rot.

### 3. Parts IV–VI have no claim-ledger rows — FIXED 2026-09-17

The ledger runs `C-I` (19 rows), `C-II` (62), `C-III` (22), and stops. The
**generated** chapters do not need rows — every number in them is read from the
repository at build time and gated, which is stronger than a ledger row. The
three **authored** framing chapters do, and have none:

- `04-catalogue/00-howtoread.typ` — "a high gap count is a better sign than a
  zero one" is an interpretation.
- `05-open/00-intro.typ` — the three things "a book would normally leave out".
- `06-tutorials/00-intro.typ` — "a check that can fail and a lesson that teaches
  are the same event" is the part's central interpretive claim, unledgered.

**Backfilled 2026-09-17**: 14 rows, `C-IV-01..04`, `C-V-01..03`, `C-VI-01..03`,
`C-P-01..04` (the preface, which postdates this check). The generated chapters
still have none and need none.

The backfill earned itself immediately. V.0 claimed "roughly half the open
backlog items were opened by the audits of Part III" — **written without a
count**. A keyword proxy matches 29 of 46, but the matcher also hits capsule
items unrelated to those audits, so it overcounts by an unknown amount. The
prose now says "many"; `C-V-03` records the fraction as `low` confidence with
the real fix (hand-classify the items by origin) named. Two more rows came out
marked as untested theses rather than findings: `C-IV-02` (a high gap count is
the better sign) and `C-VI-02` (Part VI's central claim).

### 4. The corpus counts have rotted, exactly as the ledger predicted

Ledger row C-I-08 already carries `caveats: "ROTS"` and names the fix: *"the
eventual fix is to generate it, as Parts IV and V are."*

| stated | where | actual at `845ea24` |
|---|---|---|
| "Fifty skills nobody can evaluate is worse than five" | `01-pile/01-asset.typ` | **53** |
| "50 skills, 161 commits, ten days" | `outline/fat-outline.md` | **53 skills, 210 commits, 12 days** (2026-09-05 → 09-17) |
| "the standard governing 50 skills" | `outline/GAPS.md` | **53** |

**Fixed 2026-09-17** by `corpus-facts.typ`, a registry of named constants
generated by `tools/gen-facts.py` and gated by `check-book.sh`. Three of the four
sites now read from it (`#n-skills`, `#corpus-asof`, `#n-commits`); the fourth is
the rhetorical "Fifty", which is a voice decision and keeps its REWRITE-PASS
marker. Ledger row C-I-08's `draft-anyway` can be retired.

Building it surfaced a trap worth recording: the commit count and corpus age
move with **every commit**, so diff-gating them would fail `check-book.sh` after
each one — a gate that cries wolf is a gate somebody switches off, which is this
book's own subject. Those values are therefore *stamped*, not gated: carried
forward untouched until someone runs `gen-facts.py --stamp`. The mutation suite
asserts both halves, including that a stale stamp leaves the gate green.

### 5. Two stale planning artifacts — ledger header FIXED 2026-09-17

- `claim-ledger.md`'s header says *"Rows so far: **Part I only**… Part III was
  drafted before this ledger existed and has no rows yet"*. Both false: 84 rows
  existed beyond Part I, including 22 for Part III. **Rewritten 2026-09-17** to
  state what the ledger actually covers, and why the generated chapters are
  exempt.
- `outline/fat-outline.md` is titled *"Fat outline — Parts I, II, IV, V"* and
  describes a five-part book.

---

## Findings raised and withdrawn

Recorded because a check that never comes back negative is the defect this book
is about, and because both of these would have been wrong in the report.

**"Part III abandoned the practice mitigation."** The brief's stated mitigation
for the mode-mixing risk was that *every audit chapter must land on a practice*.
A first pass counted `#practice[` blocks and found one across five chapters.
That count was misleading: four of the five chapters close by **cross-referencing
the Part II practice** that addresses the finding — `@pr-harness` in the `bc`
chapter, `@pr-oracle` in the graph chapter, `@pr-premise` in the premises
chapter — and the Lean chapter, whose finding has no Part II practice,
introduces a new one. The synthesis then names the set as four questions.

So the mitigation is met by reference rather than by repetition, which avoids
duplicating a practice per part. **It is still a deviation from the written
mitigation and should be ratified in the brief or reverted.**

**"A blocking ledger row reached the draft."** The ledger's gate is that every
drafting-blocking claim is `high` or explicitly `draft-anyway`, and one row
(C-I-17) is `blocking` at `low` confidence. Reading the row, it is blocking
*conditionally* — `# for any sentence stating it as observed` — and the draft
states the opposite. No violation.

---

## What this check does not cover

- **Prose quality.** This is Pass 1 only. Passes 2–5 (argument & evidence,
  reader usability, line, copyedit) have not been run over Parts IV–VI.
- **Parts I and II are still agent drafts** awaiting the author's rewrite; drift
  found here is drift against the plan, not against the author's voice.
- **No outside reader has seen any of it.** The brief's accepted exception on
  reader interviews still stands, and the acceptance checklist in the
  `nonfiction-book` skill has not been run.
