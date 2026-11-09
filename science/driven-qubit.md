# Stationary driven-qubit source

A coherently driven, radiatively damped qubit has an exact stationary entanglement frontier across a one-way propagation delay. For a fixed source, optimizing every causal receiver is equivalent to evaluating one two-qubit state. Optimizing the static source parameters then gives the sharp long-delay law proved in [long-delay-law.md](long-delay-law.md).

## Model and operational scope

The source qubit is $`A`$. Its ground and excited states are $`|0\rangle`$ and $`|1\rangle`$, with

```math
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\sigma_-=|0\rangle\langle1|.
```

In particular, the physical relaxation axis is the positive $`Z`$ axis. Define $`\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$. The source generator is

```math
\mathcal L_{\Omega,\Delta}(\rho)
=-i\left[\frac{\Omega X+\Delta Z}{2},\rho\right]
+\gamma\mathcal D[\sigma_-](\rho),
\qquad \gamma>0,\quad\Omega\ge0,\quad\Delta\in\mathbb R.
```

The drive amplitude and detuning are constant during operation. They may be chosen separately for each propagation delay $`\tau`$; the decay rate $`\gamma`$ is fixed. A constant drive phase can be absorbed into a rotation about $`Z`$.

The output field is the complete vacuum output associated with the coupling operator $`\sqrt\gamma\,\sigma_-`$. It travels one way to a downstream receiver after delay $`\tau`$. The receiver has no feedback to the source, no access to the field still in flight, and no faster communication path. Source and receiver begin without shared entanglement. The source is evaluated in stationary operation.

The scored subsystem is a **designated receiver qubit** $`B`$. Arbitrary local ancillary systems and deterministic causal processing are allowed, but the ancillary systems and any unreported records are traced out before evaluating $`C(\rho_{AB})`$. The score is the concurrence of this unconditional two-qubit state. A postselected ensemble or entanglement with the receiver's entire memory would define a different score.

These assumptions do not optimize over transient excitation of the source, pulsed source control, changes in $`\gamma`$, additional source decay channels, intermediate repeaters, or multiple independent source qubits. In particular, the stationary result below is not a bound on all transient emission protocols.

## Stationary state and its purification concurrence

Let

```math
D=\gamma^2+4\Delta^2+2\Omega^2.
```

Solving $`\mathcal L(\pi)=0`$ gives

```math
\pi=\frac1D
\begin{pmatrix}
\gamma^2+4\Delta^2+\Omega^2&\Omega(2\Delta+i\gamma)\\
\Omega(2\Delta-i\gamma)&\Omega^2
\end{pmatrix}.
```

Its Bloch vector and determinant are

```math
r_\pi=\frac1D
\begin{pmatrix}
4\Delta\Omega\\-2\gamma\Omega\\\gamma^2+4\Delta^2
\end{pmatrix},\qquad
\det\pi=\frac{\Omega^4}{D^2}.
```

The useful dimensionless source parameter is

```math
s:=2\sqrt{\det\pi}
=\frac{2\Omega^2}{D}.
```

This is the concurrence of any two-qubit purification of $`\pi`$. For finite parameters, $`0\le s<1`$. The state is faithful when $`\Omega>0`$. If $`\Omega=0`$, it is the pure ground state and the stationary source cannot be entangled with any receiver.

Write its eigenvalues as $`q=1-p`$ and $`p\le1/2`$, where

```math
p=\frac{1-\sqrt{1-s^2}}2
=\frac{s^2}{2(1+\sqrt{1-s^2})}.
```

The second expression is numerically preferable near $`s=0`$. The small eigenvalue is $`p\sim s^2/4`$; it is distinct from the excited-state population in the physical basis, which is $`\pi_{11}=s/2`$.

## Exact stationary receiver frontier

Let $`\mathcal E_\tau=e^{\tau\mathcal L}`$, and define the normalized canonical purification and the delayed state

```math
|\sqrt\pi\rangle
=\sum_{i,j=0}^1(\sqrt\pi)_{ij}|i\rangle_A|j\rangle_R,
\qquad
\sigma_\tau
=(\mathcal E_\tau\otimes\operatorname{id}_R)
\bigl(|\sqrt\pi\rangle\langle\sqrt\pi|\bigr).
```

The reference $`R`$ is a qubit, and its marginal is $`\pi^T`$. In the stationary eigenbasis, the purification is simply $`\sqrt q\,|00\rangle+\sqrt p\,|11\rangle`$.

Denote the supremum of the stationary designated-qubit score over admissible receivers by $`\mathfrak C_\tau(\Omega,\Delta)`$. The causal bound and attainability results give

```math
\boxed{\mathfrak C_\tau(\Omega,\Delta)=C(\sigma_\tau).}
```

The [causal-bound.md](causal-bound.md) argument implies that every attainable state has the form

```math
\rho_{AB}
=(\mathcal E_\tau\otimes\Lambda)
\bigl(|\sqrt\pi\rangle\langle\sqrt\pi|\bigr)
```

for a qubit-to-qubit CPTP map $`\Lambda:R\to B`$. This follows by cutting the field at the receiver's most recent accessible emission time: the receiver is an extension of the stationary source state at that cut, and every such extension is obtained from a purification by a channel on its purifying system. Source evolution over the inaccessible interval applies $`\mathcal E_\tau`$ to $`A`$. Monotonicity of concurrence under the local channel $`\Lambda`$ gives the upper bound. The [attainability.md](attainability.md) construction supplies the reverse inequality; the explicit matched receiver for this source is described in [receiver-resources.md](receiver-resources.md).

This distinction matters: the finite-dimensional calculation of $`C(\sigma_\tau)`$ alone would provide an upper bound without the receiver-attainment result.

### Choi-state formula

Let

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},\qquad
J_\tau=(\mathcal E_\tau\otimes\operatorname{id})
\bigl(|\Phi^+\rangle\langle\Phi^+|\bigr).
```

