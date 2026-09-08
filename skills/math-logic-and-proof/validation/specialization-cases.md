# Specializations & hypothesis-dropped counterexamples (generated from results/*.yaml)

One `## <node>` section per headline result: at least one specialization /
boundary case, and at least one counterexample showing a named hypothesis
cannot be dropped (or a note that every hypothesis is essential / the
statement is unconditional). The remaining 109 nodes carry this on their
`nodes/<id>.md` detail page.


## wff_unique_readability

- **spec:** atoms: the base case, one parse trivially
- **spec:** first-order wffs: the same theorem, extended with the R(t1..tn), t=u, forall x, exists x clauses (see first_order_wff)
- **spec:** Polish (prefix) notation: unique readability holds with NO parentheses at all -- the classic alternative
- **drop `fully_parenthesised_or_precedence_fixed`:** the string "p and q or r" has two parses (p and q) or r  vs  p and (q or r); without a precedence convention or full parentheses, unique readability fails and every semantic function is ill-defined

## de_morgan_prop

- **spec:** iterate: not(p and q and r) iff not p or not q or not r
- **spec:** infinitary / quantified form: not(forall x, P x) iff exists x, not P x -- this is quantifier_negation, and inherits the same needs_LEM split
- **spec:** p = q: not(p and p) iff not p (with idempotence)
- **drop `classical_logic`:** in intuitionistic logic, not(p and not p) is a theorem but (not p or not not p) is not -- so not(p and q) -> not p or not q fails; Kripke countermodel: one world forcing neither p nor not p

## functional_completeness

- **spec:** n = 2: all 16 binary connectives expressible; xor = (p or q) and not(p and q)
- **spec:** the empty basis expresses only... nothing; {and, or} (no negation) expresses only the monotone functions -- NOT complete
- **spec:** majority(p,q,r) = (p and q) or (p and r) or (q and r)
- **drop `none_all_hypotheses_vacuous`:** the theorem is unconditional. But the BASIS matters: {and,or,T,bottom} is not functionally complete (misses negation / every non-monotone function, e.g. NOT p); {iff, not} is not complete (only the affine functions); {imp} alone is not complete (cannot express bottom)

## deduction_theorem

- **spec:** Gamma empty: |- psi under assumption phi  iff  |- phi -> psi
- **spec:** iterate: Gamma, phi1, ..., phin |- psi  iff  Gamma |- phi1 -> ... -> phin -> psi
- **spec:** this IS the ->I rule of natural deduction -- the theorem is why Hilbert can simulate ND (nd_hilbert_equivalence)
- **drop `hilbert_axioms_1_and_2`:** a Hilbert system with only modus ponens and P->(Q->P) does not admit the deduction theorem -- axiom 2 (the distribution axiom) is exactly what the MP case of the induction needs
- **drop `first_order_side_condition`:** without "phi has no free variable generalised in the sub-derivation": from {P(x)} one derives forall x, P(x), so {P(x)} |- forall x P(x), but NOT |- P(x) -> forall x P(x) (false in any structure where P holds of some but not all elements)

## nd_hilbert_equivalence

- **spec:** Gamma empty: the theorems coincide
- **spec:** a sequent calculus LK added as a third system: |-_LK coincides too (mentioned_alternative), so "provable" is robust
- **spec:** first-order: the analogous derivability_fol equivalence (ND + eigenvariable conditions  iff  Hilbert + generalisation)
- **drop `same_connective_set_both_calculi`:** Hilbert with only P->(Q->P) + MP proves strictly fewer wffs (no -> distribution); the equivalence needs the full schema list
- **drop `classical_rule_present_on_both_or_neither`:** ND with raa_rule vs an intuitionistic Hilbert system: ND proves not not p -> p, the Hilbert system does not -- equivalence breaks
- **drop `deduction_theorem_available`:** the ND => H direction has no route for ->I without the deduction theorem as a meta-result

## soundness_prop

