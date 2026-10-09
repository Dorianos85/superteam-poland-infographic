"""AGENT 10 — ENTRY ENGINE: picks the entry mode (A aggressive / B standard / C momentum)."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..models import JsonMixin
from .pivot import PivotResult
from .retest import CONFIRMED, RetestResult


@dataclass
class EntryResult(JsonMixin):
    mode: str | None = None  # "A_AGGRESSIVE" / "B_STANDARD" / "C_MOMENTUM"
    ready: bool = False
    entry: float | None = None
    trigger_level: float | None = None
    waiting_for: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


class EntryEngineAgent:
    name = "ENTRY_ENGINE"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def decide(self, price: float, pivot: PivotResult, retest: RetestResult,
               score: float, extended: bool) -> EntryResult:
        cfg = self.cfg.entry
        res = EntryResult()
        if not pivot.pivot_detected:
            res.waiting_for.append("PIVOT")
            return res
        if extended:
            res.waiting_for.append("RETEST (extended)")
            return res
        if retest.status == CONFIRMED:
            if retest.broke_local_high:
                res.mode, res.ready = "C_MOMENTUM", True
                res.trigger_level = retest.local_high
            elif retest.trigger:
                res.mode, res.ready = "B_STANDARD", True
                res.trigger_level = retest.trigger_level
            else:
                res.mode = "B_STANDARD"
                res.trigger_level = retest.trigger_level
                res.waiting_for.append(f"TRIGGER close > {retest.trigger_level:.6g}")
        elif (pivot.bars_since_pivot is not None
              and pivot.bars_since_pivot <= cfg.aggressive_max_bars_since_pivot
              and score >= cfg.aggressive_min_score
              and pivot.confirmation_count >= cfg.aggressive_min_confirmations):
            res.mode, res.ready = "A_AGGRESSIVE", True
            res.trigger_level = pivot.breakout_price
        else:
            res.waiting_for.append("RETEST")
            if not pivot.pivot_confirmed:
                res.waiting_for.append("PIVOT_CONFIRMATION")
        if res.ready:
            res.entry = price
        return res
