# Type / well-formedness checks (generated from results/*.yaml)

For every node: the statement's type-check status, the well-formedness note
(what must hold for the statement to even make sense), and each symbol's type.
A passing type check is **necessary, not sufficient** — a well-typed statement
can still be false on a missing hypothesis, a strictness, or a quantifier order.


## set_algebra

- **status:** `well_formed`
- **note:** operations are on subsets of one fixed Omega; an indexed intersection needs I nonempty for the usual identities. Discharged from math-sets-functions-cardinality.
- **symbols:**
  - `A, B` — subsets of a set Omega, type: element of 2^Omega
  - `{A_i}` — an indexed family, type: I -> 2^Omega
- **hypotheses:** (none / unconditional within scope)

## preimage_algebra

- **status:** `well_formed`
- **note:** f^{-1} here is the preimage OPERATOR ON SETS, defined for every f (not an inverse function). It is a Boolean-algebra homomorphism 2^Y -> 2^X; the forward image is only a join-homomorphism.
- **symbols:**
  - `f` — any function X -> Y, type: function
  - `B_i` — subsets of the codomain Y, type: element of 2^Y
- **hypotheses:** (none / unconditional within scope)

## countable_set

- **status:** `well_formed`
- **note:** 'countable' includes finite here. A countable union of countable sets needs the axiom of countable choice (noted, not used elsewhere in this capsule). Discharged from math-sets-functions-cardinality.
- **symbols:**
  - `A` — a set, type: set
  - `N` — the natural numbers, type: set
- **hypotheses:** (none / unconditional within scope)

## real_field

- **status:** `well_formed`
- **note:** the completeness axiom (lub property) is taken as given; a construction of R (Dedekind cuts / Cauchy completion) is cited to math-real-analysis, not built.
- **symbols:**
  - `R` — the real numbers, type: complete ordered field
- **hypotheses:** (none / unconditional within scope)

## sequence_limit

- **status:** `well_formed`
- **note:** the quantifier order is 'for all eps EXISTS N' (N may depend on eps); the uniform form ('exists N for all eps') is a different, stronger statement -- relevant to the difference between the convergence modes downstream. Discharged from math-real-analysis.
- **symbols:**
  - `(x_n)` — a real sequence, type: N -> R
  - `L` — the limit, type: real
- **hypotheses:** (none / unconditional within scope)

## limsup_liminf

- **status:** `well_formed`
- **note:** for sets, 'A_n infinitely often' (i.o.) is limsup A_n; 'A_n eventually / all but finitely often' is liminf A_n. Both are events (countable operations on F). Discharged from math-real-analysis.
- **symbols:**
  - `(a_n)` — a real sequence, type: N -> R
  - `(A_n)` — a sequence of events, type: N -> F
- **hypotheses:** (none / unconditional within scope)

## series_convergence

- **status:** `well_formed`
- **note:** a series of NONNEGATIVE terms always has a sum in [0, +inf] (monotone partial sums) -- this is what makes countable additivity of a measure well-posed. Discharged from math-real-analysis.
- **symbols:**
  - `(a_n)` — the terms, type: N -> R
  - `sum a_n` — the sum, type: real or +inf
- **hypotheses:** (none / unconditional within scope)

## convex_function

- **status:** `well_formed`
- **note:** convexity is on an interval I; at an interior point c there is at least one supporting line phi(x) >= phi(c) + m (x - c). Jensen's inequality is exactly 'take x = X, c = E[X], then integrate'. Discharged from math-real-analysis.
- **symbols:**
  - `phi` — the function, type: I -> R with I an interval
  - `supporting line at c` — an affine L with L(c)=phi(c), L<=phi, type: affine function
- **hypotheses:** (none / unconditional within scope)

## abstract_integral

- **status:** `well_formed`
- **note:** CITED, not constructed. The integral is linear, monotone, and satisfies MCT / DCT / Fatou; E[X] is this integral against P. f measurable is required for the sup to be over a well-defined set.
- **symbols:**
  - `f` — a measurable function, type: Omega -> R (or [0, inf])
  - `mu` — the measure, type: measure on F
  - `integral f dmu` — the integral, type: real or +-inf
- **hypotheses:** (none / unconditional within scope)

## monotone_convergence_theorem

- **status:** `well_formed`
- **note:** CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).
- **symbols:**
  - `f_n, f` — measurable functions, type: Omega -> R
  - `mu` — a (sigma-finite) measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## dominated_convergence_theorem

- **status:** `well_formed`
- **note:** CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).
- **symbols:**
  - `f_n, f` — measurable functions, type: Omega -> R
  - `mu` — a (sigma-finite) measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## fatou_lemma

- **status:** `well_formed`
- **note:** CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).
- **symbols:**
  - `f_n, f` — measurable functions, type: Omega -> R
  - `mu` — a (sigma-finite) measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## fubini_tonelli

- **status:** `well_formed`
- **note:** CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).
- **symbols:**
  - `f_n, f` — measurable functions, type: Omega -> R
  - `mu` — a (sigma-finite) measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## radon_nikodym

- **status:** `well_formed`
- **note:** CITED. The exchange-of-limit toolkit for the integral; each is stated for a general measure and specialised to P for expectations (MCT/DCT/Fatou for E, Fubini for E[XY] and convolutions).
- **symbols:**
  - `f_n, f` — measurable functions, type: Omega -> R
  - `mu` — a (sigma-finite) measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## sigma_algebra

- **status:** `well_formed`
- **note:** closure is under COUNTABLE unions, not arbitrary; the three axioms give closure under countable intersection and set difference. The pair (Omega, F) is a measurable space.
- **symbols:**
  - `Omega` — the sample space, type: set
  - `F` — the family of events, type: subset of 2^Omega
- **hypotheses:** (none / unconditional within scope)

## generated_sigma_algebra

- **status:** `well_formed`
- **note:** the intersection is over a nonempty family (2^Omega always qualifies), so sigma(C) exists and is itself a sigma-algebra; it is the unique smallest one.
- **symbols:**
  - `C` — a collection of subsets, type: subset of 2^Omega
  - `sigma(C)` — the generated sigma-algebra, type: sigma-algebra
- **hypotheses:** (none / unconditional within scope)

## borel_sigma_algebra

- **status:** `well_formed`
- **note:** the half-lines form a pi-system generating B(R); this is why a CDF (a function of the half-lines) determines the whole law. Every set one can 'write down' -- intervals, countable unions, F-sigma, G-delta -- is Borel.
- **symbols:**
  - `B(R)` — the Borel sets of R, type: sigma-algebra on R
  - `R^d` — Euclidean d-space, type: set
- **hypotheses:** (none / unconditional within scope)

## measurable_space

- **status:** `well_formed`
- **note:** no measure is attached yet; a measurable space is the domain on which measures and measurable functions are defined.
- **symbols:**
  - `Omega` — underlying set, type: set
  - `F` — sigma-algebra, type: subset of 2^Omega
- **hypotheses:** (none / unconditional within scope)

## measure

- **status:** `well_formed`
- **note:** countable additivity is over a COUNTABLE disjoint family; the sum is a series in [0, inf] and always has a value. mu is sigma-finite if Omega is a countable union of finite-measure sets -- the hypothesis of Radon-Nikodym and Fubini.
- **symbols:**
  - `mu` — the measure, type: F -> [0, inf]
  - `(A_n)` — a countable disjoint family, type: N -> F
- **hypotheses:** (none / unconditional within scope)

## dynkin_pi_lambda

