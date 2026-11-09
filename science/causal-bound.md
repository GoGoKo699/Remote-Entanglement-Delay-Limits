# The causal receiver bound

For a stationary Markovian source, propagation delay restricts the simultaneous source–receiver state before any particular receiver is chosen. The relevant state is the source channel over one propagation time, applied to a purification of its stationary state. Every admissible receiver produces a local postprocessing of this state.

## Model and notation

The source $`A`$ has finite dimension $`d`$ and a fixed generator

```math
\mathcal L(X)=-i[H,X]
+\sum_{j=1}^{m}\left(
L_jXL_j^\dagger-\frac12\{L_j^\dagger L_j,X\}
\right),\qquad \mathcal E_t=e^{t\mathcal L}.
```

It starts in a stationary state $`\pi`$, so $`\mathcal E_t(\pi)=\pi`$. A vacuum input-output dilation supplies the independent fresh noise increments that generate this semigroup. The receiver starts independently of the source and may use arbitrary finite quantum memory, local ancillas, measurements, classical records and causal local controls. It does not act back on the source.

At physical time $`t`$, every source output accessible to the receiver was emitted no later than $`t-\tau`$. No additional channel conveys more recent source information. Known clock signals and predetermined control waveforms are allowed. The state considered below is unconditional; retained measurement outcomes can be included in the receiver register. These assumptions concern the physical equal-time state $`\rho_{AB}(t)`$, not a correlation function whose source and receiver times differ by $`\tau`$.

The upper bound allows incomplete field collection, propagation noise and additional receiver latency. Exact optimality will use the ideal case in which every purifying output channel is delivered coherently with the same pure delay $`\tau`$; [attainability](attainability.md) gives the construction and [receiver resources](receiver-resources.md) records its resource assumptions.

Choose a basis on $`A`$ and an isomorphic register $`R`$. For a matrix $`X`$, use the vectorization

```math
|X\rangle\!\rangle_{AR}
=\sum_{a,r}X_{ar}|a\rangle_A|r\rangle_R.
```

The canonical stationary purification and delayed state are

```math
\Phi_\pi=|\sqrt\pi\rangle\!\rangle
\langle\!\langle\sqrt\pi|,
\qquad
\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id}_R)(\Phi_\pi).
```

The marginals of $`\Phi_\pi`$ are $`\pi`$ and $`\pi^T`$. Changing the chosen basis changes only the corresponding representation of the reference register.

## Theorem: domination by one delayed channel state

For every admissible receiver and every $`t\ge\tau`$, there is a channel $`\Lambda_t:R\to B`$ such that

```math
\boxed{\rho_{AB}(t)
=(\mathrm{id}_A\otimes\Lambda_t)(\sigma_\tau).}
```

Neither the receiver's internal dimension nor the complexity of its controls appears in the bound. The channel $`\Lambda_t`$ is a mathematical description of its output state; the statement does not require that it be known or implemented separately.

### Proof

Set $`s=t-\tau`$. Let $`F_{\le s}`$ denote all source output emitted through source time $`s`$, including inaccessible outputs if convenient. At that cut the joint state $`\eta_{AF_{\le s}}(s)`$ has source marginal $`\pi`$.

The source's evolution from $`s`$ to $`t`$ uses fresh independent input increments. The receiver's complete processing through physical time $`t`$ acts only on the old output and its independent local resources. These operations commute in the dilation. Combining all receiver operations, including averaged adaptive branches, into a channel $`\mathcal R_t`$ gives

```math
\rho_{AB}(t)
=(\mathcal E_\tau\otimes\mathcal R_t)
  \bigl(\eta_{AF_{\le s}}(s)\bigr)
=(\mathcal E_\tau\otimes\mathrm{id}_B)(\omega_{AB}),
\qquad
\omega_A=\pi.
```

Every extension of $`\pi`$ is a channel image of a purification of $`\pi`$. To see this, purify $`\omega_{AB}`$ to $`ABC`$ and use the isometric equivalence of purifications: an isometry $`V:R\to BC`$ maps $`|\sqrt\pi\rangle\!\rangle`$ to that purification. Tracing out $`C`$ defines a channel $`\Lambda_t`$ with

```math
\omega_{AB}
=(\mathrm{id}_A\otimes\Lambda_t)(\Phi_\pi).
```

Commuting the two local channels yields the asserted formula. The purification step is standard; see Watrous, Theorem 2.12 and the channel dilation results in Chapter 2.[^watrous]

## Optimal entanglement values

Let $`E`$ be a bipartite entanglement monotone under deterministic local channels. Then the theorem gives, at each physical time,

```math
E\bigl(\rho_{AB}(t)\bigr)\le E(\sigma_\tau).
```

For the corresponding equality, assume $`\pi>0`$ and that the source is primitive, in the explicit sense

```math
\lim_{t\to\infty}\mathcal E_t(X)=\pi\,\mathrm{Tr}X.
```

