# Gravity correction composition

A temporary composition of four independent source revisions passes the full Lean build, seven correction tests, three certificate checks and all 38 listed file hashes. Nothing was merged or pushed to main.

| Pull request | Frozen source head |
| --- | --- |
| [PR 10](https://github.com/Foundation-0/gravity/pull/10) | `57fece7db800233765eea32350f57f52d74362dc` |
| [PR 13](https://github.com/Foundation-0/gravity/pull/13) | `e5d7ee813e33de03c91857e48a2d55a0caf55506` |
| [PR 14](https://github.com/Foundation-0/gravity/pull/14) | `416255853a922d80654a1d6af6435a3f12974996` |
| [PR 15](https://github.com/Foundation-0/gravity/pull/15) | `0bf72bf773346fe34b8f4f7a71b1a31049932117` |

Base: `364fa3e9f740f42acaa1991428ce043f547e10dd`. The PR 13 revision is its reviewed source-correction commit, without subsequent review-record additions.

## Procedure and conflicts

Apply each base-to-source diff in the table order, retaining all source changes. The C-33 claim text overlaps: PR 13 describes the original false chirp bound and references the pending repair, while PR 10 corrects its power from `4^2` to `4^3`.

The composition keeps PR 13's physical qualifications and PR 10's corrected arithmetic bullet, with a sentence stating that the repair is included. This bounded documentary resolution was reviewed before application. No executable source conflict occurred.

The changelog insertions share an insertion point. Both entries are retained. Root checksum edits overlap across branches: preserve the union of their listed paths, then recompute every listed SHA-256 from the composed files. This yields 38 entries, including PR 13's correction test and explanation. The original branch manifests and provenance remain records of their own snapshots.

The Wave 11/12 generators and correction test match PR 13 byte for byte. Wave 12 Lean matches PR 10, Wave 5/6/7 Lean matches PR 14, and the repaired Wave 4 certificate matches PR 15. No scientific calculation was edited during composition.

## Validation

- `lake build`: passes, 15 jobs, using Lean 4.35.0. The existing Wave 10 unused `hPos` warning remains.
- `python3 -m unittest -v test_wave11_12_corrections.py`: all seven controls pass.
- Wave 11, Wave 12 and Wave 4 generators with `--check`: all pass byte-identical certificate checks.
- `shasum -a 256 -c SHA256SUMS`: all 38 entries pass after recomputation.
- `git diff --check`: passes.

The long Wave 7 generator was not repeated. Its source and certificate are unchanged, and its earlier byte-identical check passed in the PR 15 snapshot.

`results.json` records the source map and outcomes. `SHA256SUMS.composed` preserves the recomputed file inventory. These hashes describe this temporary composition and must be recomputed after later changes.

## Exact replay

Create a fresh isolated checkout at `e5d7ee813e33de03c91857e48a2d55a0caf55506`. From that checkout, apply the bundled patch using its absolute path:

```sh
git apply /path/to/gravity-composition.patch
lake build
python3 -m unittest -v test_wave11_12_corrections.py
python3 wave11_machian_pairing_unification.py --check
python3 wave12_cosmic_dawn_quasar_collapse.py --check
python3 wave4_unified_field_solver.py --check
shasum -a 256 -c SHA256SUMS
git diff --check
```

The patch freezes the approved documentary resolution, source corrections and recomputed manifest. It contains no build or cache artifacts. Its SHA-256 is recorded in `results.json`.

## Limits

This is a local integration check, not a merged-main result or hosted CI result. Lean establishes the encoded arithmetic statements. Generator agreement and numerical controls do not establish the physical models, seed formation, merger hardening or a gravitational-wave population prediction. The existing scientific review boundaries remain in force.

The patch preserves unified-diff context markers on blank lines. Those markers are patch syntax. Whitespace checks pass on the applied source.
