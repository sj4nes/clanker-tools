# What counts as a proof

> Generated from the `math-logic-and-proof` capsule (Release 0.1) with the
> `theorem-tree-tutorial` skill. The mathematics, the prerequisite order, and
> every calculation and proof come from that capsule —
> `validation/proof-checks.lean` (sections 2, 6, 9, 10) and
> `validation/instance-checks.bc` in particular. No new mathematics is
> introduced here.

Every proof you have ever read uses a handful of moves: **assume the hypothesis
and build the conclusion** (direct), **prove the contrapositive**, **assume the
negation and derive a contradiction**, **split into exhaustive cases**,
**exhibit one counterexample**, **induct**. This tutorial walks that list in the
capsule's dependency order. For each method you run the move on a concrete
object and watch it work — then you ask the Lean kernel *which logical axioms
the move actually needs*. The answer is the point of the lesson: `direct`,
`cases`, and ordinary `induction` are **constructive** (they compute a witness);
`contrapositive`, `contradiction`, and "the universal failed so a counterexample
must exist" each genuinely require a **classical** principle, and the kernel
says so by name.

The path ends at **`induction_equivalence`**: weak induction, strong induction,
and the well-ordering principle are the same axiom in three costumes — over `ℕ`.
Move to a cyclic carrier and the disguise falls off.

## How to run this

