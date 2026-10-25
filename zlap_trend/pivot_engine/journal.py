"""Setup journal (SQLite): every setup, its alerts, paper position tracking and outcome.

Feeds the Self-Improvement agent. Outcome model (per setup, in R):
* SL before TP1                      -> LOSS, -1R
* TP1 hit -> partial close, SL to BE -> MANAGEMENT
* then TP2                           -> WIN_TP2
* then back to BE                    -> WIN_TP1
* max hold reached                   -> TIMEOUT (open part marked to market)
Untaken setups (PIVOT_DETECTED but filtered) are evaluated the same way from the
moment they were first recorded, so the optimizer can measure what each filter
is worth.
"""
from __future__ import annotations

import json
import sqlite3
from typing import Any

from .config import Config
from .indicators import last_atr
from .models import HOUR_MS, Line, Status

SCHEMA = """
CREATE TABLE IF NOT EXISTS setups (
    setup_id TEXT PRIMARY KEY,
    symbol TEXT NOT NULL,
    first_seen INTEGER NOT NULL,
    timestamp INTEGER NOT NULL,
    status TEXT,
    best_status TEXT,
    taken INTEGER DEFAULT 0,
    entry_time INTEGER,
    entry_mode TEXT,
    pivot_score REAL,
    entry REAL, sl REAL, tp1 REAL, tp2 REAL, rr REAL, rr_tp2 REAL,
    rs_4h REAL, rs_3d REAL, rs_7d REAL,
    volume_score REAL, volume_ratio REAL,
    oi_change REAL, oi_regime TEXT,
    funding REAL, funding_state TEXT,
    correction_depth REAL, atr_1h REAL,
    retest_status TEXT, pivot_confirmations INTEGER, critic_majors INTEGER,
    line_json TEXT, components_json TEXT, failed_json TEXT,
    position_status TEXT,
    outcome TEXT, exit_time INTEGER, realized_r REAL,
    mfe REAL, mae REAL, max_r REAL, false_breakout INTEGER
);
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    setup_id TEXT, symbol TEXT, kind TEXT, timestamp INTEGER, text TEXT
);
CREATE TABLE IF NOT EXISTS proposals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created INTEGER, kind TEXT, parameter TEXT,
    old_rule TEXT, new_rule TEXT, backtest_json TEXT,
    expected_impact TEXT, risk TEXT, status TEXT DEFAULT 'PENDING_HUMAN_REVIEW'
);
"""

ORDER = {s: i for i, s in enumerate(Status.ORDER)}


