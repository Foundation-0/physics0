# Gravity correction composition on current main

A temporary composition on main at `d1444481cdefc59a275ede2fef740ea2cf48eeec` passes the full Lean build, seven correction tests, three certificate checks and all 39 listed file hashes. Nothing was merged or pushed to main. The earlier composition bundle remains a historical record.

| Pull request | Frozen source head |
| --- | --- |
| [PR 10](https://github.com/Foundation-0/gravity/pull/10) | `57fece7db800233765eea32350f57f52d74362dc` |
| [PR 13](https://github.com/Foundation-0/gravity/pull/13) | `cce0284d03efb5c5c6ce8a70014ea436d7a3a801` |
| [PR 14](https://github.com/Foundation-0/gravity/pull/14) | `b473fc9c30378862cd66d5d69b555842144febed` |
| [PR 15](https://github.com/Foundation-0/gravity/pull/15) | `ca55815cd2ca6f43356cc7ad5a7148fa83cec030` |

## Construction and checks

Start with the complete PR 13 tree, which incorporates current main and its review records. Take the Wave 12 Lean repair from PR 10, the three Wave 5/6/7 Lean repairs from PR 14, and the Wave 4 certificate repair and checksum provenance from PR 15.

Preserve PR 13's physical qualifications for C-33 and replace its obsolete false-bound description with PR 10's corrected `4^3` arithmetic statement. State that this composition includes that proof repair. Retain the current main and PR 13 changelog entries and add PR 14's Lean repair entry.

Preserve the union of manifest paths from all four heads and recompute every listed hash. The union has 39 entries, including the PR 13 review wrapper README. The included checksum provenance describes the earlier branch snapshots. The recomputed manifest here describes this composed tree.

All 32 Python, Lean and certificate files match their respective source heads byte for byte. `results.json` lists the source for each. No scientific calculation or proof source was edited during composition.

- Full `lake build` passes, 15 jobs, on Lean 4.35.0. The existing Wave 10 unused `hPos` warning remains.
- All seven controls in `python3 -m unittest -v test_wave11_12_corrections.py` pass.
- Wave 11, Wave 12 and Wave 4 generators with `--check` pass byte-identical certificate checks.
- All 39 manifest entries pass `shasum -a 256 -c SHA256SUMS`.
- `git diff --check` passes.

The long Wave 7 generator was not repeated. Its source and certificate remain unchanged. Its earlier successful check is historical evidence.

## Exact replay

Create an isolated checkout at the frozen PR 13 head, `cce0284d03efb5c5c6ce8a70014ea436d7a3a801`. Apply the patch from this bundle using its absolute path:

```sh
git apply /absolute/path/to/gravity-composition.patch
lake build
python3 -m unittest -v test_wave11_12_corrections.py
python3 wave11_machian_pairing_unification.py --check
python3 wave12_cosmic_dawn_quasar_collapse.py --check
python3 wave4_unified_field_solver.py --check
shasum -a 256 -c SHA256SUMS
git diff --check
```

A fresh replay checkout accepted the patch, passed all 39 hashes and `git diff --check`, and matched all 53 tracked files in the tested composition. `results.json` records the patch hash and manifest hash. The patch contains no build or cache files.

## Limits

This is a local integration check, not a merged-main or hosted CI result. Lean establishes the encoded arithmetic statements. Generator agreement and numerical controls do not establish the physical models, seed formation, merger hardening or a gravitational-wave population prediction. Recompute the manifest after any listed file changes.

The raw patch retains required blank context markers from unified diff format. These context spaces are preserved for exact replay. The applied source tree passes its whitespace check.
