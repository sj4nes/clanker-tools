# Balancing an Equation When the Electrons Move

> Generated from the `chemistry-foundations` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The chemistry, the prerequisite order, and
> every calculation come from that capsule.

Most equations balance by counting atoms. A **redox** equation has a second
ledger: electrons move from one species to another, and the count of electrons
lost must equal the count gained. This tutorial walks the capsule's short chain
for that second ledger, ending in a fully balanced permanganate–iron equation:

`oxidation_number_rules` → `oxidation_reduction` → `oxidizing_reducing_agent` →
`half_reaction` → **`balancing_redox_half_reactions`**.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/chemistry-foundations/tutorial/balancing-a-redox-equation.md` for
the interactive walk, or
`upmd --ci --all skills/chemistry-foundations/tutorial/balancing-a-redox-equation.md`
to run every calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so
`upmd --ci -b capstone skills/chemistry-foundations/tutorial/balancing-a-redox-equation.md`
runs the whole chain up to the capstone. Two blocks call `lean` to
kernel-check an arithmetic instance; if `lean` is not on your `PATH` they print
`SKIP` and pass.

## What you need first

Integer arithmetic and the idea of a signed charge; that a `chemical_formula`
names atom counts and an `ion` carries a net charge; and
`balancing_chemical_equations` (choosing coefficients so atoms match) and
`conservation_of_charge` (total charge matches too). These are the capsule's
upstream nodes — assumed here, not rebuilt.

Redox bookkeeping is all integers: there are no dimensional checks in this
tutorial, only atom counts, charge sums, and electron counts that must come out
equal.

---

## 0. Setup

The worked example is the reaction of permanganate with iron(II) in acid, the
capsule's own case (`half_reaction` and `balancing_redox_half_reactions`
entries):

`MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O`

```bash [name:setup]
export RXN="MnO4- + 5 Fe2+ + 8 H+  ->  Mn2+ + 5 Fe3+ + 4 H2O   (acidic solution)"
echo "target reaction: $RXN"
```

## 1. Oxidation numbers

An oxidation number is a bookkeeping charge assigned to each atom by a fixed
priority hierarchy (`oxidation_number_rules`): a free element is 0; a monatomic
ion equals its charge; F is −1; O is −2 (except peroxides and OF₂); H is +1 with
nonmetals; and **the weighted sum over a species equals its total charge**. That
last rule is what pins down every unknown. The check solves for the metal in two
species of the target reaction.

Rule: **`Σᵢ (countᵢ · oxidation_numberᵢ) = species charge`**

```bash [name:chk_oxidation_number_rules, deps:setup]
awk 'BEGIN{
  # Fe2O3, neutral:  2*x + 3*(-2) = 0        (capsule special case -> +3)
  fe = (0 - 3*(-2)) / 2
  # MnO4^-, charge -1:  x + 4*(-2) = -1
  mn = (-1 - 4*(-2)) / 1
  printf "Fe in Fe2O3 : %+d   (capsule special case: +3)\n", fe
  printf "Mn in MnO4- : %+d\n", mn
  printf "Mn in Mn2+  : %+d   (monatomic ion = its charge)\n", 2
  if (fe==3 && mn==7) print "PASS: the sum rule fixes each unknown oxidation number"
  else { print "FAIL"; exit 1 }
}'
```

Manganese enters the reaction as `+7` in `MnO₄⁻` and leaves as `+2` in `Mn²⁺`.

## 2. Oxidation, reduction, and the agents

`oxidation_reduction`: oxidation is loss of electrons and a **rise** in oxidation
number; reduction is gain and a **fall**. They always occur together — every
electron lost by one species is gained by another. The species that is *reduced*
is the `oxidizing_reducing_agent` called the **oxidizing agent** (it took the
electrons); the species *oxidized* is the **reducing agent**. The agent's own
change is opposite to the change it drives. The check tracks the oxidation-number
change for the capsule's Zn/Cu²⁺ case and for the target reaction.

Rule: **oxidation: Δ(oxidation number) > 0; reduction: Δ < 0; the two are equal and opposite in electrons**

```bash [name:chk_oxidation_reduction, deps:chk_oxidation_number_rules]
awk 'BEGIN{
  # capsule special case:  Zn + Cu2+ -> Zn2+ + Cu
  dZn = 2 - 0        # 0 -> +2
  dCu = 0 - 2        # +2 -> 0
  printf "Zn  0 -> +2  (delta %+d : loses e-, OXIDIZED  -> Zn is the reducing agent)\n", dZn
  printf "Cu +2 ->  0  (delta %+d : gains e-, REDUCED   -> Cu2+ is the oxidizing agent)\n", dCu
  # target reaction:
  dMn = 2 - 7        # MnO4- (+7) -> Mn2+ (+2)
  dFe = 3 - 2        # Fe2+ (+2) -> Fe3+ (+3)
  printf "Mn +7 -> +2  (delta %+d : REDUCED, gains 5 e-  -> MnO4- is the oxidizing agent)\n", dMn
  printf "Fe +2 -> +3  (delta %+d : OXIDIZED, loses 1 e- -> Fe2+ is the reducing agent)\n", dFe
  if (dZn==2 && dCu==-2 && dMn==-5 && dFe==1) print "PASS: oxidation-number change = electrons moved"
  else { print "FAIL"; exit 1 }
}'
```

Manganese drops by 5 (gains 5 electrons); each iron rises by 1 (loses 1). Those
counts have to be reconciled.

## 3. Half-reactions

A `half_reaction` writes the oxidation or the reduction on its own, with the
electrons shown explicitly, and it is balanced only when **both** mass and
charge match across the arrow. In acid you balance oxygen with `H₂O` and
hydrogen with `H⁺`. The check verifies the capsule's two half-reactions for this
system.

Oxidation: **`Fe²⁺ → Fe³⁺ + e⁻`**   Reduction: **`MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O`**

```bash [name:chk_half_reaction, deps:chk_oxidation_reduction]
awk 'BEGIN{
  # oxidation:  Fe2+ -> Fe3+ + e-
  o_mass = (1 == 1)                       # Fe: 1 = 1
  o_chg  = (2 == 3 + (-1))                # +2 = +3 + (-1)
  # reduction (acidic):  MnO4- + 8 H+ + 5 e-  ->  Mn2+ + 4 H2O
  r_mn = (1 == 1)
  r_o  = (4 == 4*1)                       # 4 O on left, 4 in 4 H2O
  r_h  = (8 == 4*2)                       # 8 H+ on left, 8 in 4 H2O
  r_chg = ((-1) + 8*1 + 5*(-1) == 2 + 0)  # LHS charge = RHS charge
  printf "oxidation  Fe2+ -> Fe3+ + e-              : mass %s  charge %s\n", (o_mass?"ok":"BAD"), (o_chg?"ok":"BAD")
  printf "reduction  MnO4- +8H+ +5e- -> Mn2+ +4H2O  : Mn %s  O %s  H %s  charge %s\n", (r_mn?"ok":"BAD"),(r_o?"ok":"BAD"),(r_h?"ok":"BAD"),(r_chg?"ok":"BAD")
  if (o_mass && o_chg && r_mn && r_o && r_h && r_chg) print "PASS: each half-reaction balances mass AND charge"
  else { print "FAIL"; exit 1 }
}'
```

Each half stands on its own — atoms balanced, and the electrons carrying exactly
the charge difference.

## 4. Oxidation number is not formal charge

Both are electron-bookkeeping devices, and the capsule flags confusing them as
the top misuse of `oxidation_number_rules` (`edges/relations.tsv`:
`commonly_confused_with formal_charge`). The difference is how a shared bond is
split: an **oxidation number** gives both bonding electrons to the more
electronegative atom; a **formal charge** splits every bond evenly. This aside
is not part of the redox chain — `formal_charge` has its own prerequisites
(Lewis structures) — but the arithmetic contrast is worth one runnable line: the
capsule's formal-charge instance for carbon monoxide, `FC = V − N_lone − ½N_bond`.

Rule: **`FC = (valence e⁻) − (lone-pair e⁻) − ½(bonding e⁻)`,  `Σ FC = species charge`**

```bash [name:lean_formal_charge_contrast, deps:setup]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/fc.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 9 (formal_charge)
-- CO:  C has FC 4 - 2 - 6/2 = -1 ;  O has FC 6 - 2 - 6/2 = +1 ;  sum = 0 (neutral CO)
example : ((4 - 2 - 6/2 : Int) + (6 - 2 - 6/2)) = 0 := by decide
EOF
if lean "$d/fc.lean"; then
  echo "PASS: Lean kernel verified the CO formal charges (-1 and +1) sum to 0"
  echo "      -- a different split of the same bonds; oxidation numbers of C and O in CO are +2 and -2"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Same molecule, same bonds, two different bookkeeping conventions — for CO the