Suppose also that all source noise outputs are available coherently with the same delay. The finite-memory continuous receiver in [attainability](attainability.md) has a designated $`d`$-dimensional output register $`C`$ and, for every $`\epsilon>0`$, can satisfy

```math
\|\rho_{AC}(t)-\sigma_\tau\|_1<\epsilon
\quad\text{for every sufficiently late }t.
```

Consequently, for every continuous entanglement monotone on $`d\times d`$ states,

```math
\boxed{
\sup_{\mathsf R}\liminf_{t\to\infty}
E\bigl(\rho_{AC}^{\mathsf R}(t)\bigr)
=E(\sigma_\tau).
}
```

The supremum allows the receiver controls to depend on the desired accuracy. The designated output has fixed dimension; arbitrary internal receiver memory is permitted in the converse. Continuity is needed only for passing from approximate attainment to equality of values. The finite-time upper bound itself does not require continuity or primitivity.

For the driven-qubit application, $`A`$ and the designated output $`C`$ are qubits, and $`E`$ can be ordinary Wootters concurrence. Arbitrary internal receiver memory is still allowed. The matched receiver in [attainability](attainability.md#an-autonomous-matched-qubit-receiver) is itself one qubit and reaches the optimum in its stationary limit.

## The exact entanglement horizon

When $`\pi>0`$, the delayed state is separable exactly when the source channel is entanglement breaking:

```math
\sigma_\tau\text{ is separable}
\quad\Longleftrightarrow\quad
\mathcal E_\tau\text{ is entanglement breaking}.
```

Indeed, if $`|\Phi_d\rangle=d^{-1/2}\sum_i|i i\rangle`$ and

```math
J_\tau=(\mathcal E_\tau\otimes\mathrm{id})
(|\Phi_d\rangle\langle\Phi_d|),
```

then

```math
\sigma_\tau
=d\,\bigl(I\otimes(\sqrt\pi)^T\bigr)J_\tau
       \bigl(I\otimes(\sqrt\pi)^T\bigr).
```

The filter is invertible, so it preserves separability in both directions. The Choi-state characterization of entanglement-breaking channels then applies.[^hsr]

Define

```math
t_{\mathrm{EB}}
=\inf\{t\ge0:\mathcal E_t\text{ is entanglement breaking}\}.
```

The semigroup property and closedness of the set of entanglement-breaking channels imply that every $`\tau\ge t_{\mathrm{EB}}`$ is forbidden for source–receiver entanglement, including the endpoint. Conversely, if $`\tau<t_{\mathrm{EB}}`$, then $`\sigma_\tau`$ is entangled. Since the finite-dimensional separable set is closed, a sufficiently accurate finite-time receiver approximation is also entangled. Under the ideal collection assumptions, this identifies the receiver-independent horizon exactly with $`t_{\mathrm{EB}}`$.

For primitive finite-dimensional semigroups with a faithful stationary state, $`t_{\mathrm{EB}}<\infty`$. This eventual-entanglement-breaking property is established by Hanson, Rouzé and Stilck França, Theorem 2.1.[^hanson] Here it is used to identify the operational propagation-delay horizon. In dimension at least three, entanglement before the horizon need not be distillable; the assertion concerns entanglement itself.

A normalized heralded branch need not obey the same numerical monotone bound as an unconditional state. It cannot evade the entanglement-breaking horizon: each local completely positive branch maps a separable state to an unnormalized separable state.

## Relation to spatial channel cuts

The same structural idea appears in matrix-product states: tracing out a separating interval applies a power of the transfer channel, after which the two retained blocks are obtained by local maps. Ferydouni, Jackson and Scalet use this construction to prove finite entanglement length for normal matrix-product states.[^fjs] The theorem above applies the channel cut to a causal receiver and combines it with attainable stationary purification. It does not assert that propagation delay removes every retarded-time correlation.

## References

[^watrous]: J. Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), Chapter 2, especially Theorem 2.12, “Unitary equivalence of purifications.” [Author's chapter PDF](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

[^hsr]: M. Horodecki, P. W. Shor and M. B. Ruskai, “General Entanglement Breaking Channels,” *Reviews in Mathematical Physics* **15**, 629–641 (2003), Theorem 4. [DOI](https://doi.org/10.1142/S0129055X03001709); [arXiv:quant-ph/0302031v2](https://arxiv.org/abs/quant-ph/0302031v2).

[^hanson]: E. P. Hanson, C. Rouzé and D. Stilck França, “Eventually Entanglement Breaking Markovian Dynamics: Structure and Characteristic Times,” *Annales Henri Poincaré* **21**, 1517–1571 (2020), Theorem 2.1. [DOI](https://doi.org/10.1007/s00023-020-00906-4); [arXiv:1902.08173](https://arxiv.org/abs/1902.08173).

[^fjs]: R. Ferydouni, T. Jackson and S. O. Scalet, “Entanglement Sudden Death in Gapped Ground States,” arXiv:2610.17038v1 (2026), Section 3, Eq. (3), Proposition 2 and Theorem 2. [Primary preprint](https://arxiv.org/abs/2610.17038v1).
