"""Cited bridge roots — imported from math-probability / math-real-analysis, or
(for linear algebra) assumed with no capsule.  Thin stubs: the statement, the
citation, lean_status: cited."""
from nodespec import ROOT

# --- math-probability -------------------------------------------------------
ROOT("prob_probability_space", "math-probability:probability_space",
     "A probability space (Omega, F, P): a sigma-algebra F of events and a countably additive P with P(Omega)=1.")
ROOT("prob_random_variable", "math-probability:random_variable",
     "A random variable X: Omega -> R is F/Borel-measurable; its law is the pushforward P o X^{-1}.")
ROOT("prob_random_vector", "math-probability:random_variable",
     "A random vector X: Omega -> R^k is measurable into the Borel sigma-algebra of R^k.")
ROOT("prob_cdf", "math-probability:cdf",
     "F_X(x) = P(X <= x): nondecreasing, right-continuous, limits 0 and 1; determines the law.")
ROOT("prob_pmf", "math-probability:pmf",
     "For discrete X, p_X(x) = P(X = x); sums to 1 over the countable support.")
ROOT("prob_pdf", "math-probability:pdf",
     "For absolutely continuous X, a density f_X >= 0 with P(X in A) = int_A f_X dx (Radon-Nikodym).")
ROOT("prob_joint_distribution", "math-probability:joint_distribution",
     "The law of (X_1,...,X_n) on R^n; for an independent sample it is the product of the marginals.")
ROOT("prob_marginal_distribution", "math-probability:marginal_distribution",
     "The law of a subvector, obtained by integrating the joint density over the other coordinates.")
ROOT("prob_conditional_distribution", "math-probability:conditional_distribution",
     "The law of X given Y = y, with density f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y) where f_Y(y) > 0.")
ROOT("prob_expectation", "math-probability:expectation",
     "E[X] = int X dP = int x dF_X(x), defined when E|X| < inf.")
ROOT("prob_lotus", "math-probability:lotus",
     "Law of the unconscious statistician: E[g(X)] = int g(x) dF_X(x).")
ROOT("prob_expectation_linearity", "math-probability:expectation_linearity",
     "E[aX + bY] = a E[X] + b E[Y] whenever the expectations exist (no independence needed).")
ROOT("prob_variance", "math-probability:variance",
     "Var(X) = E[(X - E X)^2] = E[X^2] - (E X)^2 >= 0; Var(aX + b) = a^2 Var(X).")
ROOT("prob_covariance", "math-probability:covariance",
     "Cov(X,Y) = E[XY] - E[X]E[Y]; bilinear, symmetric, Cov(X,X) = Var(X).")
ROOT("prob_correlation", "math-probability:correlation",
     "rho(X,Y) = Cov(X,Y) / sqrt(Var X Var Y) in [-1, 1]; |rho| = 1 iff an a.s. affine relation.")
ROOT("prob_mgf", "math-probability:mgf",
     "M_X(t) = E[e^{tX}]; where finite near 0 it determines the law, and M_{X+Y} = M_X M_Y for independent X, Y.")
ROOT("prob_characteristic_function", "math-probability:characteristic_function",
     "phi_X(t) = E[e^{itX}]; always exists, |phi_X| <= 1, determines the law, phi_{X+Y} = phi_X phi_Y for independent X, Y.")
ROOT("prob_moment", "math-probability:moment",
     "The k-th (raw) moment E[X^k] and central moment E[(X - E X)^k], when E|X|^k < inf.")
ROOT("prob_independence_rv", "math-probability:independence_random_variables",
     "X, Y independent iff the joint law factorizes: F_{X,Y}(x,y) = F_X(x) F_Y(y) for all x, y.")
ROOT("prob_iid", "math-probability:iid",
     "X_1, X_2, ... are independent and identically distributed: mutually independent, one common law.")
ROOT("prob_independence_factorization", "math-probability:independence_factorization",
     "X _||_ Y implies E[g(X) h(Y)] = E[g(X)] E[h(Y)] for all bounded measurable g, h; hence Cov = 0.")