class Journal:
    def __init__(self, path: str = "zlap_trend_journal.sqlite", cfg: Config | None = None):
        self.cfg = cfg or Config()
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    # ---------------------------------------------------------------- record
    def record(self, a) -> None:
        """Upsert a setup from a SetupAnalysis (only once a pivot exists)."""
        if not a.setup_id or a.pivot is None or not a.pivot.pivot_detected:
            return
        r = a.risk
        if r is None or r.sl is None or r.tp1 is None or r.entry is None or r.entry <= r.sl:
            return
        row = self.get(a.setup_id)
        taken_now = a.status == Status.LONG_READY
        if row and row["taken"]:
            self.db.execute("UPDATE setups SET timestamp=?, status=? WHERE setup_id=?",
                            (a.timestamp, a.status, a.setup_id))
            self.db.commit()
            return
        best = a.status if not row or ORDER.get(a.status, -1) > ORDER.get(row["best_status"], -1) else row["best_status"]
        line = a.trendlines.correction_line
        data: dict[str, Any] = {
            "setup_id": a.setup_id, "symbol": a.symbol, "timestamp": a.timestamp,
            "status": a.status, "best_status": best,
            "pivot_score": a.score.pivot_score,
            "rs_4h": a.scan.rs_4h, "rs_3d": a.scan.rs_3d, "rs_7d": a.scan.rs_7d,
            "volume_score": a.volume.volume_score, "volume_ratio": a.volume.volume_ratio,
            "oi_change": a.derivatives.oi_change, "oi_regime": a.derivatives.oi_regime,
            "funding": a.derivatives.funding, "funding_state": a.derivatives.funding_state,
            "correction_depth": a.correction.correction_depth,
            "atr_1h": last_atr(a.candles["1h"]),
            "retest_status": a.retest.status, "pivot_confirmations": a.pivot.confirmation_count,
            "critic_majors": sum(1 for o in a.critic.objections if o["severity"] in ("MAJOR", "CRITICAL")),
            "line_json": json.dumps(line.to_dict()) if line else None,
            "components_json": json.dumps(a.score.components),
            "failed_json": json.dumps(failed_filters(a, self.cfg)),
        }
        levels = {"entry": r.entry, "sl": r.sl, "tp1": r.tp1, "tp2": r.tp2, "rr": r.rr, "rr_tp2": r.rr_tp2,
                  "entry_time": a.timestamp, "entry_mode": a.entry.mode}
        if not row:
            data.update(levels, first_seen=a.timestamp, taken=int(taken_now),
                        position_status=Status.ACTIVE_POSITION if taken_now else None)
            cols = ",".join(data)
            self.db.execute(f"INSERT INTO setups ({cols}) VALUES ({','.join('?' * len(data))})",
                            list(data.values()))
        else:
            if taken_now:  # freeze the real entry; reset the hypothetical outcome
                data.update(levels, taken=1, position_status=Status.ACTIVE_POSITION, outcome=None,
                            exit_time=None, realized_r=None, mfe=None, mae=None, max_r=None, false_breakout=None)
            else:
                for k in ("pivot_score", "components_json"):
                    data.pop(k)  # hypothetical setups keep their first snapshot
            sets = ",".join(f"{k}=?" for k in data if k != "setup_id")
            self.db.execute(f"UPDATE setups SET {sets} WHERE setup_id=?",
                            [v for k, v in data.items() if k != "setup_id"] + [a.setup_id])
        self.db.commit()

    def get(self, setup_id: str):
        return self.db.execute("SELECT * FROM setups WHERE setup_id=?", (setup_id,)).fetchone()

    def rows(self, closed_only: bool = False) -> list[dict]:
        q = "SELECT * FROM setups" + (" WHERE outcome IS NOT NULL AND outcome != 'OPEN'" if closed_only else "")
        return [dict(r) for r in self.db.execute(q + " ORDER BY first_seen")]

    def position_status(self, setup_id: str) -> str | None:
        row = self.get(setup_id)
        return row["position_status"] if row and row["taken"] else None

    # ---------------------------------------------------------------- alerts
    def add_alert(self, setup_id, symbol, kind, timestamp, text) -> None:
        self.db.execute("INSERT INTO alerts (setup_id, symbol, kind, timestamp, text) VALUES (?,?,?,?,?)",
                        (setup_id, symbol, kind, timestamp, text))
        self.db.commit()

    def alert_sent(self, setup_id: str, kind: str) -> bool:
        return self.db.execute("SELECT 1 FROM alerts WHERE setup_id=? AND kind=?",
                               (setup_id, kind)).fetchone() is not None

    def find_recent_signal(self, symbol, setup_id, ts, cooldown_h) -> str | None:
        row = self.db.execute(
            "SELECT setup_id, timestamp FROM alerts WHERE kind='LONG_READY' AND "
            "(setup_id=? OR (symbol=? AND ? - timestamp < ?)) ORDER BY timestamp DESC LIMIT 1",
            (setup_id, symbol, ts, cooldown_h * HOUR_MS)).fetchone()
        return f"{row['setup_id']} @ {row['timestamp']}" if row else None

    # ---------------------------------------------------------------- outcomes
    def update_outcomes(self, provider) -> int:
        """Advance open setups with candles closed since entry. Returns number closed."""
        closed = 0
        rows = self.db.execute("SELECT * FROM setups WHERE outcome IS NULL OR outcome='OPEN'").fetchall()
        for row in rows:
            candles = [c for c in provider.klines(row["symbol"], "1h", 1000) if c.t >= row["entry_time"]]
            res = simulate(dict(row), candles, self.cfg)
            self.db.execute(
                "UPDATE setups SET outcome=?, exit_time=?, realized_r=?, mfe=?, mae=?, max_r=?, "
                "false_breakout=?, position_status=? WHERE setup_id=?",
                (res["outcome"], res["exit_time"], res["realized_r"], res["mfe"], res["mae"], res["max_r"],
                 res["false_breakout"], res["position_status"] if row["taken"] else None, row["setup_id"]))
            closed += res["outcome"] != "OPEN"
        self.db.commit()
        return closed

    # ---------------------------------------------------------------- proposals
    def save_proposal(self, p: dict, created: int) -> None:
        self.db.execute(
            "INSERT INTO proposals (created, kind, parameter, old_rule, new_rule, backtest_json, "
            "expected_impact, risk) VALUES (?,?,?,?,?,?,?,?)",
            (created, p["kind"], p.get("parameter"), p["old_rule"], p["new_rule"],
             json.dumps(p["backtest_result"]), p["expected_impact"], p["risk"]))
        self.db.commit()

    def proposals(self) -> list[dict]:
        return [dict(r) for r in self.db.execute("SELECT * FROM proposals ORDER BY id DESC")]


