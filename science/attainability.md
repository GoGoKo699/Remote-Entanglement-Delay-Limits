# Finite-memory attainment

The causal bound identifies a single optimal state,

```math
\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id})(\Phi_\pi).
```

This section supplies two receiver constructions. A general primitive source admits arbitrarily accurate continuous-time attainment with a fixed $`d^2`$-dimensional memory. For a continuously driven amplitude-damped qubit, one matched receiver qubit reaches the optimum in its stationary limit.

The constructions assume that every vacuum output channel in the source dilation is collected coherently and delivered with the same delay. The source model and propagation phases are known. All controls below act locally at the receiver; the source remains autonomous.

## A continuous purification tracker

The construction uses the purification and sequential-decoder mechanism underlying coherent quantum absorbers.[^yang][^tsang] We give the time-dependent drift explicitly and regularize its initialization. This avoids assuming that an arbitrary stationary absorber attracts its designated pure state.

### Theorem

Let $`A`$ have dimension $`d`$, with a faithful stationary state $`\pi`$ and

```math
\mathcal E_t(X)\longrightarrow\pi\mathrm{Tr}X.
```

For every $`\epsilon>0`$, there is a continuous Markovian receiver with memory

```math
M=C\otimes R',\qquad \dim C=\dim R'=d,
```

initially independent of the source, and a finite time $`T`$ such that its designated output register $`C`$ obeys

```math
\|\rho_{AC}(t)-\sigma_\tau\|_1<\epsilon
\qquad\text{for all }t\ge T.
```

For each fixed $`\epsilon`$, the receiver Hamiltonian and its coupling operators can be chosen bounded and continuous in time. Their bounds may depend on $`\epsilon`$. The memory dimension does not depend on accuracy, delay or elapsed operating time. The receiver processes the incoming fields continuously and does not store a temporal block of field modes.

### A faithful regularized target

Introduce an inaccessible mathematical reference $`R`$ purifying the source's initial state. It is not an apparatus supplied to the receiver. With the vectorization convention of [the causal bound](causal-bound.md), define

```math
\chi_u=(\mathcal E_u\otimes\mathrm{id}_R)(\Phi_\pi),
\qquad
\chi_\infty=\pi\otimes\pi^T.
```

We first need the following positivity fact:

```math
\chi_u>0\qquad\text{for every }u>0.
```

To prove it, note that $`\det\chi_u`$ is a real analytic function of $`u`$. Its limit is $`\det(\pi\otimes\pi^T)>0`$, so it cannot vanish throughout any open interval. Thus every interval $`(0,u)`$ contains a time $`v`$ with $`\chi_v>0`$.

Finite-dimensional GKLS evolution preserves strict positivity. In fact, if

```math
K_A=-iH-\frac12\sum_j L_j^\dagger L_j,
```

the no-jump term in the quantum-trajectory expansion gives

```math
\mathcal E_s(X)\succeq e^{sK_A}Xe^{sK_A^\dagger}>0
\qquad(X>0, s<\infty).
```

The same statement holds after tensoring with an identity channel. Therefore $`\chi_u=(\mathcal E_{u-v}\otimes\mathrm{id})(\chi_v)>0`$, as claimed.

Fix a regularization time $`\delta>0`$. At receiver processing time $`u`$, use the positive square root

```math
C_u=\sqrt{\chi_{u+\delta}}.
```

The register $`M`$ is a basis copy of $`A\otimes R`$, with $`C`$ copying $`A`$ and $`R'`$ copying $`R`$. The desired comparison state on $`ARM`$ is

```math
|C_u\rangle\!\rangle_{AR:M}.
```

Its norm is one. The regularization is part of the receiver design, not an extra propagation delay.

### Receiver operators

Regard $`S=A\otimes R`$ as the source for the purpose of writing matrices. Its actual couplings act only on $`A`$:

```math
V_j=L_j\otimes I_R,
\qquad
K=K_A\otimes I_R.
```

For this subsection, write $`\chi=\chi_{u+\delta}`$, $`C=C_u`$, and

```math
F=\sum_j V_j\chi V_j^\dagger.
```

All transposes below are ordinary matrix transposes in the fixed copy bases. Set

```math
\boxed{
\begin{aligned}
J_j(u)&=-\bigl(C^{-1}V_jC\bigr)^T,\\
Q(u)&=C^{-1}\bigl(\dot C-KC-FC^{-1}\bigr),\\
K_M(u)&=Q(u)^T,\\
H_M(u)&=\frac{i}{2}\bigl(K_M(u)-K_M(u)^\dagger\bigr).
\end{aligned}}
```

