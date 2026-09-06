# lebesgue_measure_caratheodory

## Type
construction

## Statement
There is a unique measure lambda on B(R) with lambda([a,b]) = b - a. It is built by extending interval length to an outer measure lambda* on all of 2^R, then restricting to the Caratheodory-measurable sets, which include B(R).

## Symbols
- `lambda` — Lebesgue measure, type: measure on B(R)
- `lambda*` — Lebesgue outer measure, type: 2^R -> [0, inf]

## Epistemic status
constructive_result (non-constructive) (uses choice)

## Prerequisites (tsort edges into this node)
borel_sigma_algebra, measure, real_field

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Caratheodory extension theorem: an outer measure's Caratheodory-measurable sets form a sigma-algebra on which it is a complete measure; interval length is a premeasure on the algebra of finite unions of intervals, so it extends; pi-lambda gives uniqueness on B(R)
derives_from: dynkin_pi_lambda
lean_status: cited — Folland Real Analysis 2e Thm 1.14, 1.19; Billingsley Thm 12.4

## Type / well-formedness check
CITED. lambda is sigma-finite (R = bigcup [-n, n]) and translation-invariant; it is the reference measure for 'absolutely continuous' random variables and densities. Non-measurable sets (Vitali) exist, using AC.

## Specialization / boundary cases
- lambda restricted to [0,1] is the uniform probability measure -- the model probability space
- lambda({x}) = 0, lambda(Q) = 0, lambda(Cantor set) = 0 -- uncountable null sets exist

## Hypothesis-dropped counterexamples
- **caratheodory_measurability**: lambda* is only finitely subadditive-not-additive on all of 2^R; a Vitali set V has lambda*(V) > 0 but the translates of V partition [0,1] into countably many congruent pieces, so countable additivity would force a contradiction -- V is not measurable

## Common misuse
- assuming every subset of R has a Lebesgue measure
- confusing lambda (on B(R)) with its completion (Lebesgue sigma-algebra)

## Related nodes (non-prerequisite)
- uses: axiom_of_choice (for non-measurable sets, not for lambda itself)
- extends: interval length

## Sources
folland_real_analysis, billingsley_probability_measure