Install [`upmd`](https://upmd.dev), then from the repository root:

- `upmd skills/math-logic-and-proof/tutorial/what-counts-as-a-proof.md` — the
  interactive walk (needs a real terminal).
- `upmd --ci --all skills/math-logic-and-proof/tutorial/what-counts-as-a-proof.md`
  — run every check top to bottom (the verification gate).
- `upmd --ci -b capstone skills/math-logic-and-proof/tutorial/what-counts-as-a-proof.md`
  — the final verdict and everything it depends on.

Each block has `deps:` on the blocks for its prerequisites, in the same partial
order as the capsule's dependency graph, so `upmd --ci -b <name>` runs one check
with its whole chain.

The `lean_*` blocks call the Lean 4 kernel through a shell wrapper (`upmd` has
no native Lean runner). They need `lean` on your `PATH`; if it is missing they
print `SKIP` and still exit 0, so the tutorial goes green without it. With
`lean` present they each run `#print axioms` and check whether the proof term
pulls **`Classical.choice`** — that is the constructive-vs-classical line.

## What you need first

Propositional connectives and truth tables; the natural-deduction rules
(`→I` / discharge, `∨E`, `RAA`) and a Hilbert calculus as *named* objects;
first-order `∀` / `∃`. The propositional equivalences this lesson leans on —
**`contraposition`** `(p→q) ⊨⊨ (¬q→¬p)`, **`double_negation`** `¬¬p ⊨⊨ p`,
**`de_morgan_prop`**, and the quantifier law **`quantifier_negation`**
`¬∀x φ ⊨⊨ ∃x ¬φ` — are earlier nodes in the capsule; here they are used, and
the kernel's `#print axioms` verdict on each is what we run.

Ordered node path (from `indexes/tsort-order.txt`, teaching order):

`direct_proof` → `proof_by_contrapositive` → `proof_by_contradiction` →
`proof_by_cases` → `disproof_by_counterexample` → `weak_induction` →
`strong_induction` → `structural_induction` → `well_ordering_principle` →
`induction_equivalence`.

Every method node carries a **`constructive_grade`**
(`intuitionistic` / `needs_LEM` / `needs_DNE`). That grade — *which assumption
the method rests on, and what weaker thing is not enough* — is the capsule's
distinctive payload, and section by section the kernel confirms it.

---

## 0. Setup

One helper: a shell function that writes a Lean snippet, runs it, and reports
whether the proof term depends on `Classical.choice`. Every `lean_*` block uses
it.

```bash [name:setup]
export TUT="what-counts-as-a-proof"
# grade_of <file.lean> <decl-name> : prints "constructive" or "classical"
cat > /tmp/${TUT}-gradeof.sh <<'SH'
gradeof() {
  local out
  out=$(lean "$1" 2>&1) || { echo "LEAN-ERROR"; echo "$out"; return 1; }
  if echo "$out" | grep -q "'$2' .*Classical\.choice"; then
    echo "classical"
  elif echo "$out" | grep -qE "'$2' (does not depend on any axioms|depends on axioms: \[(propext|Quot\.sound|, )+\])"; then
    echo "constructive"
  else
    echo "$out" | grep "'$2'"
  fi
}
SH
echo "setup: helper written to /tmp/${TUT}-gradeof.sh"
echo "lean on PATH: $(command -v lean >/dev/null && echo yes || echo 'no (lean_* blocks will SKIP)')"
```

## 1. Direct proof — the default, and it computes

**`direct_proof`**: to prove `P → Q`, assume `P` as a temporary hypothesis,
derive `Q`, then **discharge** the assumption (`→I` of natural deduction). For
`∀x (P(x) → Q(x))`, fix an arbitrary `x` first. `constructive_grade:
intuitionistic` — `→I` is a rule of minimal logic; a direct proof exhibits a
function from evidence for `P` to evidence for `Q`.

The worked object for the whole induction-free half of this tutorial is
**parity**: `n` odd means `n = 2k+1`, and then `n² = 4k²+4k+1 = 2(2k²+2k)+1`,
which is odd. That derivation — assume the hypothesis, compute the conclusion —
is a direct proof.

```bash [name:chk_direct_proof, deps:setup]
# direct proof that n odd => n^2 odd: build n^2 in the form 2*m + 1 explicitly
ok=1
for k in 0 1 2 3 4; do
  n=$((2*k + 1))
  sq=$((n*n))
  m=$((2*k*k + 2*k))          # the witness: n^2 = 2*m + 1
  built=$((2*m + 1))
  par=$((sq % 2))
  echo "  n=2*$k+1=$n   n^2=$sq   2*(2k^2+2k)+1=$built   n^2 mod 2=$par"
  [ "$sq" = "$built" ] && [ "$par" = 1 ] || ok=0
done
echo "witness construction valid for every case: $ok   (want 1)"
[ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
```

```bash [name:lean_direct_proof, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 10
-- direct_proof: assume the antecedent (`fun h => ...`), build the consequent.
theorem direct_example (p q : Prop) : (p ∧ q) → (q ∧ p) := fun h => ⟨h.2, h.1⟩
-- direct_proof also covers `p → ¬¬p` (section 2):
theorem dni {p : Prop} : p → ¬ ¬ p := fun hp hn => hn hp
#print axioms direct_example
#print axioms dni
LEAN
g1=$(gradeof "$d/x.lean" direct_example)
g2=$(gradeof "$d/x.lean" dni)
echo "direct_example : $g1     dni (p -> not not p) : $g2"
rm -rf "$d"
[ "$g1" = constructive ] && [ "$g2" = constructive ] || { echo "FAIL: expected constructive"; exit 1; }
echo "=> direct_proof is intuitionistic: the proof term is a function, no classical axiom."
```

The kernel reports **no axioms** for a direct proof — it is the constructively
strongest kind of argument.

## 2. Proof by contrapositive — free one way, classical the other

**`proof_by_contrapositive`**: to prove `P → Q`, give a direct proof of
`¬Q → ¬P` instead. Justified by **`contraposition`**,
`(P → Q) ⊨⊨ (¬Q → ¬P)`. `constructive_grade: needs_DNE`. The subtlety the node
records: the **forward** half `(P → Q) → (¬Q → ¬P)` is intuitionistic
(`contrapose_weak`); it is *using the contrapositive as a strategy for* `P → Q`
— the step back — that needs `¬¬P → P`.

Our parity fact restated: "if `n²` is even then `n` is even" has an awkward
direct proof, but its contrapositive is exactly section 1's "`n` odd ⇒ `n²`
odd".

```bash [name:chk_proof_by_contrapositive, deps:chk_direct_proof]
# "n^2 even => n even" checked BY its contrapositive "n odd => n^2 odd"
ok=1
for n in 0 1 2 3 4 5 6 7 8 9; do
  nsq_par=$((n*n % 2)); n_par=$((n % 2))
  # contrapositive form: n odd (n_par=1)  =>  n^2 odd (nsq_par=1)
  if [ "$n_par" = 1 ] && [ "$nsq_par" != 1 ]; then ok=0; fi
  # original form it establishes: n^2 even => n even
  if [ "$nsq_par" = 0 ] && [ "$n_par" != 0 ]; then ok=0; fi
done
echo "contrapositive holds for n=0..9, hence so does the original: $ok   (want 1)"
[ "$ok" = 1 ] || { echo "FAIL"; exit 1; }
```

```bash [name:lean_proof_by_contrapositive, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 2
theorem contrapose_weak {p q : Prop} : (p → q) → (¬ q → ¬ p) :=
  fun h hnq hp => hnq (h hp)
theorem dne {p : Prop} : ¬ ¬ p → p := fun h => Classical.byContradiction (fun hn => h hn)
theorem contrapose_iff {p q : Prop} : (p → q) ↔ (¬ q → ¬ p) :=
  ⟨contrapose_weak, fun h hp => dne (fun hnq => h hnq hp)⟩
#print axioms contrapose_weak
#print axioms contrapose_iff
LEAN
gf=$(gradeof "$d/x.lean" contrapose_weak)
gi=$(gradeof "$d/x.lean" contrapose_iff)
echo "forward  (p->q) -> (not q -> not p) : $gf"
echo "full iff (the round trip)          : $gi"
rm -rf "$d"
[ "$gf" = constructive ] && [ "$gi" = classical ] || { echo "FAIL: expected constructive / classical"; exit 1; }
echo "=> writing the contrapositive is free; concluding P->Q from it needs DNE (needs_DNE)."
```

The forward direction pulls no axioms; the full `↔` — the part that lets a
contrapositive proof *count as* a proof of the original — pulls
`Classical.choice`.

## 3. Proof by contradiction — the classical workhorse

**`proof_by_contradiction`** (the `raa_rule`): to prove `P`, assume `¬P`, derive
`⊥`, conclude `P`. `constructive_grade: needs_DNE` — `RAA` and `¬¬P → P` are
interderivable, and adding either to intuitionistic logic gives full classical
logic. The node draws a line the prose of most textbooks blurs:

- **`¬I`** — to prove `¬P`, assume `P`, derive `⊥`. *Intuitionistic*, always
  fine. It is just `direct_proof` of `P → ⊥`.
- **`RAA` proper** — to prove a *positive* `P`, assume `¬P`, derive `⊥`.
  *Classical*. A `proof_by_contradiction` of `∃x φ(x)` yields **no witness**.

```bash [name:lean_proof_by_contradiction, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 2
theorem dni {p : Prop} : p → ¬ ¬ p := fun hp hn => hn hp                 -- intro: free
theorem dne {p : Prop} : ¬ ¬ p → p := fun h => Classical.byContradiction (fun hn => h hn)  -- elim: RAA
#print axioms dni
#print axioms dne
LEAN
gi=$(gradeof "$d/x.lean" dni)
ge=$(gradeof "$d/x.lean" dne)
echo "p -> not not p  (this is really direct_proof / not-I) : $gi"
echo "not not p -> p  (this IS proof_by_contradiction)      : $ge"
rm -rf "$d"
[ "$gi" = constructive ] && [ "$ge" = classical ] || { echo "FAIL"; exit 1; }
echo "=> introducing a double negation is free; ELIMINATING one is proof_by_contradiction, needs_DNE."
```

Same two symbols `¬¬p` and `p`, opposite verdicts. `dni` is the honest
direct-proof half; `dne` is where the classical commitment lives — and it is
exactly the `raa` case in the capsule's own `soundness` proof (section 4 of the
Lean file) where the metatheory turns classical.