These are local receiver matrices of dimension $`d^2`$. They require knowledge of the source model, but no access to the reference $`R`$, no measurement of the source, and no feedback.

The receiver operators define a valid GKLS coupling. Indeed,

```math
\dot\chi=K\chi+\chi K^\dagger+F,
\qquad
\dot\chi=\dot C\,C+C\dot C.
```

Multiplication by $`C^{-1}`$ on both sides gives

```math
Q+Q^\dagger=-C^{-1}FC^{-1}
=-\left(\sum_jJ_j^\dagger J_j\right)^T.
```

Hence

```math
K_M+K_M^\dagger=-\sum_jJ_j^\dagger J_j,
\qquad
K_M=-iH_M-\frac12\sum_jJ_j^\dagger J_j.
```

For fixed $`\delta`$, the smallest eigenvalue of $`\chi_{u+\delta}`$ is bounded away from zero uniformly for $`u\ge0`$: use continuity on a compact initial interval and convergence to the faithful product state on the tail. The same reasoning, together with the Sylvester equation for $`\dot C`$, bounds all receiver coefficients. The derivative in $`Q`$ fixes the time-dependent purification gauge explicitly.

### Exact tracking of the comparison state

In a zero-delay cascaded representation, the combined jumps and effective no-jump drift are

```math
\mathsf J_j=V_j\otimes I_M+I_S\otimes J_j,
```

```math
\mathsf K
=K\otimes I_M+I_S\otimes K_M
-\sum_jV_j\otimes J_j^\dagger.
```

This is the standard source-then-receiver cascade; the cross term is induced by the common directional field, not by a separately supplied interaction between source and receiver.[^stannigel]

Using $`(A\otimes B)|C\rangle\!\rangle=|ACB^T\rangle\!\rangle`$ gives

```math
\mathsf J_j|C\rangle\!\rangle=0,
```

and

```math
\begin{aligned}
\mathsf K|C\rangle\!\rangle
&=\left|KC+CQ+FC^{-1}\right\rangle\!\rangle\\
&=|\dot C\rangle\!\rangle.
\end{aligned}
```

Therefore the unconditional cascaded dynamics exactly follows the pure state $`|C_u\rangle\!\rangle`$ when started from its comparison initial state $`|C_0\rangle\!\rangle=|\sqrt{\chi_\delta}\rangle\!\rangle`$. Every outgoing field is vacuum along this ideal comparison evolution.

### Independent physical initialization and error bound

The correlated comparison initial state is not required as a physical resource. Let

```math
|\phi_\pi\rangle=|\sqrt\pi\rangle\!\rangle_{AR}.
```

Since $`\chi_0=|\phi_\pi\rangle\langle\phi_\pi|`$ is pure, its canonical purification factors as

```math
|\sqrt{\chi_0}\rangle\!\rangle_{AR:M}
=|\phi_\pi\rangle_{AR}
 \otimes|\overline{\phi_\pi}\rangle_M.
```

Thus the physical receiver starts in the known local pure state $`|\overline{\phi_\pi}\rangle_M`$, independently of the source. This uses only local preparation inside $`M`$.

For positive operators, the square-root trace inequality is

```math
\|\sqrt X-\sqrt Y\|_2^2\le\|X-Y\|_1.
```

Together with the trace distance between pure states, it implies

```math
\left\|
|\sqrt X\rangle\!\rangle\langle\!\langle\sqrt X|
-|\sqrt Y\rangle\!\rangle\langle\!\langle\sqrt Y|
\right\|_1
\le2\sqrt{\|X-Y\|_1}
```

for normalized $`X,Y`$.[^powers]

The actual and comparison initial states therefore differ by at most

```math
2\sqrt{\|\chi_\delta-\Phi_\pi\|_1}.
```

They evolve under the same physical source–receiver channel. Trace-distance contractivity preserves this bound at every later time. Meanwhile, the comparison target tends to

```math
|\sqrt{\chi_\infty}\rangle\!\rangle
=|\sqrt\pi\rangle\!\rangle_{AC}
 \otimes|\sqrt{\pi^T}\rangle\!\rangle_{RR'},
```

after regrouping the factors. The designated register $`C`$ thus approaches a purification of the current source; $`R'`$ retains the information associated with its initial inaccessible reference.

For physical delay $`\tau`$, start the receiver when the first source output arrives and use processing time $`u=t-\tau`$. The source evolves for another $`\tau`$ beyond the causal cut. Partial trace and $`\mathcal E_\tau`$ are contractive, giving the explicit physical equal-time bound

