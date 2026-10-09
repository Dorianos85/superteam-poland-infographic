"""AGENT 1 — MARKET SCANNER: universe, liquidity, returns, relative strength vs BTC."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..data.base import MarketDataProvider
from ..indicators import clamp, return_over
from ..models import JsonMixin


@dataclass
class ScanResult(JsonMixin):
    symbol: str
    price: float = 0.0
    return_4h: float | None = None
    return_24h: float | None = None
    return_3d: float | None = None
    return_7d: float | None = None
    rs_4h: float | None = None
    rs_3d: float | None = None
    rs_7d: float | None = None
    quote_volume_24h: float = 0.0
    market_cap: float | None = None
    volume_to_mcap: float | None = None
    spread_pct: float | None = None
    volume_score: float = 0.0
    momentum_rank: int = 0
    unusual_mover: bool = False
    liquid: bool = True
    status: str = "SCANNING"
    notes: list[str] = field(default_factory=list)

    @property
    def is_leader(self) -> bool:
        return self.status == "TREND_LEADER"


@dataclass
class BtcContext(JsonMixin):
    return_4h: float = 0.0
    return_24h: float = 0.0
    return_3d: float = 0.0
    return_7d: float = 0.0


class MarketScannerAgent:
    name = "MARKET_SCANNER"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    @staticmethod
    def returns(candles_1h) -> dict:
        return {
            "return_4h": return_over(candles_1h, 4),
            "return_24h": return_over(candles_1h, 24),
            "return_3d": return_over(candles_1h, 72),
            "return_7d": return_over(candles_1h, 168),
        }

    def scan(self, provider: MarketDataProvider, symbols: list[str] | None = None,
             benchmark: str = "BTCUSDT") -> tuple[list[ScanResult], BtcContext]:
        cfg = self.cfg.scanner
        tickers = provider.tickers()
        universe = symbols or [s for s in provider.symbols() if s.endswith(cfg.quote_asset)]
        caps = provider.market_caps()

        btc_r = self.returns(provider.klines(benchmark, "1h", 200))
        btc = BtcContext(**{k: (v or 0.0) for k, v in btc_r.items()})

        # Liquidity pre-filter, then the most liquid N get full return analysis.
        ranked = sorted((s for s in universe if s != benchmark and s in tickers),
                        key=lambda s: tickers[s].quote_volume_24h, reverse=True)
        results: list[ScanResult] = []
        for sym in ranked[: cfg.max_symbols]:
            t = tickers[sym]
            r = ScanResult(symbol=sym, price=t.last_price, quote_volume_24h=t.quote_volume_24h,
                           spread_pct=t.spread_pct, market_cap=caps.get(sym))
            if r.market_cap:
                r.volume_to_mcap = r.quote_volume_24h / r.market_cap
            if t.quote_volume_24h < cfg.min_quote_volume_24h:
                r.liquid = False
                r.notes.append(f"24h volume {t.quote_volume_24h/1e6:.1f}M < min")
            if r.spread_pct is not None and r.spread_pct > cfg.max_spread_pct:
                r.liquid = False
                r.notes.append(f"spread {r.spread_pct:.3f}% > max")
            candles = provider.klines(sym, "1h", 200)
            if len(candles) < 169:
                r.notes.append("not enough 1H history for 7D return")
                results.append(r)
                continue
            r.price = candles[-1].c
            for k, v in self.returns(candles).items():
                setattr(r, k, v)
            r.rs_4h = r.return_4h - btc.return_4h
            r.rs_3d = r.return_3d - btc.return_3d
            r.rs_7d = r.return_7d - btc.return_7d
            avg_daily_vol = sum(c.v * c.c for c in candles[-168:]) / 7
            last_day_vol = sum(c.v * c.c for c in candles[-24:])
            r.unusual_mover = avg_daily_vol > 0 and last_day_vol > cfg.unusual_volume_mult * avg_daily_vol
            results.append(r)

        self._score_volume(results)
        self._rank_momentum(results)
        for r in results:
            self._classify(r)
        return results, btc

    def _score_volume(self, results: list[ScanResult]) -> None:
        vols = sorted(r.quote_volume_24h for r in results)
        n = len(vols)
        for r in results:
            pct = (sum(1 for v in vols if v <= r.quote_volume_24h) / n) if n else 0
            score = 60 * pct
            if r.volume_to_mcap is not None:
                score += 25 * clamp(r.volume_to_mcap / 0.25)
            else:
                score += 12.5
            if r.unusual_mover:
                score += 15
            r.volume_score = round(min(100.0, score), 1)

    @staticmethod
    def _rank_momentum(results: list[ScanResult]) -> None:
        def m(r):
            if r.rs_7d is None:
                return float("-inf")
            return 0.25 * r.rs_4h + 0.35 * r.rs_3d + 0.40 * r.rs_7d
        for i, r in enumerate(sorted(results, key=m, reverse=True), 1):
            r.momentum_rank = i

    def _classify(self, r: ScanResult) -> None:
        if r.rs_3d is None or r.rs_7d is None:
            r.status = "SCANNING"
            return
        strong = r.rs_3d > 0 and r.rs_7d > 0
        if self.cfg.scanner.require_rs_4h:
            strong = strong and r.rs_4h > 0
        if strong and r.liquid:
            r.status = "TREND_LEADER"
            if r.rs_4h <= 0:
                r.notes.append("RS_4H <= 0 (preferred > 0)")
        else:
            r.status = "SCANNING"
            if not strong:
                r.notes.append("not stronger than BTC on 3D and 7D")
