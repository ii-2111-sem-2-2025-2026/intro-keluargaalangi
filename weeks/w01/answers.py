"""answers_solution.py — w01 (REFERENCE SOLUTION)

Instructor-only reference solution for validating the pipeline.
"""


from __future__ import annotations

import math
import numpy as np
from scipy.stats import norm


def q01() -> float:
    # At least one head in 3 flips: 1 - P(all tails) = 1 - (1/2)^3
    return 1.0 - (0.5 ** 3)


def q02() -> int:
    # Choose 3 from 10: C(10,3)
    return math.comb(10, 3)


def q03() -> float:
    # P(Python | R) = P(P ∩ R) / P(R) = 10/18
    return 10 / 18


def q04() -> float:
    pD = 0.01
    p_pos_given_D = 0.95
    p_neg_given_notD = 0.90
    p_pos_given_notD = 1 - p_neg_given_notD

    p_pos = p_pos_given_D * pD + p_pos_given_notD * (1 - pD)
    return (p_pos_given_D * pD) / p_pos


def q05() -> float:
    # E[X] for values 0,1,2,3 with probs 0.1,0.2,0.3,0.4
    return 0*0.1 + 1*0.2 + 2*0.3 + 3*0.4


def q06() -> list[float]:
    # Binomial pmf n=4 p=0.3
    n, p = 4, 0.3
    pmf = []
    for k in range(n + 1):
        pmf.append(math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)))
    return pmf


def q07() -> float:
    # Var of fair die values 1..6
    values = [1, 2, 3, 4, 5, 6]
    mu = sum(values) / 6
    return sum((x - mu) ** 2 for x in values) / 6


def q08() -> float:
    # corr = cov / (sx * sy)
    cov = 2
    sx = math.sqrt(9)
    sy = math.sqrt(16)
    return cov / (sx * sy)


def q09() -> float:
    # P(8 < X < 12) for N(10,2)
    return float(norm.cdf(12, loc=10, scale=2) - norm.cdf(8, loc=10, scale=2))


def q10() -> float:
    # margin of error = z * sigma / sqrt(n)
    z = 1.96
    sigma = 4
    n = 25
    return z * sigma / math.sqrt(n)


def q11() -> float:
    # two-sided p = 2*(1 - Phi(|z|))
    z = 2.1
    return float(2 * (1 - norm.cdf(abs(z))))


def q12() -> float:
    rng = np.random.default_rng(123)
    z = rng.standard_normal(200_000)
    return float((z > 1.5).mean())