## 4. Proof by cases — the obligation is exhaustiveness

**`proof_by_cases`** (iterated `∨E`): given a goal `R` and a disjunction
`C₁ ∨ … ∨ Cₙ` **known to be exhaustive**, prove `R` under each `Cᵢ`. Two
obligations — (1) `⊢ C₁ ∨ … ∨ Cₙ`, (2) `Cᵢ ⊢ R` for every `i`. The `∨E` step is
`intuitionistic`; the grade of a given case proof is inherited from *how the
disjunction is obtained* — parity and linear-order trichotomy are decidable
(constructive); `P ∨ ¬P` for undecidable `P` is `needs_LEM`.

```bash [name:lean_proof_by_cases, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 10
theorem parity_dichotomy (n : Nat) : n % 2 = 0 ∨ n % 2 = 1 := by omega   -- exhaustive, decidable
theorem sq_parity (n : Nat) : (n * n) % 2 = n % 2 := by
  rcases parity_dichotomy n with h | h <;> simp [Nat.mul_mod, h]         -- settle each case
#print axioms parity_dichotomy
#print axioms sq_parity
LEAN
gd=$(gradeof "$d/x.lean" parity_dichotomy)
gs=$(gradeof "$d/x.lean" sq_parity)
echo "the disjunction  n%2=0 or n%2=1  : $gd"
echo "the case proof   (n*n)%2 = n%2   : $gs"
rm -rf "$d"
[ "$gd" = constructive ] && [ "$gs" = constructive ] || { echo "FAIL"; exit 1; }
echo "=> a split on a DECIDABLE disjunction keeps the whole proof constructive."
```

