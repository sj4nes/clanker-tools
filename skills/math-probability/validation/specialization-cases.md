# Specialization & hypothesis-dropped counterexamples (generated from results/*.yaml)

For every node: at least one specialization / boundary case, and at least one
counterexample showing a named hypothesis cannot be dropped (or a note that
every hypothesis is essential / the statement is unconditional).


## set_algebra

- **spec:** two sets: A cup A^c = Omega, A cap A^c = empty
- **spec:** indexed: (bigcup_i A_i)^c = bigcap_i A_i^c (De Morgan, arbitrary)
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## preimage_algebra

- **spec:** f measurable iff f^{-1}(generating sets) are all measurable -- this is why the preimage algebra, not the image, drives measurability
- **spec:** image only satisfies f[A cap B] subset f[A] cap f[B], with equality iff f injective
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## countable_set

- **spec:** Q is countable; the algebraic numbers are countable
- **spec:** a sigma-algebra is closed under countable unions, so it is the natural domain for a countably additive measure
- **drop `countable_choice`:** without countable choice it is consistent that a countable union of countable sets of reals is uncountable (Feferman-Levy)

## real_field

- **spec:** [0,1] with its order is where every probability P(A) lives
- **spec:** the extended reals [0, inf] carry measure and integral values
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## sequence_limit

- **spec:** P(A_n) -> P(A) statements (continuity of probability) are sequence limits in [0,1]
- **spec:** convergence of a series is convergence of its partial-sum sequence
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## limsup_liminf

- **spec:** Borel-Cantelli lemmas are statements about P(limsup A_n)
- **spec:** a_n -> a iff limsup a_n = liminf a_n = a
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## series_convergence

- **spec:** countable additivity: P(bigcup A_n) = sum P(A_n) is a convergent series bounded by 1
- **spec:** sum P(A_n) < inf is the hypothesis of the first Borel-Cantelli lemma
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## convex_function

- **spec:** phi(x) = x^2, |x|, e^{tx} are convex on R -- the cases used for variance, Jensen, and the Chernoff/Hoeffding bounds
- **spec:** phi affine: Jensen holds with equality
- **drop `convexity`:** phi(x) = -x^2 (concave): Jensen reverses, phi(E[X]) >= E[phi(X)]

## abstract_integral

- **spec:** mu = P: integral X dP = E[X]
- **spec:** mu = counting measure on N: integral f dmu = sum_n f(n) -- series are integrals
- **spec:** f = 1_A: integral 1_A dmu = mu(A)
- **drop `measurability_of_f`:** a non-measurable f has no well-defined integral -- the defining sup is over an ill-specified family and Fubini/Tonelli fail

## monotone_convergence_theorem

- **spec:** mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma
- **drop `monotonicity_f_n_up`:** f_n = 1_{[n, n+1]} -> 0 pointwise but integral f_n = 1 not -> 0 (not monotone; DCT also fails, no dominating integrable g)

## dominated_convergence_theorem

- **spec:** mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma
- **drop `integrable_dominator_g`:** f_n = n 1_{(0, 1/n]} on ([0,1], lambda): f_n -> 0 a.e. but integral f_n = 1; no integrable g dominates (sup_n f_n is not integrable)

## fatou_lemma

- **spec:** mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma
- **drop `nonnegativity_f_n`:** f_n = -1_{[n,n+1]}: liminf f_n = 0 with integral 0, but liminf integral f_n = -1 -- the inequality direction needs f_n >= 0

## fubini_tonelli

- **spec:** mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma
- **drop `sigma_finiteness_or_integrability`:** f(x,y) = (x^2 - y^2)/(x^2 + y^2)^2 on (0,1)^2: the two iterated integrals are +pi/4 and -pi/4 -- f is not integrable, so Fubini does not apply

## radon_nikodym

- **spec:** mu = P: the probability form used for E[lim] = lim E, differentiating an MGF, and Scheffe's lemma
- **drop `absolute_continuity_nu_ll_mu`:** nu = delta_0, mu = Lebesgue on R: nu({0}) = 1 but mu({0}) = 0, so nu is NOT << mu and has no density; nu is purely singular

## sigma_algebra

- **spec:** Omega countable: F = 2^Omega is the usual choice
- **spec:** Omega = R: F = B(R), strictly smaller than 2^R (non-measurable sets exist under AC)
- **drop `countable_union_closure`:** the family of finite-or-cofinite subsets of N is closed under complement and FINITE unions but not countable ones -- it is an algebra, not a sigma-algebra

## generated_sigma_algebra

- **spec:** C = { (-inf, x] : x in Q }: sigma(C) = B(R)
- **spec:** C = a single set A: sigma(C) = { empty, A, A^c, Omega }
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## borel_sigma_algebra

- **spec:** singletons {x} = bigcap_n (x-1/n, x+1/n) are Borel, so every countable set is Borel and Borel-null under Lebesgue measure
- **spec:** B(R^d) = B(R) tensor ... tensor B(R), the product sigma-algebra
- **drop `generated_by_a_pi_system`:** if one generates from a collection that is not a pi-system, the pi-lambda uniqueness argument for measures fails

## measurable_space

- **spec:** (R, B(R)) is the canonical target for a real random variable
- **spec:** (Omega, {empty, Omega}) -- the trivial sigma-algebra: only constants are measurable
- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used in the proof; see the block above

## measure

- **spec:** mu(Omega) = 1: a probability measure (kolmogorov_axioms)
- **spec:** mu = counting measure on a countable Omega: mu(A) = |A|
- **spec:** mu = delta_x: mu(A) = 1 if x in A else 0
- **drop `countable_additivity`:** a merely finitely additive set function (e.g. a Banach limit / finitely additive extension of density on N) is not a measure and breaks continuity from below and Borel-Cantelli

## dynkin_pi_lambda

- **spec:** two probability measures equal on { (-inf, x] : x in R } are equal on B(R) -- this proves cdf_determines_law
- **spec:** independence checked on generating pi-systems extends to the generated sigma-algebras (independence_factorization)
- **drop `pi_system`:** measures can agree on a generating collection that is NOT a pi-system yet differ: on Omega={1,2,3,4}, uniform vs the measure (3/8,1/8,1/8,3/8) agree on {1,2} and {1,3} but not on {1} = {1,2} cap {1,3}

## lebesgue_measure_caratheodory

- **spec:** lambda restricted to [0,1] is the uniform probability measure -- the model probability space
- **spec:** lambda({x}) = 0, lambda(Q) = 0, lambda(Cantor set) = 0 -- uncountable null sets exist
- **drop `caratheodory_measurability`:** lambda* is only finitely subadditive-not-additive on all of 2^R; a Vitali set V has lambda*(V) > 0 but the translates of V partition [0,1] into countably many congruent pieces, so countable additivity would force a contradiction -- V is not measurable

## measure_monotonicity

- **spec:** mu = P: P(A) <= P(B) and P(A) in [0,1]; Boole's inequality is the probability form of subadditivity
- **spec:** equality in subadditivity iff the A_n are pairwise disjoint (mod null sets)
- **drop `nonnegativity_of_mu`:** for a signed measure monotonicity fails: a set of negative measure can contain one of positive measure

## measure_continuity

- **spec:** mu = P: continuity_of_probability, no finiteness caveat needed (P <= 1)
- **spec:** cdf right-continuity: F_X(x_n) -> F_X(x) for x_n decreasing to x, via { X <= x_n } down { X <= x }
- **drop `finite_measure_for_continuity_from_above`:** Lebesgue measure, A_n = [n, inf): A_n down empty but lambda(A_n) = inf for all n, so lambda(A_n) does not converge to lambda(empty) = 0

## null_set

- **spec:** mu = P: a P-null set is the complement of an almost-sure event; 'a.e.' becomes 'almost surely'
- **spec:** Lebesgue: Q is null, so 'x irrational' holds Lebesgue-a.e.
- **drop `countability_of_the_union`:** an UNCOUNTABLE union of null sets need not be null: R = bigcup_{x} {x}, each {x} Lebesgue-null, but lambda(R) = inf

## almost_sure

- **spec:** X_n -> X a.s. is the strongest of the four convergence modes
- **spec:** E[X | G] is defined only up to a.s. equality
- **drop `countable_intersection_only`:** an uncountable family of a.s. events can have intersection of probability 0: on [0,1] uniform, A_x = { omega != x } has P(A_x) = 1 but bigcap_x A_x = empty

## kolmogorov_axioms

- **spec:** Omega finite, F = 2^Omega: P determined by the pmf p(omega) >= 0 summing to 1; countable additivity is automatic (finite sums)
- **spec:** A single event A: P(A^c) = 1 - P(A) follows immediately
- **spec:** disjoint A,B: P(A cup B) = P(A) + P(B) -- finite additivity as the 2-set case
- **drop `countable_additivity`:** on Omega = N with F = 2^N, "P(A) = 0 if A finite, 1 if cofinite" is finitely additive and normalized but NOT countably additive (singletons have measure 0 but union to measure 1) -- and it is not sigma-additive-extendable, so it is not a probability measure. This is why the third axiom is countable, not finite.
- **drop `normalization`:** drop P(Omega)=1 and any measure qualifies; "probability" statements (expectations as weighted averages, Bayes) collapse.
- **drop `nonnegativity`:** signed measures are not probabilities; P(A) in [0,1] and monotonicity both fail.

