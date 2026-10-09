"""AGENT 13 — SETUP SCORING: PIVOT SCORE 0-100."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..indicators import clamp
from ..models import JsonMixin, score_label
from .correction import CorrectionResult
from .derivatives import DerivativesResult
from .impulse import ImpulseResult
from .pivot import PivotResult
from .retest import CONFIRMED, IN_PROGRESS, RetestResult
from .risk import RiskResult
from .scanner import ScanResult
from .structure import BULLISH, CORRECTION, StructureResult
from .trendline import TrendlineResult
from .volume import VolumeResult


@dataclass
class ScoreResult(JsonMixin):
    pivot_score: float = 0.0
    label: str = "IGNORE"
    components: dict = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)


class SetupScoringAgent:
    name = "SETUP_SCORING"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def score(self, scan: ScanResult, st: StructureResult, imp: ImpulseResult, corr: CorrectionResult,
              tl: TrendlineResult, piv: PivotResult, vol: VolumeResult, der: DerivativesResult,
              ret: RetestResult, risk: RiskResult) -> ScoreResult:
        w = self.cfg.scoring
        c: dict[str, float] = {}

        rs = 0.0
        for val, target, share in ((scan.rs_4h, w.rs_target_4h, 0.25), (scan.rs_3d, w.rs_target_3d, 0.375),
                                   (scan.rs_7d, w.rs_target_7d, 0.375)):
            if val is not None:
                rs += share * clamp(val / target)
        c["relative_strength"] = w.w_rs * rs

        t = 0.0
        t += {BULLISH: 1 / 3, CORRECTION: 1 / 6}.get(st.trend_1d, 0)
        t += 7 / 15 if st.trend_4h == BULLISH else 0
        t += 0.2 * st.structure_quality / 100
        c["trend_quality"] = w.w_trend * t

        c["impulse_quality"] = w.w_impulse * imp.impulse_quality / 100 if imp.found else 0.0
        c["correction_quality"] = w.w_correction * corr.correction_quality / 100 if corr.correction_detected else 0.0

        lb = 0.0
        if piv.pivot_detected and not piv.false_breakout:
            lb = 0.4 + 0.25 * tl.line_quality / 100 + (0.2 if piv.confirmed_4h else 0.1)
            lb += 0.15 * piv.confirmation_count / 5
        c["line_break"] = w.w_line_break * min(1.0, lb)

        c["volume"] = w.w_volume * vol.volume_score / 100 if piv.pivot_detected else 0.0
        c["oi_funding"] = w.w_derivatives * der.derivatives_score / 100
        c["retest"] = w.w_retest * {CONFIRMED: 1.0, IN_PROGRESS: 0.5}.get(ret.status, 0.0)

        rr = risk.rr or 0.0
        if rr >= 3:
            rr_pts = 1.0
        elif rr >= 2:
            rr_pts = 0.6 + 0.4 * (rr - 2)
        else:
            rr_pts = max(0.0, (rr - 1) * 0.3)
        c["rr"] = w.w_rr * rr_pts

        total = round(sum(c.values()), 1)
        return ScoreResult(pivot_score=total, label=score_label(total, self.cfg),
                           components={k: round(v, 2) for k, v in c.items()})
