# Receiver resources and the scope of the optimum

The receiver-independent upper bound and its attainment use different amounts of structure. The bound needs the causal cut and a stationary source marginal. Attainment also needs coherent access to the source's full purifying output. This section records those resources and explains which changes would define a different optimization.

## Continuous receivers

The detailed operators and convergence proofs are in [attainability](attainability.md). Their requirements are summarized here.

| Resource | General primitive source | Driven amplitude-damped qubit |
|---|---|---|
| Source | Known, fixed finite-dimensional generator, initialized in its faithful stationary state | $`H_A=(\Omega X+\Delta Z)/2`$, $`L_A=\sqrt\gamma\,\sigma_-`$, with fixed $`\gamma>0`$ and static $`\Omega,\Delta`$ |
| Collected field | Every independent output channel in the pure-input Markov dilation | The complete radiative output defining $`\gamma\mathcal D[\sigma_-]`$ |
| Propagation | A common deterministic delay, with known phases compensated locally | The same assumption |
| Coherent receiver memory | Sufficient dimension $`d^2`$, split into a designated $`d`$-dimensional output and a $`d`$-dimensional auxiliary register | One receiver qubit suffices |
| Receiver control | Known time-dependent local Hamiltonian and coupling operators | Constant matched drive, opposite detuning, and the same radiative coupling strength |
| Initialization | A known receiver-local pure state, independent of the source | Any initial receiver state; the matched cascade is globally attractive |
| Accuracy statement | For every accuracy, one bounded-control receiver stays within that error at every sufficiently late time | Exact attainment in the late-time limit, up to a fixed local output unitary |

The general $`d^2`$ bound is sufficient, with no minimality assertion. The second factor of its memory retains the information associated with a mathematical purification of the source's initial mixed state. That reference is never supplied to the receiver. The receiver's initial entanglement, if any, is confined to its own local registers.

No coherent temporal block of the traveling field is retained by the continuous construction. Its finite memory interacts with the fields as they arrive. The coefficients remain bounded for each chosen regularization, but this theorem does not place a common bound on their norms as the requested error tends to zero. It assumes noiseless receiver memory and ideal control of the specified interactions. A hardware bound on coupling strength, control bandwidth, collection efficiency or memory lifetime would impose an additional constraint.

The matched qubit receiver is the established cascaded dark-dimer construction of Stannigel, Rabl and Zoller.[^stannigel] In the convention $`Z=|g\rangle\langle g|-|e\rangle\langle e|`$, its Hamiltonian and coupling are

```math
H_B=\frac{\Omega X-\Delta Z}{2},
\qquad L_B=\sqrt\gamma\,\sigma_-^B.
```