formal charges are `−1/+1` and the oxidation numbers are `+2/−2`. Use oxidation
numbers for redox.

## 5. Balancing by half-reactions

`balancing_redox_half_reactions`: balance each half (atoms, then O with `H₂O`, H
with `H⁺`, charge with `e⁻`), **scale each half so the electrons are equal**,
then add — the electrons cancel and drop out. The reduction half here consumes
5 electrons; the oxidation half releases 1; so the oxidation half is multiplied
by 5. The Lean beat kernel-checks the electron equality and the net-charge sum.

Rule: **electrons lost = electrons gained** (scale the halves to the lowest common multiple)

```bash [name:chk_balancing_redox_half_reactions, deps:chk_half_reaction]
awk 'BEGIN{
  e_red = 5      # reduction half: 5 e- consumed
  e_ox  = 1      # oxidation half: 1 e- released
  k_red = 5 / e_red      # x1
  k_ox  = 5 / e_ox       # x5
  printf "reduction half x %d ,  oxidation half x %d\n", k_red, k_ox
  printf "electrons:  %d gained  vs  %d lost\n", e_red*k_red, e_ox*k_ox
  if (e_red*k_red == e_ox*k_ox) print "PASS: 5 electrons gained = 5 electrons lost (capsule: 5 = 5x1)"
  else { print "FAIL"; exit 1 }
}'
```

