"""Market-data provider interface."""
from __future__ import annotations

from dataclasses import dataclass

from ..models import Candle


@dataclass
class Ticker:
    symbol: str
    last_price: float
    quote_volume_24h: float
    price_change_pct_24h: float
    bid: float | None = None
    ask: float | None = None

    @property
    def spread_pct(self) -> float | None:
        if self.bid and self.ask and self.bid > 0:
            return (self.ask - self.bid) / ((self.ask + self.bid) / 2) * 100
        return None


class MarketDataProvider:
    """Everything the agents need. Implementations: Binance (live), Synthetic, Replay."""

    name = "base"

    def now_ms(self) -> int:
        raise NotImplementedError

    def symbols(self) -> list[str]:
        """Tradeable perpetual futures symbols (e.g. 'PYTHUSDT')."""
        raise NotImplementedError

    def tickers(self) -> dict[str, Ticker]:
        raise NotImplementedError

    def klines(self, symbol: str, interval: str, limit: int) -> list[Candle]:
        """Closed candles only, oldest first."""
        raise NotImplementedError

    def funding_rate_pct(self, symbol: str) -> float | None:
        """Last/predicted funding rate in percent (0.01 == 0.01%)."""
        return None

    def open_interest_hist(self, symbol: str, period: str, limit: int) -> list[tuple[int, float]]:
        """[(timestamp ms, open interest value)], oldest first."""
        return []

    def market_caps(self) -> dict[str, float]:
        """Optional: symbol -> market cap in USD."""
        return {}
