"""Walk-forward backtest: replays history step by step through the full orchestrator.

Every step sees only candles closed before the cursor (no look-ahead). Setups,
alerts and outcomes go to the journal, which then feeds the Self-Improvement agent.
"""
from __future__ import annotations

import time

from .agents.orchestrator import PivotOrchestrator
from .alerts import AlertDispatcher
from .config import Config
from .journal import Journal
from .models import HOUR_MS, INTERVAL_MS


def run_backtest(provider, cfg: Config, journal: Journal, symbols: list[str] | None = None,
                 step_h: int = 4, warmup_days: int = 25, days: float | None = None,
                 progress: bool = True) -> dict:
    """`provider` must support set_cursor() and expose end_ms (Synthetic/Replay providers)."""
    orch = PivotOrchestrator(cfg, provider, journal)
    dispatcher = AlertDispatcher(journal, sinks=[])
    end = provider.end_ms
    first = min(provider.klines(s, "1h", 10**6)[0].t for s in (symbols or provider.symbols()))
    start = first + warmup_days * INTERVAL_MS["1d"]
    if days is not None:
        start = max(start, end - int(days * INTERVAL_MS["1d"]))
    t, steps, t0 = start, 0, time.time()
    total = max(1, (end - start) // (step_h * HOUR_MS))
    statuses: dict[str, int] = {}
    while t <= end:
        provider.set_cursor(t)
        results = orch.run(symbols)
        for a in results:
            journal.record(a)
            statuses[a.status] = statuses.get(a.status, 0) + 1
        dispatcher.process(results)
        journal.update_outcomes(provider)
        steps += 1
        if progress and steps % 25 == 0:
            print(f"  backtest {steps}/{total} steps ({time.time() - t0:.0f}s)", flush=True)
        t += step_h * HOUR_MS
    provider.set_cursor(end)
    journal.update_outcomes(provider)
    rows = journal.rows()
    return {"steps": steps, "seconds": round(time.time() - t0, 1), "status_counts": statuses,
            "setups": len(rows), "taken": sum(r["taken"] for r in rows),
            "closed": sum(1 for r in rows if r["outcome"] not in (None, "OPEN"))}
