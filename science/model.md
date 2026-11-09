# Stationary entanglement across a delayed quantum link

How much entanglement can a stationary emitter retain with a remote receiver when its output takes a nonzero time to arrive? The receiver may collect the entire output coherently, store quantum information and choose its own controls. The delay still leaves a part of the emitter's evolution inaccessible at the time the two nodes are compared.

This account gives an exact receiver-independent state envelope and a sharp long-delay law for a driven two-level emitter. The two results have different scopes: the state envelope applies to general finite-dimensional primitive Markov sources; the optimized concurrence law uses the specific static driven-amplitude-damping generator.

## 1. Source, propagation and receiver

The source $`A`$ has Hilbert-space dimension $`d`$ and a known, time-independent Lindblad generator

```math
\mathcal L(X)=-i[H,X]+\sum_{\mu=1}^{m}
\left(L_\mu X L_\mu^\dagger-
\frac12\{L_\mu^\dagger L_\mu,X\}\right),
\qquad \mathcal E_t=e^{t\mathcal L}.
```

Assume primitivity in the following explicit sense: a unique faithful density matrix $`\pi`$ satisfies $`\mathcal L(\pi)=0`$, and $`\mathcal E_t(X)\to\pi\mathrm{Tr}X`$ as $`t\to\infty`$. The finite-dimensional convergence is uniform on bounded sets. Initialize the source in $`\pi`$, so its unconditional state is stationary at every time.

Use a fixed vacuum input-output dilation, or an equivalent fully accessible purified Markov dilation, with independent pure incoming field increments. All output channels that purify the source dynamics propagate toward the receiver with the same deterministic delay $`\tau\ge0`$. A thermal or partially observed environment is covered by the tight statement only if its complete purification is included in the accessible output. A prescribed classical source drive is part of $`H`$; it is not an information channel from the evolving source to the receiver.

The receiver starts independently of the source and input fields. It can process arriving output causally, use noiseless finite-dimensional quantum memory, discard local systems and perform known time-dependent controls. It cannot act on output that has not arrived, drive the source through a return path, or use a faster source-information channel. The construction in [attainability](attainability.md) gives a sufficient memory dimension; no minimality claim is made.

At physical time $`t\ge\tau`$, the receiver has access only to source output emitted through $`t-\tau`$. The score is the unconditional joint state $`\rho_{AB}(t)`$ of the current source and a retained receiver output register $`B`$. This is an equal-physical-time quantity. Comparing the source at $`t-\tau`$ with the receiver at $`t`$ instead measures a different, retarded-time correlation.

## 2. The receiver-universal envelope

Fix a basis on $`A`$ and use a copy $`A'`$. Define the normalized canonical purification and its delayed state by

```math
|\sqrt\pi\rangle=\sum_{j,k}(\sqrt\pi)_{jk}|j\rangle_A|k\rangle_{A'},
\qquad
\Phi_\pi=|\sqrt\pi\rangle\langle\sqrt\pi|,
\qquad
\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id})(\Phi_\pi).
```

The second marginal of $`\Phi_\pi`$ is $`\pi^T`$ in this convention. A different purification basis changes only a receiver-local unitary.

**Causal envelope.** For every admissible receiver and every $`t\ge\tau`$, there is a completely positive trace-preserving map $`\Lambda_t:A'\to B`$ such that

```math
\rho_{AB}(t)=(\mathrm{id}\otimes\Lambda_t)(\sigma_\tau).
```

The map can depend on the protocol and time; the envelope does not. The proof uses the physical time cut, fresh input independence and universality of purification. It is given in [the causal bound](causal-bound.md).

**Attainability.** In the ideal full-output model, $`\sigma_\tau`$ lies in the closure of late-time states achievable with fixed finite receiver memory and deterministic causal control. Consequently, the closure of all such states with a specified finite output dimension is exactly

```math
\mathcal S_\tau(B)
=\left\{(\mathrm{id}\otimes\Lambda)(\sigma_\tau):
\Lambda:A'\to B\text{ is CPTP}\right\}.
```

The construction and order of limits are developed in [attainability](attainability.md). Any continuous entanglement measure that cannot increase under a local channel is therefore bounded by its value on $`\sigma_\tau`$; for a $`d`$-dimensional receiver output this bound is the ideal supremum. The statement is a state envelope, not a communication capacity or a stream of consumable pairs.

Since $`\pi`$ is faithful, $`\sigma_\tau`$ is an invertible receiver-local filtering of the channel's normalized Choi state. It is separable exactly when $`\mathcal E_\tau`$ is entanglement breaking. Thus the fixed-source existence-of-entanglement horizon is the channel's entanglement-breaking time. The finite horizon of a primitive finite-dimensional continuous semigroup is an established theorem; its operational interpretation here follows from the envelope and attainment. See [the causal bound](causal-bound.md) and [related work](../references/RELATED_WORK.md).

## 3. Sharp law for a statically driven emitter

