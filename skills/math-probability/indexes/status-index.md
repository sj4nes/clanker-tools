# Result index by node type (generated)

## primitive
- **set_algebra** (logic) — unions, intersections, complements, De Morgan, indexed families (from math-sets)
- **preimage_algebra** (logic) — f^-1 commutes with union, intersection, complement (from math-sets)
- **countable_set** (logic) — injects into N; countable unions of countable sets are countable (from math-sets)
- **real_field** (analysis) — the least-upper-bound property and its consequences (from math-real-analysis)
- **sequence_limit** (analysis) — epsilon-N convergence, algebra of limits, squeeze (from math-real-analysis)
- **limsup_liminf** (analysis) — limsup A_n = intersection of tails; for sets, {omega in infinitely many A_n}
- **series_convergence** (analysis) — partial sums, comparison, absolute convergence (from math-real-analysis)
- **convex_function** (analysis) — f(tx+(1-t)y) <= t f(x)+(1-t)f(y); supporting line at every interior point

## axiom
- **kolmogorov_axioms** (probability_space) — P >= 0 ; P(Omega) = 1 ; P is countably additive on disjoint events

## structure
- **measurable_space** (measure) — a pair (Omega, F) with F a sigma-algebra on Omega
- **probability_space** (probability_space) — a triple (Omega, F, P) satisfying the Kolmogorov axioms

## notation_convention
- **almost_sure** (measure) — an event of probability 1; "P-a.s." = "outside a P-null set"

## principle_law

