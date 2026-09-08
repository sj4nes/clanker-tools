# Verifying the nonfiction-book skill

`sh run.sh` (needs `python3` stdlib-only, `tsort`, `sh`; ~1 s).

## What it does

The skill is a methodology skill, so it is verified by **exercising the
prescribed workflow on a tractable case with a knowable pass/fail** — the same
approach as `design-of-experiments` and `simulation`.

The case is a worked ~3-chapter mini-book, **"When Did This Line Change?"**, a
prescriptive guide to reading git history. It is carried through the first four
phases:

| File | Phase | Artifact |
|---|---|---|
| `mini-book/positioning-brief.json` | 1 Positioning | the 10-field brief |
| `mini-book/claim-ledger.json` | 2 Research | 6 claims: fact / interpretation / recommendation rows, tiers, citation-check status |
| `mini-book/fat-outline.json` | 3 Architecture | governing structure, a concept dependency graph, 3 chapter briefs |
| `mini-book/chapter-2-draft.md` | 4 Drafting | one drafted chapter, marked draft, citing ledger rows |

Fixtures are JSON so `check.py` runs on the standard library alone. The shipped
`templates/` use YAML with the same field names.

## The four checks

1. **Good artifacts pass every gate.** `check.py` validates the brief, ledger,
   and outline against the phase-gate checklists in the SKILL and exits 0 with
   no errors.
2. **The concept graph linearises under the real `tsort(1)`**, not only the
   in-script Kahn implementation.
3. **13 planted defects are each caught** — one at a time, the harness mutates a
   copy of the good artifacts and asserts `check.py` emits the specific error
   code and exits 1:

   | Defect | Code |
   |---|---|
   | topic-led promise ("everyone interested in git") | `reader-not-concrete` |
   | `will_not_cover` emptied | `no-exclusions` |
   | fewer than 3 comparable titles | `too-few-comps` |
   | an unanswered blocking question | `open-blocking-questions` |
   | a high-confidence claim resting on a discovery source | `discovery-load-bearing` |
   | a high-confidence cited claim never citation-checked | `citation-unverified` |
   | a `blocking` claim entering drafting | `claim-blocking` |
   | a chapter outcome of "know more about X" | `reader-can-now-vague` |
   | a chapter with no distinct job | `chapter-not-distinct` |
   | a missing through-line transition | `no-through-line` |
   | a cycle added to the concept graph | `concept-cycle` |
   | a chapter citing a non-existent ledger row | `dangling-evidence` |
   | two neighbouring chapters making the same claim | `chapter-repeats-neighbour` |

4. **The drafted chapter follows the practical-chapter pattern** (hook → problem
   → principle → evidence → example → method → pitfalls → reader action →
   transition) and cites only claim-ledger rows that exist.

## What this does and does not show

It shows the phase gates are mechanically enforceable and that the prescribed
artifacts, filled properly, pass them — and that the common failure modes the
SKILL names are detectable. It does **not** show that a book built this way is
good; developmental judgement, voice, and evidence adjudication stay human. The
`check.py` gates are necessary conditions, not sufficient ones.