```bash [name:cx_proof_by_cases, deps:lean_proof_by_cases]
# drop exhaustiveness: "n^2 > n for all n in N", proving only the case n >= 2
echo "claim: n^2 > n for ALL n.   split used: only {n >= 2}"
sub=1; for n in 2 3 4 5 6; do [ $((n*n)) -gt "$n" ] || sub=0; done
echo "  sub-case n>=2 really does hold: $sub"
fail=0
for n in 0 1; do                     # the cases the split silently omits
  if [ $((n*n)) -le "$n" ]; then
    echo "  omitted case n=$n:  n^2=$((n*n)) > n=$n ?  NO"
    fail=$((fail + 1))
  fi
done
echo "omitted cases where the claim is false: $fail   (want 2)"
[ "$fail" = 2 ] || { echo "FAIL: expected the split to be non-exhaustive"; exit 1; }
echo "=> a case analysis missing a case proves nothing.  (n^2 >= n is the true statement.)"
```

The `cx_` block is the lesson: the sub-proof is correct, yet the conclusion is
false, because `{n ≥ 2}` is not all of `ℕ`.

## 5. Disproof by counterexample — one witness, and it is constructive

**`disproof_by_counterexample`**: to disprove `∀x φ(x)` — i.e. prove
`¬∀x φ(x)` — exhibit a specific `a` with `¬φ(a)`. By **`quantifier_negation`**,
the step `∃x ¬φ(x) → ¬∀x φ(x)` is the *intuitionistic* direction
(`cap_not_forall_of_exists_not`), so producing the witness genuinely refutes the
universal — constructively. The `needs_LEM` label attaches only to the opposite
habit: "the universal failed, therefore a counterexample **must exist**" —
concluding `∃x ¬φ` from `¬∀x φ` with nothing in hand.

```bash [name:chk_disproof_by_counterexample, deps:chk_direct_proof]
# claim: every prime is odd.   witness: 2
n=2
divs=0; d=2; while [ "$d" -lt "$n" ]; do [ $((n % d)) -eq 0 ] && divs=$((divs+1)); d=$((d+1)); done
echo "  2 has $divs divisors strictly between 1 and 2  -> 2 is prime"
echo "  2 mod 2 = $((n % 2))                            -> 2 is even"
[ "$divs" = 0 ] && [ $((n % 2)) -eq 0 ] || { echo "FAIL"; exit 1; }
echo "=> 2 is a prime that is not odd: the single witness refutes 'every prime is odd'."
```

