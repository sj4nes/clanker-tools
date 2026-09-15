# Changelog — role-deck

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. The full record is

    git log -- skills/role-deck/

## 2.1.0 — 2026-09-15

**MINOR.** Adds the laziness search as a sixteenth gate, `work-floor` — the
only gate that is not a safety property. Every other asks *does anything bad
happen on any path*; this asks *what is the least work a run can do while
breaking none of them*, which is the defect class that let `invent` v0.1.0 pass
everything and still be wrong. `coverage` is its n=1 case.

- `check_deck.py` always prints **min..max plays per card per complete run**;
  that line is the laziest run the deck permits. `minimum_work` (per deck, or
  per exit) turns an intention into an assertion, with a **laziest witness
  path** printed on failure.
- `played_at_least` now accepts a list, so one unlock can require work on
  several cards.
- Applying it found two more holes: `invent` could trial the **same**
  development twice (fixed: two each of develop, cull, try — `generate`'s range
  fell 1..6 → 1..4 as padding was squeezed out), and `decide` could **commit on
  a single round of evidence** (fixed: commit unlocks after two, while defer and
  drop stay reachable on one).
- Four new mutations, two of which strip the enforcing unlock and assert the
  floor then fails — because a floor *describes* and an unlock *enforces*, and
  a declaration nothing can break may be describing what the deck would have
  done anyway. 107 assertions.

## 2.0.0 — 2026-09-15

**MAJOR — the skill was wrong.** `run_deck.py verify` reported *"run completed
without wearing required roles"* on a **valid completed run** of any deck whose
`required_roles` is a map (per-exit) rather than a list. `set(a_dict)` yields
the keys — card ids — which were compared against role names. Latent since
`coverage` became per-terminal; invisible because `diagnose` is list-form and no
map-form deck had ever been played to a terminal until `invent` was. Anyone who
ran `decide` to completion under 1.0.0 got a spurious failure. Re-verify any
ledger that reported one. A completed map-form run is now in `runner-check.sh`.

Also in this version, all additive:

- a **resource `unlock`** primitive — the only way to say "you may not stop
  yet", keying on plays / spend / remaining budget / per-card counts and never
  on judgement. It costs no state-space growth, because all four are already
  functions of the counts vector.
- the **`invent` deck**, previously recorded as blocked on that primitive.
- `simulate.py` rewritten from **path enumeration to state-space DP**. Same
  numbers, reproduced to the digit on `diagnose`; `invent` has 22,302,788 paths
  over 1,182 states and did not previously return. Now 0.66 s.
- a new **`unlocks`** gate (15 total), four unlock mutations (26 total), and a
  completed map-form runner case (20 total). 100 assertions.

## 1.0.0 — 2026-09-15

First release, verified at release. Promoted from `experiments/role-deck/`,
where it was built over six commits with the checker written *before* the first
deck. Ships two decks (`diagnose`, `decide`), a static checker with 14 gates, a
runner with a replay-verified ledger, and an exact-enumeration simulator.
Verification: 22 planted deck defects, 19 runner refusal/tamper cases, two
die-driven property tests — 73 assertions. Fifteen findings, including three
where the test was broken rather than the thing under test, are recorded in
`references/findings.md` (`465bd44`, `af14526`, `4698ddd`, `914af76`,
`7c25d03`, `629d32a`, `95a8cb1`, `f9188dd`).
