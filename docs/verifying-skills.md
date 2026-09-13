# Verifying a skill

Every methodology skill in this repo ships a `verification/` directory that
*re-solves a problem with a known answer* using the workflow the skill
prescribes, then checks that each prescribed step produced the right call. This
document is the shared contract for that directory: the run-script shape, the
portability rules that have already bitten (once per skill, historically), and
the "what counts as verified" bar.

It exists because the fixes below were discovered independently in
`simulation`, `statistics`, `design-of-experiments`, `control-systems`,
`visualization-design`, `unknown-discovery`, and every capsule `build/`. Read
this first and you skip that tax. The per-skill findings are summarised in the
Verification table in the [README](../README.md); this is the reusable core.

Templates to copy from: [`templates/verification/`](../templates/verification/).

---

## 1. What "verified" means here

A methodology skill has no bespoke CLI, so you cannot unit-test it. Instead:

1. **Pick a case with a closed form or an exact known answer.** M/M/1 for
   `simulation` (`L = ρ/(1−ρ)`); a normal mean for `statistics` (exact t
   interval); a mass–spring–damper for `control-systems` (analytic poles); the
   WCAG contrast formula for `visualization-design`. The case must be small
   enough to also compute by hand or by a second independent method.
2. **Run the skill's own workflow on it** — the same steps, in the same order,
   that `SKILL.md` tells an agent to take.
3. **Assert each prescribed check fires as claimed**, including the *negative*
   contrast: the naive z-interval must undercover, the pseudoreplicated analysis
   must inflate the false-positive rate, the too-slow loop rate must diverge.
   A guardrail you never see fail is not verified.
4. **Fold findings back.** Anything you had to fix to make the workflow run —
   a wrong constant in a reference `bc` snippet, an ambiguous step — is a defect
   in the skill, not in the harness. Fix the skill and note it in the README row.

`check.py` gates (as in `nonfiction-book`) are **necessary, not sufficient**:
they catch mechanical defects, not bad judgement. Say so in the skill's
`verification/README.md`.

---

## 2. The `run.sh` shape

```sh
#!/bin/sh
# Verification run for the `<skill>` skill: exercises the prescribed workflow
# on <known-answer case> and confirms each prescribed check behaves as claimed.
#
#   1. <check> ... (bc)
#   2. <check> ... (Monte Carlo / py)
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. <name> (bc) ==="
# `bc`'s exit status reports INTERPRETER errors (2 syntax, 3 undefined function,
# 4 missing file, 1 math error), NOT whether your claims were true -- a false
# claim is a VALUE to a calculator, not an error, and `quit` takes no status.
# So `set -e` catches a broken file but never a wrong answer.  Inspect the OUTPUT.
bcout=$(bc -lq checks.bc 2>&1) && bcstatus=0 || bcstatus=$?
printf '%s\n' "$bcout"
if [ "$bcstatus" -ne 0 ] \
   || ! printf '%s\n' "$bcout" | grep -q "ALL BC CHECKS PASSED" \
   || printf '%s\n' "$bcout" | grep -q '*** FAIL'; then
    echo "bc checks FAILED (exit status $bcstatus)" >&2; exit 1
fi
echo

echo "=== 2. <name> (python, stdlib only) ==="
$PY sim.py
```

Rules:

- **`#!/bin/sh`, not bash.** These run on the macOS system shell.
- **`set -e` and `cd "$(dirname "$0")"`** on every script — callable from any
  directory, fails loud.
- **`PY=python3`** in one place. Do not assume `python`.
- **`bc` section first, then Python.** `bc` does the exact arithmetic (formulas,
  bounds, identities); Python does anything needing loops, RNG, or arrays.
- **Print `PASS` / `FAIL` per check and exit non-zero on any failure.** For a
  multi-check Python block, accumulate `fail` and end with
  `raise SystemExit(1 if fail else 0)`.
- Wall time budget: seconds, not minutes. Monte Carlo reps in the low tens of
  thousands. `citation-check` (real network) is the sole exception at ~60–90 s.

---

## 3. `bc` portability rules (GNU bc 7.x / Gavin Howard bc)

