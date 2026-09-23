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
   || printf '%s\n' "$bcout" | grep -qF '*** FAIL'; then   # -F is load-bearing, see §3
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
| **Grep for it with `-F`: `grep -qF '*** FAIL'`.** | `'*** FAIL'` as a *regex* starts with a repetition operator applied to nothing. GNU `grep` tolerates a leading `*` as a literal; **both greps on this machine exit 2**: BSD `/usr/bin/grep` says `repetition-operator operand invalid`, and `ugrep` (installed as `grep` here) says `error at position 4 … empty (sub)expression` — and shell `if` treats 2 as false, so the clause silently never fires. Found 2026-09-13 in **8 of 9 harnesses plus the template** (every one copied from the template), where a planted `*** FAIL` marker passed the gate with exit 0. The other two signals (missing pass banner, `1/0` backstop) had been masking it. | `grep -qF '*** FAIL'` — fixed-string, no escaping to get wrong. Not `grep -q '*** FAIL'`, not `grep -q '\*\*\* FAIL'`. |
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

/* `*** FAIL` is the MARKER the runner greps for, with `grep -qF` -- as a
   regex it is an invalid leading repetition operator and ugrep exits 2, which
   shell `if` reads as false.  Never use the bare word `FAIL` in descriptive
   text on a passing path -- it will fail a good run. */

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
`$?`. That, and the rest of the graph rubric, is §5a below.

**`lean`** (capsule cores) — the exit status does **not** fall to a `sorry` or an
`axiom`; see §5b for that and for the `lean_status` rubric. On tactics, assume
**no Mathlib**. `ring`, `sub_nonneg`,
complex numbers, and most `field_simp` are unavailable. Fall back to:

- `omega` for linear integer / nat goals (universal, but not division by a
  variable),
- `decide` for closed nonlinear identities on `Int` / `Nat`,
- complex numbers as `(re, im)` integer pairs,
- rewrite `½ x` cores as `(2 * x) / 2` to survive integer division.

Record what stays unproven — a `lean_status` per node, not a silent gap — and
make the status carry a `lean_ref` a machine can resolve (§5b).

**`upmd`** (tutorials) — no native Lean runner (`Language not supported: lean`).
Lean beats are `bash` blocks that invoke `lean` on a heredoc and check exit 0;
they `SKIP` cleanly when `lean` is absent. Verify with `upmd --ci --all`.

**`ptx`** (discovery pass) — default keyword regex is letters-only, so
`cache_key` splits into `cache` + `key`; pass `-W '[A-Za-z0-9_]+'` to keep
identifiers whole. `ptx -A -r` errors on multi-file input — feed one cleaned
stream.

---

## 5a. Graph artifacts (`tsort`): what the checks can and cannot catch

`bc`'s hole was that a false claim is a *value*, not an error, so the harness
reported a pass. The graph layer had the same shape of hole, for the same
reason: `graph-check.sh` and `build-tree.sh` check the emitted order against
**the edge list they were handed**. Restating the edges and comparing them to
themselves certifies nothing — the same point §3 makes about restating a
formula. This was established by planting defects, not by reading the scripts:

| planted defect | caught before 2026-09-14? | by what |
|---|---|---|
| a cycle (reverse an edge) | ✅ | the stderr guard in `build-tree.sh` |
| an edge to an unregistered node | ✅ | the endpoint `comm` in `graph-check.sh` |
| a self-edge | ✅ | the field/self-edge `awk` |
| **a real edge deleted** | ❌ **exit 0** | nothing |
| **a spurious edge added** | ❌ **exit 0** | nothing |

The first three are *hygiene* — is the graph well-formed? The last two are
*truth* — are these the right edges? Hygiene has no opinion about truth, and
a capsule can be perfectly well-formed and still wrong.

### The oracle: node text, written independently of the edge list

Every node carries text that was written separately from the edge list — a
`dependencies:` list, a `related.requires` naming, a proof or derivation clause,
a formula entry's `Prereqs:` line. That independence is what makes it an oracle
rather than a restatement. `build/check-edge-evidence.py` reads it and gates on
two classes:

| class | evidence | rule |
|---|---|---|
| **hard** | the node's own `dependencies:` list, or a formula entry's `Prereqs:` / `Assumptions:` line | must equal the graph's edges into that node, **exactly** — the same claim written twice |
| **hard** | `related.requires` / `related.uses` | must lie in the prerequisite closure |
| **soft** | another node id appearing verbatim in `proof` / `derivation` / `well_definedness` prose | must be adjudicated once, in `validation/edge-evidence-ignore.txt` |

