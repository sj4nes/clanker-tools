# bounded_completeness

## Type
definition

## Statement
T is boundedly complete if E_theta[g(T)] = 0 for all theta implies g(T) = 0 a.s. whenever g is bounded.

## Symbols
- `g` — a bounded measurable function

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
completeness_statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A property of the family of laws of T.

## Type / well-formedness check
Weaker than completeness. It is exactly what is needed for the identifiability of a structural function in some econometric models, and it suffices for one direction of Basu's theorem.

## Specialization / boundary cases
- complete => boundedly complete (trivially)
- there exist boundedly-complete-but-not-complete families (Lehmann-Scheffe example)
- used in nonparametric IV: bounded completeness of the instrument given the endogenous regressor identifies the structural function

## Hypothesis-dropped counterexamples
- **bounded_completeness**: a family rich enough to kill bounded unbiased-of-zero g but not unbounded ones -- rare in the parametric models here, central in nonparametric identification

## Common misuse
- treating bounded completeness as equivalent to completeness in general -- it is strictly weaker

## Related nodes (non-prerequisite)
- generalizes_from: completeness_statistic

## Sources
lehmann_romano_tsh, newey_powell_2003
