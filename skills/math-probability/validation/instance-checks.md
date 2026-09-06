# Instance checks — index (generated from results/*.yaml)

Which concrete check backs each node. Kernel-checked cores and `decide`
instances live in `validation/proof-checks.lean` (see `proof-checks.md` for
the genuine-vs-instance split); numerical worksheets in
`validation/instance-checks.bc`. `cited` = established in the literature,
not re-checked here.


## set_algebra

- **well-definedness:** the powerset 2^Omega is a complete Boolean algebra under subset-or-equal; every identity used downstream (De Morgan, distributivity, A = (A cap B) cup (A cap B^c)) holds there.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## preimage_algebra

- **well-definedness:** f^{-1}(B) := { x : f(x) in B } is defined for every f and every B; the three commutation identities are immediate from the definition of membership.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## countable_set

- **well-definedness:** injectivity into N is a well-defined property; the Cantor pairing N x N -> N is an explicit bijection (see instance-checks in the sibling capsule).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## real_field

- **well-definedness:** R is the unique complete ordered field up to isomorphism (math-number-systems); [0, inf] is its two-point compactification, the range of a measure.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## sequence_limit

- **well-definedness:** limits are unique (a Hausdorff fact for R); the algebra of limits (sum, product, quotient with nonzero denominator) is standard.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## limsup_liminf

- **well-definedness:** limsup a_n = inf_N sup_{n>=N} a_n exists in [-inf, +inf]; the set versions are countable unions and intersections, hence in any sigma-algebra containing the A_n.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## series_convergence

- **well-definedness:** the sum is the limit of the monotone (for nonnegative terms) partial-sum sequence; rearrangement is safe for absolutely convergent series only.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convex_function

- **well-definedness:** a convex function on an open interval is continuous and has one-sided derivatives everywhere; the supporting-line family is nonempty at every interior point.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## abstract_integral

- **lean_status:** `cited` — Folland Real Analysis 2e SS2.2-2.4; Billingsley SS15-16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## monotone_convergence_theorem

- **lean_status:** `cited` — Folland Real Analysis 2e ch. 2; Billingsley SS16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## dominated_convergence_theorem

- **lean_status:** `cited` — Folland Real Analysis 2e ch. 2; Billingsley SS16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## fatou_lemma

- **lean_status:** `cited` — Folland Real Analysis 2e ch. 2; Billingsley SS16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## fubini_tonelli

- **lean_status:** `cited` — Folland Real Analysis 2e ch. 2; Billingsley SS16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## radon_nikodym

- **lean_status:** `cited` — Folland Real Analysis 2e ch. 2; Billingsley SS16
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## sigma_algebra

- **well-definedness:** {empty, Omega} is a sigma-algebra and 2^Omega is a sigma-algebra, so the notion is non-vacuous; an arbitrary intersection of sigma-algebras is a sigma-algebra, which is what makes sigma(C) well-defined.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## generated_sigma_algebra

- **lean_status:** `cited`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## borel_sigma_algebra

- **well-definedness:** all listed generating collections yield the same sigma-algebra (each contains a countable subfamily generating the others); B(R) is a proper subset of 2^R (a Vitali set is not Borel, using AC).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## measurable_space

- **well-definedness:** any set with any sigma-algebra on it is a measurable space; morphisms are measurable functions (preimage of measurable is measurable).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## measure

- **well-definedness:** mu(empty) = 0 follows from countable additivity unless mu is identically +inf; monotonicity and countable subadditivity are consequences. Counting measure, Lebesgue measure, and Dirac delta_x are the standard examples.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## dynkin_pi_lambda

- **lean_status:** `cited` — Billingsley Thm 3.2; Durrett A.1.4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## lebesgue_measure_caratheodory

- **lean_status:** `cited` — Folland Real Analysis 2e Thm 1.14, 1.19; Billingsley Thm 12.4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## measure_monotonicity

- **lean_status:** `core` — validation/proof-checks.lean Prob.union_bound (the two-set case)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## measure_continuity

- **lean_status:** `cited` — Billingsley Thm 10.2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## null_set

- **well-definedness:** mu(N) = 0 is well-defined; the a.e. quantifier is closed under countable conjunction: if P_n holds a.e. for each n, then all P_n hold simultaneously a.e.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## almost_sure

