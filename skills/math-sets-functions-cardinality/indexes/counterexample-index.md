# Counterexample index (generated from results/*.yaml)

`dropped hypothesis`  ->  `witnessing counterexample`  (from which result)

- **cantor_diagonal** — binary_not_decimal_ambiguity: 'over decimal digits one must avoid 9-tails (0.4999... = 0.5); over {0,1} with the "flip" rule there is no such collision, so the binary form is cleanest here'
- **cantor_schroeder_bernstein** — injection_each_way: 'one injection alone gives only |X| <= |Y|; e.g. omega injects into R but they are not equinumerous'
- **cantor_theorem** — none_the_hypotheses_are_empty: 'the theorem is unconditional -- there is no finite or "small" X that escapes it. The instance-checks.bc worked example (X = {0,1,2,3}) shows D explicitly.'
- **continuum_hypothesis** — it_cannot_be_dropped_or_assumed_in_general: 'any theorem whose proof uses CH must flag it; the result is then conditional. Many "CH-sensitive" statements in analysis (automatic continuity, the size of certain sigma-algebras) are genuinely undecided in ZFC.'
- **countable_closure_properties** — countable_choice: 'consistent with ZF (Feferman-Levy) that R is a countable union of countable sets -- the union clause genuinely needs CC'
- **countable_closure_properties** — countably_many_pieces: 'an uncountable union of singletons is uncountable (X = union of {x})'
- **equivalence_partition_correspondence** — transitivity: 'the relation "differ by less than 1" on R is reflexive and symmetric but not transitive; its "classes" overlap without being equal -- not a partition'
- **equivalence_partition_correspondence** — reflexivity: 'a symmetric transitive relation that is not reflexive (the empty relation) leaves some x in no class -- the classes do not cover X'
- **omega_construction** — axiom_infinity: 'without Infinity, ZF - Infinity is consistent with "every set is finite" (the hereditarily finite sets V_omega model it); omega does not exist'
- **omega_construction** — axiom_separation: 'needed to carve omega out of I_0 as the intersection of all inductive sets'
- **peano_holds_in_omega** — minimality_of_omega: 'a larger inductive set I_0 (with an extra Z-chain) satisfies Peano axioms 1-4 but not induction -- the extra chain is an inductive proper subset'
- **peano_holds_in_omega** — foundation_or_ordinal_structure: 'S injective needs that x notin x ; in a non-well-founded universe with a Quine atom x = {x}, S(x) = x and S is not injective'
- **preimage_algebra** — using_the_image_instead: 'f[A cap B] can be a PROPER subset of f[A] cap f[B] -- e.g. f(x)=x^2, A={-1}, B={1}: f[A cap B] = f[emptyset] = emptyset, but f[A] cap f[B] = {1}. Only the preimage algebra is clean.'
- **quantifier_negation** — classical_logic: 'in intuitionistic logic, not (forall x, P x or not P x) is refutable, but forall x, (P x or not P x) is NOT provable -- the exists-not form is strictly classical'
- **recursion_theorem** — induction_via_minimality_of_omega: 'over a larger inductive set with an extra Z-chain, f is unconstrained on the chain -- existence and uniqueness both fail'
- **well_defined_on_quotient** — h_respects_the_relation: 'on Z/6Z, the rule [n] -> n^2 mod 12 is NOT well-defined: [0] = [6] but 0 != 36 mod 12 = 0... take [n] -> n mod 4 on Z/6Z: [0]=[6] but 0 != 2. The rule depends on the representative.'
- **zorn_lemma** — every_chain_has_an_upper_bound: 'the half-open interval [0,1) under <= : every chain is bounded above by 1 IN [0,1]... but 1 is not in [0,1), so chains {1 - 1/n} have NO upper bound in [0,1); and indeed [0,1) has no maximal element'

