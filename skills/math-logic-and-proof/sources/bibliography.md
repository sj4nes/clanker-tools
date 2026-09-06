# Bibliography — Release 0.1

| key | reference |
|---|---|
| `enderton_logic_2e` | H. B. Enderton, *A Mathematical Introduction to Logic*, 2nd ed., Academic Press, 2001. |
| `vandalen_5e` | D. van Dalen, *Logic and Structure*, 5th ed., Springer, 2013. |
| `chiswell_hodges` | I. Chiswell & W. Hodges, *Mathematical Logic*, Oxford, 2007. |
| `mendelson_6e` | E. Mendelson, *Introduction to Mathematical Logic*, 6th ed., CRC Press, 2015. |
| `shoenfield` | J. R. Shoenfield, *Mathematical Logic*, A K Peters, 1967 (reprint 2001). |
| `velleman_3e` | D. J. Velleman, *How to Prove It*, 3rd ed., Cambridge, 2019. |
| `hammack_bop` | R. Hammack, *Book of Proof*, 3rd ed., 2018 (open access). |
| `bbj_5e` | G. Boolos, J. Burgess & R. Jeffrey, *Computability and Logic*, 5th ed., Cambridge, 2007. |
| `smith_godel_2e` | P. Smith, *An Introduction to Gödel's Theorems*, 2nd ed., Cambridge, 2013. |
| `smullyan_fol` | R. Smullyan, *First-Order Logic*, Springer, 1968 (Dover reprint 1995). |
| `mathlib_firstorder` | mathlib4, `Mathlib.ModelTheory.*` (`FirstOrder.Language`, satisfaction, the completeness development). Consulted for the Lean formalisation. |
| `hodges_shorter` | W. Hodges, *A Shorter Model Theory*, Cambridge, 1997. (Cited for canonical models, LS, non-categoricity — model theory proper is out of scope but referenced.) |
| `jech_set_theory` | T. Jech, *Set Theory*, 3rd millennium ed., Springer, 2003. (Cited for BPIT vs AC in `lindenbaum_lemma_fol`.) |
| `kunen_set_theory` | K. Kunen, *Set Theory: An Introduction to Independence Proofs*, North-Holland, 1980. (Cited for absoluteness in `skolem_paradox`.) |
| `halmos_boolean` | P. Halmos & S. Givant, *Introduction to Boolean Algebras*, Springer, 2009 (orig. Halmos, *Lectures on Boolean Algebras*, 1963). (Cited for the Lindenbaum–Tarski algebra in the `prop_laws` pages.) |
| `sep_pl` | *Stanford Encyclopedia of Philosophy*: "Classical Logic", "Automated Reasoning", "Gödel's Incompleteness Theorems". Orientation only, not cited for a statement. |

## Per-area primary source

| area | primary | secondary |
|---|---|---|
| propositional syntax / semantics | `vandalen_5e` ch. 1 | `enderton_logic_2e` §1 |
| normal forms, functional completeness | `enderton_logic_2e` §1.5 | `chiswell_hodges` ch. 3 |
| natural deduction | `vandalen_5e` ch. 2 | `chiswell_hodges` ch. 4 |
| Hilbert system, deduction theorem | `mendelson_6e` ch. 1 | `enderton_logic_2e` §2.4 |
| propositional completeness (Post) | `enderton_logic_2e` §1.7 | `vandalen_5e` §1.5 |
| first-order syntax, substitution, free-for | `enderton_logic_2e` §2.1–2.2 | `vandalen_5e` ch. 3 |
| Tarski satisfaction, structures | `enderton_logic_2e` §2.2 | `chiswell_hodges` ch. 5 |
| quantifier laws, prenex form | `vandalen_5e` §3.1 | `mendelson_6e` §2.7 |
| soundness, Henkin, Gödel completeness | `enderton_logic_2e` §2.5 | `vandalen_5e` §3.1–3.2, `mathlib_firstorder` |
| compactness, Löwenheim–Skolem | `enderton_logic_2e` §2.6 | `chiswell_hodges` ch. 6 |
| proof methods, induction | `velleman_3e` | `hammack_bop` |
| boundary nodes (incompleteness, undecidability) | `smith_godel_2e` | `bbj_5e` |
