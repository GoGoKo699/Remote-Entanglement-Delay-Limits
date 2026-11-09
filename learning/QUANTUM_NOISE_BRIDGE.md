# From Quantum Noise to delayed stationary entanglement

A driven atom continually emits into a traveling field. A downstream device can absorb that field and retain quantum information. If the field takes time to arrive, however, the atom continues to evolve while the receiver processes its earlier output. This project asks how much entanglement the **current** atom can retain with that receiver.

The selected educational anchor is **Crispin Gardiner and Peter Zoller, *Quantum Noise*, third edition, Springer, 2004**, hardcover ISBN **978-3-540-22301-6**. Its input-output and cascaded-system framework supplies the physical starting point. This bridge adds the channel and entanglement arguments needed for the project's actual result. It is a route into the [30-milestone map](MILESTONES.md), not a requirement to finish the book first.

The exact scientific statements remain in [the model](../science/model.md), [causal bound](../science/causal-bound.md), [attainability](../science/attainability.md), and [long-delay proof](../science/long-delay-law.md). The explanations below use the repository's conventions throughout.

## Selected source and reading route

The [Springer record](https://link.springer.com/book/9783540223016) verifies the third edition and 2004 hardcover. The section numbers and starting pages below are verified against the [publisher-authorized preview](https://books.google.com.sg/books?id=a_xsT8oGhdgC) with the same ISBN. Page numbers refer to that edition; the later softcover printing has a different ISBN. The table gives topic descriptions rather than reproducing the contents page. No unverified textbook equation numbers are used.

| Source location | Starting page | Connection to this project |
|---|---:|---|
| Chapter 3, Section 3.2 | 51 | Treat damping as an interaction with incoming and outgoing fields. |
| Chapter 3, Section 3.6 | 76 | Connect reduced system evolution to a master equation. |
| Chapter 5, Sections 5.1 and 5.2 | 131, 143 | Identify the Markov assumptions and distinguish states from multitime correlations. |
| Chapter 5, Section 5.4 | 161 | Work with the reduced generator and its dynamical channel. |
| Chapter 9, Section 9.2 | 278 | Establish the driven, radiatively damped two-level source. |
| Chapter 11, Sections 11.1–11.3 | 343, 345, 351 | Relate stochastic evolution, effective drift, and photon-counting descriptions. |
| Chapter 12, Section 12.1 | 398 | Form a directional cascade by feeding one output into another system. |
| Chapter 12, Section 12.3 | 407 | Connect an emitting atom and a downstream atom through a nonclassical field. |

For the physical question, start with Sections 3.2, 5.2 and 12.1. For the explicit qubit calculation, add Section 9.2. For the general continuous receiver, add Chapter 11. The required quantum-information facts are explained below and in the linked project proofs; they are not silently assigned as another textbook prerequisite.

## The physical question

Three facts must be kept separate. A source can have a stationary reduced state while continuously becoming correlated with new output. A directional cascade can have a simple description after shifting the receiver's clock. The entanglement present between both devices at one physical time still depends on what happened to the source during propagation.

The general source has finite dimension $`d`$, a time-independent generator $`\mathcal L`$, and channel $`\mathcal E_t=e^{t\mathcal L}`$. It starts in its faithful stationary state $`\pi`$. Primitivity means

```math
\mathcal E_t(X)\longrightarrow\pi\mathrm{Tr}X.
```

The receiver starts independently, has no feedback or faster source-information path, and processes only output that has arrived. Tightness assumes coherent collection of every output of a pure-input Markov dilation with the same deterministic delay $`\tau`$. The scored state is unconditional. A retained receiver qubit is specified when using ordinary two-qubit concurrence.

For each fixed source and delay, an ideal finite-memory receiver can approach one state arbitrarily closely at sufficiently late times. For the driven qubit, a matched receiver qubit reaches the corresponding optimum in its stationary limit. The large-delay optimization is performed **after** this late-time preparation, with the decay rate fixed. These are distinct limiting statements.

This is the integrated setting of [M01–M12](MILESTONES.md#m01). The book supplies the open-system language; the receiver-universal question requires the additional reasoning in [M13–M30](MILESTONES.md#m13).

## Notation and conventions

Matching physical coefficients is more reliable than matching letters across accounts. The following dictionary fixes the convention used in every equation here. The translation rules apply when reading an equivalent textbook formula; they do not assume that every chapter uses the same rate symbol.

| Object | Repository convention | Translation or check |
|---|---|---|
| State and reduced state | $`\rho_{AB}`$, $`\rho_A=\mathrm{Tr}_B\rho_{AB}`$ | Tracing out a field removes access to it; it does not say the field was uncorrelated with the source. |
| Dissipator | $`\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$ | A formula $`\kappa(2c\rho c^\dagger-\{c^\dagger c,\rho\})`$ equals $`\mathcal D[\sqrt{2\kappa}\,c](\rho)`$. |
| Emission rate | $`L=\sqrt\gamma\,\sigma_-`$ | With no drive, excited population decays at rate $`\gamma`$ and atomic coherence at rate $`\gamma/2`$. |
| Atomic inversion | $`Z=\mathrm{diag}(1,-1)`$ in the ground/excited basis | A convention with positive excited-state inversion uses $`-Z`$. Translate the detuning sign with it. |
| Drive | $`H=(\Omega X+\Delta Z)/2`$ | If an account writes its resonant drive as $`\Omega'X`$, then $`\Omega=2\Omega'`$. |
| Propagation and operation | $`\tau`$ is delay; $`t`$ is physical time; $`u=t-\tau`$ is the latest accessible source time | The symbol $`t`$ in the specialist long-delay proof denotes channel duration, hence propagation delay in its application. |
| Effective drift | $`K=-iH-\tfrac12\sum_jL_j^\dagger L_j`$ | This is the drift between jumps in a trajectory representation. Using it algebraically does not mean postselecting a no-count outcome. |
| Purification | $`\lvert C\rangle\!\rangle=\sum_{jk}C_{jk}\lvert j\rangle\lvert k\rangle`$ | $`(A\otimes B)\lvert C\rangle\!\rangle=\lvert ACB^T\rangle\!\rangle`$; the transpose fixes receiver signs and copy-basis conventions. |
| Source mixedness | $`s=2\sqrt{\det\pi}`$ for a qubit | This is its purification concurrence, not its excited population or the small eigenvalue of $`\pi`$. |

The source Hamiltonian is expressed in a rotating frame, with $`\hbar=1`$. A known propagation phase can be absorbed into receiver operators. It does not remove propagation time.

## From fields to channels

The field interpretation in Sections 3.2 and 5.4 makes an essential distinction: irreversible **reduced** evolution can arise from a reversible interaction with a larger field. A receiver that collects the output accesses part of that larger system.

For the vacuum input-output representation used in the continuous proof, write the input increment as $`dB_j(t)`$. Its vacuum Itô rule is

```math
dB_j\,dB_k^\dagger=\delta_{jk}\,dt,
\qquad dB_j^\dagger dB_k=0.
```

With identity scattering, choose the unitary evolution convention

```math
dU_t=\left[
\sum_j\bigl(L_j\,dB_j^\dagger-L_j^\dagger\,dB_j\bigr)
-\left(iH+\frac12\sum_jL_j^\dagger L_j\right)dt
\right]U_t.
```

Tracing the field gives the repository's Lindblad generator. In the same convention, the boundary relation is $`dB_{{\rm out},j}=dB_{{\rm in},j}+L_j(t)dt`$. These equations are local explanations in repository notation, not quotations or equation-number translations from the book.

The important Markov assumption is independence of future input increments from the source and past output. It does **not** require the source to be independent of its earlier radiation. The old radiation is precisely where the receiver's useful quantum information resides.

### A complete rate check

Set $`H=0`$ and $`L=\sqrt\gamma\,|g\rangle\langle e|`$. Direct evaluation of the dissipator gives

```math
\frac{d\rho_{ee}}{dt}=-\gamma\rho_{ee},
\qquad
\frac{d\rho_{ge}}{dt}=-\frac\gamma2\rho_{ge}.
```

Thus one propagation interval multiplies an atomic coherence by $`a=e^{-\gamma\tau/2}`$, while an excited population is multiplied by $`a^2`$. Confusing these rates would change the headline exponent. The final stationary optimum also scales as $`a^2`$, but that result requires source optimization; the two differential equations alone do not prove it.

### A cascade is directional

For source coupling $`L_A`$ and receiver coupling $`L_B`$, the zero-delay cascade has combined jump

```math
J=L_A\otimes I+I\otimes L_B
```

and Hamiltonian

```math
H_{AB}=H_A\otimes I+I\otimes H_B
+\frac{L_A\otimes L_B^\dagger-L_A^\dagger\otimes L_B}{2i}.
```

The cross Hamiltonian and the cross terms in $`\mathcal D[J]`$ must be considered together. Tracing out the receiver then recovers the source's original generator. Keeping the cross Hamiltonian alone would describe a different physical interaction and can suggest spurious feedback. Section 12.1 is the anchor for this connection; the implemented conventions are checked in [attainability](../science/attainability.md#an-autonomous-matched-qubit-receiver).

## From a delayed field to a universal state

Sections 5.2 and 12.1 prepare the time bookkeeping. Suppose the receiver is observed at physical time $`t=u+\tau`$. Its input comes from source times through $`u`$. During the interval $`(u,u+\tau]`$, the source interacts with fresh input that the receiver cannot yet access.

In the dilation, the receiver's processing of old output commutes with that last interval of source evolution. Consequently,

```math
\rho_{AB}(u+\tau)
=(\mathcal E_\tau\otimes\mathrm{id}_B)(\omega_{AB}),
\qquad \omega_A=\pi.
```

The state $`\omega_{AB}`$ includes everything the receiver has accomplished using the accessible output. This is the causal cut. It does not depend on the receiver being an atom, on its controls being constant, or on its internal memory being small.

### The missing quantum-information step

A purification represents a mixed state as part of a pure state on a larger system. For a qubit with stationary eigenvalues $`q,p`$, one such state is

```math
|\phi_\pi\rangle=\sqrt q\,|00\rangle+\sqrt p\,|11\rangle.
```

Its source marginal is $`\pi`$. More generally, use $`\Phi_\pi=|\sqrt\pi\rangle\!\rangle\langle\!\langle\sqrt\pi|`$ in any fixed basis. Every joint state with source marginal $`\pi`$ can be produced by applying a channel to this purifying register. One way to prove this is to purify that joint state once more, relate the two purifications by an isometry on the added registers, and then discard the extra register. The [causal proof](../science/causal-bound.md#theorem-domination-by-one-delayed-channel-state) gives the complete argument.

Applying it at the cut gives a receiver-local channel $`\Lambda_t`$ such that

```math
\rho_{AB}(t)
=(\mathrm{id}\otimes\Lambda_t)(\sigma_\tau),
\qquad
\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id})(\Phi_\pi).
```

This moves the optimization over physical receivers into a local-processing relation between states. Any entanglement measure that cannot increase under deterministic local channels is bounded by its value on $`\sigma_\tau`$. The state relation is exact at each time; equality of optimal values still needs a receiver construction.

### Why the horizon is an entanglement-breaking time

An entanglement-breaking channel produces a separable state with every untouched reference, for every input. Its normalized Choi state is obtained by applying the channel to half a maximally entangled pair. Since $`\pi`$ is faithful, the canonical stationary purification is an **invertible local filter** of that pair. The filtered Choi state is $`\sigma_\tau`$. Invertible local filtering preserves separability in both directions, so

```math
\sigma_\tau\text{ separable}
\quad\Longleftrightarrow\quad
\mathcal E_\tau\text{ entanglement breaking}.
```

The Choi criterion and eventual entanglement breaking of primitive finite-dimensional semigroups are imported research ingredients, identified in [related work](../references/RELATED_WORK.md). The project's operational step is to show that an admissible receiver can approach the state on the other side of this bound. Nonseparability before the horizon is an entanglement-existence statement; in higher dimensions it is not automatically a distillability statement.

## From a purification to a physical receiver

Chapter 12 suggests coherent absorption: choose a downstream device so that the outgoing field loses the correlations of interest while its memory gains them. Finding a pure dark state is only one part of this task. The receiver must begin independently, and the proposed state must be approached by allowed dynamics.

### Why a memory of dimension d squared is sufficient

Introduce a mathematical reference $`R`$ of dimension $`d`$ that purifies the source's initial $`\pi`$. It is not supplied to the receiver. The reduced state on $`AR`$ after source time $`u`$ is

```math
\chi_u=(\mathcal E_u\otimes\mathrm{id}_R)(\Phi_\pi),
\qquad
\chi_u\longrightarrow\pi\otimes\pi^T.
```

A memory $`M=C\otimes R'`$, of dimension $`d^2`$, can purify this entire $`AR`$ state. In a collision model, after each source emission the receiver applies a unitary to its memory and the newly arrived unit, placing the emitted unit in a fixed pure state while keeping the purification in memory. Equality of the two $`AR`$ marginals guarantees that such a unitary exists. This is the sequential purification mechanism; the [resource account](../science/receiver-resources.md#appendix-an-exact-collision-model-construction) gives its induction.