These are the ones that have actually broken a run. The [`bc`](../skills/bc/SKILL.md)
skill has the full treatment; this is the verification-relevant subset.

| Rule | Why | Do |
|---|---|---|
| **Identifiers: lowercase, letter-initial, `[a-z0-9]` only.** | `bc` 7.x rejects `_` and single uppercase letters (`L`, `W`, `Pr`, `dim_sum`, `_d` all error with `bad expression` / `bad assignment`). | `ll`, `ww`, `pr`, `dimsum`. |
| **`bc -l` (or `-lq`) whenever you use `e()`, `l()`, `s()`, `c()`, `a()`.** | The math library is not loaded by default. | Always pass `-l` in `run.sh`; note it in the `checks.bc` header. |
| **`-l` sets `scale = 20`, so `%` becomes fractional.** | `a % b` under `-l` is not integer remainder. | For integer sections: `scale = 0` then `a - b*(a/b)`, or a sign-flip variable for `n % 2`. |
| **`x / 1` does not truncate on BSD `bc`** (and you may hit BSD `bc` if GNU is absent). | Truncation is a GNU-ism. | Drop to `scale = 0` for the division itself, restore after. |
| **`define` with no explicit `return` prints a stray `0` per call.** | Statement-value echo. | Sink it: `zz = myfunc(...)` instead of a bare `myfunc(...)`. |
| **Set `scale` before the first calculation, and reset it explicitly** when a block changes precision. | `scale` is global and sticky. | One `scale = N` near the top; re-set per block that needs different precision. |
| **Base conversion: set `obase` before `ibase`.** | After `ibase = 16`, the token `10` means base-16 sixteen. | `obase = A` (or set `obase` first). |
| End the script with `quit`. | Clean exit under `-q`. | |
| **The exit status reports interpreter errors, not false claims.** | `bc` exits 2 on a syntax error, 3 on an undefined function, 4 on a missing file, 1 on a math error — all documented in `man bc`. But a claim that is simply *wrong* is a value, not an error, and `quit` takes no status argument (`quit 1` exits 0). So `set -e` catches a **broken** file and never a **wrong** one. That partial protection is what made this look safe in 20 of 24 harnesses; see [`bc-verification-audit.md`](bc-verification-audit.md). | Capture the output and `grep` for both a pass banner and the absence of the failure marker. |
| **A pipe replaces `bc`'s status with the last command's.** | `bc f.bc \| tail` reports `tail`'s success even when `bc` died with a parse error. Easy to hit while *testing* a harness. | Redirect to a file, or capture with `$( )`, and check the status before piping. |
| **Force a nonzero exit too, with a deliberate `1/0`.** | `bc` has no `assert` and `quit` takes no status, but a divide-by-zero raises a documented math error and exits 1. This is the backstop for a runner that forgets to grep — the mistake that shipped in 20 of 24 harnesses. Verified: a naive `set -e; bc checks.bc` now catches a false claim. | End `checks.bc` with `if (fails > 0) { zz = 1/0 }`, **after** the FAIL lines and summary — a math error halts `bc` immediately, so put it last or you lose the diagnostics. |
| **Capture `bc`'s status explicitly; don't let `set -e` or a pipe eat it.** | Under `set -e` a failing `$( )` assignment aborts *before* the captured output is printed, losing the diagnostic. A pipe replaces `bc`'s status with the last command's. | `bcout=$(bc -lq checks.bc 2>&1) && bcstatus=0 \|\| bcstatus=$?`, print `$bcout`, then test both signals. |
| **Grep for the marker `*** FAIL`, never bare `FAIL`.** | Descriptive text legitimately contains the word — `visualization-design` prints `(claim: < 3 -> FAILS as a standalone cue)`, which made a bare `grep -q FAIL` fail a passing run. | Emit `*** FAIL: <claim>` from assertions only, and grep for exactly that. |
| **`abs` is a RESERVED name in macOS `bc`.** | `define abs(x)` fails with `bad function definition`, even without `-l`. | Name it something else — `aval`. |
| **BSD `bc` functions take NUMERIC arguments only.** | No strings, so a failure message cannot be passed to an assertion helper. | Print the message at the call site: `bad = chk(expr, tol); if (bad) { print "*** FAIL: ...\n" }`. |
| **Multi-line `define` bodies are the portable form.** | `define f(x) { if (c) return (a); return (b) }` parses on some builds and not others. | Put each statement on its own line, `{ }`-blocked. |