ROOT("prob_conditional_expectation", "math-probability:conditional_expectation_abstract",
     "E[X | G]: the a.s.-unique G-measurable random variable with E[(X - E[X|G]) 1_A] = 0 for every A in G; the L^2 projection of X onto L^2(G).")
ROOT("prob_tower_property", "math-probability:tower_property",
     "E[E[X | G]] = E[X]; more generally E[E[X | G] | H] = E[X | H] for H subset G.")
ROOT("prob_law_total_variance", "math-probability:law_of_total_variance",
     "Var(X) = E[Var(X | T)] + Var(E[X | T]); the second term alone is <= Var(X).")
ROOT("prob_bernoulli", "math-probability:bernoulli_distribution",
     "Bernoulli(p): P(X=1)=p, P(X=0)=1-p; mean p, variance p(1-p); a one-parameter exponential family.")
ROOT("prob_binomial", "math-probability:binomial_distribution",
     "Binomial(n,p): the sum of n iid Bernoulli(p); mean np, variance np(1-p).")
ROOT("prob_poisson", "math-probability:poisson_distribution",
     "Poisson(lambda): P(X=k) = e^{-lambda} lambda^k / k!; mean = variance = lambda; closed under independent sums.")
ROOT("prob_uniform_continuous", "math-probability:continuous_uniform_distribution",
     "Uniform(a,b): density 1/(b-a) on [a,b]; mean (a+b)/2, variance (b-a)^2/12.")
ROOT("prob_exponential", "math-probability:exponential_distribution",
     "Exponential(lambda): density lambda e^{-lambda x} on x >= 0; mean 1/lambda; the unique memoryless continuous law.")
ROOT("prob_gamma", "math-probability:gamma_distribution",
     "Gamma(k, theta): density proportional to x^{k-1} e^{-x/theta}; additive in the shape k for a common rate.")
ROOT("prob_beta", "math-probability:beta_distribution",
     "Beta(a,b): density proportional to x^{a-1}(1-x)^{b-1} on [0,1]; mean a/(a+b); conjugate to the binomial.")
ROOT("prob_normal", "math-probability:normal_distribution",
     "Normal(mu, sigma^2): density (2 pi sigma^2)^{-1/2} exp(-(x-mu)^2 / 2 sigma^2); a two-parameter exponential family.")
ROOT("prob_standard_normal", "math-probability:standard_normal",
     "N(0,1): mean 0, variance 1; CDF Phi, density phi; quantiles z_p = Phi^{-1}(p).")
ROOT("prob_normal_affine_closure", "math-probability:normal_affine_closure",
     "aX + b is normal when X is; independent sums of normals are normal, with means and variances adding.")
ROOT("prob_cauchy_no_mean", "math-probability:cauchy_no_mean",
     "The Cauchy law has no mean; the sample mean of n iid Cauchy variables has the same Cauchy law for every n.")
ROOT("prob_conv_as", "math-probability:convergence_almost_sure",
     "X_n -> X almost surely: P(X_n -> X) = 1. Implies convergence in probability.")
ROOT("prob_conv_p", "math-probability:convergence_in_probability",
     "X_n -> X in probability: P(|X_n - X| > eps) -> 0 for every eps > 0. Implies convergence in distribution.")
ROOT("prob_conv_d", "math-probability:convergence_in_distribution",
     "X_n -> X in distribution: F_{X_n}(x) -> F_X(x) at every continuity point of F_X.")
ROOT("prob_wlln", "math-probability:weak_law_large_numbers",
     "For iid X_i with E|X_1| < inf, the sample mean converges to E[X_1] in probability.")
ROOT("prob_slln", "math-probability:strong_law_large_numbers",
     "For iid X_i with E|X_1| < inf, the sample mean converges to E[X_1] almost surely.")
ROOT("prob_clt", "math-probability:central_limit_theorem",
     "For iid X_i with mean mu and variance sigma^2 in (0, inf), sqrt(n)(Xbar_n - mu)/sigma -> N(0,1) in distribution.")