At late times, the desired purification of $`\pi\otimes\pi^T`$ factorizes into a purification of the current source on $`AC`$ and a separate state on $`RR'`$. The auxiliary factor $`R'`$ therefore has a concrete role: it retains the initial-reference information while $`C`$ becomes the useful output. The count $`d^2`$ is sufficient, not claimed minimal.

### What a continuous implementation must add

Time-bin compression by itself does not establish a continuous receiver with controlled coefficients. The continuous construction regularizes a rank-deficient starting point. Choose $`\delta>0`$ and set

```math
W_u=\sqrt{\chi_{u+\delta}}.
```

The symbol $`W_u`$ here is the matrix called $`C_u`$ in the specialist proof; the register $`C`$ remains the designated receiver output. For a primitive source, $`\chi_v>0`$ for every $`v>0`$. Analyticity and the full-rank limiting state provide an earlier positive time, and the invertible no-jump part of Lindblad evolution propagates strict positivity forward. This justifies the inverse in the receiver formulas.

On the mathematical source $`S=AR`$, define

```math
V_j=L_j\otimes I_R,
\qquad K=\left(-iH-\frac12\sum_jL_j^\dagger L_j\right)\otimes I_R,
\qquad F_u=\sum_jV_j\chi_{u+\delta}V_j^\dagger.
```

