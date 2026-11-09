# Thirty milestones for remote entanglement delay limits

This map follows one scientific question: **how much unconditional entanglement can a stationary emitter retain with a downstream receiver at the same physical time, when its complete output arrives only after a delay?** Its targets and dependencies are defined by the project. They apply to any reader and do not depend on an assessment of prior knowledge.

The selected educational anchor is C. W. Gardiner and P. Zoller, *Quantum Noise*, third edition (Springer, 2004), abbreviated **QN** below.[^qn] The [source-to-project bridge](QUANTUM_NOISE_BRIDGE.md) translates its notation and identifies the steps supplied by this repository. Section numbers refer to that edition. An anchor pointer identifies relevant foundations; it does not attribute the project's channel-theoretic or optimization results to the textbook. The canonical science pages retain the primary research references for those ingredients.

## Allocation and scientific route

The **12 background/preliminaries milestones, M01–M12**, connect four kinds of object: an open emitter, its traveling quantum field, a causal receiver, and a channel-state description of entanglement. This project needs that connection before a delay can be interpreted as a bound on every receiver. The phase moves from individual states and generators to a complete operational model, integrated in M12.

The **18 narrative/innovation milestones, M13–M30**, follow the actual proof structure. They connect the causal converse to attainable receivers, then use the driven-qubit source's specific dynamics to establish a uniform long-delay optimum. More milestones are assigned here because neither an abstract bound without attainment nor a fixed-parameter decay calculation proves the central result. M30 integrates the mechanism, the sharp law, its attribution and its physical scope.

