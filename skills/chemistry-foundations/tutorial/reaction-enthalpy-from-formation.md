# The Enthalpy of a Reaction You Never Ran

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

Burning methane releases 890 kJ per mole — a number you can get without a
calorimeter, without ever running the reaction, from a table of *formation*
enthalpies. This tutorial walks the capsule's dependency chain from the mole up
to that result:

`amount_of_substance` → `conservation_of_mass` → `mole_ratio` →
`first_law_thermo` → `enthalpy` → `hess_law` → `standard_enthalpy_of_formation`
→ **`enthalpy_from_formation_enthalpies`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/reaction-enthalpy-from-formation.md`
for the interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/reaction-enthalpy-from-formation.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/reaction-enthalpy-from-formation.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

Algebra, logarithms, ratios, and summation notation; that atoms and elements
exist and are conserved in chemical change; and elementary energy/temperature
from physics. These are the capsule's discharged primitives (`si_units`,
`summation_notation`, `ratio_proportion`, `atom`, `atomic_structure`,
`atomic_number`, `element`, `ion`) — assumed here, not built.

The dimensional checks track exponents on the `[M, L, T, Θ, N]` basis — mass,
length, time, temperature, and **amount of substance** (`N`, the mole, a base
dimension in this capsule). A consistent relation prints `0 0 0 0 0` for
(left side − right side).

Two first-class regime nodes appear along the way and are named where they bite:
`heat_work_sign_convention` (`ΔU = q − w`) and `standard_state`
(`P° = 1 bar`, tables at 298.15 K).

---

## 0. Setup

These are the standard molar enthalpies of formation the capsule tabulates for
the methane-combustion example (kJ/mol, `standard_enthalpy_of_formation` entry),
and the reaction enthalpy it states as the answer.

```bash [name:setup]
export DHF_CH4=-74.8      # kJ/mol, dHf(CH4, g)
export DHF_O2=0           # kJ/mol, dHf(O2, g)  -- element in its standard form
export DHF_CO2=-393.5     # kJ/mol, dHf(CO2, g)
export DHF_H2O_L=-285.8   # kJ/mol, dHf(H2O, l)
export WANT_DHRXN=-890.3  # kJ/mol, the capsule's stated dH_rxn for CH4 + 2 O2 -> CO2 + 2 H2O(l)
echo "formation enthalpies loaded (kJ/mol): CH4=$DHF_CH4  O2=$DHF_O2  CO2=$DHF_CO2  H2O(l)=$DHF_H2O_L"
```

## 1. The mole

`amount_of_substance` (`n`, unit mole, dimension `N`) is the SI base quantity
that counts specified entities. It is tied to a raw count by the Avogadro
constant: `N = n · N_A`, with `N_A = 6.02214076×10²³ mol⁻¹` fixed exactly by the
2019 SI redefinition. `N` is a pure number (dimensionless); `N_A` carries `N⁻¹`,
so the product `n · N_A` is dimensionless — which is the whole point of the
check below. Every "convert through the mole" step downstream rides on this.

Formula: **`N = n N_A`**

```bash [name:chk_amount_of_substance, deps:setup]
bc -l <<'EOF'
/* exponents (m, l, t, th, n) for each quantity */
nm=0; nl=0; nt=0; nth=0; nn=1        /* amount n        -> N        */
am=0; al=0; at=0; ath=0; an=-1       /* Avogadro N_A    -> N^-1     */
bm=0; bl=0; bt=0; bth=0; bn=0        /* count N         -> 1        */
print bm-(nm+am)," ",bl-(nl+al)," ",bt-(nt+at)," ",bth-(nth+ath)," ",bn-(nn+an)," (want 0 0 0 0 0)\n"
EOF
```

The count equals amount times `N_A`, and the dimensions cancel to nothing — a
mole is a fixed *number*, not a mass or a volume.

## 2. Conservation of mass and charge

A `chemical_reaction` rearranges atoms among substances; it creates and destroys
nothing. `conservation_of_mass` says every element's atom count is identical on
both sides of the arrow (`Σ m(reactants) = Σ m(products)`), and
`conservation_of_charge` says the same for total charge. These two laws are the
entire basis for *balancing* an equation. The check takes the reaction this
whole tutorial builds toward and inventories its atoms.

Formula: **`Σ atoms(reactants) = Σ atoms(products)`**, element by element

```bash [name:chk_conservation_of_mass, deps:setup]
awk 'BEGIN{
  # CH4 + 2 O2  ->  CO2 + 2 H2O
  cL = 1;      cR = 1
  hL = 4;      hR = 2*2
  oL = 2*2;    oR = 2 + 2*1
  printf "C: %d = %d   H: %d = %d   O: %d = %d\n", cL, cR, hL, hR, oL, oR
  if (cL==cR && hL==hR && oL==oR) print "PASS: every element is conserved"
  else { print "FAIL: equation does not balance"; exit 1 }
}'
```

Carbon, hydrogen, and oxygen each balance — so the coefficients `1, 2, 1, 2` are
a legal balanced equation, not a guess.

## 3. Balancing and the mole ratio

Once an equation is balanced, its `stoichiometric_coefficient`s (`ν`) are the
fixed recipe. The `mole_ratio` reads amounts straight off them:
`n_B = n_A · (ν_B / ν_A)`. It is a ratio of *amounts*, never of masses. The check
uses the capsule's own worked case, ammonia synthesis `N₂ + 3H₂ → 2NH₃`.

Formula: **`n_B = n_A · (ν_B / ν_A)`**

```bash [name:chk_mole_ratio, deps:"chk_amount_of_substance | chk_conservation_of_mass"]
awk 'BEGIN{
  # N2 + 3 H2 -> 2 NH3 ; nuN2=1, nuH2=3, nuNH3=2
  nN2 = 1
  nH2  = nN2 * 3 / 1
  nNH3 = nN2 * 2 / 1
  printf "1 mol N2 needs %g mol H2 and gives %g mol NH3\n", nH2, nNH3
  if (nH2==3 && nNH3==2) print "PASS: amounts follow the coefficient ratio 1:3:2"
  else { print "FAIL"; exit 1 }
}'
```

The coefficients are a proportion between amounts — the conversion factor for
every stoichiometry calculation, including the formation-enthalpy sum at the end.

## 4. Heat, work, and the first law

Split the universe into a `system` and its `surroundings`. Energy crossing the
boundary is heat `q` or work `w`, and the capsule's sign convention
(`heat_work_sign_convention`) is `ΔU = q − w`: `q > 0` is heat *into* the
system, `w > 0` is work done *by* the system. `first_law_thermo` is then just
energy conservation for a closed system — `ΔU`, `q`, `w` all in joules
(`M L² T⁻²`). Watch the convention: some texts write `ΔU = q + w` and flip every
`w`.

Formula: **`ΔU = q − w`**

```bash [name:chk_first_law_thermo, deps:setup]
bc -l <<'EOF'
/* dU, q and w must all carry the SAME dimension (you cannot subtract dimensions);
   check dU against one of them -- an energy, M L^2 T^-2 -> (1, 2, -2, 0, 0). */
