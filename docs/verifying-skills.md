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
bc -lq checks.bc
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

`checks.bc` header block to copy:

```
/* Exact-arithmetic checks for the `<skill>` skill.
 * Run:  bc -lq skills/<skill>/verification/checks.bc   (needs -l for l(), e())
 * bc truncates; scale is set explicitly. Lowercase identifiers only,
 * no `_`, no single uppercase letters.  See docs/verifying-skills.md.
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

## 7. Checklist before marking a skill verified

- [ ] `sh verification/run.sh` exits 0 from a clean checkout, from any directory.
- [ ] Every prescribed check has a visible `PASS` line **and** a negative
      contrast case that would `FAIL` if the guardrail were removed.
- [ ] `bc` runs with `-l`, lowercase identifiers, explicit `scale`, no stray `0`.
- [ ] Python imports stdlib only; every RNG stream is seeded from an argument.
- [ ] Capsule graph checks read `tsort` stderr for `cycle`.
- [ ] Lean cores are Mathlib-free or labelled as requiring it.
- [ ] `verification/README.md` has the step→check→result table and the
      folded-back findings (or "no correctness fix needed in the skill body").
- [ ] The README Verification table has a row with the tool versions and the
      headline numbers.