### Assert, do not annotate

**Printing a number next to a prose `(want >= 4.5)` is a documented example, not
a check.** Nothing fails when the formula drifts, and the file reads as
verification while providing none. The 2026-09-13 audit found this in 15 of 24
`bc` harnesses — including capsules whose `.bc` already computed an
**independent oracle** and simply never compared it to the closed form.

Every claim gets an assertion:

```
define aval(x) {
  if (x < 0) { return (-x) }
  return (x)
}
define chk(claim, tol) {        /* 1 on FAILURE, else 0 */
  if (aval(claim) <= tol) { return (0) }
  return (1)
}
fails = 0
bad = 0

bad = chk(got - want, 0.000000001); if (bad) { print "*** FAIL: <claim>\n" }
fails += bad

/* ...and END the file with the backstop, AFTER the summary: */
if (fails > 0) { zz = 1/0 }     /* forces exit 1; a math error halts bc here */

/* `*** FAIL` is the MARKER the runner greps for.  Never use the bare word
   `FAIL` in descriptive text on a passing path -- it will fail a good run. */

if (fails == 0) { print "ALL BC CHECKS PASSED\n" }
if (fails > 0)  { print "*** ", fails, " BC CHECK(S) FAILED\n" }
```

Prefer an **independent oracle** to a restatement: compute the quantity a second
way (direct summation against a closed form, substitution back into the original
equation) and assert the two agree. Restating a formula and comparing it to
itself certifies nothing — this is the same point the `test-writing` backlog
entry makes about expected values that encode the implementation's own output.

`checks.bc` header block to copy:

```
/* Exact-arithmetic checks for the `<skill>` skill.
 * Run:  bc -lq skills/<skill>/verification/checks.bc   (needs -l for l(), e())
 * bc truncates; scale is set explicitly. Lowercase identifiers only,
 * no `_`, no single uppercase letters.  `abs` is reserved on macOS -- use
 * `aval`.  EVERY CLAIM IS ASSERTED via chk() and prints a FAIL line, because
 * bc's `quit` always exits 0 and the runner greps the output.
 * See docs/verifying-skills.md and docs/bc-verification-audit.md.
 */
scale = 12
```

---

## 4. Python portability rules

| Rule | Why | Do |
|---|---|---|
| **Standard library only.** No `numpy`, `scipy`, `pandas`. | The harness must run on a bare Python 3. | `random`, `statistics`, `math`. Write the RNG helpers you need (`random.Random(seed)`). |
| **Seed every stream explicitly** and pass the seed as an argument. | Reproducible counterexamples; a reviewer re-runs and gets the same numbers. | `rng = random.Random(20260906)`; expose `seed=` on each function. |
| **Fixtures are JSON, not YAML.** | No `yaml` in stdlib. | Ship `verification/fixtures/*.json`; the skill's `templates/` stay YAML with the same field names, and say so in the README. |
| **`python3` in the shebang and the `$PY` var.** | `python` may be 2 or absent. | `#!/usr/bin/env python3` only if executed directly; otherwise call via `$PY`. |
| Keep functions importable (`from sim import replicate`) so `run.sh` can do targeted `python3 - <<'EOF'` blocks. | Lets `run.sh` show the contrast cases inline. | No top-level side effects; guard with `if __name__ == "__main__"`. |

---

## 5. Other tools

**`tsort`** (capsule graph checks) — BSD `tsort` **exits 0 on a cycle** and
writes `cycle in data` to stderr. Cycle detection must grep stderr, not check
`$?`:

```sh
err=$(tsort edges.txt 2>&1 >order.txt)
case $err in *cycle*) echo "CYCLE: $err"; exit 1;; esac
```

**`lean`** (capsule cores) — assume **no Mathlib**. `ring`, `sub_nonneg`,
complex numbers, and most `field_simp` are unavailable. Fall back to:

- `omega` for linear integer / nat goals (universal, but not division by a
  variable),