um=1; ul=2; ut=-2; uth=0; un=0     /* dU */
qm=1; ql=2; qt=-2; qth=0; qn=0     /* q  */
print um-qm," ",ul-ql," ",ut-qt," ",uth-qth," ",un-qn," (want 0 0 0 0 0)\n"
EOF
```

Internal energy change, heat, and work all carry energy dimensions — the
equation `ΔU = q − w` only adds quantities of the same kind.

## 5. Enthalpy

At constant pressure the useful bookkeeping quantity is `enthalpy`,
`H = U + P V` (imported from `physics-thermodynamics`). Its value is that
`ΔH = q_p` — the heat of a constant-pressure process — so a reaction run in an
open flask releases or absorbs exactly `ΔH`. `H` is an energy (`M L² T⁻²`);
`P V` must be too, and that is the check.

Formula: **`H = U + P V`**

```bash [name:chk_enthalpy, deps:chk_first_law_thermo]
bc -l <<'EOF'
/* U and P*V must each match [H]; check [H] against [P]+[V] (the capsule's form). */
hm=1; hl=2; ht=-2; hth=0; hn=0     /* H   -> M L^2 T^-2 */
pm=1; pl=-1; pt=-2; pth=0; pn=0    /* P   -> M L^-1 T^-2 */
vm=0; vl=3; vt=0; vth=0; vn=0      /* V   -> L^3 */
print hm-(pm+vm)," ",hl-(pl+vl)," ",ht-(pt+vt)," ",hth-(pth+vth)," ",hn-(pn+vn)," (want 0 0 0 0 0)\n"
EOF
```

`P V` carries energy dimensions, so `U + P V` is an energy and `H` is
well-formed.

## 6. State functions and Hess's law

`H` is a **state function**: it depends only on the current state, not the path
taken to reach it, so `∮ dH = 0` around any cycle. That single fact is
`hess_law`: the enthalpy change from reactants to products is the same whatever
sequence of steps you route it through, `ΔH_rxn = Σ ΔH(steps)`. You may add,
reverse, and scale known reactions and the enthalpies follow the same
operations. The Lean beat kernel-checks the capsule's arithmetic instance:
a two-step path `A→B→C` with `ΔH₁ = −30`, `ΔH₂ = −70` totals `−100`, and
reversing a step negates its `ΔH`.

Formula: **`ΔH_rxn = Σ ΔH(steps)`**  (any path, because `H` is a state function)

```bash [name:lean_hess_law, deps:chk_enthalpy]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/hess.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 1 (hess_law)
-- path independence: dH(A->C) = dH(A->B) + dH(B->C)
example : ((-30 : Int) + (-70)) = -100 := by decide
-- reversing a step flips its sign: dH(B->A) = -dH(A->B)
example : (-(-30 : Int)) = 30 := by decide
EOF
if lean "$d/hess.lean"; then
  echo "PASS: Lean kernel verified the path-independence instance (-30)+(-70) = -100"
  echo "      and the step-reversal instance -(-30) = 30"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Lean verified the *arithmetic* of adding and reversing steps — not that `H` is