- **well-definedness:** P(A) = 1 is well-defined; the a.s. quantifier is closed under countable intersection: P(bigcap A_n) = 1 if P(A_n) = 1 for all n (complement is a countable union of null sets).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## kolmogorov_axioms

- **well-definedness:** P is a measure (measure node) with the extra normalization P(Omega)=1; consistency of the three requirements: the zero measure fails normalization, counting measure on an infinite Omega fails it too, so normalization is a genuine constraint. Countable additivity forces P(empty)=0 (take all A_n = empty).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## probability_measure

- **well-definedness:** a measure with P(Omega) = 1 exists on any measurable space (e.g. a Dirac point mass); the constraint is consistent and non-vacuous.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## probability_space

- **well-definedness:** any (Omega, F) with any probability measure P is a probability space; the canonical one for a real random variable with law mu is (R, B(R), mu).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## complement_rule

- **lean_status:** `core` — validation/proof-checks.lean Prob.union_bound / incl_excl_2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## finite_additivity

- **lean_status:** `core` — validation/proof-checks.lean Prob.incl_excl_2 (n=2)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## inclusion_exclusion

- **lean_status:** `core` — validation/proof-checks.lean Prob.incl_excl_2, Prob.incl_excl_3
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## boole_inequality

- **lean_status:** `core` — validation/proof-checks.lean Prob.union_bound (two-set case)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## continuity_of_probability

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## borel_cantelli_first

- **lean_status:** `core` — validation/proof-checks.lean Prob.union_bound is the Boole step
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## borel_cantelli_second

- **lean_status:** `cited` — Billingsley Thm 4.4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_probability

- **well-definedness:** P(. | B) satisfies the Kolmogorov axioms: nonnegative, P(Omega | B) = P(B)/P(B) = 1, countably additive (inherited from P). So all earlier results apply to it.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## multiplication_rule

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## law_of_total_probability

- **lean_status:** `core` — validation/proof-checks.lean Prob.bayes_denominator
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## bayes_theorem

- **lean_status:** `core` — validation/proof-checks.lean Prob.bayes_denominator (denominator = P(A)) + the disease-test decide instance
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## measurable_function

- **well-definedness:** the collection { B : f^{-1}(B) in F } is a sigma-algebra, so it suffices to check measurability on a generating collection of E' (the half-lines for B(R)).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## random_variable

- **well-definedness:** measurability makes { X <= x } an event for every x, so the CDF and the pushforward law are well-defined; sums, products, and limits of random variables are random variables.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## indicator_rv

- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## distribution_pushforward

- **well-definedness:** P_X inherits countable additivity from P via the preimage algebra (X^{-1} commutes with countable disjoint unions); P_X(R) = P(Omega) = 1.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cdf

- **well-definedness:** F_X is well-defined for every random variable (the half-lines are Borel); its four characterizing properties are cdf_properties.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cdf_properties

- **lean_status:** `cited` — Billingsley Thm 12.4; Durrett Thm 1.2.2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cdf_determines_law

- **lean_status:** `cited` — Billingsley Thm 12.4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## discrete_rv

- **well-definedness:** a countable S with P(X in S) = 1 makes P_X purely atomic; the smallest such S is { x : P(X = x) > 0 }.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## pmf

- **well-definedness:** sum_{x in S} P(X = x) = P(X in S) = 1 by countable additivity over the disjoint singletons; nonnegativity is immediate.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## absolutely_continuous_rv

- **well-definedness:** P_X << lambda is a well-defined relation between measures; by Radon-Nikodym (P_X finite, lambda sigma-finite) it is equivalent to the existence of a density.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## pdf

- **well-definedness:** existence and a.e.-uniqueness of f_X is exactly Radon-Nikodym for P_X << lambda; the normalization integral f_X = P_X(R) = 1.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## quantile_function

- **well-definedness:** { x : F_X(x) >= u } is nonempty (F_X -> 1) and bounded below (F_X -> 0), and closed to the right (F_X right-continuous), so the inf is attained and finite for u in (0,1).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## probability_integral_transform