## probability_measure

- **spec:** Omega finite: P given by a pmf on Omega
- **spec:** P = lambda restricted to [0,1]: the uniform model space
- **drop `normalization`:** drop P(Omega)=1 and expectations are no longer weighted averages; Bayes' normalizing constant is meaningless

## probability_space

- **spec:** ([0,1], B, lambda): supports a random variable of ANY law via the quantile transform (probability_integral_transform)
- **spec:** (Omega, {empty, Omega}, P): only P(empty)=0, P(Omega)=1 -- no non-trivial events
- **drop `F_a_sigma_algebra`:** if F is only an algebra, countable additivity has no content and the limit theorems (which are about countable families) cannot even be stated

## complement_rule

- **spec:** A = Omega: P(empty) = 0
- **spec:** A = B: P(B \ B) = 0
- **drop `P_a_probability_measure`:** for a general (unnormalized) measure there is no '1 -' form; only mu(B \ A) = mu(B) - mu(A) with mu(A) < inf survives

## finite_additivity

- **spec:** n = 2: P(A cup B) = P(A) + P(B) for disjoint A, B
- **spec:** partition of Omega: sum_i P(B_i) = 1
- **drop `disjointness`:** P(A cup B) = P(A) + P(B) - P(A cap B) in general; without disjointness the sum overcounts the overlap (inclusion_exclusion)

## inclusion_exclusion

- **spec:** n = 2: P(A cup B) = P(A) + P(B) - P(A cap B)
- **spec:** Bonferroni: truncating after k terms gives an upper bound (k odd) or lower bound (k even)
- **spec:** derangements: P(no fixed point of a uniform random permutation) -> 1/e
- **drop `none_all_terms_needed`:** dropping the higher-order terms gives only the Bonferroni one-sided bounds, not equality

## boole_inequality

- **spec:** finitely many A_n: the finite union bound
- **spec:** A_n with sum P(A_n) < 1: P(no A_n occurs) >= 1 - sum P(A_n) > 0 -- the probabilistic method's first-moment argument
- **spec:** if sum P(A_n) < inf then P(A_n i.o.) = 0 (borel_cantelli_first)
- **drop `none_unconditional`:** the bound holds for every countable family; it is tight iff the A_n are pairwise disjoint (mod null sets)

## continuity_of_probability

- **spec:** A_n = { X <= x + 1/n } down { X <= x }: gives right-continuity of the CDF
- **spec:** A_n = { |X_k - X| <= eps for all k <= n }: used to relate a.s. and in-probability convergence
- **spec:** P(bigcup_{n} A_n) = lim_N P(bigcup_{n<=N} A_n)
- **drop `monotonicity_of_A_n`:** for a non-monotone sequence only Fatou-type bounds hold: P(liminf A_n) <= liminf P(A_n) <= limsup P(A_n) <= P(limsup A_n)

## borel_cantelli_first

- **spec:** A_n = { |X_n - X| > eps }: sum P < inf gives X_n -> X a.s. -- the standard route from a rate to a.s. convergence
- **spec:** A_n = { X_n / n > 1 + eps } with sum P < inf: proves a.s. bounds like the SLLN's a.s. o(n) growth
- **drop `none_unconditional_direction`:** the converse needs independence (borel_cantelli_second); without it sum P(A_n) = inf gives no lower bound -- take A_n all equal to a fixed A with 0 < P(A) < 1: sum diverges but P(A i.o.) = P(A) < 1

## borel_cantelli_second

- **spec:** together with BC1: for INDEPENDENT events, P(A_n i.o.) is 0 or 1 according as sum P(A_n) converges or diverges -- a zero-one law
- **spec:** A_n = { X_n > c_n } for iid X_n: P(X_n > c_n i.o.) is 0 or 1 by whether sum P(X_1 > c_n) converges
- **drop `independence`:** A_n = A fixed with 0 < P(A) < 1: sum P(A_n) = inf but P(A i.o.) = P(A) != 1. Pairwise independence is not quite enough in general; mutual (or the Kochen-Stone refinement) is the clean hypothesis.

## conditional_probability

- **spec:** B = Omega: P(A | Omega) = P(A)
- **spec:** A subset B: P(A | B) = P(A)/P(B) >= P(A)
- **spec:** A, B disjoint: P(A | B) = 0
- **drop `positivity_of_P_B`:** P(B) = 0 makes the ratio 0/0 -- the Borel-Kolmogorov paradox shows the 'limit' answer depends on the approximating sequence of positive-probability events

## multiplication_rule

- **spec:** independent A, B: P(A cap B) = P(A) P(B)
- **spec:** drawing without replacement: P(both aces) = (4/52)(3/51) -- the chain rule computes sequential-sampling probabilities
- **spec:** P(A_1 cap ... cap A_n) for a Markov chain telescopes to P(A_1) prod P(A_{i+1} | A_i)
- **drop `positive_probability_of_the_conditioning_events`:** if some prefix intersection has probability 0, that conditional factor is undefined -- but then the whole intersection also has probability 0, so the identity is read as 0 = 0

## law_of_total_probability

- **spec:** two-part partition {B, B^c}: P(A) = P(A|B) P(B) + P(A|B^c) P(B^c)
- **spec:** the denominator of Bayes' theorem is exactly this expansion
- **spec:** first-step analysis: P(gambler ruin) = p P(ruin | up) + (1-p) P(ruin | down)
- **drop `the_B_i_partition_Omega`:** if the B_i do not cover Omega, sum_i P(A|B_i) P(B_i) = P(A cap bigcup B_i) < P(A) -- you undercount the part of A outside the B_i

## bayes_theorem

- **spec:** two hypotheses B, B^c: P(B|A) = P(A|B)P(B) / [P(A|B)P(B) + P(A|B^c)P(B^c)] -- the odds form: posterior odds = likelihood ratio x prior odds
- **spec:** uniform prior P(B_i) = 1/n: P(B_j|A) proportional to the likelihood P(A|B_j) alone
- **spec:** A independent of every B_i: P(B_j|A) = P(B_j) -- evidence moves nothing
- **drop `partition_of_Omega`:** if the B_i do not cover Omega, sum_i P(A|B_i)P(B_i) < P(A) and the formula gives a posterior that does not sum to 1 over j. (base-rate fallacy is the special case of ignoring P(B_j).)
- **drop `positive_prior_P_B_i`:** P(B_j) = 0 makes P(A|B_j) undefined; a hypothesis with prior 0 can never gain posterior mass -- "Cromwell's rule".
- **drop `positive_evidence_P_A`:** P(A) = 0 makes every P(B_j|A) undefined (0/0).

## measurable_function

- **spec:** f = 1_A: measurable iff A in F
- **spec:** f continuous: Borel measurable
- **spec:** f = sup_n f_n of measurable f_n: measurable
- **drop `generating_collection_check`:** checking f^{-1} of a non-generating family is not enough; and a pointwise limit of measurable functions is measurable but a limit of continuous functions need not be continuous

## random_variable

- **spec:** X = 1_A: a Bernoulli random variable
- **spec:** X constant = c: measurable w.r.t. any F; sigma(X) = { empty, Omega }
- **spec:** X = g(Y) for measurable g: sigma(X) subset sigma(Y) (Doob-Dynkin)
- **drop `measurability`:** an arbitrary function Omega -> R (e.g. the indicator of a non-measurable set) is not a random variable -- P(X in B) is undefined

## indicator_rv

- **spec:** A = Omega: 1_A = 1 constant
- **spec:** sum_i 1_{A_i} counts how many A_i occur; E of it is sum P(A_i) by linearity
- **drop `A_in_F`:** if A is not an event, 1_A is not a random variable and E[1_A] is undefined -- this is the only hypothesis

## distribution_pushforward

- **spec:** X discrete: P_X = sum_x p_X(x) delta_x
- **spec:** X absolutely continuous: P_X(B) = integral_B f_X dlambda
- **spec:** X = c constant: P_X = delta_c
- **drop `measurability_of_X`:** without it X^{-1}(B) need not be an event and P_X(B) is undefined

## cdf

- **spec:** X ~ Uniform(0,1): F_X(x) = x on [0,1]
- **spec:** X = c: F_X = step at c (0 below, 1 from c on)
- **spec:** F_X has an atom at x iff P(X = x) = F_X(x) - F_X(x^-) > 0
- **drop `none_defined_for_every_rv`:** F_X always exists; the content is in cdf_properties (which functions are CDFs) and cdf_determines_law

## cdf_properties

