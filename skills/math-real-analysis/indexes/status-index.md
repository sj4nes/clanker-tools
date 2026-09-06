# Result index by node type (generated)

## primitive
- **set** (foundations) — -
- **natural_number** (foundations) — Peano: 1 in N; successor; induction
- **rational_field** (foundations) — Q is an ordered field, not complete
- **real_number** (reals) — -

## notation_convention
- **epsilon_delta** (cross_domain) — quantifier order is forall eps exists delta/N

## definition
- **function** (foundations) — f assigns to each x in D exactly one f(x)
- **absolute_value** (foundations) — |x| = x if x>=0 else -x
- **upper_bound** (reals) — u is an upper bound of A if a <= u for all a in A
- **supremum** (reals) — sup A is the least upper bound of A
- **infimum** (reals) — inf A is the greatest lower bound of A
- **completeness_of_R** (reals) — R is an ordered field satisfying lub_axiom
- **interval** (reals) — a subset I of R such that x,y in I, x<z<y implies z in I
- **sequence** (sequences) — a function x : N -> R
- **sequence_convergence** (sequences) — forall eps>0 exists N forall n>=N |x_n - L| < eps
- **subsequence** (sequences) — x composed with a strictly increasing n_j : N -> N
- **subsequential_limit** (sequences) — a limit of some convergent subsequence
- **cauchy_sequence** (sequences) — forall eps>0 exists N forall m,n>=N |x_m - x_n| < eps
- **limsup_liminf** (sequences) — limsup x_n = inf_N sup_{n>=N} x_n ; liminf dually
- **series** (series) — the formal sum of the terms of a sequence
- **partial_sum** (series) — s_n = a_1 + ... + a_n
- **series_convergence** (series) — Sigma a_n converges if the partial sums converge
- **absolute_convergence** (series) — Sigma a_n converges absolutely if Sigma |a_n| converges
- **open_set** (topology) — U is open if every point has an interval neighbourhood inside U
- **closed_set** (topology) — A is closed if its complement is open
- **limit_point** (topology) — every neighbourhood of p meets A in a point other than p
- **closure** (topology) — the union of A with its set of limit points
- **open_cover** (topology) — a family of open sets whose union contains A
- **compact_set** (topology) — every open cover of K has a finite subcover
- **connected_set** (topology) — not the union of two disjoint nonempty relatively open sets
- **function_limit** (continuity) — forall eps>0 exists delta>0 : 0<|x-c|<delta implies |f(x)-L|<eps
- **continuity_at_point** (continuity) — forall eps>0 exists delta>0 : |x-c|<delta implies |f(x)-f(c)|<eps
- **continuity_on_set** (continuity) — f is continuous at every point of D
- **uniform_continuity** (continuity) — forall eps>0 exists delta>0 forall x,y |x-y|<delta implies |f(x)-f(y)|<eps
- **derivative** (differentiation) — f'(c) = lim_{x->c} (f(x)-f(c))/(x-c) when the limit exists
- **partition** (integration) — a finite set a = t_0 < ... < t_n = b
- **darboux_sums** (integration) — U(f,P) = sum M_i dt_i ; L(f,P) = sum m_i dt_i
- **riemann_integral** (integration) — the common value of inf_P U(f,P) and sup_P L(f,P) when they are equal
- **pointwise_convergence** (function_sequences) — f_n(x) -> f(x) for each fixed x in D
- **uniform_convergence** (function_sequences) — sup_{x in D} |f_n(x) - f(x)| -> 0
- **power_series** (function_sequences) — Sigma a_n (x - c)^n
- **radius_of_convergence** (function_sequences) — 1/R = limsup |a_n|^{1/n} ; converges for |x-c| < R

## axiom
- **lub_axiom** (reals) — every nonempty subset of R bounded above has a supremum in R
- **axiom_of_choice** (cross_domain) — every family of nonempty sets has a choice function
- **countable_choice** (cross_domain) — a countable family of nonempty sets has a choice function

## structure
- **ordered_field** (foundations) — field axioms + total order compatible with + and *

## hypothesis
- **bounded_sequence** (sequences) — exists M forall n |x_n| <= M
- **monotone_sequence** (sequences) — nondecreasing or nonincreasing
- **bounded_set** (topology) — A subset of some [-M, M]
- **bounded_function** (integration) — exists M forall x in D |f(x)| <= M
- **monotone_function** (integration) — nondecreasing or nonincreasing on D

## principle_law
- **induction** (foundations) — if S contains 1 and is successor-closed then S = N

## mathematical_identity
- **geometric_series** (series) — Sigma_{n>=0} r^n = 1/(1-r) for |r| < 1

