#!/usr/bin/env python3
"""Check matched-dimer and continuous-purification-tracker identities.

Run from the repository root:
    python verification/verify_receivers.py
    python verification/verify_receivers.py --json > receiver-results.json

The checks independently construct physical GKLS generators, source marginals,
and the time-dependent purification gauge. Finite spectral and propagation
checks illustrate the analytic convergence proof; they do not replace it.
No files are written unless standard output is redirected by the caller.
"""

import argparse
import json
import platform

import numpy as np
import scipy
from scipy.linalg import expm, solve_sylvester


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)
TOLERANCE = 2e-8


def adjoint(a):
    return a.conj().T


def lindblad_apply(hamiltonian, jumps, state):
    result = -1j * (hamiltonian @ state - state @ hamiltonian)
    for jump in jumps:
        number = adjoint(jump) @ jump
        result += jump @ state @ adjoint(jump)
        result -= (number @ state + state @ number) / 2
    return result


def liouvillian(hamiltonian, jumps):
    """Column-vectorized density matrices; tensor state order is |A,B>."""
    identity = np.eye(len(hamiltonian))
    result = -1j * (np.kron(identity, hamiltonian)
                    - np.kron(hamiltonian.T, identity))
    for jump in jumps:
        number = adjoint(jump) @ jump
        result += np.kron(jump.conj(), jump)
        result -= (np.kron(identity, number)
                   + np.kron(number.T, identity)) / 2
    return result


def stationary_state(hamiltonian, jumps):
    dimension = len(hamiltonian)
    equations = liouvillian(hamiltonian, jumps)
    equations[0] = np.eye(dimension).reshape(-1, order='F')
    rhs = np.zeros(dimension**2, dtype=complex)
    rhs[0] = 1
    state = np.linalg.solve(equations, rhs).reshape(dimension, dimension, order='F')
    return (state + adjoint(state)) / 2


def positive_sqrt(state):
    values, vectors = np.linalg.eigh((state + adjoint(state)) / 2)
    if values[0] <= 0:
        raise AssertionError(f'Expected positive matrix; smallest eigenvalue {values[0]}')
    return (vectors * np.sqrt(values)) @ adjoint(vectors)


