# Type vocabulary — math-linear-algebra Release 0.1

What kind of thing each object in the capsule IS. Every result's
`type_check_status` is an assertion that its statement is well-formed in this
vocabulary; `validation/type-checks.md` records the per-node check.

## The ladder of structures

    set
     |  + two operations, invertibility of nonzero elements
    field  F
     |  + an abelian group acted on by F
    vector space  V
     |  + a positive-definite conjugate-symmetric form
    inner product space  (V, <.,.>)

Each level adds structure and therefore **loses generality**. The capsule's
`field_scope` tag records exactly where each result sits on this ladder:
`any_field` results survive at the top, `real_or_complex` results need the
bottom rung.

## Object kinds and where they live

| kind | inhabits | examples |
|---|---|---|
| scalar | `F` | `a`, `det A`, `tr A`, `lambda`, `<u,v>` |
| vector | `V` | `v`, `e_i`, an eigenvector |
| subspace | the lattice of subspaces of `V` | `ker T`, `col(A)`, `E_lambda`, `U^perp` |
| coset | `V/U` | `v + U` |
| functional | `V^*` | `b_i^*`, an element of `U^0` |
| linear map | `L(V,W)` | `T`, `P_U`, `T^*` |
| operator | `L(V)` — an **algebra** | `T`, `I`, `N` nilpotent, `p(T)` |
| matrix | `F^{m x n}` — a vector space | `A`, `Q`, `L`, `Sigma` |
| square matrix | `F^{n x n}` — an algebra | the only shape with `det`, `tr`, eigenvalues |
| polynomial | `F[t]` — a PID | `p_A`, `m_T` |
| permutation | `S_n` — a group | `sigma`, with `sgn(sigma)` |
| natural number | `N` | `dim V`, `rank A`, multiplicities |
| nonnegative real | `R_{>=0}` | `\|\|v\|\|`, `sigma_i`, `rho(A)`, `kappa(A)` |
| equivalence relation | on matrices | `~_r`, `~`, `~_c` |

## The shape discipline

Most type failures in linear algebra are **shape** failures, and they are
mechanical to check:

- `A + B` requires equal shapes; `AB` requires the inner shapes to agree.
- `det A`, `tr A`, `p_A`, eigenvalues, `A^k`, similarity: **square only**.
  Rectangular analogues exist but are different objects — `singular_values`,
  not eigenvalues; `moore_penrose_pseudoinverse`, not the inverse.
- `x^T A x` requires `x` a column of length `n` and `A` in `F^{n x n}`.
- `[S o T] = [S][T]` requires the **middle basis to be the same** on both
  factors — a shape condition on bases, not on integers, and the one most often
  violated silently (`matrix_mult_is_composition`).

## The four type checks that are not shape checks

Four nodes carry a type check whose content is genuine mathematics, not
bookkeeping. Each is a **well-definedness** obligation:

1. **`quotient_space`** — the operations are defined on representatives;
   independence of representative uses *both* closure properties of `U`, one
   per operation.
2. **`first_isomorphism_theorem`** — `v + ker T -> T(v)` is well-defined
   exactly because the fibres of `T` are cosets of `ker T`.
3. **`orthogonal_projection`** — the formula names an orthonormal basis of `U`;
   independence of that choice is established by the basis-free
   characterisation.
4. **`permutation_sign`** — a permutation has many decompositions into
   transpositions; `sgn` is a function only because their parities agree.

A fifth, **`determinant`**, is a *definite-description* obligation rather than
a well-definedness one: "the unique normalised alternating form" presupposes
`determinant_existence_uniqueness`, which is why that theorem precedes it in
the graph.

## Overloadings the capsule tolerates, and how they are resolved

| symbol | readings | resolution |
|---|---|---|
| `0` | zero scalar, vector, matrix, subspace `{0}` | by position; each node's `symbols` block types it |
| `+` | addition in `F`, in `V`, of subspaces, of matrices | by the types of its arguments |
| `*` (as `^*`) | conjugate transpose `A^*`; adjoint `T^*`; dual space `V^*` | by what it decorates: matrix, map, or space |
| `adjoint` | the adjugate `adj(A)`; the Hermitian adjoint `A^*` | the capsule always writes `adj` for the classical adjoint |
| `>=` on matrices | Loewner (PSD) ordering only — never entrywise | stated in `notation.md`; entrywise comparison is never used |
| `perp` vs `0` | orthogonal complement in `V`; annihilator in `V^*` | different nodes, different ambient spaces |

## What this capsule does NOT type

- **Topology.** No convergence, continuity, or closure of a subspace, except
  where `compactness_cited` and `extreme_value_cited` are imported for one
  proof step. "Closed subspace" appears only inside counterexamples pointing at
  the infinite-dimensional boundary.
- **Measure.** `determinant_volume` cites a notion of volume rather than
  constructing one.
- **Modules.** Everything is over a field; `smith_normal_form_boundary` is the
  single node that names the module-theoretic generalisation, and it is
  `draft`.
