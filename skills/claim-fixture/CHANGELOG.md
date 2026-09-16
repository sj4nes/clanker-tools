# Changelog — claim-fixture

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/claim-fixture/

## 2.0.0 — 2026-09-15

**MAJOR: the method was missing a step, and a run was lost to it.** Any fixture
designed under 1.0.0 needs re-checking against the new gate before its result is
believed.

`directed-verification` b1 run 2 was invalid because its **control arm received
the treatment** — `test-writing` was in every arm-A subject's context, and it
prescribes the discipline under test. 1.0.0 had nothing to say about this:
behaviour 2 demands subjects naive about the *hypothesis*, which they were, and
that is not the same as clean of the *intervention*.

Worse, the design's pre-registered ceiling rule fired first and returned a
respectable "no headroom", which concealed the cause. Pre-registering how to read
a null result is not the same as checking the experiment ran.

- **New behaviour 3 — prove the control did not already receive the treatment,
  before reading any outcome.** Fingerprint list, manipulation check, and the
  ordering rule that a contamination failure *voids* the run rather than
  annotating it. Old behaviours 3–6 renumber to 4–7.
- **New `references/pre-flight.md`** — a rubric of 7 gates, each derived from a
  named failure in this corpus's four runs (2 refuted, 2 invalid). Nothing in it
  is invented.
- **New `verification/preflight.sh`** — scores a fixture design before subjects
  are spawned, and **blocks on any gate it cannot evaluate**, because a missing
  manipulation check reading as compliance is how run 2 got through.
- **New `verification/preflight-check.sh`** — clears a compliant fixture, breaks
  one gate at a time and asserts the *specific* gate fires, and confirms the gate
  blocks the real b1 fixture on the gate that caused its failure.

Also now stated plainly: this method has produced **zero positive results** in
four runs, so its sensitivity is untested and its refutations are weaker than
they look. G4 demands a positive control of every fixture; the method still owes
one of itself. `preflight-check.sh` is the first instance of that discipline
applied reflexively — the gate is shown to pass, not only to fail.

## 1.0.0 — 2026-09-15

First release. Extracted from two experiments run against `role-deck` on the
same day, both of which **refuted the claim they were built to support** (8/8
each). The method is the transferable part: split structural from behavioural,
naive subjects, unforgeable measurement, pre-registration in a separate commit,
a fixture where the shortcut passes its own confirmation, and striking rather
than rewording a refuted claim. Verification checks the one mechanically
provable part — pre-registration order — and **fails on one of the two case
studies**, which is the author's own lapse and is recorded rather than repaired.
