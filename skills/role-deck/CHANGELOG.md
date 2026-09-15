# Changelog — role-deck

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. The full record is

    git log -- skills/role-deck/

## 2.4.0 — 2026-09-15

**MINOR — the second behavioural justification is refuted, and struck.** The
ordering fixture ran: 8 fresh agents, a bug with a visible cause that fully
explains the symptom and a second cause invisible in the output. **8/8 found
both.** 4/8 went further and closed a third hole that was never planted. Scored
by executing each subject's own fix, against bands pre-registered before the
run.

Both of this skill's behavioural claims are now measured and false — agents do
not skip cheap grounding, and they do not stop at their first explanation.
`SKILL.md` now says so in a table rather than asserting anything about agent
thoroughness. What survives is auditability and repeatability, which the gates
prove and the StructOrder example run demonstrated.

## 2.3.0 — 2026-09-15

**MINOR.** Closes the plurality gap: `hypothesize` demanded "at least two
competing explanations" in prose and the runner accepted one. Artifacts may now
declare `min_items`; the runner enforces it; a new `min-items` gate (17 total)
checks the rule is well formed; `diagnose` 0.8.0 declares `candidates >= 2`.
Found by a design question, not a gate — deciding whether the ordering fixture
needed one arm or two required knowing whether the deck *enforced* the
discipline or merely asked for it.

Also adds `verification/ordering-fixture/` — built and pre-registered, **not
run**. Tests whether an agent, having formed a plausible explanation, asks
*"how do I confirm this?"* rather than *"what else would produce this
symptom?"*. Scored by executing the subject's own fix.

## 2.2.0 — 2026-09-15

**MINOR — the skill's stated REASON was wrong; none of its prescriptions were.**
Judgement call, recorded because it is one: every mechanism works as documented
and anyone following this skill built a working deck, so nothing needs redoing.
What changed is why you would adopt it, which means re-read before relying on
the rationale.

The founding premise — *"an agent left to choose its own sequence will skip the
expensive hat"* — was fixtured and **refuted**. Eight fresh agents were given a
harness whose true cause (`*** FAIL` as a regex → invalid repetition operator →
exit 2 → shell `if` reads false) is reachable only by executing it. **8/8 ran it
unprompted**, with no deck, no prompt to run, and no knowledge of what was being
measured. Scored by `score.py`, committed before any result was seen, against
bands pre-registered in `design.md`.

The claim is **struck**, not rewritten into a similar-sounding untested one —
that substitution is the move `evaluator-integrity` exists to catch. `SKILL.md`
and the `description` now say the draw buys **auditability and repeatability**,
which is what the structural gates actually prove.

Bycatch: subjects who ran both greps found `docs/verifying-skills.md` attributes
`repetition-operator operand invalid` to ugrep. That is BSD grep's message;
ugrep says `error at position 4 … empty (sub)expression`. Both exit 2, so every
conclusion held — the attribution did not. Corrected.

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