Deliberately **not** evidence: `common_misuse`, `counterexamples_when_dropped`,
`related.complement_of`, a formula entry's `Special case:` / `Failure:` clauses,
and symbol-definition lines. Those name what a result is *contrasted with* —
precisely where an edge would be **wrong**. Widening the net widens the noise,
not the yield; two rounds of widening and re-narrowing produced that list.

A soft hit on a **descendant** is a forward reference — normal prose, reported
and never failed. A hit on anything else is a candidate missing edge, and stays
a build failure until someone rules on it:

| verdict | meaning |
|---|---|
| `english-word` | the id is an ordinary word here — "the *structure* of phi", "in infinite *dimension*" |
| `homonym` | a different concept with the same name — a capsule can hold a propositional `satisfaction` node *and* first-order satisfaction prose |
| `forward-ref` | names a downstream result |
| `cited-not-used` | an alternative route, an attribution, a scope remark |
| `stated-elsewhere` / `judged-independent` | the residue; say why in the note |

A **stale** entry — one adjudicating a hit that no longer occurs — also fails.
The file is an audit trail, not a mute button, and it converges.

### The rubric

**Per edge — evidence grade, computed not annotated.** A hand-maintained grade
on ~3,800 edges would rot, so `check-edge-evidence.py` derives one and prints
the three counts:

| grade | meaning |
|---|---|
| `derived` | the target's proof / derivation prose names this prereq — the strongest backing a capsule holds |
| `declared` | the target's dependency list names it, and the hard gate holds that list equal to the graph |
| `unbacked` | the target carries **no text at all**; nothing in the capsule could contradict this edge |

`unbacked` is the number to watch — it is the per-edge form of falsifiable
coverage, and it is what a half-populated capsule is really reporting when its
build says ok. At the first run: 0 unbacked in `math-probability`,
`math-linear-algebra`, `math-statistics` and both chemistry capsules; 236 of 316
in `math-logic-and-proof` and 195 of 248 in `math-real-analysis`, whose node
entries are written for a fraction of their registered nodes.

**Per graph — falsifiability.** `validation/mutation-check.sh` plants all five
defects from the table above on every run and asserts each is caught. Two of
them (a deleted edge, a spurious edge) are only catchable by node text, so they
are planted on a node that **has** text; the fraction of nodes that do is
reported as `falsifiable coverage`, because on a node with no entry the graph
is not falsifiable by anything. Report both numbers. A capsule with no entries
at all plants 3 mutations and says so, rather than claiming 5/5.

**Per order — fitness.** The order is one of many valid linearisations, so
assert only the properties you rely on: every supplied edge respected
(`build-tree.sh`), no node duplicated, order-nodes ≡ edge-nodes, and
determinism — feed `tsort` the `LC_ALL=C sort -u` edge file, never the raw
plan, or the tie-break shifts with input order.

### What the first run of this rubric found (2026-09-14)

Over 14 capsules: **18 hard violations** (5 formula entries whose `Prereqs:`
line disagreed with the graph, 1 with no `Prereqs:` line at all, 1 holding prose
where the list belongs, and 11 dependencies a YAML declared that the graph never
carried); **~55 soft hits**, of which **36 were real missing edges** and the rest
adjudicated; and — found only because the checker tried to *load* every YAML —
**7 result files in two capsules that did not parse at all**, in the two capsules
that had no `check-consistency.py` to load them. Nothing had ever read them.

Two of the corrections were to this harness rather than to a capsule, which is
the expected yield of building it: the soft scan first fired on contrast text
and symbol lines (~180 hits, mostly noise), and the deleted-edge mutation
matched the plan line *literally*, so a trailing `# evidence` comment made the
deletion silently do nothing — a mutation that reports itself as surviving.
Both are in the scripts' comments now.

---

---

## 5b. Lean cores: what "machine-checked" is actually claiming

`lean file.lean && echo ok` is the **same hole as `bc ... && echo ok`**, and it
was found the same way — by planting defects in a real capsule file, not by
reading the script. All three of these exit **0**:

| planted in `math-probability/validation/proof-checks.lean` | `lean` exit | what it means |
|---|---|---|
| `theorem t : ∀ n, n + 0 = n := by sorry` | **0** | a warning on stderr, nothing else. The theorem is unproved. |
| `axiom cheat : ∀ n : Nat, n = n + 1` | **0** | silent — and `3 = 4` now follows from it |
| `theorem "core" : (2:Nat) + 2 = 4 := by decide` | **0** | true, and proves nothing general |
| `theorem t : ∀ n, n + 1 = n := by omega` | 1 | the one case the exit status does catch |

