#!/usr/bin/env python3
"""Numerical seed checks for five equal masses, not a census or certificate."""
import json
import math


def polygon(n):
    return [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(n)]


def check(points):
    n = len(points)
    centre = tuple(sum(p[d] for p in points) / n for d in range(2))
    x = [tuple(p[d] - centre[d] for d in range(2)) for p in points]
    force = []
    for i, a in enumerate(x):
        f = [0., 0.]
        for j, b in enumerate(x):
            if i == j:
                continue
            delta = [b[d] - a[d] for d in range(2)]
            r2 = sum(v*v for v in delta)
            if r2 == 0:
                raise ValueError('colliding points')
            for d in range(2):
                f[d] += delta[d] / r2**1.5
        force.append(f)
    inertia = sum(v*v for a in x for v in a)
    if inertia == 0:
        raise ValueError('zero inertia')
    rate = -sum(a[d] * f[d] for a, f in zip(x, force) for d in range(2)) / inertia
    residual = max(math.hypot(*(f[d] + rate*a[d] for d in range(2))) for a, f in zip(x, force))
    return {'masses': n, 'lambda': rate, 'max_force_residual': residual}


def self_check():
    for n in (3, 4, 5, 6):
        result = check(polygon(n))
        reference = sum(1 / (4 * math.sin(math.pi*k/n)) for k in range(1, n))
        assert abs(result['lambda'] - reference) < 1e-12
        assert result['max_force_residual'] < 1e-12
    square_centre = polygon(4) + [(0., 0.)]
    assert check(square_centre)['max_force_residual'] < 1e-12
    perturbed = polygon(5)
    perturbed[0] = (1.01, 0.)
    assert check(perturbed)['max_force_residual'] > 1e-3
    try:
        check([(0., 0.), (0., 0.)])
    except ValueError:
        pass
    else:
        raise AssertionError('collision accepted')


if __name__ == '__main__':
    self_check()
    print(json.dumps({'status': 'numerical seeds only; no completeness or existence certificate',
                      'regular_pentagon': check(polygon(5)),
                      'square_and_centre': check(polygon(4) + [(0., 0.)])}, indent=2))