ROOT("prob_levy_continuity", "math-probability:levy_continuity_theorem",
     "phi_{X_n}(t) -> phi(t) pointwise with phi continuous at 0 iff X_n converges in distribution to the law with CF phi.")
ROOT("prob_slutsky", "math-probability:slutsky_theorem",
     "If X_n -> X in distribution and Y_n -> c (constant) in probability, then X_n + Y_n -> X + c and X_n Y_n -> cX in distribution.")
ROOT("prob_continuous_mapping", "math-probability:continuous_mapping_theorem",
     "If g is continuous P_X-a.s. and X_n -> X (a.s. / in prob / in dist), then g(X_n) -> g(X) in the same mode.")
ROOT("prob_delta_method", "math-probability:delta_method",
     "If sqrt(n)(T_n - theta) -> N(0, v) and g is differentiable at theta, then sqrt(n)(g(T_n) - g(theta)) -> N(0, g'(theta)^2 v).")
ROOT("prob_markov_ineq", "math-probability:markov_inequality",
     "For X >= 0 and a > 0, P(X >= a) <= E[X] / a.")
ROOT("prob_chebyshev_ineq", "math-probability:chebyshev_inequality",
     "P(|X - mu| >= k sigma) <= 1/k^2, where mu = E[X], sigma^2 = Var(X) < inf.")
ROOT("prob_jensen_ineq", "math-probability:jensen_inequality",
     "For convex phi, phi(E[X]) <= E[phi(X)]; conditional form phi(E[X|G]) <= E[phi(X)|G].")
ROOT("prob_cauchy_schwarz", "math-probability:cauchy_schwarz_expectation",
     "E[XY]^2 <= E[X^2] E[Y^2]; equality iff X and Y are a.s. proportional.")
ROOT("prob_hoeffding", "math-probability:hoeffding_inequality",
     "For independent X_i in [a_i, b_i], P(S_n - E S_n >= t) <= exp(-2 t^2 / sum (b_i - a_i)^2).")

# --- math-real-analysis ----------------------------------------------------
ROOT("ra_continuity", "math-real-analysis:continuity",
     "f is continuous at x_0 if for every eps > 0 there is delta > 0 with |f(x) - f(x_0)| < eps whenever |x - x_0| < delta.")
ROOT("ra_differentiability", "math-real-analysis:differentiation",
     "f is differentiable at x_0 if the limit f'(x_0) = lim_{h->0} (f(x_0+h) - f(x_0))/h exists; in R^d, the gradient.")
ROOT("ra_taylor_theorem", "math-real-analysis:taylor_theorem",
     "f(x) = sum_{j<n} f^{(j)}(a)(x-a)^j / j! + R_n with R_n = f^{(n)}(xi)(x-a)^n / n! for some xi between a and x.")
ROOT("ra_mean_value_theorem", "math-real-analysis:mean_value_theorem",
     "If f is continuous on [a,b] and differentiable on (a,b), then f(b) - f(a) = f'(c)(b - a) for some c in (a,b).")
ROOT("ra_compactness", "math-real-analysis:compactness",
     "A continuous real function on a nonempty compact set attains its maximum and minimum (extreme value theorem).")
ROOT("ra_convex_function", "math-real-analysis:convex_function",
     "f is convex if f(t x + (1-t) y) <= t f(x) + (1-t) f(y) for all x, y and t in [0,1]; twice-differentiable iff f'' >= 0.")
ROOT("ra_interchange_limit_integral", "math-real-analysis:interchange_limit_integral",
     "If |d/dtheta f(x; theta)| <= g(x) with int g < inf, then d/dtheta int f(x; theta) dx = int d/dtheta f(x; theta) dx (dominated convergence).")

# --- no capsule: finite-dimensional linear algebra ------------------------
ROOT("linear_algebra_background", "linear-algebra:background-assumed",
     "Assumed without a capsule: vector spaces and subspaces, rank, transpose, inverse; symmetric and positive-(semi)definite matrices; the spectral theorem for real symmetric matrices; orthogonal projection onto a subspace and its idempotent symmetric projection matrix; trace; quadratic forms x^T A x. FLAGGED for a future math-linear-algebra capsule.")