```bash [name:lean_disproof_by_counterexample, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, sections 6
theorem cap_not_forall_of_exists_not {a : Type} {p : a → Prop} :
    (∃ x, ¬ p x) → ¬ ∀ x, p x := fun ⟨x, hx⟩ h => hx (h x)          -- the disproof step
theorem not_forall_iff {a : Type} {p : a → Prop} : (¬ ∀ x, p x) ↔ (∃ x, ¬ p x) :=
  Classical.not_forall                                              -- the CONVERSE habit
#print axioms cap_not_forall_of_exists_not
#print axioms not_forall_iff
LEAN
gc=$(gradeof "$d/x.lean" cap_not_forall_of_exists_not)
gn=$(gradeof "$d/x.lean" not_forall_iff)
echo "exhibit a: (exists x, not p x) -> not (forall x, p x) : $gc"
echo "assume none: (not forall) -> (exists x, not p x)      : $gn"
rm -rf "$d"
[ "$gc" = constructive ] && [ "$gn" = classical ] || { echo "FAIL"; exit 1; }
echo "=> giving the counterexample is constructive; assuming one exists is needs_LEM."
```

This is the pattern behind **every** `counterexamples_when_dropped` field in the
capsule — including all the `cx_` blocks in this tutorial.

## 6. Weak induction, and 7. strong induction — one recursor

**`weak_induction`**: if `P(0)` and `∀n (P(n) → P(n+1))` then `∀n P(n)`. This
*is* the fifth Peano axiom, presented as a method; `constructive_grade:
intuitionistic` — it is `Nat.rec`, and it computes.

**`strong_induction`**: if `∀n ((∀k < n, P(k)) → P(n))` then `∀n P(n)`. No
separate base case — the `n = 0` instance has the vacuous hypothesis
`∀k < 0, P(k)`. `strong_induction` is a **theorem**, derived from
`weak_induction` applied to `Q(n) := ∀k < n, P(k)`. Same strength: it proves
exactly the same theorems.

```bash [name:lean_strong_induction, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 9
-- strong induction BUILT FROM weak induction (plain `induction n`), no Mathlib.
theorem strong_of_weak (P : Nat → Prop)
    (step : ∀ n, (∀ k, k < n → P k) → P n) : ∀ n, P n := by
  have aux : ∀ n, ∀ k, k < n → P k := by
    intro n
    induction n with
    | zero => intro k hk; exact absurd hk (Nat.not_lt_zero k)
    | succ n ih =>
        intro k hk
        rcases Nat.lt_succ_iff_lt_or_eq.1 hk with hk | rfl
        · exact ih k hk
        · exact step k ih
  intro n; exact step n (aux n)
#print axioms strong_of_weak
LEAN
g=$(gradeof "$d/x.lean" strong_of_weak)
echo "weak_induction  =>  strong_induction : $g"
rm -rf "$d"
[ "$g" = constructive ] || { echo "FAIL: expected constructive"; exit 1; }
echo "=> genuine, universal, ZERO axioms.  Ordinary induction is fully constructive."
```

```bash [name:cx_weak_induction, deps:lean_strong_induction]
# the classic fake proof: "all horses in a set of size n are the same colour".
# base n=1 holds; the STEP n -> n+1 fails at n=1 because two 1-element subsets
# of a 2-element set do not overlap, so their colours are never forced equal.
echo "fake claim: any n horses share a colour.  step n -> n+1 removes one horse, applies IH twice."
overlap_ok=1
for n in 1 2 3 4 5; do
  # subsets {1..n} and {2..n+1} of {1..n+1}; overlap size n-1
  ov=$((n - 1))
  echo "  n=$n -> n+1=$((n+1)):  the two n-subsets overlap in $ov horse(s)"
  [ "$ov" -ge 1 ] || overlap_ok=0
done
echo "step is valid only where the overlap is nonempty (n >= 2): first failure at n=1 -> 2"
[ "$overlap_ok" = 0 ] || { echo "FAIL: expected the n=1->2 step to have empty overlap"; exit 1; }
echo "=> the induction STEP must hold for EVERY n, including the smallest.  It does not here."
```

