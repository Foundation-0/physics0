# Five-mass central-configuration pilot

Status: numerical consistency checks, awaiting independent review. No new
configuration, complete list or certified existence result is claimed.
This is a first executable step for the celestial-mechanics track in issue 8.

Run `python3 pilots/central_configurations.py`. Units set G and each mass to 1.
The script subtracts the centre of mass, sums the Newtonian pair forces,
fits lambda by projection and reports the largest residual of F_i + lambda x_i.
It checks a regular pentagon and a square with a fifth mass at the centre.
Neither example exhausts the five-body configurations.

For regular n-gons, a separate trigonometric radial-force sum checks lambda.
A displaced pentagon supplies a negative control, and collisions are rejected.
Passing floating-point residuals establishes numerical consistency only.

## Next acceptance checks

1. Compare the seeds with the five-mass catalogue and state its equivalence
   convention: rotations, reflections, permutations and scaling.
2. Adapt the point-charges certifier with the attractive equal-mass equations,
   centre-of-mass constraints and a scale condition. Reusing the implementation
   without checking those equations does not certify this problem.
3. Use interval enclosures for roots and exclude collisions and unbounded
   regions. Root finding alone cannot establish completeness.
4. Reproduce the complete five-mass list with independent review before
   estimating the eight-mass cost.

The broader roadmap also retains periodic-orbit existence, Lean statements,
quantum-code searches, lattice statistical physics, astronomical-data work and
claim replication. Those tracks require their own data, sources and acceptance
checks. This pilot neither resolves those tasks nor closes the roadmap issue.

Prepared by gpt-forge (OpenAI) for Ahraz Arifuddin.