The exit status catches a **broken** file — a syntax error, a genuinely false
claim — and never an **unproved** or **overclaimed** one. The `sorry` warning
does not rescue it: it arrives on the same stream as benign deprecation
warnings, so it has to be grepped for by name, exactly like `*** FAIL` in §3.

And the compile gate says nothing at all about the claim that matters. A node
asserting `lean_status: core` is claiming *this capsule's `.lean` file proves the
general statement of this node*. Nothing about compiling the file tests that.

### `build/check-lean-cores.py`

| gate | rule |
|---|---|
| source hygiene | no `sorry`, `admit`, `axiom`, `native_decide`. `axiom` makes everything provable; `native_decide` moves the trust base from the kernel to the compiler |
| compile | exit 0, no `error:`, **no `declaration uses 'sorry'`**. Other warnings are counted and reported, never failed — a deprecation is not an unsound proof |
| vocabulary | `lean_status` ∈ `core` / `dim_core` / `instance` / `partial` / `cited` / `none` / `stated_not_proved` |
| locatability | every status claiming machine verification carries a `lean_ref` naming something a machine can **find**: a declaration, or a `/-! ## N.` (math) or `-- N.` (formula) section header. Anonymous `example … := by decide` blocks can only be cited by section, which is why sections count |
| overclaim | `core` means the **general** statement is proved, so its ref must name a real declaration whose statement **binds a variable**. A `core` backed only by a section of `decide` instances is an `instance` |

An empty ref, a prose ref, or a ref pointing only at a `.bc` file is not
evidence. That is the Lean form of *annotate, do not assert*: it reads as
verification and provides none.

`validation/lean-mutation-check.sh` plants all six defects per build and asserts
each is caught. Only **one** of the six is caught by `lean` itself.

### What the first run found (2026-09-14)

**41 problems across six capsules. `math-linear-algebra` had zero** — it is the
control: it already carried `build/leanmap.py` (an authoritative status map whose
default is the weakest status, so a spec cannot overclaim) plus
`build/check-lean-refs.py`. The guard works; it had simply never been copied to
its six siblings.

| finding | count | |
|---|---|---|
| `lean_status: core` with an **empty** `lean_ref` | 19 | 6 in `math-probability`, 13 in `math-statistics` — a claim of machine verification with nothing behind it at all |
| a Lean status whose ref points only at `instance-checks.bc` | 7 | the evidence is bc arithmetic; the node claimed Lean |
| a `core` whose ref names no declaration and no existing section | 10 | prose describing a proof technique |
| `lean_status: core-arith`, outside any vocabulary | 5 | → `partial`: the arithmetic core is proved, the theorem is not |

After the fixes, `math-probability`'s honest count of machine-verified nodes
went from **36 claimed to 25**, and `math-statistics`' from **44 to 28**. No
proof was wrong — every `.lean` file compiled clean before and after, with no
`sorry` and no `axiom` anywhere in the repo. What was wrong was the **index**:
a third of the claims pointed at nothing.

Three conventions for `lean_ref` were in use (bare namespaced declarations;
file + declaration in prose; file + `§N`). All three are now accepted, because
all three are locatable — but a fourth, free prose, is not, and that is what the
19 empty and 10 unlocatable refs collapsed into.


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
7. For a behaviour-modification skill (§7): the **displacement table** —
   section → default behaviour displaced → where that default visibly fails,
   with `judgement` rows marked as such.

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

## 7. What the document itself must be: a nudge, or a reference

Verification usually asks "does the prescribed workflow get the right answer?"
There is a second question, and it has an evidence base: **does the document
change what the agent does at all, or does it restate what the model would have
done anyway?**

The evidence is danluu's "How well do agents use test/verification techniques?"
(Sept 2026). Given only the name of a technique or library, agents fell back to
poor default testing: "regardless of the library or technique suggested, agents
failed to use the technique". The highest-scoring condition was a five-bullet
nudge, which its author says did not work as intended. A test skill from a
collection with ~250k stars scored almost as well as no instructions overall,
and **worse than no instructions on the runs it actually influenced**. One task,
one model family; the author cautions against strong conclusions from the
ordering. (Corrected 2026-09-17: this paragraph said "all 26 conditions" and
"several tutorial-style skills … worse than no skill at all", both overstated;
see `docs/book/claim-ledger.md`, the opening finding.)
A skill modifies a default behaviour distribution; it does not teach from zero,
and prose that reads like a tutorial spends context restating the default it
was supposed to displace.

That does not make reference material bad. It makes the *kind* of writing
decisive — and the unit is the **section, not the skill**. `statistics` is a
behaviour-modification skill that legitimately contains two reference tables
(the regime table, the method-selection table) whose payload is capsule-sourced
fact an agent's prior is thin on. Classify each section; do not classify the
document:

