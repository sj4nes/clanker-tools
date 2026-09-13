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

**Fixture-first.** This directory was built *before* `SKILL.md`. The six
prescribed checks in `prescribed_tests.py` are the behaviours
[`SKILL.md`](../SKILL.md) tells an agent to adopt; the fixture is what makes
them falsifiable rather than advice. The bug shapes are taken from danluu's "How well do agents use
test/verification techniques?" eval (Sept 2026) and from Yossi Kreinin on
fixed input/output testing.

## Run

```
sh skills/test-writing/verification/run.sh
```

Tooling: `bc` 7.x (`-lq`), Python 3 (stdlib only), macOS `/bin/sh`. ~2 s wall.

Subject F was added later, when the `test-oracle-design` candidate in
`BACKLOG-BACKLOG.md` was folded into this skill rather than split out: its
proposed fixture was *this* fixture, and the one oracle route it named that
`SKILL.md` did not yet cover — differential testing — needed a planted bug of
its own to stay falsifiable.

## The subjects and their planted bugs

| | Subject (`subjects.py`) | Spec | Planted bug | Bug shape |
|---|---|---|---|---|
| A | `net_cents` | whole-percent discount, round **half-up** to the cent | truncates | expected values that encode the implementation's own output |
| B | `pack` / `unpack` | wire format writes symbols back-to-front (Zstd-style), so the reader consumes from the end | reader forgets the reversal | symmetric / palindromic input data masking a reversal bug |
| C | `step` | `table[state][symbol]` | `table[symbol][state]` | symmetric jump table masking an index transposition |
| D | `parse_kv` | `k=v;k=v`; on a repeated key, **last wins** | first wins | naive randomization where every input falls down the same rejection path |
| E | `median` | even `n` → mean of the two middle values | returns the lower middle | a property test that checks one trivial always-true property |
| F | `to_base_iterative` / `to_base_recursive` | render `n` in base `b` with `0-9a-z` | the **shared** `digit_char` helper drops the `-10` offset (digit 10 → `'k'`) | a differential test against a second implementation that shares the defect |

## What each step demonstrates

| Step | Prescribed check | Result |
|---|---|---|
| 1 (bc) | independent oracle for A's rounding, derived from the *spec sentence* in exact integer arithmetic — plus the two properties that make the shape dangerous | `19.90 @ 15% = 1691.5c` → half-up `1692`, truncated `1691` (**disagree**); `19.99 @ 15%` → both `1699` (**agree**); the `remainder ≥ 50 ⟺ half-up − truncated = 1` relation holds over all 2000 gross amounts — **pass** |
| 2 (py) | detection matrix, 6 bugs × {prescribed, naive} × {buggy, fixed} | every row `detects / green / misses` — **pass** |
| 2 — negative contrast | the naive suite on each buggy subject | all six run **green over the bug** — **pass** (the guardrail is visibly absent) |
| 2 — A's fourth cell | the captured-output suite on the *corrected* subject | **FAILS** — the naive test does not merely miss the bug, it **certifies** it, and would reject the fix. Kreinin's point, made executable |
| 2 — F's premise | two renderers with *different algorithms* (division loop vs recursion) calling one defective helper | the diff is **green over the bug** for all 2000 random `(n, b)` pairs; the stdlib `int(s, b)` round trip, which shares no code with either renderer, catches it — **pass** |
| 3 (py) | branch coverage of the two generators for D | uniform random bytes reach the repeated-key branch in **0.0000%** of 20 000 inputs; the grammar-driven, steered generator reaches it in **72.3%** — **pass** |

The prescribed checks also carry their own **fixture-quality assertions**, which
is half the point: B asserts its generated data is not a palindrome (and that it
produced ≥ 400 such cases), C asserts its table is asymmetric off-diagonal, D
asserts the generator reached the branch at all. A check whose fixture cannot
discriminate is the naive test wearing a costume.

## Displacement table

Required by [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) §7
for a behaviour-modification skill: every `SKILL.md` section must name the
default behaviour it displaces, and the verification must show that default
failing. A row that does neither is tutorial prose and belongs elsewhere; a row
that cannot be falsified by a fixture must say `judgement` out loud.

