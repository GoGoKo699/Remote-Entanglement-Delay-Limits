# Related work and contribution boundary

The result concerns unconditional entanglement between a stationary source and a receiver at the **same physical time**. The source dynamics and its coupling rate are fixed while the receiver can process every output that has arrived. The sharp qubit asymptotic further optimizes all static source drive strengths and detunings at fixed spontaneous-emission rate. Primary-source comparison updated on 9 November 2026.

## What is established here

For an autonomous stationary source with reduced channel $`\mathcal E_\tau`$ and stationary state $`\pi`$, every admissible receiver state is a local postprocessing of

```math
\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id})
\bigl(|\sqrt\pi\rangle\langle\sqrt\pi|\bigr).
```

Full collection of the purifying output permits arbitrarily accurate late-time attainment by a causal finite-memory decoder. A regularized continuous decoder has finite coefficients for each prescribed accuracy; no accuracy-independent control bound is asserted. Thus $`\sigma_\tau`$ gives the supremum of every continuous entanglement monotone. For faithful $`\pi`$, its entanglement vanishes exactly when $`\mathcal E_\tau`$ is entanglement breaking. Neither the eventual-entanglement-breaking property nor finite-delay loss of entanglement for particular receivers is new by itself.

The sharper physical result is obtained for

```math
\mathcal L\rho=-i[(\Omega X+\Delta Z)/2,\rho]
+\gamma\mathcal D[\sigma_-]\rho,
\qquad\gamma>0\text{ fixed}.
```

After optimizing the retained output qubit over arbitrary causal receiver processing and optimizing both static source parameters,

```math
\sup_{\Omega,\Delta,\mathrm{receiver}}C
=\left(\frac12+o(1)\right)e^{-\gamma\tau}.
```

The estimate is uniform even when drive and detuning depend on delay. Its optimizing stationary mixedness is
$`s=2\sqrt{\det\pi}\sim e^{-\gamma\tau/2}`$, and its finite-ratio limit is
$`C/e^{-\gamma\tau}\to\max\{0,k-k^2/2\}`$ when
$`s/e^{-\gamma\tau/2}\to k`$. This identifies the cost of extending the source's entanglement horizon: weaker stationary source entanglement must be traded against longer survival. It is not a universal limit on transient quantum communication or on sources with adjustable decay rate.

## Cascaded absorbers and entangled steady states

**Stannigel, Rabl, and Zoller (2012).** Their cascaded-network construction already supplies coherent absorbers, stationary purifications, and the driven-qubit dark dimer. Section 3.1 gives the two-spin pure state for matched drives and opposite detunings; Appendix B.1 addresses uniqueness. The finite-delay project inherits that mechanism. The new use is the physical equal-time channel acting during propagation, followed by an optimization that no more elaborate downstream receiver can improve. The inspected paper's optimization concerns imperfections and entanglement patterns, rather than the uniform propagation-delay law. [Primary article](https://doi.org/10.1088/1367-2630/14/6/063014), [arXiv:1112.1690v2](https://arxiv.org/abs/1112.1690v2).

