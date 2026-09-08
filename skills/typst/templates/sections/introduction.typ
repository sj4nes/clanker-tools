// Body markup only. No #set page, no #show: apply-base — the entrypoint did that.
#import "../preamble.typ": keyterm

= Introduction <intro>

#keyterm[Typst] is a markup-based typesetting system. This section is a separate
file spliced into the document by `#include` in `manuscript.typ`.

Prior work on reproducible document builds @knuth1984 motivates keeping
formatting out of the prose. As set out in @intro, this template keeps every
`#set` and `#show` rule in `preamble.typ`.

The model under study is $y = beta_0 + beta_1 x + epsilon$, estimated by least
squares:

$ hat(beta) = (X^T X)^(-1) X^T y $ <eq:ols>

Equation @eq:ols has a unique solution when $X^T X$ is invertible.