- **spec:** a pure-jump F (step function with jumps summing to 1): F_X of a discrete X
- **spec:** F absolutely continuous: F(x) = integral_{-inf}^x f, X has density f
- **spec:** the Cantor function: a continuous F with F' = 0 a.e. -- a singular continuous law, neither discrete nor absolutely continuous
- **drop `right_continuity`:** a function that is left-continuous with jumps is not a CDF in this convention -- it would be x |-> P(X < x)
- **drop `the_limit_conditions`:** F(x) = arctan(x)/pi + 1/2 works; F(x) = arctan(x) does not reach 1 (defective / sub-probability distribution -- mass escapes to +inf)

## cdf_determines_law

- **spec:** hence P(X in B) can always be computed from F_X (by pi-lambda / Caratheodory), even for complicated Borel B
- **spec:** the analogous statement in R^d: the joint CDF F(x_1,...,x_d) = P(X_1<=x_1, ..., X_d<=x_d) determines the joint law
- **drop `pi_system_generates_the_sigma_algebra`:** agreeing on a non-generating or non-pi-system family is not enough -- see the dynkin_pi_lambda counterexample

## discrete_rv

- **spec:** S finite: a simple random variable, a finite sum of indicators
- **spec:** S = N: e.g. Poisson, geometric
- **drop `countability_of_S`:** if the smallest such S is uncountable then no pmf exists -- e.g. any absolutely continuous X has P(X = x) = 0 for every x

## pmf

- **spec:** Bernoulli: p(1) = p, p(0) = 1 - p
- **spec:** Poisson: p(k) = e^{-lambda} lambda^k / k!
- **drop `discreteness`:** for an absolutely continuous X, p_X(x) = P(X = x) = 0 everywhere -- the object that works is the pdf

## absolutely_continuous_rv

- **spec:** Uniform, exponential, normal, gamma, beta: all absolutely continuous
- **spec:** P(X = x) = 0 for every x (no atoms) is necessary but NOT sufficient (singular continuous laws also have no atoms)
- **drop `absolute_continuity_vs_continuous_cdf`:** the Cantor distribution: F_X continuous and strictly increasing on the Cantor set, F_X' = 0 lambda-a.e., P_X concentrated on a lambda-null set -- continuous CDF, no density

## pdf

- **spec:** Uniform(a,b): f_X = 1/(b-a) on [a,b]
- **spec:** standard normal: f_X(x) = e^{-x^2/2}/sqrt(2 pi)
- **spec:** Exponential(lambda): f_X(x) = lambda e^{-lambda x} for x >= 0
- **drop `absolute_continuity`:** a discrete or singular X has no density; writing 'f_X' for them is a type error

## quantile_function

- **spec:** F_X continuous and strictly increasing: F_X^{-1} is the ordinary inverse
- **spec:** median = F_X^{-1}(1/2); quartiles at u = 1/4, 3/4
- **spec:** discrete X: F_X^{-1} is a step function taking values in the support
- **drop `u_in_open_interval`:** at u = 0 the inf is over all of R (gives -inf or the essential infimum); at u = 1 it may be +inf -- the transform is stated for u in (0,1)

## probability_integral_transform

- **spec:** F(x) = 1 - e^{-lambda x} (exponential): F^{-1}(u) = -ln(1-u)/lambda -- inversion sampling for the exponential
- **spec:** F discrete: F^{-1}(U) picks value x_k when U falls in (F(x_{k-1}), F(x_k)] -- the alias/CDF method
- **spec:** goodness-of-fit: if the model F is right, the transformed data F(x_i) should look Uniform(0,1) (the basis of PP-plots and the Kolmogorov-Smirnov test)
- **drop `continuity_of_F_X_for_the_forward_direction`:** X ~ Bernoulli(1/2): F_X(X) takes only the values 1/2 and 1, not Uniform(0,1) -- atoms in F_X break the forward transform (the inverse direction still works)

## transformation_univariate

- **spec:** g(x) = a x + b, a != 0: f_Y(y) = f_X((y-b)/a) / |a| -- affine rescaling
- **spec:** g(x) = e^x on a normal X: Y is lognormal
- **spec:** g(x) = x^2 (NOT monotone on R): split into x > 0 and x < 0 and add the two branches -- f_Y(y) = [f_X(sqrt y) + f_X(-sqrt y)] / (2 sqrt y)
- **drop `monotonicity_of_g`:** g(x) = x^2 with X ~ N(0,1): the naive one-branch formula gives half the correct density; Y ~ chi-squared_1 requires summing both preimages
- **drop `g_is_C1_with_nonzero_derivative`:** if g'(x_0) = 0 the change of variables blows up; the density of Y develops a singularity there

## jacobian_transformation

- **spec:** polar coordinates on (X_1, X_2) ~ iid N(0,1): shows R^2 ~ Exponential and Theta ~ Uniform -- the Box-Muller method
- **spec:** linear map Y = A X, A invertible: f_Y(y) = f_X(A^{-1} y) / |det A|
- **spec:** sum-and-difference: (X+Y, X-Y) to get the distribution of a sum from a joint density
- **drop `g_a_diffeomorphism`:** if g is not injective (e.g. (x_1,x_2) -> (x_1^2, x_2)) the preimage has multiple sheets and their Jacobian contributions must be summed
- **drop `det_J_nonzero`:** at a critical point det J_{g^{-1}} = inf and the transformed density is singular

## joint_distribution

- **spec:** independent components: P_X = P_{X_1} tensor ... tensor P_{X_n}, joint density factorizes
- **spec:** X_2 = X_1: the joint law is concentrated on the diagonal { x_1 = x_2 }, a lambda_2-null set (no joint density)
- **drop `none_the_marginals_do_not_determine_it`:** (X,Y) and (X, X) can have the same marginals (both standard normal) but wildly different joint laws -- Cov 0 vs Cov 1

## marginal_distribution

- **spec:** joint uniform on the unit disk: each marginal has a semicircular density, not uniform
- **spec:** bivariate normal: marginals are normal (but normal marginals do not imply joint normal)
- **drop `none_well_defined_always`:** the marginal always exists; the caution is that MANY joints share it

## conditional_distribution

- **spec:** independence: f_{Y|X}(y|x) = f_Y(y), no dependence on x
- **spec:** bivariate normal: Y | X = x is normal with mean mu_Y + rho (sigma_Y/sigma_X)(x - mu_X) -- the linear regression line
- **spec:** (X,Y) uniform on the triangle 0 < y < x < 1: Y | X = x is Uniform(0, x)
- **drop `positive_marginal_density`:** where f_X(x) = 0 the ratio is 0/0 -- conditioning on a value X never takes is undefined
- **drop `existence_of_a_joint_density`:** for singular joints (e.g. Y = X^2) there is no f_{X,Y}; conditioning requires the abstract construction (Borel-Kolmogorov paradox: the answer depends on how the conditioning event is approached)

## independence_events

- **spec:** two events: independence is the single equation P(A cap B) = P(A) P(B)
- **spec:** A with P(A) in {0, 1}: A is independent of every event
- **spec:** pairwise independence: only the |S| = 2 equations -- strictly weaker (pairwise_not_mutual)
- **drop `all_subsets_not_just_pairs`:** pairwise_not_mutual: X, Y iid fair bits, Z = X XOR Y -- each pair independent, but P(X=Y=Z=0) = 1/4 != 1/8
- **drop `the_empty_and_singleton_S_are_trivial`:** the content is in |S| >= 2

## independence_sigma_algebras

- **spec:** G_i = sigma(X_i): recovers independence_random_variables
- **spec:** G = { empty, Omega }: independent of every sigma-algebra
- **spec:** the tail sigma-algebra of an independent sequence is independent of every finite prefix -- Kolmogorov's zero-one law
- **drop `factorization_on_a_pi_system_that_generates`:** checking factorization on a generating family that is not intersection-closed does not extend (dynkin_pi_lambda counterexample)

## independence_random_variables

- **spec:** densities factorize: f_{X_1,...,X_n}(x) = prod_i f_{X_i}(x_i) (independence_factorization)
- **spec:** g_1(X_1), ..., g_n(X_n) are independent for any measurable g_i
- **spec:** iid = independent + identically distributed
- **drop `all_n_together_not_just_pairs`:** three variables can be pairwise independent but not mutually independent -- e.g. X_1, X_2 iid uniform on {-1,1}, X_3 = X_1 X_2
- **drop `the_joint_law_not_just_marginals`:** same marginals, different dependence: (X, X) vs (X, -X) vs (X, Y independent)

## independence_factorization

- **spec:** a joint density that is a product g(x) h(y) (even unnormalized) => X, Y independent with marginals proportional to g, h -- the 'factorization criterion'
- **spec:** checking independence: it is enough that the SUPPORT is a product AND the density factors on it
- **drop `factorization_over_the_full_support`:** f_{X,Y}(x,y) = 2 on the triangle 0 < x < y < 1: the density is 'constant' but the support is not a rectangle, so X, Y are NOT independent (Y | X = x is Uniform(x, 1))

## pairwise_not_mutual

- **spec:** the |S| = 2 factorization equations all hold; the |S| = 3 equation P(X=Y=Z=1) = P(X=1)P(Y=1)P(Z=1) fails
- **spec:** consequence: E[XYZ] = E[1] = 1 != 0 = E[X]E[Y]E[Z], so 'expectation factors' can fail even when it holds for every pair
- **drop `this_IS_the_counterexample`:** it shows the |S| >= 3 conditions in independence_events are not redundant