- **spec:** Gamma empty: |- phi implies phi is a tautology
- **spec:** contrapositive: Gamma not |= phi (a countermodel exists) implies Gamma not |- phi -- how you show something is UNprovable
- **spec:** phi = bottom: if Gamma |- bottom then Gamma is unsatisfiable -- i.e. satisfiable implies consistent
- **drop `rules_are_truth_preserving`:** add an unsound rule, e.g. "from p or q infer p": then {p or q} |- p but {p or q} not |= p (assignment p=F, q=T). Soundness is exactly the guarantee that the rule set is not like this.

## post_completeness_theorem

- **spec:** Gamma empty: |= phi implies |- phi -- every tautology is a theorem
- **spec:** Gamma finite: reduces to "the conjunction of Gamma implies phi is a tautology, hence a theorem"
- **spec:** this is the propositional fragment of godel_completeness_theorem (no terms, no Henkin witnesses)
- **drop `classical_calculus`:** an intuitionistic propositional calculus is NOT complete for classical (Boolean) semantics: not not p -> p is a tautology but not intuitionistically derivable. It IS complete for Kripke / Heyting-algebra semantics (a different result).

## compactness_prop

- **spec:** graph k-colourability: an infinite graph is k-colourable iff every finite subgraph is (de Bruijn-Erdos) -- a direct corollary
- **spec:** Gamma finite: trivial (Gamma is its own finite subset)
- **spec:** first-order lift: compactness_fol, proved the same way from godel_completeness_theorem
- **drop `finite_satisfiability`:** the sole nontrivial hypothesis, and essential. Drop it and the theorem is false: {p, not p} has an unsatisfiable finite subset (itself) and is unsatisfiable. The theorem's force is entirely that FINITE satisfiability suffices -- a set all of whose finite subsets are satisfiable but which is itself unsatisfiable would be the counterexample, and compactness is precisely the assertion that none exists.

## free_for

- **spec:** t a constant or closed term: free for x in every phi (this is why Henkin witness constants c_psi need no renaming)
- **spec:** x not free in phi: vacuously free for x (phi[t/x] = phi)
- **spec:** t = x: always free for x in phi
- **spec:** phi quantifier-free: always free
- **drop `free_for_condition`:** phi = exists y (y > x), t = y: phi[y/x] = exists y (y > y). In (N,<) the premise forall x, exists y (y > x) is true but exists y (y > y) is false -- forall-elimination becomes unsound. This is the canonical capture bug.

## tarski_satisfaction

- **spec:** propositional reduct: no quantifiers, no terms -> recovers satisfaction (v |= phi)
- **spec:** finite structure: satisfaction is decidable (the forall/exists clauses are finite conjunctions/disjunctions) -- this is what bc checks
- **spec:** atomic sentence R(c,d): true iff (c^A, d^A) in R^A
- **drop `nonempty_domain`:** if A = empty were allowed: forall x phi is vacuously true and exists x phi is false for every phi, so exists x (x = x) is false -- breaking quantifier duality and the standard axioms. Free logic handles this; out of scope.
- **drop `s_defined_on_free_variables`:** A |= (x = y)[s] is meaningless if s(x) or s(y) is undefined

## substitution_lemma_semantic

- **spec:** t = a constant c: A |= phi[c/x][s] iff A |= phi[s(x -> c^A)] -- the form used in forall-elimination soundness
- **spec:** t = x: both sides are A |= phi[s] (identity substitution)
- **spec:** phi atomic: reduces to the term-evaluation sub-lemma
- **drop `t_free_for_x_in_phi`:** phi = exists y (x = y) has y not free for... take phi = exists y not(x = y), t = y, A = (any 2+ element domain). phi[y/x] = exists y not(y = y) is unsatisfiable; but A |= phi[s(x -> s(y))] holds whenever the domain has another element. The two sides disagree -- the lemma is FALSE without free_for.

## quantifier_negation

