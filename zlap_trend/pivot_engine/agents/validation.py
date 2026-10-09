"""AGENT 15 — VALIDATION: audits the other agents' work. Any failed critical test -> BLOCK_ALERT."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..config import Config
from ..models import INTERVAL_MS, Candle


@dataclass
class ValidationResult:
    tests: dict = field(default_factory=dict)  # name -> True / False / None (n/a)
    failures: dict = field(default_factory=dict)  # name -> reason
    passed: bool = True
    block_alert: bool = False

    def to_dict(self) -> dict:
        return {"tests": self.tests, "failures": self.failures, "passed": self.passed,
                "block_alert": self.block_alert}


CRITICAL_TESTS = ("DATA_VALID", "STRUCTURE_VALID", "TRENDLINE_VALID", "CORRECTION_VALID",
                  "PIVOT_VALID", "RR_VALID", "NO_DUPLICATE_SIGNAL")


class ValidationAgent:
    name = "VALIDATION"

    def __init__(self, cfg: Config, journal=None):
        self.cfg = cfg
        self.journal = journal

    def validate(self, a, now_ms: int, intends_long: bool) -> ValidationResult:
        res = ValidationResult()

        def put(name, ok, reason=""):
            res.tests[name] = ok
            if ok is False:
                res.failures[name] = reason

        put("DATA_VALID", *self._data(a, now_ms))
        put("STRUCTURE_VALID", *self._structure(a))
        put("CORRECTION_VALID", *self._correction(a))
        put("TRENDLINE_VALID", *self._trendline(a))
        put("PIVOT_VALID", *self._pivot(a))
        put("RR_VALID", *self._rr(a, intends_long))
        put("NO_DUPLICATE_SIGNAL", *self._duplicate(a, intends_long))
        res.passed = all(res.tests.get(t) is not False for t in CRITICAL_TESTS)
        res.block_alert = not res.passed
        return res

    # -- tests (each returns (ok|None, reason)) ----------------------------
    def _data(self, a, now_ms):
        v = self.cfg.validation
        mins = {"1h": v.min_candles_1h, "4h": v.min_candles_4h, "1d": 20, "15m": 50}
        for tf, need in mins.items():
            cs: list[Candle] = a.candles.get(tf) or []
            if len(cs) < need:
                return False, f"{tf}: {len(cs)} candles < {need}"
            step = INTERVAL_MS[tf]
            for p, c in zip(cs, cs[1:]):
                if c.t - p.t != step:
                    return False, f"{tf}: gap/unordered candles at {c.t}"
                if not (c.l <= min(c.o, c.c) <= max(c.o, c.c) <= c.h) or c.l <= 0:
                    return False, f"{tf}: inconsistent OHLC at {c.t}"
            age = now_ms - cs[-1].close_time
            if tf in ("1h", "15m") and age > v.max_data_age_bars * step:
                return False, f"{tf}: stale data ({age // 60000} min old)"
        return True, ""

    @staticmethod
    def _structure(a):
        imp = a.impulse
        if imp is None or not imp.found:
            return None, ""
        if imp.impulse_high <= imp.impulse_low or imp.impulse_high_t <= imp.impulse_low_t:
            return False, "impulse high must be after and above impulse low"
        if imp.prev_swing_high is not None and imp.impulse_high <= imp.prev_swing_high:
            return False, "impulse high not above previous swing high"
        return True, ""

    def _correction(self, a):
        c = a.correction
        if c is None or not c.correction_detected:
            return None, ""
        if not c.valid:
            return False, "correction low below impulse low"
        if len(c.lower_highs) < self.cfg.correction.min_lower_highs:
            return False, "not enough lower highs"
        anchors = a.trendlines.correction_line_anchors if a.trendlines else []
        prices = [s.price for s in (anchors or c.lower_highs[:1])]
        if any(b >= a_ for a_, b in zip(prices, prices[1:])) or prices[0] >= a.impulse.impulse_high:
            return False, "lower highs are not descending below the impulse high"
        return True, ""

    @staticmethod
    def _trendline(a):
        tl = a.trendlines
        if tl is None or tl.correction_line is None:
            return None, ""
        line = tl.correction_line
        if line.slope_per_hour >= 0:
            return False, "correction line is not descending"
        for s in tl.correction_line_anchors:
            if s.t <= a.impulse.impulse_high_t:
                return False, "correction line anchored before the impulse high"
        if tl.trend_line is not None and tl.trend_line.slope_per_hour <= 0:
            return False, "trend line is not rising"
        return True, ""

    @staticmethod
    def _pivot(a):
        p = a.pivot
        if p is None or not p.pivot_detected:
            return None, ""
        c1h = a.candles["1h"]
        i = p.pivot_idx_1h
        line = a.trendlines.correction_line
        if i is None or i < 1 or i >= len(c1h):
            return False, "pivot index out of range"
        cur, prev = c1h[i], c1h[i - 1]
        if not (cur.c > line.value(cur.close_time)):
            return False, "pivot candle did not close above the line"
        if a.trendlines.correction_line_anchors and cur.t <= a.trendlines.correction_line_anchors[-1].t:
            return False, "pivot before the last line anchor"
        if prev.c > line.value(prev.close_time) and not p.confirmed_4h:
            return False, "previous close already above the line (no cross)"
        return True, ""

    def _rr(self, a, intends_long):
        r = a.risk
        if not intends_long:
            return None, ""
        if r is None or r.sl is None or r.tp1 is None or r.entry is None:
            return False, "missing entry/SL/TP"
        if not (r.sl < r.entry < r.tp1):
            return False, f"levels out of order SL {r.sl} / entry {r.entry} / TP1 {r.tp1}"
        rr = (r.tp1 - r.entry) / (r.entry - r.sl)
        if self.cfg.risk.rr_target == "TP1" and abs(rr - (r.rr or 0)) > 0.02:
            return False, f"RR mismatch {rr:.2f} vs reported {r.rr}"
        if (r.rr or 0) < self.cfg.risk.min_rr:
            return False, f"RR {r.rr} < {self.cfg.risk.min_rr}"
        return True, ""

    def _duplicate(self, a, intends_long):
        if not intends_long or self.journal is None:
            return None, ""
        dup = self.journal.find_recent_signal(a.symbol, a.setup_id, a.timestamp,
                                              self.cfg.validation.duplicate_cooldown_h)
        if dup:
            return False, f"signal already sent: {dup}"
        return True, ""