- **lean_status:** `cited` — Durrett Thm 1.2.2; Devroye Non-Uniform Random Variate Generation ch. 2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## transformation_univariate

- **lean_status:** `cited` — Durrett; Grimmett-Stirzaker 4.7
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## jacobian_transformation

- **lean_status:** `cited` — Folland; Billingsley Thm 17.2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## joint_distribution

- **well-definedness:** (X_1,...,X_n) is measurable iff each X_i is (B(R^n) is generated by the coordinate projections); the pushforward is a probability measure on B(R^n).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## marginal_distribution

- definition/axiom — see the type check
- **lean_status:** `cited` — Billingsley Thm 18.3
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_distribution

- **well-definedness:** integral f_{Y|X}(y|x) dy = integral f_{X,Y}(x,y) dy / f_X(x) = f_X(x)/f_X(x) = 1 for a.e. x; the exceptional set { f_X = 0 } is P_X-null.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## independence_events

- **well-definedness:** the condition is a finite conjunction of numeric identities per subset; it is preserved under complementation of any subset of the A_i.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## independence_sigma_algebras

- **well-definedness:** the set of A_1 for which the factorization holds (with A_2, ..., A_n fixed in generating pi-systems) is a lambda-system; pi-lambda extends it to all of G_1, then iterate.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## independence_random_variables

- **well-definedness:** the product measure P_{X_1} tensor ... tensor P_{X_n} exists and is a probability measure on B(R^n); independence says the joint law equals it.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## independence_factorization

- **lean_status:** `cited` — Billingsley Thm 20.1; Durrett Thm 2.1.7
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## pairwise_not_mutual

- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## iid

- **well-definedness:** the infinite product measure (P_{X_1})^{tensor N} on (R^N, B(R)^{tensor N}) exists (Kolmogorov extension) and realizes an iid sequence via coordinate projections.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convolution_formula

- **lean_status:** `cited` — Grimmett-Stirzaker 4.8; Durrett Thm 2.1.10
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## expectation

- **well-definedness:** for X >= 0, integral X dP in [0, inf] always exists (sup over simple functions); for signed X, E[X] = E[X^+] - E[X^-] provided not both are +inf. X integrable <=> X in L^1(P).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## lotus

- **lean_status:** `cited` — Billingsley Thm 16.13
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## expectation_linearity

- **lean_status:** `core` — validation/proof-checks.lean Prob.expectation_linearity (GENUINE: universal in the scalars a,b, list induction + grind) + the general measure-theoretic case cited (integral linearity)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## expectation_monotonicity

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## markov_inequality

- **lean_status:** `core` — validation/proof-checks.lean Prob.markov_finite (finite-support case, universal, induction)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## jensen_inequality

- **lean_status:** `core` — validation/proof-checks.lean Prob.jensen_sq (phi = square, GENUINE universal in t,x,y,n via the factorization t(n-t)(x-y)^2)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## variance

- **well-definedness:** (X - E[X])^2 >= 0 so its expectation is well-defined in [0, inf]; finite iff E[X^2] < inf (expand and use E[X]^2 < inf).
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## variance_computational

- **lean_status:** `core` — validation/proof-checks.lean Prob.centid (GENUINE, universal list-induction identity Sum p(x-m)^2 = Sum px^2 - 2m Sum px + m^2 Sum p)
- **bc:** see `validation/instance-checks.bc`

## variance_affine

- **lean_status:** `core` — validation/proof-checks.lean Prob.var_affine (GENUINE: the 2ab.n.sx and b^2 n^2 terms cancel)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## chebyshev_inequality

- **lean_status:** `core` — validation/proof-checks.lean Prob.chebyshev_reduction_fwd (GENUINE: the {|y|>=k} => {y^2>=k^2} direction Chebyshev uses) + the decide grid; the Markov core is Prob.markov_finite
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## covariance

- **well-definedness:** XY in L^1 by Cauchy-Schwarz (|E[XY]| <= ||X||_2 ||Y||_2 < inf); the centered form equals the raw form by linearity.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## covariance_bilinear

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cauchy_schwarz_expectation

- **lean_status:** `core` — validation/proof-checks.lean Prob.corr_bound_iff + the 2-point CS/Jensen decide grid; full universal CS over Z is a real-number fact (cited)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## correlation