actually a state function (that is the imported thermodynamics), only that the
bookkeeping is consistent.

## 7. Standard states and formation enthalpies

To tabulate enthalpies you need a common reference: the `standard_state`
(`P° = 1 bar`, solutes at `1 mol/L`, pure phases as themselves; tables at
298.15 K though the standard state does not fix temperature). The
`standard_enthalpy_of_formation` `ΔH_f°` is the enthalpy change to form **1 mol**
of a compound from its elements in their standard states — and for an element
already in its standard form (`O₂` gas, graphite, not diamond) it is **exactly
zero** by definition. The check asserts that zero and lists the tabulated values
the capstone will use.

Formula: **`ΔH_f°(element, standard form) ≡ 0`**

```bash [name:chk_standard_enthalpy_of_formation, deps:chk_enthalpy]
echo "dHf(O2,  g) = $DHF_O2      kJ/mol   <- element, standard form"
echo "dHf(CO2, g) = $DHF_CO2   kJ/mol"
echo "dHf(H2O, l) = $DHF_H2O_L   kJ/mol   (the gas value differs by the enthalpy of vaporisation)"
echo "dHf(CH4, g) = $DHF_CH4    kJ/mol"
awk -v x="$DHF_O2" 'BEGIN{
  if (x==0) print "PASS: the element reference O2(g) is exactly zero"
  else { print "FAIL"; exit 1 }
}'
```

Every compound value is measured against elements pinned at zero — which is what
makes the products-minus-reactants sum work.

## 8. Reaction enthalpy from formation enthalpies

Apply Hess's law to formation reactions and you get the payoff relation:

**`ΔH_rxn° = Σ n · ΔH_f°(products) − Σ n · ΔH_f°(reactants)`**

`n` is each species' stoichiometric coefficient (from section 3), `ΔH_f°` from
the table (section 7), the whole thing valid because `H` is a state function
(section 6). Both sides are a molar reaction enthalpy, `M L² T⁻² N⁻¹` — the
dimensional check — and the Lean beat kernel-checks the capsule's integer
instance of the CH₄ combustion sum, `(−393 + 2(−286)) − (−75 + 0) = −890`, plus
the scaling `2 × (−890) = −1780`.