```bash [name:lean_balancing_redox_half_reactions, deps:chk_balancing_redox_half_reactions]
command -v lean >/dev/null 2>&1 || { echo "SKIP: lean not on PATH"; exit 0; }
d=$(mktemp -d)
cat > "$d/redox.lean" <<'EOF'
-- capsule validation/derivation-checks.lean, check 8 (balancing_redox_half_reactions)
-- electrons lost = electrons gained:  reduction gains 5, oxidation is 5 x (1 lost)
example : ((5 : Int) * 1) = 1 * 5 := by decide
-- net charge, left vs right, of the added equation:
--   (-1) + 5*(2) + 8*(1)  =  5*(3) + 2  =  17
example : (((-1 : Int) + 5*2 + 8*1)) = (5*3 + 2) := by decide
EOF
if lean "$d/redox.lean"; then
  echo "PASS: Lean kernel verified 5*1 = 1*5 (electron balance) and the net charge 17 = 17"
else
  echo "FAIL: lean rejected the snippet"; rm -rf "$d"; exit 1
fi
rm -rf "$d"
```

Multiply, add, cancel the electrons: `MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O`.

---

## Capstone: check the whole equation

You have both ledgers. Verify the final equation on every count at once — each
element, the net charge, and that no free electrons are left.

```bash [name:capstone, deps:"chk_balancing_redox_half_reactions | lean_balancing_redox_half_reactions | lean_formal_charge_contrast"]
awk 'BEGIN{
  # MnO4- + 5 Fe2+ + 8 H+  ->  Mn2+ + 5 Fe3+ + 4 H2O
  mnL=1;         mnR=1
  feL=5;         feR=5
  oL =4;         oR =4*1          # 4 O in 4 H2O
  hL =8;         hR =4*2          # 8 H in 4 H2O
  qL = (-1) + 5*2 + 8*1           # MnO4- , 5 Fe2+ , 8 H+
  qR = 2 + 5*3 + 4*0              # Mn2+ , 5 Fe3+ , 4 H2O
  e_left_in_equation = 0

  printf "Mn: %d = %d\n", mnL, mnR
  printf "Fe: %d = %d\n", feL, feR
  printf "O : %d = %d\n", oL, oR
  printf "H : %d = %d\n", hL, hR
  printf "net charge:  %+d  =  %+d\n", qL, qR
  printf "free electrons remaining in the equation: %d\n", e_left_in_equation

  ok = (mnL==mnR && feL==feR && oL==oR && hL==hR && qL==qR && e_left_in_equation==0)
  if (ok) print "PASS: every element balances, net charge balances (+17 = +17), no electrons left over"
  else { print "FAIL"; exit 1 }
}'
```

If the capstone prints `PASS`, both ledgers closed: the atom counts match
(mass), the charge sums match at `+17` on each side, and the five electrons
manganese gained are exactly the five the iron atoms gave up — so they cancelled
and left a clean equation.

## Where to go next

- The full [`chemistry-foundations`](../SKILL.md) capsule. Redox in Release 0.1
  is **balancing only** — `electrochemistry` (cells, standard electrode
  potentials, the Nernst equation, Faraday's laws) is out of scope, a future
  capsule (`scope.md`).
- `formal_charge`, `lewis_structure`, `octet_rule`, `vsepr` — the bonding feeder
  nodes, where the formal-charge aside in section 4 is properly developed
  (`indexes/topic-index.md`, the bonding band).
- `titration` and `equivalence_point` — a permanganate titration is a common
  way to *use* this balanced equation quantitatively.
- The sibling tutorials
  [`how-much-can-this-make.md`](how-much-can-this-make.md) (percent yield) and
  [`reaction-enthalpy-from-formation.md`](reaction-enthalpy-from-formation.md)
  (reaction enthalpy).