**Pichler, Ramos, Daley, and Zoller (2015).** Their chiral-spin-network theory uses a Markovian master equation and derives entangled dark states. Its conclusion explicitly identifies neglected photon/phonon propagation times as a limitation of that treatment. Consequently distance independence of the instantaneous cascaded model is not a statement about equal-time entanglement for arbitrary finite propagation delay. [Primary article](https://doi.org/10.1103/PhysRevA.91.042116), [author-university PDF](https://pure.strath.ac.uk/ws/portalfiles/portal/43979674/Pichler_etal_PRA2015_quantum_optics_of_chiral_spin_networks.pdf).

**Pichler and Zoller (2016).** A purely unidirectional cascade can be written in a retarded-time coordinate, unlike a network with feedback loops. This is an inherited simplification of the dynamics. It does not equate the source at time $`t-\tau`$ with the source at time $`t`$, which is the distinction needed for simultaneous bipartite entanglement. [Primary article](https://doi.org/10.1103/PhysRevLett.116.093601), [arXiv:1510.04646](https://arxiv.org/abs/1510.04646).

**Motzoi et al. (2016).** This work develops robust stationary entanglement over lossy unidirectional and bidirectional channels. Section VI treats unidirectional delay through correlations between qubits at different times. The finite-delay result here instead bounds the physical simultaneous state and separates receiver improvements from source retuning. This qualification does not invalidate the earlier loss analysis or its retarded correlations. [Primary article](https://doi.org/10.1103/PhysRevA.94.032313), [arXiv:1512.03415v2](https://arxiv.org/abs/1512.03415v2).

## Current experimental and finite-delay context

**Irfan et al. (2026).** This experiment stabilizes remote entanglement in two superconducting devices in a cascaded network and improves robustness using a modified symmetry. The devices are connected by approximately 60 cm of cable. Section II describes the ideal chiral protocol as fully distance independent, citing the earlier Markovian spin-network treatment. The present result specifies the long-delay, equal-physical-time qualification to that ideal statement; it is not a challenge to the reported experiment. The experiment's loss and mismatch optimization differs from optimization over a finite propagation delay. [Phys. Rev. X 16, 031004](https://doi.org/10.1103/z6zz-vw5q), published 13 July 2026; [primary PDF](https://journals.aps.org/prx/pdf/10.1103/z6zz-vw5q).

**Andrés-Juanes et al. (2026).** A separate Josephson parametric converter supplies two-mode squeezed microwave fields that drive two remote qubits into a stationary entangled state. This is a different architecture from an autonomous amplitude-damped source qubit feeding a receiver. It demonstrates the relevance of stationary entanglement distribution but does not fall under the specific fixed-$`\gamma`$, single-source qubit asymptotic. [Phys. Rev. X 16, 031005](https://doi.org/10.1103/r4jt-j39w), published 13 July 2026; [primary PDF](https://journals.aps.org/prx/pdf/10.1103/r4jt-j39w).

**Agustí, Minoguchi, Fink, and Rabl (2022).** Section V A explicitly distinguishes simultaneous entanglement from delayed measurement correlations. Equation (38) maps the former to unequal-time correlations of a zero-delay master equation; Figure 5 evaluates concurrence and a finite delay threshold for two qubits driven by a separate parametric amplifier. This distinction and delay-induced entanglement death are therefore established antecedents. Equal path delays in that two-arm architecture do not cause the differential-delay degradation considered there. The present addition is receiver-universal optimization for a fixed autonomous source and the sharp source-tuning law for the driven amplitude-damped qubit. [Phys. Rev. A 105, 062454](https://doi.org/10.1103/PhysRevA.105.062454), [arXiv:2204.02993v2](https://arxiv.org/abs/2204.02993v2). The [2025 erratum](https://doi.org/10.1103/PhysRevA.111.049903) corrects effective-purity expressions, state-normalization typos and a loss-channel comparison. The delay treatment is also presented in Agustí's [2025 thesis](https://mediatum.ub.tum.de/doc/1773342/1773342.pdf), Section 3.7.2.

## The close matrix-product-state antecedent

**Ferydouni, Jackson, and Scalet (2026).** For normal translation-invariant matrix product states, Section 3, Eq. (3) expresses separated blocks as local postprocessings of the transfer channel across the omitted interval. Proposition 2 proves eventual entanglement breaking of a primitive channel, and Theorem 2 obtains a block-size-independent finite entanglement length. This is the closest mathematical antecedent for the channel-cut converse. The causal theorem uses that shared mechanism. Its operational addition is a causal receiver interpretation with finite-memory attainability, while its quantitative physics addition is the uniform static-driven-qubit optimum. Combining the MPS channel cut with standard purification/decoding tools is not an independent new compression principle. [arXiv:2610.17038v1](https://arxiv.org/abs/2610.17038v1), *Entanglement Sudden Death in Gapped Ground States*.

**Hanson, Rouzé, and Stilck França (2020).** The eventual-entanglement-breaking theorem for primitive continuous-time quantum Markov semigroups is established in this work. The source-channel horizon uses this theorem and the standard Choi characterization; the claim is the equality of the operational receiver horizon with the channel's actual entanglement-breaking time under full collection, not the existence of an eventual time. [Ann. Henri Poincaré 21, 1517–1571](https://doi.org/10.1007/s00023-020-00906-4), [arXiv:1902.08173](https://arxiv.org/abs/1902.08173).

## Receiver decoding and the attraction distinction

**Yang, Huelga, and Plenio (2023).** Section IV B, Eqs. (29)–(32), and Appendix B construct a time-dependent quantum decoder by sequential SVD/right normalization; Eq. (36) identifies a source-decoder purification. The known-pure-source construction uses a memory with the source's dimension. Applying this purification mechanism to source plus an inaccessible initial reference gives the stationary mixed-start $`d^2`$-memory construction used here. That extension is an application of an existing decoder method. The continuous mixed-start construction regularizes the initial rank deficiency and establishes the supremum with bounded coefficients for each fixed target accuracy. [Phys. Rev. X 13, 031012](https://doi.org/10.1103/PhysRevX.13.031012), [arXiv:2209.08777v3](https://arxiv.org/abs/2209.08777v3).

**Tsang (2025).** The reverser/coherent-absorber theory provides a prescribed pure steady state, but convergence from other initial states is outside its general existence theorem. It therefore cannot alone justify an attractive autonomous receiver for every primitive source. [Quantum 9, 1650](https://doi.org/10.22331/q-2025-02-26-1650), [arXiv:2402.02502v3](https://arxiv.org/abs/2402.02502v3).

**Pocklington and Clerk (2024).** Their preparation-time/entanglement tradeoff includes a strong-symmetry obstruction to preparing a maximally entangled pure state in equal-dimensional local common-bath dynamics. This is a concrete warning against inferring absorber attraction merely from source primitivity. A time-dependent finite-memory decoder and the explicitly attractive driven-qubit dimer have different hypotheses. [PRX Quantum 5, 040305](https://doi.org/10.1103/PRXQuantum.5.040305), [arXiv:2404.03625v2](https://arxiv.org/abs/2404.03625v2).

## Driven-qubit entanglement decay and inherited algebra

**Goyal, Banerjee, and Ghosh (2012).** Section V of the current arXiv version studies resonance fluorescence. Its Eq. (18) includes the resonantly driven amplitude-damped qubit as the zero-temperature case, Eqs. (19)–(20) give the channel and Choi state, and Figure 3 shows that stronger driving shortens the sudden-death time. The paper already uses channel-state duality and concurrence factorization. The new result is not driven-qubit sudden death. It weights the source channel by the same source's stationary purification, optimizes the resulting simultaneous receiver resource, and proves a sharp upper bound uniform over arbitrary detuning and delay-dependent static drive. [Phys. Rev. A 85, 012327](https://doi.org/10.1103/PhysRevA.85.012327), [arXiv:1102.4403v2](https://arxiv.org/abs/1102.4403v2).

The concurrence formula is due to [Wootters (1998)](https://doi.org/10.1103/PhysRevLett.80.2245). The pure-input one-sided factorization
$`C((\mathcal E\otimes\mathrm{id})(\psi))=C(\psi)C(J_\mathcal E)`$
is due to [Konrad et al. (2008)](https://doi.org/10.1038/nphys885). The equivalent homogeneous local-filter identity used in the asymptotic proof is inherited algebra. Entanglement-breaking equivalence with separability of the Choi state is the standard [Horodecki–Shor–Ruskai characterization (2003)](https://doi.org/10.1142/S0129055X03001709). These tools support the new optimization rather than constituting separate contributions.

## Scope of the comparison

The shared channel-cut, purification and decoding methods are credited above. The added conclusion is the receiver-optimized stationary tradeoff and the uniform all-static-drive coefficient $`1/2`$, with the exact fixed-source horizon and the shrinking optimal source mixedness specified together. The comparison does not claim a new coherent-absorber mechanism, a new eventual-entanglement-breaking theorem, or a bound on transient communication.