- **spec:** not forall x (P x -> Q x)  iff  exists x (P x and not Q x)
- **spec:** negating continuity: not(forall eps>0 exists delta>0 forall x, |x-c|<delta -> |f x - f c|<eps)  iff  exists eps>0 forall delta>0 exists x, |x-c|<delta and |f x - f c| >= eps  -- the definition of discontinuity
- **spec:** not(X countable) = "no injection X -> omega"
- **drop `classical_metatheory`:** in intuitionistic predicate logic not(forall x, P x or not P x) is refutable while forall x (P x or not P x) is not provable -- the not-forall -> exists-not direction fails. Kripke countermodel: ascending chain of worlds where P turns true later at each node.
- **drop `nonempty_domain`:** free logic: forall x phi can be vacuously true while exists x phi is false, breaking the duality

## quantifier_order

- **spec:** phi = (x < y) over (N, <): forall x exists y (x < y) is TRUE (y = x+1); exists y forall x (x < y) is FALSE (no greatest+1). The standard witness.
- **spec:** epsilon-delta: "continuous" (forall x, forall eps, exists delta ...) vs "uniformly continuous" (forall eps, exists delta, forall x ...) -- swapping the delta out is exactly this
- **spec:** over a domain with one element: the two orders coincide
- **drop `order_matters`:** treating forall x exists y phi as exists y forall x phi: f: R -> R continuous but not uniformly continuous (f(x) = x^2 on R, or 1/x on (0,1)) -- for each x a delta exists, no delta works for all x
- **drop `distinct_variables`:** if x and y are the same variable the statement is malformed

## soundness_fol

- **spec:** Gamma empty: |- phi implies phi is valid
- **spec:** contrapositive: a formula with a countermodel is not derivable -- the tool for proving non-theorems (e.g. that exists x P x -> forall x P x is not a theorem)
- **spec:** propositional reduct: recovers soundness_prop
- **drop `eigenvariable_condition_enforced`:** drop the "y not free in open assumptions" side condition on forall-I: from P(y) derive forall x P(x), so {P(y)} |- forall x P(x); but {P(y)} not|= forall x P(x) (a structure where P holds of s(y) only). Soundness fails.
- **drop `rules_truth_preserving`:** an unsound quantifier rule, e.g. "from exists x phi infer phi[c/x] for arbitrary already-used c", breaks soundness (c may already be constrained)

## godel_completeness_theorem

- **spec:** propositional fragment: reduces to post_completeness_theorem (no terms, no witnesses)
- **spec:** Gamma finite: |= (conj Gamma -> phi) implies |- (conj Gamma -> phi)
- **spec:** Gamma complete and consistent: the term model is a canonical model of Gamma
- **drop `first_order`:** second-order logic with standard semantics has NO complete proof system: (N,+,.,<) is categorical in SOL, so a complete SOL calculus would decide arithmetic, contradicting godel_incompleteness_first
- **drop `classical_logic`:** intuitionistic FOL is complete for Kripke semantics, not for classical (Tarski) semantics
- **drop `equality_is_identity`:** without the equality axioms the term-model quotient is not well-defined and interpretations are not functions

## compactness_fol

- **spec:** a theory with arbitrarily large finite models has an infinite model (add constants c_1, ..., c_n and axioms c_i != c_j for all n; every finite subset is satisfiable)
- **spec:** non-standard models of arithmetic: PA union {c > 0, c > 1, c > 2, ...} is finitely satisfiable, so has a model -- with an element exceeding every numeral
- **spec:** propositional reduct: compactness_prop
- **drop `finite_satisfiability`:** essential and sole nontrivial hypothesis -- {P(c), not P(c)} has an unsatisfiable finite subset and no model
- **drop `first_order`:** compactness FAILS for second-order logic and for infinitary L_{omega_1,omega}. In SOL one can write a single sentence true exactly in the infinite structures and another true exactly in the finite ones; their consequences violate compactness. First-order-ness is what makes the theorem hold.

