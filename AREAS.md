# Where Foundation0 can make progress in physics

A survey made on 18 October 2026, when physics0 was empty. Foundation0's research so far (the incentre lattice,
integer multiplication, GF(2) circuits, exact Fourier transforms) has been mathematics. Its most useful habit is
the same everywhere: pick a question whose answer a machine can check, let AI agents do the search and the
careful code, and publish the certificate alongside the claim. The areas below were chosen for that fit.

Each entry gives the open question, why it suits people working with AI agents, how a result would be checked,
and a first step.

## 1. Maxwell's point-charge problem (started: [`maxwell/`](maxwell/))

**Open question.** How many equilibria can $n$ positive point charges have? Maxwell's bound $(n-1)^2$ was
disproved in July 2026 for five charges, and is open for three (bound between 4 and 6) and four charges.

**Fit.** A small parameter space, a fast forward problem, and AI-suggested constructions already proved
decisive (the counterexample's idea came from an OpenAI model).

**Checking.** Interval arithmetic and Krawczyk tests give exact counts, with two independent verifiers.

**Done so far.** Certified exact counts: four charges reach 9, an explicit five-charge counterexample with
exactly 24, and six charges with 29 > 25.

**Next.** Decide $n=4$. A computer-assisted proof for three charges through the inverse-map reformulation.
Constructions that grow faster than linearly in $n$.

## 2. Computer-assisted proofs in celestial mechanics

**Open questions.**
- The complete list of planar central configurations of 8 equal masses: rigidly rotating solutions of the
  N-body problem, Smale's sixth problem in the equal-mass case. It is proved only up to $n=7$ (Moczurad
  and Zgliczyński, Celest. Mech. Dyn. Astr. 131:46, 2019; arXiv:1812.07279), and up to $n=6$ in space
  (arXiv:2006.06768).
- Existence proofs for the thousands of periodic three-body orbits found numerically since Šuvakov and
  Dmitrašinović (PRL 2013), including the Li–Liao catalogues. Only a few have proofs (Kapela and Simó,
  Nonlinearity 2007, among them).

**Fit.** The same machinery as the Maxwell study: interval Newton/Krawczyk, exhaustive subdivision, and
symmetry reduction. These are engineering-heavy proofs where agents save months.

**Checking.** Rigorous enclosures, replayable by an independent verifier.

**First step.** Reproduce the $n=5$ planar list with our certifier, then measure what $n=8$ costs.

## 3. Physics in Lean

**Open question.** Most of physics has no machine-checked statements. PhysLean (formerly HepLean) has begun
on particle physics and electromagnetism.

**Fit.** Foundation0 already values Lean (its exact Fourier transform record is Lean-verified), and AI agents
now formalise at scale.

**Checking.** The Lean kernel.

**First step.** State the Maxwell problem and the certified counts in Lean. A formalisation request is open
as google-deepmind/formal-conjectures issue 4682.

## 4. Quantum-information records with exact certificates

**Open questions.** Gaps in Grassl's tables of best known quantum error-correcting codes
([codetables.de](https://codetables.de)). The value of the Grothendieck constant $K_G(3)$, which bounds
quantum correlations: recent bounds come from Frank–Wolfe searches by Designolle and co-authors. Maximal
quantum violations of small Bell inequalities.

**Fit.** Combinatorial search plus exact verification, the pattern of the GF(2) circuit work.

**Checking.** A code's minimum distance can be checked exactly; a Bell or Grothendieck bound comes with a
rational certificate.

**First step.** Pick the smallest open entries in the qubit stabilizer table and run a quasi-cyclic search
with exact distance checks.

## 5. Statistical physics on the incentre lattice

**Open question.** Founding member Ahraz Arifuddin's incentre lattice includes the boron network of CaB₆. Its
percolation thresholds, Ising critical temperature and lattice sums (Madelung constants) do not seem to
have been computed.

**Fit.** Quick, open and tied to existing Foundation0 work. The significance is modest.

**Checking.** Exact lattice sums to many digits; Monte Carlo thresholds with error bars and released seeds.

**First step.** Madelung constant and bond and site percolation thresholds of the CaB₆ boron net.

## 6. Searches in open astronomical data

**Open question.** Signals the official pipelines missed, as in eumemic's TESS exoplanet search: eclipsing
binaries and single transits in full-frame images, or sub-threshold events in gravitational-wave open data.

**Fit.** Proven in Foundation0 already. It needs storage and compute beyond a single session.

**Checking.** Released candidate lists, vetting statistics, and follow-up by observers.

**First step.** Ask eumemic which by-products of the TESS search (for example eclipsing-binary
false positives) would be worth a catalogue.

## 7. Independent checks of AI-made physics claims

**Open question.** Several 2026 AI physics results are preprints or announcements only, as the Ledger shows: a
claimed nine-loop six-gluon amplitude (25 September 2026), and single-minus gluon and graviton amplitudes.

**Fit.** Reproduction is exactly the kind of checking Foundation0 records. A failed check is as useful as a
passed one.

**Checking.** Numerical evaluation against the published formulas, or symbolic re-derivation.

**First step.** List which of these come with code or data that can be rerun.

---

**Ranking.** Area 1 has a live frontier and results already. Area 2 reuses the same tools on a better-known
problem. Area 3 is the most durable. Areas 4 and 5 are quick wins. Areas 6 and 7 need partners or data
access more than new ideas.
