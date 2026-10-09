"""AGENT 11 — RISK ENGINE: structural stop loss, TP1/TP2/TP3 and RR.

Stops are always placed below a market structure level, never as a random %.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import find_swings, highs, last_atr, lows
from ..models import Candle, JsonMixin
from .correction import CorrectionResult
from .impulse import ImpulseResult
from .pivot import PivotResult


@dataclass
class RiskResult(JsonMixin):
    entry: float | None = None
    sl: float | None = None
    sl_basis: str | None = None
    sl_candidates: dict = field(default_factory=dict)
    tp1: float | None = None
    tp2: float | None = None
    tp2_basis: str | None = None
    tp3: float | None = None
    tp3_basis: str | None = None
    supply_4h: tuple | None = None  # (low, high)
    supply_1d: tuple | None = None
    demand_zone: tuple | None = None
    risk: float | None = None
    rr_tp1: float | None = None
    rr_tp2: float | None = None
    rr: float | None = None
    rr_valid: bool = False
    notes: list[str] = field(default_factory=list)


def _supply_above(candles: list[Candle], level: float, k: int):
    """Nearest swing-high supply zone (body top .. high) above `level`."""
    cands = [s for s in highs(find_swings(candles, k)) if s.price > level * 1.002]
    if not cands:
        return None
    s = min(cands, key=lambda x: x.price)
    c = candles[s.idx]
    low = c.body_top if c.body_top > level else (level + s.price) / 2
    return (low, s.price)


class RiskEngineAgent:
    name = "RISK_ENGINE"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def plan(self, entry: float, c15m: list[Candle], c1h: list[Candle], c4h: list[Candle],
             c1d: list[Candle], impulse: ImpulseResult, corr: CorrectionResult,
             pivot: PivotResult) -> RiskResult:
        cfg = self.cfg.risk
        res = RiskResult(entry=entry)
        atr1h = last_atr(c1h)
        buffer = cfg.sl_buffer_atr * atr1h
        min_dist = cfg.min_sl_atr * atr1h

        cands: dict[str, float] = {}
        since = pivot.pivot_t or impulse.impulse_high_t or 0
        hl15 = [s for s in lows(find_swings(c15m, 2)) if s.t >= since and s.price < entry]
        if hl15:
            cands["15M_HL"] = hl15[-1].price
        sl1h = [s for s in lows(find_swings(c1h, 3)) if s.price < entry
                and s.t >= (impulse.impulse_high_t or 0)]
        if sl1h:
            cands["1H_SWING_LOW"] = sl1h[-1].price
        if corr.correction_low is not None and corr.correction_low < entry:
            cands["CORRECTION_LOW"] = corr.correction_low
        sl4h = [s for s in lows(find_swings(c4h, 3)) if s.price < entry]
        if sl4h:
            cands["4H_SWING_LOW"] = sl4h[-1].price
        res.sl_candidates = {k: round(v, 10) for k, v in cands.items()}
        valid = {k: v - buffer for k, v in cands.items() if entry - (v - buffer) >= min_dist}
        if valid:
            basis = max(valid, key=valid.get)  # tightest structural stop
            res.sl, res.sl_basis = valid[basis], basis
        else:
            res.notes.append("no structural stop level at a sane distance")

        if impulse.found:
            res.tp1 = impulse.impulse_high
            size = impulse.impulse_size
            sup4 = _supply_above(c4h, impulse.impulse_high, 3)
            if sup4:
                res.supply_4h, res.tp2, res.tp2_basis = sup4, sup4[0], "4H_SUPPLY"
            else:
                res.tp2, res.tp2_basis = impulse.impulse_high + 0.618 * size, "PROJECTION_1.618"
            sup1d = _supply_above(c1d, res.tp2, 2)
            if sup1d:
                res.supply_1d, res.tp3, res.tp3_basis = sup1d, sup1d[0], "1D_SUPPLY"
            else:
                res.tp3, res.tp3_basis = impulse.impulse_high + 1.0 * size, "PROJECTION_2.0"
            if res.tp3 <= res.tp2:
                res.tp3 = None
        if corr.correction_low_t is not None:
            c = next((x for x in c1h if x.t == corr.correction_low_t), None)
            if c:
                res.demand_zone = (c.l, max(c.body_bottom, c.l + 0.25 * atr1h))

        if res.sl is not None and res.tp1 is not None:
            res.risk = entry - res.sl
            res.rr_tp1 = round((res.tp1 - entry) / res.risk, 2) if res.tp1 > entry else 0.0
            res.rr_tp2 = round((res.tp2 - entry) / res.risk, 2) if res.tp2 else None
            res.rr = res.rr_tp1 if cfg.rr_target == "TP1" else res.rr_tp2
            res.rr_valid = res.rr is not None and res.rr >= cfg.min_rr
            if not res.rr_valid:
                res.notes.append(f"RR {res.rr} < {cfg.min_rr} -> NO_TRADE")
        return res
