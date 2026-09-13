# inner_product

## Type
structure

## Statement
An inner product on a vector space V over F in {R, C} is a map <.,.>: V x V -> F that is linear in the FIRST slot, conjugate-symmetric (<y,x> = conj(<x,y>)), and POSITIVE DEFINITE (<x,x> > 0 for x != 0).

## Symbols
- `<x,y>` — type: element of F
- `F` — restricted to R or C

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
complex_number, inner_product_convention, real_number, vector_space

## Hypotheses
F = R or C, positive definiteness
## Type / well-formedness check
Well-formed. Conjugate-symmetry forces <x,x> = conj(<x,x>), i.e. REAL, without which 'positive' would be meaningless -- so the two axioms are linked, not independent. Over R conjugation is trivial and the form is symmetric bilinear.

## Specialization / boundary cases
- F^n with <x,y> = sum_i x_i conj(y_i) = y^* x: the standard inner product
- weighted: <x,y> = y^* W x for a positive definite W (positive_definite) -- every inner product on F^n is of this form
- continuous functions on [0,1] with <f,g> = integral f conj(g): infinite-dimensional, and the setting of Fourier series

## Hypothesis-dropped counterexamples
- **positive_definiteness**: the Minkowski form <x,y> = x_1y_1 - x_2y_2 on R^2 is symmetric and bilinear but indefinite: the null vector (1,1) has <x,x> = 0 without being 0. There is then no norm, no Cauchy-Schwarz in the usual direction, and no orthogonal decomposition -- Lorentzian geometry, not Euclidean
- **conjugate_symmetry**: the plain bilinear form sum x_i y_i on C^2 gives <(1,i),(1,i)> = 1 - 1 = 0 with the vector nonzero (see inner_product_convention)
- **the_field**: over F_2, x^T x = sum x_i^2 = sum x_i, so (1,1) is 'self-orthogonal'. No ordered field, no positivity, no inner product

## Common misuse
- calling a symmetric bilinear form an inner product without checking definiteness
- using the physicist's (second-slot-linear) convention alongside this one

## In the wild
- the L^2 inner product underlies Fourier analysis, least squares, and the Hilbert-space formulation of quantum mechanics
- the covariance inner product <X,Y> = E[XY] makes uncorrelated random variables orthogonal, which is why regression is projection

## Related nodes (non-prerequisite)
- required_by: induced_norm, cauchy_schwarz, orthogonality

## Sources
axler_lada_4e, hoffman_kunze_2e