The [explicit dark state and convergence proof](attainability.md#an-autonomous-matched-qubit-receiver) fix the cascade signs and show that this one-qubit receiver reaches the fixed-source envelope. Generic autonomous absorber existence is not a substitute for that attraction proof. General reverser constructions specify a stationary pure state without asserting its convergence from arbitrary initial conditions.[^tsang] Restrictions on attractive maximally entangled steady states further illustrate why this distinction matters.[^pocklington]

## Fixed source lifetime and reduced brightness

For the optimized qubit law, the decay rate $`\gamma`$ is fixed. Static source parameters may depend on the chosen delay, but they remain constant throughout each protocol. The late-time limit is taken for each source and receiver design before the large-delay limit. No uniform preparation-time bound is part of this optimization.

The stationary excited population and radiative photon flux are

```math
\pi_{ee}
=\frac{\Omega^2}{\gamma^2+4\Delta^2+2\Omega^2}
=\frac{s}{2},
\qquad
\mathcal F=\operatorname{Tr}(L_A^\dagger L_A\pi)
=\frac{\gamma s}{2}.
```

The sharp long-delay law is attained when $`s\sim e^{-\gamma\tau/2}`$. Therefore its source flux satisfies

```math
\mathcal F\sim\frac\gamma2 e^{-\gamma\tau/2}.
```

On resonance, one such choice is $`\Omega\sim(\gamma/\sqrt2)e^{-\gamma\tau/4}`$. The optimized stationary concurrence thus comes with decreasing source excitation and decreasing photon flux. Keeping brightness fixed would change the optimization. Allowing $`\gamma`$ to decrease with delay would also change the regime: the proven law is in $`\gamma\tau`$, and does not impose a lifetime-independent distance limit.

These statements concern the entanglement present in a retained receiver register. Destructively reading out, transferring or consuming that register generally changes the state on which subsequent receiver evolution depends. The result does not supply a stream of independent entangled pairs or a repeated-use distribution rate. A preparation, extraction and recovery schedule would need its own analysis.

## Why stationarity matters: an explicit transient example

An initially excited, undriven source illustrates the scope of the stationary optimum. Take $`\Omega=0`$ and initialize $`A`$ in $`|e\rangle`$. At source time $`u`$, its joint pure state with the emitted field is

```math
|\Psi(u)\rangle
=\sqrt p\,|e\rangle|0\rangle_F
+\sqrt{1-p}\,|g\rangle|1_{f_u}\rangle_F,
\qquad p=e^{-\gamma u},
```

where $`|1_{f_u}\rangle`$ is the normalized one-photon wavepacket on $`[0,u]`$ with envelope

```math
f_u(v)=\frac{\sqrt\gamma\,e^{-\gamma v/2}}
{\sqrt{1-e^{-\gamma u}}},
\qquad 0\le v\le u.
```

The old field occupies only the two-dimensional span of vacuum and this known one-photon mode. Ideal coherent mode access can encode that span into a receiver qubit, with arbitrary accuracy sufficient here. At physical time $`u+\tau`$, the source has meanwhile undergone an extra amplitude-damping channel. Writing $`a=e^{-\gamma\tau/2}`$, the equal-time state is

```math
\begin{aligned}
\rho_{AB}={}&p a^2|e0\rangle\langle e0|
+(1-p)|g1\rangle\langle g1|\\
&+p(1-a^2)|g0\rangle\langle g0|\\
&+a\sqrt{p(1-p)}
\bigl(|e0\rangle\langle g1|+|g1\rangle\langle e0|\bigr).
\end{aligned}
```

Its concurrence is

```math
C(\rho_{AB})=2a\sqrt{p(1-p)}.
```

Choosing the half-decay time $`u=(\log 2)/\gamma`$ gives

```math
C=e^{-\gamma\tau/2},
```

which is parametrically larger than the optimized stationary value $`(1/2+o(1))e^{-\gamma\tau}`$. The state before the extra delay is maximally entangled with the already emitted wavepacket.

For an explicit continuous capture limit, a receiver qubit with zero local Hamiltonian and coupling $`L_B(v)=\sqrt{\kappa(v)}\,\sigma_-^B`$ uses

```math
\kappa(v)=\frac{\gamma}{e^{\gamma v}-1}.
```

Its ideal aligned cascade tracks $`e^{-\gamma v/2}|eg\rangle-\sqrt{1-e^{-\gamma v}}|ge\rangle`$: the total jump annihilates this vector and the no-jump drift gives its derivative. The minus sign is a removable local receiver phase. The coupling is singular at $`v=0`$. To obtain bounded controls, discard output before a small $`\delta>0`$ and start the receiver in its ground state at the corresponding arrival time. At that cut the actual state differs from the ideal comparison state by $`O(\sqrt{\gamma\delta})`$. Contractivity bounds the subsequent error by the same amount, and the remaining coupling rate is bounded by $`\gamma/(e^{\gamma\delta}-1)`$. Choosing $`\delta`$ arbitrarily small therefore approaches the stated concurrence without requiring an exact singular endpoint control.

There is no conflict with the causal cut. At the relevant cut, this source's marginal is $`(1-p)|g\rangle\langle g|+p|e\rangle\langle e|`$, not its stationary ground state. The stationary purification used in the envelope is consequently the wrong input for this transient protocol.

## Loss, postselection and other changes of resources

Incomplete collection or propagation noise can be included in the receiver's local channel, so the complete-output causal envelope remains an upper bound. These effects generally prevent the receiver from reaching that envelope. An inaccessible bath is especially consequential for the purification tracker: it continually retains source information that the receiver cannot coherently collect.

Predetermined drives and shared clock references are allowed. A source-dependent signal that reaches the receiver faster than $`\tau`$, a feedback path that changes the source dynamics, an additional protected source register, or initial source–receiver entanglement changes the model underlying the bound. The theorem also does not optimize over time-dependent source control.

The state is unconditional. Measurement records can be retained as local receiver registers, and deterministic processing of them stays within the envelope. Conditioning on a successful event can increase the concurrence of a normalized branch. Appropriate entanglement monotones still obey their average monotonicity inequalities. Separability after the entanglement-breaking horizon survives every local completely positive branch, regardless of normalization.

Ordinary Wootters concurrence in the qubit application is evaluated only between the source and a designated receiver qubit. Additional receiver memory is permitted, but is traced out before that score is evaluated. For larger dimensions, the general envelope controls entanglement monotones on their stated bipartite spaces; nonseparability alone does not imply distillability.

## Appendix: an exact collision-model construction

An exact discrete construction makes the memory count transparent and supplies a version that does not require matrix inverses. It is the purification/SVD mechanism used in sequential quantum decoders.[^yang] The continuous construction in [attainability](attainability.md) supplies the separate regularity and initialization argument needed for continuous fields.

Let one source step be an isometry $`V:A\to A\otimes E`$ with a finite-dimensional pure input unit. Its reduced channel $`\mathcal T`$ is primitive, has stationary state $`\pi`$, and all emitted units arrive after $`m`$ steps. Introduce a mathematical reference $`R`$ purifying the initial state and set

```math
\chi_n=(\mathcal T^n\otimes\operatorname{id}_R)(\Phi_\pi).
```

Use memory $`M=C\otimes R'`$ with dimension $`d^2`$, in a copy basis of $`A\otimes R`$. The intended pure state after processing $`n`$ units is

```math
|\sqrt{\chi_n}\rangle\!\rangle_{AR:M}.
```

At $`n=0`$, this canonical purification factors into the given source-reference purification and a known receiver-local pure state. Suppose the target has been reached after step $`n-1`$. Applying the next source isometry produces a pure state on $`ARME`$ with marginal $`\chi_n`$ on $`AR`$. The target

```math
|\sqrt{\chi_n}\rangle\!\rangle_{AR:M}\otimes|0\rangle_E
```

has the same marginal. Unitary equivalence of purifications therefore gives a unitary on $`M E`$ mapping the actual state to this target.[^watrous] The receiver applies that known unitary when the corresponding unit arrives. It acts on neither $`A`$ nor $`R`$, and the processed unit leaves in a fixed pure state. Induction proves exact tracking for every step with the same memory dimension.

Since $`\chi_n\to\pi\otimes\pi^T`$, the target factorizes asymptotically into a stationary purification on $`AC`$ and a separate state on $`RR'`$. The square-root trace inequality used in [attainability](attainability.md) yields

```math
\left\|\rho_{AC}(n+m)
-(\mathcal T^m\otimes\operatorname{id})(\Phi_\pi)\right\|_1
\le2\sqrt{\|\chi_n-\pi\otimes\pi^T\|_1}.
```

This is one sequential receiver, exposing its designated output after every step. Its controls depend on the known model and the step number; its coherent memory does not grow with the number of arrivals. A finite time-bin implementation has the bin's own processing latency. The continuous theorem does not infer zero-latency attainment by ignoring that latency; it constructs a continuous receiver directly.

## References

[^stannigel]: K. Stannigel, P. Rabl and P. Zoller, “Driven-dissipative preparation of entangled states in cascaded quantum-optical networks,” *New Journal of Physics* **14**, 063014 (2012), Section 3.1 and Appendix B.1. [DOI](https://doi.org/10.1088/1367-2630/14/6/063014); [arXiv:1112.1690v2](https://arxiv.org/abs/1112.1690v2).

[^tsang]: M. Tsang, “Quantum reversal: a general theory of coherent quantum absorbers,” *Quantum* **9**, 1650 (2025). The Introduction expressly distinguishes reverser existence from convergence. [DOI](https://doi.org/10.22331/q-2025-02-26-1650); [arXiv:2402.02502v3](https://arxiv.org/abs/2402.02502v3).

[^pocklington]: A. Pocklington and A. A. Clerk, “Universal Time-Entanglement Trade-off in Open Quantum Systems,” *PRX Quantum* **5**, 040305 (2024), Section III. [DOI](https://doi.org/10.1103/PRXQuantum.5.040305); [arXiv:2404.03625v2](https://arxiv.org/abs/2404.03625v2).

[^yang]: D. Yang, S. F. Huelga and M. B. Plenio, “Efficient Information Retrieval for Sensing via Continuous Measurement,” *Physical Review X* **13**, 031012 (2023), Section IV B and Appendix B. [DOI](https://doi.org/10.1103/PhysRevX.13.031012); [arXiv:2209.08777v3](https://arxiv.org/abs/2209.08777v3).

[^watrous]: J. Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), Chapter 2, Theorem 2.12. [Author's chapter PDF](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).
