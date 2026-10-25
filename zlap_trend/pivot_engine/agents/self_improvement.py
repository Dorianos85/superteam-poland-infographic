"""SELF-IMPROVEMENT AGENT.

Analyses closed setups from the journal and produces SYSTEM_OPTIMIZATION_PROPOSAL
entries (OLD RULE / NEW RULE / BACKTEST RESULT / EXPECTED IMPACT / RISK).

It NEVER changes the configuration itself: every proposal is stored with status
PENDING_HUMAN_REVIEW. A human applies it by editing the JSON config.

Out-of-sample discipline: setups are split in time. A rule or weight change is
chosen on the TRAIN part (first `train_fraction`) and is proposed only if the
gain also holds on the TEST part it never saw. Both results, with bootstrap
confidence intervals, are reported.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field

from ..config import Config
from ..stats import bootstrap_ci, bootstrap_diff_ci


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
        "expectancy_ci95": bootstrap_ci(rs, 1000),
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
        closed_t = sorted(closed, key=lambda r: r["entry_time"])
        cut = int(len(closed_t) * cfg.train_fraction)
        train, test = closed_t[:cut], closed_t[cut:]
        rep.sample.update({"train_setups": len(train), "test_setups": len(test),
                           "train_taken": sum(r["taken"] for r in train),
                           "test_taken": sum(r["taken"] for r in test)})
        rejected = []
        for cand in self._candidates():
            p = self._evaluate(cand, train, test)
            if p and p.get("status") == "PENDING_HUMAN_REVIEW":
                rep.proposals.append(p)
            elif p:
                rejected.append(p)
        w = self._weights_proposal(train, test)
        if w and w.get("status") == "PENDING_HUMAN_REVIEW":
            rep.proposals.append(w)
        elif w:
            rejected.append(w)
        rep.analysis["rejected_out_of_sample"] = [
            {"parameter": p["parameter"], "new_rule": p["new_rule"], "reason": p["reason"]} for p in rejected]
        if not rep.proposals:
            rep.notes.append("no rule change improves expectancy both in-sample (train) and out-of-sample (test)")
        if sum(r["taken"] for r in test) < cfg.min_bucket:
            rep.notes.append(f"test window has only {sum(r['taken'] for r in test)} LONG_READY trades — "
                             "tightening rules cannot be confirmed out-of-sample yet")
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

    @staticmethod
    def _apply(cand: Candidate, rows: list[dict]) -> tuple[list[dict], list[dict]]:
        """(rows the system takes today, rows it would take under the new rule)."""
        taken = [r for r in rows if r["taken"]]
        if cand.keep is not None:
            return taken, [r for r in taken if cand.keep(r)]
        # Relaxing: add setups that were filtered out ONLY by the rule being relaxed.
        allowed = {cand.relax_failed}
        if cand.relax_failed == "RR>=2":
            allowed |= {"CriticRejected=FALSE", "RR_TOO_LOW"}
        extra = []
        for r in rows:
            failed = set(json.loads(r.get("failed_json") or "[]"))
            if not r["taken"] and cand.relax_failed in failed and failed <= allowed and cand.relax_ok(r):
                extra.append(r)
        return taken, taken + extra

    def _evaluate(self, cand: Candidate, train: list[dict], test: list[dict]) -> dict | None:
        cfg = self.cfg.self_improvement
        tr_before, tr_after = self._apply(cand, train)
        if len(tr_after) < cfg.min_bucket:
            return None
        tr_gain = _gain(tr_before, tr_after)
        if tr_gain < cfg.min_expectancy_gain_r:
            return None  # not even better in-sample
        te_before, te_after = self._apply(cand, test)
        te_gain = _gain(te_before, te_after)
        diff_ci = bootstrap_diff_ci([r["realized_r"] for r in te_before], [r["realized_r"] for r in te_after], 1000)
        prop = {
            "kind": "RULE_CHANGE",
            "parameter": cand.parameter,
            "old_rule": cand.old_rule,
            "new_rule": cand.new_rule,
            "config_patch": {cand.parameter: cand.new_value},
            "backtest_result": {
                "train": {"before": _stats(tr_before), "after": _stats(tr_after), "gain_r": round(tr_gain, 3)},
                "test": {"before": _stats(te_before), "after": _stats(te_after), "gain_r": round(te_gain, 3),
                         "gain_ci95": diff_ci},
                # kept for the CLI summary: the out-of-sample numbers are the ones that count
                "before": _stats(te_before), "after": _stats(te_after),
            },
            "expected_impact": (f"OUT-OF-SAMPLE: expectancy {_e(te_before)}R -> {_e(te_after)}R ({te_gain:+.3f}R/trade, "
                                f"95% CI {diff_ci}), trades {len(te_before)} -> {len(te_after)}; "
                                f"in-sample gain was {tr_gain:+.3f}R"),
            "risk": self._risk_text(len(te_after), len(te_after) - len(te_before), cand.keep is None, diff_ci),
            "status": "PENDING_HUMAN_REVIEW",
        }
        if len(te_after) < max(5, cfg.min_bucket // 3):
            prop.update(status="REJECTED", reason=f"test window too small ({len(te_after)} trades)")
        elif te_gain <= 0:
            prop.update(status="REJECTED", reason=f"in-sample {tr_gain:+.3f}R but out-of-sample {te_gain:+.3f}R")
        return prop

    @staticmethod
    def _risk_text(n: int, trade_change: int, relaxing: bool, diff_ci=None) -> str:
        parts = [f"out-of-sample result on {n} trades; forward-test before adopting"]
        if diff_ci is not None and diff_ci[0] <= 0:
            parts.append("95% CI of the gain includes 0 — not statistically significant")
        if n < 50:
            parts.append("small sample (<50): high variance of the estimate")
        if relaxing:
            parts.append("relaxing a filter adds trades the system did not take live; fills and slippage untested")
        elif trade_change < 0:
            parts.append(f"fewer signals ({trade_change:+d}); may miss strong trends")
        return "; ".join(parts)

    def _weights_proposal(self, train: list[dict], test: list[dict]) -> dict | None:
        cfg = self.cfg.self_improvement
        w = self.cfg.scoring
        weights = {"relative_strength": w.w_rs, "trend_quality": w.w_trend, "impulse_quality": w.w_impulse,
                   "correction_quality": w.w_correction, "line_break": w.w_line_break, "volume": w.w_volume,
                   "oi_funding": w.w_derivatives, "retest": w.w_retest, "rr": w.w_rr}
        tr = [r for r in train if r.get("components_json")]
        te = [r for r in test if r.get("components_json")]
        if len(tr) < cfg.min_samples:
            return None
        comps = [json.loads(r["components_json"]) for r in tr]
        corr = {k: _pearson([c.get(k, 0) for c in comps], [r["realized_r"] for r in tr]) for k in weights}
        raw = {k: weights[k] * min(1.5, max(0.5, 1 + corr[k])) for k in weights}
        scale = 100 / sum(raw.values())
        new_w = {k: round(v * scale, 1) for k, v in raw.items()}
        thr = self.cfg.scoring.long_ready

        def select(rows, ws):
            out = []
            for r in rows:
                c = json.loads(r["components_json"])
                if sum(c.get(k, 0) * (ws[k] / weights[k] if weights[k] else 0) for k in weights) >= thr:
                    out.append(r)
            return out

        tr_gain = _gain(select(tr, weights), select(tr, new_w))
        if len(select(tr, new_w)) < cfg.min_bucket or tr_gain < cfg.min_expectancy_gain_r:
            return None
        te_old, te_new = select(te, weights), select(te, new_w)
        te_gain = _gain(te_old, te_new)
        diff_ci = bootstrap_diff_ci([r["realized_r"] for r in te_old], [r["realized_r"] for r in te_new], 1000)
        prop = {
            "kind": "WEIGHTS_CHANGE",
            "parameter": "scoring.w_*",
            "old_rule": json.dumps(weights),
            "new_rule": json.dumps(new_w),
            "config_patch": {f"scoring.{_wkey(k)}": v for k, v in new_w.items()},
            "component_correlation_with_R_train": {k: round(v, 3) for k, v in corr.items()},
            "backtest_result": {"selection": f"PivotScore >= {thr}",
                                "train_gain_r": round(tr_gain, 3), "test_gain_r": round(te_gain, 3),
                                "test_gain_ci95": diff_ci,
                                "before": _stats(te_old), "after": _stats(te_new)},
            "expected_impact": f"OUT-OF-SAMPLE expectancy of score>={thr} setups {_e(te_old)}R -> {_e(te_new)}R "
                               f"({te_gain:+.3f}R, 95% CI {diff_ci}); in-sample gain {tr_gain:+.3f}R",
            "risk": self._risk_text(len(te_new), len(te_new) - len(te_old), False, diff_ci)
                    + "; weights fitted on the train window only",
            "status": "PENDING_HUMAN_REVIEW",
        }
        if len(te_new) < max(5, cfg.min_bucket // 3):
            prop.update(status="REJECTED", reason=f"test window too small ({len(te_new)} setups)")
        elif te_gain <= 0:
            prop.update(status="REJECTED", reason=f"in-sample {tr_gain:+.3f}R but out-of-sample {te_gain:+.3f}R")
        return prop


def _e(rows: list[dict]):
    return round(sum(r["realized_r"] for r in rows) / len(rows), 3) if rows else None


def _gain(before: list[dict], after: list[dict]) -> float:
    if not before or not after:
        return 0.0  # nothing to compare against
    return _e(after) - _e(before)


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