```bash [name:chk_enthalpy_from_formation_enthalpies, deps:"lean_hess_law | chk_standard_enthalpy_of_formation | chk_mole_ratio"]
bc -l <<'EOF'
/* molar reaction enthalpy: M L^2 T^-2 N^-1 -> (1, 2, -2, 0, -1) ; n is dimensionless */
lm=1; ll=2; lt=-2; lth=0; ln=-1     /* dH_rxn (LHS)               */
rm=1; rl=2; rt=-2; rth=0; rn=-1     /* sum n dHf (RHS), n cancels  */
print lm-rm," ",ll-rl," ",lt-rt," ",lth-rth," ",ln-rn," (want 0 0 0 0 0)\n"
EOF
```

```bash [name:lean_enthalpy_from_formation_enthalpies, deps:chk_enthalpy_from_formation_enthalpies]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/dhf.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 2
-- CH4(g) + 2 O2(g) -> CO2(g) + 2 H2O(l), kJ/mol (integer instance):
-- dHf: CH4 -75, O2 0, CO2 -393, H2O(l) -286
example : (((-393 : Int) + 2*(-286)) - ((-75) + 2*0)) = -890 := by decide
-- scaling the equation by k = 2 scales dH_rxn by 2:
example : (2 * (-890 : Int)) = -1780 := by decide
EOF
if lean "$d/dhf.lean"; then
  echo "PASS: Lean kernel verified the products-minus-reactants sum = -890 (integer kJ/mol instance)"
  echo "      and the scaling instance 2 * -890 = -1780"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

The sum is dimensionally a molar enthalpy, and its arithmetic is
kernel-checked — not the tabulated `ΔH_f°` values themselves, and not that `H`
is a state function.

---

## Capstone: burn methane on paper

You have the whole chain. Compute `ΔH_rxn°` for
`CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)` from the capsule's formation enthalpies,
check it against the value the capsule states, then scale the equation.

```bash [name:capstone, deps:"chk_enthalpy_from_formation_enthalpies | lean_enthalpy_from_formation_enthalpies"]
# dH_rxn = [1*dHf(CO2) + 2*dHf(H2O,l)] - [1*dHf(CH4) + 2*dHf(O2)]
dhrxn=$(echo "scale=4; (1*($DHF_CO2) + 2*($DHF_H2O_L)) - (1*($DHF_CH4) + 2*($DHF_O2))" | bc -l)
echo "dH_rxn = [1*(${DHF_CO2}) + 2*(${DHF_H2O_L})] - [1*(${DHF_CH4}) + 2*(${DHF_O2})]"
echo "       = ${dhrxn} kJ/mol"
echo "capsule states: ${WANT_DHRXN} kJ/mol"

diff=$(echo "scale=4; d = $dhrxn - ($WANT_DHRXN); if (d < 0) d = -d; d" | bc -l)
awk -v d="$diff" 'BEGIN{
  if (d < 0.05) print "PASS: matches the capsule value within 0.05 kJ/mol"
  else { print "FAIL: off by " d " kJ/mol"; exit 1 }
}'

# scale the balanced equation by 2 -> dH_rxn scales by 2 (state-function bookkeeping)
scaled=$(echo "scale=4; 2 * $dhrxn" | bc -l)
echo
echo "2 CH4(g) + 4 O2(g) -> 2 CO2(g) + 4 H2O(l):  dH_rxn = ${scaled} kJ/mol"
echo "  (Lean-checked integer instance: 2 * -890 = -1780)"
```

If the capstone prints `PASS`, every link held: the mole and the coefficient
ratio fed the sum, the first law and enthalpy made `ΔH` the right quantity, and
Hess's law — `H` as a state function — is what let you get a combustion enthalpy
from a table instead of a flame.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule — solution and gas
  stoichiometry, equilibrium, acid–base, redox, all with regimes and checks.
- The other route to `ΔH_rxn` in the capsule: `enthalpy_from_bond_enthalpies`
  (`ΔH_rxn ≈ Σ D(broken) − Σ D(formed)`) — an *approximation* using averaged
  bond energies, and `bond_enthalpy`, `covalent_bond`, `lewis_structure` behind
  it.
- `heat_of_reaction_calorimetry` (`q_rxn = − q_calorimeter`) — measuring `ΔH_rxn`
  directly, the thing this tutorial let you skip.
- `standard_conditions_stp`, `calorimetry`, `specific_heat_capacity` — the rest
  of the thermochemistry band in `indexes/topic-index.md`.
