"""AGENT 3 — IMPULSE DETECTOR: last complete bullish impulse on 4H."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import atr_at, clamp, find_swings, highs
from ..models import Candle, JsonMixin


@dataclass
class ImpulseResult(JsonMixin):
    found: bool = False
    in_progress: bool = False  # price is printing new highs: impulse not finished
    impulse_low: float | None = None
    impulse_low_t: int | None = None
    impulse_high: float | None = None
    impulse_high_t: int | None = None
    prev_swing_high: float | None = None
    impulse_size: float | None = None
    impulse_atr: float | None = None  # move expressed in ATR_4H
    atr_4h: float | None = None
    impulse_volume_ratio: float | None = None
    impulse_duration_bars: int | None = None
    impulse_quality: float = 0.0
    notes: list[str] = field(default_factory=list)

    @property
    def impulse_id(self) -> str | None:
        return str(self.impulse_high_t) if self.impulse_high_t else None


class ImpulseDetectorAgent:
    name = "IMPULSE_DETECTOR"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def detect(self, c4h: list[Candle], swing_k: int | None = None) -> ImpulseResult:
        cfg = self.cfg.impulse
        k = swing_k or cfg.swing_4h
        res = ImpulseResult()
        swings = find_swings(c4h, k)
        hs = highs(swings)
        if len(hs) < 2:
            res.notes.append("not enough 4H swing highs")
            return res
        for j in range(len(hs) - 1, 0, -1):
            h = hs[j]
            # The impulse must break structure: above every swing high of the lookback window.
            prior = [s for s in hs[:j] if s.idx >= h.idx - cfg.structure_lookback_bars]
            if not prior:
                continue
            p = max(prior, key=lambda s: s.price)
            if h.price <= p.price:
                continue  # a lower high: belongs to a correction, look further back
            if max(c.h for c in c4h[h.idx + 1:] or [c4h[h.idx]]) > h.price:
                break  # exceeded later: the newest impulse is not complete yet
            seg = c4h[p.idx:h.idx + 1]
            lo_i = p.idx + min(range(len(seg)), key=lambda i: seg[i].l)
            low = c4h[lo_i].l
            atr = atr_at(c4h, h.idx, cfg.atr_period)
            move = h.price - low
            mult = move / atr if atr else 0
            res.prev_swing_high = p.price
            if mult < cfg.min_atr_mult:
                res.notes.append(f"move {mult:.2f}x ATR_4H < {cfg.min_atr_mult}")
                return res
            imp = c4h[lo_i:h.idx + 1]
            before = c4h[max(0, lo_i - 20):lo_i]
            vr = None
            if before:
                avg_before = sum(c.v for c in before) / len(before)
                vr = (sum(c.v for c in imp) / len(imp)) / avg_before if avg_before else None
            res.found = True
            res.impulse_low, res.impulse_low_t = low, c4h[lo_i].t
            res.impulse_high, res.impulse_high_t = h.price, h.t
            res.impulse_size = move
            res.impulse_atr = round(mult, 2)
            res.atr_4h = atr
            res.impulse_volume_ratio = round(vr, 2) if vr else None
            res.impulse_duration_bars = h.idx - lo_i
            res.impulse_quality = self._quality(mult, vr, h.idx - lo_i)
            if mult < cfg.preferred_atr_mult:
                res.notes.append(f"impulse {mult:.2f}x ATR below preferred {cfg.preferred_atr_mult}")
            return res
        res.notes.append("no completed 4H impulse (swing high above prior structure)")
        window = c4h[-cfg.structure_lookback_bars:]
        if max(c.h for c in c4h[-(k + 1):]) >= max(c.h for c in window):
            res.in_progress = True
            res.notes.append("price printing new highs — impulse in progress")
        return res

    def _quality(self, mult: float, vol_ratio: float | None, bars: int) -> float:
        cfg = self.cfg.impulse
        q = 45 * clamp((mult - cfg.min_atr_mult) / (4.0 - cfg.min_atr_mult)) + 25
        if vol_ratio is not None:
            q += 20 * clamp((vol_ratio - 0.8) / 1.2)
        else:
            q += 10
        # Clean impulses are fast: penalise very long grinds.
        q += 10 * clamp(1 - max(0, bars - 12) / 30)
        return round(min(100.0, q), 1)