Then

```math
\boxed{\mathfrak C_\tau(\Omega,\Delta)=s\,C(J_\tau).}
```

This is the pure-input concurrence factorization law [2]. It also follows directly from the local-filter identity proved in [long-delay-law.md](long-delay-law.md): in the eigenbasis of $`\pi`$, apply $`\operatorname{diag}(\sqrt{2q},\sqrt{2p})`$ to the reference half of $`J_\tau`$. Its determinant is $`s`$, and the resulting state is normalized because the reference marginal of $`J_\tau`$ is $`I/2`$.

For an unnormalized positive two-qubit matrix $`W`$, use homogeneous concurrence, $`C(W)=\operatorname{tr}(W)C(W/\operatorname{tr}W)`$. Wootters' formula [1] is

```math
\widetilde W=(Y\otimes Y)W^*(Y\otimes Y),\qquad
C(W)=\max\{0,\lambda_1-\lambda_2-\lambda_3-\lambda_4\},
```

where $`\lambda_1\ge\cdots\ge\lambda_4\ge0`$ are the eigenvalues of the positive matrix $`\sqrt{\sqrt W\,\widetilde W\,\sqrt W}`$.

## Finite-delay evaluation

In the physical Bloch basis, $`\rho=(I+r\cdot\sigma)/2`$ obeys

```math
\dot r=A r+\gamma e_z,\qquad
A=\begin{pmatrix}
-\gamma/2&-\Delta&0\\
\Delta&-\gamma/2&-\Omega\\
0&\Omega&-\gamma
\end{pmatrix}.
```

Set $`T_\tau=e^{\tau A}`$ and $`c_\tau=(I-T_\tau)r_\pi`$. The exact normalized Choi matrix is

```math
J_\tau=\frac14\left[
I\otimes I+(c_\tau\cdot\sigma)\otimes I
+\sum_{i,j=x,y,z}(T_\tau)_{ij}\,\sigma_i\otimes\sigma_j^T
\right].
```

The transpose on the second Pauli operator is essential: $`Y^T=-Y`$. This formula and $`sC(J_\tau)`$ suffice to evaluate the exact frontier at every finite delay. They do not imply that resonance is globally optimal at every finite delay; the global optimization proved here is asymptotic.

### A finite entanglement-breaking horizon for each driven source

The symmetric part of $`A`$ gives

```math
A+A^T=-\gamma\operatorname{diag}(1,1,2),\qquad
\|T_\tau\|_2\le a:=e^{-\gamma\tau/2}.
```

For $`\Omega>0`$, $`\sigma_\tau`$ is an invertible local filtering of $`J_\tau`$. It is therefore separable exactly when $`J_\tau`$ is separable, equivalently when $`\mathcal E_\tau`$ is entanglement breaking [3,4].

There is an explicit, deliberately loose finite-time bound. Let $`\Gamma_R`$ denote partial transpose on the reference. Since $`c_\tau-r_\pi=-T_\tau r_\pi`$,

```math
\left\|J_\tau^{\Gamma_R}-\pi\otimes\frac I2\right\|_\infty
\le\frac{\|T_\tau r_\pi\|_2+\|T_\tau\|_*}{4}
\le a\frac{|r_\pi|+3}{4}\le a.
```

