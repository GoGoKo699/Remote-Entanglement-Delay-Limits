# Reproduce the scientific calculations

The written proofs establish the receiver-universal envelope, continuous-time attainment and the uniform optimization over all static source parameters. The finite calculations here check the delicate algebraic and numerical steps against independently constructed representations. They are not a substitute for those proofs.

## Environment and commands

The checked environment uses Python 3.12 with `mpmath 1.3.0`, `numpy 2.3.5`, `scipy 1.17.0` and `matplotlib 3.10.8`. Install the pinned dependencies and run from the repository root:

```bash
python3 -m pip install -r requirements-verification.txt
python3 verification/run_all.py
```

The driver stops if either scientific check fails. Each script also runs independently and supports `--json`:

```bash
python3 verification/verify_receivers.py --json > verification/outputs/receivers.json
python3 verification/verify_driven_qubit.py --json > verification/outputs/driven-qubit.json
```

The committed output files contain the full parameters and numerical residuals. Rerunning them overwrites only those outputs when the explicit shell redirection above is used; the verification scripts themselves print results without changing files.

## Receiver construction

[verify_receivers.py](verify_receivers.py) checks the matched two-qubit cascade in the Pauli convention used by the science pages, including its source marginal, dark state, stationary behavior and local unitary relating the dimer to the canonical stationary purification. The source's autonomous reduced generator is checked on all matrix units. The script also checks the continuous purification tracker's receiver GKLS identity, dark jumps and time-dependent drift against the matrix square-root derivative. Four dimer and four tracker cases include multiple bath channels and a unital source. These tests target transposition, cascade sign and purification-gauge errors.

The general faithfulness argument, uniform-in-time control bound, independent initialization estimate and global attraction proof are in [attainability](../science/attainability.md). A finite sample cannot prove those statements for all sources.

## Driven-qubit channel and sharp law

[verify_driven_qubit.py](verify_driven_qubit.py) constructs the channel in three ways:

1. Exponentiate the four-dimensional physical Lindblad superoperator with column vectorization.
2. Exponentiate the three-dimensional physical Bloch generator and build its normalized Choi matrix.
3. Rotate to the stationary frame and use the exact signed matrix entries from the asymptotic proof.

It checks the stationary state, frame rotation, all signed state entries, reference Pauli transpose, Choi concurrence factorization and local-filter covariance. It also verifies the finite-time contraction, cross-block, longitudinal and tangent-rotation inequalities. Five general finite-time parameter choices include weak drives and nonzero detunings.

The asymptotic tables include 33 resonant samples at $`\gamma\tau=10,20,40`$ with $`k=0,0.25,\ldots,2.5`$ and exact $`s=ke^{-\gamma\tau/2}`$; nine $`k=1`$ samples at $`\gamma\tau=20,40,60`$ and $`\Delta/\gamma=0,1,100`$; and twelve samples on the two sides of the weak-source entanglement-breaking transition.

For example, at $`\gamma\tau=60`$ and $`k=1`$:

| Detuning $`\Delta/\gamma`$ | Scaled concurrence $`C/e^{-\gamma\tau}`$ |
|---:|---:|
| 0 | 0.499999999997941322946846952358 |
| 1 | 0.499999999997292098498328716784 |
| 100 | 0.499999999997192713968890056060 |

These computations use 80 decimal digits. Concurrence is evaluated from Hermitian eigenvectors and singular values, avoiding a direct non-Hermitian eigenvalue calculation of $`\rho\widetilde\rho`$. The small stationary eigenvalue is evaluated with a cancellation-free formula. The script rejects substantial negative eigenvalues instead of silently clipping them. The largest identity residual among the five general finite-time cases is below $`5\times10^{-64}`$; across the much more ill-conditioned long-delay samples it is below $`5.4\times10^{-41}`$.

To check the precision of the smallest roots, run:

```bash
python3 verification/verify_driven_qubit.py --dps 100 --json
```

The [100-digit repeat](outputs/driven-qubit-100-digits.json) passes the same assertions. All 54 scaled concurrence entries in the finite-ratio, detuning and horizon tables agree with the 80-digit run at all 30 reported digits. The largest long-delay identity residual decreases to below $`6.6\times10^{-61}`$.

The uniform large-delay coefficient is proved by the [stationary-axis estimates and subsequence argument](../science/long-delay-law.md), which allow arbitrary delay-dependent static detuning. A bounded numerical detuning grid cannot establish that uniformity. The finite-delay examples also do not claim that resonance is globally optimal at every finite delay.

## Figure

[plot_tradeoff.py](plot_tradeoff.py) renders the committed high-precision samples against the analytic limiting parabola:

```bash
python3 verification/plot_tradeoff.py
```

It writes [the SVG figure](../figures/stationary-tradeoff.svg) and [its PNG copy](../figures/stationary-tradeoff.png). The curve is $`[k-k^2/2]_+`$ and the symbols are exact-channel evaluations for specified resonant sources. The maximum $`1/2`$ is an asymptotic coefficient; values at finite delay can lie above it. This is a visualization of the tradeoff, not a numerical search certificate.

## Scope of validation

The calculations check finite-dimensional identities, selected inequalities and examples. The source model, delayed-state definitions and order of limits remain those in [the scientific model](../science/model.md). The analytic proofs establish causality, existence, convergence and all-parameter asymptotics. These numerical checks do not establish physical hardware bandwidth, preparation rates, behavior with uncollected baths, or results for time-dependent source control.
