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
        row = {"entry": 100.0, "sl": 98.0, "tp1": 104.0, "tp2": 108.0, "line_json": None,
               "entry_time": 0, "funding": 0.0, "quote_volume_24h": 1e9}
        win = simulate(row, candles_from([100, 101, 103, 104.5, 106, 109]), cfg)
        self.assertEqual(win["outcome"], "WIN_TP2")
        self.assertAlmostEqual(win["gross_r"], 0.5 * 2 + 0.5 * 4, places=3)
        # fees 2x0.05% + slippage 2x0.02% = 0.14% of price = 0.07R with a 2% stop
        self.assertAlmostEqual(win["cost_r"], 0.07, places=3)
        self.assertAlmostEqual(win["realized_r"], win["gross_r"] - win["cost_r"], places=3)
        loss = simulate(row, candles_from([100, 99, 97]), cfg)
        self.assertEqual(loss["outcome"], "LOSS")
        self.assertAlmostEqual(loss["gross_r"], -1.0, places=3)
        self.assertLess(loss["realized_r"], -1.0)  # costs + stop slippage make a loss worse than -1R

    def test_gap_through_stop_fills_at_open(self):
        row = {"entry": 100.0, "sl": 98.0, "tp1": 104.0, "tp2": 108.0, "line_json": None,
               "entry_time": 0, "funding": 0.0, "quote_volume_24h": 1e9}
        gap = [Candle(0, 100, 100.5, 99.5, 100, 1, 0), Candle(HOUR_MS, 96, 96.5, 95, 95.5, 1, 0)]
        res = simulate(row, gap, Config())
        self.assertAlmostEqual(res["gross_r"], -2.0, places=3)  # filled at 96, not 98

    def test_same_bar_tp1_and_breakeven_is_pessimistic(self):
        row = {"entry": 100.0, "sl": 98.0, "tp1": 104.0, "tp2": 108.0, "line_json": None,
               "entry_time": 0, "funding": 0.0, "quote_volume_24h": 1e9}
        bar = [Candle(0, 100, 104.5, 99.0, 101, 1, 0)]  # touches TP1 and goes back below entry
        res = simulate(row, bar, Config())
        self.assertEqual(res["outcome"], "WIN_TP1")
        self.assertAlmostEqual(res["gross_r"], 1.0, places=3)
        opt = simulate(row, bar, Config().with_value("costs.same_bar", "optimistic"))
        self.assertEqual(opt["outcome"], "OPEN")

    def test_funding_cost(self):
        row = {"entry": 100.0, "sl": 98.0, "tp1": 104.0, "tp2": 108.0, "line_json": None,
               "entry_time": 0, "funding": 0.1, "quote_volume_24h": 1e9}
        flat = [Candle(i * HOUR_MS, 100, 100.5, 99.5, 100, 1, 0) for i in range(8)] + \
               [Candle(8 * HOUR_MS, 100, 100.5, 97, 97.5, 1, 0)]
        res = simulate(row, flat, Config())
        no_fund = simulate(dict(row, funding=0.0), flat, Config())
        self.assertAlmostEqual(res["cost_r"] - no_fund["cost_r"], 0.1 * 9 / 8 / 100 * 100 / 2, places=3)

    def test_self_improvement_only_proposes(self):
        rows = []
        for i in range(60):
            deep = i % 2 == 0
            rows.append({"taken": 1, "entry_time": i, "symbol": "X",
                         "outcome": "LOSS" if deep else "WIN_TP2", "realized_r": -1.0 if deep else 2.0,
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

    def test_self_improvement_rejects_in_sample_only_effect(self):
        rows = []
        for i in range(100):
            deep = i % 2 == 0
            if i < 70:  # train: deep corrections lose
                r = -1.0 if deep else 2.0
            else:       # test: the effect reverses
                r = 2.0 if deep else -1.0
            rows.append({"taken": 1, "entry_time": i, "symbol": "X", "outcome": "X", "realized_r": r,
                         "correction_depth": 70.0 if deep else 45.0, "pivot_score": 85, "rs_7d": 5, "rs_4h": 1,
                         "volume_ratio": 1.3, "oi_regime": "X", "funding_state": "NEUTRAL", "funding": 0.01,
                         "retest_status": "RETEST_CONFIRMED", "entry_mode": "B_STANDARD", "rr": 2.5,
                         "mfe": 1, "mae": 0.5, "false_breakout": 0, "components_json": None,
                         "failed_json": "[]", "pivot_confirmations": 4})
        rep = SelfImprovementAgent(Config()).run(rows)
        self.assertNotIn("correction.max_depth_pct", [p["parameter"] for p in rep.proposals])
        self.assertIn("correction.max_depth_pct",
                      [p["parameter"] for p in rep.analysis["rejected_out_of_sample"]])

    def test_portfolio_report(self):
        from pivot_engine.portfolio import portfolio_report
        rows = [{"taken": 1, "outcome": "X", "realized_r": r, "gross_r": r + 0.1, "cost_r": 0.1,
                 "entry_time": i * 10 * HOUR_MS, "exit_time": i * 10 * HOUR_MS + 5 * HOUR_MS}
                for i, r in enumerate([2.0, -1.0, -1.0, -1.0, 3.0, -1.0])]
        rep = portfolio_report(rows, Config())
        self.assertEqual(rep["max_drawdown_r"], 3.0)
        self.assertEqual(rep["longest_losing_streak"], 3)
        self.assertEqual(rep["profit_factor"], 1.25)
        self.assertEqual(rep["max_concurrent_positions"], 1)


if __name__ == "__main__":
    unittest.main()


class CoinFilterTests(unittest.TestCase):
    def test_walk_forward_uses_only_past_window(self):
        from pivot_engine.coin_filter import select_coins, walk_forward
        rows = []
        for i in range(80):
            sym = "AAA" if i % 2 else "BBB"
            # AAA wins in the first half, loses in the second: an in-sample whitelist picks it and pays for it.
            r = (2.0 if i < 40 else -1.0) if sym == "AAA" else 0.5
            rows.append({"symbol": sym, "entry_time": i, "realized_r": r, "outcome": "X", "taken": 1})
        self.assertEqual(select_coins(rows[:40], 1, 0.0), {"AAA", "BBB"})
        self.assertEqual(select_coins(rows[:40], 1, 5.0), {"AAA"})  # shrunk mean above global mean
        res = walk_forward(rows, folds=2, shrink_k=5.0)
        self.assertLess(res["out_of_sample"]["whitelist"]["expectancy_r"],
                        res["out_of_sample"]["all"]["expectancy_r"])