| Part of the story | Milestones | Connection established |
|---|---|---|
| Local states and source dynamics | [M01](#m01)–[M05](#m05) | From a density operator to a stationary driven emitter |
| Traveling output and the operational question | [M06](#m06)–[M12](#m12) | From field access and time ordering to the channel-state framework |
| A universal bound and its physical attainability | [M13](#m13)–[M18](#m18) | From causality to an exact stationary receiver frontier |
| The source-specific uniform optimization | [M19](#m19)–[M28](#m28) | From stationary mixedness to the sharp coefficient and horizon |
| Physical meaning and integrated contribution | [M29](#m29)–[M30](#m30) | From optimal tuning to its costs, boundaries and significance |

The map covers the load-bearing ideas and their dependencies. Detailed matrix calculations and specialist proof steps remain in the linked scientific accounts.

## Phase I — Background and preliminaries

### M01

**Quantum states and reduced descriptions.**

- **Central question:** How can an emitter have a mixed state while the larger emitter–field system has a pure state?
- **Understanding target:** Distinguish a density operator, a joint state and a reduced state obtained by partial trace. Recognize that a fixed marginal does not specify its correlations with another system, and that purity and population are different properties.
- **Dependencies and story role:** This is the starting point. It establishes the local and joint objects used throughout the background phase.
- **Conceptual connection:** The source marginal $`\pi`$ remains stationary while its correlations with emitted light evolve. That distinction will make the receiver optimization nontrivial.
- **Source pointers:** QN Chapter 2, especially §2.5 for system–bath descriptions. Project: [causal bound, model and notation](../science/causal-bound.md#model-and-notation), including the two marginals of the canonical purification; [source stationary state](../science/driven-qubit.md#stationary-state-and-its-purification-concurrence).

### M02

**Reduced channels and Markov generators.**

- **Central question:** What mathematical object describes the emitter after the field has been ignored?
- **Understanding target:** Distinguish a completely positive trace-preserving channel $`\mathcal E_t`$ from its generator $`\mathcal L`$, and understand $`\mathcal E_t=e^{t\mathcal L}`$ and the semigroup composition rule. Identify the Hamiltonian and dissipative terms in the stated generator.
- **Dependencies and story role:** Builds on M01 by turning a static reduced description into a dynamical one.
- **Conceptual connection:** The same reduced channel that describes ordinary damping will act over the interval whose output has not yet reached the receiver.
- **Source pointers:** QN §§3.6 and 5.4. Project: [model, source generator](../science/model.md#1-source-propagation-and-receiver); [driven-qubit generator and dissipator convention](../science/driven-qubit.md#model-and-operational-scope).

### M03

**Fresh quantum input and the Markov dilation.**

- **Central question:** Which physical independence lets an old output field be separated from the source's later evolution?
- **Understanding target:** Explain the role of fresh independent input increments in a vacuum input-output dilation. Distinguish memory retained by the source or receiver from correlations already carried away in old output. Recognize that a reduced master equation alone does not identify which environmental channels are physically accessible.
- **Dependencies and story role:** Uses M01–M02 to connect the generator to a larger source–field description.
- **Conceptual connection:** Fresh input independence is the physical premise behind commuting the source's later evolution with processing of already emitted output.
- **Source pointers:** QN §§5.1–5.2 and 11.2. Project: [model, fixed Markov dilation](../science/model.md#1-source-propagation-and-receiver); [causal-cut proof](../science/causal-bound.md#proof).

### M04

**Stationarity, faithfulness and mixing.**

- **Central question:** Which properties of a stationary state are needed for which part of the result?
- **Understanding target:** Separate stationarity, $`\mathcal E_t(\pi)=\pi`$, from faithfulness, $`\pi>0`$, and from the explicit mixing assumption $`\mathcal E_t(X)\to\pi\mathrm{Tr}X`$. Understand why a stationary marginal can coexist with continuing emission, and why a pure stationary state is a distinct boundary case.
- **Dependencies and story role:** Uses M02–M03 to identify the long-time source properties before the receiver is introduced.
- **Conceptual connection:** Stationarity fixes the causal envelope, mixing supports late-time purification extraction, and faithfulness permits invertible filtering to the Choi state.
- **Source pointers:** QN §§5.4 and 9.2 for master-equation and atomic context; the precise distinctions are project definitions. Project: [model, primitivity and initialization](../science/model.md#1-source-propagation-and-receiver); [optimal values and their assumptions](../science/causal-bound.md#optimal-entanglement-values).

### M05

**The driven spontaneous-emission qubit.**

- **Central question:** What do drive strength, detuning and spontaneous-emission rate change in the source?
- **Understanding target:** Interpret $`H=(\Omega X+\Delta Z)/2`$ and $`L=\sqrt\gamma\,\sigma_-`$ in the ground/excited convention. Connect Hamiltonian rotation and damping to the affine Bloch equation. Keep fixed $`\gamma`$ separate from the two static parameters $`\Omega,\Delta`$ that will be optimized.
- **Dependencies and story role:** Uses M01–M04 to give the abstract source a concrete physical realization.
- **Conceptual connection:** The optical Bloch dynamics supplies the specific structure needed for the sharp asymptotic; a general qubit channel will not suffice.
- **Source pointers:** QN §9.2. Project: [driven-qubit model](../science/driven-qubit.md#model-and-operational-scope); [physical Bloch generator](../science/driven-qubit.md#finite-delay-evaluation); [bridge notation](QUANTUM_NOISE_BRIDGE.md#notation-and-conventions).

### M06

**Output as a quantum information carrier.**

- **Central question:** What is lost when the emitted field is measured or only partly collected?
- **Understanding target:** Distinguish coherent access to the field from a classical record of detections. Understand why complete collection means all outputs in the specified pure-input dilation, and why an inaccessible bath can retain correlations that a receiver cannot recover.
- **Dependencies and story role:** Extends M03 and M05 from source dynamics to the resource delivered downstream.
- **Conceptual connection:** Incomplete collection still respects the causal upper bound, but full coherent collection is an additional requirement for its general attainment.
- **Source pointers:** QN §§3.2 and 11.3. Project: [continuous-receiver resources](../science/receiver-resources.md#continuous-receivers); [loss and inaccessible baths](../science/receiver-resources.md#loss-postselection-and-other-changes-of-resources).

### M07

**Directional cascades and receiver freedom.**

- **Central question:** How can a receiver interact strongly with the source's light without controlling the source?
- **Understanding target:** Interpret a source-then-receiver cascade and its absence of feedback. Distinguish the field-induced cascade term from a separately controlled two-node interaction. Recognize that downstream memory, ancillas and local control enlarge the receiver class without changing the upstream generator.
- **Dependencies and story role:** Combines M02, M03 and M06 into the network architecture.
- **Conceptual connection:** The upper bound must cover every permitted downstream processor, while an explicit cascade will later provide a receiver that reaches it.
- **Source pointers:** QN §§12.1 and 12.3. Project: [source and receiver assumptions](../science/model.md#1-source-propagation-and-receiver); [matched-receiver Hamiltonian and coupling](../science/attainability.md#conventions-and-physical-receiver).

### M08

**Physical equal time and retarded time.**

- **Central question:** Why does removing delay from a directional evolution equation not remove delay from the simultaneous entanglement?
- **Understanding target:** Distinguish the pair of times $`(t,t)`$ from $`(t-\tau,t)`$. Explain why, at physical time $`t`$, the receiver has processed only source output emitted through $`t-\tau`$, while the source has continued to evolve.
- **Dependencies and story role:** Uses M03, M06 and M07 to identify the time convention that makes the problem well posed.
- **Conceptual connection:** The missing evolution interval becomes the local channel $`\mathcal E_\tau`$ in the final equal-time state. A pure retarded-time correlation need not give a pure equal-time state.
- **Source pointers:** QN §§5.2 and 12.1 for multitime and cascade context. Project: [model, physical-time score](../science/model.md#1-source-propagation-and-receiver); [source marginal and delayed optimum](../science/attainability.md#source-marginal-and-delayed-optimum).

### M09

**The unconditional output score.**

- **Central question:** Which state is being optimized when the receiver uses measurements and additional memory?
- **Understanding target:** Separate an unconditional density operator from a normalized postselected branch. Identify the designated receiver output and the tracing out of auxiliary memory. For the qubit application, recognize that ordinary Wootters concurrence is evaluated on two qubits, not on the entire potentially larger receiver.
- **Dependencies and story role:** Uses M01 and M06–M08 to settle the observable objective before introducing entanglement tools.
- **Conceptual connection:** Averaged adaptive receiver processing is a channel; conditioning on a successful record changes the numerical optimization.
- **Source pointers:** QN §§11.1 and 11.3. Project: [driven-qubit operational score](../science/driven-qubit.md#model-and-operational-scope); [postselection and designated-output qualifications](../science/receiver-resources.md#loss-postselection-and-other-changes-of-resources).

### M10

**Purifications, extensions and channel states.**

- **Central question:** How can one reference system represent every possible correlation compatible with a source marginal?
- **Understanding target:** Explain the canonical purification $`|\sqrt\pi\rangle`$, its reference marginal $`\pi^T`$, and the fact that every extension of $`\pi`$ is a channel image of that purification. Distinguish the stationary-weighted state from the normalized Choi state formed with a maximally entangled input.
- **Dependencies and story role:** Uses M01–M02 and M09 to supply the channel-state language missing from a purely optical description.
- **Conceptual connection:** Purification universality is the bridge from an unspecified receiver to one finite-dimensional resource state.
- **Source pointers:** QN §§2.5 and 11.2 provide system–field state context; the extension and Choi arguments are supplied by the project. Project: [purification convention and extension proof](../science/causal-bound.md#proof); [Choi-state formula](../science/driven-qubit.md#choi-state-formula).

### M11

**Entanglement monotonicity and channel death.**

- **Central question:** What conclusions follow from expressing a state as local processing of another state?
- **Understanding target:** Distinguish separability, a quantitative entanglement monotone and an entanglement-breaking channel. Understand deterministic local monotonicity, the two-qubit concurrence formula, and the special role of the two-qubit partial-transpose criterion. Separate entanglement from distillability in larger dimensions.
- **Dependencies and story role:** Uses M09–M10 to turn the channel-state description into an operational comparison.
- **Conceptual connection:** Local monotonicity will give the upper bound, while separability of the channel state will give a receiver-independent horizon.
- **Source pointers:** QN §§2.5 and 11.3 supply the reduced-state and measurement context; the entanglement results are research-level additions. Project: [optimal entanglement values](../science/causal-bound.md#optimal-entanglement-values); [exact horizon](../science/causal-bound.md#the-exact-entanglement-horizon); [concurrence definition](../science/driven-qubit.md#choi-state-formula).

### M12

**Background synthesis: the stationary delayed-receiver problem.**

- **Central question:** How do the source, field, receiver, time convention and score combine into one precise optimization?
- **Understanding target:** Give a connected account of an autonomous stationary Markov source, independent initialization, one-way propagation, no faster source-information route, and deterministic causal receiver processing. Separate the assumptions needed for an upper bound from full coherent collection needed for tightness. State the qubit score with fixed $`\gamma`$ and source parameters constant during each run.
- **Dependencies and story role:** Integrates M01–M11 and ends the background phase. Its output is the complete problem statement, rather than an additional isolated definition.
- **Conceptual connection:** The physical model now supports two linked questions: what no receiver can exceed, and whether a receiver can attain that limit before source tuning is optimized.
- **Source pointers:** QN §§3.2, 5.2, 9.2, 11.2 and 12.1 as the integrated foundation. Project: [model, Sections 1–3](../science/model.md); [bridge from fields to channels](QUANTUM_NOISE_BRIDGE.md#from-fields-to-channels).

## Phase II — Narrative and innovation

### M13

**The causal cut.**

- **Central question:** What part of the joint evolution is unavailable to every receiver at physical time $`t`$?
- **Understanding target:** Explain the factorization $`\rho_{AB}(t)=(\mathcal E_\tau\otimes\mathrm{id})(\omega_{AB})`$ with $`\omega_A=\pi`$. Identify where fresh input independence, absence of feedback and the delay restriction are used. Understand why arbitrary old-output processing can be included in $`\omega_{AB}`$.
- **Dependencies and story role:** Uses M03, M08 and M12 to establish the first component of the converse.
- **Conceptual connection:** The in-flight interval is a channel acting locally on the source, independently of receiver complexity.
- **Source pointers:** QN §§5.2 and 12.1. Project: [causal-bound proof, time cut and commuting operations](../science/causal-bound.md#proof); [bridge to the universal state](QUANTUM_NOISE_BRIDGE.md#from-a-delayed-field-to-a-universal-state).

### M14

**One state dominates every receiver.**

- **Central question:** How does the causal cut become a universal state envelope?
- **Understanding target:** Combine the extension characterization with M13 to obtain $`\rho_{AB}(t)=(\mathrm{id}\otimes\Lambda_t)(\sigma_\tau)`$, where $`\sigma_\tau=(\mathcal E_\tau\otimes\mathrm{id})(\Phi_\pi)`$. Distinguish a state-envelope theorem from a receiver construction, and identify which conclusions already follow from local monotonicity.
- **Dependencies and story role:** Combines M10–M11 with M13 to complete the receiver-universal upper bound.
- **Conceptual connection:** Receiver design is reduced to local processing of one delayed channel state, without specifying an absorber, detector or control schedule.
- **Source pointers:** QN §§5.2 and 12.1 for the physical cut; the purification step is project-supplied. Project: [domination theorem](../science/causal-bound.md#theorem-domination-by-one-delayed-channel-state); [monotone upper bound](../science/causal-bound.md#optimal-entanglement-values).

### M15

**The finite-memory purification mechanism.**

- **Central question:** Why need a receiver's coherent memory not grow with the amount of emitted light?
- **Understanding target:** Explain the sequential purification construction with $`M=C\otimes R'`$ of dimension $`d^2`$. Distinguish the inaccessible mathematical reference for the source's initial mixed state from the receiver's locally prepared auxiliary register. Understand how equal source-reference marginals permit a unitary on memory and the next field unit.
- **Dependencies and story role:** Uses M03–M04, M06 and M10 to begin the achievability argument after M14.
- **Conceptual connection:** Mixing lets the designated output eventually purify the current source while another finite register retains information about its initial reference.
- **Source pointers:** QN §11.2 for pure state-vector evolution and §12.1 for directional interaction. Project: [exact collision-model construction](../science/receiver-resources.md#appendix-an-exact-collision-model-construction); [continuous tracker theorem](../science/attainability.md#theorem).

### M16

**A continuous receiver with independent initialization.**

- **Central question:** How is the sequential mechanism made continuous without assuming an initially entangled receiver or singular physical controls?
- **Understanding target:** Follow the role of the faithful regularized target $`\chi_{u+\delta}`$, its canonical square root, and the derivative term in the receiver drift. Explain the comparison-state and contractivity argument that permits independent physical initialization. Distinguish bounded controls for each accuracy from a bound uniform as the error tends to zero.
- **Dependencies and story role:** Develops M15 into the continuous-time attainment theorem needed by the operational model.
- **Conceptual connection:** A valid time-dependent GKLS receiver and an explicit error bound close the gap between a formal purification and a physical causal protocol.
- **Source pointers:** QN §§11.2 and 12.1. Project: [faithful regularized target](../science/attainability.md#a-faithful-regularized-target), [receiver operators](../science/attainability.md#receiver-operators), and [independent initialization and error bound](../science/attainability.md#independent-physical-initialization-and-error-bound).

### M17

**The exact frontier and entanglement horizon.**

- **Central question:** When does the universal upper bound become an attainable optimum, and when is all entanglement impossible?
- **Understanding target:** Combine approximate attainment with continuity to identify the supremum of each continuous deterministic entanglement monotone on the source and a designated $`d`$-dimensional output. Explain the faithful-state filtering equivalence between separability of $`\sigma_\tau`$ and entanglement breaking of $`\mathcal E_\tau`$. Distinguish exact supremal equality from one general receiver attaining the state exactly at finite time.
- **Dependencies and story role:** Integrates M11, M14 and M16 into the general operational result.
- **Conceptual connection:** The fixed-source propagation horizon is exactly the channel's entanglement-breaking time under ideal collection; eventual entanglement breaking itself is an inherited theorem.
- **Source pointers:** QN §§5.4 and 12.1 for source relaxation and cascade context. Project: [optimal entanglement values](../science/causal-bound.md#optimal-entanglement-values); [exact entanglement horizon](../science/causal-bound.md#the-exact-entanglement-horizon).

### M18

**The matched qubit receiver.**

- **Central question:** Can one ordinary receiver qubit reach the fixed-source frontier for the driven emitter?
- **Understanding target:** Understand why matching the drive amplitude and reversing the detuning produces a dark dimer in the aligned cascade. Distinguish existence of a dark state from global attraction, and follow the stated convergence argument. Convert the aligned purification into the physical equal-time state by applying the extra source channel.
- **Dependencies and story role:** Uses M05, M07–M08 and M14–M17 to give a concrete autonomous realization of the qubit optimum.
- **Conceptual connection:** The established Stannigel–Rabl–Zoller absorber supplies the achiever; the causal theorem explains why more elaborate downstream devices cannot improve its unconditional two-qubit score.
- **Source pointers:** QN §§12.1 and 12.3. Project: [matched qubit receiver](../science/attainability.md#an-autonomous-matched-qubit-receiver), especially [global convergence](../science/attainability.md#global-convergence) and [delayed optimum](../science/attainability.md#source-marginal-and-delayed-optimum).

### M19

**Stationary mixedness as the source resource.**

- **Central question:** Which scalar measures the stationary source's available purification entanglement?
- **Understanding target:** Interpret $`s=2\sqrt{\det\pi}=2\Omega^2/(\gamma^2+4\Delta^2+2\Omega^2)`$ as purification concurrence. Distinguish the small eigenvalue $`p\sim s^2/4`$ from the physical excited population $`\pi_{ee}=s/2`$. Explain why $`\Omega=0`$ has zero stationary score even though undriven amplitude damping can preserve some transient entanglement.
- **Dependencies and story role:** Uses M05, M10 and M18 to identify the source parameter that organizes the optimization.
- **Conceptual connection:** Weak driving lengthens entanglement survival but reduces the stationary entanglement supplied at the causal cut.
- **Source pointers:** QN §9.2. Project: [stationary state and purification concurrence](../science/driven-qubit.md#stationary-state-and-its-purification-concurrence); [stationary-state geometry](../science/long-delay-law.md#2-geometry-of-the-stationary-state).

### M20

**Exact evaluation at a fixed source and delay.**

- **Central question:** How can the optimum over all receivers be computed without optimizing a receiver model?
- **Understanding target:** Connect the Bloch propagator to the normalized Choi matrix and the exact identity $`\mathfrak C_\tau(\Omega,\Delta)=C(\sigma_\tau)=sC(J_\tau)`$. Keep the reference transpose, including $`Y^T=-Y`$, and the normalization conventions explicit. Distinguish exact finite-delay evaluation from a global finite-delay optimization over source parameters.
- **Dependencies and story role:** Combines M10–M11 and M18–M19 into a usable quantitative frontier.
- **Conceptual connection:** Concurrence factorization separates the source's stationary resource from the channel's entanglement survival.
- **Source pointers:** QN §9.2 for the Bloch dynamics; the concurrence factorization is a cited research ingredient. Project: [exact stationary receiver frontier](../science/driven-qubit.md#exact-stationary-receiver-frontier), [Choi-state formula](../science/driven-qubit.md#choi-state-formula), and [finite-delay evaluation](../science/driven-qubit.md#finite-delay-evaluation).

### M21

**Retuning the source and taking limits in order.**

- **Central question:** Why does optimizing at long delay require more than following one fixed source for a long time?
- **Understanding target:** Separate the fixed-source entanglement-breaking horizon from a family of sources chosen for successive delays. Define $`a=e^{-\gamma\tau/2}`$ and the ratio $`s/a`$. State that the source and receiver first reach late-time operation for each design, while $`\Omega,\Delta`$ remain static within that design and $`\gamma`$ stays fixed across the optimization.
- **Dependencies and story role:** Uses M17 and M19–M20 to formulate the asymptotic question with its correct quantifiers.
- **Conceptual connection:** A uniform converse must cover delay-dependent drive and detuning sequences, including detunings with no common bound.
- **Source pointers:** QN §§5.4 and 9.2. Project: [long-delay theorem and definitions](../science/long-delay-law.md#1-statement-and-definitions); [order of limits and fixed lifetime](../science/receiver-resources.md#fixed-source-lifetime-and-reduced-brightness).

### M22

**The stationary-axis structure.**

- **Central question:** What property of this static generator gives more information than generic Bloch contraction?
- **Understanding target:** Explain why choosing the stationary Bloch direction as the longitudinal axis reveals the exact asymmetry $`A_{u\perp}=-sA_{\perp u}^{T}`$. Understand the purpose of the similarity transform that makes the cross coupling skew, and distinguish it from a physical channel or a norm-preserving basis rotation.
- **Dependencies and story role:** Uses M04–M05 and M19–M21 to identify the model-specific mechanism of the uniform converse.
- **Conceptual connection:** The source's stationary geometry constrains how longitudinal relaxation and tangential coherence can feed each other.
- **Source pointers:** QN §9.2 for optical Bloch dynamics. Project: [stationary-state geometry](../science/long-delay-law.md#2-geometry-of-the-stationary-state); [dissipative similarity transform](../science/long-delay-law.md#3-a-dissipative-similarity-transform).

### M23

**Bounds that survive arbitrary static detuning.**

- **Central question:** How can the proof remain valid when detuning and accumulated rotation become arbitrarily large?
- **Understanding target:** Follow how dissipative estimates and variation of constants control the propagator blocks independently of the tangential rotation rate. Distinguish the unequal small-$`s`$ cross-block scales, the longitudinal relaxation estimate and the removable tangential phase. Understand why a bounded detuning grid cannot establish these claims.
- **Dependencies and story role:** Develops M22 into estimates strong enough for a uniform optimization.
- **Conceptual connection:** The argument controls decay and mixing without expanding in a small detuning or a small rotation angle.
- **Source pointers:** QN §§5.4 and 9.2 for linear master-equation dynamics. Project: [uniform finite-time block estimates](../science/long-delay-law.md#4-uniform-finite-time-block-estimates), including the stated detuning-independent bounds; [numerical checks and their limits](../science/long-delay-law.md#12-reproducible-numerical-checks).

### M24

**Filtering as a mathematical change of scale.**

- **Central question:** How can vanishingly small entanglement be analyzed without losing the terms that determine its sign?
- **Understanding target:** Understand homogeneous concurrence on unnormalized positive matrices and its determinant scaling under local filters. Connect the exact two-qubit entries to the source and propagator scales. Distinguish the mathematical filters used in the proof from a heralded physical protocol with a success probability.
- **Dependencies and story role:** Combines M10–M11, M20 and M23 to prepare a stable asymptotic description near a pure stationary state.
- **Conceptual connection:** Filtering magnifies the relevant small entries while preserving an exact relation to the unconditional concurrence being optimized.
- **Source pointers:** QN §§9.2 and 11.3 provide dynamical and conditional-state context; the filtering lemma is derived in the project. Project: [exact state entries](../science/long-delay-law.md#5-exact-entries-of-the-two-qubit-state); [concurrence under local filtering](../science/long-delay-law.md#6-concurrence-under-local-filtering).

### M25

**Excluding stationary resources that are too large.**

- **Central question:** Why can a source with $`s/a\to\infty`$ not improve the long-delay optimum?
- **Understanding target:** Separate sources whose stationary mixedness stays bounded away from zero from sources with $`s\to0`$ more slowly than $`a`$. Explain why the filtered state tends to a strictly positive product-like matrix in the latter case, making its partial transpose positive and the two-qubit state eventually separable.
- **Dependencies and story role:** Uses M17 and M23–M24 to exclude the parameter region outside the finite-ratio analysis.
- **Conceptual connection:** Optimizing only a plausible weak-drive ansatz would miss this converse; actual eventual separability rules out all divergent-ratio sequences.
- **Source pointers:** QN §§5.4 and 9.2 for relaxation context. Project: [exclusion of large stationary mixedness](../science/long-delay-law.md#7-excluding-sources-with-stationary-mixedness-much-larger-than-a); [finite-time entanglement-breaking bound](../science/driven-qubit.md#a-finite-entanglement-breaking-horizon-for-each-driven-source).

### M26

**The finite-ratio limit and its parabola.**

- **Central question:** What remains when stationary source entanglement and propagation decay are made comparable?
- **Understanding target:** Explain the rescaled positive matrix obtained when $`s/a\to k<\infty`$, including removal of a local tangential phase. Connect continuity of homogeneous concurrence on that finite matrix to $`\frac{C(\sigma_\tau)}{a^2}\longrightarrow\max\{0,k-k^2/2\}`$. Distinguish a vanishing leading concurrence from a separate proof of exact separability.
- **Dependencies and story role:** Uses M23–M24 after the exclusion in M25 to identify the surviving asymptotic competition.
- **Conceptual connection:** The positive linear term and the quadratic penalty express the balance between source resource and loss of usable entanglement during the delay.
- **Source pointers:** QN §9.2 for the source dynamics. Project: [finite-ratio limit and limiting matrix](../science/long-delay-law.md#8-finite-ratio-limit); [physical mechanism](../science/driven-qubit.md#long-delay-consequence-and-its-mechanism).

### M27

**The uniform optimum and its achievers.**

- **Central question:** Why does the limiting parabola prove an optimum over all static drive strengths and detunings?
- **Understanding target:** Connect divergent-ratio exclusion, finite-ratio subsequences and the unique maximum at $`k=1`$. State the optimized law $`C_*(\tau)=(1/2+o(1))e^{-\gamma\tau}`$ and the necessary and sufficient asymptotic condition $`s/a\to1`$. Recognize resonance as one asymptotically optimal choice, not a proved global optimizer at every finite delay.
- **Dependencies and story role:** Integrates M25–M26 to close the source optimization begun in M21.
- **Conceptual connection:** The subsequence argument turns a family of local scaling limits into a uniform upper bound, while the matched receiver and a resonant tuning supply the lower bound.
- **Source pointers:** QN §§9.2 and 12.1 for the source and receiver ingredients. Project: [uniform optimization and optimal tuning](../science/long-delay-law.md#9-uniform-optimization-and-optimal-tuning); [main theorem](../science/long-delay-law.md#1-statement-and-definitions).

### M28

**The weak-source entanglement-breaking horizon.**

- **Central question:** How does the exact disappearance time move as the stationary source is weakened?
- **Understanding target:** Use strict partial-transpose signs on either side of $`k=2`$ and semigroup monotonicity to understand $`\gamma t_{\mathrm{EB}}=2\log(2/s)+o(1)`$ as $`s\to0`$. Distinguish this exact separability threshold from the looser finite-time upper bound. Explain why the exactly undriven source is excluded from the faithful-state horizon equivalence.
- **Dependencies and story role:** Connects M17 and M26–M27 to a second physical consequence of the same scaling structure.
- **Conceptual connection:** Extending the entanglement horizon requires sacrificing stationary source entanglement; the boundary $`\Omega=0`$ has zero stationary score even though its channel has no finite entanglement-breaking time.
- **Source pointers:** QN §9.2. Project: [sharp weak-source horizon](../science/long-delay-law.md#10-sharp-weak-source-entanglement-breaking-horizon); [faithful-state horizon equivalence](../science/causal-bound.md#the-exact-entanglement-horizon).

### M29

**The physical price and the boundaries of the law.**

- **Central question:** What is reduced, consumed or changed when the optimized source operates across a longer delay?
- **Understanding target:** Connect optimal tuning to the decreasing flux $`\gamma\pi_{ee}\sim(\gamma/2)e^{-\gamma\tau/2}`$. Separate a retained entangled register from a repeated-use distribution rate, and state the preparation and control-budget qualifications. Explain the excited-source transient example with concurrence $`e^{-\gamma\tau/2}`$ and why it lies outside stationary operation.
- **Dependencies and story role:** Uses M08, M21 and M27–M28 to translate the mathematical optimum into a physical resource statement.
- **Conceptual connection:** Fixed lifetime, stationary initialization, full output collection and the equal-time score carry real content; changing them can define a different and less restrictive task.
- **Source pointers:** QN §§9.2, 11.2–11.3 and 12.1. Project: [fixed lifetime and reduced brightness](../science/receiver-resources.md#fixed-source-lifetime-and-reduced-brightness); [transient example](../science/receiver-resources.md#why-stationarity-matters-an-explicit-transient-example); [loss and other resources](../science/receiver-resources.md#loss-postselection-and-other-changes-of-resources).

### M30

**Narrative synthesis: an attainable frontier with a sharp stationary tradeoff.**

- **Central question:** What complete scientific claim follows from the causal cut, receiver construction and uniform source analysis together?
- **Understanding target:** Explain the chain from one inaccessible source-evolution interval to a universal channel state, from coherent finite-memory decoding to tightness, and from stationary-axis structure to the sharp all-detuning asymptotic. Keep the general primitive-source envelope separate from the specific driven-qubit law. Identify the established ingredients and the operational optimization added here. Explain why the arbitrary-channel counterexample and the transient example prevent broader readings, and why finite numerical verification supports the proof without replacing it.
- **Dependencies and story role:** Integrates M13–M29 with the complete model of M12 and closes the narrative phase.
- **Conceptual connection:** The contribution links a physical causality restriction, an achievable quantum-information envelope and a model-specific source tradeoff. Its force depends on their connection: the upper bound alone, an absorber alone or a decay curve alone is insufficient.
- **Source pointers:** QN §§3.2, 5.2, 9.2, 11.2 and 12.1 as the common physical foundation. Project: [model and exact claims](../science/model.md), [limits of generic contraction](../science/long-delay-law.md#11-why-contraction-and-stationarity-alone-are-insufficient), [contribution boundary](../references/RELATED_WORK.md#what-is-established-here), [verification scope](../verification/README.md), and [bridge attribution](QUANTUM_NOISE_BRIDGE.md#what-comes-from-where).

## Integrated result and source roles

M12 assembles the physical question; M30 joins its two optimizations. For a fixed stationary primitive source with faithful $`\pi`$, all unconditional equal-time receiver states lie below the delayed stationary-purification state under local processing. Complete coherent access to the purifying outputs makes that bound attainable as a finite-memory supremum. For the specific static driven amplitude-damping qubit, a matched receiver qubit reaches the fixed-source frontier, and optimizing the static source parameters at fixed $`\gamma`$ gives the sharp long-delay coefficient. The source parameters may depend on delay; the theorem does not assert a globally optimal finite-delay resonant drive.

QN supplies the open-system, input-output, trajectory and cascade foundations. The repository supplies the connecting derivations and the uniform source analysis, while its scientific references attribute purification tools, entanglement criteria, absorber constructions, concurrence identities and eventual entanglement breaking to their primary sources. This division keeps the selected anchor focused without substituting its table of contents for the project's argument.

[^qn]: C. W. Gardiner and P. Zoller, *Quantum Noise*, third edition, Springer (2004), ISBN 978-3-540-22301-6. [Publisher edition record](https://link.springer.com/book/9783540223016); [publisher-authorized contents and preview](https://books.google.com.sg/books?id=a_xsT8oGhdgC). The [bridge](QUANTUM_NOISE_BRIDGE.md) gives the selected source route and the notation translation.