## lowenheim_skolem_down

- **spec:** ZFC, if consistent, has a countable model (skolem_paradox)
- **spec:** the theory of real closed fields has a countable model -- the real algebraic numbers
- **spec:** any consistent finitely axiomatised theory has a finite or countable model
- **drop `countable_language`:** a language with uncountably many constants {c_r : r in R} plus axioms c_r != c_s: every model has >= |R| elements -- no countable model
- **drop `satisfiable_theory`:** an inconsistent theory has no model at all

## induction_equivalence

- **spec:** strong induction with no explicit base case: the base is the vacuous "P(k) for all k < 0"
- **spec:** induction from a base b: shift, or restrict P to n >= b
- **spec:** structural induction on wffs / terms / derivations: the same principle along an inductive_definition (structural_induction)
- **spec:** transfinite induction (math-sets-functions-cardinality): the well-ordering -> induction direction, lifted to ordinals
- **drop `successor_injective_and_no_predecessor_of_zero`:** on Z/6Z with "successor" = +1: weak induction from 0 "proves" every element reachable (true) but the well-ordering principle fails (no least element in the cyclic order) -- the Peano structure hypotheses are what make the three coincide
- **drop `naturals_with_zero_successor_and_order`:** on Z (no least element): well-ordering fails outright; induction "downward" also fails

## undecidability_fol_validity

- **spec:** monadic first-order logic (only unary predicates, no equality, no functions): DECIDABLE (Loewenheim 1915)
- **spec:** first-order logic with equality but no other relation/function symbols: decidable
- **spec:** the Bernays-Schoenfinkel-Ramsey class (exists* forall* prefix, no functions): decidable
- **spec:** propositional logic: decidable (tautology_decidable) -- the boundary is exactly the quantifiers over a rich enough language
- **drop `language_expressive_enough`:** monadic / prefix-restricted fragments are decidable -- undecidability needs enough expressive power to encode computation (one binary relation suffices)
- **drop `church_turing_thesis`:** without identifying "algorithm" with Turing-computable, the statement has no precise content

## godel_incompleteness_first

- **spec:** T = PA: PA not|- Con(PA) (godel_incompleteness_second); Goodstein, Paris-Harrington are natural PA-independent statements
- **spec:** T = ZFC: incomplete if consistent (incompleteness_of_PA_ZFC); CH independent (via forcing, different mechanism, same headline)
- **spec:** T = Q: incomplete and essentially undecidable
- **spec:** T = true arithmetic Th(N): COMPLETE, but not recursively axiomatisable -- hypothesis 2 fails. The tight boundary.
- **spec:** T = real closed fields / (R,+,.,<): COMPLETE and decidable (Tarski) -- does not interpret N, hypothesis 3 fails
- **drop `T_consistent`:** an inconsistent T proves everything -- trivially complete
- **drop `T_recursively_axiomatised`:** Th(N) is complete
- **drop `T_interprets_Q`:** dense linear orders, Presburger arithmetic (N,+), real closed fields -- all complete and decidable

## godel_incompleteness_second

- **spec:** T = PA: PA not|- Con(PA); but PA + Con(PA) is a strictly stronger consistent theory (which then cannot prove ITS own consistency)
- **spec:** T = ZFC: ZFC not|- Con(ZFC); Con(ZFC) follows from large-cardinal axioms (e.g. an inaccessible)
- **spec:** Gentzen: PA-consistency IS provable by transfinite induction up to epsilon_0 -- in a system not contained in PA. No contradiction with the theorem.
- **drop `T_proves_HBL_derivability_conditions`:** a theory interpreting only Q (first-theorem strength) may not support the internal formalisation -- the second theorem needs more arithmetic than the first
- **drop `T_consistent`:** an inconsistent T proves Con(T) (it proves everything)
- **drop `T_recursively_axiomatised`:** Th(N) proves Con(PA) -- but is not recursively axiomatised
