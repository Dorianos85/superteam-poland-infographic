"""AGENT 16 — PIVOT ORCHESTRATOR.

Does no technical analysis of its own. It runs the specialist agents, looks for
contradictions between their outputs, orders a re-analysis (with alternative
swing sensitivity) when they disagree, rejects inconsistent setups and assigns
the final state-machine status.

    SCANNING -> TREND_LEADER -> IMPULSE -> CORRECTION -> PIVOT_DETECTED
    -> PIVOT_CONFIRMED -> RETEST_WAIT -> RETEST_CONFIRMED -> LONG_READY
    -> ACTIVE_POSITION -> MANAGEMENT -> EXIT          (ANY -> INVALIDATED)
"""
from __future__ import annotations

from ..config import Config
from ..context import SetupAnalysis
from ..data.base import MarketDataProvider
from ..indicators import last_atr
from ..models import Status
from .correction import CorrectionDetectorAgent
from .critic import SetupCriticAgent
from .derivatives import DerivativesAgent
from .entry import EntryEngineAgent
from .extension import ExtensionFilterAgent
from .impulse import ImpulseDetectorAgent
from .pivot import PivotDetectorAgent
from .retest import CONFIRMED, RetestAgent
from .risk import RiskEngineAgent
from .scanner import MarketScannerAgent, ScanResult
from .scoring import SetupScoringAgent
from .structure import BULLISH, TrendStructureAgent
from .trendline import TrendlineEngineAgent
from .validation import ValidationAgent
from .volume import VolumeMomentumAgent

LIMITS = {"1d": 200, "4h": 300, "1h": 500, "15m": 400}
BENCHMARK = "BTCUSDT"


