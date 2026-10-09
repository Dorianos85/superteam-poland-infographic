"""SELF-IMPROVEMENT AGENT.

Analyses closed setups from the journal and produces SYSTEM_OPTIMIZATION_PROPOSAL
entries (OLD RULE / NEW RULE / BACKTEST RESULT / EXPECTED IMPACT / RISK).

It NEVER changes the configuration itself: every proposal is stored with status
PENDING_HUMAN_REVIEW. A human applies it by editing the JSON config.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field

from ..config import Config


def _stats(rows: list[dict]) -> dict:
    n = len(rows)
    if not n:
        return {"n": 0, "win_rate": None, "expectancy_r": None, "avg_r": None, "total_r": 0.0}
    rs = [r["realized_r"] for r in rows]
    wins = [x for x in rs if x > 0]
    losses = [x for x in rs if x <= 0]
    return {
        "n": n,
        "win_rate": round(len(wins) / n * 100, 1),
        "expectancy_r": round(sum(rs) / n, 3),
        "avg_r": round(sum(rs) / n, 3),
        "avg_win_r": round(sum(wins) / len(wins), 3) if wins else None,
        "avg_loss_r": round(sum(losses) / len(losses), 3) if losses else None,
        "total_r": round(sum(rs), 2),
        "avg_mfe_r": round(sum(r["mfe"] or 0 for r in rows) / n, 2),
        "avg_mae_r": round(sum(r["mae"] or 0 for r in rows) / n, 2),
    }


def _bucket(rows, key, edges):
    out = {}
    for lo, hi in zip(edges, edges[1:]):
        sel = [r for r in rows if r.get(key) is not None and lo <= r[key] < hi]
        out[f"{lo}–{hi}"] = _stats(sel)
    return out


def _categories(rows, key):
    cats = sorted({str(r.get(key)) for r in rows})
    return {c: _stats([r for r in rows if str(r.get(key)) == c]) for c in cats}


@dataclass
class Candidate:
    parameter: str
    old_value: object
    new_value: object
    old_rule: str
    new_rule: str
    keep: object  # predicate on taken rows (tightening) or None
    relax_failed: str | None = None  # final-rule key a relaxed rule would now pass
    relax_ok: object = None  # predicate on rows that failed only `relax_failed`


@dataclass
class SelfImprovementReport:
    sample: dict = field(default_factory=dict)
    analysis: dict = field(default_factory=dict)
    proposals: list[dict] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"sample": self.sample, "analysis": self.analysis,
                "SYSTEM_OPTIMIZATION_PROPOSAL": self.proposals, "notes": self.notes}


class SelfImprovementAgent:
    name = "SELF_IMPROVEMENT"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def run(self, rows: list[dict]) -> SelfImprovementReport:
        cfg = self.cfg.self_improvement
        closed = [r for r in rows if r.get("outcome") not in (None, "OPEN") and r.get("realized_r") is not None]
        taken = [r for r in closed if r["taken"]]
        rep = SelfImprovementReport()
        rep.sample = {"closed_setups": len(closed), "taken": len(taken), "filtered_out": len(closed) - len(taken)}
        if len(closed) < cfg.min_samples:
            rep.notes.append(f"need >= {cfg.min_samples} closed setups for analysis (have {len(closed)})")
            return rep
        losses = [r for r in closed if r["outcome"] == "LOSS"]
        rep.analysis = {
            "taken": _stats(taken),
            "all_setups": _stats(closed),
            "filtered_out": _stats([r for r in closed if not r["taken"]]),
            "false_breakout_frequency_pct": round(
                sum(1 for r in losses if r["false_breakout"]) / len(losses) * 100, 1) if losses else 0.0,
            "by_pivot_score": _bucket(closed, "pivot_score", [0, 60, 70, 80, 90, 101]),
            "by_correction_depth": _bucket(closed, "correction_depth", [0, 30, 50, 61.8, 78.6, 100]),
            "by_rs_7d": _bucket(closed, "rs_7d", [-100, 0, 5, 10, 20, 1000]),
            "by_volume_ratio": _bucket(closed, "volume_ratio", [0, 1.0, 1.2, 1.5, 100]),
            "by_oi_regime": _categories(closed, "oi_regime"),
            "by_funding_state": _categories(closed, "funding_state"),
            "by_retest": _categories(closed, "retest_status"),
            "by_entry_mode": _categories(taken, "entry_mode"),
        }
        for cand in self._candidates():
            p = self._evaluate(cand, closed, taken)
            if p:
                rep.proposals.append(p)
        w = self._weights_proposal(closed)
        if w:
            rep.proposals.append(w)
        if not rep.proposals:
            rep.notes.append("no rule change beats the current configuration on this sample")
        return rep

    # ------------------------------------------------------------------
    def _candidates(self) -> list[Candidate]:
        c = self.cfg
        return [
            Candidate("correction.max_depth_pct", c.correction.max_depth_pct, 61.8,
                      f"CorrectionDepth <= {c.correction.max_depth_pct}%", "CorrectionDepth <= 61.8%",
                      lambda r: (r["correction_depth"] or 0) <= 61.8),
            Candidate("correction.min_depth_pct", c.correction.min_depth_pct, 30.0,
                      f"CorrectionDepth >= {c.correction.min_depth_pct}%", "CorrectionDepth >= 30%",
                      lambda r: (r["correction_depth"] or 0) >= 30),
            Candidate("volume.desired_mult", c.volume.desired_mult, c.volume.strong_mult,
                      f"Volume_1H >= {c.volume.desired_mult} x AvgVolume_20",
                      f"Volume_1H >= {c.volume.strong_mult} x AvgVolume_20",
                      lambda r: (r["volume_ratio"] or 0) >= c.volume.strong_mult),
            Candidate("scoring.long_ready", c.scoring.long_ready, c.scoring.long_ready + 5,
                      f"PivotScore >= {c.scoring.long_ready}", f"PivotScore >= {c.scoring.long_ready + 5}",
                      lambda r: (r["pivot_score"] or 0) >= c.scoring.long_ready + 5),
            Candidate("entry.aggressive_min_score", c.entry.aggressive_min_score, 101,
                      "ENTRY A allowed without retest", "Retest required (ENTRY A disabled)",
                      lambda r: r["retest_status"] == "RETEST_CONFIRMED"),
            Candidate("risk.min_rr", c.risk.min_rr, c.risk.min_rr + 0.5,
                      f"RR >= {c.risk.min_rr}", f"RR >= {c.risk.min_rr + 0.5}",
                      lambda r: (r["rr"] or 0) >= c.risk.min_rr + 0.5),
            Candidate("derivatives.funding_long_crowded_pct", c.derivatives.funding_long_crowded_pct, 0.05,
                      f"Funding > +{c.derivatives.funding_long_crowded_pct}% = LONG_CROWDED",
                      "Funding > +0.05% = LONG_CROWDED", lambda r: (r["funding"] or 0) <= 0.05),
            Candidate("scanner.require_rs_4h", c.scanner.require_rs_4h, True,
                      "RS_4H > 0 preferred", "RS_4H > 0 required", lambda r: (r["rs_4h"] or 0) > 0),
            Candidate("risk.min_rr", c.risk.min_rr, c.risk.min_rr - 0.5,
                      f"RR >= {c.risk.min_rr}", f"RR >= {c.risk.min_rr - 0.5}", None,
                      relax_failed="RR>=2", relax_ok=lambda r: (r["rr"] or 0) >= c.risk.min_rr - 0.5),
            Candidate("pivot.min_confirmations", c.pivot.min_confirmations, c.pivot.min_confirmations - 1,
                      f"PivotConfirmation >= {c.pivot.min_confirmations}/5",
                      f"PivotConfirmation >= {c.pivot.min_confirmations - 1}/5", None,
                      relax_failed="PivotConfirmation>=3/5",
                      relax_ok=lambda r: (r["pivot_confirmations"] or 0) >= c.pivot.min_confirmations - 1),
        ]

    def _evaluate(self, cand: Candidate, closed: list[dict], taken: list[dict]) -> dict | None:
        cfg = self.cfg.self_improvement
        before = _stats(taken)
        if cand.keep is not None:
            after_rows = [r for r in taken if cand.keep(r)]
        else:
            # Setups that were filtered out ONLY by the rule being relaxed.
            allowed = {cand.relax_failed}
            if cand.relax_failed == "RR>=2":
                allowed |= {"CriticRejected=FALSE", "RR_TOO_LOW"}
            extra = []
            for r in closed:
                failed = set(json.loads(r.get("failed_json") or "[]"))
                if not r["taken"] and cand.relax_failed in failed and failed <= allowed and cand.relax_ok(r):
                    extra.append(r)
            after_rows = taken + extra
        after = _stats(after_rows)
        if after["n"] < cfg.min_bucket or before["n"] == 0 and after["n"] == 0:
            return None
        gain = (after["expectancy_r"] or 0) - (before["expectancy_r"] or 0)
        if gain < cfg.min_expectancy_gain_r:
            return None
        trade_change = after["n"] - before["n"]
        return {
            "kind": "RULE_CHANGE",
            "parameter": cand.parameter,
            "old_rule": cand.old_rule,
            "new_rule": cand.new_rule,
            "config_patch": {cand.parameter: cand.new_value},
            "backtest_result": {"before": before, "after": after},
            "expected_impact": (f"expectancy {before['expectancy_r']}R -> {after['expectancy_r']}R "
                                f"({gain:+.3f}R/trade), trades {before['n']} -> {after['n']} ({trade_change:+d}), "
                                f"total {before['total_r']}R -> {after['total_r']}R"),
            "risk": self._risk_text(after["n"], trade_change, cand.keep is None),
            "status": "PENDING_HUMAN_REVIEW",
        }

    @staticmethod
    def _risk_text(n: int, trade_change: int, relaxing: bool) -> str:
        parts = [f"in-sample result on {n} trades — overfitting risk; validate out-of-sample before adopting"]
        if n < 50:
            parts.append("small sample (<50): high variance of the estimate")
        if relaxing:
            parts.append("relaxing a filter adds trades the system did not take live; fills and slippage untested")
        elif trade_change < 0:
            parts.append(f"fewer signals ({trade_change:+d}); may miss strong trends")
        return "; ".join(parts)

    def _weights_proposal(self, closed: list[dict]) -> dict | None:
        cfg = self.cfg.self_improvement
        w = self.cfg.scoring
        weights = {"relative_strength": w.w_rs, "trend_quality": w.w_trend, "impulse_quality": w.w_impulse,
                   "correction_quality": w.w_correction, "line_break": w.w_line_break, "volume": w.w_volume,
                   "oi_funding": w.w_derivatives, "retest": w.w_retest, "rr": w.w_rr}
        rows = [r for r in closed if r.get("components_json")]
        if len(rows) < cfg.min_samples:
            return None
        comps = [json.loads(r["components_json"]) for r in rows]
        rs = [r["realized_r"] for r in rows]
        corr = {k: _pearson([c.get(k, 0) for c in comps], rs) for k in weights}
        raw = {k: weights[k] * min(1.5, max(0.5, 1 + corr[k])) for k in weights}
        scale = 100 / sum(raw.values())
        new_w = {k: round(v * scale, 1) for k, v in raw.items()}

        def rescore(c, ws):
            return sum(c.get(k, 0) * (ws[k] / weights[k] if weights[k] else 0) for k in weights)

        thr = self.cfg.scoring.long_ready
        old_sel = [r for r, c in zip(rows, comps) if rescore(c, weights) >= thr]
        new_sel = [r for r, c in zip(rows, comps) if rescore(c, new_w) >= thr]
        before, after = _stats(old_sel), _stats(new_sel)
        if after["n"] < cfg.min_bucket:
            return None
        gain = (after["expectancy_r"] or 0) - (before["expectancy_r"] or 0)
        if gain < cfg.min_expectancy_gain_r:
            return None
        return {
            "kind": "WEIGHTS_CHANGE",
            "parameter": "scoring.w_*",
            "old_rule": json.dumps(weights),
            "new_rule": json.dumps(new_w),
            "config_patch": {f"scoring.{_wkey(k)}": v for k, v in new_w.items()},
            "component_correlation_with_R": {k: round(v, 3) for k, v in corr.items()},
            "backtest_result": {"before": before, "after": after, "selection": f"PivotScore >= {thr}"},
            "expected_impact": f"expectancy of score>={thr} setups {before['expectancy_r']}R -> "
                               f"{after['expectancy_r']}R ({gain:+.3f}R), trades {before['n']} -> {after['n']}",
            "risk": self._risk_text(after["n"], after["n"] - before["n"], False)
                    + "; weights fitted on the same sample they are tested on",
            "status": "PENDING_HUMAN_REVIEW",
        }


def _wkey(component: str) -> str:
    return {"relative_strength": "w_rs", "trend_quality": "w_trend", "impulse_quality": "w_impulse",
            "correction_quality": "w_correction", "line_break": "w_line_break", "volume": "w_volume",
            "oi_funding": "w_derivatives", "retest": "w_retest", "rr": "w_rr"}[component]


def _pearson(x: list[float], y: list[float]) -> float:
    n = len(x)
    if n < 3:
        return 0.0
    mx, my = sum(x) / n, sum(y) / n
    sx = math.sqrt(sum((a - mx) ** 2 for a in x))
    sy = math.sqrt(sum((b - my) ** 2 for b in y))
    if sx == 0 or sy == 0:
        return 0.0
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)
