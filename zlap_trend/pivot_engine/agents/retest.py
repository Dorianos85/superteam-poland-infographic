"""AGENT 9 — RETEST: price behaviour after the correction-line breakout."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import find_swings, last_atr, lows
from ..models import Candle, JsonMixin
from .correction import CorrectionResult
from .pivot import PivotResult
from .trendline import TrendlineResult

NONE, IN_PROGRESS, CONFIRMED, FAILED = "NO_RETEST", "RETEST_IN_PROGRESS", "RETEST_CONFIRMED", "RETEST_FAILED"


@dataclass
class RetestResult(JsonMixin):
    status: str = NONE
    zone_low: float | None = None
    zone_high: float | None = None
    zone_components: dict = field(default_factory=dict)
    retest_t: int | None = None
    retest_low: float | None = None
    retest_candle_high: float | None = None
    defense: bool = False  # retest candle closed back above the zone
    higher_low_tf: str | None = None  # "15M" / "1H"
    higher_low_price: float | None = None
    trigger: bool = False  # close above the retest candle high
    trigger_level: float | None = None
    local_high: float | None = None  # highest high between pivot and retest
    broke_local_high: bool = False
    notes: list[str] = field(default_factory=list)


class RetestAgent:
    name = "RETEST"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def analyze(self, c1h: list[Candle], c15m: list[Candle], pivot: PivotResult,
                tl: TrendlineResult, corr: CorrectionResult) -> RetestResult:
        cfg = self.cfg.retest
        res = RetestResult()
        if not pivot.pivot_detected or tl.correction_line is None:
            return res
        line = tl.correction_line
        atr = last_atr(c1h)
        i0 = pivot.pivot_idx_1h
        post = c1h[i0 + 1:]

        def zone_at(c: Candle) -> tuple[float, float]:
            lv = line.value(c.close_time)
            lo, hi = lv - cfg.zone_below_atr * atr, lv + cfg.zone_above_atr * atr
            # Broken local swing high (the last lower high) acts as support if near.
            lh = corr.lower_highs[-1].price if corr.lower_highs else None
            if lh is not None and lv < lh <= lv + cfg.local_high_max_atr * atr:
                hi = max(hi, lh)
            return lo, hi

        cur_lo, cur_hi = zone_at(c1h[-1])
        res.zone_low, res.zone_high = cur_lo, cur_hi
        res.zone_components = {"correction_line": line.value(c1h[-1].close_time),
                               "breakout_level": pivot.correction_line,
                               "local_swing_high": corr.lower_highs[-1].price if corr.lower_highs else None}
        if not post:
            return res
        # The breakout leg must first leave the zone; a touch after that is the retest.
        left_zone = False
        touch_i = None
        for j, c in enumerate(post):
            zl, zh = zone_at(c)
            if not left_zone:
                if c.l > zh:
                    left_zone = True
                continue
            if c.l <= zh:
                touch_i = j
                break
        if touch_i is None:
            res.local_high = max(c.h for c in post)
            return res
        touch = post[touch_i]
        zl, zh = zone_at(touch)
        res.local_high = max(c.h for c in post[:touch_i + 1])
        after = post[touch_i:]
        # Retest low = lowest low while price is still interacting with the zone.
        low_i = min(range(len(after)), key=lambda k: after[k].l if after[k].l <= zone_at(after[k])[1] else float("inf"))
        rc = after[low_i]
        res.retest_t, res.retest_low, res.retest_candle_high = rc.t, rc.l, rc.h
        if any(c.c < zone_at(c)[0] for c in after):
            res.status = FAILED
            res.notes.append("closed below the retest zone")
            return res
        res.defense = rc.c > zone_at(rc)[0]
        later = after[low_i + 1:]
        res.trigger_level = rc.h
        res.trigger = any(c.c > rc.h for c in later)
        res.broke_local_high = any(c.c > res.local_high for c in later)
        # Preferred: a higher low after the retest low (15M first, then 1H).
        for tf, candles, k in (("15M", c15m, 2), ("1H", c1h, 2)):
            hl = [s for s in lows(find_swings(candles, k)) if s.t > rc.t and s.price > rc.l]
            if hl:
                res.higher_low_tf, res.higher_low_price = tf, hl[-1].price
                break
        if res.defense and (res.trigger or res.higher_low_tf):
            res.status = CONFIRMED
        else:
            res.status = IN_PROGRESS
        return res
