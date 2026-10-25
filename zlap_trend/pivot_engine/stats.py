"""Small statistics helpers (stdlib only, seeded for reproducible reports)."""
from __future__ import annotations

import random


def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def bootstrap_ci(xs: list[float], runs: int = 2000, alpha: float = 0.05, seed: int = 1) -> tuple | None:
    """Percentile bootstrap CI of the mean."""
    if len(xs) < 2:
        return None
    rng = random.Random(seed)
    n = len(xs)
    means = sorted(sum(rng.choice(xs) for _ in range(n)) / n for _ in range(runs))
    return (round(means[int(runs * alpha / 2)], 3), round(means[int(runs * (1 - alpha / 2)) - 1], 3))


def bootstrap_diff_ci(a: list[float], b: list[float], runs: int = 2000, alpha: float = 0.05,
                      seed: int = 2) -> tuple | None:
    """CI of mean(b) - mean(a) with independent resampling of both groups."""
    if len(a) < 2 or len(b) < 2:
        return None
    rng = random.Random(seed)
    diffs = sorted(mean([rng.choice(b) for _ in b]) - mean([rng.choice(a) for _ in a]) for _ in range(runs))
    return (round(diffs[int(runs * alpha / 2)], 3), round(diffs[int(runs * (1 - alpha / 2)) - 1], 3))


def max_drawdown(rs: list[float]) -> float:
    """Largest peak-to-trough drop of the cumulative sum (in the units of rs)."""
    peak = cum = dd = 0.0
    for r in rs:
        cum += r
        peak = max(peak, cum)
        dd = max(dd, peak - cum)
    return dd