```math
\boxed{
\begin{aligned}
\|\rho_{AC}(u+\tau)-\sigma_\tau\|_1
\le{}&2\sqrt{\|\chi_\delta-\Phi_\pi\|_1}\\
&+2\sqrt{\|\chi_{u+\delta}-\pi\otimes\pi^T\|_1}.
\end{aligned}}
```

First choose $`\delta`$ small, then choose $`u`$ large. This proves the theorem. A fixed regularization gives uniformly small late-time error; the exact general optimum is a supremum over such receivers. No convergence claim for an arbitrary autonomous absorber is used.

## An autonomous matched qubit receiver

For the selected source family, the general construction can be replaced by the two-qubit dark dimer of Stannigel, Rabl and Zoller.[^stannigel] We state the phase and Pauli conventions explicitly and prove global convergence.

### Conventions and physical receiver

Use $`|g\rangle=|0\rangle`$, $`|e\rangle=|1\rangle`$,

```math
Z=|g\rangle\langle g|-|e\rangle\langle e|,
\qquad
\sigma_-=|g\rangle\langle e|.
```

The source is

```math
H_A=\frac{\Omega X+\Delta Z}{2},
\qquad L_A=\sqrt\gamma\,\sigma_-^A,
\qquad \gamma>0.
```

After compensating the known propagation phase, choose a receiver qubit with

```math
H_B=\frac{\Omega X-\Delta Z}{2},
\qquad L_B=\sqrt\gamma\,\sigma_-^B.
```

Its drive has the same amplitude and the opposite detuning in this convention. In the retarded, zero-delay cascaded representation, the joint generator has jump and Hamiltonian

```math
J=\sqrt\gamma\,(\sigma_-^A+\sigma_-^B),
```

```math
H_{AB}=H_A\otimes I+I\otimes H_B
+\frac{\gamma}{2i}
\left(\sigma_-^A\sigma_+^B-\sigma_+^A\sigma_-^B\right).
```

Tracing out $`B`$ gives precisely the stated source generator. The cross Hamiltonian is the cascade term and requires no direct control of the source by the receiver.

Define

```math
|S\rangle=\frac{|eg\rangle-|ge\rangle}{\sqrt2},
\qquad
|T\rangle=\frac{|eg\rangle+|ge\rangle}{\sqrt2},
```

```math
\alpha=\frac{\sqrt2\,\Omega}{2\Delta+i\gamma},
\qquad
|D\rangle=
\frac{|gg\rangle+\alpha|S\rangle}{\sqrt{1+|\alpha|^2}}.
```

The factor of two in the drive differs from the convention $`H=\Omega_{\rm SRZ}X+\delta Z_{\rm SRZ}/2`$ used by Stannigel, Rabl and Zoller:[^stannigel] here $`\Omega=2\Omega_{\rm SRZ}`$ and $`Z=-Z_{\rm SRZ}`$, so $`\Delta=-\delta`$.

Direct action gives

```math
J|gg\rangle=J|S\rangle=0,
\qquad
H_{AB}|gg\rangle=\frac{\Omega}{\sqrt2}|T\rangle,
```

```math
H_{AB}|S\rangle
=-\left(\Delta+\frac{i\gamma}{2}\right)|T\rangle.
```

Thus $`J|D\rangle=H_{AB}|D\rangle=0`$.

### Global convergence

Let $`P_D=|D\rangle\langle D|`$ and $`N=1+|\alpha|^2`$. Under the joint master equation,

```math
\frac{d}{du}\mathrm{Tr}(P_D\widetilde\rho(u))
=\frac{2\gamma}{N}
\langle T|\widetilde\rho(u)|T\rangle\ge0.
```

The dark-state population is a Lyapunov function. To identify its invariant zero-derivative set, suppose a trajectory has zero $`T`$ population for all time. Positivity then removes every coherence with $`T`$. At such a state,

```math
\frac{d}{du}\langle T|\widetilde\rho|T\rangle
=2\gamma\langle ee|\widetilde\rho|ee\rangle,
```

so the trajectory must also have zero $`ee`$ population and therefore be supported on $`\mathrm{span}\{|gg\rangle,|S\rangle\}`$. The jump vanishes on this subspace. Remaining there under the Hamiltonian requires its support to lie in the kernel of

```math
\frac{\Omega}{\sqrt2}\langle gg|
-\left(\Delta+\frac{i\gamma}{2}\right)\langle S|.
```

That kernel is exactly $`\mathrm{span}\{|D\rangle\}`$ because $`\gamma>0`$. The largest invariant zero-derivative set is therefore the single state $`P_D`$. Compactness of the finite-dimensional state space and invariance of its limit sets give

```math
\widetilde\rho(u)\longrightarrow P_D
```

