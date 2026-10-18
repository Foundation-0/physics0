# Where Foundation0 can make progress in physics

A survey made on 18 October 2026, when physics0 was empty. Areas that become projects get their own repository,
listed in the [README](README.md). Foundation0's research so far (the incentre lattice,
integer multiplication, GF(2) circuits, exact Fourier transforms) has been mathematics. Its most useful habit is
the same everywhere: pick a question whose answer a machine can check, let AI agents do the search and the
careful code, and publish the certificate alongside the claim. The areas below were chosen for that fit.

Each entry gives the open question, why it suits people working with AI agents, how a result would be checked,
and a first step.

## 1. Maxwell's point-charge problem (started: [Foundation-0/point-charges](https://github.com/Foundation-0/point-charges))

**Open question.** How many equilibria can $n$ positive point charges have? Maxwell's bound $(n-1)^2$ was
disproved in July 2026 for five charges, and is open for three (bound between 4 and 6) and four charges.

**Fit.** A small parameter space, a fast forward problem, and AI-suggested constructions already proved
decisive (the counterexample's idea came from an OpenAI model).

**Checking.** Interval arithmetic and Krawczyk tests give exact counts, with two independent verifiers.

**Done so far.** Certified exact counts: four charges reach 9, an explicit five-charge counterexample with
exactly 24, and six charges with 29 > 25.

**Next.** Decide $n=4$. A computer-assisted proof for three charges through the inverse-map reformulation.
Constructions that grow faster than linearly in $n$. These are tracked as issues in point-charges.

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

**First step.** Reproduce the $n=5$ planar list with the point-charges certifier, then measure what $n=8$ costs.

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

## 6. Searches in open astronomical data (moved to [astr0](https://github.com/Foundation-0/astr0))

Astronomy now has its own hub, [Foundation-0/astr0](https://github.com/Foundation-0/astr0). Its survey
([AREAS.md](https://github.com/Foundation-0/astr0/blob/claude/sleepy-pasteur-k5knht/AREAS.md)) covers this area, including the question of
which by-products of eumemic's TESS search deserve a catalogue. Its first project,
[plate-eclipses](https://github.com/Foundation-0/plate-eclipses), uses a century of Harvard plates to recover past
eclipses of rare eclipsing stars. Sub-threshold events in gravitational-wave open data are crowded: independent
pipelines from IAS and AresGW already exist.

## 7. Independent checks of AI-made physics claims

**Open question.** Several 2026 AI physics results are preprints or announcements only, as the Ledger shows: a
claimed nine-loop six-gluon amplitude (25 September 2026), and single-minus gluon and graviton amplitudes.

**Fit.** Reproduction is exactly the kind of checking Foundation0 records. A failed check is as useful as a
passed one.

**Checking.** Numerical evaluation against the published formulas, or symbolic re-derivation.

**First step.** List which of these come with code or data that can be rerun.

## 8. Archived temporary seismic networks: local earthquake catalogues nobody made

*Areas 8–10 come from Foundation0's [deep-fields scouting](https://github.com/Foundation-0/f0/tree/claude/sleepy-pasteur-k5knht/deep-fields)
of 18 October 2026.*

**Open question.** Hundreds of temporary seismic deployments were run to image the Earth's interior, not to
catalogue the small earthquakes they recorded. What do their waveforms show about local faults, swarms and tremor,
especially in sparsely monitored regions?

**Fit.**
- [data/seismic-networks/](data/seismic-networks/) lists 752 networks at EarthScope that meet four tests: a temporary
  code, no active-source keywords, at least 10 stations, and at least 360 days of operation.
- The waveforms are open.
- Machine-learning phase pickers ([SeisBench](https://github.com/seisbench/seisbench), PhaseNet) make a catalogue a
  pipeline job rather than a PhD.

**Checking.** Anyone can re-run the open code on the open waveforms. Compare with the ISC Bulletin, which takes
contributions from temporary networks. Publish in Seismica, SRL or GJI.

**First step.**
- Check prior work for three candidates in sparse regions. The first network the scout spot-checked (Cameroon, XB)
  had already been reprocessed with deep learning in 2024.
- Then run one month through phase picking, association and location, and compare with the ISC Bulletin.

## 9. Climate data rescue: foreign weather bulletins scanned and never transcribed

**Open question.** NOAA's Central Library holds scans of national weather bulletins from around the world, such as
Argentina's *Resumen Mensual del Tiempo* for 1942. How many of their station-years are missing from the archives
behind 20th-century reanalyses?

**Fit.**
- 5,424 PDFs (192.9 GB) sit in a public S3 bucket ([data/noaa-climate-rescue/](data/noaa-climate-rescue/)).
- Vision-language models can now read typed tables. AI transcription so far has focused mainly on UK records
  ([Hawkins and Brohan](https://climatelabbook.substack.com/p/data-rescue-with-ai)).

**Checking.**
- Two models transcribe independently, and the disagreements are listed.
- Check physical consistency, and compare with the 20CRv3 reanalysis.
- The data can go to the International Surface Pressure Databank ([ISPD](https://psl.noaa.gov/data/20CRv3_ISPD_obscounts/)),
  ICOADS ([RECLAIM](https://www.icoads.noaa.gov/reclaim)) or [Copernicus data rescue](https://datarescue.climate.copernicus.eu/aiml-and-data-rescue).

**First step.**
- Map the opaque PDF names to country, title and years.
- Check those stations and years against ISPD.
- Transcribe one volume missing from ISPD.

**Caveat.** Little headline value, but a high chance of producing something people use.

## 10. Lanthanide atomic spectra: energy levels for kilonova models

**Open question.** Models of kilonova light need atomic data for lanthanide ions that does not exist yet. Analysing
one ion's spectrum has taken a PhD student two to three years.

**Fit.**
- The Kitt Peak spectrometer archive at NSO, which includes laboratory lamps, is downloadable
  ([README](https://nispdata.nso.edu/ftp/FTS_cdrom/README)).
- A new level is supported or refuted by plain arithmetic: the Ritz combination principle.
- Imperial College is starting with machine learning ([2509.16184](https://arxiv.org/abs/2509.16184)).

**Checking.** A new level must explain several observed lines, and beat a Monte Carlo test of chance coincidences.
The NIST atomic spectra database and journals such as ApJS and JQSRT accept such results.

**First step.** Find an expert partner before anything else. The data are hard to work with.

## Crowded (do not start here)

- **CMS open data.** The collaboration runs its own anomaly searches, and agent-run analyses already exist
  ([2603.20179](https://arxiv.org/abs/2603.20179)).
- **LIGO public data.** Independent pipelines exist already.
- **Materials databases such as GNoME.** Whether their compounds are new is disputed, and confirming one needs a lab.

---

**Ranking.** Area 1 has a live frontier and results already. Area 2 reuses the same tools on a better-known
problem. Area 3 is the most durable. Areas 4 and 5 are quick wins. Area 7 needs partners or data access more than
new ideas; area 6 has moved to astr0.
- **Area 8** needs storage (a 14-month, 32-station network is about 150 GB) but little else.
- **Area 9** is a high-probability, low-glamour data contribution.
- **Area 10** needs an expert partner.