- `decide` for closed nonlinear identities on `Int` / `Nat`,
- complex numbers as `(re, im)` integer pairs,
- rewrite `½ x` cores as `(2 * x) / 2` to survive integer division.

Record what stays unproven — a `lean_status` per node, not a silent gap.

**`upmd`** (tutorials) — no native Lean runner (`Language not supported: lean`).
Lean beats are `bash` blocks that invoke `lean` on a heredoc and check exit 0;
they `SKIP` cleanly when `lean` is absent. Verify with `upmd --ci --all`.

**`ptx`** (discovery pass) — default keyword regex is letters-only, so
`cache_key` splits into `cache` + `key`; pass `-W '[A-Za-z0-9_]+'` to keep
identifiers whole. `ptx -A -r` errors on multi-file input — feed one cleaned
stream.

---

## 6. `verification/README.md` for the skill

One per `verification/` directory. Sections:

1. **What verification means for this skill** — "methodology-only, so we
   exercise the workflow on <case>".
2. **Model / case** and *why* it was chosen (has a closed form; is small).
3. **Run** — the one command, the tool versions, the wall time.
4. **What each step demonstrates** — a table mapping `SKILL.md` workflow step →
   prescribed check → result (with the actual numbers).
5. **Findings folded back into the skill** — every fix, with the target file.
   If nothing in the skill body needed a correctness fix, say that explicitly.
6. **The gates are necessary, not sufficient** — name what stays human.

---

## 6b. Octave: when the claim is about matrices

`bc` has no matrices and Mathlib-free Lean cannot quantify over dimension, so a
matrix-level claim can end up verified only at 2×2. That is the gap
[`octave`](../skills/octave/SKILL.md) fills. It is an **addition, not a
migration** — do not rewrite working `bc` checks.

| | `bc` | Octave | `lean` |
|---|---|---|---|
| arbitrary precision | **yes** | no (IEEE double) | n/a |
| matrices | no | **yes** (LAPACK) | only if hand-encoded |
| `assert` + nonzero exit | no (see §3) | **yes** | n/a |
| proves a universal | no | no | **yes** |
| startup | ~0.2s | ~1.7s | slow |

Three rules carry over from `octave/SKILL.md` and apply to any numeric check:

1. **Never check a built-in against itself.** `[Q,D]=eig(A); assert(Q*D*Q',A)`
   passes at 3e-15 and tests LAPACK, not your claim. Compute the claim by a
   route that is genuinely independent of the reference.
2. **Derive tolerances.** A residual scales as `n·eps`; a solution error scales
   as `cond(A)·eps`. A small residual never certifies an accurate solution. A
   check passing with a ~1× margin is telling you the tolerance is guessed.
3. **Octave needs no output-grepping.** It exits 1 on a failed `assert`, so
   `set -e; octave --no-gui --quiet checks.m` is sufficient — unlike `bc`.

Precision is the hard boundary: at least one existing `bc` check brackets a
quantity to 1e-25, which is inexpressible in double. Those stay in `bc`.

---

## 7. Checklist before marking a skill verified

- [ ] `sh verification/run.sh` exits 0 from a clean checkout, from any directory.
- [ ] Every prescribed check has a visible `PASS` line **and** a negative
      contrast case that would `FAIL` if the guardrail were removed.
- [ ] `bc` runs with `-l`, lowercase identifiers, explicit `scale`, no stray `0`.
- [ ] **Every `bc` claim is ASSERTED** (prints a `FAIL` line on mismatch), not
      merely annotated with a prose `(want ...)`; and `run.sh` greps the output
      rather than trusting the exit status, which `bc` fixes at 0.
- [ ] **The harness has been negative-contrast tested end to end**: corrupt one
      value, confirm `run.sh` exits nonzero, revert. An assertion never seen to
      fail is not known to be an assertion.
- [ ] Python imports stdlib only; every RNG stream is seeded from an argument.
- [ ] Capsule graph checks read `tsort` stderr for `cycle`.
- [ ] Lean cores are Mathlib-free or labelled as requiring it.
- [ ] `verification/README.md` has the step→check→result table and the
      folded-back findings (or "no correctness fix needed in the skill body").
- [ ] The README Verification table has a row with the tool versions and the
      headline numbers.
