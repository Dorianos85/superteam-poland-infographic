"""AGENT 8 — DERIVATIVES: open interest, funding, price/OI regime, crowding.

Funding never produces an entry on its own — it only adjusts the score.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..data.base import MarketDataProvider
from ..indicators import clamp, pct_change
from ..models import Candle, JsonMixin

STATE_MAP = {
    "NEW_POSITION_BUILDUP": "BULLISH_BUILDUP",
    "SHORT_COVERING": "SHORT_COVERING",
    "NEW_SHORT_BUILDUP": "BEARISH_BUILDUP",
    "LONG_LIQUIDATION": "LONG_LIQUIDATION",
    "FLAT": "NEUTRAL",
}


@dataclass
class DerivativesResult(JsonMixin):
    funding: float | None = None  # percent
    funding_state: str = "UNKNOWN"  # LONG_CROWDED / SHORT_CROWDED / NEUTRAL
    oi_change: float | None = None  # % over the window
    price_change: float | None = None
    oi_regime: str = "UNKNOWN"
    derivatives_state: str = "UNKNOWN"
    leverage_buildup: bool = False
    squeeze_conditions: bool = False
    derivatives_score: float = 50.0
    supportive: bool = False
    notes: list[str] = field(default_factory=list)


class DerivativesAgent:
    name = "DERIVATIVES"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def analyze(self, provider: MarketDataProvider, symbol: str, c1h: list[Candle]) -> DerivativesResult:
        cfg = self.cfg.derivatives
        res = DerivativesResult()
        res.funding = provider.funding_rate_pct(symbol)
        if res.funding is not None:
            if res.funding > cfg.funding_long_crowded_pct:
                res.funding_state = "LONG_CROWDED"
            elif res.funding < cfg.funding_short_crowded_pct:
                res.funding_state = "SHORT_CROWDED"
            else:
                res.funding_state = "NEUTRAL"
        oi = provider.open_interest_hist(symbol, "1h", cfg.oi_window_h + 1)
        if len(oi) >= 2 and len(c1h) > cfg.oi_window_h:
            res.oi_change = round(pct_change(oi[0][1], oi[-1][1]), 2)
            res.price_change = round(pct_change(c1h[-1 - cfg.oi_window_h].c, c1h[-1].c), 2)
            res.oi_regime = self.regime(res.price_change, res.oi_change, cfg.flat_pct)
            res.derivatives_state = STATE_MAP[res.oi_regime]
            res.leverage_buildup = res.oi_change > cfg.oi_extreme_pct
        else:
            res.notes.append("open interest history unavailable")
        res.squeeze_conditions = (res.funding_state == "SHORT_CROWDED"
                                  and (res.oi_change or 0) > 0)
        if res.squeeze_conditions and res.oi_regime == "NEW_POSITION_BUILDUP":
            res.derivatives_state = "SHORT_SQUEEZE_SETUP"
        res.derivatives_score = self._score(res)
        res.supportive = (res.oi_regime in ("NEW_POSITION_BUILDUP", "SHORT_COVERING")
                          and res.funding_state != "LONG_CROWDED" and not res.leverage_buildup)
        return res

    @staticmethod
    def regime(price_change: float, oi_change: float, flat: float) -> str:
        if abs(price_change) < flat and abs(oi_change) < flat:
            return "FLAT"
        if price_change >= 0:
            return "NEW_POSITION_BUILDUP" if oi_change >= 0 else "SHORT_COVERING"
        return "NEW_SHORT_BUILDUP" if oi_change >= 0 else "LONG_LIQUIDATION"

    def _score(self, res: DerivativesResult) -> float:
        s = 50.0
        s += {"NEW_POSITION_BUILDUP": 22, "SHORT_COVERING": 8, "FLAT": 0,
              "NEW_SHORT_BUILDUP": -10, "LONG_LIQUIDATION": -22}.get(res.oi_regime, 0)
        s += {"SHORT_CROWDED": 12, "NEUTRAL": 6, "LONG_CROWDED": -25}.get(res.funding_state, 0)
        if res.oi_change is not None and res.oi_regime == "NEW_POSITION_BUILDUP":
            s += 10 * clamp(res.oi_change / 10)
        if res.leverage_buildup:
            s -= 20
        return round(clamp(s, 0, 100), 1)
