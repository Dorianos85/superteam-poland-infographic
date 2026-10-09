"""AGENT 14 — SETUP CRITIC: the adversary. Actively tries to refute the setup."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from ..config import Config
from ..indicators import find_swings, highs, pct_change
from ..models import INTERVAL_MS
from .retest import FAILED
from .structure import BEARISH

CRITICAL, MAJOR, MINOR = "CRITICAL", "MAJOR", "MINOR"


@dataclass
class CriticResult:
    objections: list[dict] = field(default_factory=list)
    reject_setup: bool = False
    verdict: str = "NO_OBJECTION"
    notes: list[str] = field(default_factory=list)

    def add(self, code: str, severity: str, question: str, finding: str) -> None:
        self.objections.append({"code": code, "severity": severity, "question": question, "finding": finding})

    def to_dict(self) -> dict:
        return {"objections": self.objections, "reject_setup": self.reject_setup,
                "verdict": self.verdict, "notes": self.notes}


class SetupCriticAgent:
    name = "SETUP_CRITIC"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def review(self, a) -> CriticResult:  # a: SetupAnalysis
        cfg = self.cfg
        res = CriticResult()
        if not (a.pivot and a.pivot.pivot_detected):
            res.verdict = "NOT_APPLICABLE"
            return res
        c1h = a.candles["1h"]
        price = c1h[-1].c

        # 1. Over-extension
        if a.extension and a.extension.extended:
            res.add("EXTENDED", MAJOR, "Czy trend nie jest już zbyt rozciągnięty?",
                    "; ".join(a.extension.notes))
        if a.scan.return_7d is not None and a.scan.return_7d > 60:
            res.add("EXTENDED_7D", MAJOR, "Czy trend nie jest już zbyt rozciągnięty?",
                    f"7D return {a.scan.return_7d:.1f}%")

        # 2. Relative strength from a single candle?
        window = c1h[-72:]
        if len(window) > 2 and a.scan.return_3d:
            biggest = max(pct_change(x.o, x.c) for x in window)
            if a.scan.return_3d > 0 and biggest / a.scan.return_3d > cfg.critic.one_candle_rs_share \
                    and (a.scan.rs_3d or 0) - biggest <= 0:
                res.add("RS_ONE_CANDLE", MAJOR, "Czy relative strength nie pochodzi z jednej świecy?",
                        f"largest 1H candle {biggest:.1f}% vs 3D return {a.scan.return_3d:.1f}%")

        # 3. Volume
        if a.volume and a.volume.volume_trend_declining:
            res.add("VOLUME_DECLINING", MAJOR, "Czy wolumen nie maleje?",
                    "post-breakout volume fell >40% vs the breakout phase")
        elif a.volume and not a.volume.volume_confirmation:
            res.add("VOLUME_WEAK", MINOR, "Czy wolumen potwierdza wybicie?",
                    f"breakout volume {a.volume.volume_ratio}x avg")

        # 4-5. Derivatives
        if a.derivatives and a.derivatives.leverage_buildup:
            res.add("OI_EXTREME", MAJOR, "Czy OI nie jest ekstremalne?",
                    f"OI +{a.derivatives.oi_change}% in {cfg.derivatives.oi_window_h}h")
        if a.derivatives and a.derivatives.funding_state == "LONG_CROWDED":
            res.add("FUNDING_CROWDED", MAJOR, "Czy funding nie wskazuje crowdingu?",
                    f"funding {a.derivatives.funding:+.3f}%")

        # 6. False breakout
        if a.pivot.false_breakout or (a.retest and a.retest.status == FAILED):
            res.add("FALSE_BREAKOUT", CRITICAL, "Czy breakout nie jest false breakout?",
                    "close back below the correction line / retest zone")

        # 7. RR re-check from raw levels
        r = a.risk
        if r and r.sl is not None and r.tp1 is not None:
            risk = price - r.sl
            rr = (r.tp1 - price) / risk if risk > 0 else 0
            if rr < cfg.risk.min_rr:
                res.add("RR_TOO_LOW", CRITICAL, "Czy RR rzeczywiście jest >= 2?",
                        f"re-computed RR {rr:.2f} from entry {price:.6g}, SL {r.sl:.6g}, TP1 {r.tp1:.6g}")
            # 8. Supply right above the entry
            if risk > 0 and a.impulse and a.impulse.found:
                c4h = a.candles["4h"]
                near = [s.price for s in highs(find_swings(c4h, 2))
                        if s.t > a.impulse.impulse_high_t and price < s.price < price + cfg.critic.supply_within_r * risk]
                if near:
                    res.add("SUPPLY_OVERHEAD", MAJOR, "Czy nad entry nie ma bliskiej supply zone?",
                            f"4H supply at {min(near):.6g} within {cfg.critic.supply_within_r}R")

        # 9. BTC structure
        if a.btc_structure is not None:
            bad = [tf for tf in ("1d", "4h") if a.btc_structure.per_tf[tf].raw_trend == BEARISH]
            if bad:
                res.add("BTC_WEAK", MAJOR, "Czy BTC nie traci struktury?",
                        f"BTC bearish structure on {', '.join(x.upper() for x in bad)}")

        # 10. Macro
        for ev in cfg.macro_events:
            try:
                t = int(datetime.fromisoformat(ev["time"].replace("Z", "+00:00"))
                        .astimezone(timezone.utc).timestamp() * 1000)
            except (KeyError, ValueError):
                continue
            if 0 <= t - a.timestamp <= cfg.macro_window_h * INTERVAL_MS["1h"]:
                res.add("MACRO_EVENT", MAJOR, "Czy rynek nie zbliża się do istotnego makro?",
                        f"{ev.get('name', 'event')} at {ev['time']}")

        # 11. Correction identification
        if a.correction:
            n = len(a.correction.lower_highs)
            if n < cfg.correction.min_lower_highs:
                res.add("CORRECTION_UNCLEAR", CRITICAL, "Czy korekta została prawidłowo zidentyfikowana?",
                        f"{n} lower highs")
            d = a.correction.correction_depth
            if d is not None and not (cfg.critic.min_correction_depth_pct <= d <= cfg.correction.max_depth_pct):
                res.add("CORRECTION_DEPTH", MAJOR, "Czy korekta została prawidłowo zidentyfikowana?",
                        f"retracement {d}% outside {cfg.critic.min_correction_depth_pct}-{cfg.correction.max_depth_pct}%")

        # 12. Tendentious line
        if a.trendlines:
            if a.trendlines.touches < cfg.trendline.min_touches:
                res.add("LINE_TOUCHES", CRITICAL, "Czy linia korekty nie została narysowana tendencyjnie?",
                        f"{a.trendlines.touches} touches")
            if a.trendlines.wick_violations > 3:
                res.add("LINE_WICKS", MINOR, "Czy linia korekty nie została narysowana tendencyjnie?",
                        f"{a.trendlines.wick_violations} wicks pierce the line")

        crit = sum(1 for o in res.objections if o["severity"] == CRITICAL)
        major = sum(1 for o in res.objections if o["severity"] == MAJOR)
        res.reject_setup = crit > 0 or major > cfg.critic.max_major_objections
        res.verdict = "REJECT_SETUP" if res.reject_setup else ("CONCERNS" if res.objections else "NO_OBJECTION")
        return res
