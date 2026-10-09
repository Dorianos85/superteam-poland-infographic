"""Replay provider: serves stored history up to a moving cursor (walk-forward backtests on real data)."""
from __future__ import annotations

from ..models import INTERVAL_MS, Candle
from .base import MarketDataProvider, Ticker

TFS = ("15m", "1h", "4h", "1d")


class ReplayProvider(MarketDataProvider):
    name = "replay"

    def __init__(self, candles: dict[str, dict[str, list[Candle]]],
                 funding: dict[str, list[tuple[int, float]]] | None = None,
                 oi: dict[str, list[tuple[int, float]]] | None = None):
        self.candles = candles
        self.funding = funding or {}
        self.oi = oi or {}
        self.end_ms = min(c["1h"][-1].close_time for c in candles.values())
        self.start_ms = max(c["1h"][0].t for c in candles.values())
        self.cursor_ms = self.end_ms

    @classmethod
    def from_binance(cls, binance, symbols: list[str], days: int, end_ms: int | None = None) -> "ReplayProvider":
        end = end_ms or binance.now_ms()
        warm = {"15m": 5, "1h": 25, "4h": 55, "1d": 210}
        candles, funding, oi = {}, {}, {}
        for s in symbols:
            candles[s] = {tf: binance.klines_range(s, tf, end - (days + warm[tf]) * INTERVAL_MS["1d"], end)
                          for tf in TFS}
            funding[s] = binance.funding_history(s, end - days * INTERVAL_MS["1d"], end)
            oi[s] = binance.open_interest_hist(s, "1h", 500)
        return cls(candles, funding, oi)

    def set_cursor(self, t_ms: int) -> None:
        self.cursor_ms = min(t_ms, self.end_ms)

    def now_ms(self) -> int:
        return self.cursor_ms

    def symbols(self) -> list[str]:
        return list(self.candles)

    def klines(self, symbol: str, interval: str, limit: int) -> list[Candle]:
        series = self.candles[symbol][interval]
        lo, hi = 0, len(series)
        while lo < hi:
            mid = (lo + hi) // 2
            if series[mid].close_time <= self.cursor_ms:
                lo = mid + 1
            else:
                hi = mid
        return series[max(0, lo - limit):lo]

    def tickers(self) -> dict[str, Ticker]:
        out = {}
        for s in self.candles:
            hours = self.klines(s, "1h", 24)
            if hours:
                out[s] = Ticker(s, hours[-1].c, sum(c.v * c.c for c in hours),
                                (hours[-1].c - hours[0].o) / hours[0].o * 100)
        return out

    def funding_rate_pct(self, symbol: str) -> float | None:
        past = [v for t, v in self.funding.get(symbol, []) if t <= self.cursor_ms]
        return past[-1] if past else None

    def open_interest_hist(self, symbol: str, period: str, limit: int) -> list[tuple[int, float]]:
        return [x for x in self.oi.get(symbol, []) if x[0] <= self.cursor_ms][-limit:]
