"""Walk-forward test of a per-coin whitelist ("trade only coins that were profitable").

Selecting coins on the same backtest you then report is in-sample selection: it
always looks good. This module measures the idea honestly: pick coins on an
earlier window, then score the pick on the *following* window it never saw.
"""
from __future__ import annotations

from collections import defaultdict


def _summary(rows: list[dict]) -> dict:
    n = len(rows)
    if not n:
        return {"n": 0, "win_rate": None, "expectancy_r": None, "total_r": 0.0}
    rs = [r["realized_r"] for r in rows]
    return {"n": n, "win_rate": round(sum(1 for x in rs if x > 0) / n * 100, 1),
            "expectancy_r": round(sum(rs) / n, 3), "total_r": round(sum(rs), 2)}


def select_coins(rows: list[dict], min_trades: int, shrink_k: float) -> set[str]:
    """Coins whose shrunk mean R is above the global mean of the window.

    Shrinkage: mean_shrunk = (n*mean + k*global) / (n + k). Coins with few trades
    are pulled toward the global mean so one lucky trade cannot whitelist a coin.
    shrink_k = 0 reproduces the naive "sum of R > 0" rule.
    """
    by: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        by[r["symbol"]].append(r["realized_r"])
    if not rows:
        return set()
    global_mean = sum(r["realized_r"] for r in rows) / len(rows)
    keep = set()
    for sym, rs in by.items():
        if len(rs) < min_trades:
            continue
        if shrink_k <= 0:
            if sum(rs) > 0:
                keep.add(sym)
            continue
        shrunk = (sum(rs) + shrink_k * global_mean) / (len(rs) + shrink_k)
        if shrunk > global_mean:
            keep.add(sym)
    return keep


def walk_forward(rows: list[dict], folds: int = 4, min_trades: int = 1, shrink_k: float = 0.0,
                 taken_only: bool = False) -> dict:
    closed = [r for r in rows if r.get("outcome") not in (None, "OPEN") and r.get("realized_r") is not None
              and (r["taken"] or not taken_only)]
    closed.sort(key=lambda r: r["entry_time"])
    if len(closed) < folds * 2:
        return {"error": f"too few closed setups ({len(closed)}) for {folds} folds"}
    t0, t1 = closed[0]["entry_time"], closed[-1]["entry_time"] + 1
    edges = [t0 + (t1 - t0) * i // folds for i in range(folds + 1)]
    windows = [[r for r in closed if edges[i] <= r["entry_time"] < edges[i + 1]] for i in range(folds)]
    steps = []
    agg = {"all": [], "whitelist": [], "blacklist": []}
    for i in range(folds - 1):
        train, test = windows[i], windows[i + 1]
        keep = select_coins(train, min_trades, shrink_k)
        seen = {r["symbol"] for r in train}
        wl = [r for r in test if r["symbol"] in keep]
        bl = [r for r in test if r["symbol"] in seen and r["symbol"] not in keep]
        agg["all"] += test
        agg["whitelist"] += wl
        agg["blacklist"] += bl
        steps.append({"train_fold": i + 1, "test_fold": i + 2, "whitelisted_coins": len(keep),
                      "coins_seen": len(seen),
                      "in_sample_whitelist": _summary([r for r in train if r["symbol"] in keep]),
                      "test_all": _summary(test), "test_whitelist": _summary(wl), "test_blacklist": _summary(bl)})
    out = {"setups": len(closed), "folds": folds, "min_trades": min_trades, "shrink_k": shrink_k,
           "taken_only": taken_only, "steps": steps,
           "out_of_sample": {k: _summary(v) for k, v in agg.items()}}
    a, w = out["out_of_sample"]["all"], out["out_of_sample"]["whitelist"]
    if a["n"] and w["n"]:
        out["whitelist_edge_r"] = round(w["expectancy_r"] - a["expectancy_r"], 3)
    return out


def format_report(res: dict) -> str:
    if "error" in res:
        return res["error"]
    lines = [f"Walk-forward coin whitelist  (setups={res['setups']}, folds={res['folds']}, "
             f"min_trades={res['min_trades']}, shrink_k={res['shrink_k']}, taken_only={res['taken_only']})", ""]
    lines.append(f"{'step':<8}{'coins kept':<12}{'IN-SAMPLE whitelist':<26}{'TEST all':<24}{'TEST whitelist':<24}TEST blacklist")

    def f(s):
        return "—" if not s["n"] else f"n={s['n']} E={s['expectancy_r']:+.2f}R"

    for s in res["steps"]:
        lines.append(f"{s['train_fold']}→{s['test_fold']:<5}{str(s['whitelisted_coins']) + '/' + str(s['coins_seen']):<12}"
                     f"{f(s['in_sample_whitelist']):<26}{f(s['test_all']):<24}{f(s['test_whitelist']):<24}{f(s['test_blacklist'])}")
    o = res["out_of_sample"]
    lines += ["", "OUT-OF-SAMPLE total:",
              f"  all coins : {f(o['all'])}  win {o['all']['win_rate']}%",
              f"  whitelist : {f(o['whitelist'])}  win {o['whitelist']['win_rate']}%",
              f"  blacklist : {f(o['blacklist'])}  win {o['blacklist']['win_rate']}%"]
    if "whitelist_edge_r" in res:
        lines.append(f"  whitelist edge vs all: {res['whitelist_edge_r']:+.3f}R per setup")
    return "\n".join(lines)
