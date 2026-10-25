"""Portfolio report: equity curve and risk metrics of the journal's closed trades.

Win rate and expectancy alone hide how a system feels to trade. This report adds
drawdown, Sharpe/Sortino, profit factor, losing streaks, exposure, overlap of
positions, bootstrap confidence intervals and a Monte Carlo of trade order.
"""
from __future__ import annotations

import math
import random
from collections import defaultdict
from datetime import datetime, timezone

from .config import Config
from .models import HOUR_MS
from .stats import bootstrap_ci, max_drawdown, mean

DAY_MS = 24 * HOUR_MS


def _closed(rows: list[dict], taken_only: bool) -> list[dict]:
    out = [r for r in rows if r.get("outcome") not in (None, "OPEN") and r.get("realized_r") is not None
           and r.get("exit_time") and (r["taken"] or not taken_only)]
    return sorted(out, key=lambda r: r["exit_time"])


def portfolio_report(rows: list[dict], cfg: Config, taken_only: bool = True) -> dict:
    trades = _closed(rows, taken_only)
    rep: dict = {"sample": "LONG_READY trades" if taken_only else "all pivot setups (incl. filtered)",
                 "trades": len(trades)}
    if not trades:
        rep["note"] = "no closed trades"
        return rep
    pc = cfg.portfolio
    rs = [r["realized_r"] for r in trades]
    gross = [r["gross_r"] for r in trades if r.get("gross_r") is not None]
    costs = [r["cost_r"] for r in trades if r.get("cost_r") is not None]
    wins = [x for x in rs if x > 0]
    losses = [x for x in rs if x <= 0]

    # Equity: R curve and compounding % curve at a fixed risk per trade.
    eq, peak, dd_pct = 1.0, 1.0, 0.0
    for r in rs:
        eq *= 1 + r * pc.risk_per_trade_pct / 100
        peak = max(peak, eq)
        dd_pct = max(dd_pct, (peak - eq) / peak * 100)

    # Daily returns (by exit day) over the whole active period, including flat days.
    first = min(r["entry_time"] for r in trades)
    last = max(r["exit_time"] for r in trades)
    days = max(1, math.ceil((last - first) / DAY_MS))
    daily: dict[int, float] = defaultdict(float)
    for r in trades:
        daily[(r["exit_time"] - first) // DAY_MS] += r["realized_r"] * pc.risk_per_trade_pct / 100
    series = [daily.get(d, 0.0) for d in range(days)]
    mu = mean(series)
    sd = math.sqrt(mean([(x - mu) ** 2 for x in series])) if len(series) > 1 else 0.0
    down = math.sqrt(mean([min(0.0, x) ** 2 for x in series])) if series else 0.0

    # Streaks, exposure and overlap.
    streak = worst = 0
    for x in rs:
        streak = streak + 1 if x <= 0 else 0
        worst = max(worst, streak)
    events = sorted([(r["entry_time"], 1) for r in trades] + [(r["exit_time"], -1) for r in trades])
    open_n = max_open = 0
    busy = 0
    prev_t = events[0][0]
    for t, d in events:
        if open_n > 0:
            busy += t - prev_t
        open_n += d
        max_open = max(max_open, open_n)
        prev_t = t

    # Monte Carlo: same trades, random order -> distribution of max drawdown.
    rng = random.Random(7)
    mc = []
    for _ in range(pc.monte_carlo_runs):
        shuffled = rs[:]
        rng.shuffle(shuffled)
        mc.append(max_drawdown(shuffled))
    mc.sort()

    by_outcome: dict[str, list[float]] = defaultdict(list)
    for r in trades:
        by_outcome[r["outcome"]].append(r["realized_r"])
    buckets = [(-99, -1.0001), (-1.0001, 0), (0, 1), (1, 2), (2, 4), (4, 999)]
    labels = ["< -1R", "-1R..0", "0..1R", "1..2R", "2..4R", "> 4R"]

    rep.update({
        "period_days": days,
        "trades_per_month": round(len(trades) / (days / 30.44), 2),
        "win_rate": round(len(wins) / len(rs) * 100, 1),
        "expectancy_r": round(mean(rs), 3),
        "expectancy_ci95": bootstrap_ci(rs, pc.bootstrap_runs),
        "gross_expectancy_r": round(mean(gross), 3) if gross else None,
        "avg_cost_r": round(mean(costs), 3) if costs else None,
        "total_r": round(sum(rs), 2),
        "profit_factor": round(sum(wins) / -sum(losses), 2) if losses and sum(losses) < 0 else None,
        "avg_win_r": round(mean(wins), 3) if wins else None,
        "avg_loss_r": round(mean(losses), 3) if losses else None,
        "max_drawdown_r": round(max_drawdown(rs), 2),
        "risk_per_trade_pct": pc.risk_per_trade_pct,
        "return_pct": round((eq - 1) * 100, 2),
        "max_drawdown_pct": round(dd_pct, 2),
        "sharpe_annual": round(mu / sd * math.sqrt(365), 2) if sd else None,
        "sortino_annual": round(mu / down * math.sqrt(365), 2) if down else None,
        "longest_losing_streak": worst,
        "exposure_pct": round(busy / max(1, last - first) * 100, 1),
        "max_concurrent_positions": max_open,
        "monte_carlo_max_dd_r": {"p50": round(mc[len(mc) // 2], 2), "p95": round(mc[int(len(mc) * 0.95)], 2)},
        "by_outcome": {k: {"n": len(v), "avg_r": round(mean(v), 3)} for k, v in sorted(by_outcome.items())},
        "r_distribution": {lab: sum(1 for x in rs if lo < x <= hi) for (lo, hi), lab in zip(buckets, labels)},
        "start": datetime.fromtimestamp(first / 1000, tz=timezone.utc).strftime("%Y-%m-%d"),
        "end": datetime.fromtimestamp(last / 1000, tz=timezone.utc).strftime("%Y-%m-%d"),
    })
    warnings = []
    if len(trades) < 30:
        warnings.append(f"only {len(trades)} trades — every metric above has a very wide error band")
    if not taken_only:
        warnings.append("hypothetical entries that overlap in time (no position limit): "
                        "the % return / Sharpe are not achievable, use R metrics only")
    if warnings:
        rep["warning"] = "; ".join(warnings)
    return rep


def format_portfolio(rep: dict) -> str:
    if rep.get("trades", 0) == 0:
        return f"{rep['sample']}: no closed trades"
    ci = rep["expectancy_ci95"]
    ci_txt = f"[{ci[0]:+.2f}R, {ci[1]:+.2f}R]" if ci else "n/a"
    lines = [
        f"PORTFOLIO REPORT — {rep['sample']}  ({rep['start']} → {rep['end']}, {rep['period_days']} days)",
        f"  trades            {rep['trades']}  ({rep['trades_per_month']}/month)",
        f"  win rate          {rep['win_rate']}%",
        f"  expectancy (net)  {rep['expectancy_r']:+.3f}R   95% CI {ci_txt}",
        f"  gross / costs     {rep['gross_expectancy_r']}R gross, {rep['avg_cost_r']}R avg cost per trade",
        f"  total             {rep['total_r']:+.2f}R   profit factor {rep['profit_factor']}",
        f"  avg win / loss    {rep['avg_win_r']}R / {rep['avg_loss_r']}R",
        f"  max drawdown      {rep['max_drawdown_r']}R   (Monte Carlo p50 {rep['monte_carlo_max_dd_r']['p50']}R,"
        f" p95 {rep['monte_carlo_max_dd_r']['p95']}R)",
        f"  at {rep['risk_per_trade_pct']}% risk/trade  return {rep['return_pct']:+.2f}%, max DD {rep['max_drawdown_pct']}%",
        f"  Sharpe / Sortino  {rep['sharpe_annual']} / {rep['sortino_annual']} (annualised, daily)",
        f"  losing streak     {rep['longest_losing_streak']}   exposure {rep['exposure_pct']}%   "
        f"max concurrent {rep['max_concurrent_positions']}",
        "  outcomes          " + ", ".join(f"{k} {v['n']}× ({v['avg_r']:+.2f}R)" for k, v in rep["by_outcome"].items()),
        "  R distribution    " + ", ".join(f"{k}: {v}" for k, v in rep["r_distribution"].items()),
    ]
    if rep.get("warning"):
        lines.append(f"  ⚠ {rep['warning']}")
    return "\n".join(lines)
