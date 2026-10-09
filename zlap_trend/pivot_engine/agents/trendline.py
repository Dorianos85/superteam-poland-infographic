"""AGENT 5 — TRENDLINE ENGINE: main trend line (4H swing lows) and correction line (1H lower highs).

Lines are chosen by an objective rule, never "by eye":
* every pair of anchors is a candidate,
* a candidate is rejected if any candle CLOSES through it between its anchors,
* the winner has the most touches (anchors within tolerance), ties -> most recent.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations

from ..config import Config
from ..indicators import atr_at, clamp, find_swings, last_atr, line_through, lows
from ..models import INTERVAL_MS, Candle, JsonMixin, Line, Swing
from .correction import CorrectionResult
from .impulse import ImpulseResult


@dataclass
class TrendlineResult(JsonMixin):
    trend_line: Line | None = None
    trend_line_touches: int = 0
    trend_line_current: float | None = None
    trend_line_valid: bool = False
    correction_line: Line | None = None
    correction_line_anchors: list[Swing] = field(default_factory=list)
    correction_line_current: float | None = None
    correction_line_valid: bool = False
    touches: int = 0
    wick_violations: int = 0
    close_violations: int = 0
    distance_to_correction_line_pct: float | None = None
    line_quality: float = 0.0
    notes: list[str] = field(default_factory=list)


class TrendlineEngineAgent:
    name = "TRENDLINE_ENGINE"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    # ------------------------------------------------------------------
    def build(self, c4h: list[Candle], c1h: list[Candle], impulse: ImpulseResult,
              correction: CorrectionResult) -> TrendlineResult:
        res = TrendlineResult()
        self._trend_line(c4h, impulse, res)
        self._correction_line(c1h, correction, res)
        return res

    def _trend_line(self, c4h: list[Candle], impulse: ImpulseResult, res: TrendlineResult) -> None:
        cfg = self.cfg.trendline
        ims = INTERVAL_MS["4h"]
        swing_lows = lows(find_swings(c4h, self.cfg.impulse.swing_4h))[-cfg.max_swing_lows:]
        if impulse.found:
            # TrendLow_2 must not be later than the impulse low (the base of the last leg).
            swing_lows = [s for s in swing_lows if s.t <= impulse.impulse_low_t]
            if not swing_lows or swing_lows[-1].t != impulse.impulse_low_t:
                lo_idx = next((i for i, c in enumerate(c4h) if c.t == impulse.impulse_low_t), None)
                if lo_idx is not None:
                    swing_lows.append(Swing(lo_idx, c4h[lo_idx].t, c4h[lo_idx].l, "L"))
        atr = last_atr(c4h)
        tol = cfg.touch_tol_atr * atr
        best = None
        for a, b in combinations(swing_lows, 2):
            if b.price <= a.price:
                continue  # TrendLow_2 > TrendLow_1
            line = line_through(a, b, ims)
            if any(c.c < line.value(c.close_time) - tol for c in c4h[a.idx:b.idx + 1]):
                continue
            touches = sum(1 for s in swing_lows if s.idx >= a.idx
                          and abs(s.price - line.value(s.t + ims // 2)) <= tol)
            key = (touches, b.idx, a.idx)
            if best is None or key > best[0]:
                best = (key, line, touches)
        if best:
            _, line, touches = best
            res.trend_line, res.trend_line_touches = line, touches
            res.trend_line_current = line.value(c4h[-1].close_time)
            res.trend_line_valid = touches >= cfg.min_touches
            if touches < cfg.preferred_touches:
                res.notes.append(f"trend line has {touches} touches (preferred {cfg.preferred_touches})")
        else:
            res.notes.append("no valid rising trend line")

    def _correction_line(self, c1h: list[Candle], corr: CorrectionResult, res: TrendlineResult) -> None:
        cfg = self.cfg.trendline
        ims = INTERVAL_MS["1h"]
        chain = corr.lower_highs
        if len(chain) < 2:
            res.notes.append("correction line needs >= 2 lower highs")
            return
        tol = cfg.touch_tol_atr * atr_at(c1h, chain[-1].idx)
        best = None
        for a, b in combinations(chain, 2):
            if b.price >= a.price:
                continue
            line = line_through(a, b, ims)
            seg = c1h[a.idx:b.idx + 1]
            if any(c.c > line.value(c.close_time) for c in seg):
                continue  # a line that price closed through is drawn tendentiously
            wicks_above = sum(1 for c in seg if c.h > line.value(c.t + ims // 2) + tol)
            # Touches: lower highs from anchor A on that sit on the line (until price closes above it).
            end = next((i for i in range(b.idx + 1, len(c1h)) if c1h[i].c > line.value(c1h[i].close_time)),
                       len(c1h))
            on_line = [s for s in chain if a.idx <= s.idx < end
                       and abs(s.price - line.value(s.t + ims // 2)) <= tol]
            # Prefer: enough touches (capped at 'preferred'), then the line spanning the
            # whole correction, then fewer wick violations.
            span = (on_line[-1].idx if on_line else b.idx) - a.idx
            key = (min(len(on_line), cfg.preferred_touches), span, -wicks_above, b.idx)
            if best is None or key > best[0]:
                best = (key, line, len(on_line), wicks_above, on_line)
        if not best:
            res.notes.append("no correction line without close violations")
            return
        _, line, touches, wicks, anchors = best
        res.correction_line = line
        res.correction_line_anchors = anchors
        res.touches = touches
        res.wick_violations = wicks
        res.correction_line_current = line.value(c1h[-1].close_time)
        last = c1h[-1].c
        res.distance_to_correction_line_pct = round((last - res.correction_line_current)
                                                    / res.correction_line_current * 100, 2)
        res.correction_line_valid = touches >= cfg.min_touches and corr.valid
        res.line_quality = self._quality(touches, wicks, len(chain), line, c1h)

    def _quality(self, touches: int, wicks: int, n_chain: int, line: Line, c1h: list[Candle]) -> float:
        cfg = self.cfg.trendline
        q = 45 + 20 * clamp((touches - cfg.min_touches + 1) / 2)
        q += 15 * clamp(1 - wicks / 4)
        q += 10 if n_chain >= 3 else 5
        # Very steep lines are fragile: penalise slope steeper than 1 ATR_1H per 6 hours.
        atr = last_atr(c1h)
        steep = abs(line.slope_per_hour) * 6 / atr if atr else 0
        q += 10 * clamp(1.5 - steep)
        return round(min(100.0, q), 1)