## proposition
- **archimedean_property** (reals) — for every x in R there is n in N with n > x
- **density_of_rationals** (reals) — between any two reals lies a rational
- **limit_uniqueness** (sequences) — a convergent sequence has exactly one limit
- **convergent_implies_bounded** (sequences) — every convergent sequence is bounded
- **algebra_of_limits** (sequences) — limits commute with + - * and / (nonzero limit)
- **squeeze_theorem** (sequences) — a_n <= x_n <= b_n and a_n,b_n -> L imply x_n -> L
- **nth_term_test** (series) — if Sigma a_n converges then a_n -> 0
- **cauchy_criterion_series** (series) — Sigma a_n converges iff tails of partial sums are small
- **p_series** (series) — Sigma 1/n^p converges iff p > 1
- **closed_iff_seq_closed** (topology) — A is closed iff limits of convergent sequences in A stay in A
- **connected_iff_interval** (topology) — A subset of R is connected iff it is an interval
- **sequential_criterion_limit** (continuity) — lim_{x->c} f = L iff f(x_n) -> L for every x_n -> c with x_n != c
- **sequential_continuity** (continuity) — f continuous at c iff f(x_n) -> f(c) whenever x_n -> c
- **algebra_of_continuous_functions** (continuity) — sums products quotients of continuous functions are continuous
- **composition_of_continuous** (continuity) — the composite of continuous functions is continuous
- **differentiable_implies_continuous** (differentiation) — if f'(c) exists then f is continuous at c
- **differentiation_rules** (differentiation) — (f+g)'=f'+g' ; (fg)'=f'g+fg' ; (f/g)'=(f'g-fg')/g^2
- **interior_extremum_theorem** (differentiation) — if f has a local extremum at an interior point c and f'(c) exists then f'(c)=0
- **monotonicity_from_derivative** (differentiation) — f' >= 0 on an interval implies f is nondecreasing there
- **linearity_of_integral** (integration) — integral of af+bg = a int f + b int g
- **interval_additivity** (integration) — int_a^b = int_a^c + int_c^b
- **integral_monotonicity** (integration) — f <= g implies int f <= int g
- **integral_mvt** (integration) — int_a^b f = f(c)(b-a) for some c, f continuous
- **integration_by_parts** (integration) — int u v' = uv - int u' v

## theorem
- **nested_interval_theorem** (reals) — a decreasing sequence of nonempty closed bounded intervals has nonempty intersection
- **monotone_convergence_theorem** (sequences) — a bounded monotone real sequence converges to its sup or inf
- **bolzano_weierstrass** (sequences) — every bounded real sequence has a convergent subsequence
- **cauchy_convergence_criterion** (sequences) — a real sequence converges iff it is Cauchy
- **comparison_test** (series) — 0 <= a_n <= b_n and Sigma b_n converges imply Sigma a_n converges
- **abs_convergence_implies_convergence** (series) — if Sigma |a_n| converges then Sigma a_n converges
- **ratio_test** (series) — limsup |a_{n+1}/a_n| < 1 implies absolute convergence
- **root_test** (series) — limsup |a_n|^{1/n} < 1 implies absolute convergence
- **alternating_series_test** (series) — if b_n decreases to 0 then Sigma (-1)^n b_n converges
- **heine_borel** (topology) — a subset of R is compact iff it is closed and bounded
- **sequential_compactness** (topology) — K compact iff every sequence in K has a subsequence converging in K
- **continuous_image_of_compact** (continuity) — if f is continuous on compact K then f(K) is compact
- **extreme_value_theorem** (continuity) — a continuous function on [a,b] attains a maximum and a minimum
- **intermediate_value_theorem** (continuity) — a continuous function on [a,b] takes every value between f(a) and f(b)
- **heine_cantor** (continuity) — a continuous function on a compact set is uniformly continuous
- **continuous_image_of_connected** (continuity) — if f is continuous on connected D then f(D) is connected
- **chain_rule** (differentiation) — (f o g)'(c) = f'(g(c)) g'(c)
- **rolles_theorem** (differentiation) — f continuous on [a,b], differentiable on (a,b), f(a)=f(b) imply f'(c)=0 for some c
- **mean_value_theorem** (differentiation) — f'(c) = (f(b)-f(a))/(b-a) for some c in (a,b)
- **cauchy_mean_value_theorem** (differentiation) — (f(b)-f(a)) g'(c) = (g(b)-g(a)) f'(c) for some c
- **lhopital_rule** (differentiation) — lim f/g = lim f'/g' under the 0/0 or inf/inf hypotheses
- **taylor_theorem** (differentiation) — f(x) = sum_{k<n} f^{(k)}(a)(x-a)^k/k! + f^{(n)}(xi)(x-a)^n/n!
- **riemann_criterion** (integration) — f is integrable iff for every eps>0 some P has U(f,P) - L(f,P) < eps
- **continuous_implies_integrable** (integration) — a continuous function on [a,b] is Riemann integrable
- **monotone_implies_integrable** (integration) — a monotone function on [a,b] is Riemann integrable
- **ftc_part1** (integration) — F(x) = int_a^x f is differentiable with F' = f where f is continuous
- **ftc_part2** (integration) — int_a^b f = G(b) - G(a) for any antiderivative G of an integrable f
- **substitution_rule** (integration) — int_a^b f(g(x)) g'(x) dx = int_{g(a)}^{g(b)} f(u) du
- **uniform_cauchy_criterion** (function_sequences) — f_n converges uniformly iff it is uniformly Cauchy
- **weierstrass_m_test** (function_sequences) — |f_n| <= M_n and Sigma M_n converges imply Sigma f_n converges uniformly
- **uniform_limit_continuous** (function_sequences) — if f_n are continuous and f_n -> f uniformly then f is continuous
- **uniform_convergence_integral** (function_sequences) — if f_n -> f uniformly on [a,b] then int f_n -> int f
- **uniform_convergence_derivative** (function_sequences) — if f_n -> f pointwise and f_n' -> g uniformly then f' = g