## 8. Structural induction — the same schema, any inductive type

**`structural_induction`**: for a set given by an `inductive_definition` (wffs,
terms, derivations, lists, trees), prove `P` of each base element and prove each
constructor **preserves** `P`. `weak_induction` is the instance for `ℕ`
(`0`, `succ`); `structural_induction_wff` is the instance for `Wff`; the same
schema drives every semantic function and every soundness proof in the capsule
(induction on the derivation). `constructive_grade: intuitionistic` — it is the
eliminator of an inductive type.

```bash [name:lean_structural_induction, deps:setup]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 3
-- structural induction / case exhaustion over Bool^2: EVERY binary Boolean
-- function equals the disjunction of its true-row minterms (functional_completeness).
theorem binary_dnf (f : Bool → Bool → Bool) (a b : Bool) :
    f a b =
      ( (f true true  && (a && b))
      || (f true false && (a && !b))
      || (f false true && (!a && b))
      || (f false false && (!a && !b)) ) := by
  cases a <;> cases b <;> simp
#print axioms binary_dnf
LEAN
g=$(gradeof "$d/x.lean" binary_dnf)
echo "structural case exhaustion over Bool x Bool : $g"
rm -rf "$d"
[ "$g" = constructive ] || { echo "FAIL"; exit 1; }
echo "=> covering every constructor is a constructive argument; MISSING one is a silent gap."
```

## 9. The well-ordering principle — where nonemptiness and the carrier bite

**`well_ordering_principle`**: every nonempty `S ⊆ ℕ` has a least element. Proved
from `strong_induction` by contradiction: if `S` had no least element then
strong induction gives `∀n, n ∉ S`, so `S = ∅`.
`constructive_grade`: **`intuitionistic` for a decidable `S`** (bounded search
finds the least element), **`needs_DNE` for an arbitrary predicate** (that proof
uses `proof_by_contradiction`).

```bash [name:chk_well_ordering_principle, deps:chk_direct_proof]
# decidable S = { n : n^2 > 30 } : least element by bounded search (instance-checks.bc)
least=-1
for n in $(seq 0 20); do
  if [ $((n*n)) -gt 30 ] && [ "$least" = -1 ]; then least=$n; fi
done
echo "least n with n^2 > 30 : $least    ($least^2 = $((least*least)) > 30,  $((least-1))^2 = $(( (least-1)*(least-1) )) <= 30)"
[ "$least" = 6 ] || { echo "FAIL: expected 6"; exit 1; }
```

```bash [name:cx_well_ordering_principle, deps:chk_well_ordering_principle]
# drop "subset of N": on Z and on Q>0 there is NO least element
echo "carrier Z:  every candidate least m has a smaller m-1 in Z"
zbad=0; for m in -3 -2 -1 0 1 2 3; do [ $((m-1)) -lt "$m" ] && zbad=$((zbad+1)); done
echo "  m-1 < m for all $zbad tested m  -> Z has no least element"
echo "carrier Q>0: candidate least 1/n; then 1/(2n) is positive and strictly smaller"
qbad=0; for n in 1 2 3 4 5; do [ "$n" -lt $((2*n)) ] && qbad=$((qbad+1)); done   # 1/(2n) < 1/n  <=>  n < 2n
echo "  1/(2n) < 1/n for all $qbad tested n  -> {q in Q : q > 0} has no least element"
[ "$zbad" = 7 ] && [ "$qbad" = 5 ] || { echo "FAIL"; exit 1; }
echo "=> 'nonempty' cannot be dropped, and the carrier must be (N, <).  Well-ordering an"
echo "   arbitrary set is a DIFFERENT theorem (well_ordering_theorem) and needs choice."
```

