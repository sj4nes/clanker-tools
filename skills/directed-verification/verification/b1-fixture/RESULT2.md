# b1 fixture, run 2 — INVALID (control arm received the treatment)

> **Superseded finding.** This file first reported *NO HEADROOM* under the
> pre-registered ceiling rule. That reading was wrong, and the correction is
> recorded here rather than rewritten away: the ceiling was not a fact about
> undirected agents, it was **contamination**. Arm A is not a control. See
> "Why this run is invalid" below.

**Claim under test (behaviour 1):** an agent told to write verification, without
being told *what to aim at*, produces a suite that passes over the risky case —
so naming the risky area and the specific mistake first is what makes the suite
able to fail.

**Verdict: INVALID.** Not refuted, not confirmed, and not even a ceiling —
arm A was given the treatment, so there were never two conditions.

## Result

| Subject | Arm | clean | planted | Score |
|---|---|---|---|---|
| A1 | A (bare instruction) | 0 | 1 | CATCHES |
| A2 | A | 0 | 1 | CATCHES |
| A3 | A | 0 | 1 | CATCHES |
| A4 | A | 0 | 1 | CATCHES |
| A5 | A | 0 | 1 | CATCHES |
| B1 | B (directed) | 0 | 1 | CATCHES |
| B2 | B | 0 | 1 | CATCHES |
| B3 | B | 0 | 1 | CATCHES |
| B4 | B | 0 | 1 | CATCHES |
| B5 | B | 0 | 1 | CATCHES |

**Δ = (B catches) − (A catches) = 5 − 5 = 0.**

`clean=0` means the suite passes on the correct implementation; `planted=1` means
it fails on the planted defect. Both are required to score `CATCHES` — a suite
that fails on everything scores `BROKEN`, not a catch.

## Why this run is invalid

Every arm-A subject had [`test-writing`](../../../test-writing/SKILL.md) loaded
in its context. The transcripts contain its section headings verbatim:

> **"Name the risky area first, in one line."**
> **"Get the expected value from somewhere other than the code."**

`test-writing` behaviour 1 *is* `directed-verification` behaviour 1, addressed to
the agent instead of to the person directing it. So the "undirected" arm was
directed — by a skill, rather than by its prompt. The five arm-A reports are not
evidence about default behaviour; they are evidence that agents follow
`test-writing` when they have it, which nobody doubted.

The tell was in plain sight and I misread it: all five arm-A agents produced a
report section called "Risky area and targeted mistake", in near-identical
wording. I read that as five agents independently converging on good practice.
Five independent agents do not converge on a section heading. It was a prompt
echo, and it should have been checked before the result was scored.

### What the design got wrong

`design2.md` anticipated contamination and argued it was survivable:

> "**This cannot be eliminated, and it does not bias Δ.** Both arms have
> identical access, so priming raises both arms equally. What it threatens is a
> **ceiling effect**."

That is wrong in a way worth keeping. Contamination by *general competence*
would indeed raise both arms and only threaten a ceiling. Contamination by **the
treatment itself** is different in kind: it does not raise arm A toward the
ceiling, it *makes arm A into arm B*. Δ is then structurally zero regardless of
whether the claim is true, and no sample size fixes it.

The ceiling rule fired on the symptom and hid the cause. A design that can report
"no headroom" needs a prior check that the arms differ at all.

### What would have caught it

A **manipulation check**: before scoring, confirm arm A did not receive the
treatment. Here that is one grep of each subject's context and transcript for
`test-writing`'s prescriptions. It costs nothing and it invalidates the run in
seconds. Run 3 must not score without it.

## Why arm A looked so good

The plant was designed to have headroom. `plant.py` inserts

```python
if negative and 2 * rest == denominator: whole -= 1
```

which differs from the correct implementation **only at negative ties** —
931 of 28,824 enumerated cases, every one of them a negative tie. Catching it
therefore *requires* exercising a negative tie. The design's assumption was that
an undirected agent would build a positives-only fixture table and miss it.

