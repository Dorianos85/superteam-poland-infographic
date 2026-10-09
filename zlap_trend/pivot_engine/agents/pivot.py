"""AGENT 6 — PIVOT DETECTOR: close crossing above the correction line.

A cross means CORRECTION -> PIVOT_DETECTED. It is never a buy signal by itself.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import last_atr
from ..models import Candle, JsonMixin
from .trendline import TrendlineResult


@dataclass
class PivotResult(JsonMixin):
    pivot_detected: bool = False
    pivot_timeframe: str | None = None  # "4H" (preferred) or "1H" (aggressive)
    pivot_t: int | None = None  # open time of the 1H breakout candle
    pivot_idx_1h: int | None = None
    breakout_price: float | None = None
    correction_line: float | None = None  # line value at the breakout close
    confirmed_4h: bool = False
    bars_since_pivot: int | None = None
    holding: bool = False  # latest closes still above the line
    false_breakout: bool = False
    stale: bool = False
    confirmations: dict = field(default_factory=dict)
    confirmation_count: int = 0
    pivot_confirmed: bool = False
    notes: list[str] = field(default_factory=list)


def first_cross(candles: list[Candle], line, after_t: int, reset_tol: float = 0.0) -> int | None:
    """Index of the active cross: PreviousClose <= Line(prev) AND CurrentClose > Line(cur).

    If price later closes back below the line by more than `reset_tol`, that
    cross failed and the next cross (if any) becomes the active one.
    """
    active = None
    for i in range(1, len(candles)):
        c, p = candles[i], candles[i - 1]
        if c.t <= after_t:
            continue
        lv = line.value(c.close_time)
        if active is None:
            if p.c <= line.value(p.close_time) and c.c > lv:
                active = i
        elif c.c < lv - reset_tol:
            active = None
    return active


def any_cross(candles: list[Candle], line, after_t: int) -> int | None:
    for i in range(1, len(candles)):
        c, p = candles[i], candles[i - 1]
        if c.t > after_t and p.c <= line.value(p.close_time) and c.c > line.value(c.close_time):
            return i
    return None


class PivotDetectorAgent:
    name = "PIVOT_DETECTOR"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def detect(self, c4h: list[Candle], c1h: list[Candle], tl: TrendlineResult) -> PivotResult:
        cfg = self.cfg.pivot
        res = PivotResult()
        line = tl.correction_line
        if line is None or not tl.correction_line_valid:
            return res
        last_anchor_t = tl.correction_line_anchors[-1].t if tl.correction_line_anchors else line.t2
        tol = cfg.false_break_tol_atr * last_atr(c1h)
        i1 = first_cross(c1h, line, last_anchor_t, tol)
        i4 = first_cross(c4h, line, last_anchor_t, tol * 2)
        res.confirmed_4h = i4 is not None
        if i1 is None and i4 is None:
            if any_cross(c1h, line, last_anchor_t) is not None:
                res.false_breakout = True
                res.notes.append("correction line was crossed but price closed back below it (false breakout)")
            return res
        if not cfg.aggressive and i4 is None:
            res.notes.append("1H cross only; aggressive mode off — waiting for 4H close")
            return res
        if i1 is None:  # 4H crossed without a clean 1H cross (gap) — use the 4H candle's last hour
            t = c4h[i4].t
            i1 = next((i for i, c in enumerate(c1h) if c.t >= t), len(c1h) - 1)
        c = c1h[i1]
        res.pivot_detected = True
        res.pivot_timeframe = "4H" if res.confirmed_4h else "1H"
        res.pivot_t, res.pivot_idx_1h = c.t, i1
        res.breakout_price = c.c
        res.correction_line = line.value(c.close_time)
        res.bars_since_pivot = len(c1h) - 1 - i1
        recent = c1h[-cfg.hold_bars_1h:]
        res.holding = all(x.c > line.value(x.close_time) for x in recent)
        latest = c1h[-1]
        if latest.c < line.value(latest.close_time) - tol:
            res.false_breakout = True
            res.notes.append("price closed back below the correction line (false breakout)")
        if res.bars_since_pivot > cfg.max_bars_since_pivot_1h:
            res.stale = True
            res.notes.append(f"pivot is {res.bars_since_pivot} bars old (stale)")
        return res

    def confirm(self, res: PivotResult, *, structure_ok: bool, volume_ok: bool,
                derivatives_ok: bool, rs_4h_positive: bool) -> PivotResult:
        """Pivot confirmation: 5 independent checks, >= min_confirmations required."""
        if not res.pivot_detected:
            return res
        res.confirmations = {
            "STRUCTURE": structure_ok,
            "VOLUME": volume_ok,
            "DERIVATIVES": derivatives_ok,
            "RELATIVE_STRENGTH_4H": rs_4h_positive,
            "HOLD_ABOVE_LINE": res.holding or (res.confirmed_4h and not res.false_breakout),
        }
        res.confirmation_count = sum(bool(v) for v in res.confirmations.values())
        res.pivot_confirmed = (res.confirmation_count >= self.cfg.pivot.min_confirmations
                               and not res.false_breakout)
        return res