- **status:** `well_formed`
- **note:** the standard uniqueness engine: two measures agreeing on a generating pi-system (and on Omega, if finite) agree on the whole sigma-algebra -- because the agreement set is a lambda-system.
- **symbols:**
  - `P` — a pi-system, type: subset of 2^Omega
  - `L` — a lambda-system, type: subset of 2^Omega
- **hypotheses:** (none / unconditional within scope)

## lebesgue_measure_caratheodory

- **status:** `well_formed`
- **note:** CITED. lambda is sigma-finite (R = bigcup [-n, n]) and translation-invariant; it is the reference measure for 'absolutely continuous' random variables and densities. Non-measurable sets (Vitali) exist, using AC.
- **symbols:**
  - `lambda` — Lebesgue measure, type: measure on B(R)
  - `lambda*` — Lebesgue outer measure, type: 2^R -> [0, inf]
- **hypotheses:** (none / unconditional within scope)

## measure_monotonicity

- **status:** `well_formed`
- **note:** monotonicity uses mu(B) = mu(A) + mu(B \ A) >= mu(A); subadditivity disjointifies B_n = A_n \ (A_1 cup ... cup A_{n-1}) then uses countable additivity + monotonicity.
- **symbols:**
  - `mu` — a measure, type: F -> [0, inf]
  - `(A_n)` — any countable family in F, type: N -> F
- **hypotheses:** (none / unconditional within scope)

## measure_continuity

- **status:** `well_formed`
- **note:** continuity from below telescopes A = disjoint-union of (A_n \ A_{n-1}) and applies countable additivity; continuity from above applies it to the complements and needs mu(A_1) < inf to subtract.
- **symbols:**
  - `(A_n)` — a monotone sequence of events, type: N -> F
  - `A` — the limit set bigcup A_n or bigcap A_n, type: element of F
- **hypotheses:** (none / unconditional within scope)

## null_set

