"""Run: python -m unittest discover -s tests  (from the zlap_trend directory)."""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pivot_engine.agents import PivotOrchestrator  # noqa: E402
from pivot_engine.agents.derivatives import DerivativesAgent  # noqa: E402
from pivot_engine.agents.pivot import first_cross  # noqa: E402
from pivot_engine.agents.self_improvement import SelfImprovementAgent  # noqa: E402
from pivot_engine.agents.structure import BULLISH, walk_structure  # noqa: E402
from pivot_engine.alerts import AlertDispatcher, format_long_ready_alert  # noqa: E402
from pivot_engine.chart import render_dashboard  # noqa: E402
from pivot_engine.config import Config  # noqa: E402
from pivot_engine.data import SyntheticProvider  # noqa: E402
from pivot_engine.indicators import find_swings  # noqa: E402
from pivot_engine.journal import Journal, simulate  # noqa: E402
from pivot_engine.models import HOUR_MS, Candle, Line, Status  # noqa: E402
from pivot_engine.terminal import render_table  # noqa: E402


def candles_from(closes, start=0):
    out, prev = [], closes[0]
    for i, c in enumerate(closes):
        out.append(Candle(start + i * HOUR_MS, prev, max(prev, c) * 1.001, min(prev, c) * 0.999, c, 100, 50))
        prev = c
    return out


class IndicatorTests(unittest.TestCase):
    def test_swings_confirmed_only(self):
        c = candles_from([1, 2, 3, 2, 1, 2, 3, 4, 3])
        sw = find_swings(c, 2)
        self.assertEqual([(s.idx, s.kind) for s in sw], [(2, "H"), (4, "L")])

    def test_structure_bos_choch(self):
        closes = [10, 11, 12, 11, 10, 11, 13, 14, 12, 11, 10, 9, 8, 7]
        c = candles_from(closes)
        trend, events = walk_structure(c, find_swings(c, 1), 1)
        types = [e["type"] for e in events]
        self.assertIn("BOS_UP", types)
        self.assertIn("CHOCH_DOWN", types)
        self.assertEqual(trend, "BEARISH")

    def test_minor_pullback_does_not_flip_uptrend(self):
        closes = [10, 12, 11, 13, 12, 14, 13.5, 15, 14.6, 14.4, 14.8]
        c = candles_from(closes)
        trend, _ = walk_structure(c, find_swings(c, 1), 1)
        self.assertEqual(trend, BULLISH)


class PivotRuleTests(unittest.TestCase):
    def test_cross_requires_prev_below_and_close_above(self):
        line = Line(0, 10.0, 10 * HOUR_MS, 9.0)  # descending
        c = candles_from([9.5, 9.4, 9.3, 9.7, 9.8])  # line at close of #3 = 9.6
        i = first_cross(c, line, after_t=-1)
        self.assertEqual(i, 3)

    def test_failed_cross_resets(self):
        line = Line(0, 10.0, 10 * HOUR_MS, 10.0)
        c = candles_from([9.8, 10.2, 9.5, 9.6])
        self.assertIsNone(first_cross(c, line, -1, reset_tol=0.1))

    def test_oi_regimes(self):
        r = DerivativesAgent.regime
        self.assertEqual(r(2, 3, 0.5), "NEW_POSITION_BUILDUP")
        self.assertEqual(r(2, -3, 0.5), "SHORT_COVERING")
        self.assertEqual(r(-2, 3, 0.5), "NEW_SHORT_BUILDUP")
        self.assertEqual(r(-2, -3, 0.5), "LONG_LIQUIDATION")


class OrchestratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.journal = Journal(os.path.join(cls.tmp, "j.sqlite"))
        cls.provider = SyntheticProvider()
        cls.results = {a.symbol: a for a in PivotOrchestrator(Config(), cls.provider, cls.journal).run()}

    def test_demo_states(self):
        st = {s: a.status for s, a in self.results.items()}
        self.assertEqual(st["PYTHUSDT"], Status.LONG_READY)
        self.assertEqual(st["WIFUSDT"], Status.EXTENDED)
        self.assertEqual(self.results["WIFUSDT"].display_status, "WAIT_FOR_RETEST")
        self.assertEqual(st["TIAUSDT"], Status.CORRECTION)
        self.assertEqual(st["INJUSDT"], Status.IMPULSE)
        self.assertEqual(st["SUIUSDT"], Status.INVALIDATED)
        self.assertEqual(st["ARBUSDT"], Status.SCANNING)

    def test_long_ready_satisfies_final_rule(self):
        a = self.results["PYTHUSDT"]
        self.assertTrue(all(a.final_rule.values()), a.final_rule)
        self.assertGreaterEqual(a.score.pivot_score, 80)
        self.assertGreaterEqual(a.risk.rr, 2)
        self.assertLess(a.risk.sl, a.risk.entry)
        self.assertLess(a.risk.entry, a.risk.tp1)
        self.assertTrue(a.validation.passed)

    def test_pivot_alone_is_never_long(self):
        for a in self.results.values():
            if a.status == Status.LONG_READY:
                self.assertTrue(a.pivot.pivot_confirmed)
                self.assertTrue(a.entry.ready)
            if a.pivot is not None and a.pivot.pivot_detected and not a.pivot.pivot_confirmed:
                self.assertNotEqual(a.status, Status.LONG_READY)

    def test_rr_below_two_is_no_trade(self):
        cfg = Config().with_value("risk.min_rr", 50.0)
        a = {x.symbol: x for x in PivotOrchestrator(cfg, self.provider).run(["PYTHUSDT", "BTCUSDT"])}["PYTHUSDT"]
        self.assertEqual(a.status, Status.NO_TRADE)

    def test_alerts_and_dedup(self):
        tmp = tempfile.mkdtemp()
        j = Journal(os.path.join(tmp, "a.sqlite"))
        res = PivotOrchestrator(Config(), self.provider, j).run()
        sent = AlertDispatcher(j, sinks=[]).process(res)
        kinds = {(s, k) for s, k, _ in sent}
        self.assertIn(("PYTHUSDT", "LONG_READY"), kinds)
        self.assertFalse(any(s == "SUIUSDT" for s, _ in kinds))
        res2 = PivotOrchestrator(Config(), self.provider, j).run()
        self.assertEqual(AlertDispatcher(j, sinks=[]).process(res2), [])
        self.assertIn("LONG READY", format_long_ready_alert(self.results["PYTHUSDT"]))

    def test_renderers(self):
        res = list(self.results.values())
        self.assertIn("PYTHUSDT", render_table(res, color=False))
        html = render_dashboard(res)
        self.assertIn("<svg", html)
        self.assertIn("CORRECTION LINE", html)
        json.dumps([a.to_dict() for a in res], default=str)

    def test_no_lookahead(self):
        # Moving the cursor back must not change what earlier candles show.
        p = SyntheticProvider()
        full = p.klines("PYTHUSDT", "1h", 50)
        p.set_cursor(p.end_ms - 10 * HOUR_MS)
        cut = p.klines("PYTHUSDT", "1h", 40)
        self.assertEqual(cut[-1].t, full[-11].t)


class JournalTests(unittest.TestCase):
    def test_simulate_win_and_loss(self):
        cfg = Config()
        row = {"entry": 100.0, "sl": 98.0, "tp1": 104.0, "tp2": 108.0, "line_json": None}
        win = simulate(row, candles_from([100, 101, 103, 104.5, 106, 109]), cfg)
        self.assertEqual(win["outcome"], "WIN_TP2")
        self.assertAlmostEqual(win["realized_r"], 0.5 * 2 + 0.5 * 4, places=3)
        loss = simulate(row, candles_from([100, 99, 97]), cfg)
        self.assertEqual(loss["outcome"], "LOSS")
        self.assertEqual(loss["realized_r"], -1.0)

    def test_self_improvement_only_proposes(self):
        rows = []
        for i in range(60):
            deep = i % 2 == 0
            rows.append({"taken": 1, "outcome": "LOSS" if deep else "WIN_TP2", "realized_r": -1.0 if deep else 2.0,
                         "correction_depth": 70.0 if deep else 45.0, "pivot_score": 85, "rs_7d": 5, "rs_4h": 1,
                         "volume_ratio": 1.3, "oi_regime": "X", "funding_state": "NEUTRAL", "funding": 0.01,
                         "retest_status": "RETEST_CONFIRMED", "entry_mode": "B_STANDARD", "rr": 2.5,
                         "mfe": 1, "mae": 0.5, "false_breakout": 0, "components_json": None,
                         "failed_json": "[]", "pivot_confirmations": 4})
        cfg = Config()
        rep = SelfImprovementAgent(cfg).run(rows)
        params = [p["parameter"] for p in rep.proposals]
        self.assertIn("correction.max_depth_pct", params)
        self.assertTrue(all(p["status"] == "PENDING_HUMAN_REVIEW" for p in rep.proposals))
        self.assertEqual(cfg.correction.max_depth_pct, 78.6)  # config untouched


if __name__ == "__main__":
    unittest.main()
