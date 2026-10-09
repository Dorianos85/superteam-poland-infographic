"""Pure-python indicators and structure primitives."""
from __future__ import annotations

from .models import Candle, Line, Swing


def atr(candles: list[Candle], period: int = 14) -> list[float | None]:
    """Wilder ATR; None until enough data."""
    out: list[float | None] = [None] * len(candles)
    if len(candles) <= period:
        return out
    trs = []
    for i, c in enumerate(candles):
        if i == 0:
            trs.append(c.h - c.l)
        else:
            pc = candles[i - 1].c
            trs.append(max(c.h - c.l, abs(c.h - pc), abs(c.l - pc)))
    value = sum(trs[1:period + 1]) / period
    out[period] = value
    for i in range(period + 1, len(candles)):
        value = (value * (period - 1) + trs[i]) / period
        out[i] = value
    return out


def atr_at(candles: list[Candle], idx: int, period: int = 14) -> float:
    values = atr(candles[: idx + 1], period)
    v = values[idx] if idx < len(values) else None
    if v is None:  # fall back to mean range
        window = candles[max(0, idx - period): idx + 1]
        return sum(c.h - c.l for c in window) / max(1, len(window))
    return v


def last_atr(candles: list[Candle], period: int = 14) -> float:
    return atr_at(candles, len(candles) - 1, period)


def sma(values: list[float], period: int) -> float | None:
    if len(values) < period or period <= 0:
        return None
    return sum(values[-period:]) / period


def rsi(candles: list[Candle], period: int = 14) -> float | None:
    if len(candles) <= period:
        return None
    gains = losses = 0.0
    closes = [c.c for c in candles]
    for i in range(1, period + 1):
        d = closes[i] - closes[i - 1]
        gains += max(d, 0)
        losses += max(-d, 0)
    ag, al = gains / period, losses / period
    for i in range(period + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        ag = (ag * (period - 1) + max(d, 0)) / period
        al = (al * (period - 1) + max(-d, 0)) / period
    if al == 0:
        return 100.0
    return 100 - 100 / (1 + ag / al)


def pct_change(a: float, b: float) -> float:
    return (b - a) / a * 100 if a else 0.0


def return_over(candles: list[Candle], bars: int) -> float | None:
    """% return of the last close vs the close `bars` candles earlier."""
    if len(candles) <= bars:
        return None
    return pct_change(candles[-1 - bars].c, candles[-1].c)


def find_swings(candles: list[Candle], left: int, right: int | None = None) -> list[Swing]:
    """Fractal swings. A swing is confirmed only once `right` candles closed after it.

    Highs use strict inequality on the left and non-strict on the right so a
    flat top produces one swing (the first bar of the plateau).
    """
    right = left if right is None else right
    swings: list[Swing] = []
    n = len(candles)
    for i in range(left, n - right):
        c = candles[i]
        lw = candles[i - left:i]
        rw = candles[i + 1:i + 1 + right]
        if all(c.h > x.h for x in lw) and all(c.h >= x.h for x in rw):
            swings.append(Swing(i, c.t, c.h, "H"))
        if all(c.l < x.l for x in lw) and all(c.l <= x.l for x in rw):
            swings.append(Swing(i, c.t, c.l, "L"))
    swings.sort(key=lambda s: (s.idx, s.kind))
    _label(swings)
    return swings


def _label(swings: list[Swing]) -> None:
    last = {"H": None, "L": None}
    for s in swings:
        prev = last[s.kind]
        if prev is not None:
            if s.kind == "H":
                s.label = "HH" if s.price > prev.price else "LH"
            else:
                s.label = "HL" if s.price > prev.price else "LL"
        last[s.kind] = s


def highs(swings: list[Swing]) -> list[Swing]:
    return [s for s in swings if s.kind == "H"]


def lows(swings: list[Swing]) -> list[Swing]:
    return [s for s in swings if s.kind == "L"]


def line_through(a: Swing, b: Swing, interval_ms: int) -> Line:
    """Line anchored at the middle of the two swing candles."""
    half = interval_ms // 2
    return Line(a.t + half, a.price, b.t + half, b.price)


def index_at_or_after(candles: list[Candle], t: int) -> int | None:
    for i, c in enumerate(candles):
        if c.t >= t:
            return i
    return None


def index_containing(candles: list[Candle], t: int) -> int | None:
    """Index of the candle whose [open, close) interval contains t."""
    lo, hi = 0, len(candles) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        c = candles[mid]
        if c.t <= t < c.close_time:
            return mid
        if t < c.t:
            hi = mid - 1
        else:
            lo = mid + 1
    return None


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def interp(x: float, points: list[tuple[float, float]]) -> float:
    """Piecewise-linear interpolation over sorted (x, y) points, clamped at ends."""
    if x <= points[0][0]:
        return points[0][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return points[-1][1]
