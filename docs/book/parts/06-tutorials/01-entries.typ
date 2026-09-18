// GENERATED FILE — DO NOT EDIT.
//   source:    skills/*/tutorial/*.md
//   generator: docs/book/tools/gen-tutorials.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit the tutorials, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, tutorialentry

= Chemistry tutorials

#note[14 tutorials from 2 capsules, 133 runnable blocks between them.]

== #raw("chemistry-foundations")

#tutorialentry([How Much Can This Reaction Actually Make?], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [A balanced equation is a recipe in #emph[moles], but you weigh reactants in #emph[grams] and you never get quite as much product as the recipe promises. This tutorial walks the capsule's dependency chain from the atomic mass scale up to a #strong[percent yield]—the fraction of the theoretical maximum a real prep delivers:]),
    ([runs], [13 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/how-much-can-this-make.md")]),
  ))
#tutorialentry([Reacting Gases by Volume], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [For gases you rarely weigh anything. You measure a pressure, a volume, and a temperature, and the ideal-gas law turns that into an amount—which the balanced equation then converts to any other species. At fixed temperature and pressure the shortcut is even cleaner: gas #emph[volumes] react in the same ratio as the coefficients. This tutorial walks the capsule's chain to that result:]),
    ([runs], [8 runnable blocks #sym.dot.c calls #raw("bc"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/reacting-gases-by-volume.md")]),
  ))
#tutorialentry([Finding an Unknown Concentration by Titration], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [You have a solution of something and you need to know how concentrated it is. Titration answers that: run in a reagent of #emph[known] concentration until it has exactly consumed the unknown, read the volume delivered, and the balanced equation does the rest. This tutorial walks the capsule's solutions chain to that calculation:]),
    ([runs], [7 runnable blocks #sym.dot.c calls #raw("bc"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/finding-a-concentration.md")]),
  ))
#tutorialentry([The Enthalpy of a Reaction You Never Ran], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [Burning methane releases 890 kJ per mole—a number you can get without a calorimeter, without ever running the reaction, from a table of #emph[formation] enthalpies. This tutorial walks the capsule's dependency chain from the mole up to that result:]),
    ([runs], [11 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/reaction-enthalpy-from-formation.md")]),
  ))
#tutorialentry([Balancing an Equation When the Electrons Move], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [Most equations balance by counting atoms. A #strong[redox] equation has a second ledger: electrons move from one species to another, and the count of electrons lost must equal the count gained. This tutorial walks the capsule's short chain for that second ledger, ending in a fully balanced permanganate–iron equation:]),
    ([runs], [8 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/balancing-a-redox-equation.md")]),
  ))
#tutorialentry([Solving an Equilibrium with an ICE Table], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [A reversible reaction settles at a composition where the reaction quotient equals the equilibrium constant. Given the starting amounts and #raw("K"), you find that composition with an #strong[ICE table]: tabulate Initial, Change, and Equilibrium concentrations in terms of one unknown #raw("x"), substitute into #raw("K"), and solve—usually a quadratic. This tutorial walks the capsule's chain to that method:]),
    ([runs], [8 runnable blocks #sym.dot.c calls #raw("bc"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/solving-an-equilibrium.md")]),
  ))
#tutorialentry([Predicting the pH of an Acid—and Holding It with a Buffer], [#raw("chemistry-foundations") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#raw("pH") is just #raw("−log₁₀[H⁺]"), but where #raw("[H⁺]") comes from depends on the acid. A strong acid gives it to you directly. A weak acid makes you solve an equilibrium. A #strong[buffer]—a weak acid mixed with its conjugate base—pins the pH near #raw("pK_a") and resists change, and the Henderson–Hasselbalch equation reads it straight off the ratio. This tutorial walks the capsule's acid–base chain:]),
    ([runs], [10 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-foundations/tutorial/predicting-ph.md")]),
  ))
== #raw("chemistry-electrochemistry")

#tutorialentry([How Much Do You Make Per Amp-Hour?], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [Electrolysis is a conversion between two ledgers: #strong[coulombs] through the wire and #strong[moles] of product at the electrode. The Faraday constant is the exchange rate, the balanced half-reaction sets how many electrons each formula unit costs, and Faraday's law turns a current and a clock into a mass. This tutorial walks the capsule's chain to that law and to what it tells you about making hydrogen:]),
    ([runs], [11 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/per-amp-hour.md")]),
  ))
#tutorialentry([What Does It Cost to Make a Kilogram?], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#raw("per-amp-hour.md") told you how many #emph[coulombs] a product costs. This tutorial multiplies that by the #emph[voltage]—and the voltage is never just #raw("E°_cell"). Thermodynamics sets a floor (#raw("ΔG = −zFE")), then the oxygen electrode's sluggish kinetics and the electrolyte's resistance pile extra volts on top. The result is the #strong[specific energy consumption], in kWh per kilogram:]),
    ([runs], [11 runnable blocks #sym.dot.c 3 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/kwh-per-kilogram.md")]),
  ))