Take a qubit with ground/excited basis $`(|g\rangle,|e\rangle)`$, $`Z=|g\rangle\langle g|-|e\rangle\langle e|`$, and $`\sigma_-=|g\rangle\langle e|`$. Its generator is

```math
\mathcal L_{\Omega,\Delta}(\rho)
=-i\left[\frac{\Omega X+\Delta Z}{2},\rho\right]
+\gamma\mathcal D[\sigma_-](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The decay rate $`\gamma>0`$ is fixed. The drive $`\Omega\ge0`$ and detuning $`\Delta\in\mathbb R`$ are constant during each protocol. They may be chosen differently for each delay. For $`\Omega>0`$ the stationary state is faithful. At $`\Omega=0`$ it is the pure ground state and the stationary entanglement is zero; that boundary is included separately.

Score Wootters concurrence between the source and a designated retained receiver **qubit**, after tracing out any auxiliary memory. Let

```math
C_*(\tau)=\sup_{\Omega\ge0,\,\Delta\in\mathbb R}
C\bigl(\sigma_\tau^{\Omega,\Delta}\bigr),
\qquad
s=2\sqrt{\det\pi}
=\frac{2\Omega^2}{\gamma^2+4\Delta^2+2\Omega^2}.
```

The envelope identifies this with the supremum over all admissible receivers and all static source parameters. A standard matched driven-qubit receiver attains the fixed-source envelope in its late-time limit; see [receiver resources](receiver-resources.md). The main asymptotic is

```math
\boxed{\displaystyle
C_*(\tau)=\left(\frac12+o(1)\right)e^{-\gamma\tau}
\quad\text{as }\gamma\tau\to\infty.}
```

This is uniform over all static detunings and drive strengths, including unbounded delay-dependent sequences. Writing $`a=e^{-\gamma\tau/2}`$, the more informative scaling law is

```math
\frac{s}{a}\longrightarrow k\in[0,\infty)
\quad\Longrightarrow\quad
\frac{C(\sigma_\tau)}{a^2}
\longrightarrow\max\left\{0,k-\frac{k^2}{2}\right\}.
```

If $`s/a\to\infty`$, the delayed state is eventually separable. The parabola has its unique maximum at $`k=1`$. An asymptotically optimal resonant choice is

```math
\Delta=0,
\qquad
\Omega\sim\frac{\gamma}{\sqrt2}e^{-\gamma\tau/4}.
```

The fixed-parameter stationary state, exact finite-delay calculation and channel representation are in [the driven-qubit account](driven-qubit.md). The uniform converse and matching construction are proved in [the long-delay law](long-delay-law.md).

## 4. Limits and resources that change the question

The late-time limit is taken for each fixed delay, source and receiver design before the large-delay limit. A preparation-time constraint would define another optimization. For the general receiver theorem, arbitrarily accurate approximation can require increasing control strengths; no delay-independent engineering budget is asserted. The explicit qubit receiver has its own preparation dynamics.

The optimized source becomes weakly excited. Its stationary photon flux is

```math
\gamma\pi_{ee}=\frac{\gamma s}{2}
\sim\frac\gamma2 e^{-\gamma\tau/2}
```

along an asymptotically optimal sequence. The result therefore does not maintain a fixed brightness while increasing distance. Allowing $`\gamma`$ itself to decrease with delay would change the dimensionless regime; the theorem is a law in $`\gamma\tau`$, not a distance-only impossibility independent of source lifetime.

Stationarity is essential. An initially excited undriven source can become maximally entangled with its past vacuum/one-photon wavepacket after a half-decay time. The additional delay then leaves concurrence $`e^{-\gamma\tau/2}`$, which exceeds the stationary optimized asymptotic. This transient construction is explained in [receiver resources](receiver-resources.md); it is outside the stationary objective.

Incomplete collection, loss or extra inaccessible baths preserve the causal upper-bound argument for the complete purification, but need not permit its attainment. Feedback, time-dependent source control, protected source ancillas and preshared source–receiver entanglement change the assumptions. Postselection can increase concurrence on a normalized successful branch; the deterministic bound applies to unconditional states, while suitable entanglement monotones remain bounded on average. For $`d\ge3`$, nonseparability is not a guarantee of distillability.

## 5. Reading and proof dependencies

| Question | Authoritative account |
|---|---|
| Why can no causal receiver exceed the envelope? | [Causal bound](causal-bound.md) |
| Can a fixed-memory continuous receiver approach it? | [Attainability](attainability.md) |
| What does the physical qubit receiver require? | [Receiver resources](receiver-resources.md) |
| How is the delayed qubit state computed exactly? | [Driven qubit](driven-qubit.md) |
| Why do arbitrary static detunings obey the same sharp asymptotic? | [Long-delay law](long-delay-law.md) |
| Which ingredients are established and what is added here? | [Related work](../references/RELATED_WORK.md) |
| Which finite calculations can be reproduced? | [Verification](../verification/README.md) |
