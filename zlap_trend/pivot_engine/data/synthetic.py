"""Deterministic synthetic futures market.

Used for offline demos, tests and for exercising the full pipeline
(backtest -> journal -> self-improvement) without network access.

Each symbol is described by price waypoints ``(day, multiplier, volume_mult)``.
15-minute candles are generated around the waypoint path with seeded noise and
aggregated to 1H / 4H / 1D.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field

from ..indicators import interp
from ..models import INTERVAL_MS, Candle
from .base import MarketDataProvider, Ticker

DAY_MS = INTERVAL_MS["1d"]
BAR_MS = INTERVAL_MS["15m"]
# Fixed epoch so the demo is reproducible: 2026-08-10 00:00 UTC
EPOCH_MS = 1786320000000


@dataclass
class SymbolSpec:
    symbol: str
    base_price: float
    waypoints: list[tuple[float, float, float]]  # (day, price multiplier, volume multiplier)
    base_volume_usd: float = 40_000_000.0  # per day
    noise: float = 0.0012
    wick: float = 0.0018
    funding_pct: float = 0.01
    oi_change_24h_pct: float = 0.0
    seed: int = 1
    meta: dict = field(default_factory=dict)


def _uptrend_into(offset: float, start_mult: float = 0.62, cycle: float = 4.0,
                  vol: float = 1.0) -> list[tuple[float, float, float]]:
    """Zig-zag uptrend (HH/HL) ending with a higher low of 1.0 at `offset` days."""
    pts = []
    k = 0
    while True:
        d_low = offset - cycle * k
        low = 1.0 * (0.955 ** k)
        if d_low < 0 or low < start_mult:
            break
        pts.append((d_low, low, vol))
        pts.append((d_low - cycle * 0.375, low * 1.045, vol * 1.1))
        k += 1
    pts.append((0.0, pts[-1][1] * 0.97 if pts else start_mult, vol))
    pts.sort()
    return [p for p in pts if p[0] >= 0]


# Relative-day template of IMPULSE -> CORRECTION (3 lower highs). Prices are
# multipliers of the impulse low.
_IMPULSE = [(0.0, 1.00, 1.2), (3.5, 1.17, 2.2)]
_CORRECTION = [(4.5, 1.10, 0.7), (5.5, 1.145, 0.6), (6.5, 1.09, 0.6), (7.5, 1.125, 0.55),
               (8.5, 1.085, 0.55), (9.5, 1.105, 0.5), (10.5, 1.07, 0.5)]

STAGE_TAILS: dict[str, list[tuple[float, float, float]]] = {
    "impulse": [(4.3, 1.13, 0.8)],
    "correction": _CORRECTION[:-1] + [(10.5, 1.075, 0.5), (11.0, 1.079, 0.45)],
    "pivot_fresh": _CORRECTION + [(11.3, 1.082, 0.9), (11.6, 1.096, 1.0)],
    "retest_wait": _CORRECTION + [(11.5, 1.096, 2.6), (12.0, 1.118, 2.0), (12.3, 1.109, 0.9)],
    "long_ready": _CORRECTION + [(11.5, 1.096, 2.6), (12.0, 1.114, 2.0), (12.85, 1.080, 0.7),
                                 (13.25, 1.093, 1.4), (13.45, 1.088, 0.9), (13.75, 1.100, 1.8)],
    "false_breakout": _CORRECTION + [(11.5, 1.10, 2.0), (12.3, 1.13, 1.6), (13.0, 1.085, 1.8),
                                     (13.3, 1.048, 1.6)],
    "invalidated": _CORRECTION[:-1] + [(10.5, 1.03, 1.2), (11.2, 0.975, 1.6), (11.5, 0.985, 1.0)],
    "extended": _CORRECTION + [(11.5, 1.10, 2.5), (12.4, 1.16, 3.0), (13.3, 1.52, 5.0)],
}


def setup_spec(symbol: str, base_price: float, stage: str, end_day: float = 60.0, **kw) -> SymbolSpec:
    tail = _IMPULSE + STAGE_TAILS[stage]
    offset = end_day - tail[-1][0]
    pts = _uptrend_into(offset) + [(offset + d, m, v) for d, m, v in tail if d > 0]
    return SymbolSpec(symbol=symbol, base_price=base_price, waypoints=pts, **kw)


def demo_specs() -> list[SymbolSpec]:
    """Market snapshot: BTC losing structure, a few alts showing strength."""
    btc = SymbolSpec("BTCUSDT", 62000.0, [
        (0, 0.90, 1), (6, 0.95, 1), (9, 0.93, 1), (15, 0.99, 1), (18, 0.97, 1), (25, 1.03, 1),
        (28, 1.01, 1), (35, 1.08, 1.1), (38, 1.06, 1), (45, 1.12, 1.2), (49, 1.09, 1),
        (52, 1.105, 0.9), (55, 1.07, 1.1), (57, 1.08, 0.9), (60, 1.02, 1.2)],
        base_volume_usd=9e9, noise=0.0007, wick=0.0012, funding_pct=0.005, oi_change_24h_pct=-2, seed=11)
    eth = SymbolSpec("ETHUSDT", 2600.0, [
        (0, 0.92, 1), (8, 0.97, 1), (12, 0.95, 1), (20, 1.01, 1), (24, 0.99, 1), (33, 1.06, 1),
        (37, 1.03, 1), (45, 1.10, 1.1), (50, 1.07, 1), (53, 1.08, 1), (56, 1.04, 1.1), (60, 1.005, 1.1)],
        base_volume_usd=4e9, noise=0.0009, wick=0.0014, funding_pct=0.006, oi_change_24h_pct=-1, seed=12)
    arb = SymbolSpec("ARBUSDT", 0.62, [
        (0, 1.25, 1), (8, 1.20, 1), (14, 1.24, 1), (22, 1.12, 1.1), (27, 1.15, 1), (35, 1.04, 1.2),
        (40, 1.07, 1), (48, 0.96, 1.2), (52, 0.99, 1), (57, 0.92, 1.2), (60, 0.90, 1.1)],
        base_volume_usd=1.2e8, funding_pct=0.004, oi_change_24h_pct=3, seed=13)
    return [
        btc, eth, arb,
        setup_spec("PYTHUSDT", 0.078, "long_ready", base_volume_usd=1.6e8, funding_pct=-0.008,
                   oi_change_24h_pct=7.3, seed=21),
        setup_spec("JUPUSDT", 0.52, "retest_wait", base_volume_usd=1.1e8, funding_pct=0.012,
                   oi_change_24h_pct=6.0, seed=22),
        setup_spec("SOLUSDT", 140.0, "pivot_fresh", base_volume_usd=2.5e9, funding_pct=0.12,
                   oi_change_24h_pct=1.0, seed=23),
        setup_spec("TIAUSDT", 4.1, "correction", base_volume_usd=1.3e8, funding_pct=0.004,
                   oi_change_24h_pct=-1.5, seed=24),
        setup_spec("INJUSDT", 21.0, "impulse", base_volume_usd=1.5e8, funding_pct=0.03,
                   oi_change_24h_pct=9.0, seed=25),
        setup_spec("WIFUSDT", 1.9, "extended", base_volume_usd=4e8, funding_pct=0.14,
                   oi_change_24h_pct=31.0, seed=26),
        setup_spec("SUIUSDT", 1.6, "false_breakout", base_volume_usd=3e8, funding_pct=0.01,
                   oi_change_24h_pct=4.0, seed=27),
    ]


def random_history_specs(n_symbols: int = 16, days: float = 180.0, seed: int = 7) -> list[SymbolSpec]:
    """Many randomised trend/impulse/correction/breakout cycles with random outcomes.

    Feeds the backtest so the Self-Improvement agent has a meaningful sample.
    """
    rng = random.Random(seed)
    specs = [SymbolSpec("BTCUSDT", 60000.0, _random_walk_points(rng, days, 0.006), base_volume_usd=9e9,
                        noise=0.0007, wick=0.0012, seed=seed)]
    for n in range(n_symbols):
        pts = [(0.0, 1.0, 1.0)]
        d, p = 0.0, 1.0
        while d < days - 8:
            # uptrend leg with HH/HL
            for _ in range(rng.randint(1, 3)):
                d += rng.uniform(2.0, 3.0); p *= rng.uniform(1.05, 1.09); pts.append((d, p, 1.1))
                d += rng.uniform(1.0, 1.8); p *= rng.uniform(0.95, 0.975); pts.append((d, p, 0.9))
            # impulse
            imp_low = p
            d += rng.uniform(2.5, 4.0); p *= rng.uniform(1.12, 1.25); pts.append((d, p, 2.2))
            imp_high = p
            size = imp_high - imp_low
            depth = rng.uniform(0.25, 0.85)
            n_lh = rng.randint(2, 3)
            lh = imp_high
            for k in range(n_lh):
                d += rng.uniform(0.8, 1.2)
                low_k = imp_high - size * depth * (k + 1) / (n_lh + 1) * rng.uniform(0.9, 1.1)
                pts.append((d, low_k, 0.6))
                d += rng.uniform(0.8, 1.2)
                lh = min(lh - size * 0.06, low_k + size * rng.uniform(0.2, 0.35))
                pts.append((d, lh, 0.55))
            d += rng.uniform(0.8, 1.2); p = imp_high - size * depth; pts.append((d, p, 0.6))
            # breakout through the correction line
            d += rng.uniform(1.0, 1.5); p = lh * rng.uniform(0.99, 1.01); pts.append((d, p, rng.uniform(0.8, 2.8)))
            d += rng.uniform(0.4, 0.8); p *= rng.uniform(1.01, 1.03); pts.append((d, p, 1.8))
            d += rng.uniform(0.6, 1.0); p *= rng.uniform(0.975, 0.995); pts.append((d, p, 0.8))
            outcome = rng.random()
            if outcome < 0.5:  # trend resumes
                d += rng.uniform(1.5, 3.0); p = imp_high * rng.uniform(1.0, 1.12); pts.append((d, p, 1.8))
            elif outcome < 0.8:  # false breakout
                d += rng.uniform(1.0, 2.0); p = (imp_high - size * depth) * rng.uniform(0.92, 0.99)
                pts.append((d, p, 1.5))
            else:  # chop
                d += rng.uniform(1.5, 2.5); p *= rng.uniform(0.99, 1.02); pts.append((d, p, 0.8))
        specs.append(SymbolSpec(f"SYN{n:02d}USDT", rng.uniform(0.2, 50.0),
                                [x for x in pts if x[0] <= days], base_volume_usd=rng.uniform(5e7, 5e8),
                                funding_pct=rng.uniform(-0.05, 0.12), oi_change_24h_pct=rng.uniform(-10, 20),
                                seed=seed * 100 + n))
    return specs


def _random_walk_points(rng: random.Random, days: float, daily_sd: float):
    pts, p, d = [], 1.0, 0.0
    while d <= days:
        pts.append((d, p, 1.0))
        d += 2
        p *= math.exp(rng.gauss(0.0005, daily_sd * math.sqrt(2)))
    return pts


class SyntheticProvider(MarketDataProvider):
    name = "synthetic"

    def __init__(self, specs: list[SymbolSpec] | None = None, epoch_ms: int = EPOCH_MS):
        self.specs = {s.symbol: s for s in (specs or demo_specs())}
        self.epoch_ms = epoch_ms
        self._series: dict[str, dict[str, list[Candle]]] = {}
        for spec in self.specs.values():
            base = self._generate(spec)
            self._series[spec.symbol] = {
                "15m": base,
                "1h": _aggregate(base, 4, INTERVAL_MS["1h"]),
                "4h": _aggregate(base, 16, INTERVAL_MS["4h"]),
                "1d": _aggregate(base, 96, INTERVAL_MS["1d"]),
            }
        self.end_ms = max(s["15m"][-1].close_time for s in self._series.values())
        self.cursor_ms = self.end_ms  # replay: data visible up to this time

    # -- generation -----------------------------------------------------
    def _generate(self, spec: SymbolSpec) -> list[Candle]:
        rng = random.Random(spec.seed)
        days = spec.waypoints[-1][0]
        n = int(days * 96)
        log_pts = [(d, math.log(m)) for d, m, _ in spec.waypoints]
        vol_pts = [(d, v) for d, _, v in spec.waypoints]
        out: list[Candle] = []
        noise = 0.0
        prev_close = spec.base_price * math.exp(log_pts[0][1])
        bar_vol_usd = spec.base_volume_usd / 96
        for i in range(n):
            day = (i + 1) / 96
            target = interp(day, log_pts)
            noise = 0.85 * noise + rng.gauss(0, spec.noise)
            close = spec.base_price * math.exp(target + noise)
            o = prev_close
            w1, w2 = abs(rng.gauss(0, spec.wick)), abs(rng.gauss(0, spec.wick))
            h = max(o, close) * (1 + w1)
            lo = min(o, close) * (1 - w2)
            ret = (close - o) / o
            # next-segment volume multiplier (segment that ends at the next waypoint)
            seg_mult = next((v for d, v in vol_pts if d >= day), vol_pts[-1][1])
            vol_mult = seg_mult * (1 + 40 * abs(ret)) * math.exp(rng.gauss(0, 0.25))
            vol = bar_vol_usd * vol_mult / close
            buy_ratio = min(0.75, max(0.25, 0.5 + 25 * ret + rng.gauss(0, 0.03)))
            out.append(Candle(self.epoch_ms + i * BAR_MS, o, h, lo, close, vol, vol * buy_ratio, BAR_MS))
            prev_close = close
        return out

    # -- provider interface ---------------------------------------------
    def set_cursor(self, t_ms: int) -> None:
        self.cursor_ms = min(t_ms, self.end_ms)

    def now_ms(self) -> int:
        return self.cursor_ms

    def symbols(self) -> list[str]:
        return list(self.specs)

    def _visible(self, symbol: str, interval: str) -> list[Candle]:
        series = self._series[symbol][interval]
        # binary search last candle closed at cursor
        lo, hi = 0, len(series)
        while lo < hi:
            mid = (lo + hi) // 2
            if series[mid].close_time <= self.cursor_ms:
                lo = mid + 1
            else:
                hi = mid
        return series[:lo]

    def klines(self, symbol: str, interval: str, limit: int) -> list[Candle]:
        return self._visible(symbol, interval)[-limit:]

    def full_history(self, symbol: str, interval: str) -> list[Candle]:
        return self._series[symbol][interval]

    def tickers(self) -> dict[str, Ticker]:
        out = {}
        for sym in self.specs:
            hours = self._visible(sym, "1h")[-24:]
            if not hours:
                continue
            last = hours[-1].c
            spread = 0.0004 if sym.startswith(("BTC", "ETH", "SOL")) else 0.0012
            out[sym] = Ticker(sym, last, sum(c.v * c.c for c in hours),
                              (last - hours[0].o) / hours[0].o * 100,
                              bid=last * (1 - spread / 200), ask=last * (1 + spread / 200))
        return out

    def funding_rate_pct(self, symbol: str) -> float | None:
        return self.specs[symbol].funding_pct

    def open_interest_hist(self, symbol: str, period: str, limit: int) -> list[tuple[int, float]]:
        spec = self.specs[symbol]
        hours = self._visible(symbol, "1h")[-limit:]
        if not hours:
            return []
        end = hours[-1].close_time
        base = spec.base_volume_usd * 0.6
        out = []
        for c in hours:
            frac = max(0.0, min(1.0, 1 - (end - c.close_time) / (24 * INTERVAL_MS["1h"])))
            out.append((c.close_time, base * (1 + spec.oi_change_24h_pct / 100 * frac)))
        return out

    def market_caps(self) -> dict[str, float]:
        return {s: spec.base_volume_usd * 12 for s, spec in self.specs.items()}


def _aggregate(candles: list[Candle], factor: int, interval_ms: int) -> list[Candle]:
    out = []
    for i in range(0, len(candles) - factor + 1, factor):
        chunk = candles[i:i + factor]
        if (chunk[0].t - candles[0].t) % interval_ms:
            continue
        out.append(Candle(chunk[0].t, chunk[0].o, max(c.h for c in chunk), min(c.l for c in chunk),
                          chunk[-1].c, sum(c.v for c in chunk), sum(c.buy_v for c in chunk), interval_ms))
    return out