The local receiver coefficients are

```math
\begin{aligned}
J_j(u)&=-\bigl(W_u^{-1}V_jW_u\bigr)^T,\\
Q(u)&=W_u^{-1}\bigl(\dot W_u-KW_u-F_uW_u^{-1}\bigr),\\
K_M(u)&=Q(u)^T,\\
H_M(u)&=\frac{i}{2}\bigl(K_M(u)-K_M(u)^\dagger\bigr).
\end{aligned}
```

Two checks make these more than formal inverse matrices. First,

```math
K_M+K_M^\dagger=-\sum_jJ_j^\dagger J_j,
```

so they define a physical Lindblad receiver. Second, each total cascade jump annihilates $`|W_u\rangle\!\rangle`$, while the total effective drift maps it to $`|\dot W_u\rangle\!\rangle`$. Chapter 11's trajectory language thus becomes a useful algebraic tool for verifying an **unconditional** moving pure state. No measurement outcome is selected.

The comparison state at $`u=0`$ is correlated across source and receiver, but it is not required as a resource. The actual initial receiver state is the known local pure state that purifies $`\chi_0`$ canonically; because $`\chi_0`$ itself is pure, that canonical purification factorizes across $`AR:M`$. As $`\delta\to0`$, the actual and comparison initial states become close. Contractivity of their common dynamics keeps them close thereafter.

