# Bibliography — Release 0.1

| Key | Reference |
|---|---|
| `Cal` | H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, 2nd ed., Wiley, 1985. |
| `Fermi` | E. Fermi, *Thermodynamics*, Dover, 1956 (reprint of the 1937 lectures). |
| `Zemansky` | M. W. Zemansky & R. H. Dittman, *Heat and Thermodynamics*, 7th ed., McGraw-Hill, 1997. |
| `SI` | BIPM, *The International System of Units (SI Brochure)*, 9th ed., 2019. |

## Convention notes

- **Callen** uses `dU = δQ − δW` with `δW = P dV` — the convention of this
  capsule. Callen's fundamental-relation-first development is the basis for the
  `fundamental_relation_u` / potentials / Maxwell nodes.
- **Fermi** uses the same sign convention and is the source for the first/second
  law statements, the Carnot analysis, and the ideal-gas results.
- **Zemansky** is the source for the empirical / measurement-oriented framing of
  temperature, heat capacity, and the `T dS` equations.
- Any result quoted from a text using `dU = δQ + δW` (work done *on* the system)
  has been rewritten to this capsule's convention; the node's source note flags
  it where relevant.