class PivotOrchestrator:
    name = "PIVOT_ORCHESTRATOR"

    def __init__(self, cfg: Config, provider: MarketDataProvider, journal=None):
        self.cfg = cfg
        self.provider = provider
        self.journal = journal

    # ------------------------------------------------------------------
    def run(self, symbols: list[str] | None = None) -> list[SetupAnalysis]:
        scanner = MarketScannerAgent(self.cfg)
        scans, btc = scanner.scan(self.provider, symbols, BENCHMARK)
        btc_structure = self._btc_structure()
        out = [self.analyze_symbol(s, btc, btc_structure) for s in scans]
        order = {s: i for i, s in enumerate(Status.ORDER)}
        out.sort(key=lambda a: (a.status != Status.INVALIDATED, order.get(a.status, 5),
                                a.score.pivot_score if a.score else 0), reverse=True)
        return out

    def _btc_structure(self):
        p = self.provider
        try:
            return TrendStructureAgent(self.cfg).analyze(
                p.klines(BENCHMARK, "1d", LIMITS["1d"]), p.klines(BENCHMARK, "4h", LIMITS["4h"]),
                p.klines(BENCHMARK, "1h", LIMITS["1h"]), p.klines(BENCHMARK, "15m", LIMITS["15m"]))
        except Exception:
            return None

    # ------------------------------------------------------------------
    def analyze_symbol(self, scan: ScanResult, btc, btc_structure) -> SetupAnalysis:
        a = SetupAnalysis(symbol=scan.symbol, timestamp=self.provider.now_ms(), scan=scan, btc=btc,
                          btc_structure=btc_structure)
        if not scan.is_leader:
            a.status = a.display_status = Status.SCANNING
            a.reasons = list(scan.notes)
            return a
        a.candles = {tf: self.provider.klines(scan.symbol, tf, n) for tf, n in LIMITS.items()}
        self._pipeline(a, self.cfg)
        contradictions = self._contradictions(a)
        if contradictions:
            # Ask the specialists to look again with a different swing sensitivity.
            a.reanalysed = True
            alt = (self.cfg.with_value("impulse.swing_4h", self.cfg.impulse.swing_4h + 1)
                   .with_value("correction.swing_1h", self.cfg.correction.swing_1h + 1))
            self._pipeline(a, alt)
            remaining = self._contradictions(a)
            a.contradictions = contradictions + [f"after re-analysis: {c}" for c in remaining]
            if remaining:
                a.status = a.display_status = Status.INVALIDATED
                a.reasons = ["INCONSISTENT_DATA: " + "; ".join(remaining)]
                a.block_alert = True
                return a
        self._decide(a)
        return a

    def _pipeline(self, a: SetupAnalysis, cfg: Config) -> None:
        c = a.candles
        p = self.provider
        a.structure = TrendStructureAgent(cfg).analyze(c["1d"], c["4h"], c["1h"], c["15m"])
        a.impulse = ImpulseDetectorAgent(cfg).detect(c["4h"])
        a.correction = CorrectionDetectorAgent(cfg).detect(c["1h"], a.impulse)
        a.trendlines = TrendlineEngineAgent(cfg).build(c["4h"], c["1h"], a.impulse, a.correction)
        if a.derivatives is None:
            a.derivatives = DerivativesAgent(cfg).analyze(p, a.symbol, c["1h"])
        pivot_agent = PivotDetectorAgent(cfg)
        a.pivot = pivot_agent.detect(c["4h"], c["1h"], a.trendlines)
        a.volume = VolumeMomentumAgent(cfg).analyze(c["1h"], a.pivot.pivot_idx_1h)
        a.retest = RetestAgent(cfg).analyze(c["1h"], c["15m"], a.pivot, a.trendlines, a.correction)
        h1 = a.structure.per_tf["1h"]
        last_anchor_t = (a.trendlines.correction_line_anchors[-1].t
                         if a.trendlines.correction_line_anchors else None)
        structure_ok = bool(
            (last_anchor_t is not None and any(e["type"] in ("CHOCH_UP", "BOS_UP") and e["t"] > last_anchor_t
                                               for e in h1.events))
            or a.retest.higher_low_tf)
        pivot_agent.confirm(a.pivot, structure_ok=structure_ok,
                            volume_ok=a.volume.volume_confirmation,
                            derivatives_ok=a.derivatives.supportive,
                            rs_4h_positive=(a.scan.rs_4h or 0) > 0)
        price = c["1h"][-1].c
        atr4 = a.impulse.atr_4h or last_atr(c["4h"])
        a.extension = ExtensionFilterAgent(cfg).check(price, a.scan.return_24h,
                                                      a.pivot.correction_line if a.pivot.pivot_detected else None,
                                                      atr4)
        a.risk = RiskEngineAgent(cfg).plan(price, c["15m"], c["1h"], c["4h"], c["1d"],
                                           a.impulse, a.correction, a.pivot)
        a.score = SetupScoringAgent(cfg).score(a.scan, a.structure, a.impulse, a.correction, a.trendlines,
                                               a.pivot, a.volume, a.derivatives, a.retest, a.risk)
        a.entry = EntryEngineAgent(cfg).decide(price, a.pivot, a.retest, a.score.pivot_score,
                                               a.extension.extended)
        a.critic = SetupCriticAgent(cfg).review(a)

    @staticmethod
    def _contradictions(a: SetupAnalysis) -> list[str]:
        out = []
        if a.pivot.pivot_detected and not a.correction.correction_detected:
            out.append("pivot detected without a valid correction")
        if a.retest.status == CONFIRMED and not a.pivot.pivot_detected:
            out.append("retest confirmed without a pivot")
        tl = a.trendlines
        if (tl.correction_line is not None and tl.correction_line_valid and not a.pivot.pivot_detected
                and not a.pivot.false_breakout and tl.distance_to_correction_line_pct is not None
                and tl.distance_to_correction_line_pct > 0.5):
            out.append("price closed above the correction line but no cross was detected")
        if a.impulse.found and a.correction.impulse_high_idx_1h is None:
            out.append("impulse high not found on 1H")
        r = a.risk
        if a.entry.ready and r.sl is not None and r.tp1 is not None and not (r.sl < r.entry < r.tp1):
            out.append("risk levels out of order")
        return out

    # ------------------------------------------------------------------
    def _decide(self, a: SetupAnalysis) -> None:
        cfg = self.cfg
        imp, corr, tl, piv, st = a.impulse, a.correction, a.trendlines, a.pivot, a.structure
        reasons = a.reasons

        a.final_rule = {
            "TrendLeader": a.scan.is_leader,
            "Trend4H_BULLISH": st.trend_4h == BULLISH,
            "CorrectionDetected": corr.correction_detected,
            "CorrectionLineValid": tl.correction_line_valid,
            "CrossCorrectionLine": piv.pivot_detected and not piv.false_breakout,
            "PivotConfirmation>=3/5": piv.confirmation_count >= cfg.pivot.min_confirmations,
            "RelativeStrengthPositive": (a.scan.rs_3d or 0) > 0 and (a.scan.rs_7d or 0) > 0,
            "RR>=2": bool(a.risk.rr_valid),
            "TrendBroken=FALSE": not st.trend_broken,
            "CriticRejected=FALSE": not a.critic.reject_setup,
            "ValidationPassed": True,  # filled after validation below
        }

        status = self._progress_status(a, reasons)
        candidate_long = (status not in (Status.INVALIDATED, Status.EXTENDED)
                          and all(v for k, v in a.final_rule.items() if k != "ValidationPassed")
                          and a.entry.ready and a.score.pivot_score >= cfg.scoring.long_ready)

        validation = ValidationAgent(cfg, self.journal).validate(a, self.provider.now_ms(), candidate_long)
        a.validation = validation
        hard_fail = {k: v for k, v in validation.failures.items() if k != "NO_DUPLICATE_SIGNAL"}
        a.final_rule["ValidationPassed"] = not hard_fail
        a.block_alert = validation.block_alert

        if candidate_long and not hard_fail:
            status = Status.LONG_READY
            reasons.append(f"all filters passed, entry {a.entry.mode}")
        elif status not in (Status.INVALIDATED, Status.EXTENDED) and piv.pivot_detected:
            failed = [k for k, v in a.final_rule.items() if not v]
            other_critic = [o for o in a.critic.objections if o["code"] != "RR_TOO_LOW"
                            and o["severity"] == "CRITICAL"]
            majors = sum(1 for o in a.critic.objections if o["severity"] == "MAJOR")
            only_rr = ("RR>=2" in failed and set(failed) <= {"RR>=2", "CriticRejected=FALSE"}
                       and not other_critic and majors <= cfg.critic.max_major_objections)
            if only_rr and a.entry.ready:
                status = Status.NO_TRADE
                reasons.append(f"RR {a.risk.rr} < {cfg.risk.min_rr}")
            else:
                if failed:
                    reasons.append("final rule failed: " + ", ".join(failed))
                if a.critic.reject_setup:
                    reasons.append("critic: REJECT_SETUP (" + ", ".join(
                        o["code"] for o in a.critic.objections if o["severity"] in ("CRITICAL", "MAJOR")) + ")")
                if hard_fail:
                    reasons.append("validation: " + "; ".join(f"{k}: {v}" for k, v in hard_fail.items()))
                if a.entry.waiting_for:
                    reasons.append("waiting for: " + ", ".join(a.entry.waiting_for))
                elif a.entry.ready and a.score.pivot_score < cfg.scoring.long_ready:
                    reasons.append(f"pivot score {a.score.pivot_score} < {cfg.scoring.long_ready}")

        # Positions tracked by the journal override the analysis state.
        if self.journal is not None and a.setup_id:
            pos = self.journal.position_status(a.setup_id)
            if pos in (Status.ACTIVE_POSITION, Status.MANAGEMENT, Status.EXIT):
                reasons.append(f"journal: position {pos}")
                status = pos
                a.block_alert = True
        a.status = status
        a.display_status = "WAIT_FOR_RETEST" if status == Status.EXTENDED else status

    def _progress_status(self, a: SetupAnalysis, reasons: list[str]) -> str:
        imp, corr, piv, st = a.impulse, a.correction, a.pivot, a.structure
        if corr.correction_low is not None and not corr.valid:
            reasons.append("correction broke the impulse low")
            return Status.INVALIDATED
        if a.extension.extended:
            reasons.extend(a.extension.notes)
            return Status.EXTENDED
        if not imp.found:
            reasons.extend(imp.notes)
            return Status.IMPULSE if imp.in_progress else Status.TREND_LEADER
        if st.trend_broken:
            reasons.append("4H trend broken")
            return Status.INVALIDATED
        if not corr.correction_detected:
            reasons.extend(corr.notes or ["waiting for correction (>= 2 lower highs)"])
            return Status.IMPULSE
        if not piv.pivot_detected:
            if piv.false_breakout:
                reasons.extend(piv.notes)
                return Status.INVALIDATED
            if a.trendlines.correction_line_current is not None:
                reasons.append(f"waiting for close above correction line {a.trendlines.correction_line_current:.6g}")
            return Status.CORRECTION
        if piv.stale and not a.entry.ready:
            reasons.extend(piv.notes)
            return Status.INVALIDATED
        if a.retest.status == "RETEST_FAILED":
            reasons.extend(a.retest.notes)
            return Status.INVALIDATED
        if not piv.pivot_confirmed:
            reasons.append(f"pivot confirmations {piv.confirmation_count}/5")
            return Status.PIVOT_DETECTED
        if a.retest.status == CONFIRMED:
            return Status.RETEST_CONFIRMED
        fresh = (a.retest.status == "NO_RETEST" and piv.bars_since_pivot is not None
                 and piv.bars_since_pivot <= self.cfg.entry.aggressive_max_bars_since_pivot)
        return Status.PIVOT_CONFIRMED if fresh else Status.RETEST_WAIT
