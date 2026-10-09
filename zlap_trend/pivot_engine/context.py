"""SetupAnalysis: the full record the orchestrator assembles for one symbol."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .models import Candle, JsonMixin


@dataclass
class SetupAnalysis(JsonMixin):
    symbol: str
    timestamp: int
    status: str = "SCANNING"
    display_status: str = "SCANNING"  # e.g. WAIT_FOR_RETEST for EXTENDED
    reasons: list[str] = field(default_factory=list)
    final_rule: dict = field(default_factory=dict)
    contradictions: list[str] = field(default_factory=list)
    reanalysed: bool = False
    block_alert: bool = False
    scan: Any = None
    btc: Any = None
    btc_structure: Any = None
    structure: Any = None
    impulse: Any = None
    correction: Any = None
    trendlines: Any = None
    pivot: Any = None
    volume: Any = None
    derivatives: Any = None
    retest: Any = None
    extension: Any = None
    risk: Any = None
    entry: Any = None
    score: Any = None
    critic: Any = None
    validation: Any = None
    candles: dict[str, list[Candle]] = field(default_factory=dict, repr=False)

    @property
    def setup_id(self) -> str | None:
        if self.impulse is not None and getattr(self.impulse, "impulse_high_t", None):
            return f"{self.symbol}-{self.impulse.impulse_high_t}"
        return None

    @property
    def price(self) -> float | None:
        c = self.candles.get("1h")
        if c:
            return c[-1].c
        return self.scan.price if self.scan else None

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.pop("candles", None)
        d["setup_id"] = self.setup_id
        d["price"] = self.price
        return d