## iid

- **spec:** repeated independent trials of one experiment (coin, die, measurement with iid noise)
- **spec:** the empirical distribution of an iid sample converges to P_{X_1} (Glivenko-Cantelli)
- **spec:** a random sample in statistics IS an iid sequence (design permitting)
- **drop `identically_distributed`:** independent but not identical: the Lindeberg CLT (lindeberg_clt) is what replaces 'identical' for a non-degenerate limit
- **drop `independence`:** identically distributed but dependent (e.g. a stationary time series): the LLN can still hold (ergodic theorem) but the CLT rate and variance change (long-range dependence)

## convolution_formula

- **spec:** Exponential(lambda) * Exponential(lambda) = Gamma(2, 1/lambda) -- sum of two iid exponentials
- **spec:** N(0, s_1^2) * N(0, s_2^2) = N(0, s_1^2 + s_2^2)
- **spec:** Poisson(a) * Poisson(b) = Poisson(a + b) (discrete convolution of the pmfs)
- **drop `independence`:** for dependent X, Y the density of X + Y involves the joint density and is not a convolution -- e.g. Y = -X gives X + Y = 0, a point mass
- **drop `existence_of_densities`:** if X is discrete and Y continuous, X + Y has a density (a mixture of shifted f_Y), but the pure convolution-of-densities formula does not apply directly

## expectation

- **spec:** X = 1_A: E[X] = P(A)
- **spec:** X discrete: E[X] = sum_x x p_X(x)
- **spec:** X with density: E[X] = integral x f_X(x) dx
- **spec:** X = c: E[X] = c
- **drop `integrability_E_abs_X_finite`:** X ~ Cauchy: E[|X|] = (2/pi) integral_0^inf x/(1+x^2) dx = inf, so E[X] does not exist -- neither the LLN nor the CLT apply

## lotus

- **spec:** g(x) = x: E[X] from the law directly
- **spec:** g(x) = x^k: the k-th moment
- **spec:** g(x) = e^{tx}: the MGF
- **spec:** g(x) = 1_B(x): E[1_B(X)] = P(X in B)
- **drop `integrability_of_g_X`:** g(x) = x on a Cauchy X: E[g(X)] = integral x/(pi(1+x^2)) dx does not converge absolutely -- LOTUS gives no finite value

## expectation_linearity

- **spec:** X_i = 1_{A_i} indicators: E[sum 1_{A_i}] = sum P(A_i) -- the mean of a count, e.g. the number of fixed points of a random permutation is 1 regardless of n
- **spec:** binomial X = sum of n iid Bernoulli(p): E[X] = np immediately, with no combinatorial sum
- **spec:** a = 1, b = -1: E[X - Y] = E[X] - E[Y]
- **drop `X_integrable`:** X ~ Cauchy, Y = -X: X + Y = 0 has E = 0, but E[X] and E[Y] do not exist, so E[X] + E[Y] is undefined -- linearity needs both pieces integrable. (X + Y integrable is NOT enough.)

## expectation_monotonicity

- **spec:** X = 1_A <= 1_B = Y when A subset B: recovers P(A) <= P(B)
- **spec:** E[X] = 0 with X >= 0 a.s.: X = 0 a.s. -- the 'no negative mass' rigidity used in L^p norms
- **drop `a_s_inequality`:** X <= Y on a null set only is not enough to compare -- but changing X, Y on a null set changes neither expectation, so 'a.s.' is exactly the right hypothesis
- **drop `existence_of_both_expectations`:** if E[Y] = +inf and E[X] = -inf the inequality is vacuous/ill-posed

## markov_inequality

- **spec:** X = |Y - E[Y]|^2, a = k^2: gives Chebyshev's inequality
- **spec:** X = e^{tY} (t > 0), a = e^{ts}: gives the Chernoff bound after optimising over t
- **spec:** X an indicator 1_A, a = 1: P(A) <= E[1_A] = P(A), an equality -- the bound is tight
- **drop `X_nonnegative_a_s`:** X = -1 constant, a = 1: P(X >= 1) = 0 but also E[X]/a = -1 < 0; more sharply X taking values +-M with mean 0 has P(X >= a) = 1/2 while E[X]/a = 0. The one-sided nonnegativity is essential.
- **drop `a_positive`:** a <= 0 makes E[X]/a <= 0 (or undefined), while P(X >= a) can be 1.

## jensen_inequality

- **spec:** phi(x) = x^2: E[X]^2 <= E[X^2], i.e. Var(X) >= 0
- **spec:** phi(x) = |x|: |E[X]| <= E[|X|]
- **spec:** phi(x) = e^x: e^{E[X]} <= E[e^X] (used in the Chernoff/entropy bounds)
- **spec:** phi(x) = -log x on X > 0: log E[X] >= E[log X] (AM-GM in expectation form)
- **drop `convexity_of_phi`:** phi concave (e.g. sqrt, log): the inequality REVERSES, phi(E[X]) >= E[phi(X)] -- applying Jensen the wrong way is the single most common error
- **drop `integrability`:** phi(x) = x^2 on a Cauchy X: E[phi(X)] = inf, the inequality is vacuous

## variance

- **spec:** X = 1_A: Var = P(A)(1 - P(A)), maximized at P(A) = 1/2
- **spec:** X = c constant: Var = 0
- **spec:** X ~ N(mu, sigma^2): Var = sigma^2 (the parameter)
- **drop `finite_second_moment`:** X ~ t-distribution with 2 degrees of freedom, or Cauchy: E[X^2] = inf, Var undefined -- the CLT fails, the sample variance does not stabilize

## variance_computational

- **spec:** X ~ Bernoulli(p): E[X^2] = p, so Var = p - p^2 = p(1-p)
- **spec:** X ~ Poisson(lambda): E[X^2] = lambda^2 + lambda, Var = lambda
- **spec:** the sample analogue: (1/n) sum x_i^2 - xbar^2 -- but this is biased; divide by n-1 for the unbiased estimator
- **drop `finite_second_moment`:** if E[X^2] = inf both sides are +inf (or ill-posed); the identity is only useful when Var is finite

## variance_affine

- **spec:** standardization: Z = (X - mu)/sigma has Var(Z) = 1
- **spec:** a = -1: Var(-X) = Var(X)
- **drop `none_holds_whenever_Var_X_is_finite`:** unconditional given a finite second moment

## chebyshev_inequality

- **spec:** k = c * sd(X): P(|X - E[X]| >= c sd) <= 1/c^2 -- the "how many standard deviations" form
- **spec:** X = sample mean of n iid variables, Var = sigma^2/n: P(|mean - mu| >= eps) <= sigma^2/(n eps^2) -> 0, i.e. the WLLN
- **spec:** two-point symmetric law at +-k with the stated variance: equality -- Chebyshev is tight
- **drop `finite_variance`:** X ~ Cauchy (cauchy_no_mean): Var and E both fail to exist; the tail P(|X| >= k) ~ 2/(pi k) decays like 1/k, not 1/k^2, and no variance bound applies.
- **drop `k_positive`:** k <= 0: the right side is infinite or undefined and the statement is vacuous or meaningless.

## covariance

- **spec:** Y = X: Cov(X, X) = Var(X)
- **spec:** Y = aX + b: Cov(X, Y) = a Var(X)
- **spec:** X, Y independent: Cov = 0 (independence_expectation)
- **drop `finite_second_moments`:** if E[X^2] or E[Y^2] is infinite, E[XY] may not exist and Cov is undefined

## covariance_bilinear

- **spec:** Cov(sum a_i X_i, sum b_j Y_j) = sum_{i,j} a_i b_j Cov(X_i, Y_j) -- the general bilinear expansion behind variance_of_sum
- **spec:** Cov(X, c) = 0 for constant c
- **drop `none_holds_on_all_of_L2`:** bilinearity is unconditional on L^2(P); it is the inner-product structure (X, Y) |-> Cov(X, Y) on the quotient by constants

## cauchy_schwarz_expectation

- **spec:** Y = 1: (E[X])^2 <= E[X^2], i.e. Var(X) >= 0
- **spec:** centered X, Y: (Cov(X,Y))^2 <= Var(X) Var(Y), hence |rho| <= 1 (correlation)
- **spec:** Y = X^{p-1} style: a route to Holder / the moment ladder
- **drop `finite_second_moments`:** X ~ Cauchy, Y = 1: E[X^2] = inf and E[XY] = E[X] does not exist -- the inequality is between undefined quantities
- **drop `equality_needs_linear_dependence`:** if X, Y are not proportional a.s. the inequality is strict

## correlation

- **spec:** Y = aX + b, a > 0: rho = 1; a < 0: rho = -1
- **spec:** X, Y independent: rho = 0
- **spec:** bivariate normal: rho is the single parameter governing dependence -- and here rho = 0 DOES imply independence
- **drop `positive_finite_variances`:** a constant Y has sd(Y) = 0 -- rho is 0/0, undefined
- **drop `linearity_of_the_relationship`:** Y = X^2 with X ~ Uniform(-1,1): perfect functional dependence but rho = 0 -- correlation only sees LINEAR association