- **status:** `well_formed`
- **note:** a countable union of null sets is null (countable subadditivity) -- this is why 'a.e.' statements can be combined countably. A measure is complete if every subset of a null set is measurable (Lebesgue measure's completion adds exactly these).
- **symbols:**
  - `N` — a null set, type: element of F with measure 0
  - `mu` — the ambient measure, type: measure
- **hypotheses:** (none / unconditional within scope)

## almost_sure

- **status:** `well_formed`
- **note:** 'a.s.' is 'a.e.' for a probability measure. Countably many a.s. events hold simultaneously a.s. (their intersection has probability 1). X = Y a.s. means P(X = Y) = 1; it is an equivalence relation on random variables and is the identification used to define L^p and E[X | G].
- **symbols:**
  - `A` — an event, type: element of F
  - `P` — the probability measure, type: F -> [0,1]
- **hypotheses:** (none / unconditional within scope)

## kolmogorov_axioms

- **status:** `well_formed`
- **note:** countable additivity quantifies over COUNTABLE disjoint families; the sum is a series of nonnegative reals, convergent because bounded by 1. Finite additivity is the special case padding with the empty set.
- **symbols:**
  - `Omega` — {'meaning': 'sample space', 'type': 'nonempty set'}
  - `F` — {'meaning': 'event sigma-algebra', 'type': 'sigma-algebra on Omega'}
  - `P` — {'meaning': 'probability measure', 'type': 'F -> [0,1]'}
  - `(A_n)` — {'meaning': 'a countable disjoint family of events', 'type': 'N -> F'}
- **hypotheses:** (none / unconditional within scope)

## probability_measure

- **status:** `well_formed`
- **note:** the only change from a general measure is the normalization P(Omega) = 1, which forces P <= 1 everywhere and removes every finiteness caveat (continuity from above always holds).
- **symbols:**
  - `P` — the probability measure, type: F -> [0,1]
  - `(Omega, F)` — a measurable space, type: measurable space
- **hypotheses:** (none / unconditional within scope)

## probability_space

- **status:** `well_formed`
- **note:** the single object every probabilistic statement is implicitly relative to. Random variables are measurable maps out of it; independence and conditioning are properties of sub-sigma-algebras of F.
- **symbols:**
  - `Omega` — sample space, type: set
  - `F` — events, type: sigma-algebra
  - `P` — probability, type: F -> [0,1]
- **hypotheses:** (none / unconditional within scope)

## complement_rule

- **status:** `well_formed`
- **note:** A and A^c are disjoint with union Omega, so P(A) + P(A^c) = P(Omega) = 1 by finite additivity and normalization.
- **symbols:**
  - `A, B` — events, type: element of F
- **hypotheses:** (none / unconditional within scope)

## finite_additivity

- **status:** `well_formed`
- **note:** the finite case of countable additivity: pad the finite family with A_{n+1} = A_{n+2} = ... = empty and apply the countable axiom (the tail terms are 0).
- **symbols:**
  - `A_i` — pairwise disjoint events, type: element of F
  - `n` — a fixed positive integer, type: natural number
- **hypotheses:** (none / unconditional within scope)

## inclusion_exclusion

- **status:** `well_formed`
- **note:** an alternating sum over all nonempty subsets S of the indices; the terms are probabilities of intersections, always well-defined.
- **symbols:**
  - `A_i` — events, type: element of F
  - `S` — a subset of {1..n}, type: index set
- **hypotheses:** (none / unconditional within scope)

## boole_inequality

- **status:** `well_formed`
- **note:** the countable subadditivity of P; disjointify B_n = A_n minus (A_1 cup ... cup A_{n-1}), so B_n subset A_n, the B_n are disjoint with the same union, and countable additivity + monotonicity finish it.
- **symbols:**
  - `(A_n)` — any countable family of events, type: N -> F
- **hypotheses:** (none / unconditional within scope)

## continuity_of_probability

- **status:** `well_formed`
- **note:** the specialisation of measure_continuity to a finite (probability) measure; continuity from above needs no extra hypothesis because P(A_1) <= 1 < inf.
- **symbols:**
  - `(A_n)` — a monotone sequence of events, type: N -> F
  - `A` — bigcup A_n or bigcap A_n, type: element of F
- **hypotheses:** (none / unconditional within scope)

## borel_cantelli_first

- **status:** `well_formed`
- **note:** no independence needed. P(limsup A_n) = P(bigcap_N bigcup_{n>=N} A_n) <= P(bigcup_{n>=N} A_n) <= sum_{n>=N} P(A_n) -> 0 as N -> inf (tail of a convergent series).
- **symbols:**
  - `(A_n)` — any sequence of events (no independence), type: N -> F
  - `limsup A_n` — the i.o. event, type: element of F
- **hypotheses:** (none / unconditional within scope)

## borel_cantelli_second

- **status:** `well_formed`
- **note:** the partial converse to BC1, and it does need independence. P(no A_n for n in [M, N]) = prod (1 - P(A_n)) <= prod e^{-P(A_n)} = e^{-sum} -> 0, so P(some A_n for n >= M) = 1 for every M.
- **symbols:**
  - `(A_n)` — an independent sequence of events, type: N -> F
- **hypotheses:** (none / unconditional within scope)

## conditional_probability

- **status:** `well_formed`
- **note:** the positivity P(B) > 0 is a genuine precondition; conditioning on probability-zero events needs conditional_expectation_abstract. P(. | B) restricts and renormalizes P to B.
- **symbols:**
  - `A, B` — events, type: element of F
  - `P(. | B)` — the conditioned measure, type: F -> [0,1]
- **hypotheses:** (none / unconditional within scope)

## multiplication_rule

- **status:** `well_formed`
- **note:** a rearrangement of the definition of conditional probability, iterated. The order of the A_i can be permuted; each requires its predecessor-intersection to have positive probability.
- **symbols:**
  - `A_i` — events with the running intersections of positive probability, type: element of F
- **hypotheses:** (none / unconditional within scope)

## law_of_total_probability

- **status:** `well_formed`
- **note:** A is the disjoint union of A cap B_i; apply countable additivity, then the multiplication rule to each term.
- **symbols:**
  - `A` — an event, type: element of F
  - `{B_i}` — a countable measurable partition of Omega, type: family in F
- **hypotheses:** (none / unconditional within scope)

## bayes_theorem

- **status:** `well_formed`
- **note:** the denominator is P(A) rewritten by the law of total probability; every term needs its conditioning event to have positive probability. j ranges over the same index set as i.
- **symbols:**
  - `A` — {'meaning': 'the observed event', 'type': 'element of F'}
  - `{B_i}` — {'meaning': 'a countable measurable partition of Omega', 'type': 'family in F'}
  - `P(.|.)` — {'meaning': 'conditional probability', 'type': 'F x F_{>0} -> [0,1]'}
- **hypotheses:** partition_of_Omega, positive_prior_P_B_i, positive_evidence_P_A

## measurable_function

- **status:** `well_formed`
- **note:** measurability is preservation of structure BACKWARD (preimage), which is why the preimage algebra -- not the image -- is the tool. Continuous functions R -> R are Borel measurable; measurable functions are closed under +, x, sup_n, liminf_n, limits.
- **symbols:**
  - `f` — the function, type: Omega -> E
  - `(E, E')` — the target measurable space, type: measurable space
- **hypotheses:** (none / unconditional within scope)

## random_variable

- **status:** `well_formed`
- **note:** a random variable is not random and not a variable -- it is a fixed measurable function; the randomness is in P. Two random variables can be equal in law without being equal as functions. sigma(X) = X^{-1}(B(R)) is the information X carries.
- **symbols:**
  - `X` — the random variable, type: Omega -> R measurable
  - `(Omega, F, P)` — the base probability space, type: probability space
- **hypotheses:** (none / unconditional within scope)

## indicator_rv

- **status:** `well_formed`
- **note:** the bridge between set operations and arithmetic: 1_{A cap B} = 1_A 1_B, 1_{A cup B} = 1_A + 1_B - 1_A 1_B, 1_{A^c} = 1 - 1_A. Turning a probability into an expectation (P(A) = E[1_A]) is the move behind Markov's inequality and the first-moment method.
- **symbols:**
  - `A` — an event, type: element of F
  - `1_A` — its indicator, type: Omega -> {0,1}
- **hypotheses:** (none / unconditional within scope)

## distribution_pushforward

- **status:** `well_formed`
- **note:** P_X packages everything about X that does not depend on the underlying Omega; equality in law is P_X = P_Y. The pushforward of a probability measure by a measurable map is a probability measure (preimage of B(R) is a sigma-algebra, countable additivity transfers).
- **symbols:**
  - `P_X` — the law of X, type: probability measure on B(R)
  - `X` — a random variable, type: Omega -> R
- **hypotheses:** (none / unconditional within scope)

## cdf

- **status:** `well_formed`
- **note:** F_X evaluates the law on the half-lines, which form a pi-system generating B(R) -- hence F_X determines P_X (cdf_determines_law). Right-continuity (not left) is the convention, from { X <= x } = bigcap_n { X <= x + 1/n }.
- **symbols:**
  - `F_X` — the CDF, type: R -> [0,1]
  - `x` — a real threshold, type: real
- **hypotheses:** (none / unconditional within scope)

## cdf_properties

- **status:** `well_formed`
- **note:** nondecreasing: monotonicity of P. Right-continuity and the limits: continuity of probability along { X <= x_n } for x_n decreasing to x (resp. to -inf, +inf). The converse builds X = F^{-1}(U) on ([0,1], lambda) via the quantile function.
- **symbols:**
  - `F_X` — the CDF, type: R -> [0,1]
- **hypotheses:** (none / unconditional within scope)

## cdf_determines_law

- **status:** `well_formed`
- **note:** the half-lines { (-inf, x] } are a pi-system generating B(R); two probability measures agreeing on a generating pi-system (and both giving R measure 1) agree on the whole sigma-algebra by the pi-lambda theorem.
- **symbols:**
  - `F_X, F_Y` — CDFs, type: R -> [0,1]
  - `P_X, P_Y` — laws, type: probability measure on B(R)
- **hypotheses:** (none / unconditional within scope)

## discrete_rv

- **status:** `well_formed`
- **note:** the law is then a countable sum of point masses P_X = sum_{x in S} p_X(x) delta_x, entirely described by the pmf.
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `S` — the countable support, type: countable subset of R
- **hypotheses:** (none / unconditional within scope)

## pmf

- **status:** `well_formed`
- **note:** the pmf is the density of P_X with respect to counting measure on S; it determines the discrete law completely.
- **symbols:**
  - `p_X` — the pmf, type: S -> [0,1]
  - `S` — the countable support, type: countable set
- **hypotheses:** (none / unconditional within scope)

## absolutely_continuous_rv

- **status:** `well_formed`
- **note:** 'absolutely continuous' is a property of the LAW relative to lambda, distinct from F_X being a continuous function (the Cantor function is continuous but its law is singular). Radon-Nikodym then supplies the density f_X = dP_X/dlambda.
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `lambda` — Lebesgue measure, type: measure on B(R)
- **hypotheses:** (none / unconditional within scope)

## pdf

- **status:** `well_formed`
- **note:** f_X is defined only up to a lambda-null set; f_X(x) is NOT a probability (it can exceed 1) but f_X(x) dx is an infinitesimal probability. Where F_X is differentiable, f_X = F_X'.
- **symbols:**
  - `f_X` — the density, type: R -> [0, inf), defined lambda-a.e.
  - `P_X` — the law, type: probability measure << lambda
- **hypotheses:** (none / unconditional within scope)

## quantile_function

- **status:** `well_formed`
- **note:** defined for every CDF, including discrete ones (where it is a step function) -- the inf makes it left-continuous and well-defined even where F_X jumps or is flat. F_X^{-1}(u) <= x iff u <= F_X(x), the Galois connection that powers the probability integral transform.
- **symbols:**
  - `F_X^{-1}` — the quantile function, type: (0,1) -> R
  - `u` — a probability level, type: real in (0,1)
- **hypotheses:** (none / unconditional within scope)

## probability_integral_transform

- **status:** `well_formed`
- **note:** the inverse direction (F^{-1}(U) ~ F) needs NO continuity and is the basis of simulation: to sample any distribution, sample a uniform and apply the quantile function.
- **symbols:**
  - `X` — a random variable with continuous CDF, type: Omega -> R
  - `U` — a uniform variable, type: Omega -> (0,1)
  - `F` — any target CDF, type: R -> [0,1]
- **hypotheses:** (none / unconditional within scope)

## transformation_univariate

- **status:** `well_formed`
- **note:** derived by differentiating the CDF relation F_Y(y) = F_X(g^{-1}(y)) (increasing g) or 1 - F_X(g^{-1}(y)) (decreasing g); the absolute value handles both.
- **symbols:**
  - `g` — the transformation, type: strictly monotone C^1 function
  - `Y` — g(X), type: Omega -> R
- **hypotheses:** (none / unconditional within scope)

## jacobian_transformation

- **status:** `well_formed`
- **note:** the multivariate change-of-variables formula for integrals, applied to P(Y in B) = P(X in g^{-1}(B)) = integral_{g^{-1}(B)} f_X = integral_B f_X(g^{-1}(y)) |det J_{g^{-1}}(y)| dy.
- **symbols:**
  - `g` — a diffeomorphism, type: R^n -> R^n, C^1 with C^1 inverse
  - `J_{g^{-1}}` — the Jacobian matrix of g^{-1}, type: n x n matrix
- **hypotheses:** (none / unconditional within scope)

## joint_distribution

- **status:** `well_formed`
- **note:** the joint law carries strictly more information than the collection of marginal laws -- it also encodes the dependence structure (correlation, copula). Rectangles B_1 x ... x B_n form a pi-system generating B(R^n), so the joint CDF determines it.
- **symbols:**
  - `X` — the random vector, type: Omega -> R^n
  - `P_X` — the joint law, type: probability measure on B(R^n)
- **hypotheses:** (none / unconditional within scope)

## marginal_distribution

- **status:** `well_formed`
- **note:** marginalization is projection of the joint law; it discards all dependence information. Fubini-Tonelli justifies the integration (nonnegative integrand).
- **symbols:**
  - `f_X` — the joint density, type: R^n -> [0, inf)
  - `f_{X_i}` — a marginal density, type: R -> [0, inf)
- **hypotheses:** (none / unconditional within scope)

## conditional_distribution

- **status:** `well_formed`
- **note:** for each fixed x with f_X(x) > 0, y |-> f_{Y|X}(y|x) is a genuine probability density (nonnegative, integrates to 1). Conditioning on the measure-zero event { X = x } is legitimate here because of the density; the general case needs conditional_expectation_abstract / regular conditional distributions.
- **symbols:**
  - `f_{Y|X}` — the conditional density, type: (R x R) -> [0, inf)
  - `f_X` — the marginal density of X, type: R -> [0, inf)
- **hypotheses:** (none / unconditional within scope)

## independence_events

- **status:** `well_formed`
- **note:** defined by FACTORIZATION, not by conditioning -- this keeps independence available for null events and sigma-algebras, and avoids the independence <-> conditional-probability circularity (see edges/cycles.md). 'P(A|B) = P(A)' is then a theorem, valid when P(B) > 0.
- **symbols:**
  - `A_i` — events, type: element of F
  - `S` — any subset of the index set, type: index set
- **hypotheses:** (none / unconditional within scope)

## independence_sigma_algebras

- **status:** `well_formed`
- **note:** the right level of generality: independence of random variables is independence of the sigma-algebras they generate. By the pi-lambda theorem it suffices to verify the factorization on generating pi-systems (this is what makes it checkable).
- **symbols:**
  - `G_i` — sub-sigma-algebras, type: sigma-algebra subset F
  - `A_i` — A_i in G_i, type: element of G_i
- **hypotheses:** (none / unconditional within scope)

## independence_random_variables

- **status:** `well_formed`
- **note:** the sets { X_i in B_i } for B_i Borel form a generating pi-system for sigma(X_i), so factorization on rectangles (checked via CDFs or densities) is enough by pi-lambda. Functions of disjoint independent blocks stay independent.
- **symbols:**
  - `X_i` — random variables, type: Omega -> R
  - `B_i` — Borel sets, type: element of B(R)
- **hypotheses:** (none / unconditional within scope)

## independence_factorization

- **status:** `well_formed`
- **note:** the half-line rectangles (-inf, x] x (-inf, y] are a pi-system generating B(R^2); the factorization of the joint CDF there extends to full independence by the pi-lambda theorem.
- **symbols:**
  - `F_{X,Y}, f_{X,Y}` — joint CDF / density, type: R^2 -> [0,1] / [0, inf)
- **hypotheses:** (none / unconditional within scope)

## pairwise_not_mutual

- **status:** `well_formed`
- **note:** each of Z, X, Y is Uniform{-1,1} and any two are independent (checking the four sign combinations), but the three are functionally linked: XYZ = 1 always, so knowing two determines the third.
- **symbols:**
  - `X, Y` — iid Uniform{-1,1}, type: Omega -> {-1,1}
  - `Z` — XY, type: Omega -> {-1,1}
- **hypotheses:** (none / unconditional within scope)

## iid

- **status:** `well_formed`
- **note:** 'identically distributed' constrains the marginals; 'independent' constrains the dependence. An iid sequence on a single probability space exists for any law (product / Kolmogorov extension construction).
- **symbols:**
  - `(X_n)` — an iid sequence, type: N -> (Omega -> R)
  - `P_{X_1}` — the common law, type: probability measure on B(R)
- **hypotheses:** (none / unconditional within scope)

## convolution_formula

- **status:** `well_formed`
- **note:** P(X + Y <= z) = integral integral_{x + y <= z} f_X(x) f_Y(y) dy dx (product law, Fubini); differentiate in z. Convolution is commutative and associative, matching X + Y = Y + X and sums of three.
- **symbols:**
  - `f_X, f_Y` — the marginal densities, type: R -> [0, inf)
  - `*` — convolution, type: binary operation on densities
- **hypotheses:** (none / unconditional within scope)

## expectation

- **status:** `well_formed`
- **note:** E[X] is the Lebesgue integral of X against P; all its properties (linearity, monotonicity, MCT/DCT/Fatou) are the integral's, specialised. E[X] may FAIL to exist (Cauchy: E[X^+] = E[X^-] = inf).
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `E[X]` — its mean, type: real or +-inf or undefined
- **hypotheses:** (none / unconditional within scope)

## lotus

- **status:** `well_formed`
- **note:** the change-of-variables formula for the pushforward: integral_Omega (g o X) dP = integral_R g d(P o X^{-1}). Requires E[|g(X)|] < inf for a finite answer.
- **symbols:**
  - `g` — a measurable function, type: R -> R
  - `X` — a random variable, type: Omega -> R
- **hypotheses:** (none / unconditional within scope)

## expectation_linearity

- **status:** `well_formed`
- **note:** aX + bY is integrable because |aX + bY| <= |a||X| + |b||Y| and L^1 is a vector space (triangle inequality + monotonicity of the integral).
- **symbols:**
  - `X` — {'meaning': 'integrable random variable', 'type': 'L^1(P)'}
  - `Y` — {'meaning': 'integrable random variable', 'type': 'L^1(P)'}
  - `a` — {'meaning': 'scalar', 'type': 'real'}
  - `b` — {'meaning': 'scalar', 'type': 'real'}
- **hypotheses:** X_integrable, Y_integrable

## expectation_monotonicity

- **status:** `well_formed`
- **note:** monotonicity of the Lebesgue integral: Y - X >= 0 a.s. so E[Y - X] = integral (Y-X) dP >= 0, then linearity. The a.s. qualifier is enough (null sets do not affect the integral).
- **symbols:**
  - `X, Y` — integrable random variables, type: L^1(P)
- **hypotheses:** (none / unconditional within scope)

## markov_inequality

- **status:** `well_formed`
- **note:** E[X] is well defined in [0, inf] because X >= 0 (no integrability precondition needed); if E[X] = inf the bound is vacuous.
- **symbols:**
  - `X` — {'meaning': 'a nonnegative random variable', 'type': 'Omega -> [0, inf)'}
  - `a` — {'meaning': 'threshold', 'type': 'positive real'}
- **hypotheses:** X_nonnegative_a_s, a_positive

## jensen_inequality

- **status:** `well_formed`
- **note:** take a supporting line L(x) = phi(E[X]) + m(x - E[X]) <= phi(x) at the point E[X]; then E[phi(X)] >= E[L(X)] = L(E[X]) = phi(E[X]) by linearity and monotonicity of expectation.
- **symbols:**
  - `phi` — a convex function, type: R -> R (or on an interval containing the range of X)
  - `X` — an integrable random variable, type: L^1(P)
- **hypotheses:** (none / unconditional within scope)

## variance

- **status:** `well_formed`
- **note:** the mean squared deviation from the mean; needs a finite second moment (which by moment_ladder implies a finite first moment, so E[X] exists). It is the L^2(P) squared distance from X to the constant E[X].
- **symbols:**
  - `X` — a random variable with E[X^2] < inf, type: L^2(P)
  - `sd(X)` — standard deviation, type: nonnegative real
- **hypotheses:** (none / unconditional within scope)

## variance_computational

- **status:** `well_formed`
- **note:** expand (X - E[X])^2 = X^2 - 2 E[X] X + E[X]^2 and apply linearity of expectation, treating E[X] as a constant.
- **symbols:**
  - `X` — a random variable in L^2(P), type: L^2(P)
- **hypotheses:** (none / unconditional within scope)

## variance_affine

- **status:** `well_formed`
- **note:** E[aX + b] = a E[X] + b, so (aX + b) - E[aX + b] = a(X - E[X]); square and take expectations.
- **symbols:**
  - `a, b` — constants, type: real
  - `X` — a random variable in L^2(P), type: L^2(P)
- **hypotheses:** (none / unconditional within scope)

## chebyshev_inequality

- **status:** `well_formed`
- **note:** Var(X) < inf implies E[X] finite (moment_ladder), so E[X] and the centred variable X - E[X] are well defined.
- **symbols:**
  - `X` — {'meaning': 'a random variable with a finite second moment', 'type': 'Omega -> R'}
  - `k` — {'meaning': 'deviation threshold', 'type': 'positive real'}
- **hypotheses:** finite_variance, k_positive

## covariance

- **status:** `well_formed`
- **note:** a measure of linear co-variation; the product XY is integrable by Cauchy-Schwarz when X, Y in L^2. Cov > 0 / < 0 / = 0 means positive / negative / no linear association (NOT independence).
- **symbols:**
  - `X, Y` — random variables in L^2(P), type: L^2(P)
- **hypotheses:** (none / unconditional within scope)

## covariance_bilinear

- **status:** `well_formed`
- **note:** bilinearity is linearity of expectation applied in each argument after centering; constants have zero covariance with everything, so Cov(X + c, Y) = Cov(X, Y).
- **symbols:**
  - `X, Y, Z` — random variables in L^2(P), type: L^2(P)
  - `a, b` — constants, type: real
- **hypotheses:** (none / unconditional within scope)

## cauchy_schwarz_expectation

- **status:** `well_formed`
- **note:** the L^2(P) inner-product Cauchy-Schwarz: the quadratic t |-> E[(X + tY)^2] = E[X^2] + 2t E[XY] + t^2 E[Y^2] is nonnegative for all real t, so its discriminant is <= 0.
- **symbols:**
  - `X, Y` — random variables in L^2(P), type: L^2(P)
- **hypotheses:** (none / unconditional within scope)

## correlation

- **status:** `well_formed`
- **note:** the scale-invariant, dimensionless version of covariance -- the cosine of the angle between the centered variables in L^2(P). The bound |rho| <= 1 is Cauchy-Schwarz applied to the centered variables.
- **symbols:**
  - `rho` — the correlation coefficient, type: real in [-1,1]
  - `X, Y` — random variables with positive finite variance, type: L^2(P)
- **hypotheses:** (none / unconditional within scope)

## variance_of_sum

- **status:** `well_formed`
- **note:** expand Var(sum X_i) = Cov(sum X_i, sum X_j) by bilinearity; the diagonal terms are Var(X_i), the off-diagonal terms pair up.
- **symbols:**
  - `X_i` — random variables in L^2(P), type: L^2(P)
  - `n` — a fixed positive integer, type: natural number
- **hypotheses:** (none / unconditional within scope)

## independence_expectation

- **status:** `well_formed`
- **note:** the joint law is the product P_X tensor P_Y; E[XY] = integral integral xy dP_X dP_Y = (integral x dP_X)(integral y dP_Y) by Fubini-Tonelli (applicable since the product |x||y| integrates).
- **symbols:**
  - `X, Y` — independent integrable random variables, type: L^1(P)
- **hypotheses:** (none / unconditional within scope)

## uncorrelated_not_independent

- **status:** `well_formed`
- **note:** correlation measures only LINEAR association; the relationship here is purely quadratic (even), so it is invisible to covariance. P(Y < 1/4 | X > 1/2) = 0 != P(Y < 1/4), witnessing dependence.
- **symbols:**
  - `X` — Uniform(-1,1), type: Omega -> (-1,1)
  - `Y` — X^2, type: Omega -> [0,1)
- **hypotheses:** (none / unconditional within scope)

## moment

- **status:** `well_formed`
- **note:** m_k is defined (finite) when E[|X|^k] < inf; by the moment ladder this then implies all lower moments are finite. mu_1 = 0, mu_2 = Var.
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `k` — a nonnegative integer, type: natural number
- **hypotheses:** (none / unconditional within scope)

## lp_space

- **status:** `well_formed`
- **note:** elements are a.s.-equivalence classes, not functions. The triangle inequality is Minkowski; completeness (Riesz-Fischer) is cited. On a PROBABILITY space the L^p are nested (moment_ladder), unlike on infinite measure spaces.
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `p` — an exponent, type: real >= 1
- **hypotheses:** (none / unconditional within scope)

## moment_ladder

- **status:** `well_formed`
- **note:** apply Jensen's inequality to the convex function phi(u) = |u|^{p/q} and the variable |X|^q: E[|X|^q]^{p/q} = phi(E[|X|^q]) <= E[phi(|X|^q)] = E[|X|^p]. Uses P(Omega) = 1 crucially.
- **symbols:**
  - `X` — a random variable, type: Omega -> R
  - `p, q` — exponents with 1 <= q <= p, type: real
- **hypotheses:** (none / unconditional within scope)

## holder_inequality

- **status:** `well_formed`
- **note:** Young's inequality ab <= a^p/p + b^q/q (a convexity fact) applied pointwise to a = |X|/||X||_p, b = |Y|/||Y||_q, then take expectations: E[|XY|]/(||X||_p ||Y||_q) <= 1/p + 1/q = 1.
- **symbols:**
  - `X` — in L^p(P), type: L^p(P)
  - `Y` — in L^q(P), type: L^q(P)
  - `p, q` — conjugate exponents, type: real > 1
- **hypotheses:** (none / unconditional within scope)

## mgf

- **status:** `well_formed`
- **note:** M_X(0) = 1 always; M_X(t) may be +inf for all t != 0 (e.g. Cauchy, lognormal). The useful hypothesis is 'M_X finite on (-h, h) for some h > 0' (X is then sub-exponential).
- **symbols:**
  - `M_X` — the MGF, type: (subset of R) -> (0, inf]
  - `t` — a real parameter, type: real
- **hypotheses:** (none / unconditional within scope)

## mgf_moments

- **status:** `well_formed`
- **note:** differentiate under the expectation: d^k/dt^k E[e^{tX}] = E[X^k e^{tX}], justified by DCT since finiteness on (-h, h) provides a dominating function e^{h'|X|} for |t| < h' < h.
- **symbols:**
  - `M_X` — the MGF, type: (-h, h) -> R
  - `k` — a nonnegative integer, type: natural number
- **hypotheses:** (none / unconditional within scope)

## mgf_uniqueness

- **status:** `well_formed`
- **note:** finiteness on a neighborhood of 0 forces the law to have exponentially decaying tails, and such laws are determined by their moment sequence (the moment problem is determinate); alternatively the MGF extends to a strip in C and equals the CF, which always determines the law (cf_properties).
- **symbols:**
  - `M_X, M_Y` — MGFs finite near 0, type: (-h, h) -> R
- **hypotheses:** (none / unconditional within scope)

## characteristic_function

- **status:** `well_formed`
- **note:** the Fourier transform of the law P_X. Unlike the MGF it always exists because |e^{itX}| = 1 is bounded. It determines the law (inversion), is uniformly continuous, and turns sums of independents into products.
- **symbols:**
  - `phi_X` — the characteristic function, type: R -> C, |phi_X| <= 1
  - `t` — a real parameter, type: real
- **hypotheses:** (none / unconditional within scope)

## cf_properties

- **status:** `well_formed`
- **note:** uniform continuity: |phi(t+h) - phi(t)| <= E|e^{ihX} - 1| -> 0 by DCT. Inversion: for a < b continuity points, P_X((a,b]) = lim_T (1/2 pi) integral_{-T}^{T} (e^{-ita} - e^{-itb})/(it) phi_X(t) dt.
- **symbols:**
  - `phi_X` — the characteristic function, type: R -> C
  - `a, b` — constants, type: real
- **hypotheses:** (none / unconditional within scope)

## mgf_sum_independent

- **status:** `well_formed`
- **note:** e^{t(X+Y)} = e^{tX} e^{tY} is a product of independent (functions of independent) variables, so its expectation factors by independence_expectation. Same for e^{it(X+Y)}.
- **symbols:**
  - `X, Y` — independent random variables, type: Omega -> R
- **hypotheses:** (none / unconditional within scope)

## chernoff_bound

- **status:** `well_formed`
- **note:** for fixed t > 0, { X >= a } = { e^{tX} >= e^{ta} }; apply Markov to the nonnegative variable e^{tX}: P(X >= a) <= E[e^{tX}]/e^{ta} = e^{-ta} M_X(t). Then optimize over t.
- **symbols:**
  - `X` — a random variable with M_X(t) < inf for some t > 0, type: Omega -> R
  - `a` — a threshold, type: real
- **hypotheses:** (none / unconditional within scope)

## hoeffding_lemma

- **status:** `well_formed`
- **note:** by convexity of x |-> e^{tx} on [a, b], e^{tX} <= (b - X)/(b - a) e^{ta} + (X - a)/(b - a) e^{tb}; take expectations (E[X] = 0), define psi(t) = log of the result, and show psi''(t) <= (b - a)^2 / 4 by a variance argument, so psi(t) <= t^2 (b-a)^2 / 8.
- **symbols:**
  - `X` — a bounded centered random variable, type: Omega -> [a, b]
  - `t` — a real parameter, type: real
- **hypotheses:** (none / unconditional within scope)

## hoeffding_inequality

- **status:** `well_formed`
- **note:** Chernoff on S - E[S]: P(S - E[S] >= s) <= e^{-ts} prod_i E[e^{t(X_i - E X_i)}] <= e^{-ts} exp(t^2 sum (b_i - a_i)^2 / 8) by independence (MGFs multiply) and Hoeffding's lemma; optimize t = 4s / sum (b_i - a_i)^2.
- **symbols:**
  - `X_i` — independent bounded random variables, type: Omega -> [a_i, b_i]
  - `s` — the deviation, type: positive real
- **hypotheses:** (none / unconditional within scope)

## bernoulli_distribution

- **status:** `well_formed`
- **note:** the building block: any event A gives 1_A ~ Bernoulli(P(A)). E[X] = E[X^2] = p (since X^2 = X), so Var = p - p^2.
- **symbols:**
  - `X` — a Bernoulli variable, type: Omega -> {0,1}
  - `p` — success probability, type: real in [0,1]
- **hypotheses:** (none / unconditional within scope)

## binomial_distribution

- **status:** `well_formed`
- **note:** X = sum_{i=1}^n Y_i with Y_i iid Bernoulli(p); the mean and variance follow from linearity and independence (variance_of_sum), not from the combinatorial sum.
- **symbols:**
  - `X` — a binomial count, type: Omega -> {0,1,...,n}
  - `n` — number of trials, type: positive integer
  - `p` — success probability, type: real in [0,1]
- **hypotheses:** (none / unconditional within scope)

## geometric_distribution

- **status:** `well_formed`
- **note:** the unique memoryless distribution on the positive integers: P(X > m + k | X > m) = P(X > k). (Convention varies: some define X as the number of FAILURES before the first success, support {0,1,2,...}, E = (1-p)/p.)
- **symbols:**
  - `X` — the first-success index, type: Omega -> {1,2,...}
  - `p` — success probability, type: real in (0,1]
- **hypotheses:** (none / unconditional within scope)

## poisson_distribution

- **status:** `well_formed`
- **note:** the law of counts of rare events: the limit of Binomial(n, lambda/n) as n -> inf (poisson_limit_theorem), and the one-parameter family with equal mean and variance. Sums of independent Poissons are Poisson (rates add).
- **symbols:**
  - `X` — a Poisson count, type: Omega -> {0,1,2,...}
  - `lambda` — the rate / mean, type: positive real
- **hypotheses:** (none / unconditional within scope)

## poisson_limit_theorem

- **status:** `well_formed`
- **note:** the 'law of rare events': many trials, each very unlikely, with a stable expected count. Proof by direct pmf limit, or by MGF: (1 - p_n + p_n e^t)^n = (1 + (n p_n)(e^t - 1)/n)^n -> exp(lambda(e^t - 1)).
- **symbols:**
  - `X_n` — Binomial(n, p_n), type: Omega -> {0,...,n}
  - `lambda` — the limiting mean, type: positive real
- **hypotheses:** (none / unconditional within scope)

## continuous_uniform_distribution

- **status:** `well_formed`
- **note:** the maximum-entropy law on a bounded interval; the target of the probability integral transform (F_X(X) ~ Uniform(0,1)) and the source for inversion sampling (F^{-1}(U) ~ any law).
- **symbols:**
  - `X` — a uniform variable, type: Omega -> [a,b]
  - `a < b` — the endpoints, type: real
- **hypotheses:** (none / unconditional within scope)

## exponential_distribution

- **status:** `well_formed`
- **note:** the unique memoryless distribution on [0, inf): P(X > s + t | X > s) = P(X > t). The waiting time between events of a rate-lambda Poisson process; the continuous analogue of the geometric.
- **symbols:**
  - `X` — an exponential variable, type: Omega -> [0, inf)
  - `lambda` — the rate, type: positive real
- **hypotheses:** (none / unconditional within scope)

## memorylessness

- **status:** `well_formed`
- **note:** the survival function G(x) = P(X > x) satisfies G(s + t) = G(s) G(t) (Cauchy's functional equation); the only monotone solutions are G(x) = e^{-lambda x} (continuous) or G(k) = (1-p)^k (discrete).
- **symbols:**
  - `X` — a nonnegative random variable, type: Omega -> [0, inf) or {1,2,...}
  - `s, t` — nonnegative reals/integers
- **hypotheses:** (none / unconditional within scope)

## gamma_distribution

- **status:** `well_formed`
- **note:** the flexible right-skewed family on (0, inf): shape k < 1 gives a pole at 0, k = 1 is exponential, k large approaches normal. Closed under sums with common scale (shapes add). Rate parameterization uses beta = 1/theta.
- **symbols:**
  - `X` — a gamma variable, type: Omega -> (0, inf)
  - `k` — shape, type: positive real
  - `theta` — scale, type: positive real
- **hypotheses:** (none / unconditional within scope)

## beta_distribution

- **status:** `well_formed`
- **note:** the canonical family for a random PROBABILITY or proportion. Beta(1,1) = Uniform(0,1). It is the conjugate prior for a Bernoulli/binomial rate: prior Beta(a,b) + k successes in n trials -> posterior Beta(a + k, b + n - k).
- **symbols:**
  - `X` — a beta variable, type: Omega -> (0,1)
  - `a, b` — shape parameters, type: positive real
- **hypotheses:** (none / unconditional within scope)

## normal_distribution

- **status:** `well_formed`
- **note:** parameterized by the VARIANCE sigma^2 (not sigma). The universal limit law (CLT), the maximum-entropy law for a given mean and variance, closed under affine maps and independent sums, and the only law where zero correlation implies independence (jointly).
- **symbols:**
  - `X` — a normal variable, type: Omega -> R
  - `mu` — mean, type: real
  - `sigma^2` — variance, type: positive real
- **hypotheses:** (none / unconditional within scope)

## standard_normal

- **status:** `well_formed`
- **note:** the reference point: any N(mu, sigma^2) variable is mu + sigma Z, and any normal probability reduces to Phi. The CLT limit is stated as convergence to Z.
- **symbols:**
  - `Z` — a standard normal variable, type: Omega -> R
  - `Phi` — its CDF, type: R -> (0,1)
- **hypotheses:** (none / unconditional within scope)

## normal_affine_closure

- **status:** `well_formed`
- **note:** affine closure by transformation_univariate; the sum by multiplying MGFs: exp(mu_1 t + s_1^2 t^2/2) exp(mu_2 t + s_2^2 t^2/2) = exp((mu_1+mu_2) t + (s_1^2 + s_2^2) t^2/2), then mgf_uniqueness.
- **symbols:**
  - `X, Y` — normal random variables, type: Omega -> R
  - `a, b` — constants, a != 0, type: real
- **hypotheses:** (none / unconditional within scope)

## cauchy_no_mean

- **status:** `well_formed`
- **note:** the canonical finite-density law with no mean: the tails decay only like 1/x^2, so integral |x| f_X(x) dx = (2/pi) integral_0^inf x/(1+x^2) dx = inf. Its characteristic function phi_X(t) = e^{-|t|} exists (and is non-differentiable at 0, consistent with the missing mean).
- **symbols:**
  - `X` — a standard Cauchy variable, type: Omega -> R
  - `f_X` — its density, type: R -> (0, inf)
- **hypotheses:** (none / unconditional within scope)

## convergence_almost_sure

- **status:** `well_formed`
- **note:** the convergence set { omega : X_n(omega) -> X(omega) } is an event (a countable combination of { |X_n - X| < 1/k }); a.s. convergence requires it to have probability 1. This is the strongest of the four modes together with L^p.
- **symbols:**
  - `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
  - `X` — the limit random variable (or law), type: Omega -> R (or a law)
- **hypotheses:** (none / unconditional within scope)

## convergence_in_probability

- **status:** `well_formed`
- **note:** a statement about the MARGINAL of |X_n - X| for each n -- no joint trajectory needed beyond a common space. Weaker than a.s. (which controls the whole tail at once) and than L^p (Markov), stronger than in distribution.
- **symbols:**
  - `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
  - `X` — the limit random variable (or law), type: Omega -> R (or a law)
- **hypotheses:** (none / unconditional within scope)

## convergence_in_lp

- **status:** `well_formed`
- **note:** convergence in the L^p(P) norm; requires X_n, X in L^p. By Markov's inequality (applied to |X_n - X|^p) it implies convergence in probability; the converse needs uniform integrability.
- **symbols:**
  - `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
  - `X` — the limit random variable (or law), type: Omega -> R (or a law)
- **hypotheses:** (none / unconditional within scope)

## convergence_in_distribution

- **status:** `well_formed`
- **note:** the WEAKEST mode: it is a statement about the LAWS, not the random variables, so X_n and X need not live on the same space. The 'continuity point' clause is essential -- CDFs can converge everywhere except at jumps of the limit.
- **symbols:**
  - `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
  - `X` — the limit random variable (or law), type: Omega -> R (or a law)
- **hypotheses:** (none / unconditional within scope)

## convergence_implications

- **status:** `well_formed`
- **note:** each arrow is a short proof; the content is equally in the NON-arrows, witnessed by standard counterexamples (the typewriter sequence, escaping mass, a symmetric two-point law).
- **symbols:**
  - `X_n, X` — random variables on a common space (except the d-only statements), type: N -> (Omega -> R)
- **hypotheses:** (none / unconditional within scope)

## portmanteau_theorem

- **status:** `well_formed`
- **note:** the CDF definition is the special case A = (-inf, x] with P(X = x) = 0. Form (i) is the working definition of weak convergence on general metric spaces; forms (iii)-(v) are what make it a topology on laws.
- **symbols:**
  - `g` — a test function, type: R -> R bounded and continuous
  - `C, U, A` — closed / open / continuity Borel sets, type: element of B(R)
- **hypotheses:** (none / unconditional within scope)

## continuous_mapping_theorem

- **status:** `well_formed`
- **note:** for a.s. and in-probability, pointwise/along-subsequence continuity carries the limit through; for in-distribution, use the portmanteau form (bounded continuous test functions compose with g to bounded a.e.-continuous functions).
- **symbols:**
  - `g` — a measurable function continuous P_X-a.e., type: R -> R^k
  - `D_g` — the set of discontinuities of g, type: Borel set
- **hypotheses:** (none / unconditional within scope)

## slutsky_theorem

- **status:** `well_formed`
- **note:** the key asymmetry: one sequence may converge only in distribution, but the OTHER must converge in probability to a CONSTANT (not a random variable). Then (X_n, Y_n) -> (X, c) jointly in distribution and the continuous map applies.
- **symbols:**
  - `X_n` — sequence converging in distribution, type: N -> (Omega -> R)
  - `Y_n` — sequence converging in probability to a constant c, type: N -> (Omega -> R)
  - `c` — a constant, type: real
- **hypotheses:** (none / unconditional within scope)

## weak_law_large_numbers

- **status:** `well_formed`
- **note:** convergence mode: IN PROBABILITY (weaker than the SLLN's a.s.). Finite mean is enough; the classical finite-variance proof is a one-line Chebyshev bound, the general case uses truncation or characteristic functions.
- **symbols:**
  - `X_i` — an iid sequence, type: N -> L^1(P)
  - `mu` — the common mean E[X_1], type: real
  - `Xbar_n` — the sample mean, type: Omega -> R
- **hypotheses:** (none / unconditional within scope)

## strong_law_large_numbers

- **status:** `well_formed`
- **note:** convergence mode: ALMOST SURELY -- strictly stronger than the WLLN. A finite mean is necessary AND sufficient. Etemadi's proof needs only pairwise independence and uses truncation + a fourth-moment-free Borel-Cantelli argument (choice-free).
- **symbols:**
  - `X_i` — an iid sequence, type: N -> L^1(P)
  - `mu` — the common mean, type: real
- **hypotheses:** (none / unconditional within scope)

## levy_continuity_theorem

- **status:** `well_formed`
- **note:** the workhorse for proving convergence in distribution: reduce to a pointwise limit of characteristic functions (which factor over sums). The continuity of phi at 0 rules out mass escaping to infinity (tightness).
- **symbols:**
  - `phi_{X_n}` — characteristic functions, type: R -> C
  - `phi` — the pointwise limit, type: R -> C
- **hypotheses:** (none / unconditional within scope)

## central_limit_theorem

- **status:** `well_formed`
- **note:** the limit is a fixed N(0,1) LAW, not a random variable; "-->^{d}" is convergence of CDFs at every continuity point (here, everywhere, since the normal CDF is continuous). sigma > 0 is needed to divide.
- **symbols:**
  - `(X_i)` — {'meaning': 'an i.i.d. sequence', 'type': 'N -> L^2(P)'}
  - `mu` — {'meaning': 'common mean E[X_1]', 'type': 'real'}
  - `sigma^2` — {'meaning': 'common variance', 'type': 'positive finite real'}
  - `mean_n` — {'meaning': 'sample mean (X_1 + ... + X_n)/n', 'type': 'Omega -> R'}
- **hypotheses:** iid, finite_mean, finite_nonzero_variance

## lindeberg_clt

- **status:** `well_formed`
- **note:** the definitive CLT for NON-identically-distributed independent summands: the Lindeberg condition says no single term contributes a non-negligible fraction of the total variance. It implies (and under a uniform-asymptotic-negligibility assumption, is equivalent to) asymptotic normality; Lyapunov's (2 + delta)-moment condition is a convenient sufficient case.
- **symbols:**
  - `X_{n,i}` — a triangular array of row-independent, mean-0 variables, type: array of L^2(P)
  - `s_n^2` — the row variance sum, type: positive real
- **hypotheses:** (none / unconditional within scope)

## delta_method

- **status:** `well_formed`
- **note:** a first-order Taylor expansion g(T_n) approx g(theta) + g'(theta)(T_n - theta), made rigorous by Slutsky: sqrt(n)(g(T_n) - g(theta)) = [g'(theta) + o_p(1)] sqrt(n)(T_n - theta).
- **symbols:**
  - `T_n` — an asymptotically normal estimator, type: N -> (Omega -> R)
  - `g` — a transformation differentiable at theta, type: R -> R
  - `theta` — the true parameter, type: real
- **hypotheses:** (none / unconditional within scope)

## conditional_expectation_elementary

- **status:** `well_formed`
- **note:** the concrete, computational conditional expectation. E[X | Y] is a RANDOM VARIABLE (a function of Y); E[X | Y = y] is a NUMBER for each y. Matches the abstract E[X | sigma(Y)] where both are defined.
- **symbols:**
  - `X` — an integrable random variable, type: L^1(P)
  - `Y` — the conditioning variable, type: Omega -> R
  - `g` — the regression function y |-> E[X|Y=y], type: R -> R
- **hypotheses:** (none / unconditional within scope)

## conditional_expectation_abstract

- **status:** `well_formed`
- **note:** the defining property is (i) measurability + (ii) matching integrals on G-sets; conditioning on a variable is E[X | sigma(Y)]. This handles conditioning on probability-zero events, which the elementary definition cannot.
- **symbols:**
  - `X` — an integrable random variable, type: L^1(P)
  - `G` — a sub-sigma-algebra (the conditioning information), type: sigma-algebra subset F
  - `Z` — the conditional expectation E[X | G], type: L^1(Omega, G, P)
- **hypotheses:** (none / unconditional within scope)

## conditional_expectation_existence

- **status:** `well_formed`
- **note:** two standard constructions: (a) Radon-Nikodym -- nu(A) = integral_A X dP is a (signed) measure on (Omega, G) with nu << P|_G, so nu has a G-measurable density, which is E[X|G]; (b) for X in L^2, orthogonal projection onto the closed subspace L^2(G), then extend to L^1 by density and monotonicity.
- **symbols:**
  - `X` — an integrable random variable, type: L^1(P)
  - `G` — a sub-sigma-algebra, type: sigma-algebra subset F
- **hypotheses:** (none / unconditional within scope)

## tower_property

- **status:** `well_formed`
- **note:** the smaller sigma-algebra wins: conditioning on more then less information equals conditioning on less. Proof: E[X | H] is H-measurable (hence G-measurable) and its integral matches X on H-sets; check that E[X|G] has the same integrals on H-sets (it does, since H subset G).
- **symbols:**
  - `X` — an integrable random variable, type: L^1(P)
  - `H, G` — nested sub-sigma-algebras H subset G subset F, type: sigma-algebra
- **hypotheses:** (none / unconditional within scope)

## law_of_total_variance

- **status:** `well_formed`
- **note:** 'within-group + between-group variance'. Decomposes total variability into the average conditional (unexplained) variance plus the variance of the conditional means (explained). Proof: apply variance_computational and the tower property.
- **symbols:**
  - `X` — a square-integrable random variable, type: L^2(P)
  - `G` — a sub-sigma-algebra, type: sigma-algebra subset F
- **hypotheses:** (none / unconditional within scope)

## conditional_expectation_l2_projection

- **status:** `well_formed`
- **note:** the geometric meaning of conditioning: E[X | G] is the BEST PREDICTOR of X using only G-information, in mean-square. The residual X - E[X | G] is orthogonal to every G-measurable function (E[(X - E[X|G]) W] = 0 for W in L^2(G)).
- **symbols:**
  - `X` — a square-integrable random variable, type: L^2(P)
  - `G` — a sub-sigma-algebra, type: sigma-algebra subset F
- **hypotheses:** (none / unconditional within scope)

## martingale

- **status:** `well_formed`
- **note:** the model of a fair game: the best forecast of tomorrow given everything known today is today's value. By the tower property E[X_n] = E[X_0] for all n. The convergence theorem, optional stopping, and the maximal / Doob inequalities are the content of a future release.
- **symbols:**
  - `(X_n)` — an adapted integrable sequence, type: N -> L^1(P)
  - `(F_n)` — a filtration, type: increasing sequence of sub-sigma-algebras
- **hypotheses:** (none / unconditional within scope)

## stochastic_process

- **status:** `well_formed`
- **note:** for fixed omega, t |-> X_t(omega) is a sample path; for fixed t, X_t is a random variable. The finite-dimensional distributions (laws of (X_{t_1}, ..., X_{t_k})) are the observable data; Kolmogorov's extension theorem builds the process from consistent f.d.d.s.
- **symbols:**
  - `(X_t)` — the process, type: T -> (Omega -> R)
  - `T` — the index set (e.g. N, [0, inf)), type: set
- **hypotheses:** (none / unconditional within scope)

## kolmogorov_extension_theorem

- **status:** `well_formed`
- **note:** the existence theorem underlying every stochastic-process construction (iid sequences, Markov chains from a transition kernel, Gaussian processes from a covariance function). Consistency is exactly the compatibility needed; the built measure lives on the product sigma-algebra of R^T.
- **symbols:**
  - `mu_{t_1..t_k}` — the prescribed finite-dimensional laws, type: probability measures on R^k
  - `(X_t)` — the resulting process, type: T -> (Omega -> R)
- **hypotheses:** (none / unconditional within scope)