| `SKILL.md` section | default behaviour it displaces | where that default visibly fails |
|---|---|---|
| 1 — name the risky area | test what is easy to reach: getters, the happy path, the code you just wrote | **judgement** — no fixture can show this, because the fixture hands you the subject |
| 2 — state the likely mistake and the alternative interpretation | assert the behaviour you just observed, without naming a rival reading of the spec | **judgement, partly demonstrated** — subjects A ("half-up or truncate?") and D ("last-wins or first-wins?") *are* two-reading ambiguities, and the discriminating input exists only because the rival reading was named; naming it stays judgement |
| 3 — expected value from somewhere other than the code | paste in what the implementation printed; "diff against a second implementation" that shares the defect | subject A (captured-output suite passes the bug **and fails the fix**) and subject F (two algorithms, one bad helper, green diff) |
| 4 — break fixture symmetry and assert you did | symmetric tables, palindromic buffers, identical streams, equal lengths, round numbers | subjects B and C; the assertion half is `prescribed_b`'s ≥ 400 non-palindromes and `prescribed_c`'s off-diagonal asymmetry check |
| 5 — randomize structurally, report the coverage number | uniform random input, reported as "I fuzzed it" | subject D — **0.0000%** of 20 000 random-byte inputs reach the branch under test, vs **72.3%** for the steered generator |
| 6 — run the check against code you believe correct | run the new check only against the bug it was written for | matrix cell 2, and corruption NC3: a vacuous `return False` scores as a perfect detector until that cell exists |
| "properties must discriminate" | ship a property that is true of every possible answer | subject E — `min <= median <= max` passes the lower-middle bug; metamorphic negation symmetry does not |
| "before you call it tested" | — | a pre-ship gate over the six behaviours, not a seventh behaviour |

Two of the eight rows are `judgement`, and both are about *choosing* what to
test. That is the same boundary the closing section names, now located
precisely rather than gestured at.

## Negative-contrast audit of this harness

Four independent corruptions. The first three are each caught by a *different*
cell, so the three cells are not redundant; the fourth shows that the
`naive misses` cell also guards the **premise** of a subject — break the shared
helper and the fixture correctly stops claiming that differential testing is
fooled:

| Corruption | Caught by | Exit |
|---|---|---|
| `checks.bc` oracle `1692` → `1693` | bc `*** FAIL` marker + grep in `run.sh` | 1 |
| bug E un-planted (subject made correct, fixture left alone) | `prescribed on buggy` → `MISSES` | 1 |
| `prescribed_c` made vacuous (`return False`) | `prescribed on fixed` → `FALSE ALARM` | 1 |
| F's recursive renderer given its own **correct** helper (the shared-defect premise broken) | `naive on buggy` → `detects` | 1 |

Reverted after each; `sh run.sh` exits 0.

## Findings folded back

- **A prescribed check needs its own no-false-alarm cell.** Running only
  "prescribed detects the bug" scores a vacuous `return False` as perfect. This
  became the third cell of the matrix, and `SKILL.md` behaviour 6:
  *run your new check against the code you believe is correct, too.*
- **Coverage is the observable for the randomization failure mode.** "Use
  structured generators" is unfalsifiable advice; *fraction of inputs reaching
  the branch under test* is measurable, and the naive generator scores exactly
  zero. `SKILL.md` behaviour 5 asks for that number, not for the adjective.
- **"Two implementations" is not the property that matters.** Subject F's two
  renderers use different algorithms and are wrong identically, because the
  defect is in the helper they share. `SKILL.md` behaviour 3 therefore ends on
  an independence test — *does my oracle share code with the thing it is
  judging?* — rather than on a list of oracle types.
- The eval's meta-finding (long tutorial-style skills degrade results) means
  this README, not `SKILL.md`, is where the detail lives.

## The gates are necessary, not sufficient

`run.sh` proves that six specific checks beat six specific naive tests on six
planted bugs. It cannot prove an agent will *notice* which shape it is facing.
The displacement table above names exactly which parts are unfalsifiable here:
**behaviours 1 and 2** — choosing what is risky, and naming the likely mistake
and the rival reading of the spec. A fixture hands you the subject and the bug;
those two steps are the ones that have to find them. That is why the skill is a
nudge and not a checklist.

---

See [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) for the
shared run-script shape and the `bc` / Python portability rules.
