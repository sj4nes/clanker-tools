# independence_random_variables

## Type
definition

## Statement
Random variables X_1, ..., X_n are independent if the sigma-algebras sigma(X_1), ..., sigma(X_n) are independent; equivalently P(X_1 in B_1, ..., X_n in B_n) = prod_i P(X_i in B_i) for all Borel B_i; equivalently the joint law is the product of the marginals.

## Symbols
- `X_i` — random variables, type: Omega -> R
- `B_i` — Borel sets, type: element of B(R)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
distribution_pushforward, independence_sigma_algebras, joint_distribution, random_variable

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the product measure P_{X_1} tensor ... tensor P_{X_n} exists and is a probability measure on B(R^n); independence says the joint law equals it.

## Type / well-formedness check
the sets { X_i in B_i } for B_i Borel form a generating pi-system for sigma(X_i), so factorization on rectangles (checked via CDFs or densities) is enough by pi-lambda. Functions of disjoint independent blocks stay independent.

## Specialization / boundary cases
- densities factorize: f_{X_1,...,X_n}(x) = prod_i f_{X_i}(x_i) (independence_factorization)
- g_1(X_1), ..., g_n(X_n) are independent for any measurable g_i
- iid = independent + identically distributed

## Hypothesis-dropped counterexamples
- **all_n_together_not_just_pairs**: three variables can be pairwise independent but not mutually independent -- e.g. X_1, X_2 iid uniform on {-1,1}, X_3 = X_1 X_2
- **the_joint_law_not_just_marginals**: same marginals, different dependence: (X, X) vs (X, -X) vs (X, Y independent)

## Common misuse
- inferring independence from zero correlation (uncorrelated_not_independent)
- assuming a function of ALL the X_i stays independent of another such function

## In the wild
- naive Bayes classifiers assume the features are conditionally independent given the label -- the classic spam-filter deployment, and still a strong baseline for text classification
- the whole toolkit for sums of independent variables (MGF/CF factorise, variances add, the CLT) rests on this definition -- risk aggregation, the bootstrap, randomized algorithm analysis

## Related nodes (non-prerequisite)
- special_case: iid
- checked_by: independence_factorization
- implies: independence_expectation

## Sources
billingsley_probability_measure, durrett_pte