## definition
- **sigma_algebra** (measure) — a family of subsets closed under complement and countable union, containing Omega
- **borel_sigma_algebra** (measure) — B(R) = sigma(open intervals); the events a real random variable can produce
- **measure** (measure) — mu: F -> [0, infinity], mu(empty)=0, countably additive on disjoint unions
- **null_set** (measure) — N in F with mu(N) = 0; a property holds almost everywhere if it fails only on a null set
- **probability_measure** (probability_space) — a measure P on (Omega, F) with P(Omega) = 1
- **conditional_probability** (independence) — P(A | B) = P(A cap B) / P(B) when P(B) > 0
- **measurable_function** (random_variable) — f^-1(B) in F for every B in the target sigma-algebra
- **random_variable** (random_variable) — a measurable function X: (Omega,F) -> (R, B(R)) (or R^d, B(R^d))
- **distribution_pushforward** (random_variable) — P_X = P compose X^-1, a probability measure on (R, B(R))
- **cdf** (random_variable) — F_X(x) = P(X <= x)
- **discrete_rv** (random_variable) — X takes values in a countable set
- **pmf** (random_variable) — p_X(x) = P(X = x) ; sums to 1 over the support
- **absolutely_continuous_rv** (random_variable) — P_X << Lebesgue measure
- **pdf** (random_variable) — f_X = dP_X/dLebesgue ; P(X in B) = integral_B f_X ; f_X >= 0, integrates to 1
- **quantile_function** (random_variable) — F_X^-1(u) = inf { x : F_X(x) >= u }, the generalized inverse
- **joint_distribution** (random_variable) — the law of the random vector (X_1,...,X_n) on (R^n, B(R^n))
- **marginal_distribution** (random_variable) — the law of a subvector, obtained by integrating out the others
- **conditional_distribution** (random_variable) — f_{Y|X}(y|x) = f_{X,Y}(x,y) / f_X(x) where f_X(x) > 0
- **independence_events** (independence) — P(cap_{i in S} A_i) = prod_{i in S} P(A_i) for every finite S (mutual)
- **independence_sigma_algebras** (independence) — P(A cap B) = P(A)P(B) for all A in G_1, B in G_2
- **independence_random_variables** (independence) — the generated sigma-algebras are independent ; equivalently the joint law is a product
- **iid** (independence) — (X_n) mutually independent and all with the same law
- **expectation** (expectation) — E[X] = integral X dP, defined when E[|X|] < infinity (or X >= 0)
- **variance** (moments) — Var(X) = E[(X - E[X])^2], defined when E[X^2] < infinity
- **covariance** (moments) — Cov(X,Y) = E[(X-E[X])(Y-E[Y])] = E[XY] - E[X]E[Y]
- **correlation** (moments) — rho(X,Y) = Cov(X,Y) / (sd(X) sd(Y)) ; |rho| <= 1 by Cauchy-Schwarz
- **moment** (moments) — m_k = E[X^k] ; mu_k = E[(X - E[X])^k] ; skewness, kurtosis
- **lp_space** (moments) — L^p(P) = { X : E[|X|^p] < infinity }, norm ||X||_p = E[|X|^p]^{1/p}
- **mgf** (moments) — M_X(t) = E[e^{tX}], where it is finite on a neighborhood of 0
- **characteristic_function** (moments) — phi_X(t) = E[e^{i t X}] ; always exists, |phi_X| <= 1, phi_X(0) = 1
- **bernoulli_distribution** (distributions) — P(X=1)=p, P(X=0)=1-p ; E=p, Var=p(1-p) ; MGF (1-p)+p e^t
- **binomial_distribution** (distributions) — sum of n iid Bernoulli(p) ; P(X=k)=C(n,k)p^k(1-p)^{n-k} ; E=np, Var=np(1-p)
- **geometric_distribution** (distributions) — P(X=k)=(1-p)^{k-1}p ; E=1/p, Var=(1-p)/p^2 ; memoryless
- **poisson_distribution** (distributions) — P(X=k)=e^{-lambda} lambda^k / k! ; E=Var=lambda ; MGF exp(lambda(e^t-1))
- **continuous_uniform_distribution** (distributions) — f(x) = 1/(b-a) on [a,b] ; E=(a+b)/2, Var=(b-a)^2/12
- **exponential_distribution** (distributions) — f(x)=lambda e^{-lambda x}, x>=0 ; E=1/lambda, Var=1/lambda^2 ; memoryless
- **gamma_distribution** (distributions) — f(x) prop x^{k-1} e^{-x/theta} ; sum of k iid Exponential ; E=k theta, Var=k theta^2
- **beta_distribution** (distributions) — f(x) prop x^{a-1}(1-x)^{b-1} on [0,1] ; conjugate prior for a Bernoulli rate
- **normal_distribution** (distributions) — f(x) = (1/(sigma sqrt(2 pi))) exp(-(x-mu)^2/(2 sigma^2)) ; E=mu, Var=sigma^2
- **standard_normal** (distributions) — Z ~ N(0,1) ; CF exp(-t^2/2) ; Z = (X - mu)/sigma
- **convergence_almost_sure** (convergence) — P( X_n -> X ) = 1  (convergence mode tag: a.s.)
- **convergence_in_probability** (convergence) — for all eps > 0, P(|X_n - X| > eps) -> 0  (mode tag: p)
- **convergence_in_lp** (convergence) — E[|X_n - X|^p] -> 0  (mode tag: L^p)
- **convergence_in_distribution** (convergence) — F_{X_n}(x) -> F_X(x) at every continuity point of F_X  (mode tag: d)
- **conditional_expectation_elementary** (conditional_expectation) — E[X | Y = y] = sum x p_{X|Y}(x|y)  (or the density analogue)
- **conditional_expectation_abstract** (conditional_expectation) — E[X | G] is the a.s.-unique G-measurable Z with integral_A Z = integral_A X for all A in G

## construction
- **generated_sigma_algebra** (measure) — sigma(C) is the smallest sigma-algebra containing the collection C
- **lebesgue_measure_caratheodory** (measure) — the outer-measure / Caratheodory extension gives Lebesgue measure on B(R) (CITED)