- **well-definedness:** requires sd(X), sd(Y) > 0 (non-degenerate) and finite; then |Cov(X,Y)| <= sd(X) sd(Y) by Cauchy-Schwarz, so rho in [-1, 1].
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## variance_of_sum

- **lean_status:** `core` — validation/proof-checks.lean Prob.var_of_sum_raw and Prob.cov_bilinear_raw (GENUINE raw-moment identities)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## independence_expectation

- **lean_status:** `cited` — Billingsley Thm 21.2; Durrett Thm 2.1.9
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## uncorrelated_not_independent

- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## moment

- **well-definedness:** E[|X|^k] in [0, inf] always exists; m_k finite iff X in L^k(P). The central moments are polynomials in the raw moments via the binomial expansion.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## lp_space

- **well-definedness:** ||.||_p is a genuine norm on the quotient by a.s.-equality (||X||_p = 0 iff X = 0 a.s., by expectation_monotonicity); Minkowski gives the triangle inequality.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## moment_ladder

- **lean_status:** `core` — validation/proof-checks.lean Prob.jensen_sq (GENUINE, universal in t,x,y,n) is the p/q = 2 core
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## holder_inequality

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## mgf

- **well-definedness:** e^{tX} > 0 so E[e^{tX}] in (0, inf] is always defined; the set { t : M_X(t) < inf } is an interval containing 0.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## mgf_moments

- **lean_status:** `cited` — Billingsley Thm 21.1; Durrett 3.3
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## mgf_uniqueness

- **lean_status:** `cited` — Billingsley Thm 30.1; Curtiss 1942
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## characteristic_function

- **well-definedness:** |e^{itX}| = 1 so e^{itX} is bounded, hence integrable against the probability measure P; phi_X is defined for all t.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cf_properties

- **lean_status:** `cited` — Billingsley Thm 26.2, 26.1; Durrett 3.3
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## mgf_sum_independent

- **lean_status:** `core` — validation/proof-checks.lean -- binomial MGF^n instance
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## chernoff_bound

- **lean_status:** `core` — validation/proof-checks.lean Prob.markov_finite (Markov core; e^{tX} transform is one line)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## hoeffding_lemma

- **lean_status:** `cited` — Hoeffding 1963 Lemma; Boucheron-Lugosi-Massart Lemma 2.2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## hoeffding_inequality

- **lean_status:** `core` — validation/proof-checks.lean Prob.markov_finite (Markov/Chernoff core); the assembly is algebra
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## bernoulli_distribution

- **well-definedness:** a two-point law with masses p and 1 - p summing to 1; well-defined for every p in [0,1].
- **bc:** see `validation/instance-checks.bc`

## binomial_distribution

- definition/axiom — see the type check
- **lean_status:** `core` — validation/proof-checks.lean -- Binomial(4,1/2) mean/var decide instances + Prob.var_of_sum_raw
- **bc:** see `validation/instance-checks.bc`

## geometric_distribution

- **well-definedness:** sum_{k>=1} (1-p)^{k-1} p = p / (1 - (1-p)) = 1 (geometric series); needs p > 0.
- **bc:** see `validation/instance-checks.bc`

## poisson_distribution

- definition/axiom — see the type check
- **lean_status:** `core` — validation/instance-checks.bc -- Poisson(2) E and Var = 2
- **bc:** see `validation/instance-checks.bc`

## poisson_limit_theorem

- **lean_status:** `cited` — Durrett Thm 3.6.1; Billingsley Thm 23.2
- **bc:** see `validation/instance-checks.bc`

## continuous_uniform_distribution

- **well-definedness:** f_X >= 0 and integral_a^b 1/(b-a) dx = 1; well-defined for any a < b.
- **bc:** see `validation/instance-checks.bc`

## exponential_distribution

- definition/axiom — see the type check
- **lean_status:** `core` — validation/instance-checks.bc -- Exponential(0.5): E=2, Var=4, memoryless check
- **bc:** see `validation/instance-checks.bc`

## memorylessness

- **lean_status:** `cited` — Grimmett-Stirzaker 4.8; Feller I.XIII
- **bc:** see `validation/instance-checks.bc`

## gamma_distribution

