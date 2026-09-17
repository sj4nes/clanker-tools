# Changelog — directed-verification

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/directed-verification/

## 1.4.0 — 2026-09-17

**MINOR: a cited result restated; re-read it.** "Two premises … refuted 8/8" is
now 8/8 and 3/8 proven, after `claim-fixture` F10 (`role-deck` 2.5.0).

## 1.3.0 — 2026-09-17

**MINOR: behaviour 3's evidence was restated; no prescription changed.** Re-read
it. The count of self-corrections published in 1.2.2 was overstated, and the
claim now rests on commits read by hand.

The detector reported 5. Two were not admissions: a hypothetical in `0fbb03c`,
and this skill's own release commit (`6fbfac2`), describing what the detector
counts. At release the published "at least three" rested on 2 real matches.
Found while drafting the book's II.6 (ledger C-II-47), by reading each matched
sentence rather than the total.

- The count was called a lower bound. It is no bound: it matched false
  sentences and misses true ones (`dde3f82`). Withdrawn everywhere.
- The claim ≥3 is kept, because it is true: `197b313`, `95a8cb1`, `d084b25`,
  read by hand.
- `--history` checks the scan against those commits and the two known false
  ones. A real sentence it miscounted joins the negatives. Commits that touch
  the detector are skipped. Each guard broken alone fails the run.
- README: `test-writing` has 5 covered rows, not 6.

## 1.2.2 — 2026-09-16

**PATCH: no statement changed. Behaviour 1 is still unmeasured, after three
attempts.** Run 3 is recorded INVALID in `b1-fixture/RESULT3.md`.

All fifteen subjects scored `NO-HARNESS`: they were spawned with no tool
permissions, so none could write a file or execute anything. Six ran and were
blocked; the other nine hit an account session limit. The two are unrelated —
the permission defect would have struck on a fresh quota.

What run 3 did establish, none of it about the claim:

- **Run 2's contamination is fixed.** The isolation probe saw `NONE`, and all
  five arm-A transcripts were clean of every fingerprint.
- **Interleaving works.** The session limit truncated A3–5, B3–5 and C3–5 —
  all three arms equally. Run 1's F4 wiped four of five arm-B subjects.
- **`NO-HARNESS` kept distinct from `0 killed` is why the failure was legible**
  rather than reading as fifteen agents writing useless tests.

Fixed for the next attempt: an explicit identical toolset per arm, a capability
probe before spawning (`claim-fixture` G9), and attrition no longer recorded as
completion — a session-limit stub used to be written with a `.done`, so a
resumed run would have skipped the nine subjects that never ran.

## 1.2.1 — 2026-09-16

**PATCH: no statement changed.** Behaviour 1 is still marked unmeasured; this is
run 3's pre-registration, committed before any run-3 subject exists.

`b1-fixture/design3.md` clears all seven pre-flight gates and records the G5
judgement by hand. What changed from run 2:

- **The measure.** A kill rate over a frozen 20-mutant set replaces the single
  planted defect. One plant makes the whole run depend on guessing the one
  defect an undirected agent misses; guess wrong and Δ is zero whatever the
  truth is.
- **The subject.** `subject3/` is a duration parser/formatter whose intent lives
  in a separate `SPEC.md` and whose code carries no worked examples. Run 2's
  docstring wrote out the plant's discriminating case for the subject to read.
- **A third arm.** Arm C is handed the risky areas — a positive control. If C
  does not beat A, the run is UNINTERPRETABLE and Δ is not reported. This method
  has four runs and no positive result behind it; until an effect it knows is
  there shows up, every refutation it has produced is an unknown-sensitivity
  null.
- **Subjects are Bash-invoked separate processes**, not Agent-tool subagents,
  and the isolation probe runs before spawning.

Two defects were found by running the scorer's preconditions rather than by
reasoning about them: one of the first twenty mutants was equivalent to the
reference (unkillable, and it would have depressed both arms invisibly), and the
probe corpus mislabelled a string as valid. Measured instrument range before any
subject exists: a two-assertion suite scores 4/20, an oracle-based suite 20/20.

Run 1 and run 2's prompts move to `b1-fixture/archive-runs-1-2/`.

## 1.2.0 — 2026-09-15

**MINOR: a reported result was withdrawn; re-read it.** Corrects 1.1.0, which reported b1 run 2 as *no headroom*. It was **invalid**:
the control arm received the treatment.

Every arm-A subject had `test-writing` loaded in context — its behaviour 1
("Name the risky area first"; "Get the expected value from somewhere other than
the code") is `directed-verification` behaviour 1 addressed to the agent. Their
transcripts quote it verbatim. The arms were one condition, so Δ = 0 was
structural and no sample size would have fixed it.

The tell was five arm-A reports sharing a near-identical "Risky area and
targeted mistake" heading. 1.1.0 read that as independent convergence on good
practice; independent agents do not converge on a section heading.

Withdrawn from 1.1.0: the claim that undirected agents already test the
discriminating case, and the filing of this run alongside the two `role-deck`
refutations. Neither is supported — arm A was not undirected.

Added: run 3 must run subjects in an environment without this corpus's skills,
and must run a **manipulation check** confirming the arms differ before scoring.
The pre-registered ceiling rule is kept but demoted — it fired on the symptom and
hid the cause.

## 1.1.0 — 2026-09-15 (superseded by 1.2.0)

**MINOR: evidential status restated; re-read it.** Behaviour 1's fixture ran twice. It is still unmeasured, and the page now says
so precisely rather than calling it "logged as work".

- **Run 1 invalid.** The subject function was itself buggy (`int()` truncates
  toward zero), so arm-A agents scored `BROKEN` for correct work.
  `verification/b1-fixture/RESULT.md`.
- **Run 2: NO HEADROOM.** Clean subject, pre-registered design (`e3e8498`,
  committed before any subject ran). Both arms scored 5/5 `CATCHES`; Δ = 0. The
  pre-registered **ceiling rule** requires reporting this as *no headroom*, not
  as a refutation — a design in which the treatment cannot score higher has not
  tested the treatment. `verification/b1-fixture/RESULT2.md`.
- The plant had headroom (differed from correct code only at negative ties,
  931/28,824 cases); the **population** did not. All five undirected agents named
  the tie-and-sign discrimination unprompted, and one caught a stale-`.pyc`
  flake in its own mutation harness without being asked. A third run needs a
  defect a competent undirected suite genuinely misses.

No behaviour changed. `SKILL.md` and `verification/README.md` restate
behaviour 1's evidential status; the six behaviours are as released.

## 1.0.0 — 2026-09-15

First release. Closes the second gap the book's fat outline found: three
concepts with no source at all, clustered on the book's own stated
differentiator — the agent as a participant in quality rather than a producer of
text. Fifty-one skills, every one produced by a human and an agent working
together, and none about doing that.

Displacement table: **1 covered, 4 judgement, 2 gaps** — a weak table, reported
as weak. Behaviour 1 is measurable with `claim-fixture` and has not been
measured; that is logged rather than glossed.