That assumption was wrong, and the subjects say why in their own words. Every
arm-A agent identified the tie-and-sign interaction unprompted, and several named
the exact discrimination the plant exploits before writing a line of test code:

- **A2:** "the mistake I aimed at is half-**up** (toward +inf) masquerading as
  half-**away-from-zero**: the two are identical on every positive input and
  differ by 1 on every negative tie, so a positives-only fixture table cannot
  see it."
- **A5:** tabulated `-5/2` across half-away / half-up / truncate to show the
  three readings "only diverge" on the negative side.
- **A1:** "All five agree with the implementation on `4/2` and `6/3`, so those
  are deliberately not the fixtures."

**This is not evidence about undirected agents.** Every quotation above comes
from an agent that had `test-writing` in context telling it to do precisely this.
The reports are faithful; they are just reports of the treatment working, in both
arms. All ten subjects also wrote a mutation harness or an in-file mutant set
that neither *prompt* asked for — because `test-writing` asks for it.

One subject (A4, nominally **arm A**) went further and caught a defect in its own
harness: Python keys its bytecode cache on source mtime at 1-second resolution
plus file size, so single-byte mutants written within the same second silently
reused each other's stale `.pyc`, and one mutant scored `SURVIVED` on 2 of 3
runs. It fixed this with `PYTHONDONTWRITEBYTECODE=1` and made a failing baseline
abort rather than score mutants — because a module that fails to import marks
every mutant "killed". That is `directed-verification`'s own subject matter (a
check that cannot fail is not a check) — good work, and not unprompted.

## What this does and does not license

- **It does not refute behaviour 1.** No contrast existed to measure.
- **It does not support behaviour 1 either.** Two runs, no evidence.
- **It says nothing about undirected agents.** The earlier version of this file
  claimed it did. That claim is withdrawn.
- **It is not evidence for the `role-deck` pattern** ("an unprompted agent will
  skip the careful step keeps failing to reproduce"). Those two fixtures scored
  unforgeable artifacts and their subjects were not handed the treatment; this
  one was. Filing it alongside them would be inflating a pattern with a case
  that does not belong to it.

## What a run 3 would need

**Arm isolation is now the blocking problem, ahead of the plant.** In order:

1. **A genuinely undirected control.** Subjects must run without this corpus's
   skills in context — a clean environment, not merely a different working
   directory. Spawning from a session inside the repo was not sufficient, and
   the design's claim that it was is the error that cost this run.
2. **A manipulation check before scoring.** Grep each subject's context and
   transcript for the treatment's fingerprints. A run that cannot show the arms
   differed does not get scored.
3. **Then** the plant question: whether a defect that a competent undirected
   suite genuinely misses can be built at all. That is still open, and still
   probably means leaving self-contained pure functions behind — but it cannot
   be assessed until 1 and 2 hold.

Until then, behaviour 1 stays **unmeasured**.

Run 1 is at [`RESULT.md`](RESULT.md) — invalid for a different reason (the subject
itself was buggy, so arm-A agents scored `BROKEN` for correct work).

## Provenance

- Design pre-registered: `e3e8498`, 2026-09-15 22:31:13 −0500, before any subject ran.
- Subject `rounding.py` md5 `127904733d75847a47bd1499913a6692`, verified identical
  in all ten working directories after the run — no subject modified the code it
  was testing.
- Scoring by `score2.sh`, which asserts its 28,824-case `Fraction` precondition
  (clean code correct, planted code wrong only at negative ties) before scoring.
  That precondition held. It is the **arm assignment**, not the scoring, that
  failed — `score2.sh` has no way to detect a contaminated control, which is the
  gap the manipulation check closes.
- Contamination established from the subjects' own transcripts under
  `tasks/*.output`, which quote `test-writing/SKILL.md` lines 37 and 48.