The resulting physical-time estimate is

```math
\begin{aligned}
\|\rho_{AC}(u+\tau)-\sigma_\tau\|_1
\le{}&2\sqrt{\|\chi_\delta-\Phi_\pi\|_1}\\
&+2\sqrt{\|\chi_{u+\delta}-\pi\otimes\pi^T\|_1}.
\end{aligned}
```

The first term is made small by selecting a receiver design; the second becomes small by waiting. For each fixed accuracy the coefficients are bounded and continuous. A common bound as accuracy tends to zero is not proved. This establishes the general **supremum** of every continuous deterministic entanglement monotone on a source and an equally sized output. The [full continuous proof](../science/attainability.md#a-continuous-purification-tracker) supplies the positivity, drift and initialization details.

### Why the driven qubit permits a simpler receiver

For $`H_A=(\Omega X+\Delta Z)/2`$ and $`L_A=\sqrt\gamma\,\sigma_-`$, choose a receiver qubit with the same drive amplitude and coupling, and opposite detuning. The aligned cascade has the dark state

```math
|D\rangle=
\frac{|gg\rangle+\alpha|S\rangle}{\sqrt{1+|\alpha|^2}},
\qquad
|S\rangle=\frac{|eg\rangle-|ge\rangle}{\sqrt2},
\qquad
\alpha=\frac{\sqrt2\,\Omega}{2\Delta+i\gamma}.
```

This is the established coherent-absorber dimer of Stannigel, Rabl and Zoller, translated into the repository convention. Its source marginal is $`\pi`$. The project also gives an explicit attraction proof, so the state is reached from an independent receiver start in the stationary limit. The physical simultaneous state is $`(\mathcal E_\tau\otimes\mathrm{id})(|D\rangle\langle D|)`$, locally equivalent to $`\sigma_\tau`$. This exact qubit limit is stronger than the general regularized approximation statement.

## From optical Bloch equations to the optimal source

Section 9.2 provides the atomic setting. Write the source state as $`\rho=(I+r\cdot\sigma)/2`$. The repository generator gives

```math
\dot r=A r+\gamma e_z,
\qquad
A=\begin{pmatrix}
-\gamma/2&-\Delta&0\\
\Delta&-\gamma/2&-\Omega\\
0&\Omega&-\gamma
\end{pmatrix}.
```

Solving the three stationary equations gives, with $`D=\gamma^2+4\Delta^2+2\Omega^2`$,

```math
r_\pi=\frac1D(4\Delta\Omega,-2\gamma\Omega,\gamma^2+4\Delta^2)^T,
\qquad
s=2\sqrt{\det\pi}=\frac{2\Omega^2}{D}.
```

For $`\Omega>0`$ the stationary state is faithful. At $`\Omega=0`$ it is the pure ground state and its stationary source–receiver concurrence is zero. The faithful-state horizon argument is not applied to that boundary; the undriven amplitude-damping channel itself is not entanglement breaking at any finite time.

There are two different small probabilities. The physical excited population is $`\pi_{ee}=s/2`$, whereas the small eigenvalue of the stationary density matrix is

```math
p=\frac{1-\sqrt{1-s^2}}2\sim\frac{s^2}{4}.
```

A weak coherent drive therefore produces a state that is closer to pure than its excited population alone suggests. Its two-qubit purification has concurrence $`s`$. This is the source's supply of entanglement at the causal cut.

### The exact fixed-source score

Let $`J_\tau=(\mathcal E_\tau\otimes\mathrm{id})(|\Phi^+\rangle\langle\Phi^+|)`$, with $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$. The pure-input concurrence factorization law gives

```math
C(\sigma_\tau)=s\,C(J_\tau).
```

This imported identity separates the concurrence of the initial purification from the channel's action on it. It does not let one optimize the two factors independently: both are determined by the **same** source generator. The causal theorem and receiver construction are what make this two-qubit calculation an operational optimum. The exact finite-delay channel is given in [the driven-qubit account](../science/driven-qubit.md#finite-delay-evaluation).

### Why arbitrary detuning is a genuine proof issue

The Bloch generator obeys $`A+A^T=-\gamma\mathrm{diag}(1,1,2)`$, hence $`\|e^{\tau A}\|_2\le a`$ with $`a=e^{-\gamma\tau/2}`$. That contraction bound alone does not establish the sharp stationary law. The proof also uses how the stationary direction is tied to the generator.

In coordinates with one axis along $`r_\pi`$, the longitudinal-to-transverse and transverse-to-longitudinal blocks are asymmetric. When $`s`$ is small, the corresponding propagator bounds have different orders, with constants uniform in detuning:

```math
\|T_{u\perp}\|=O(s^{3/2}a),
\qquad
\|T_{\perp u}\|=O(s^{1/2}a),
\qquad T=e^{\tau A}.
```

Here the subscript $`u`$ labels the stationary spatial axis, not operating time. A weighted similarity transform makes the cross couplings antisymmetric and keeps the detuning term as a rotation. The estimates are therefore uniform in its frequency, including detunings chosen to grow with $`\tau`$. A small-detuning expansion or a bounded numerical search would not supply that conclusion. See [Sections 2–4 of the proof](../science/long-delay-law.md#2-geometry-of-the-stationary-state).

### How the coefficient one half appears

For sequences with $`s/a\to k<\infty`$, an analytic local filter isolates the small entries that determine concurrence. In the stationary eigenbasis, after a local phase adjustment, put

```math
F_a=\mathrm{diag}(a,1),
\qquad
M_\tau=a^{-4}(F_a\otimes F_a)\sigma_\tau(F_a\otimes F_a).
```

The uniform estimates imply

```math
M_\tau\longrightarrow
\begin{pmatrix}
1&0&0&k/2\\
0&k^2/4&0&0\\
0&0&k^2/4&0\\
k/2&0&0&k^2/4+k^4/16
\end{pmatrix}.
```

Homogeneous concurrence scales by the product of local filter determinants. Thus $`C(M_\tau)=a^{-2}C(\sigma_\tau)`$. The limit has coherence $`k/2`$ competing with the two middle populations $`k^2/4`$, giving

```math
\frac{C(\sigma_\tau)}{a^2}
\longrightarrow f(k)=\max\{0,k-k^2/2\}.
```

The filtering is a proof device, not a successful branch of a physical receiver protocol. The state being optimized remains unconditional. The missing global step is also essential: sequences with $`s/a\to\infty`$ are proved eventually separable. Only after that exclusion can the finite-ratio parabola control the supremum over every static source.

Its unique maximum is $`f(1)=1/2`$. Therefore

```math
\sup_{\Omega\ge0,\;\Delta\in\mathbb R,\;\text{causal receivers}}
C
=\left(\frac12+o(1)\right)e^{-\gamma\tau},
\qquad \gamma>0\text{ fixed}.
```

All asymptotically optimal source sequences have $`s/a\to1`$. On resonance, one exact tuning is

```math
\Omega^2=\frac{\gamma^2a}{2(1-a)},
```

which makes $`s=a`$ for each positive delay. In particular, $`\Omega\sim(\gamma/\sqrt2)e^{-\gamma\tau/4}`$. This establishes a matching asymptotic construction. It does not assert that resonance is the unique optimizer, or an exact global optimizer at every finite delay.

## Scope through two worked comparisons

### Comparing sources at the same large delay

The finite-ratio law compares different static sources on one common scale:

| Limiting ratio $`k=s/a`$ | Limiting $`C/a^2`$ | Interpretation |
|---:|---:|---|
| $`1/2`$ | $`3/8`$ | The source supplies too little initial purification concurrence to reach the optimum. |
| $`1`$ | $`1/2`$ | Supply and delay-induced degradation have the optimal balance. |
| $`3/2`$ | $`3/8`$ | The increase in stationary source mixedness has already reduced the eventual score. |
| $`3`$ | $`0`$ | The stricter partial-transpose argument makes such a sequence eventually separable. |

The case $`k=2`$ has zero leading concurrence but lies exactly at the limiting boundary; the leading term alone does not decide finite-delay separability there. For fixed small nonzero $`s`$, the sharper horizon result is

```math
\gamma\tau_{\rm EB}=2\log(2/s)+o(1),\qquad s\to0.
```

Retuning the source extends that horizon by making its stationary state nearly pure. It also reduces the exact photon flux:

```math
\mathcal F=\gamma\pi_{ee}=\frac{\gamma s}{2}
\sim\frac\gamma2e^{-\gamma\tau/2}.
```

This is a state-quality and brightness tradeoff. It does not supply an independent pair every time a photon is emitted, or bound a repeated-use entanglement production rate.

### Comparing stationary and transient operation

Initialize an undriven source in $`|e\rangle`$. At time $`u`$ it is entangled with the vacuum/one-photon subspace of its emitted field:

```math
|\Psi(u)\rangle
=\sqrt p\,|e,0\rangle+\sqrt{1-p}\,|g,1_{f_u}\rangle,
\qquad p=e^{-\gamma u}.
```

At $`u=(\log2)/\gamma`$, this is a maximally entangled pair between source and an effective field qubit. A receiver with coherent mode access can approach a qubit encoding of that past field. Meanwhile the source undergoes an additional amplitude-damping interval $`\tau`$. Its equal-time concurrence becomes

```math
C=2e^{-\gamma\tau/2}\sqrt{p(1-p)}
=e^{-\gamma\tau/2}
\quad\text{at }p=1/2.
```

This is larger than the stationary optimum at large delay. The causal cut still applies, but its source marginal is the transient state at time $`u`$, not the stationary ground state. The [resource account](../science/receiver-resources.md#why-stationarity-matters-an-explicit-transient-example) gives a continuous bounded-control approximation to the capture. This comparison identifies why stationarity is a controlling assumption rather than merely a convenient way to solve the equations.

The other controlling boundaries are equally physical. Loss or an inaccessible bath can reduce attainability. Feedback or a faster source-dependent signal changes the cut. Allowing the source decay rate to shrink with distance changes $`\gamma\tau`$. Conditioning on a successful measurement changes the numerical score. The [model](../science/model.md#4-limits-and-resources-that-change-the-question) states these boundaries together.

## What comes from where

The selected book is the single educational anchor. The primary research sources below establish imported ingredients or nearby physical models; they do not form an additional prerequisite curriculum.

| Layer | Role in the argument | Authoritative route |
|---|---|---|
| Textbook foundations | Input-output fields, Markov master equations, multitime bookkeeping, two-level atoms, trajectories and cascades | The verified *Quantum Noise* sections above |
| Standard channel reasoning, explained locally | Purification, channels on a purifying register, and the passage from a causal cut to local state processing | [Causal bound](../science/causal-bound.md) |
| Imported entanglement ingredients | Concurrence and its factorization; separability of the Choi state; eventual entanglement breaking | Wootters, Konrad et al., Horodecki–Shor–Ruskai, and Hanson–Rouzé–Stilck França, cited in [related work](../references/RELATED_WORK.md) |
| Existing receiver mechanisms | The matched dark dimer; sequential decoders and reverser constructions | [Stannigel et al. (2012)](https://doi.org/10.1088/1367-2630/14/6/063014), [Yang et al. (2023)](https://doi.org/10.1103/PhysRevX.13.031012), and [Tsang (2025)](https://doi.org/10.22331/q-2025-02-26-1650) |
| Close established physical and mathematical connections | Delay-dependent simultaneous entanglement, driven-channel sudden death, and the transfer-channel cut in matrix-product states | Agustí et al. (2022, with 2025 erratum), Goyal et al. (2012), and Ferydouni et al. (2026), compared in [related work](../references/RELATED_WORK.md) |
| Local operational derivations | The receiver-universal envelope, exact channel horizon under full collection, continuous mixed-start regularization, and explicit qubit attraction | [Causal bound](../science/causal-bound.md), [attainability](../science/attainability.md) |
| Local quantitative result | The detuning-uniform scaling law, global coefficient $`1/2`$, optimal retuning, and sharp weak-source horizon | [Long-delay law](../science/long-delay-law.md) |

“Locally derived” identifies where a statement is proved in this repository. It does not claim every lemma or mechanism is new. In particular, coherent absorption, finite-delay entanglement loss, concurrence factorization, and eventual entanglement breaking are established ingredients. The research comparison concerns the attainable operational frontier and the uniform optimization of this specific stationary source family.

## Proof and reproduction routes

The [milestone map](MILESTONES.md) connects local objects into the full physical story. Its background phase ends with the model in [M12](MILESTONES.md#m12); the narrative phase closes with the contribution and its boundaries in [M30](MILESTONES.md#m30).

For the causal argument, follow [M13–M17](MILESTONES.md#m13) with the causal and attainability pages. For the explicit receiver and exact qubit score, follow [M18–M20](MILESTONES.md#m18). For the uniform proof, follow [M21–M28](MILESTONES.md#m21); the analytic estimates and limiting argument are necessary even though the final parabola is simple. [M29](MILESTONES.md#m29) returns the mathematics to resources and alternative physical tasks.

The [verification guide](../verification/README.md) supplies the commands and tested scope. Independent channel representations and high-precision concurrence checks help detect wrong signs, factors and numerical cancellation. They do not establish a uniform theorem by sampling detunings, and this bridge does not replace the full proof with such a computation.
