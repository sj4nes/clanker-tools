# `test-writing` skill — verification run

`test-writing` is a *nudge away from known testing failure modes*, not a
tutorial. So verification cannot mean "re-solve a case with a closed form".
It means the thing the skill is actually claiming:

> **plant a bug of each documented shape; write the test an agent writes by
> DEFAULT and the check the skill PRESCRIBES; confirm the default runs green
> over the bug while the prescribed check catches it — and does not
> false-alarm on the corrected code.**

That last clause is the one that is easy to skip, and without it a check that
returns `FAIL` unconditionally would score as a perfect detector. Every subject
therefore ships with a `buggy=True|False` switch and every row of the matrix
is a three-cell claim.

**Fixture-first.** This directory was built *before* `SKILL.md`. The five
prescribed checks in `prescribed_tests.py` are the behaviours the skill will
tell an agent to adopt; the fixture is what makes them falsifiable rather than
advice. The bug shapes are taken from danluu's "How well do agents use
test/verification techniques?" eval (Sept 2026) and from Yossi Kreinin on
fixed input/output testing.

## Run

```
sh skills/test-writing/verification/run.sh
```

Tooling: `bc` 7.x (`-lq`), Python 3 (stdlib only), macOS `/bin/sh`. ~2 s wall.

## The subjects and their planted bugs

| | Subject (`subjects.py`) | Spec | Planted bug | Bug shape |
|---|---|---|---|---|
| A | `net_cents` | whole-percent discount, round **half-up** to the cent | truncates | expected values that encode the implementation's own output |
| B | `pack` / `unpack` | wire format writes symbols back-to-front (Zstd-style), so the reader consumes from the end | reader forgets the reversal | symmetric / palindromic input data masking a reversal bug |
| C | `step` | `table[state][symbol]` | `table[symbol][state]` | symmetric jump table masking an index transposition |
| D | `parse_kv` | `k=v;k=v`; on a repeated key, **last wins** | first wins | naive randomization where every input falls down the same rejection path |
| E | `median` | even `n` → mean of the two middle values | returns the lower middle | a property test that checks one trivial always-true property |

## What each step demonstrates

| Step | Prescribed check | Result |
|---|---|---|
| 1 (bc) | independent oracle for A's rounding, derived from the *spec sentence* in exact integer arithmetic — plus the two properties that make the shape dangerous | `19.90 @ 15% = 1691.5c` → half-up `1692`, truncated `1691` (**disagree**); `19.99 @ 15%` → both `1699` (**agree**); the `remainder ≥ 50 ⟺ half-up − truncated = 1` relation holds over all 2000 gross amounts — **pass** |
| 2 (py) | detection matrix, 5 bugs × {prescribed, naive} × {buggy, fixed} | every row `detects / green / misses` — **pass** |
| 2 — negative contrast | the naive suite on each buggy subject | all five run **green over the bug** — **pass** (the guardrail is visibly absent) |
| 2 — A's fourth cell | the captured-output suite on the *corrected* subject | **FAILS** — the naive test does not merely miss the bug, it **certifies** it, and would reject the fix. Kreinin's point, made executable |
| 3 (py) | branch coverage of the two generators for D | uniform random bytes reach the repeated-key branch in **0.0000%** of 20 000 inputs; the grammar-driven, steered generator reaches it in **72.3%** — **pass** |

The prescribed checks also carry their own **fixture-quality assertions**, which
is half the point: B asserts its generated data is not a palindrome (and that it
produced ≥ 400 such cases), C asserts its table is asymmetric off-diagonal, D
asserts the generator reached the branch at all. A check whose fixture cannot
discriminate is the naive test wearing a costume.

## Negative-contrast audit of this harness

Three independent corruptions, each caught by a *different* cell — so the three
cells are not redundant:

| Corruption | Caught by | Exit |
|---|---|---|
| `checks.bc` oracle `1692` → `1693` | bc `*** FAIL` marker + grep in `run.sh` | 1 |
| bug E un-planted (subject made correct, fixture left alone) | `prescribed on buggy` → `MISSES` | 1 |
| `prescribed_c` made vacuous (`return False`) | `prescribed on fixed` → `FALSE ALARM` | 1 |

Reverted after each; `sh run.sh` exits 0.

## Findings folded back

- **A prescribed check needs its own no-false-alarm cell.** Running only
  "prescribed detects the bug" scores a vacuous `return False` as perfect. This
  became the third cell of the matrix and belongs in `SKILL.md` as a rule:
  *run your new check against the code you believe is correct, too.*
- **Coverage is the observable for the randomization failure mode.** "Use
  structured generators" is unfalsifiable advice; *fraction of inputs reaching
  the branch under test* is measurable, and the naive generator scores exactly
  zero. `SKILL.md` should ask for that number, not for the adjective.
- The eval's meta-finding (long tutorial-style skills degrade results) means
  this README, not `SKILL.md`, is where the detail lives.

## The gates are necessary, not sufficient

`run.sh` proves that five specific checks beat five specific naive tests on five
planted bugs. It cannot prove an agent will *notice* which shape it is facing —
choosing what is risky, what the likely mistake is, and what an independent
oracle would even be for the code in front of it stays human (or stays with the
agent, and is why the skill is a nudge and not a checklist).

---

See [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) for the
shared run-script shape and the `bc` / Python portability rules.