- definition/axiom — see the type check
- **lean_status:** `cited` — Grimmett-Stirzaker 4.14
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## beta_distribution

- **well-definedness:** the Beta function B(a,b) = integral_0^1 x^{a-1}(1-x)^{b-1} dx converges for a, b > 0 and normalizes the density.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## normal_distribution

- definition/axiom — see the type check
- **lean_status:** `core` — validation/instance-checks.bc -- standard normal pdf integrates to 1, second moment 1
- **bc:** see `validation/instance-checks.bc`

## standard_normal

- definition/axiom — see the type check
- **lean_status:** `core` — validation/instance-checks.bc -- Phi(1) = 0.8413...
- **bc:** see `validation/instance-checks.bc`

## normal_affine_closure

- **lean_status:** `core`
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## cauchy_no_mean

- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convergence_almost_sure

- definition/axiom — see the type check
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convergence_in_probability

- definition/axiom — see the type check
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convergence_in_lp

- definition/axiom — see the type check
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convergence_in_distribution

- definition/axiom — see the type check
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## convergence_implications

- **lean_status:** `core` — validation/proof-checks.lean Prob.markov_finite + Prob.union_bound (the Boole/BC1 step)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## portmanteau_theorem

- **lean_status:** `cited` — Billingsley Convergence of Probability Measures Thm 2.1; Durrett Thm 3.2.5
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## continuous_mapping_theorem

- **lean_status:** `cited` — Billingsley CPM Thm 2.7; Durrett Thm 3.2.10
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## slutsky_theorem

- **lean_status:** `cited` — Durrett Thm 3.2.8 (Ex); Billingsley Thm 25.4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## weak_law_large_numbers

- **lean_status:** `core` — validation/proof-checks.lean Prob.chebyshev_reduction_fwd + Prob.var_of_sum_raw
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## strong_law_large_numbers

- **lean_status:** `cited` — Durrett Thm 2.4.1 (Etemadi); Williams 12.10 (martingale proof)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## levy_continuity_theorem

- **lean_status:** `cited` — Billingsley Thm 26.3; Durrett Thm 3.3.6
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## central_limit_theorem

- **lean_status:** `cited` — CITED -- Billingsley Probability and Measure 3e Thm 27.1; Durrett PTE 5e Thm 3.4.1. Not formalized here (no Mathlib real-analysis / CF machinery in the Lean core).
- **bc:** see `validation/instance-checks.bc`

## lindeberg_clt

- **lean_status:** `cited` — Billingsley Thm 27.2; Durrett Thm 3.4.5
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## delta_method

- **lean_status:** `cited` — Durrett; van der Vaart Asymptotic Statistics Thm 3.1
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_expectation_elementary

- **well-definedness:** for each y with positive mass/density, x |-> p_{X|Y}(x|y) is a probability distribution, so its mean g(y) is a well-defined number when E|X| < inf; the exceptional y-set is P_Y-null.
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_expectation_abstract

- definition/axiom — see the type check
- **lean_status:** `cited` — Williams ch. 9; Durrett ch. 4
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_expectation_existence

- **lean_status:** `cited` — Williams Thm 9.2; Durrett Thm 4.1.1
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## tower_property

- **lean_status:** `core` — validation/proof-checks.lean -- linearity core; the tower is the defining-property chase
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## law_of_total_variance

- **lean_status:** `core` — validation/proof-checks.lean Prob.centid + Prob.expectation_linearity (GENUINE)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## conditional_expectation_l2_projection

- **lean_status:** `core` — validation/proof-checks.lean Prob.jensen_sq (the L^2 convexity core)
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## martingale

- **lean_status:** `cited` — Williams Probability with Martingales chs. 10-14; Durrett ch. 5
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## stochastic_process

- **lean_status:** `cited` — Billingsley SS36; Durrett ch. 6-8; Karatzas-Shreve ch. 1-2
- **bc:** (no numeric worksheet; the type check and specialization cases apply)

## kolmogorov_extension_theorem

- **lean_status:** `cited` — Billingsley Thm 36.1; Durrett Thm 6.1.1 (Kolmogorov); Tao
- **bc:** (no numeric worksheet; the type check and specialization cases apply)
