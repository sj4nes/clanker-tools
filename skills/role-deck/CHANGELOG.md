# Changelog — role-deck

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. The full record is

    git log -- skills/role-deck/

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