def trace_b(state):
    return np.trace(state.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def norm(a):
    return float(np.linalg.norm(a))


def require_residuals(residuals, label):
    for name, value in residuals.items():
        if value > TOLERANCE:
            raise AssertionError(f'{label}: {name}={value} exceeds {TOLERANCE}')


def dimer_case(gamma, omega, delta):
    ha = (omega * X + delta * Z) / 2
    hb = (omega * X - delta * Z) / 2
    la = np.sqrt(gamma) * LOWER
    jump = np.kron(la, I2) + np.kron(I2, la)
    h = np.kron(ha, I2) + np.kron(I2, hb)
    h += (np.kron(la, adjoint(la)) - np.kron(adjoint(la), la)) / (2j)
    alpha = np.sqrt(2) * omega / (2 * delta + 1j * gamma)
    singlet = np.array([0, -1, 1, 0], dtype=complex) / np.sqrt(2)
    dark = (np.array([1, 0, 0, 0]) + alpha * singlet) / np.sqrt(1 + abs(alpha)**2)
    target = np.outer(dark, dark.conj())
    denominator = gamma**2 + 4 * delta**2 + 2 * omega**2
    pi = np.array([[gamma**2 + 4 * delta**2 + omega**2,
                    omega * (2 * delta + 1j * gamma)],
                   [omega * (2 * delta - 1j * gamma), omega**2]]) / denominator
    residuals = dict(jump_dark=norm(jump @ dark), hamiltonian_dark=norm(h @ dark),
                     marginal=norm(trace_b(target) - pi),
                     stationary_source=norm(lindblad_apply(ha, [la], pi)),
                     stationary_dimer=norm(lindblad_apply(h, [jump], target)))
    # Check the no-feedback identity on a complete operator basis, including
    # non-Hermitian matrix units, rather than only on the dark state.
    autonomy = 0.0
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1
            autonomy = max(autonomy, norm(trace_b(lindblad_apply(h, [jump], unit))
                                         - lindblad_apply(ha, [la], trace_b(unit))))
    residuals['source_autonomy'] = autonomy
    if omega > 0:
        coefficient = dark.reshape(2, 2)
        unitary = np.linalg.solve(positive_sqrt(pi), coefficient).T
        residuals['purification_unitary'] = norm(adjoint(unitary) @ unitary - I2)
        residuals['purification_identity'] = norm(
            np.kron(I2, unitary) @ positive_sqrt(pi).reshape(-1) - dark)
    require_residuals(residuals, 'dimer')

    generator = liouvillian(h, [jump])
    eigenvalues = np.linalg.eigvals(generator)
    zeros = abs(eigenvalues) < 1e-9
    if int(np.count_nonzero(zeros)) != 1:
        raise AssertionError('The sampled dimer does not have exactly one zero mode')
    gap = float(-max(eigenvalues[~zeros].real))
    if gap <= 0:
        raise AssertionError('The sampled dimer has a nondecaying nonstationary mode')
    initial = np.kron(pi, np.diag([0., 1.]))
    elapsed = 40 / gap
    evolved = (expm(elapsed * generator) @ initial.reshape(-1, order='F')).reshape(4, 4, order='F')
    difference = evolved - target
    convergence_error = float(sum(abs(np.linalg.eigvalsh((difference + adjoint(difference)) / 2))))
    if convergence_error > TOLERANCE:
        raise AssertionError(f'Dimer convergence check failed: {convergence_error}')
    return dict(gamma=gamma, omega=omega, delta=delta, residuals=residuals,
                zero_modes=int(np.count_nonzero(zeros)), spectral_gap=gap,
                propagation_time=elapsed, final_trace_norm_error=convergence_error)


def tracker_case(name, h, jumps, elapsed):
    pi = stationary_state(h, jumps)
    phi = positive_sqrt(pi).reshape(-1)  # row vectorization of purification matrix
    chi0 = np.outer(phi, phi.conj())
    hs = np.kron(h, I2)
    vs = [np.kron(jump, I2) for jump in jumps]
    generator = liouvillian(hs, vs)
    chi = (expm(elapsed * generator) @ chi0.reshape(-1, order='F')).reshape(4, 4, order='F')
    chi = (chi + adjoint(chi)) / 2
    c = positive_sqrt(chi)
    ci = np.linalg.inv(c)
    cdot = solve_sylvester(c, c, lindblad_apply(hs, vs, chi))
    number = sum(adjoint(v) @ v for v in vs)
    k = -1j * hs - number / 2
    f = sum(v @ chi @ adjoint(v) for v in vs)
    receiver_jumps = [-(ci @ v @ c).T for v in vs]
    q = ci @ (cdot - k @ c - f @ ci)
    km = q.T
    hm = 0.5j * (km - adjoint(km))
    receiver_number = sum(adjoint(j) @ j for j in receiver_jumps)

    # A separately expanded Hamiltonian exposes the derivative of the chosen
    # canonical purification gauge. Omitting this term is not a valid general
    # time-dependent tracker.
    gauge = (0.5j * (ci @ cdot - cdot @ ci)).T
    expanded_hm = (-0.5 * (ci @ hs @ c + c @ hs @ ci)
                   + 0.25j * (ci @ number @ c - c @ number @ ci)).T + gauge
    identity = np.eye(4)
    total_h = np.kron(hs, identity) + np.kron(identity, hm)
    total_k = np.kron(k, identity) + np.kron(identity, km)
    total_jumps = []
    for v, j in zip(vs, receiver_jumps):
        total_h += (np.kron(v, adjoint(j)) - np.kron(adjoint(v), j)) / (2j)
        total_k -= np.kron(v, adjoint(j))
        total_jumps.append(np.kron(v, identity) + np.kron(identity, j))
    vector, derivative = c.reshape(-1), cdot.reshape(-1)
    target = np.outer(vector, vector.conj())
    target_derivative = np.outer(derivative, vector.conj()) + np.outer(vector, derivative.conj())
    residuals = dict(
        sqrt=norm(c @ c - chi),
        sqrt_derivative=norm(cdot @ c + c @ cdot - lindblad_apply(hs, vs, chi)),
        gkls_drift=norm(km + adjoint(km) + receiver_number),
        expanded_hamiltonian=norm(hm - expanded_hm),
        total_no_jump=norm(total_k + 1j * total_h
                           + sum(adjoint(j) @ j for j in total_jumps) / 2),
        dark=max(norm(j @ vector) for j in total_jumps),
        vector_drift=norm(total_k @ vector - derivative),
        density_derivative=norm(lindblad_apply(total_h, total_jumps, target) - target_derivative))
    require_residuals(residuals, f'tracker {name}')
    ungauged_error = norm(lindblad_apply(total_h - np.kron(identity, gauge), total_jumps, target)
                         - target_derivative)
    return dict(name=name, elapsed=elapsed, output_channels=len(jumps),
                smallest_chi_eigenvalue=float(np.linalg.eigvalsh(chi)[0]),
                residuals=residuals, gauge_norm=norm(gauge),
                derivative_error_without_gauge=ungauged_error)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='emit a machine-readable report')
    args = parser.parse_args()
    dimers = [dimer_case(*parameters) for parameters in
              [(1., 0., .3), (1., .7, .3), (.8, 2., -4.), (1.3, .2, -.4)]]
    trackers = [
        tracker_case('driven_decay', (.7 * X + .3 * Z) / 2, [LOWER], 1.2),
        tracker_case('detuned_decay', (2 * X - 4 * Z) / 2, [LOWER], 1.1),
        tracker_case('three_channel_thermal', .6 * X - .2 * Y + .35 * Z,
                     [np.sqrt(.8) * LOWER, np.sqrt(.3) * adjoint(LOWER), np.sqrt(.1) * Z], .7),
        tracker_case('three_channel_unital', .4 * X + .7 * Y + .1 * Z,
                     [np.sqrt(.3) * X, np.sqrt(.2) * Y, np.sqrt(.15) * Z], .6)]
    if max(row['derivative_error_without_gauge'] for row in trackers) < 1e-4:
        raise AssertionError('The cases do not meaningfully test the time-dependent gauge')
    report = dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                  floating_point='complex128', absolute_residual_tolerance=TOLERANCE,
                  matched_dimers=dimers, continuous_trackers=trackers,
                  status='all receiver identity and finite convergence assertions passed')
    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(report['status'])
    print(f"numpy {np.__version__}; scipy {scipy.__version__}; tolerance {TOLERANCE:g}")
    for row in dimers:
        print(f"Dimer gamma={row['gamma']:g}, Omega={row['omega']:g}, Delta={row['delta']:g}: "
              f"gap={row['spectral_gap']:.6g}, residual={max(row['residuals'].values()):.3g}, "
              f"late error={row['final_trace_norm_error']:.3g}")
    for row in trackers:
        print(f"Tracker {row['name']}: residual={max(row['residuals'].values()):.3g}, "
              f"error without gauge={row['derivative_error_without_gauge']:.3g}")
    print('Use --json for individual residuals and runtime versions.')


if __name__ == '__main__':
    main()