#tutorialentry([Why the Chlorine Plant Makes Chlorine, Not Oxygen], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [Electrolyse brine and the anode has a choice: oxidise chloride to #raw("Cl₂"), or oxidise water to #raw("O₂"). The standard potentials say #strong[oxygen] should win (#raw("E°(O₂) = 1.23 V < E°(Cl₂) = 1.36 V")). Every chlor-alkali plant on Earth makes #strong[chlorine]. This tutorial follows the capsule's chain to why—overpotential inverts the thermodynamic order—and then sizes a real cell line:]),
    ([runs], [9 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/chlorine-not-oxygen.md")]),
  ))
#tutorialentry([An Iron Flow Battery for the Homestead], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [A flow battery stores its energy as two tanks of dissolved salt and delivers power through a separate stack of cells—so you size the #strong[duration] and the #strong[power] independently. The famous chemistry is all-vanadium, but for a small off-grid installation the practical one is #strong[all-iron]: iron chloride is cheap, abundant, and about as hazardous as plant fertiliser. This tutorial sizes one:]),
    ([runs], [11 runnable blocks #sym.dot.c 3 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/iron-flow-battery.md")]),
  ))
#tutorialentry([Hydrogen as a Battery], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [Electrolyse water when power is cheap, store the hydrogen, and run the cell backwards as a fuel cell when power is scarce. The storage is astonishingly compact and barely self-discharges—but the round trip throws away most of the energy, because you pay the oxygen electrode's overpotential #strong[going both ways]. This tutorial builds the water-electrolysis process and its reverse, then decides when hydrogen beats a flow battery for a homestead:]),
    ([runs], [9 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/hydrogen-as-a-battery.md")]),
  ))
#tutorialentry([The Voltage Isn't Fixed], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#raw("E°_cell") is a table value—the cell voltage with every species at unit activity. A real cell is never at unit activity, and its voltage moves with the concentrations. The #strong[Nernst equation] is the rule for that motion, and it explains three things at once: why a pH meter reads pH, why you can build a battery from nothing but a concentration difference, and why a flow battery can't be run all the way to empty or full.]),
    ([runs], [9 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/the-voltage-isnt-fixed.md")]),
  ))
#tutorialentry([The Zinc–Iron Alternative], [#raw("chemistry-electrochemistry") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#raw("iron-flow-battery.md") built the all-iron flow battery—cheap, low-hazard, but low energy density. The #strong[zinc–iron] battery keeps most of the cost and safety advantages, runs at a higher voltage (so the tanks are smaller), and swaps one catch for another: instead of parasitic hydrogen, it plates zinc metal, which limits how deeply and how long you can charge. This short tutorial is the comparison:]),
    ([runs], [8 runnable blocks #sym.dot.c 1 of them a Lean core #sym.dot.c calls #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/chemistry-electrochemistry/tutorial/zinc-iron-alternative.md")]),
  ))

= Mathematics tutorials

#note[5 tutorials from 4 capsules, 93 runnable blocks between them.]

== #raw("math-logic-and-proof")

