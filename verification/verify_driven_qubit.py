#!/usr/bin/env python3
"""High-precision verification of the stationary driven-qubit delay law.

Run from the repository root:
    python verification/verify_driven_qubit.py
    python verification/verify_driven_qubit.py --json > verification-results.json

Independent constructions:
  * a physical 4-by-4 Lindblad superoperator with column vectorization;
  * a physical 3-by-3 Bloch propagator and its Choi formula;
  * the exact stationary-axis two-qubit entries in long-delay-law.md.

The assertions concern exact identities and finite-time inequalities. Tables
report asymptotic convergence without treating a finite grid as an optimization
proof. No files are written unless the caller redirects standard output.
"""

import argparse
import json
import platform

import mpmath as mp


def conj(a):
    return a.apply(mp.conj)


def dag(a):
    return conj(a.T)


def kron(a, b):
    out = mp.zeros(a.rows * b.rows, a.cols * b.cols)
    for i in range(out.rows):
        for j in range(out.cols):
            out[i, j] = a[i // b.rows, j // b.cols] * b[i % b.rows, j % b.cols]
    return out


def maxabs(a):
    return max(abs(v) for v in a)


def opnorm(a):
    return mp.svd(a, compute_uv=False)[0]


def cross(a, b):
    return mp.matrix([a[1] * b[2] - a[2] * b[1],
                      a[2] * b[0] - a[0] * b[2],
                      a[0] * b[1] - a[1] * b[0]])


def paulis():
    return (mp.eye(2), mp.matrix([[0, 1], [1, 0]]),
            mp.matrix([[0, -1j], [1j, 0]]), mp.diag([1, -1]))


def vec(a):
    return mp.matrix([a[i, j] for j in range(a.cols) for i in range(a.rows)])


def apply_source(evolution, state):
    """Apply a column-vectorized source channel to A in ordering |A,B>."""
    out = mp.zeros(4)
    for b in range(2):
        for d in range(2):
            block = mp.matrix([state[2 * a + b, 2 * c + d]
                               for c in range(2) for a in range(2)])
            evolved = evolution * block
            for a in range(2):
                for c in range(2):
                    out[2 * a + b, 2 * c + d] = evolved[a + 2 * c]
    return out


def partial_transpose_b(state):
    out = mp.zeros(4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    out[2 * a + d, 2 * c + b] = state[2 * a + b, 2 * c + d]
    return out


def concurrence(state):
    """Homogeneous concurrence from Hermitian eigenvectors and singular values.

    If state=K K^dagger, the singular values of K^T(Y tensor Y)K are the
    Wootters roots. This avoids directly diagonalizing state*spinflip(state).
    Tiny negative eigenvalues are clipped only within the working-precision
    roundoff tolerance; larger negativity raises an error.
    """
    state = (state + dag(state)) / 2
    values, vectors = mp.eigh(state)
    tolerance = mp.power(10, -mp.mp.dps + 15) * max(1, maxabs(state))
    if min(values) < -tolerance:
        raise ArithmeticError("Concurrence input is not PSD at working precision")
    factor = vectors * mp.diag([mp.sqrt(max(0, v)) for v in values])
    y = paulis()[2]
    roots = mp.svd(factor.T * kron(y, y) * factor, compute_uv=False)
    return max(mp.mpf(0), roots[0] - sum(roots[i] for i in range(1, 4)))


def assert_small(value, label, scale=1):
    tolerance = mp.power(10, -(mp.mp.dps // 2)) * max(1, scale)
    if abs(value) > tolerance:
        raise AssertionError(f"{label}: residual {mp.nstr(value, 12)}")


def assert_bound(observed, bound, label):
    tolerance = mp.power(10, -(mp.mp.dps // 2))
    if observed > bound * (1 + tolerance) + tolerance:
        raise AssertionError(f"{label}: observed {mp.nstr(observed, 12)}, "
                             f"bound {mp.nstr(bound, 12)}")


def stationary_model(gamma, omega, delta):
    gamma, omega, delta = map(mp.mpf, (gamma, omega, delta))
    identity, x, y, z = paulis()
    lowering = mp.matrix([[0, 1], [0, 0]])
    number = dag(lowering) * lowering
    h = (omega * x + delta * z) / 2
    liouvillian = (-1j * (kron(identity, h) - kron(h.T, identity))
                   + gamma * (kron(conj(lowering), lowering)
                              - (kron(identity, number)
                                 + kron(number.T, identity)) / 2))
    denominator = gamma**2 + 4 * delta**2 + 2 * omega**2
    pi = mp.matrix([[gamma**2 + 4 * delta**2 + omega**2,
                     omega * (2 * delta + 1j * gamma)],
                    [omega * (2 * delta - 1j * gamma), omega**2]]) / denominator
    r = mp.matrix([4 * delta * omega, -2 * gamma * omega,
                   gamma**2 + 4 * delta**2]) / denominator
    s = 2 * omega**2 / denominator
    p = s**2 / (2 * (1 + mp.sqrt(1 - s**2)))
    a_physical = mp.matrix([[-gamma / 2, -delta, 0],
                            [delta, -gamma / 2, -omega],
                            [0, omega, -gamma]])
    return dict(gamma=gamma, omega=omega, delta=delta, pi=pi, r=r,
                s=s, p=p, q=1-p, L=liouvillian, A=a_physical)


def stationary_frame(model):
    """Return Bloch rotation R=(w,v,u) and its qubit representative U."""
    s, r = model['s'], model['r']
    u = r / mp.sqrt(1 - s**2)
    cosine = mp.sqrt((1 - s) / (1 + s))
    sine = mp.sqrt(2 * s / (1 + s))
    v = (mp.matrix([0, 0, 1]) - cosine * u) / sine
    w = cross(v, u)
    rotation = mp.matrix([[w[i], v[i], u[i]] for i in range(3)])
    _, x, y, z = paulis()
    plus = mp.matrix([mp.sqrt((1 + u[2]) / 2),
                      (u[0] + 1j*u[1]) / mp.sqrt(2 * (1 + u[2]))])
    minus = (w[0]*x + w[1]*y + w[2]*z) * plus
    unitary = mp.matrix([[plus[0], minus[0]], [plus[1], minus[1]]])
    return rotation, unitary


def signed_state_entries(t, s, p):
    """Exact Section 5 state, in axes (w,v,u) and ordering 00,01,10,11."""
    q = 1 - p
    x = s * (t[2, 0] + 1j*t[2, 1]) / 4
    y = s**2 * (t[0, 2] - 1j*t[1, 2]) / 4
    w = s * (t[0, 0] + t[1, 1] + 1j*(t[0, 1] - t[1, 0])) / 4
    z = s * (t[0, 0] - t[1, 1] - 1j*(t[0, 1] + t[1, 0])) / 4
    mid = p*q*(1 - t[2, 2])
    return mp.matrix([[q*q + p*q*t[2, 2], x, y, w],
                      [mp.conj(x), mid, z, -y],
                      [mp.conj(y), mp.conj(z), mid, -x],
                      [mp.conj(w), -mp.conj(y), -mp.conj(x),
                       p*p + p*q*t[2, 2]]])


def case(gamma, omega, delta, time):
    model = stationary_model(gamma, omega, delta)
    time = mp.mpf(time)
    s, p, q = model['s'], model['p'], model['q']
    if not (0 < s < 1):
        raise ValueError("stationary-axis verification requires 0<s<1")
    rotation, unitary = stationary_frame(model)
    evolution = mp.expm(time * model['L'])
    t_physical = mp.expm(time * model['A'])
    t_frame = rotation.T * t_physical * rotation
    identity, x, y, z = paulis()
    pauli = [x, y, z]
    phi = mp.matrix([1, 0, 0, 1]) / mp.sqrt(2)
    choi = apply_source(evolution, phi * dag(phi))
    displacement = (mp.eye(3) - t_physical) * model['r']
    choi_bloch = mp.eye(4)
    for i in range(3):
        choi_bloch += displacement[i] * kron(pauli[i], identity)
        for j in range(3):
            choi_bloch += t_physical[i, j] * kron(pauli[i], pauli[j].T)
    choi_bloch /= 4
    root_pi = unitary * mp.diag([mp.sqrt(q), mp.sqrt(p)]) * dag(unitary)
    purification = mp.matrix([root_pi[i, j] for i in range(2) for j in range(2)])
    sigma_physical = apply_source(evolution, purification * dag(purification))
    to_frame = kron(dag(unitary), unitary.T)
    sigma_frame = to_frame * sigma_physical * dag(to_frame)
    sigma_formula = signed_state_entries(t_frame, s, p)
    gamma = model['gamma']
    kappa = model['delta'] * mp.sqrt((1 + s) / (1 - s))
    b = gamma * mp.sqrt(2*s) / ((1+s)*mp.sqrt(1-s))
    d = gamma / (1+s)
    a_expected = mp.matrix([[-gamma/2, -kappa, 0],
                            [kappa, -gamma*(1+3*s)/(2*(1+s)), -b],
                            [0, s*b, -d]])
    a = mp.exp(-gamma*time/2)
    phase = mp.diag([mp.exp(1j*kappa*time/2), mp.exp(-1j*kappa*time/2)])
    phase_both = kron(phase, identity)
    sigma_rotated = phase_both * sigma_frame * dag(phase_both)
    filter_both = kron(mp.diag([a, 1]), mp.diag([a, 1]))
    filtered = filter_both * sigma_rotated * filter_both / a**4
    return dict(**model, time=time, a=a, kappa=kappa, b=b, d=d,
                rotation=rotation, unitary=unitary, T=t_frame,
                generator_frame=rotation.T*model['A']*rotation,
                generator_expected=a_expected, choi=choi, choi_bloch=choi_bloch,
                sigma=sigma_frame, sigma_formula=sigma_formula, filtered=filtered)


def target_matrix(k):
    k = mp.mpf(k)
    return mp.matrix([[1, 0, 0, k/2], [0, k*k/4, 0, 0],
                      [0, 0, k*k/4, 0], [k/2, 0, 0, k*k/4+k**4/16]])


def check_identities(data):
    errors = dict(
        stationary=maxabs(data['L'] * vec(data['pi'])),
        stationary_axis=maxabs(data['generator_frame']-data['generator_expected']),
        unitary=maxabs(dag(data['unitary'])*data['unitary']-mp.eye(2)),
        choi_construction=maxabs(data['choi']-data['choi_bloch']),
        signed_state_entries=maxabs(data['sigma']-data['sigma_formula']))
    for label, error in errors.items():
        assert_small(error, label)
    c = concurrence(data['sigma'])
    cj = concurrence(data['choi'])
    cf = concurrence(data['filtered'])
    errors['choi_factorization'] = abs(c-data['s']*cj)
    errors['filter_identity'] = abs(cf-c/data['a']**2)
    assert_small(errors['choi_factorization'], 'Choi concurrence factorization')
    assert_small(errors['filter_identity'], 'local filter covariance', cf)
    return errors, c


def finite_time_checks():
    parameters = [('1', '.4', '0', '2'), ('.7', '.3', '1.1', '3.2'),
                  ('1', '.01', '10', '4'), ('1', '4', '3', '1.7'),
                  ('1', '1e-6', '2', '12')]
    rows = []
    for gamma, omega, delta, time in parameters:
        data = case(gamma, omega, delta, time)
        errors, c = check_identities(data)
        s, a, t = data['s'], data['a'], data['T']
        gamma, time = data['gamma'], data['time']
        g = gamma*(1-s)/(2*(1+s))
        beta = mp.sqrt(s)*data['b']
        ks = beta/g
        f1 = -mp.expm1(-g*time)
        f2 = f1-g*time*mp.exp(-g*time)
        angle = data['kappa']*time
        rotation = mp.matrix([[mp.cos(angle), -mp.sin(angle)],
                              [mp.sin(angle), mp.cos(angle)]])
        observations = dict(contraction=opnorm(t),
                            longitudinal_to_tangent=opnorm(t[:2, 2:3]),
                            tangent_to_longitudinal=opnorm(t[2:3, :2]),
                            longitudinal_error=abs(t[2, 2]-mp.exp(-data['d']*time)),
                            tangent_rotation_error=opnorm(t[:2, :2]/a-rotation))
        bounds = dict(contraction=a,
                      longitudinal_to_tangent=ks*a*f1/mp.sqrt(s),
                      tangent_to_longitudinal=mp.sqrt(s)*ks*a*f1,
                      longitudinal_error=ks**2*a*f2,
                      tangent_rotation_error=gamma*s*time/(1+s)
                      + beta*ks*(time-f1/g))
        for label, observed in observations.items():
            assert_bound(observed, bounds[label], label)
        rows.append(dict(gamma=gamma, omega=data['omega'], delta=data['delta'],
                         time=time, s=s, concurrence=c, identity_errors=errors,
                         bound_fractions={label: observations[label]/bounds[label]
                                          for label in bounds}))
    return rows


def fixed_ratio_case(time, k, delta=0):
    time, k, delta = map(mp.mpf, (time, k, delta))
    a = mp.exp(-time/2)
    if k == 0:
        return dict(time=time, k=k, delta=delta, s=mp.mpf(0), omega=mp.mpf(0),
                    scaled_concurrence=mp.mpf(0), limiting_concurrence=mp.mpf(0))
    s = k*a
    omega = mp.sqrt((1+4*delta**2)*s/(2*(1-s)))
    data = case(1, omega, delta, time)
    errors, c = check_identities(data)
    return dict(time=time, k=k, delta=delta, s=s, omega=omega,
                scaled_concurrence=c/a**2,
                limiting_concurrence=max(mp.mpf(0), k-k*k/2),
                filtered_matrix_error=opnorm(data['filtered']-target_matrix(k)),
                filtered_pt_min=mp.eigh(partial_transpose_b(data['filtered']))[0][0],
                largest_identity_error=max(errors.values()))


def finite_ratio_samples():
    return [fixed_ratio_case(time, mp.mpf(j)/4)
            for time in (10, 20, 40) for j in range(11)]


def detuning_samples():
    return [fixed_ratio_case(time, 1, delta)
            for time in (20, 40, 60) for delta in (0, 1, 100)]


def horizon_samples():
    rows = []
    for s_text in ('1e-2', '1e-4', '1e-8'):
        s = mp.mpf(s_text)
        for delta in (0, 10):
            for k_text in ('1.8', '2.2'):
                k = mp.mpf(k_text)
                time = 2*mp.log(k/s)
                row = fixed_ratio_case(time, k, delta)
                row['leading_horizon'] = 2*mp.log(2/s)
                row['limiting_pt_min'] = k*k/4-k/2
                # At the smallest sampled s, the strict signs provide a
                # meaningful finite-precision check on the EB-side distinction.
                if s_text == '1e-8':
                    if row['filtered_pt_min'] * row['limiting_pt_min'] <= 0:
                        raise AssertionError('Incorrect side of sampled EB transition')
                rows.append(row)
    return rows


def serializable(value):
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [serializable(item) for item in value]
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    return mp.nstr(value, 30)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dps', type=int, default=80,
                        help='decimal working precision; at least 80 (default: 80)')
    parser.add_argument('--json', action='store_true', help='emit machine-readable tables')
    args = parser.parse_args()
    if args.dps < 80:
        parser.error('At least 80 digits are required for the default time=60 cases.')
    mp.mp.dps = args.dps
    report = dict(python=platform.python_version(), mpmath=mp.__version__,
                  decimal_precision=args.dps, finite_time_checks=finite_time_checks(),
                  finite_ratio_samples=finite_ratio_samples(),
                  detuning_samples=detuning_samples(), horizon_samples=horizon_samples(),
                  status='all exact-identity and finite-bound assertions passed')
    if args.json:
        print(json.dumps(serializable(report), indent=2))
        return
    print(report['status'])
    print(f"mpmath {mp.__version__}; decimal precision {args.dps}")
    print('\nFinite-ratio samples: gamma=1, Delta=0, s=k*exp(-time/2)')
    print(' time      k          C/exp(-time)           limit')
    for row in report['finite_ratio_samples']:
        print(f"{int(row['time']):5d} {mp.nstr(row['k'], 4):>6} "
              f"{mp.nstr(row['scaled_concurrence'], 18):>24} "
              f"{mp.nstr(row['limiting_concurrence'], 8):>12}")
    print('\nDetuning samples at k=1:')
    for row in report['detuning_samples']:
        print(f"time={mp.nstr(row['time'], 4):>4}, Delta={mp.nstr(row['delta'], 5):>6}, "
              f"C/exp(-time)={mp.nstr(row['scaled_concurrence'], 20)}")
    print('\nUse --json for identity residuals, finite-bound fractions, and PPT diagnostics.')


if __name__ == '__main__':
    main()
