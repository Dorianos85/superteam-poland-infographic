"""AGENT 7 — VOLUME & MOMENTUM: quality of the breakout."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import clamp, interp, return_over, rsi
from ..models import Candle, JsonMixin


@dataclass
class VolumeResult(JsonMixin):
    volume_1h: float | None = None
    avg_volume_20: float | None = None
    volume_ratio: float | None = None
    volume_acceleration: float | None = None
    buy_volume: float | None = None
    sell_volume: float | None = None
    buy_ratio: float | None = None
    rsi_1h: float | None = None
    momentum_6h: float | None = None
    volume_trend_declining: bool = False
    volume_score: float = 0.0
    volume_confirmation: bool = False
    strong_confirmation: bool = False
    notes: list[str] = field(default_factory=list)


class VolumeMomentumAgent:
    name = "VOLUME_MOMENTUM"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def analyze(self, c1h: list[Candle], pivot_idx: int | None) -> VolumeResult:
        cfg = self.cfg.volume
        res = VolumeResult()
        idx = pivot_idx if pivot_idx is not None else len(c1h) - 1
        if idx < cfg.avg_period:
            res.notes.append("not enough candles for volume baseline")
            return res
        # Breakout volume: strongest of the breakout candle and the next one
        # (a 1H breakout often completes over two candles).
        window = c1h[idx:idx + 2]
        bar = max(window, key=lambda c: c.v)
        base = c1h[idx - cfg.avg_period:idx]
        avg = sum(c.v for c in base) / len(base)
        res.volume_1h, res.avg_volume_20 = bar.v, avg
        res.volume_ratio = round(bar.v / avg, 2) if avg else None
        last3 = c1h[-3:]
        prev = c1h[-23:-3]
        if prev:
            pv = sum(c.v for c in prev) / len(prev)
            res.volume_acceleration = round((sum(c.v for c in last3) / 3) / pv, 2) if pv else None
        res.buy_volume = sum(c.buy_v for c in window)
        res.sell_volume = sum(c.v - c.buy_v for c in window)
        tot = res.buy_volume + res.sell_volume
        res.buy_ratio = round(res.buy_volume / tot, 3) if tot else None
        res.rsi_1h = rsi(c1h[-100:])
        res.momentum_6h = return_over(c1h, 6)
        post = c1h[idx:]
        if len(post) >= 6:
            first, second = post[: len(post) // 2], post[len(post) // 2:]
            res.volume_trend_declining = (sum(c.v for c in second) / len(second)
                                          < 0.6 * sum(c.v for c in first) / len(first))
        ratio = res.volume_ratio or 0
        res.volume_confirmation = ratio >= cfg.desired_mult
        res.strong_confirmation = ratio >= cfg.strong_mult
        score = interp(ratio, [(0.5, 10), (1.0, 35), (cfg.desired_mult, 55), (cfg.strong_mult, 72), (2.5, 90)])
        if res.buy_ratio is not None:
            score += 20 * clamp((res.buy_ratio - 0.45) / 0.2) - 5
        if res.rsi_1h is not None:
            if 50 <= res.rsi_1h <= 72:
                score += 5
            elif res.rsi_1h > 80:
                score -= 10
        res.volume_score = round(clamp(score, 0, 100), 1)
        if not res.volume_confirmation:
            res.notes.append(f"breakout volume {ratio:.2f}x avg < {cfg.desired_mult}x")
        return res