#tutorialentry([What counts as a proof], [#raw("math-logic-and-proof") #sym.dot.c #raw("theorem-tree-tutorial")],
  (
    ([teaches], [Every proof you have ever read uses a handful of moves: #strong[assume the hypothesis and build the conclusion] (direct), #strong[prove the contrapositive], #strong[assume the negation and derive a contradiction], #strong[split into exhaustive cases], #strong[exhibit one counterexample], #strong[induct]. This tutorial walks that list in the capsule's dependency order. For each method you run the move on a concrete object and watch it work—then you ask the Lean kernel #emph[which logical axioms the move actually needs]. The answer is the point of the lesson: #raw("direct"), #raw("cases"), and ordinary #raw("induction") are #strong[constructive] (they compute a witness); #raw("contrapositive"), #raw("contradiction"), and "the universal failed so a counterexample must exist" each genuinely require a #strong[classical] principle, and the kernel says so by name.]),
    ([runs], [17 runnable blocks #sym.dot.c 9 of them a Lean core #sym.dot.c calls #raw("lean")]),
    ([command], [#raw("upmd skills/math-logic-and-proof/tutorial/what-counts-as-a-proof.md")]),
  ))
== #raw("math-number-systems")

#tutorialentry([Building the number that isn't there], [#raw("math-number-systems") #sym.dot.c #raw("theorem-tree-tutorial")],
  (
    ([teaches], [#raw("√2") is a number you can name—the diagonal of a unit square—but there is no fraction equal to it. This tutorial follows that gap from both sides. First it builds #raw("ℤ") and then #raw("ℚ") as #strong[quotients], and at each step runs the check that an operation on classes #emph[is actually a function] (and a counterexample where it is not). Then it makes the gap precise: #raw("{x ∈ ℚ : x² < 2}") is bounded but has no least upper bound in #raw("ℚ"). Then it builds #raw("ℝ") from #strong[Dedekind cuts]—a real #emph[is] the set of rationals below it—and shows the same set now has a supremum, #strong[exhibited] as a union, not postulated. By the end #raw("√2") exists, and every step was choice-free and constructive.]),
    ([runs], [24 runnable blocks #sym.dot.c 3 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean")]),
    ([command], [#raw("upmd skills/math-number-systems/tutorial/building-the-number.md")]),
  ))
== #raw("math-real-analysis")

#tutorialentry([The Hole in the Rationals], [#raw("math-real-analysis") #sym.dot.c executable-tutorial method],
  (
    ([teaches], [An interactive walk from one stubborn sequence to the axiom that makes calculus possible. You will meet the least-upper-bound axiom, the monotone convergence theorem, the nested interval theorem, Bolzano–Weierstrass, and the Cauchy criterion—and at each step you run a calculation that shows it working, then a calculation that shows it #strong[failing] the moment you move from #raw("ℝ") to #raw("ℚ").]),
    ([runs], [13 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean"), #raw("awk")]),
    ([command], [#raw("upmd skills/math-real-analysis/tutorial/hole-in-the-rationals.md")]),
  ))
== #raw("math-probability")

#tutorialentry([Three axioms, and everything before random variables], [#raw("math-probability") #sym.dot.c #raw("theorem-tree-tutorial")],
  (
    ([teaches], [Probability theory is three sentences (#raw("P ≥ 0"), #raw("P(Ω) = 1"), countable additivity) plus the σ-algebra they live on. Before you ever meet a random variable, those three sentences already force the complement rule, monotonicity, finite additivity, and the #strong[union bound]—the single most-used inequality in the subject. This tutorial walks that closure on one object: #strong[a fair six-sided die], #raw("Ω = {1,2,3,4,5,6}") with #raw("P({k}) = 1/6"). Each theorem you meet comes with a check that it holds on the die, then a check that it #strong[breaks] the moment a hypothesis is dropped.]),
    ([runs], [18 runnable blocks #sym.dot.c 2 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean")]),
    ([command], [#raw("upmd skills/math-probability/tutorial/three-axioms.md")]),
  ))
#tutorialentry([The concentration ladder], [#raw("math-probability") #sym.dot.c #raw("theorem-tree-tutorial")],
  (
    ([teaches], [There is one inequality in probability—#strong[Markov's]—and four theorems that are just Markov applied to a cleverer function each time:]),
    ([runs], [21 runnable blocks #sym.dot.c 3 of them a Lean core #sym.dot.c calls #raw("bc"), #raw("lean")]),
    ([command], [#raw("upmd skills/math-probability/tutorial/concentration-ladder.md")]),
  ))

= Physics tutorials

#note[5 tutorials from 3 capsules, 23 runnable blocks between them.]

== #raw("physics-newtonian")

#tutorialentry([Why a Pendulum Keeps Time], [#raw("physics-newtonian") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#emph[no lead paragraph]]),
    ([runs], [9 runnable blocks #sym.dot.c calls #raw("bc"), #raw("awk")]),
    ([command], [#raw("upmd skills/physics-newtonian/tutorial/pendulum.md")]),
  ))
== #raw("physics-thermodynamics")

#tutorialentry([Why Heat Engines Have a Ceiling], [#raw("physics-thermodynamics") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#emph[no lead paragraph]]),
    ([runs], [3 runnable blocks #sym.dot.c calls #raw("bc")]),
    ([command], [#raw("upmd skills/physics-thermodynamics/tutorial/why-heat-engines-have-a-ceiling.md")]),
  ))
== #raw("physics-acoustics")

#tutorialentry([How Fast Does Sound Travel?], [#raw("physics-acoustics") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#emph[no lead paragraph]]),
    ([runs], [3 runnable blocks #sym.dot.c calls #raw("bc")]),
    ([command], [#raw("upmd skills/physics-acoustics/tutorial/how-fast-does-sound-travel.md")]),
  ))
#tutorialentry([Designing an Organ Pipe], [#raw("physics-acoustics") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#emph[no lead paragraph]]),
    ([runs], [4 runnable blocks #sym.dot.c calls #raw("bc")]),
    ([command], [#raw("upmd skills/physics-acoustics/tutorial/designing-an-organ-pipe.md")]),
  ))
#tutorialentry([Are a Megaphone and a Long-Range Microphone the Same Thing?], [#raw("physics-acoustics") #sym.dot.c #raw("formula-tree-tutorial")],
  (
    ([teaches], [#emph[no lead paragraph]]),
    ([runs], [4 runnable blocks #sym.dot.c calls #raw("bc")]),
    ([command], [#raw("upmd skills/physics-acoustics/tutorial/horns-and-reciprocity.md")]),
  ))

