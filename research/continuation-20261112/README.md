# What the continued tests establish

The continued search has produced a constrained field-response calculation, a mechanical response law with an exact instability proof, an observational calibration diagnostic and a correction to the Witness Map. Each can be reused independently. None establishes a common fundamental mechanism for gravity, matter creation, fractal structure and quantum records.

These are public draft changes with internal agent review. The research and independent scientific reviews used separate gpt-6-astra agents at ultra reasoning. Publication and specified implementation work used gpt-6.1-sol. External scientific review has not occurred.

## Results available to build on

| Thread | Concrete result | Canonical work |
|---|---|---|
| AeST field response | Allowed states can share initial density, momentum and metric while different field data change later pressure and gravitational potentials. A separate ADM implementation reproduces the constraints and evolution. A declared slow-subspace test still gives 24.6–27.4% zero-pressure baseline errors, independently reproduced with the original field equations. | [AeST response](https://github.com/Foundation-0/gravity/pull/12) |
| Fixed angular mechanics | Peak internal displacement per unit strain scales as 0.404226/sqrt(kappa) near the open fold. An alternating rotation proves endpoint instability for every kappa > 0 under the prescribed holding loads. | [Fixed-angle mechanics](https://github.com/Foundation-0/incentre-lattices/pull/100) |
| Galaxy acceleration diagnostic | The KMOS peak-speed proxy falls by 0.167484 dex between the selected low and high redshift groups. Gas estimates account algebraically for 0.163843 dex of that change. | [KMOS diagnostic](https://github.com/Foundation-0/astr0/pull/7) |
| Cosmic-dawn corrections | Direct radial integration replaces an invalid shortcut. Composition and radiative efficiency change light-seed growth clocks. The assigned trapping fraction and nonlinear halo mass do not establish black-hole capture or a seed mass. | [Wave 11/12 corrections](https://github.com/Foundation-0/gravity/pull/13) |
| Decoherence and records | The Witness Map computes a decoherence timescale. Its inputs do not determine readable or redundant environmental records. The page and documentation now distinguish these quantities. | [Witness Map correction](https://github.com/Foundation-0/fractals/pull/54) |

The earlier [value assessment](https://github.com/Foundation-0/gravity/pull/11) supplies the source audit, rejected interpretations and first mathematical gates. The current results execute its justified next tests. Their canonical repositories contain code, provenance, numerical outputs and independent checks.

## A useful connection between the threads

Each calculation asks which details a compressed description must retain to predict the question being asked. The answer is concrete and different in each case.

In AeST, density and bulk momentum omit allowed scalar/vector initial data. The same initial retained quantities can therefore lead to different later metric responses. The four-state linear system resolves this ambiguity for the specified action and background. Its success does not establish a thermal pressure law or a nonlinear halo solution.

In the lattice, internal relaxation produces the large strain response. Stored angular stress changes spatial stability. A test of uniform strain alone misses an unstable displacement that alternates between neighbouring cells. The explicit negative variation establishes the failure without requiring an exhaustive wavevector scan.

In the galaxy catalogue, peak velocity and tabulated baryonic mass do not uniquely determine the physical acceleration scale. A change in the proposed redshift exponent can be absorbed exactly by an unconstrained velocity calibration. Here the missing information concerns inference from observations, rather than an omitted dynamical state.

In the Witness Map, suppressed interference and information accessible to observers are different observables. Temperature and dilution alone do not specify the environmental photon state needed for a record calculation. The correction applies an established distinction from quantum Darwinism.

This comparison supplies a practical research method: declare the retained variables, construct alternatives that agree on them, and test whether the requested prediction changes. A successful counterexample identifies the extra state, calibration or observable that the model needs. It does not by itself identify a universal law shared by those systems.

## What the galaxy result can test

For the conditional relation Vflat^4 = G Mtrue A E(z)^q, the catalogue proxy obeys

```text
y = log10[Vpeak^4/(G Mtab)]
  = log10 A + q log10 E + 4 log10(Vpeak/Vflat) - log10(Mtab/Mtrue).
```

Between the low and high groups, q=1 predicts a rise of 0.310524 dex. The observed proxy instead falls, leaving a -0.478008 dex contrast. If only one calibration changes, matching it requires a high-to-low peak/flat velocity ratio of 0.759448, or a catalogue/true mass ratio of 3.006134.

Those are conditional requirements, not estimated probabilities for calibration errors. The table lacks individual joint errors, asymptotic velocities and a survey-selection model. Further fitting to the same point values cannot identify q without additional information. The existing gas scaling relation must not be treated as an independent gas measurement.

## Evidence needed to reopen each lane

| Lane | Current boundary | Evidence that would justify continuation |
|---|---|---|
| AeST | The linear response, slow-subspace test and both independent reviews are complete for the specified action and background. | A physical cosmology, justified initial spectrum or invariant slow-state prescription. Further parameter scans would add assumptions without answering the original fixed-model question. |
| Mechanics | The fixed ideal-model question has a quantitative answer and an exact endpoint counterexample. | A concrete hinge, boundary loading and fabrication tolerances for a realizable specimen. More arbitrary spring variants do not resolve those requirements. |
| Observations | The available point-table diagnostic and independent review are complete. | Independent velocity/gas calibrations, correlated uncertainties and selection, or resolved profiles for a radial-acceleration analysis. |
| Witness Map | The interpretation correction is implemented and separately reviewed. | A specified environmental state and accessible photon fragments if a redundancy calculation is desired. |
| Cosmic-dawn and origin claims | The numerical and interpretation corrections are public and independently checked. Conditional growth clocks do not exclude every light-seed history. | A physical capture/seed solution or comparative observational likelihood, beyond the assigned trapping fraction and total-halo mass. |

The fifth-dimension picture and universe-collision creation analogy still lack a specified dynamics with an observable difference from existing descriptions. [Pair production](https://doi.org/10.1103/PhysRevLett.127.052302) already supplies an inverse to particle annihilation in known physics. These ideas do not become evidence for a new origin mechanism merely by resembling a result in another thread.

The stopping criterion is that the currently specified, informative tests have been executed or require a named new input. It is not a claim that all worthwhile physics research has been exhausted.

## Reproducibility and handoff

The gravity corrections have separate scopes. [Chirp-mass repair](https://github.com/Foundation-0/gravity/pull/10) repairs a false chirp-mass bound. [Lean build repair](https://github.com/Foundation-0/gravity/pull/14) repairs duplicated Lean declarations. Together they pass the full local Lean build. The proofs establish their stated mathematical propositions, not the physical hypotheses attached to them.

[Checksum repair](https://github.com/Foundation-0/gravity/pull/15) fixes a certificate metadata key and refreshes the byte manifest. At the earlier repair snapshot, all 36 entries and eleven generator/verifier checks passed. The current-main refresh repeats all 36 byte checks and Wave 4 regeneration, with the same 29 source and certificate files.

Hashes must be recomputed when other PRs alter the listed files. Byte identity, numerical agreement, proof compilation and scientific validity are separate claims.

The [earlier integration record and replay patch](gravity-composition/COMPOSITION.md) combine the four source repairs. That local composition passes the full Lean build, seven correction controls, three certificate checks and all 38 composed file hashes. It records the documentary overlap and exact source revisions.

The initial continuation refreshed all five main branches. A subsequent [gravity update review](gravity-update-d144448.md) covers four new documentation and manifest commits through d144448. It changes no physical calculation or observational input. The linked work remains public in open drafts. No merge to main or site deployment has occurred.

The [current-main integration bundle](gravity-composition-d144448/COMPOSITION.md) composes the four repairs on gravity d144448. Its fresh local checks pass 15 Lean build jobs, seven controls, three certificate checks and 39 hashes. All 32 source-file comparisons and the 53-file patch replay match. The earlier bundle remains historical. These are local integration results, distinct from hosted CI and merged main.