from every initial two-qubit state. In particular, no initial source–receiver entanglement is needed. This proves the attraction property used here directly; Appendix B.1 of Stannigel, Rabl and Zoller establishes uniqueness for the same dimer family.[^stannigel]

### Source marginal and delayed optimum

Write

```math
\mathcal D=\gamma^2+4\Delta^2+2\Omega^2.
```

The source marginal of $`P_D`$ is

```math
\pi=\frac1{\mathcal D}
\begin{pmatrix}
\gamma^2+4\Delta^2+\Omega^2&\Omega(2\Delta+i\gamma)\\
\Omega(2\Delta-i\gamma)&\Omega^2
\end{pmatrix}.
```

It is the stationary state of the isolated source and is faithful whenever $`\Omega>0`$. Hence $`|D\rangle`$ is a purification of $`\pi`$. There is a fixed unitary $`U`$ on the receiver such that

```math
|D\rangle=(I\otimes U)|\sqrt\pi\rangle\!\rangle.
```

For example, if $`F_D`$ is the coefficient matrix of $`|D\rangle`$,

```math
F_D=\frac1{\sqrt{1+|\alpha|^2}}
\begin{pmatrix}1&-\alpha/\sqrt2\\ \alpha/\sqrt2&0\end{pmatrix},
\qquad
U=\left(\pi^{-1/2}F_D\right)^T.
```

For a pure one-way delay, the aligned source–receiver state $`\widetilde\rho(u)`$ obeys the zero-delay cascaded equation, while the physical equal-time state is

```math
\rho_{AB}(u+\tau)
=(\mathcal E_\tau\otimes\mathrm{id}_B)
\bigl(\widetilde\rho(u)\bigr).
```

This is the causal cut, with the receiver operating on output emitted through source time $`u`$. Taking the stationary limit gives

```math
\boxed{
\rho_{AB}^{\rm ss}(\tau)
=(\mathcal E_\tau\otimes\mathrm{id})(P_D)
=(I\otimes U)\sigma_\tau(I\otimes U^\dagger).
}
```

A fixed local change of receiver basis therefore attains $`\sigma_\tau`$ itself, and every locally unitary invariant entanglement measure already has its optimal value without that change. This includes the two-qubit concurrence frontier used in the static-drive asymptotic. If $`\Omega=0`$, the source and dimer limit are the ground product state and the optimal concurrence is zero.

The retarded-time change of variables is a standard property of a purely directional cascade.[^pichler] The additional source evolution $`\mathcal E_\tau`$ is essential when converting its stationary state into a state of the two nodes at the same physical time.

## References

[^yang]: D. Yang, S. F. Huelga and M. B. Plenio, “Efficient Information Retrieval for Sensing via Continuous Measurement,” *Physical Review X* **13**, 031012 (2023), Section IV B, Eqs. (29)–(32), and Appendix B.1–B.2. These give the sequential SVD decoder and its purification interpretation. [DOI](https://doi.org/10.1103/PhysRevX.13.031012); [arXiv:2209.08777v3](https://arxiv.org/abs/2209.08777v3).

[^tsang]: M. Tsang, “Quantum reversal: a general theory of coherent quantum absorbers,” *Quantum* **9**, 1650 (2025), Introduction and Sections 3–5. Reverser existence specifies a pure stationary state; convergence from other initial states is outside the general theorem's scope. [DOI](https://doi.org/10.22331/q-2025-02-26-1650); [arXiv:2402.02502v3](https://arxiv.org/abs/2402.02502v3).

[^stannigel]: K. Stannigel, P. Rabl and P. Zoller, “Driven-dissipative preparation of entangled states in cascaded quantum-optical networks,” *New Journal of Physics* **14**, 063014 (2012), Section 2.1, Eqs. (2)–(3); Section 3.1, Eqs. (8)–(9); and Appendix B.1. [DOI](https://doi.org/10.1088/1367-2630/14/6/063014); [arXiv:1112.1690v2](https://arxiv.org/abs/1112.1690v2).

[^powers]: R. T. Powers and E. Størmer, “Free states of the canonical anticommutation relations,” *Communications in Mathematical Physics* **16**, 1–33 (1970). The square-root trace estimate is the Powers–Størmer inequality. [DOI](https://doi.org/10.1007/BF01645492).

[^pichler]: H. Pichler and P. Zoller, “Photonic Circuits with Time Delays and Quantum Feedback,” *Physical Review Letters* **116**, 093601 (2016), discussion of the purely cascaded limit following the time-bin construction. [DOI](https://doi.org/10.1103/PhysRevLett.116.093601); [arXiv:1510.04646](https://arxiv.org/abs/1510.04646).