## proposition
- **measure_monotonicity** (measure) — A subset B => mu(A) <= mu(B); mu(union A_n) <= sum mu(A_n)
- **measure_continuity** (measure) — A_n up A => mu(A_n) -> mu(A); A_n down A with mu(A_1)<inf => mu(A_n) -> mu(A)
- **finite_additivity** (probability_space) — pairwise disjoint A_1..A_n => P(union) = sum P(A_i)  (from countable additivity)
- **continuity_of_probability** (probability_space) — A_n up A => P(A_n) -> P(A) ; A_n down A => P(A_n) -> P(A)
- **expectation_monotonicity** (expectation) — X <= Y a.s. => E[X] <= E[Y] ; |E[X]| <= E[|X|]
- **covariance_bilinear** (moments) — Cov is symmetric bilinear ; Cov(X,X) = Var(X)
- **memorylessness** (distributions) — P(X > s+t | X > s) = P(X > t) ; characterizes geometric (discrete) and exponential (continuous)
- **normal_affine_closure** (distributions) — aX+b ~ N(a mu + b, a^2 sigma^2) ; independent normals sum to a normal

## theorem
- **dynkin_pi_lambda** (measure) — a lambda-system containing a pi-system contains the sigma-algebra it generates
- **inclusion_exclusion** (probability_space) — P(union A_i) = sum P(A_i) - sum P(A_i cap A_j) + ...
- **boole_inequality** (probability_space) — P(union A_n) <= sum P(A_n)
- **borel_cantelli_first** (probability_space) — sum P(A_n) < infinity  =>  P(A_n infinitely often) = 0
- **borel_cantelli_second** (probability_space) — A_n independent and sum P(A_n) = infinity  =>  P(A_n infinitely often) = 1
- **law_of_total_probability** (independence) — {B_i} a partition, P(B_i)>0  =>  P(A) = sum P(A|B_i) P(B_i)
- **bayes_theorem** (independence) — P(B_j | A) = P(A|B_j) P(B_j) / sum_i P(A|B_i) P(B_i)
- **cdf_properties** (random_variable) — F nondecreasing, right-continuous, F(-inf)=0, F(+inf)=1 ; every such F is some law
- **cdf_determines_law** (random_variable) — F_X = F_Y  =>  P_X = P_Y  (pi-lambda on the half-lines)
- **probability_integral_transform** (random_variable) — F continuous => F(X) ~ Uniform(0,1) ; and F^-1(U) has law F  (the simulation bridge)
- **transformation_univariate** (random_variable) — Y = g(X), g monotone C^1 => f_Y(y) = f_X(g^-1(y)) |d/dy g^-1(y)|
- **jacobian_transformation** (random_variable) — Y = g(X), g a diffeomorphism => f_Y(y) = f_X(g^-1(y)) |det J_{g^-1}(y)|
- **independence_factorization** (independence) — X,Y independent iff F_{X,Y} = F_X F_Y iff (densities) f_{X,Y} = f_X f_Y
- **convolution_formula** (independence) — X,Y independent => f_{X+Y}(z) = integral f_X(x) f_Y(z-x) dx  (sum in the discrete case)
- **lotus** (expectation) — E[g(X)] = integral g dP_X = sum g(x) p_X(x) = integral g(x) f_X(x) dx
- **expectation_linearity** (expectation) — E[aX + bY] = a E[X] + b E[Y]  (no independence needed)
- **markov_inequality** (inequalities) — X >= 0, a > 0  =>  P(X >= a) <= E[X] / a
- **jensen_inequality** (inequalities) — phi convex, E[|X|]<inf  =>  phi(E[X]) <= E[phi(X)]
- **chebyshev_inequality** (inequalities) — k > 0  =>  P(|X - E[X]| >= k) <= Var(X) / k^2
- **cauchy_schwarz_expectation** (inequalities) — (E[XY])^2 <= E[X^2] E[Y^2]
- **variance_of_sum** (moments) — Var(sum X_i) = sum Var(X_i) + 2 sum_{i<j} Cov(X_i, X_j)
- **independence_expectation** (independence) — X,Y independent and integrable  =>  E[XY] = E[X] E[Y] ; hence Cov = 0
- **moment_ladder** (moments) — on a probability space, p > q >= 1  =>  ||X||_q <= ||X||_p , so L^p subset L^q
- **holder_inequality** (inequalities) — 1/p + 1/q = 1  =>  E[|XY|] <= ||X||_p ||Y||_q
- **mgf_moments** (moments) — M_X finite near 0 => M_X is C^infinity there and M_X^{(k)}(0) = E[X^k]
- **mgf_uniqueness** (moments) — M_X = M_Y finite on a neighborhood of 0  =>  P_X = P_Y
- **cf_properties** (moments) — uniformly continuous ; phi determines the law (inversion) ; phi_{aX+b}(t) = e^{itb} phi_X(at)
- **chernoff_bound** (inequalities) — P(X >= a) <= inf_{t>0} e^{-ta} M_X(t)  (Markov applied to e^{tX})
- **hoeffding_inequality** (inequalities) — X_i independent in [a_i,b_i]  =>  P(S - E[S] >= s) <= exp(-2 s^2 / sum (b_i-a_i)^2)
- **poisson_limit_theorem** (distributions) — Binomial(n, lambda/n) -> Poisson(lambda) as n -> infinity
- **convergence_implications** (convergence) — a.s. => p ; L^p => p ; p => d ; p => a.s. subsequence ; d to a constant => p ; none reverse in general
- **portmanteau_theorem** (convergence) — X_n -> X in distribution iff E[g(X_n)] -> E[g(X)] for all bounded continuous g (and 3 more forms)
- **continuous_mapping_theorem** (convergence) — X_n -> X (a.s. / p / d) and g continuous on a set of P_X-measure 1 => g(X_n) -> g(X) in the same mode
- **slutsky_theorem** (convergence) — X_n -> X in d, Y_n -> c in p  =>  X_n + Y_n -> X + c and X_n Y_n -> cX in d
- **weak_law_large_numbers** (convergence) — X_i iid, E|X_1| < inf  =>  sample mean -> E[X_1] in probability  (mode tag: p)
- **strong_law_large_numbers** (convergence) — X_i iid, E|X_1| < inf  =>  sample mean -> E[X_1] almost surely  (mode tag: a.s.)
- **levy_continuity_theorem** (convergence) — phi_{X_n}(t) -> phi(t) for all t, phi continuous at 0  =>  X_n -> X in distribution (CITED)
- **central_limit_theorem** (convergence) — X_i iid, mean mu, var sigma^2 in (0,inf)  =>  sqrt(n)(mean - mu)/sigma -> N(0,1) in distribution (CITED)
- **lindeberg_clt** (convergence) — independent, not identically distributed ; the Lindeberg condition  =>  normalized sum -> N(0,1) (CITED)
- **delta_method** (convergence) — sqrt(n)(T_n - theta) -> N(0,sigma^2), g differentiable  =>  sqrt(n)(g(T_n)-g(theta)) -> N(0, g'(theta)^2 sigma^2)
- **conditional_expectation_existence** (conditional_expectation) — X integrable  =>  E[X|G] exists and is a.s. unique (Radon-Nikodym, or L^2 projection then extend) (CITED)
- **tower_property** (conditional_expectation) — H subset G  =>  E[ E[X|G] | H ] = E[X|H] ; in particular E[E[X|G]] = E[X]
- **law_of_total_variance** (conditional_expectation) — Var(X) = E[ Var(X|G) ] + Var( E[X|G] )
- **conditional_expectation_l2_projection** (conditional_expectation) — for X in L^2, E[X|G] minimizes E[(X - Z)^2] over G-measurable Z

## corollary

## mathematical_identity