## variance_of_sum

- **spec:** pairwise uncorrelated (in particular independent) X_i: Var(sum) = sum Var(X_i) -- 'variances add'
- **spec:** iid X_i: Var(sum) = n Var(X_1), so Var(sample mean) = Var(X_1)/n -- the 1/n that drives the LLN and the sqrt(n) in the CLT
- **spec:** X_i = X for all i: Var(nX) = n^2 Var(X) -- maximal positive correlation
- **drop `uncorrelatedness_for_the_clean_form`:** X_1 ~ N(0,1), X_2 = -X_1: Var(X_1 + X_2) = Var(0) = 0, not Var(X_1) + Var(X_2) = 2 -- the -2 Cov term matters

## independence_expectation

- **spec:** more generally E[g(X) h(Y)] = E[g(X)] E[h(Y)] for measurable g, h with the products integrable
- **spec:** Var(X + Y) = Var(X) + Var(Y) for independent X, Y
- **spec:** the MGF and CF of a sum of independents factor (mgf_sum_independent)
- **drop `independence_not_merely_uncorrelated`:** X ~ Uniform(-1,1), Y = X^2: E[XY] = E[X^3] = 0 = E[X] E[Y], so uncorrelated, but X, Y are strongly dependent -- the converse is FALSE (uncorrelated_not_independent)
- **drop `integrability`:** independent Cauchy X, Y: E[XY] does not exist even though E[X], E[Y] individually fail too

## uncorrelated_not_independent

- **spec:** general principle: for any symmetric X with finite third moment, X and |X| (or X^2) are uncorrelated but dependent
- **spec:** the one place the converse DOES hold: (X, Y) jointly Gaussian => uncorrelated implies independent
- **drop `this_IS_the_counterexample`:** it shows independence_expectation is a one-way implication

## moment

- **spec:** k = 1: the mean; k = 2 central: the variance
- **spec:** symmetric law: all odd central moments are 0
- **spec:** normal: mu_{2k} = sigma^{2k} (2k-1)!! -- so kurtosis 0 (the baseline for 'excess')
- **drop `finite_k_th_absolute_moment`:** Student's t with nu degrees of freedom has E[|X|^k] = inf for k >= nu -- moments beyond a point simply do not exist for heavy-tailed laws

## lp_space

- **spec:** p = 1: integrable variables, E[X] defined
- **spec:** p = 2: finite variance, the Hilbert space where E[X|G] is a projection
- **spec:** p = inf: ||X||_inf = ess sup |X|, the a.s.-bounded variables
- **drop `probability_space_for_nesting`:** on (R, lambda), 1/x is in L^2(1, inf) but not L^1(1, inf) -- the nesting L^p subset L^q (p > q) needs a FINITE measure

## moment_ladder

- **spec:** p = 2, q = 1: E[|X|] <= sqrt(E[X^2]) -- finite variance implies finite mean, so Var and E both exist together
- **spec:** the sequence ||X||_q is nondecreasing in q, converging to ||X||_inf
- **drop `finite_total_measure`:** on an infinite measure space the inclusion reverses partially and can fail entirely -- the ladder is a probability-space phenomenon (P(Omega) = 1 is the hidden hypothesis)

## holder_inequality

- **spec:** p = q = 2: Cauchy-Schwarz, (E|XY|)^2 <= E[X^2] E[Y^2]
- **spec:** p = 1, q = inf: E[|XY|] <= E[|X|] ess-sup|Y|
- **spec:** Y = 1: E[|X|] <= ||X||_p (part of the moment ladder)
- **spec:** generalized (three factors): E[|XYZ|] <= ||X||_r ||Y||_s ||Z||_t with 1/r + 1/s + 1/t = 1
- **drop `conjugacy_1_over_p_plus_1_over_q_eq_1`:** with 1/p + 1/q < 1 the inequality is false in general (dimensional analysis / scaling X -> cX breaks it)
- **drop `X_in_Lp_and_Y_in_Lq`:** if X not in L^p the right side is infinite -- the bound holds but says nothing

## mgf

- **spec:** X ~ N(mu, sigma^2): M_X(t) = exp(mu t + sigma^2 t^2 / 2), finite for all t
- **spec:** X ~ Exponential(lambda): M_X(t) = lambda/(lambda - t) for t < lambda only
- **spec:** X ~ Poisson(lambda): M_X(t) = exp(lambda(e^t - 1))
- **drop `finiteness_near_0`:** X ~ Cauchy or lognormal: M_X(t) = inf for every t != 0, so the MGF carries no information -- use the characteristic function instead

## mgf_moments

- **spec:** N(0,1): M(t) = e^{t^2/2}, M''(0) = 1 = E[Z^2], M^{(4)}(0) = 3 = E[Z^4]
- **spec:** Exponential(1): M(t) = 1/(1-t), M^{(k)}(0) = k! = E[X^k]
- **drop `finiteness_of_M_X_near_0`:** if M_X is finite only at 0, none of this holds -- a distribution can have all moments finite yet no MGF? no: all-moments-finite does not give an MGF (lognormal: every moment finite, MGF infinite, and the moment sequence does NOT determine the law)

## mgf_uniqueness

- **spec:** sum of independent Poissons: M = product of exp(lambda_i(e^t - 1)) = exp((sum lambda_i)(e^t - 1)) => Poisson(sum lambda_i)
- **spec:** sum of independent N(mu_i, sigma_i^2): M = exp(sum mu_i t + (sum sigma_i^2) t^2 / 2) => N(sum mu_i, sum sigma_i^2)
- **drop `finiteness_on_an_interval`:** agreement of M_X and M_Y only AT t = 0 (both equal 1) says nothing; and two different laws can share every moment (lognormal and a discrete perturbation) -- but then neither has an MGF finite near 0

## characteristic_function

- **spec:** N(0,1): phi(t) = e^{-t^2/2}
- **spec:** Cauchy: phi(t) = e^{-|t|} (exists! even though no moments do)
- **spec:** X = c: phi(t) = e^{itc}
- **spec:** Bernoulli(p): phi(t) = 1 - p + p e^{it}
- **drop `none_always_defined`:** the CF is the tool precisely because it needs no hypothesis -- every law has one

## cf_properties

- **spec:** phi real-valued <=> P_X symmetric about 0
- **spec:** phi integrable => P_X has a bounded continuous density f(x) = (1/2 pi) integral e^{-itx} phi(t) dt
- **spec:** affine: standardizing X to (X - mu)/sigma multiplies the CF argument by sigma and adds a phase
- **drop `moment_for_smoothness`:** Cauchy: phi(t) = e^{-|t|} is NOT differentiable at 0 -- consistent with E|X| = inf
- **drop `continuity_points_for_inversion`:** the inversion formula recovers P_X((a,b]) only at continuity points a, b of F_X

## mgf_sum_independent

- **spec:** sum of n iid: M_{S_n} = M_X^n, phi_{S_n} = phi_X^n -- the engine of the CLT proof
- **spec:** N(mu_1, s_1^2) + N(mu_2, s_2^2) independent = N(mu_1 + mu_2, s_1^2 + s_2^2), by exp adding in the exponent
- **spec:** Poisson(lambda) + Poisson(mu) independent = Poisson(lambda + mu)
- **drop `independence`:** X + X = 2X: phi_{2X}(t) = phi_X(2t) != phi_X(t)^2 in general -- the product rule is exactly the independence assumption
- **drop `finiteness_for_the_MGF_version`:** the CF version is unconditional; the MGF version needs both MGFs finite at t

## chernoff_bound

- **spec:** X ~ N(0, sigma^2): optimizing gives P(X >= a) <= e^{-a^2 / (2 sigma^2)} -- the Gaussian tail
- **spec:** X = sum of n iid: M_X(t) = M_{X_1}(t)^n, so the bound is exponentially small in n -- the large-deviations rate function I(a) = sup_t (ta - log M_{X_1}(t))
- **spec:** X ~ Poisson(lambda), a = lambda(1 + delta): the multiplicative Chernoff bound e^{-lambda delta^2/(2+delta)}
- **drop `existence_of_the_MGF_for_some_t_gt_0`:** heavy-tailed X (Cauchy, power law): M_X(t) = inf for all t > 0, the bound is vacuous -- only polynomial (Markov/Chebyshev/moment) bounds apply

## hoeffding_lemma

- **spec:** X ~ Uniform{-c, c} (or any symmetric law on [-c, c]): recovers the sub-Gaussian bound e^{c^2 t^2 / 2}
- **spec:** the (b - a)^2 / 8 constant is sharp for the two-point law at a, b with mean 0
- **drop `boundedness`:** an unbounded centered X (e.g. centered exponential) is not sub-Gaussian -- its MGF grows faster than any e^{ct^2}, only e^{c|t|} for small t (sub-exponential); Hoeffding's inequality is replaced by Bernstein's
- **drop `E_X_eq_0`:** without centering, M_X(t) has an extra e^{t E[X]} factor -- the lemma is stated for the centered variable