Here $`\|T\|_*`$ is the sum of its three singular values. The first inequality follows by decomposing the real matrix $`T`$ into singular vectors; each corresponding product of unit-length Pauli operators has operator norm one. Thus $`J_\tau^{\Gamma_R}\ge0`$ whenever $`a\le p/2`$. The two-qubit PPT criterion [3] yields

```math
\tau_{\mathrm{EB}}
:=\inf\{t\ge0:\mathcal E_t\text{ is entanglement breaking}\}
\le\frac2\gamma\log\frac2p<\infty.
```

Composition with later source evolution preserves the entanglement-breaking property. Consequently no admissible receiver can recover source–receiver entanglement beyond this fixed-source horizon, even with arbitrary downstream auxiliaries. The sharp weak-source asymptotic of this horizon is substantially smaller and is proved in [long-delay-law.md](long-delay-law.md).

## Long-delay consequence and its mechanism

In stationary operation,

```math
\sup_{\Omega\ge0,\;\Delta\in\mathbb R}
\mathfrak C_\tau(\Omega,\Delta)
=\left(\frac12+o(1)\right)e^{-\gamma\tau}.
```

Every asymptotically optimal source satisfies

```math
s\sim e^{-\gamma\tau/2},\qquad
\frac{\Omega^2}{\gamma^2+4\Delta^2}
\sim\frac12e^{-\gamma\tau/2}.
```

On resonance, this is $`\Omega\sim(\gamma/\sqrt2)e^{-\gamma\tau/4}`$. The full proof permits detuning to grow with delay and therefore excludes a detuning-dependent improvement in the leading coefficient.

The balance is between the source's stationary purification concurrence and the noise acquired during the inaccessible propagation interval. In the relevant limit, their combined effect is

```math
\mathfrak C_\tau
=a^2\left[k-\frac{k^2}{2}+o(1)\right]_+,
\qquad k=\frac{s}{a},\qquad a=e^{-\gamma\tau/2},
```

for convergent finite $`k`$. The maximum occurs at $`k=1`$. At fixed source parameters, the state eventually becomes exactly separable; maintaining a nonzero frontier at successively longer delays requires retuning the stationary source toward its pure ground state.

## Reproducible verification

Run the high-precision checks from the repository root:

```bash
python -m pip install -r requirements-verification.txt
python verification/verify_driven_qubit.py
```

The script compares the physical four-dimensional Liouvillian against independently constructed Bloch and stationary-axis expressions, verifies the finite-time estimates, checks the local-filter and Choi factorizations, and reports the approach to the predicted long-delay limit. It uses arbitrary precision and a Hermitian/SVD formulation of concurrence. Direct double-precision eigenvalues of $`W\widetilde W`$ can misidentify tiny roots in this regime and produce false improvements.

## Relation to earlier channel dynamics

Driven-qubit sudden death and the resonant channel/Choi calculation are established results. Goyal, Banerjee, and Ghosh [5, Section V] use concurrence factorization and study how resonant driving changes sudden-death times. The present calculation uses those channel-theoretic ingredients inside a stationary delayed-receiver optimization. The causal receiver envelope, its attainable interpretation, and the uniform optimization over static source parameters are separate claims from the existence of driven-qubit sudden death.

## References

1. W. K. Wootters, “Entanglement of Formation of an Arbitrary State of Two Qubits,” *Physical Review Letters* **80**, 2245–2248 (1998). [DOI](https://doi.org/10.1103/PhysRevLett.80.2245).
2. T. Konrad et al., “Evolution equation for quantum entanglement,” *Nature Physics* **4**, 99–102 (2008). [DOI](https://doi.org/10.1038/nphys885).
3. M. Horodecki, P. Horodecki, and R. Horodecki, “Separability of mixed states: necessary and sufficient conditions,” *Physics Letters A* **223**, 1–8 (1996). [DOI](https://doi.org/10.1016/S0375-9601(96)00706-2).
4. M. Horodecki, P. W. Shor, and M. B. Ruskai, “Entanglement Breaking Channels,” *Reviews in Mathematical Physics* **15**, 629–641 (2003). [arXiv](https://arxiv.org/abs/quant-ph/0302031).
5. S. K. Goyal, S. Banerjee, and S. Ghosh, “Effect of control procedures on the evolution of entanglement in open quantum systems,” *Physical Review A* **85**, 012327 (2012). [Primary manuscript](https://arxiv.org/abs/1102.4403).