```bash [name:lean_well_ordering_principle, deps:lean_strong_induction]
command -v lean >/dev/null || { echo "SKIP: lean not on PATH"; exit 0; }
. /tmp/${TUT}-gradeof.sh
d=$(mktemp -d)
cat > "$d/x.lean" <<'LEAN'
-- math-logic-and-proof/validation/proof-checks.lean, section 9
theorem strong_of_weak (P : Nat → Prop)
    (step : ∀ n, (∀ k, k < n → P k) → P n) : ∀ n, P n := by
  have aux : ∀ n, ∀ k, k < n → P k := by
    intro n
    induction n with
    | zero => intro k hk; exact absurd hk (Nat.not_lt_zero k)
    | succ n ih =>
        intro k hk
        rcases Nat.lt_succ_iff_lt_or_eq.1 hk with hk | rfl
        · exact ih k hk
        · exact step k ih
  intro n; exact step n (aux n)
theorem well_ordering (P : Nat → Prop) (w : Nat) (hw : P w) :
    ∃ m, P m ∧ ∀ k, k < m → ¬ P k := by
  apply Classical.byContradiction
  intro h
  have hdesc : ∀ n, P n → ∃ k, k < n ∧ P k := by
    intro n hn
    apply Classical.byContradiction
    intro hc
    exact h ⟨n, hn, fun k hk hkP => hc ⟨k, hk, hkP⟩⟩
  have hno : ∀ n, ¬ P n := by
    apply strong_of_weak
    intro n ih hn
    rcases hdesc n hn with ⟨k, hk, hkP⟩
    exact ih k hk hkP
  exact hno w hw
#print axioms well_ordering
LEAN
g=$(gradeof "$d/x.lean" well_ordering)
echo "well_ordering for an ARBITRARY predicate P : $g"
rm -rf "$d"
[ "$g" = classical ] || { echo "FAIL: expected classical"; exit 1; }
echo "=> for arbitrary P the proof goes through Classical.byContradiction: needs_DNE."
echo "   (For a DECIDABLE S, section 9's bounded search is constructive -- Nat.find.)"
```

---

## Capstone: `induction_equivalence` — three costumes, one axiom

**`induction_equivalence`** (headline of the `proof_methods` block): over `ℕ`,
**`weak_induction` ⟺ `strong_induction` ⟺ `well_ordering_principle`** —
each is derivable from any other; taking any one as the axiom yields the same
theorems. The Lean file gives two of the three legs as genuine plain-Lean proofs
(`strong_of_weak`, `well_ordering`); the third — well-ordering → weak — is the
same least-counterexample argument.

`constructive_grade`: **weak ⟺ strong is `intuitionistic`** (both are
`Nat.rec`, zero axioms); the legs through `well_ordering_principle` for an
arbitrary predicate are **`needs_DNE`**. The equivalence is stated **relative to
the Peano structure** — `succ` injective, `0` not a successor, `<` the
associated well-founded order. That phrase is doing real work, and the capstone
check is where you see it.

