"""AGENT 2 — TREND STRUCTURE: swings, HH/HL/LH/LL, BOS, CHoCH per timeframe."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import find_swings, highs, lows
from ..models import Candle, JsonMixin, Swing

BULLISH, BEARISH, CORRECTION, RANGE, UNKNOWN = "BULLISH", "BEARISH", "CORRECTION", "RANGE", "UNKNOWN"


@dataclass
class TfStructure(JsonMixin):
    timeframe: str
    trend: str = UNKNOWN
    raw_trend: str = UNKNOWN  # trend before higher-TF context is applied
    last_event: str | None = None  # BOS_UP / BOS_DOWN / CHOCH_UP / CHOCH_DOWN
    last_event_t: int | None = None
    events: list[dict] = field(default_factory=list)
    swing_labels: list[str] = field(default_factory=list)
    last_swing_high: float | None = None
    last_swing_low: float | None = None
    quality: float = 0.0


@dataclass
class StructureResult(JsonMixin):
    trend_1d: str = UNKNOWN
    trend_4h: str = UNKNOWN
    trend_1h: str = UNKNOWN
    trend_15m: str = UNKNOWN
    structure_quality: float = 0.0
    trend_broken: bool = False
    per_tf: dict = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)


def walk_structure(candles: list[Candle], swings: list[Swing], right: int) -> tuple[str, list[dict]]:
    """Market-structure walk (BOS / CHoCH) without look-ahead.

    * BOS: close beyond the last confirmed swing in the trend direction. The
      extreme of the pullback before that break becomes the *protected* level.
    * CHoCH: close beyond the protected level -> trend flips.
    Minor pullback lows inside an uptrend therefore do not flip the trend;
    only losing the protected low does. A swing is usable `right` bars after it formed.
    """
    trend = UNKNOWN
    events: list[dict] = []
    hi: Swing | None = None
    lo: Swing | None = None
    hi_broken = lo_broken = False
    protected: float | None = None
    seg_start = 0
    sw_iter = iter(sorted(swings, key=lambda s: s.idx + right))
    pending = next(sw_iter, None)

    def ev(kind, i, level):
        events.append({"type": kind, "t": candles[i].t, "idx": i, "level": level})

    for i, c in enumerate(candles):
        while pending is not None and pending.idx + right <= i:
            if pending.kind == "H":
                hi, hi_broken = pending, False
            else:
                lo, lo_broken = pending, False
            pending = next(sw_iter, None)
        if trend == UNKNOWN:
            seg_start = max(seg_start, i - 60)
        if trend != BEARISH and hi is not None and not hi_broken and c.c > hi.price:
            ev("BOS_UP", i, hi.price)
            protected = min(x.l for x in candles[seg_start:i + 1])
            trend, hi_broken, seg_start = BULLISH, True, i
        elif trend == BULLISH and protected is not None and c.c < protected:
            ev("CHOCH_DOWN", i, protected)
            protected = max(x.h for x in candles[seg_start:i + 1])
            trend, seg_start = BEARISH, i
        elif trend != BULLISH and lo is not None and not lo_broken and c.c < lo.price:
            ev("BOS_DOWN", i, lo.price)
            protected = max(x.h for x in candles[seg_start:i + 1])
            trend, lo_broken, seg_start = BEARISH, True, i
        elif trend == BEARISH and protected is not None and c.c > protected:
            ev("CHOCH_UP", i, protected)
            protected = min(x.l for x in candles[seg_start:i + 1])
            trend, seg_start = BULLISH, i
    return trend, events


class TrendStructureAgent:
    name = "TREND_STRUCTURE"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def analyze_tf(self, candles: list[Candle], timeframe: str, k: int) -> TfStructure:
        out = TfStructure(timeframe=timeframe)
        if len(candles) < 4 * k + 2:
            return out
        swings = find_swings(candles, k)
        trend, events = walk_structure(candles, swings, k)
        hs, ls = highs(swings), lows(swings)
        out.raw_trend = trend
        out.events = events[-6:]
        if events:
            out.last_event, out.last_event_t = events[-1]["type"], events[-1]["t"]
        out.swing_labels = [s.label for s in swings[-8:] if s.label]
        out.last_swing_high = hs[-1].price if hs else None
        out.last_swing_low = ls[-1].price if ls else None
        if trend == UNKNOWN and len(hs) >= 2 and len(ls) >= 2:
            hh, hl = hs[-1].price > hs[-2].price, ls[-1].price > ls[-2].price
            trend = BULLISH if hh and hl else BEARISH if not hh and not hl else RANGE
        out.trend = trend
        out.quality = self._quality(trend, events, swings)
        return out

    @staticmethod
    def _quality(trend: str, events: list[dict], swings: list[Swing]) -> float:
        if trend != BULLISH:
            return 20.0 if trend == RANGE else 0.0
        consecutive = 0
        for e in reversed(events):
            if e["type"] in ("BOS_UP", "CHOCH_UP"):
                consecutive += 1
            else:
                break
        labels = [s.label for s in swings[-8:] if s.label]
        bull_ratio = sum(1 for x in labels if x in ("HH", "HL")) / len(labels) if labels else 0
        q = 35 + 12 * min(consecutive, 3) + 30 * bull_ratio
        return round(min(100.0, q), 1)

    def analyze(self, c1d, c4h, c1h, c15m) -> StructureResult:
        s = self.cfg.structure
        d = self.analyze_tf(c1d, "1D", s.swing_1d)
        h4 = self.analyze_tf(c4h, "4H", s.swing_4h)
        h1 = self.analyze_tf(c1h, "1H", s.swing_1h)
        m15 = self.analyze_tf(c15m, "15M", s.swing_15m)
        # Lower timeframe pulling back inside a higher-timeframe uptrend = CORRECTION.
        for lower, higher in ((h1, h4), (m15, h1)):
            if lower.trend == BEARISH and higher.raw_trend == BULLISH:
                lower.trend = CORRECTION
        if h4.trend == BEARISH and d.raw_trend == BULLISH:
            h4.trend = CORRECTION
        res = StructureResult(trend_1d=d.trend, trend_4h=h4.trend, trend_1h=h1.trend,
                              trend_15m=m15.trend,
                              per_tf={"1d": d, "4h": h4, "1h": h1, "15m": m15})
        res.trend_broken = h4.raw_trend == BEARISH
        q = 0.6 * h4.quality + 0.25 * d.quality + 0.15 * (h1.quality if h1.raw_trend == BULLISH else 40)
        res.structure_quality = round(q, 1)
        if res.trend_broken:
            res.notes.append(f"4H structure broken ({h4.last_event})")
        return res
