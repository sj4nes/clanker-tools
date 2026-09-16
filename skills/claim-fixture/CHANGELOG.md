# Changelog — claim-fixture

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/claim-fixture/

## 2.2.0 — 2026-09-16

**MINOR: a new gate, G8 — what population is this a claim about?** An agent
subject is a model at an effort level. Neither b1 run 1 nor run 2 records which
model produced its subjects (F8), so neither is reproducible and neither claim
has a stated scope. A design must now carry a line `Primary configuration:
<what a subject is>`, recorded per subject at spawn time rather than
reconstructed afterwards.

G8's third checkbox is the one with teeth: if more than one configuration will
be run, the design must say which is **primary** and which are labelled
replications. Configuration is cheap to vary and expensive to vary honestly —
*k* models × *m* effort levels is *k·m* chances to land the band you wanted at
n=5. Behaviour 5 pre-commits the bands; it does not by itself pre-commit which
cell counts. Block, do not cross. Where a configuration is varied deliberately,
the rubric asks for a directional prediction registered in advance, because an
interaction chosen once the cells are visible is a description of noise.

A fixture whose subjects are not model-driven still declares the line — it
declares people, or a fixed program. The gate asks you to name your subjects.

The first version of G8 tested only the extracted value, which collapsed
"absent" into "present but empty" and left its FAIL arm unreachable. The label
and the value are now tested separately, and `preflight-check.sh` asserts both
arms fire.

`references/pre-flight.md` predicted, in 2.0.0, that "a fifth run will probably
add a gate". The fifth run has not been spawned yet and has already added one.

## 2.1.0 — 2026-09-16

**MINOR: G3 now scores the scorer the design actually claims.** A fixture
directory accumulates runs. `preflight.sh` took the newest `score*` file off a
glob, so a run-3 design cleared G3 on a run-2 scorer written for a different
subject — the gate said CLEAR while the scorer for the run being flown did not
exist.

A design in a multi-run directory must now carry a line `Scorer: <file>`. The
declared file must exist, or G3 is BLOCKED. Single-run directories are
unaffected and still fall back to the glob.

The first version of this inferred the scorer from prose instead of a
declaration, and promptly picked the scorer's own *check harness* out of a
sentence about it. Inference from prose is not a declaration.

`preflight-check.sh` §3 is rebuilt. It asserted the b1 fixture blocks at a named
gate; repairing that fixture moved the gate twice and broke the assertion twice.
It now checks both sides against the real fixture: run 2's state, reconstructed
from the files that run actually used, must be blocked at G2a/G2b/G4 — and the
repaired fixture must CLEAR, so the first half cannot be satisfied by a gate
that refuses everything.

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