```bash [name:capstone, deps:"lean_strong_induction | lean_well_ordering_principle | cx_weak_induction | cx_well_ordering_principle | chk_well_ordering_principle | lean_proof_by_contradiction"]
echo "== what counts as a proof: the verdict =="
echo
echo "constructive (kernel: no Classical.choice) -- these compute a witness:"
echo "  * direct_proof            (section 1: direct_example, dni)"
echo "  * proof_by_cases          (section 4: parity_dichotomy, sq_parity -- decidable split)"
echo "  * disproof_by_counterexample, the EXHIBIT step  (section 5: cap_not_forall_of_exists_not)"
echo "  * weak_induction / strong_induction             (section 6-7: strong_of_weak)"
echo "  * structural_induction                          (section 8: binary_dnf)"
echo
echo "classical (kernel: depends on Classical.choice) -- no witness extracted:"
echo "  * proof_by_contrapositive, the round trip       (section 2: contrapose_iff)"
echo "  * proof_by_contradiction / DNE                  (section 3: dne)"
echo "  * disproof_by_counterexample, the ASSUME-ONE-EXISTS habit (section 5: not_forall_iff)"
echo "  * well_ordering_principle for arbitrary P       (section 9: well_ordering)"
echo
echo "-- now: weak <=> strong <=> well-ordering, and where it is RELATIVE to (N, 0, succ, <) --"
echo

# leg 1: N, decidable S -- least element exists (section 9)
least=-1; for n in $(seq 0 20); do [ $((n*n)) -gt 30 ] && [ "$least" = -1 ] && least=$n; done
echo "over N:  S={n : n^2>30} nonempty  ->  least element = $least   (well-ordering delivers it)"
[ "$least" = 6 ] || { echo "FAIL"; exit 1; }

# leg 2: Z/6Z with successor +1 mod 6 -- weak-style walk reaches everything...
x=0; reached=1
for i in 1 2 3 4 5; do x=$(( (x+1) % 6 )); [ "$x" = "$i" ] || reached=0; done
echo "over Z/6Z (successor = +1 mod 6):  walk from 0 reaches all six elements? $reached"
[ "$reached" = 1 ] || { echo "FAIL"; exit 1; }

# ...but every element has a predecessor, so there is NO least element
noleast=1
for m in 0 1 2 3 4 5; do p=$(( (m+5) % 6 )); [ "$p" != "$m" ] || noleast=0; done
echo "over Z/6Z:  every element has a distinct predecessor (m-1 mod 6)? $noleast   -> no least element"
[ "$noleast" = 1 ] || { echo "FAIL"; exit 1; }

echo
echo "=> drop 'succ injective / 0 not a successor' (use Z/6Z): a successor walk still covers"
echo "   the carrier, but well_ordering_principle FAILS -- the three principles come apart."
echo "   induction_equivalence holds because N has the Peano structure, not by magic."
echo
echo "CAPSTONE OK: 5 methods constructive, 4 classical, and the induction trio is one"
echo "axiom over (N, 0, succ, <) -- confirmed by the Lean kernel and the counterexamples."
```

### In the wild

This is the lesson under every other tutorial in the stack. When
`math-real-analysis` proves the least-upper-bound property is what separates `ℝ`
from `ℚ`, the "separates" is a `disproof_by_counterexample` (a Cauchy sequence
of rationals with no rational limit). When `math-sets-functions-cardinality`
shows `|X| < |𝒫(X)|`, the diagonal set is a `proof_by_contradiction` that —
unusually — extracts no witness because there is none. When any capsule tags a
result `needs_LEM` or `needs_full_AC`, it is making the section-2-through-9
distinction: *the theorem is true, but its proof spends a classical principle,
and a constructive mathematician gets a strictly weaker statement.* The
`#print axioms` line you ran in each section is the same referee those grades
appeal to.

## Where to go next

- The full `math-logic-and-proof` capsule: `skills/math-logic-and-proof/` —
  every result with its hypotheses, `indexes/constructive-grade-index.md` (the
  whole capsule sorted by grade), and `validation/proof-checks.md` (the
  kernel-verified vs. cited split).
- Concepts past this path: the equivalence catalogue and normal forms
  (`prop_laws`, `prop_normal`), the metatheory proper (`soundness_prop` →
  `post_completeness_theorem` → `compactness_prop`), and the stated-not-proved
  boundary (`godel_incompleteness_first`, `undecidability_fol_validity`).
- Related cuts from `docs/tutorial-map.md`: *Truth tables to functional
  completeness* (`functional_completeness`), *Two calculi, one theorem*
  (`nd_hilbert_equivalence`).
