"""ZŁAP TREND — Pivot Engine command line.

    python -m pivot_engine scan     [--provider binance|synthetic] [--symbols ...] [--html out.html]
    python -m pivot_engine watch    --interval 15            (scan loop, alerts)
    python -m pivot_engine detail   SYMBOL                    (full agent report, JSON)
    python -m pivot_engine backtest [--provider synthetic-history|binance] [--days N]
    python -m pivot_engine optimize                           (SYSTEM_OPTIMIZATION_PROPOSAL)
    python -m pivot_engine journal                            (setups + outcomes)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone

from .agents.orchestrator import PivotOrchestrator
from .agents.self_improvement import SelfImprovementAgent
from .alerts import AlertDispatcher, ConsoleSink, FileSink, TelegramSink, WebhookSink
from .chart import render_dashboard
from .config import Config
from .journal import Journal
from .terminal import legend, render_detail, render_table


def _provider(name: str, args):
    from .data import BinanceFuturesProvider, SyntheticProvider, random_history_specs
    if name == "binance":
        return BinanceFuturesProvider(market_cap_file=getattr(args, "mcap_file", None))
    if name == "synthetic":
        return SyntheticProvider()
    if name == "synthetic-history":
        return SyntheticProvider(random_history_specs(n_symbols=args.n_symbols, days=args.history_days,
                                                      seed=args.seed))
    raise SystemExit(f"unknown provider {name}")


def _sinks(args) -> list:
    sinks = [] if args.quiet_alerts else [ConsoleSink()]
    if args.alerts_file:
        sinks.append(FileSink(args.alerts_file))
    if args.telegram:
        sinks.append(TelegramSink())
    if args.webhook:
        sinks.append(WebhookSink(args.webhook))
    return sinks


def _ts(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def cmd_scan(args, cfg: Config) -> list:
    provider = _provider(args.provider, args)
    journal = Journal(args.journal, cfg)
    journal.update_outcomes(provider)
    orch = PivotOrchestrator(cfg, provider, journal)
    results = orch.run(args.symbols or None)
    for a in results:
        journal.record(a)
    sent = AlertDispatcher(journal, _sinks(args)).process(results)
    color = not args.no_color and sys.stdout.isatty()
    shown = results if args.all else [a for a in results if a.status != "SCANNING"] or results
    print(f"\n🎯 ZŁAP TREND — PIVOT ENGINE   {provider.name}   {_ts(provider.now_ms())}\n")
    print(render_table(shown, color))
    print("\n" + legend(color) + "\n")
    for a in shown:
        if a.status != "SCANNING":
            print(render_detail(a, color))
    if args.html:
        alerts = {sym: text for sym, _, text in sent}
        with open(args.html, "w", encoding="utf-8") as fh:
            fh.write(render_dashboard(shown, subtitle=f"{provider.name} · {_ts(provider.now_ms())}", alerts=alerts))
        print(f"\ndashboard: {args.html}")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump([a.to_dict() for a in results], fh, indent=1, default=str)
        print(f"json: {args.json}")
    return results


def cmd_watch(args, cfg: Config) -> None:
    while True:
        try:
            cmd_scan(args, cfg)
        except Exception as exc:  # keep the loop alive on transient API errors
            print(f"scan failed: {exc}", file=sys.stderr)
        time.sleep(args.interval * 60)


def cmd_detail(args, cfg: Config) -> None:
    provider = _provider(args.provider, args)
    orch = PivotOrchestrator(cfg, provider, Journal(args.journal, cfg))
    results = orch.run([args.symbol, "BTCUSDT"] if args.symbol != "BTCUSDT" else None)
    a = next((x for x in results if x.symbol == args.symbol), None)
    if a is None:
        raise SystemExit(f"{args.symbol} not found")
    print(json.dumps(a.to_dict(), indent=1, default=str))


def cmd_backtest(args, cfg: Config) -> None:
    from .backtest import run_backtest
    if args.provider == "binance":
        from .data import BinanceFuturesProvider
        from .data.replay import ReplayProvider
        if not args.symbols:
            raise SystemExit("--symbols required for a Binance replay")
        syms = list(dict.fromkeys(args.symbols + ["BTCUSDT"]))
        provider = ReplayProvider.from_binance(BinanceFuturesProvider(), syms, args.days)
    else:
        provider = _provider(args.provider, args)
    journal = Journal(args.journal, cfg)
    summary = run_backtest(provider, cfg, journal, args.symbols or None, step_h=args.step_h,
                           days=args.days if args.provider == "binance" else None)
    print(json.dumps(summary, indent=1))
    rep = SelfImprovementAgent(cfg).run(journal.rows())
    print(json.dumps(rep.analysis.get("taken", {}), indent=1))
    print(f"journal: {args.journal} — run `optimize` for proposals")


def cmd_optimize(args, cfg: Config) -> None:
    journal = Journal(args.journal, cfg)
    rep = SelfImprovementAgent(cfg).run(journal.rows())
    now = int(time.time() * 1000)
    for p in rep.proposals:
        journal.save_proposal(p, now)
    out = rep.to_dict()
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out["sample"], indent=1))
    for n in rep.notes:
        print("note:", n)
    for i, p in enumerate(rep.proposals, 1):
        print(f"\nSYSTEM_OPTIMIZATION_PROPOSAL #{i} [{p['status']}]")
        print(f"  OLD RULE:        {p['old_rule']}")
        print(f"  NEW RULE:        {p['new_rule']}")
        b = p["backtest_result"]
        print(f"  BACKTEST RESULT: before n={b['before']['n']} win={b['before']['win_rate']}% "
              f"E={b['before']['expectancy_r']}R | after n={b['after']['n']} win={b['after']['win_rate']}% "
              f"E={b['after']['expectancy_r']}R")
        print(f"  EXPECTED IMPACT: {p['expected_impact']}")
        print(f"  RISK:            {p['risk']}")
    print(f"\nfull report: {args.out}  (proposals are NOT applied — edit your --config JSON to adopt one)")


def cmd_journal(args, cfg: Config) -> None:
    rows = Journal(args.journal, cfg).rows()
    cols = ["setup_id", "best_status", "taken", "entry_mode", "pivot_score", "entry", "sl", "tp1", "rr",
            "outcome", "realized_r", "mfe", "mae"]
    print("  ".join(cols))
    for r in rows[-args.limit:]:
        print("  ".join(str(round(r[c], 5) if isinstance(r[c], float) else r[c]) for c in cols))


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="pivot_engine", description="ZŁAP TREND — multi-agent Pivot Engine")
    ap.add_argument("--config", help="JSON config override")
    ap.add_argument("--journal", default="zlap_trend_journal.sqlite")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, default_provider="binance"):
        p.add_argument("--provider", default=default_provider,
                       choices=["binance", "synthetic", "synthetic-history"])
        p.add_argument("--symbols", nargs="*")
        p.add_argument("--mcap-file", help="JSON {symbol: market_cap} (Binance has no market caps)")
        p.add_argument("--n-symbols", type=int, default=16)
        p.add_argument("--history-days", type=float, default=150)
        p.add_argument("--seed", type=int, default=7)

    for name in ("scan", "watch"):
        p = sub.add_parser(name)
        common(p)
        p.add_argument("--all", action="store_true", help="also list non-leaders")
        p.add_argument("--html", help="write the HTML dashboard with charts")
        p.add_argument("--json", help="write every agent's output as JSON")
        p.add_argument("--no-color", action="store_true")
        p.add_argument("--alerts-file")
        p.add_argument("--telegram", action="store_true")
        p.add_argument("--webhook")
        p.add_argument("--quiet-alerts", action="store_true")
        if name == "watch":
            p.add_argument("--interval", type=float, default=15, help="minutes between scans")
    p = sub.add_parser("detail")
    common(p)
    p.add_argument("symbol")
    p = sub.add_parser("backtest")
    common(p, "synthetic-history")
    p.add_argument("--days", type=float, default=60)
    p.add_argument("--step-h", type=int, default=4)
    p = sub.add_parser("optimize")
    p.add_argument("--out", default="SYSTEM_OPTIMIZATION_PROPOSAL.json")
    p = sub.add_parser("journal")
    p.add_argument("--limit", type=int, default=50)

    args = ap.parse_args(argv)
    cfg = Config.load(args.config)
    {"scan": cmd_scan, "watch": cmd_watch, "detail": cmd_detail, "backtest": cmd_backtest,
     "optimize": cmd_optimize, "journal": cmd_journal}[args.cmd](args, cfg)


if __name__ == "__main__":
    main()