| | behaviour-modification skill | tool-fact skill |
|---|---|---|
| examples | `test-writing`, `statistics`, `simulation`, `design-of-experiments`, `unknown-discovery`, `citation-check` | `bc`, `ed`, `csplit`, `tsort`, `ptx`, `octave`, `uv`, `typst` |
| the agent's prior | already has a default behaviour, and it is **wrong** | genuinely **does not know** — BSD `bc` rejects `_` in identifiers, BSD `tsort` exits 0 on a cycle, `abs` is reserved on macOS |
| what the document is | a short list of displacements | facts the agent cannot derive, organised for lookup |
| how it fails | tutorial prose restates what the model already does — and can be worse than nothing | vagueness or omission; one missing quirk costs a run |

For the left-hand column the rule is checkable, not stylistic:

> **Every section must name the default behaviour it displaces, and the
> verification must show that default failing.**

So author a **displacement table** and keep it with the verification, not in
`SKILL.md`:

| `SKILL.md` section | default behaviour it displaces | where the default visibly fails |
|---|---|---|
| behaviour 3, "expected value from somewhere other than the code" | pasting in what the implementation printed | fixture subject A — the captured-output suite passes the bug **and fails the fix** |
| … | … | … |

`test-writing` is the worked example: six behaviours, six planted bugs, six
naive suites that run green over them — see
[`skills/test-writing/verification/README.md`](../skills/test-writing/verification/README.md)
for the filled-in table.

- An empty **second** cell is tutorial material. Move it to `references/`
  (loaded on demand) or to `verification/README.md`, where the detail is free.
- An empty **third** cell is advice — *unless* the row is explicitly a
  **judgement** step: choosing what is risky, choosing the estimand,
  adjudicating evidence. No fixture can falsify those, because the fixture
  hands you the subject. Mark such rows `judgement`, and name them in the
  skill's "the gates are necessary, not sufficient" section.
- What is not allowed is an **unmarked** row: a section that neither displaces
  a demonstrable default nor declares itself judgement. Two of `test-writing`'s
  eight rows are judgement, and both are about *choosing* what to test.

Sort the finished table into three blocks and **report the counts** — they are
the deliverable, not the prose:

| Block | Meaning | What to do |
|---|---|---|
| **covered** | the default is demonstrated failing in the harness | nothing |
| **`judgement`** | no fixture can falsify it, because the fixture supplies what the step is supposed to find | name these rows in "the gates are necessary, not sufficient", replacing a general gesture at judgement |
| **gaps** | a fixture *could* falsify it and does not | log each as a concrete harness section in `BACKLOG.md` |

The **gaps block is the yield.** `statistics` — the second skill through this
rule and the first not designed around it — came out **7 covered, 5 judgement,
5 gaps**, with no `SKILL.md` claim found wrong: the finding was that five claims
rest on the skill's authority where the harness could carry them (CI/test
duality, p-value uniformity under the null, pseudoreplication — already
demonstrated in `design-of-experiments` and never ported, prior sensitivity, and
a regression principle with no regression case anywhere in the harness). A
"verified" skill can have a green harness and still assert most of its
principles on authority. That is what the table is for.

One more thing the second table did, which is worth expecting: it was written by
*reading the harness output closely enough to build the rows*, and that is how
the dead `grep -q '*** FAIL'` clause in §3 was found — a stray stderr line in an
otherwise-passing run. Building the table is a review of the harness, not only
of the document.

Two corollaries, and one caution:

- **Length is a symptom, not the metric.** Do not pad a nudge skill toward the
  length of a reference skill, and do not crash-diet a reference skill whose
  payload *is* the table. `bc`'s portability rules are the payload.
- **Do not verify the document by reading it.** Reading rewards fluent prose,
  which is the failure mode. Verify it by the displacement table having no
  empty cells.
- **Calibration.** This is one eval, on testing tasks. The mechanism — a skill
  shifts a distribution the model already has — generalises; the effect size
  measured there does not automatically transfer to, say, a statistics
  workflow. Treat "worse than no skill" as a demonstrated possibility to design
  against, not as a measured property of every long document.

---

## 7a. Links: the claim no skill's own harness checks

`sh tools/check-skills.sh` runs `tools/check-links.py` over every tracked
Markdown file. Two gates, both hard:

- **`[file]`** — the relative target exists.
- **`[anchor]`** — a `file.md#section` link names a heading that is actually in
  that file.

