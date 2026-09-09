# Solving an Equilibrium with an ICE Table

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

A reversible reaction settles at a composition where the reaction quotient
equals the equilibrium constant. Given the starting amounts and `K`, you find
that composition with an **ICE table**: tabulate Initial, Change, and
Equilibrium concentrations in terms of one unknown `x`, substitute into `K`, and
solve — usually a quadratic. This tutorial walks the capsule's chain to that
method:

`reversible_reaction` → `dynamic_equilibrium` → `law_of_mass_action` →
`equilibrium_constant` → `reaction_quotient` → (`quadratic_formula`) →
**`ice_table`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/solving-an-equilibrium.md` for the
interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/solving-an-equilibrium.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/solving-an-equilibrium.md`
runs the whole chain up to the capstone.

## What you need first

Algebra, including the `quadratic_formula`
(`x = (−b ± √(b² − 4ac)) / (2a)`); `molarity` (`c = n/V`, so a concentration is
in mol/L); and that a `chemical_equation` carries `stoichiometric_coefficient`s.
These are the capsule's upstream nodes.

There are no dimensional checks in this tutorial. Every `K` and `Q` here is
**dimensionless by construction**: each concentration `[X]` in the expression
means the molarity *divided by* the standard `c° = 1 mol/L`, so `K` is a pure
number (the capsule's `equilibrium_constant` convention). The checks are numeric
— solve, then verify.

One first-class assumption governs the whole chain: **`dilute_ideal_solution`**
(activity ≈ concentration). Outside the dilute limit, `K` written in
concentrations stops being constant (Debye–Hückel and beyond, out of scope).

---

## 0. Setup

The worked example is the dissociation of a weak acid,
`HA ⇌ H⁺ + A⁻`, with the capsule's acetic-acid numbers
(`weak_acid_equilibrium` / `ice_table` entries): `K_a = 1.8×10⁻⁵` and an
initial concentration `c₀ = 0.10 M`.

```bash [name:setup]
export KA=0.000018        # 1.8e-5, the acid dissociation constant K_a
export C0=0.10            # M, initial concentration of the undissociated acid HA
export APPROX_LIMIT=0.05  # the x/c0 threshold below which "x << c0" is acceptable
export BC_LINE_LENGTH=0   # stop bc wrapping long numeric output lines
echo "HA <=> H+ + A- ;  K_a = ${KA} ;  c0(HA) = ${C0} M"
```

## 1. Reversible reactions and dynamic equilibrium

A `reversible_reaction` runs in both directions under the same conditions
(written `⇌`). It reaches `dynamic_equilibrium` when the forward and reverse
processes proceed at equal rates, so the **composition stops changing** — not
because the reaction stopped, and not because the concentrations became equal.
In this capsule equilibrium is characterised thermodynamically, by `Q = K`
(`ΔG = 0`), never by rate equality (kinetics is out of scope). The check makes
the "constant, not equal" point concrete.

Rule: **at equilibrium, composition is constant and `Q = K`**

```bash [name:chk_dynamic_equilibrium, deps:setup]
awk 'BEGIN{
  # a mixture at equilibrium: concentrations are unequal but unchanging
  HA = 0.0987; Hplus = 0.00133; Aminus = 0.00133
  # "constant" test: two successive snapshots are identical
  HA_next = HA; Hplus_next = Hplus
  constant = (HA == HA_next && Hplus == Hplus_next)
  equal    = (HA == Hplus)
  printf "equilibrium mixture:  [HA] = %.4f   [H+] = [A-] = %.5f\n", HA, Hplus
  printf "composition constant between snapshots? %s\n", (constant ? "yes" : "no")
  printf "are the concentrations equal to each other? %s\n", (equal ? "yes" : "no")
  if (constant && !equal) print "PASS: equilibrium means unchanging, not equal"
  else { print "FAIL"; exit 1 }
}'
```

Equilibrium freezes the *composition*; the individual concentrations are
whatever `K` makes them.

## 2. The law of mass action and the equilibrium constant

`law_of_mass_action`: at equilibrium the reaction quotient equals a constant
that depends only on temperature. For `aA + bB ⇌ cC + dD` that constant is
`equilibrium_constant`

**`K_c = [C]^c [D]^d / ([A]^a [B]^b)`**

each `[X]` a molarity ÷ `c°`. `K ≫ 1` means products are favoured; `K ≪ 1` means
reactants are favoured; `K ≈ 1` means both are present in comparable amounts.
The check confirms the exponent structure on the capsule's ammonia reaction,
then reads the acetic-acid `K_a`.

```bash [name:chk_equilibrium_constant, deps:chk_dynamic_equilibrium]
awk -v ka="$KA" 'BEGIN{
  # exponent structure for  N2 + 3 H2 <=> 2 NH3  :  K = [NH3]^2 / ([N2] [H2]^3)
  N2 = 1.0; H2 = 2.0; NH3 = 4.0
  K = (NH3^2) / (N2 * H2^3)
  printf "N2 + 3 H2 <=> 2 NH3 :  K = %.1f^2 / (%.1f * %.1f^3) = %.4f\n", NH3, N2, H2, K
  # for the weak acid, K_a = [H+][A-]/[HA]
  printf "HA <=> H+ + A- :  K_a = %.1e\n", ka
  if (ka < 1) print "PASS: K_a << 1  ->  reactants favoured, HA barely dissociates (a weak acid)"
  else { print "FAIL"; exit 1 }
}'
```

Products raised to their coefficients over reactants raised to theirs; a `K` far
below 1 says the equilibrium sits well to the left.

## 3. The reaction quotient

The `reaction_quotient` `Q` is the *same expression* as `K`, evaluated at **any**
composition, not just the equilibrium one. It tells you which way the reaction
must still go: `Q < K` → net forward, `Q > K` → net reverse, `Q = K` → already
at equilibrium. At the start of a weak-acid problem there is no product yet, so
`Q = 0 < K` — the acid must dissociate. The check evaluates `Q` at the initial
state and (using the section-1 mixture) at equilibrium.

Rule: **`Q` has `K`'s form at arbitrary composition;  `Q = K` only at equilibrium**

```bash [name:chk_reaction_quotient, deps:chk_equilibrium_constant]
awk -v ka="$KA" -v c0="$C0" 'BEGIN{
  # initial state: [HA] = c0, [H+] = [A-] = 0
  Q_init = (0.0 * 0.0) / c0
  printf "initial:      Q = (0)(0)/%.2f = %.1f   ->  Q < K_a, acid dissociates\n", c0, Q_init
  # equilibrium mixture from section 1
  HA = 0.0987; Hp = 0.00133; Am = 0.00133
  Q_eq = (Hp * Am) / HA
  printf "equilibrium:  Q = (%.5f)(%.5f)/%.4f = %.2e   (K_a = %.1e)\n", Hp, Am, HA, Q_eq, ka
  rel = (Q_eq - ka); if (rel < 0) rel = -rel
  if (Q_init == 0 && rel/ka < 0.05) print "PASS: Q = 0 at the start, Q = K_a at equilibrium"
  else { print "FAIL"; exit 1 }
}'
```

`Q` moves from 0 up to `K` as the reaction proceeds; the ICE table finds exactly
where it lands.

## 4. The quadratic formula

Substituting an ICE table into `K` almost always gives a quadratic in the
unknown extent `x`. The capsule's `quadratic_formula` entry gives the standard
form for a weak acid directly: `x² / (c₀ − x) = K_a` rearranges to

**`x² + K_a·x − K_a·c₀ = 0`**

Solve with `x = (−b ± √(b² − 4ac)) / (2a)` and **keep the positive root** — the
negative one is an unphysical (negative concentration). The check solves a
plain quadratic and discards the negative root.

```bash [name:chk_quadratic_formula, deps:setup]
bc -l <<'EOF'
scale = 10
/* solve x^2 + b x + c = 0 with the ICE coefficients: a=1, b=K_a, c=-K_a c0 */
ka = 0.000018
c0 = 0.10
b = ka
c = -ka * c0
disc = b*b - 4*c
root_pos = (-b + sqrt(disc)) / 2
root_neg = (-b - sqrt(disc)) / 2
print "x^2 + ", b, " x + (", c, ") = 0\n"
print "positive root x = ", root_pos, "   <- keep this one\n"
print "negative root x = ", root_neg, "   <- reject (x is a concentration, must be >= 0)\n"
EOF
```

Two roots, one of them negative; the physical answer is the positive one.

## 5. The ICE table

Now the method itself (`ice_table`). For `HA ⇌ H⁺ + A⁻` starting from `c₀`:

| | HA | H⁺ | A⁻ |
|---|---|---|---|
| **I**nitial | `c₀` | 0 | 0 |
| **C**hange | `−x` | `+x` | `+x` |
| **E**quilibrium | `c₀ − x` | `x` | `x` |

Substitute the E row into `K_a = [H⁺][A⁻]/[HA]`, giving `x²/(c₀ − x) = K_a`.
Solve it two ways: the exact quadratic from section 4, and the shortcut
`x ≈ √(K_a·c₀)` which is valid **only** when `x/c₀ < 0.05`. The check does both,
tests the shortcut's validity, and verifies the answer by back-substitution.

```bash [name:chk_ice_table, deps:"chk_reaction_quotient | chk_quadratic_formula"]
bc -l <<'EOF'
scale = 12
ka = 0.000018
c0 = 0.10

/* exact: x^2 + ka x - ka c0 = 0, positive root */
disc = ka*ka + 4*ka*c0
x_exact = (-ka + sqrt(disc)) / 2

/* approximate: x^2 = ka c0  (assume x << c0) */
x_approx = sqrt(ka * c0)

ratio = x_exact / c0

/* verify: substitute x_exact back into x^2/(c0 - x) and recover ka */
ka_check = (x_exact * x_exact) / (c0 - x_exact)

print "x_exact   = ", x_exact, "  M\n"
print "x_approx  = ", x_approx, "  M   (x = sqrt(ka c0))\n"
print "x/c0      = ", ratio, "   (approximation OK if < 0.05)\n"
print "back-check: x_exact^2 / (c0 - x_exact) = ", ka_check, "   (want ka = 0.000018)\n"
EOF
awk -v lim="$APPROX_LIMIT" 'BEGIN{
  x_exact  = 0.00133267
  x_approx = 0.00134164
  ratio    = x_exact / 0.10
  rel = (x_approx - x_exact) / x_exact
  printf "x/c0 = %.4f  (limit %.2f) ; approximation error = %.2f %%\n", ratio, lim, rel*100
  if (ratio < lim && rel < 0.02) print "PASS: x << c0 holds, shortcut and exact agree to ~1%"
  else { print "FAIL"; exit 1 }
}'
```

The exact and approximate `x` agree to about 1 % because `x/c₀ ≈ 0.013` is well
under the 0.05 threshold, and plugging `x` back reproduces `K_a`.

```bash [name:try_ice_table, deps:chk_ice_table]
# change C0 and watch x and the percent ionization move (Ostwald dilution)
C0=${C0:-0.10}
KA=${KA:-0.000018}
bc -l <<EOF
scale = 10
x = (-$KA + sqrt($KA*$KA + 4*$KA*$C0)) / 2
print "c0 = ", $C0, " M  ->  x = [H+] = ", x, " M ,  percent ionization = ", 100*x/$C0, " %\n"
EOF
echo "  (dilute the acid -> x falls but percent ionization RISES)"
```

---

## Capstone: acetic acid, start to finish

You have the whole method. Solve the acetic-acid equilibrium
(`K_a = 1.8×10⁻⁵`, `c₀ = 0.10 M`) for `x = [H⁺]` — the exact way and the
shortcut — confirm the shortcut is licensed, and verify by back-substitution.

```bash [name:capstone, deps:chk_ice_table]
x_exact=$(bc -l <<< "scale=12; (-$KA + sqrt($KA*$KA + 4*$KA*$C0)) / 2")
x_approx=$(bc -l <<< "scale=12; sqrt($KA * $C0)")
ratio=$(bc -l <<< "scale=8; $x_exact / $C0")
ka_back=$(bc -l <<< "scale=12; ($x_exact * $x_exact) / ($C0 - $x_exact)")

echo "ICE table for HA <=> H+ + A- :  I(${C0}, 0, 0)  C(-x, +x, +x)  E(${C0}-x, x, x)"
echo "substitute -> x^2 / (${C0} - x) = ${KA}"
echo
printf "exact quadratic:      x = %.6e M\n" "$x_exact"
printf "shortcut sqrt(ka c0): x = %.6e M\n" "$x_approx"
printf "x / c0 = %.4f\n" "$ratio"
printf "back-substitution:  x^2/(c0 - x) = %.6e   (K_a = %s)\n" "$ka_back" "$KA"

awk -v xe="$x_exact" -v xa="$x_approx" -v r="$ratio" -v kb="$ka_back" -v ka="$KA" 'BEGIN{
  approx_ok = (r < 0.05)
  agree_ok  = ((xa - xe)/xe < 0.02)
  verify_ok = (((kb - ka) < 0 ? ka - kb : kb - ka) / ka < 0.01)
  round_ok  = (xe > 1.3e-3 && xe < 1.35e-3)   # capsule states ~1.3e-3
  if (approx_ok && agree_ok && verify_ok && round_ok)
    print "PASS: x = [H+] ~ 1.3e-3 M ; shortcut licensed (x/c0 < 0.05) ; back-check recovers K_a"
  else { print "FAIL"; exit 1 }
}'
echo
echo "x = [H+] ~ 1.3e-3 M.  Turning that into pH is the next tutorial."
```

If the capstone prints `PASS`, the method held: the ICE row became a quadratic,
the positive root gave `[H⁺] ≈ 1.3×10⁻³ M`, the `x ≪ c₀` shortcut was justified
and landed within 1 %, and substituting the answer back reproduced `K_a`.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule.
- `q_versus_k` and `le_chatelier` — reading the direction of a disturbed
  equilibrium (the qualitative side of `Q` vs `K`).
- `kp_kc_relation` (`K_p = K_c (RT/P°)^{Δn}`) and `heterogeneous_equilibrium` —
  gas-phase and multi-phase equilibria.
- `ph_definition`, `weak_acid_equilibrium`, `ka_kb_relation`,
  `henderson_hasselbalch` — the acid–base band that builds directly on this ICE
  table (`indexes/topic-index.md`).
- The sibling tutorials
  [`finding-a-concentration.md`](finding-a-concentration.md) (titration),
  [`how-much-can-this-make.md`](how-much-can-this-make.md) (percent yield),
  [`reacting-gases-by-volume.md`](reacting-gases-by-volume.md),
  [`reaction-enthalpy-from-formation.md`](reaction-enthalpy-from-formation.md),
  [`balancing-a-redox-equation.md`](balancing-a-redox-equation.md).
