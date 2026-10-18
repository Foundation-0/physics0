# physics0

The hub for Foundation0's physics work: in the open, with every claim backed by something a machine can check,
and credited to the people and the AI models that did the work.

This repository directs the effort. It keeps the list of projects, the survey of where to go next, and the
shared rules for checking results. A research project small enough to be a single note can start here; once
it grows beyond that (code, certificates, verifiers, data), it gets its own repository and is listed below.

## Projects

| project | question | status |
|---|---|---|
| [point-charges](https://github.com/Foundation-0/point-charges) | How many equilibria can $n$ point charges have? (Maxwell, 1873) | Certified exact counts: 4 charges reach Maxwell's bound of 9; an explicit 5-charge counterexample has exactly 24; 6 charges have 29, above the bound of 25. Evidence for the open 3- and 4-charge cases. Reviewed by an independent AI agent (point-charges PR #1); not yet reviewed by a person. |

## Where next

[AREAS.md](AREAS.md) surveys open physics questions where people working with AI agents can make checkable
progress: celestial mechanics proofs, physics in Lean, quantum-information records, the incentre lattice, open
astronomical data (now in [astr0](https://github.com/Foundation-0/astr0)), independent checks of AI-made physics
claims, archived seismic networks, climate data rescue and lanthanide atomic spectra. The roadmap issue tracks which of them
become projects.

## How results are checked in every project

- **Certificates, not screenshots.** A numerical claim comes with a file a short verifier can re-check, and
  where possible with two verifiers that share no code.
- **Negative controls.** Verifiers are tested on corrupted certificates and must reject them.
- **Plain status labels.** Each project says what is proved, what is computed, what is only evidence, and who
  has (or has not) reviewed it.
- **Credit.** Prior work is cited where it is used. Each project records which AI model did what.

## Licence

Copyright 2026 Foundation0 contributors.

Code (`*.py`): [Apache License 2.0](LICENSE).
Text and data (this README, `AREAS.md` and `data/`):
[Creative Commons Attribution 4.0 International](LICENSE-CC-BY-4.0) (CC BY 4.0).
Project repositories carry the same pair of licences unless they say otherwise.
