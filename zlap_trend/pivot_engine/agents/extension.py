"""AGENT 12 — EXTENSION / FOMO FILTER: never buy after an extreme move."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..models import JsonMixin


@dataclass
class ExtensionResult(JsonMixin):
    extended: bool = False
    return_24h: float | None = None
    distance_from_breakout_atr: float | None = None
    action: str | None = None  # WAIT_FOR_RETEST
    notes: list[str] = field(default_factory=list)


class ExtensionFilterAgent:
    name = "EXTENSION_FILTER"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def check(self, price: float, return_24h: float | None, breakout_level: float | None,
              atr_4h: float | None) -> ExtensionResult:
        cfg = self.cfg.extension
        res = ExtensionResult(return_24h=return_24h)
        if return_24h is not None and return_24h > cfg.max_return_24h_pct:
            res.extended = True
            res.notes.append(f"Return_24H {return_24h:.1f}% > {cfg.max_return_24h_pct}%")
        if breakout_level and atr_4h:
            res.distance_from_breakout_atr = round((price - breakout_level) / atr_4h, 2)
            if res.distance_from_breakout_atr > cfg.max_dist_atr_4h:
                res.extended = True
                res.notes.append(f"price {res.distance_from_breakout_atr}x ATR_4H above breakout")
        if res.extended:
            res.action = "WAIT_FOR_RETEST"
        return res