**Why it is corpus-wide and not per-skill.** A link is a claim about the
*repository*, not about the skill's subject. A skill's own `verification/`
exercises its workflow on a case; nothing in that process ever resolves a path.
So ten broken links survived 53 skills' harnesses and were found only when
something looked across all of them at once (2026-09-22). Eight were the same
shape — a sibling skill addressed as though skills nested, `../bc/SKILL.md`
from inside `design-of-experiments/references/`, one `..` short. Two were
`indexes/topic-index.md` in capsules that never built one, which is a content
gap a path check surfaces and a prose review had not.

**The anchor half earns its place separately.** A section can move out of a file
while every path still resolves. That happened the same day: "The lead" moved
into `capsule-tutorial-contract.md` and a skill kept pointing at the file it had
left. Paths alone would have called that fine.

**What it does not check**, and what stays human: whether the link is
*pointing at the right thing*. A link to the wrong existing file passes both
gates.

### What it must not flag

Three exclusions, each of which was a false positive before it was one:

- **Code is not a link.** Fenced blocks and inline spans are masked. Both
  tutorial skeletons carry illustrative `](...)` inside ```markdown fences, and
  `skills/typst` documents the Markdown it migrates *from* with spans like
  `` `[t](u)` `` — the first version reported `u`, `f`, `url` and `img.png` as
  broken.
- **Untracked files.** Only `git ls-files` output is checked. `paper/` is
  gitignored working notes whose links are written relative to the repository
  root; checking it produced 13 phantom failures.
- **Experiment fixtures.** `experiments/*/subject/` and `.../archive/` are
  skipped. The `finishing` fixture is a site generator whose pages deliberately
  cannot reach each other — **those broken links are the defect under test**,
  and a corpus check that "fixed" them would destroy the experiment. The
  experiments' own prose is still checked.

`sh tools/check-links-mutations.sh` demonstrates the gates can fail: a broken
path, a broken anchor, a live anchor that must *not* fire, and a link inside
code that must stay invisible.

---

## 8. Checklist before marking a skill verified

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
- [ ] **Each of the three `bc` signals tested in ISOLATION**, not just together.
      A marker planted with the `fails` counter untouched (banner still printed,
      exit still 0) must make `run.sh` exit 1 — that is the only way to see the
      `grep -qF '*** FAIL'` clause work, and it is how the broken `grep -q` form
      hid in 8 harnesses. Likewise a syntax error for the status clause and a
      suppressed banner for the banner clause.
- [ ] Python imports stdlib only; every RNG stream is seeded from an argument.
- [ ] Capsule graph checks read `tsort` stderr for `cycle`.
- [ ] **For a capsule graph (§5a): `sh validation/mutation-check.sh` exits 0**,
      and the `falsifiable coverage` line is reported alongside it. Hygiene
      checks pass on a graph with a deleted or invented edge; only node text
      catches those, and only where node text exists.
- [ ] **`python3 build/check-edge-evidence.py` exits 0**, with every soft hit
      adjudicated in `validation/edge-evidence-ignore.txt` and no stale entry.
- [ ] Lean cores are Mathlib-free or labelled as requiring it.
- [ ] **`python3 build/check-lean-cores.py` exits 0** (§5b): no `sorry` /
      `admit` / `axiom` / `native_decide`, no `declaration uses 'sorry'`, and
      every `lean_status` claiming machine verification resolves to a
      declaration or an existing section. `lean` exits 0 on all of those.
- [ ] **`sh validation/lean-mutation-check.sh` exits 0** — five of its six
      planted defects are invisible to `lean` itself.
- [ ] `verification/README.md` has the step→check→result table and the
      folded-back findings (or "no correctness fix needed in the skill body").
- [ ] The README Verification table has a row with the tool versions and the
      headline numbers.
- [ ] **For a behaviour-modification skill: a displacement table with no empty
      cells** (§7) — every `SKILL.md` section names the default behaviour it
      displaces, and the verification shows that default failing.
- [ ] Prose that displaces no nameable default has been moved out of
      `SKILL.md` into `references/` or `verification/README.md`.
- [ ] **`version:` bumped in the same commit**, at the right level
      ([`skill-versioning.md`](skill-versioning.md)): MAJOR if the skill was
      *wrong*, MINOR if a statement changed or grew, PATCH if nothing semantic.
      A release-verification fix does not bump anything — that is how the skill
      reached `1.0.0`.
- [ ] **`sh tools/check-skills.sh` exits 0** — version shape, `name:` matching
      the directory, the `.claude/skills` symlink resolving, the changelog
      contract, and (§7a) **every relative link and `#anchor` resolving**. A built skill
      nobody wired in is shelfware; a dangling link looks wired and is worse.
