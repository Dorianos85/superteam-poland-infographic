"""Live Binance USDⓈ-M Futures provider (public endpoints, no API key needed)."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request

from ..models import INTERVAL_MS, Candle
from .base import MarketDataProvider, Ticker

BASE = "https://fapi.binance.com"


class BinanceFuturesProvider(MarketDataProvider):
    name = "binance"

    def __init__(self, quote_asset: str = "USDT", timeout: float = 15.0,
                 min_interval_s: float = 0.05, market_cap_file: str | None = None):
        self.quote_asset = quote_asset
        self.timeout = timeout
        self.min_interval_s = min_interval_s
        self._last_call = 0.0
        self._cache: dict[str, object] = {}
        self._mcap_file = market_cap_file

    # -- http -------------------------------------------------------------
    def _get(self, path: str, params: dict | None = None):
        url = BASE + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        if url in self._cache:
            return self._cache[url]
        delay = self.min_interval_s - (time.time() - self._last_call)
        if delay > 0:
            time.sleep(delay)
        last_err = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "zlap-trend-pivot-engine"})
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = json.loads(resp.read().decode())
                self._last_call = time.time()
                self._cache[url] = data
                return data
            except Exception as exc:  # network / rate limit: back off
                last_err = exc
                time.sleep(2 ** attempt)
        raise RuntimeError(f"Binance request failed: {url}: {last_err}")

    # -- interface ----------------------------------------------------------
    def now_ms(self) -> int:
        return int(time.time() * 1000)

    def symbols(self) -> list[str]:
        info = self._get("/fapi/v1/exchangeInfo")
        return [s["symbol"] for s in info["symbols"]
                if s.get("contractType") == "PERPETUAL"
                and s.get("status") == "TRADING"
                and s.get("quoteAsset") == self.quote_asset]

    def tickers(self) -> dict[str, Ticker]:
        stats = self._get("/fapi/v1/ticker/24hr")
        books = {b["symbol"]: b for b in self._get("/fapi/v1/ticker/bookTicker")}
        out = {}
        for s in stats:
            b = books.get(s["symbol"], {})
            out[s["symbol"]] = Ticker(
                symbol=s["symbol"],
                last_price=float(s["lastPrice"]),
                quote_volume_24h=float(s["quoteVolume"]),
                price_change_pct_24h=float(s["priceChangePercent"]),
                bid=float(b["bidPrice"]) if b.get("bidPrice") else None,
                ask=float(b["askPrice"]) if b.get("askPrice") else None,
            )
        return out

    def klines(self, symbol: str, interval: str, limit: int) -> list[Candle]:
        raw = self._get("/fapi/v1/klines", {"symbol": symbol, "interval": interval,
                                            "limit": min(limit + 1, 1500)})
        now = self.now_ms()
        ims = INTERVAL_MS[interval]
        candles = [Candle(int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]),
                          float(k[5]), float(k[9]), ims)
                   for k in raw if int(k[6]) < now]  # closed candles only
        return candles[-limit:]

    def funding_rate_pct(self, symbol: str) -> float | None:
        try:
            data = self._get("/fapi/v1/premiumIndex", {"symbol": symbol})
            return float(data["lastFundingRate"]) * 100
        except Exception:
            return None

    def open_interest_hist(self, symbol: str, period: str, limit: int) -> list[tuple[int, float]]:
        try:
            data = self._get("/futures/data/openInterestHist",
                             {"symbol": symbol, "period": period, "limit": limit})
            return [(int(d["timestamp"]), float(d["sumOpenInterestValue"])) for d in data]
        except Exception:
            return []

    def market_caps(self) -> dict[str, float]:
        # Binance futures has no market cap endpoint; optionally load a JSON
        # file {"PYTHUSDT": 1.2e9, ...} produced by any external source.
        if not self._mcap_file:
            return {}
        with open(self._mcap_file, encoding="utf-8") as fh:
            return {k: float(v) for k, v in json.load(fh).items()}

    def klines_range(self, symbol: str, interval: str, start_ms: int, end_ms: int) -> list[Candle]:
        """Paginated history for replay/backtests."""
        ims = INTERVAL_MS[interval]
        out: list[Candle] = []
        t = start_ms
        while t < end_ms:
            raw = self._get("/fapi/v1/klines", {"symbol": symbol, "interval": interval,
                                                "startTime": t, "limit": 1500})
            if not raw:
                break
            out.extend(Candle(int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]),
                              float(k[5]), float(k[9]), ims) for k in raw if int(k[6]) < end_ms)
            t = int(raw[-1][0]) + ims
        return out

    def funding_history(self, symbol: str, start_ms: int, end_ms: int) -> list[tuple[int, float]]:
        try:
            data = self._get("/fapi/v1/fundingRate", {"symbol": symbol, "startTime": start_ms,
                                                      "endTime": end_ms, "limit": 1000})
            return [(int(d["fundingTime"]), float(d["fundingRate"]) * 100) for d in data]
        except Exception:
            return []