## hoeffding_inequality

- **spec:** X_i in [0, 1], sample mean Xbar: P(Xbar - E[Xbar] >= eps) <= e^{-2 n eps^2} -- the workhorse bound for empirical means, bandit algorithms, and PAC learning
- **spec:** n coin flips: P(#heads - n/2 >= s) <= e^{-2 s^2 / n}
- **spec:** gives the sample size n >= (1/(2 eps^2)) log(2/delta) for an eps-accurate mean with confidence 1 - delta
- **drop `boundedness_of_each_X_i`:** one unbounded X_i (even with tiny variance) breaks the sub-Gaussian MGF bound -- use Bernstein's inequality (needs a variance bound + a one-sided bound) instead
- **drop `independence`:** for dependent X_i the MGF does not factor; McDiarmid's / Azuma's inequality handles bounded-difference dependence

## bernoulli_distribution

- **spec:** p = 1/2: the fair coin, maximum variance 1/4
- **spec:** p in {0,1}: degenerate (constant), variance 0
- **spec:** sum of n iid Bernoulli(p) = Binomial(n, p)
- **drop `p_in_0_1`:** p outside [0,1] is not a probability

## binomial_distribution

- **spec:** n = 1: Bernoulli(p)
- **spec:** p = 1/2: symmetric about n/2
- **spec:** n large, p small, np = lambda: approx Poisson(lambda) (poisson_limit_theorem)
- **spec:** n large, p fixed: (X - np)/sqrt(np(1-p)) approx N(0,1) (de Moivre-Laplace, a case of the CLT)
- **drop `independence_of_trials`:** correlated trials (e.g. sampling without replacement) give the hypergeometric distribution, with the SAME mean np but SMALLER variance (finite-population correction)
- **drop `identical_p`:** varying p_i per trial gives the Poisson-binomial distribution; mean sum p_i, variance sum p_i(1-p_i)

## geometric_distribution

- **spec:** p = 1: X = 1 a.s.
- **spec:** P(X > k) = (1-p)^k -- a clean survival function
- **spec:** min of independent geometrics with rates p_i is geometric with rate 1 - prod(1 - p_i)
- **drop `memorylessness_pins_it_down`:** any non-geometric law on {1,2,...} fails P(X > m+k | X > m) = P(X > k) for some m, k
- **drop `p_gt_0`:** p = 0 gives no success ever -- X = inf, not a proper random variable

## poisson_distribution

- **spec:** number of decay events per second; typos per page; arrivals in a fixed interval of a Poisson process
- **spec:** lambda large: Poisson(lambda) approx N(lambda, lambda) (a CLT via the sum-of-Poissons representation)
- **spec:** the index of dispersion Var/mean = 1 -- overdispersed count data (Var > mean) needs negative binomial instead
- **drop `lambda_gt_0`:** lambda = 0 degenerates to X = 0 a.s.
- **drop `equal_mean_and_variance`:** real count data with Var > mean (contagion, heterogeneity) is NOT Poisson -- fitting Poisson underestimates the variance and overstates significance

## poisson_limit_theorem

- **spec:** n = 1000 trials of probability 1/1000: number of successes approx Poisson(1) -- the bc worksheet shows the pmf at k = 3 converging
- **spec:** raisins per cookie, mutations per genome, connection requests per millisecond
- **drop `n_p_n_converges_to_a_finite_positive_limit`:** if n p_n -> inf the correct limit is Gaussian (CLT); if n p_n -> 0 the count is 0 a.s. in the limit
- **drop `p_n_to_0`:** with p fixed (not -> 0), Binomial(n, p) has mean np -> inf and is approximately Gaussian, not Poisson

## continuous_uniform_distribution

- **spec:** Uniform(0,1): the RNG primitive; E = 1/2, Var = 1/12
- **spec:** -log(U) ~ Exponential(1); U^{1/n} ~ Beta(n, 1); (U_1, ..., U_n) order statistics ~ Beta
- **spec:** sum of 12 iid Uniform(0,1) minus 6 is approximately N(0,1) (a crude Gaussian generator)
- **drop `bounded_support`:** there is no uniform distribution on R or on (0, inf) -- 'improper uniform' priors are not probability measures (they still yield proper posteriors sometimes)

## exponential_distribution

- **spec:** lambda = 1: standard exponential; -log(U) for U ~ Uniform(0,1)
- **spec:** min of independent Exponentials(lambda_i) ~ Exponential(sum lambda_i) -- competing risks
- **spec:** sum of k iid Exponential(lambda) ~ Gamma(k, 1/lambda)
- **drop `memorylessness`:** the Weibull, gamma (shape != 1), and lognormal are NOT memoryless -- using an exponential for aging components (increasing hazard) underestimates late failures
- **drop `constant_hazard_rate`:** f_X(x)/P(X > x) = lambda is constant; real lifetimes usually have a bathtub or increasing hazard

## memorylessness

- **spec:** the residual lifetime of an exponential component is exactly a fresh exponential -- no 'aging'
- **spec:** a geometric number of coin flips: given the first m were failures, the additional flips to a success is again Geometric(p)
- **drop `the_characterization_is_exact`:** gamma with shape 2: P(X > s + t | X > s) DECREASES in s -- it 'remembers' (positive aging). Weibull with shape > 1 likewise. Pareto: negative aging.

## gamma_distribution

- **spec:** k = 1: Exponential(1/theta)
- **spec:** Gamma(k, 2) with 2k = nu integer: chi-squared with nu degrees of freedom
- **spec:** conjugate prior for the rate of a Poisson / the precision of a normal
- **spec:** k -> inf: (X - k theta)/sqrt(k theta^2) -> N(0,1)
- **drop `common_scale_for_the_sum_rule`:** Gamma(k_1, theta_1) + Gamma(k_2, theta_2) with theta_1 != theta_2 is NOT gamma -- the sum rule needs a shared scale
- **drop `shape_and_scale_vs_shape_and_rate`:** software differs; mixing them scales the mean by theta^2

## beta_distribution

- **spec:** a = b = 1: Uniform(0,1)
- **spec:** a = b: symmetric about 1/2; a = b large: concentrated near 1/2 (approx normal)
- **spec:** a, b < 1: U-shaped, mass near 0 and 1
- **spec:** the k-th order statistic of n iid Uniform(0,1) is Beta(k, n - k + 1)
- **spec:** if Y_1 ~ Gamma(a, 1), Y_2 ~ Gamma(b, 1) independent, then Y_1/(Y_1 + Y_2) ~ Beta(a, b)
- **drop `support_is_the_unit_interval`:** for a proportion that can be exactly 0 or 1, a zero-or-one-inflated beta is needed; plain beta puts zero mass on the endpoints

## normal_distribution

- **spec:** mu = 0, sigma = 1: standard normal Z; X = mu + sigma Z
- **spec:** sum of independent normals is normal (variances add); the sample mean of iid normals is exactly normal
- **spec:** 68-95-99.7 within 1-2-3 sigma; tail P(Z > z) approx phi(z)/z
- **drop `light_tails`:** financial returns, network delays, and many natural quantities have heavier-than-Gaussian tails -- assuming normality drastically underestimates extreme-event probabilities (a 5-sigma event is ~1 in 3.5 million under normality, far more common in reality)
- **drop `the_CLT_does_not_make_everything_normal`:** the CLT needs iid-ish summands with finite variance; a single dominant term, heavy tails, or strong dependence breaks it

## standard_normal

- **spec:** Phi(0) = 1/2; Phi(1) approx 0.8413; Phi(1.96) approx 0.975 (the 95% two-sided quantile)
- **spec:** Z^2 ~ chi-squared_1; Z_1/Z_2 ~ Cauchy for independent Z_i; sum of k iid Z_i^2 ~ chi-squared_k
- **spec:** Mills ratio: P(Z > z)/phi(z) -> 1/z as z -> inf
- **drop `none_it_is_a_fixed_law`:** the standard normal is a single distribution; the caution is downstream (assuming data is standard normal after a bad standardization)

## normal_affine_closure

- **spec:** standardization Z = (X - mu)/sigma ~ N(0,1) is the a = 1/sigma, b = -mu/sigma case
- **spec:** sample mean of n iid N(mu, sigma^2) is exactly N(mu, sigma^2/n) -- the CLT holds with no error for normal data
- **spec:** any linear combination sum a_i X_i of jointly normal X_i is normal -- the definition of a Gaussian vector
- **drop `independence_for_the_sum`:** X ~ N(0,1), Y = -X ~ N(0,1): X + Y = 0, a point mass, NOT N(0, 2) -- the sum rule needs independence (or joint normality with the right covariance)
- **drop `joint_normality_for_linear_combos`:** X ~ N(0,1) and Y = X if |X| < 1 else -X: each is N(0,1) but X + Y is not normal -- marginal normality is not joint normality

## cauchy_no_mean

- **spec:** ratio Z_1/Z_2 of independent standard normals is standard Cauchy
- **spec:** the sample mean stays Cauchy(0,1) (phi_{Xbar}(t) = phi_X(t/n)^n = e^{-|t|}) -- averaging does not help
- **spec:** the sample MEDIAN of n iid Cauchy DOES concentrate (median is well-defined) and is asymptotically normal
- **drop `this_IS_the_counterexample`:** it shows the finite-mean hypothesis of the WLLN/SLLN and the finite-variance hypothesis of the CLT are not removable

## convergence_almost_sure

- **spec:** the SLLN delivers this mode: sample mean -> E[X_1] a.s.
- **spec:** a.s. convergence is preserved by continuous functions (continuous_mapping_theorem) and is equivalent to P(sup_{m >= n} |X_m - X| > eps) -> 0 for all eps
- **drop `common_probability_space`:** a.s. convergence is meaningless for X_n and X defined on different spaces -- only the WEAKER convergence in distribution makes sense then

## convergence_in_probability

- **spec:** the WLLN delivers this mode: sample mean -> E[X_1] in probability
- **spec:** X_n -> X in probability iff every subsequence has a further subsequence converging a.s. -- the 'subsequence principle'
- **spec:** X_n -> c (a constant) in probability <=> X_n -> c in distribution
- **drop `eps_quantifier`:** P(|X_n - X| > eps) -> 0 for ONE eps is not enough; it must hold for every eps > 0

## convergence_in_lp

- **spec:** L^2 convergence of the sample mean under finite variance (a one-line Chebyshev bound), giving the L^2 WLLN
- **spec:** in a Hilbert space (L^2) it is convergence in norm; Cauchy sequences converge (Riesz-Fischer)
- **drop `uniform_integrability_for_the_converse`:** X_n = n 1_{(0, 1/n]} on ([0,1], lambda): X_n -> 0 in probability and a.s., but E[|X_n|] = 1 not -> 0 -- convergence in probability does NOT imply L^1 without a dominating / uniformly integrable family

## convergence_in_distribution

- **spec:** the CLT delivers this mode: standardized sample mean -> N(0,1) in distribution
- **spec:** equivalent forms (portmanteau_theorem): E[g(X_n)] -> E[g(X)] for bounded continuous g; limsup P(X_n in C) <= P(X in C) for closed C; phi_{X_n}(t) -> phi_X(t) for all t (Levy)
- **drop `continuity_points_only`:** X_n = 1/n (constant): F_{X_n} is a step at 1/n, F_X a step at 0; F_{X_n}(0) = 0 for all n but F_X(0) = 1 -- convergence fails AT the jump but X_n -> 0 in distribution is still true

## convergence_implications

- **spec:** finite-dimensional summary: a.s. and L^p each imply p; p implies d; that is all
- **spec:** Scheffe's lemma: if densities converge a.e. then L^1 (hence p, hence d) convergence follows -- a bridge that skips the counterexamples
- **spec:** if X_n -> X in distribution and X_n -> Y in probability then X = Y in distribution
- **drop `a_s_does_not_imply_L_p`:** X_n = n 1_{(0,1/n]}: X_n -> 0 a.s. but E|X_n| = 1 (escaping mass)
- **drop `L_p_does_not_imply_a_s`:** the typewriter sequence (indicators of [j/2^k, (j+1)/2^k] in order): -> 0 in every L^p but converges a.s. for NO omega
- **drop `p_does_not_imply_a_s`:** same typewriter sequence -- in probability but not a.s.
- **drop `d_does_not_imply_p`:** X ~ N(0,1), X_n = (-1)^n X: each X_n ~ N(0,1) so X_n -> N(0,1) in distribution, but |X_n - X_{n+1}| = 2|X| does not -> 0, so not in probability
- **drop `d_to_a_nonconstant_does_not_imply_p`:** the same example -- the limit must be a CONSTANT for the reverse arrow

## portmanteau_theorem

- **spec:** A = (-inf, x], P(X = x) = 0: the CDF form
- **spec:** g bounded uniformly continuous is enough (form ii) -- the class can be shrunk
- **spec:** the Levy metric / bounded-Lipschitz metric metrizes this convergence on laws over R
- **drop `boundedness_of_g`:** g(x) = x is continuous but unbounded: E[X_n] -> E[X] can FAIL under X_n -> X in distribution (escaping mass) -- convergence of unbounded moments needs uniform integrability
- **drop `continuity_of_g`:** g = 1_{(-inf, 0]} (discontinuous): P(X_n <= 0) -> P(X <= 0) fails when X has an atom at 0
- **drop `P_of_boundary_zero_in_(v)`:** A = {0}, X ~ N(0,1) (so P(X in bd A) = P(X = 0) = 0) is fine; A = {0}, X = 0 constant is not

## continuous_mapping_theorem

- **spec:** g(x) = x^2: X_n -> X in distribution => X_n^2 -> X^2 in distribution (e.g. sqrt(n) Xbar -> N(0, sigma^2) gives n Xbar^2 -> sigma^2 chi-squared_1)
- **spec:** g continuous everywhere: the a.e. hypothesis is automatic
- **spec:** combined with Slutsky to build asymptotic distributions of test statistics (t-statistic, Wald statistic)
- **drop `P_X_gives_the_discontinuity_set_measure_zero`:** g(x) = 1_{x >= 0}, X_n = -1/n -> 0, but g(X_n) = 0 for all n while g(0) = 1 -- g is discontinuous exactly at the limit point, which here has full mass
- **drop `same_mode_out`:** if the input is only in distribution, the output is only in distribution -- you cannot upgrade

## slutsky_theorem

- **spec:** studentization: sqrt(n)(Xbar - mu)/S_n -> N(0,1), because sqrt(n)(Xbar - mu)/sigma -> N(0,1) and sigma/S_n -> 1 in probability
- **spec:** if a_n -> a and b_n -> b (deterministic) and Z_n -> Z in distribution then a_n Z_n + b_n -> a Z + b
- **drop `the_limit_c_must_be_a_constant`:** X_n = Z ~ N(0,1) for all n (so X_n -> Z in distribution), Y_n = -Z (so Y_n -> -Z in distribution, NOT to a constant): X_n + Y_n = 0, not N(0,1) + N(0,1). Slutsky needs Y_n -> constant.
- **drop `convergence_in_probability_not_just_distribution_for_Y_n`:** if Y_n -> c only in distribution (c constant) that is equivalent to in probability, so this is automatically fine -- but Y_n -> non-constant in distribution is not enough

## weak_law_large_numbers

- **spec:** X_i ~ Bernoulli(p): the relative frequency of successes -> p in probability (Bernoulli's theorem, 1713)
- **spec:** pairwise independence and finite variance are ENOUGH for this mode (the Chebyshev proof only uses pairwise uncorrelatedness)
- **spec:** Monte Carlo integration: (1/n) sum g(U_i) -> integral g in probability
- **drop `finite_mean`:** X_i ~ Cauchy: Xbar_n ~ Cauchy for every n -- no convergence to any constant (cauchy_no_mean)
- **drop `identically_distributed_ish`:** for non-identical independent X_i, Xbar_n -> the average of the means in probability provided (1/n^2) sum Var(X_i) -> 0

## strong_law_large_numbers

- **spec:** X_i ~ Bernoulli(p): the relative frequency -> p for almost every infinite sequence of trials (Borel's normal number theorem is the p = 1/2, base-2 case)
- **spec:** the empirical CDF F_n(x) -> F(x) a.s. for each x (and uniformly -- Glivenko-Cantelli)
- **spec:** renewal theory: N(t)/t -> 1/E[interarrival] a.s.
- **drop `finite_mean`:** X_i ~ Cauchy or any law with E|X_1| = inf: limsup |Xbar_n| = inf a.s. -- the sample mean has no a.s. limit and in fact oscillates unboundedly
- **drop `identically_distributed`:** Kolmogorov's SLLN for independent non-identical X_i needs sum Var(X_i)/i^2 < inf

## levy_continuity_theorem

- **spec:** CLT: phi_{S_n}(t) = phi_{X_1}(t/sqrt n)^n -> e^{-t^2/2}, continuous at 0, hence S_n -> N(0,1)
- **spec:** Poisson limit: (1 + (lambda/n)(e^{it} - 1))^n -> exp(lambda(e^{it} - 1))
- **drop `continuity_of_the_limit_phi_at_0`:** X_n ~ N(0, n): phi_{X_n}(t) = e^{-n t^2/2} -> 1_{t = 0}, which is NOT continuous at 0 -- and indeed X_n has no distributional limit (mass escapes to +-inf). The continuity condition is exactly the tightness check.
- **drop `pointwise_convergence_for_all_t`:** convergence of phi_{X_n}(t) on a bounded interval of t is not enough in general

## central_limit_theorem

- **spec:** X_i ~ Bernoulli(p): sqrt(n)(mean - p)/sqrt(p(1-p)) -> N(0,1) -- the de Moivre-Laplace theorem; the bc worksheet shows the standardized-binomial CDF at 1 approaching Phi(1)
- **spec:** X_i ~ N(mu, sigma^2): the standardized mean is EXACTLY N(0,1) for every n (not just in the limit)
- **spec:** g differentiable at mu: sqrt(n)(g(mean) - g(mu)) -> N(0, g'(mu)^2 sigma^2) -- the delta method
- **drop `finite_nonzero_variance`:** X_i ~ Cauchy (cauchy_no_mean): mean_n is again Cauchy for every n -- no normalization makes it converge to a normal. Infinite variance breaks the theorem; stable laws with index < 2 are the correct limits.
- **drop `iid_identical`:** independent but not identically distributed can fail without a further condition -- the Lindeberg condition (lindeberg_clt) is what restores the conclusion.
- **drop `iid_independent`:** strongly dependent X_i (e.g. X_i = X_1 for all i): the standardized mean is sqrt(n)(X_1 - mu)/sigma, which diverges, not converges.
- **drop `finite_mean`:** if E|X_1| = inf the centring constant mu does not exist.

## lindeberg_clt

- **spec:** X_{n,i} iid mean 0 variance sigma^2: Lindeberg reduces to E[X_1^2 1_{|X_1| > eps sqrt n}] -> 0, true by DCT -- recovers the classical CLT
- **spec:** Lyapunov: if (1/s_n^{2+delta}) sum E|X_{n,i}|^{2+delta} -> 0 for some delta > 0, then Lindeberg holds
- **spec:** regression residuals, weighted sums with bounded weights, m-dependent sequences
- **drop `lindeberg_condition`:** X_{n,1} ~ N(0, n), X_{n,2}, ..., X_{n,n} ~ iid N(0,1): s_n^2 = 2n - 1 but the first term carries ~half the variance; the normalized sum is NOT asymptotically normal (it stays a 50-50 mix). One dominant term breaks the CLT.
- **drop `independence_within_rows`:** strong dependence needs a different CLT (martingale CLT, mixing conditions)

## delta_method

- **spec:** g(x) = x^2 at theta: asymptotic variance 4 theta^2 sigma^2 (degenerate at theta = 0 -- then a chi-squared limit at rate n, the SECOND-order delta method)
- **spec:** g = log: stabilizes a variance that scales with the mean (log-transform for count / ratio data)
- **spec:** the asymptotic variance of a sample correlation, an odds ratio, an R^2 -- all standard delta-method calculations
- **drop `g_prime_theta_nonzero`:** g(x) = x^2 at theta = 0: g'(0) = 0, the first-order limit is degenerate; n(g(T_n) - g(theta)) -> sigma^2 chi-squared_1 instead (a different rate AND a non-normal limit)
- **drop `differentiability_at_theta`:** g with a kink at theta (e.g. |x - theta|): no single derivative, the limit is a folded normal

## conditional_expectation_elementary

- **spec:** X, Y independent: E[X | Y] = E[X] (constant)
- **spec:** X = Y: E[X | Y] = Y
- **spec:** bivariate normal: E[Y | X] = mu_Y + rho (sigma_Y/sigma_X)(X - mu_X) -- linear regression
- **spec:** E[X | Y] is the best predictor of X from Y in mean square (conditional_expectation_l2_projection)
- **drop `positive_mass_or_density_at_y`:** conditioning on { Y = y } with P(Y = y) = 0 and no joint density is ambiguous (Borel-Kolmogorov) -- needs the abstract construction
- **drop `integrability_of_X`:** E[X | Y = y] can fail to exist for each y if E|X| = inf

## conditional_expectation_abstract

- **spec:** G = { empty, Omega }: E[X | G] = E[X] (a constant)
- **spec:** G = F: E[X | G] = X
- **spec:** X G-measurable: E[X | G] = X; X independent of G: E[X | G] = E[X]
- **spec:** pull-out: E[Y X | G] = Y E[X | G] when Y is G-measurable and bounded
- **drop `integrability_of_X`:** for X >= 0 not integrable one defines E[X | G] in [0, inf] by monotone approximation; for signed non-integrable X it need not exist
- **drop `measurability_condition_(i)`:** dropping (i) makes Z = X trivially satisfy (ii) -- the content is that Z is COARSER (G-measurable), a genuine projection / averaging

## conditional_expectation_existence

- **spec:** X in L^2: E[X | G] is the L^2-orthogonal projection of X onto L^2(Omega, G, P) -- the geometric picture
- **spec:** X = 1_B: E[1_B | G] is the 'conditional probability' P(B | G), a G-measurable [0,1]-valued random variable
- **drop `integrability_of_X`:** without X in L^1 (or X >= 0), the signed measure A |-> integral_A X dP may not be finite and Radon-Nikodym does not apply directly
- **drop `sigma_finiteness_is_automatic`:** P|_G is a probability measure, so the sigma-finiteness hypothesis of Radon-Nikodym is free here

## tower_property

- **spec:** H = { empty, Omega }: E[E[X | G]] = E[X] -- compute a mean by conditioning (first-step analysis, LOTUS for expectations)
- **spec:** E[X] = sum_i E[X | B_i] P(B_i) for a partition -- the law-of-total-probability analogue
- **spec:** martingale: E[X_{n+1} | F_n] = X_n gives E[X_m | F_n] = X_n for m > n by iterating
- **drop `nesting_H_subset_G`:** if H and G are not nested, E[E[X | G] | H] need NOT equal E[X | H]: with X, G, H chosen so G and H are independent and both informative about X, iterating loses information both ways and the two sides differ
- **drop `integrability`:** needs X in L^1 for all the conditional expectations to exist

## law_of_total_variance

- **spec:** G = sigma(Y): Var(X) = E[Var(X | Y)] + Var(E[X | Y]) -- the ANOVA / random-effects decomposition; R^2 = Var(E[X|Y])/Var(X) is the fraction 'explained' by Y
- **spec:** hierarchical models: total variance = measurement variance + between-unit variance
- **spec:** compound distributions: Var(sum_{i=1}^N Y_i) = E[N] Var(Y) + Var(N) (E Y)^2 for N ⟂ iid Y_i
- **drop `finite_second_moment`:** X must be in L^2 for all three variances to be finite
- **drop `both_terms_nonnegative`:** E[Var(X|G)] >= 0 and Var(E[X|G]) >= 0, so conditioning can only REDUCE expected variance: E[Var(X|G)] <= Var(X)

## conditional_expectation_l2_projection

- **spec:** G = sigma(Y): E[X | Y] = argmin_{g measurable} E[(X - g(Y))^2] -- nonparametric regression is estimating this
- **spec:** restricting Z to AFFINE functions of Y gives the best LINEAR predictor mu_X + (Cov(X,Y)/Var Y)(Y - mu_Y) -- equals E[X|Y] iff (X,Y) jointly normal
- **spec:** the Pythagorean identity: E[X^2] = E[(E[X|G])^2] + E[(X - E[X|G])^2]
- **drop `finite_second_moment`:** the projection picture needs X in L^2; for X in L^1 only, E[X | G] still exists (conditional_expectation_existence) but is not a projection and is not a mean-square minimizer
- **drop `G_measurable_predictors_only`:** allowing Z to depend on more than G lets Z = X drive the error to 0 -- the constraint Z in L^2(G) is the whole point

## martingale

- **spec:** S_n = sum of iid mean-0 increments: a martingale w.r.t. its natural filtration
- **spec:** M_n = E[Y | F_n] for a fixed integrable Y (a Doob martingale): converges a.s. and in L^1 to E[Y | F_inf]
- **spec:** the likelihood ratio prod (q(X_i)/p(X_i)) under p: a nonnegative martingale
- **drop `adaptedness_and_integrability`:** if X_n is not F_n-measurable or not integrable the conditional expectation is ill-posed
- **drop `the_equality_(fair_game)`:** E[X_{n+1} | F_n] > X_n (submartingale) models a favorable game -- convex functions of a martingale are submartingales (conditional Jensen)

## stochastic_process

- **spec:** T = N: a discrete-time sequence (e.g. a Markov chain, a time series)
- **spec:** T = [0, inf), continuous paths: Brownian motion, diffusions
- **spec:** T = [0, inf), piecewise-constant paths: the Poisson process, continuous-time Markov chains
- **drop `one_common_probability_space`:** a process is more than its marginals -- the joint law across times (the dependence) is the object of interest
- **drop `path_regularity_is_extra`:** the f.d.d.s do not determine path properties; { X_t continuous } may not even be measurable without choosing a good modification

## kolmogorov_extension_theorem

- **spec:** iid sequences: mu_{t_1,...,t_k} = mu^{tensor k} is trivially consistent -- gives the infinite product measure
- **spec:** Markov chains: mu built from an initial law and a transition kernel via Chapman-Kolmogorov consistency
- **spec:** Gaussian processes: any symmetric positive-semidefinite covariance function K(s,t) yields a centered Gaussian process
- **drop `consistency_of_the_f_d_d_s`:** an inconsistent family (e.g. mu_{1,2} with a marginal on coordinate 1 disagreeing with mu_1) realizes no process -- consistency is necessary and sufficient
- **drop `the_product_sigma_algebra_only`:** the resulting measure only sees cylinder events; { t |-> X_t continuous } is NOT in the product sigma-algebra -- path properties need a separate modification argument (Kolmogorov-Chentsov)
