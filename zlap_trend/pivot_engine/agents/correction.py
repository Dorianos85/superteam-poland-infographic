"""AGENT 4 — CORRECTION DETECTOR: lower highs after the impulse high (1H)."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import atr_at, clamp, find_swings, highs, index_containing
from ..models import INTERVAL_MS, Candle, JsonMixin, Swing
from .impulse import ImpulseResult


@dataclass
class CorrectionResult(JsonMixin):
    correction_detected: bool = False
    valid: bool = False  # CorrectionLow > ImpulseLow
    lower_highs: list[Swing] = field(default_factory=list)
    impulse_high_idx_1h: int | None = None
    correction_low: float | None = None
    correction_low_t: int | None = None
    correction_depth: float | None = None  # retracement % of the impulse
    correction_duration_bars: int | None = None
    correction_atr: float | None = None  # depth in ATR_1H
    correction_volume_ratio: float | None = None  # correction vol / impulse vol
    correction_quality: float = 0.0
    notes: list[str] = field(default_factory=list)


class CorrectionDetectorAgent:
    name = "CORRECTION_DETECTOR"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def detect(self, c1h: list[Candle], impulse: ImpulseResult, swing_k: int | None = None) -> CorrectionResult:
        cfg = self.cfg.correction
        k = swing_k or cfg.swing_1h
        res = CorrectionResult()
        if not impulse.found:
            return res
        # Locate the impulse high on 1H: highest 1H candle inside the 4H impulse-high candle.
        start = index_containing(c1h, impulse.impulse_high_t)
        if start is None:
            res.notes.append("impulse high outside 1H history")
            return res
        window = range(start, min(len(c1h), start + 4))
        ih = max(window, key=lambda i: c1h[i].h)
        res.impulse_high_idx_1h = ih
        after = c1h[ih + 1:]
        if not after:
            return res

        # Correction low and validity.
        lo_i = ih + 1 + min(range(len(after)), key=lambda i: after[i].l)
        res.correction_low, res.correction_low_t = c1h[lo_i].l, c1h[lo_i].t
        res.valid = res.correction_low > impulse.impulse_low
        size = impulse.impulse_high - impulse.impulse_low
        res.correction_depth = round((impulse.impulse_high - res.correction_low) / size * 100, 1)
        res.correction_duration_bars = len(after)
        atr1h = atr_at(c1h, len(c1h) - 1)
        res.correction_atr = round((impulse.impulse_high - res.correction_low) / atr1h, 2) if atr1h else None
        if not res.valid:
            res.notes.append("correction low broke the impulse low — correction invalid")

        # Swing highs below the impulse high, until one reaches it (correction over).
        # Which of them form the correction line is decided by the Trendline Engine.
        chain: list[Swing] = []
        ceiling = c1h[ih].h
        for s in highs(find_swings(c1h, k)):
            if s.idx <= ih:
                continue
            if s.price >= ceiling:
                break
            chain.append(s)
        res.lower_highs = chain
        res.correction_detected = len(chain) >= cfg.min_lower_highs and res.valid
        if len(chain) < cfg.min_lower_highs:
            res.notes.append(f"only {len(chain)} lower high(s) after impulse high")

        # Volume: a healthy correction runs on lower volume than the impulse.
        imp_start = index_containing(c1h, impulse.impulse_low_t) or max(0, ih - 24)
        imp_vol = c1h[imp_start:ih + 1]
        corr_end = lo_i
        corr_vol = c1h[ih + 1:corr_end + 1]
        if imp_vol and corr_vol:
            iv = sum(c.v for c in imp_vol) / len(imp_vol)
            cv = sum(c.v for c in corr_vol) / len(corr_vol)
            res.correction_volume_ratio = round(cv / iv, 2) if iv else None
        res.correction_quality = self._quality(res, len(chain))
        return res

    def _quality(self, res: CorrectionResult, n_lh: int) -> float:
        cfg = self.cfg.correction
        if not res.valid or res.correction_depth is None:
            return 0.0
        d = res.correction_depth
        if cfg.ideal_depth_low <= d <= cfg.ideal_depth_high:
            depth_pts = 40
        elif cfg.min_depth_pct <= d <= cfg.max_depth_pct:
            depth_pts = 25
        else:
            depth_pts = 5
        lh_pts = {0: 0, 1: 10, 2: 25}.get(n_lh, 35)  # refined by line touches later
        vol_pts = 12.5
        if res.correction_volume_ratio is not None:
            vol_pts = 25 * clamp((1.2 - res.correction_volume_ratio) / 0.7)
        return round(min(100.0, depth_pts + lh_pts + vol_pts), 1)

    @staticmethod
    def interval_ms() -> int:
        return INTERVAL_MS["1h"]