def failed_filters(a, cfg: Config) -> list[str]:
    """Everything that kept this setup from LONG_READY (used for what-if analysis)."""
    failed = [k for k, v in a.final_rule.items() if not v]
    failed += [o["code"] for o in a.critic.objections if o["severity"] == "CRITICAL"]
    if not a.entry.ready:
        failed.append("ENTRY_NOT_READY")
    if a.score.pivot_score < cfg.scoring.long_ready:
        failed.append("SCORE_BELOW_THRESHOLD")
    if a.status in (Status.INVALIDATED, Status.EXTENDED):
        failed.append(a.status)
    return failed


def simulate(row: dict, candles, cfg: Config) -> dict:
    entry, sl, tp1, tp2 = row["entry"], row["sl"], row["tp1"], row["tp2"]
    risk = entry - sl
    partial = cfg.risk.tp1_partial
    rr1 = (tp1 - entry) / risk
    rr2 = (tp2 - entry) / risk if tp2 else None
    line = Line(**{k: v for k, v in json.loads(row["line_json"]).items() if k in ("t1", "p1", "t2", "p2")}) \
        if row.get("line_json") else None
    stop, hit1 = sl, False
    hi, lo = entry, entry
    out = {"outcome": "OPEN", "exit_time": None, "realized_r": None, "false_breakout": 0,
           "position_status": Status.ACTIVE_POSITION}
    bars = candles  # entry_time is the scan moment: every candle here opened after the entry
    for n, c in enumerate(bars):
        hi, lo = max(hi, c.h), min(lo, c.l)
        if c.l <= stop:  # conservative: stop checked before targets on the same bar
            out["exit_time"] = c.close_time
            if hit1:
                out["outcome"], out["realized_r"] = "WIN_TP1", partial * rr1
            else:
                out["outcome"], out["realized_r"] = "LOSS", -1.0
                if line is not None:
                    out["false_breakout"] = int(any(x.c < line.value(x.close_time) for x in bars[:n + 1][:12]))
            break
        if not hit1 and c.h >= tp1:
            hit1, stop = True, entry
            out["position_status"] = Status.MANAGEMENT
        if hit1 and rr2 is not None and c.h >= tp2:
            out["outcome"], out["realized_r"], out["exit_time"] = "WIN_TP2", partial * rr1 + (1 - partial) * rr2, c.close_time
            break
        if n + 1 >= cfg.risk.max_hold_bars_1h:
            open_r = (c.c - entry) / risk
            out["outcome"], out["exit_time"] = "TIMEOUT", c.close_time
            out["realized_r"] = (partial * rr1 + (1 - partial) * max(0.0, open_r)) if hit1 else open_r
            break
    if out["outcome"] != "OPEN":
        out["position_status"] = Status.EXIT
    out["mfe"] = round((hi - entry) / risk, 3)
    out["mae"] = round((entry - lo) / risk, 3)
    out["max_r"] = out["mfe"]
    if out["realized_r"] is not None:
        out["realized_r"] = round(out["realized_r"], 3)
    return out
