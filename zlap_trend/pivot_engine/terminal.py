"""TERMINAL UI: one row per coin with every column from the spec, status colours."""
from __future__ import annotations

from .models import ANSI_RESET, STATUS_COLORS, Status

COLUMNS = ["SYMBOL", "PRICE", "4H TREND", "3D TREND", "7D TREND", "RS vs BTC (4H/3D/7D)", "VOL SCORE",
           "FUNDING", "OI", "IMPULSE", "CORR %", "CORR LINE", "DIST CL", "PIVOT", "RETEST", "ENTRY", "SL",
           "TP1", "TP2", "RR", "SCORE", "STATUS"]


def _p(x) -> str:
    if x is None:
        return "—"
    return f"{x:.5g}" if abs(x) < 1000 else f"{x:,.0f}"


def _trend_ret(r) -> str:
    if r is None:
        return "—"
    arrow = "▲" if r > 1 else "▼" if r < -1 else "►"
    return f"{arrow}{r:+.1f}%"


def row(a) -> list[str]:
    s = a.scan
    st, imp, corr, tl, piv, ret, der, risk = (a.structure, a.impulse, a.correction, a.trendlines,
                                               a.pivot, a.retest, a.derivatives, a.risk)
    rs = "—" if s.rs_7d is None else f"{s.rs_4h:+.1f}/{s.rs_3d:+.1f}/{s.rs_7d:+.1f}"
    pivot = "—"
    if piv is not None and piv.pivot_detected:
        pivot = f"{piv.pivot_timeframe} {piv.confirmation_count}/5"
    elif piv is not None and piv.false_breakout:
        pivot = "FAILED"
    ready = a.status == Status.LONG_READY or a.status in (Status.ACTIVE_POSITION, Status.MANAGEMENT)
    return [
        a.symbol,
        _p(a.price),
        st.trend_4h if st else "—",
        _trend_ret(s.return_3d),
        _trend_ret(s.return_7d),
        rs,
        f"{s.volume_score:.0f}",
        "—" if der is None or der.funding is None else f"{der.funding:+.3f}%",
        "—" if der is None or der.oi_change is None else f"{der.oi_change:+.1f}%",
        "—" if imp is None or not imp.found else f"{imp.impulse_atr:.1f}xATR",
        "—" if corr is None or corr.correction_depth is None else f"{corr.correction_depth:.0f}%",
        _p(tl.correction_line_current) if tl else "—",
        "—" if tl is None or tl.distance_to_correction_line_pct is None else f"{tl.distance_to_correction_line_pct:+.1f}%",
        pivot,
        "—" if ret is None or ret.status == "NO_RETEST" else ret.status.replace("RETEST_", ""),
        _p(risk.entry) if ready and risk else (_p(a.entry.trigger_level) + "*" if a.entry and a.entry.trigger_level else "—"),
        _p(risk.sl) if risk else "—",
        _p(risk.tp1) if risk else "—",
        _p(risk.tp2) if risk else "—",
        "—" if risk is None or risk.rr is None else f"{risk.rr:.1f}",
        "—" if a.score is None else f"{a.score.pivot_score:.0f}",
        a.display_status,
    ]


def render_table(analyses, color: bool = True) -> str:
    rows = [row(a) for a in analyses]
    widths = [max(len(h), *(len(r[i]) for r in rows)) if rows else len(h) for i, h in enumerate(COLUMNS)]
    sep = "  "
    lines = [sep.join(h.ljust(w) for h, w in zip(COLUMNS, widths)),
             sep.join("─" * w for w in widths)]
    for a, r in zip(analyses, rows):
        line = sep.join(c.ljust(w) for c, w in zip(r, widths))
        if color:
            ansi = STATUS_COLORS.get(a.status, ("", "", ""))[1]
            line = f"{ansi}{line}{ANSI_RESET}"
        lines.append(line)
    return "\n".join(lines)


def render_detail(a, color: bool = True) -> str:
    name, ansi, _ = STATUS_COLORS.get(a.status, ("", "", ""))
    c = (lambda t: f"{ansi}{t}{ANSI_RESET}") if color else (lambda t: t)
    out = [c(f"■ {a.symbol}  {a.display_status}  ({name})"
             + (f"  score {a.score.pivot_score:.1f} [{a.score.label}]" if a.score else ""))]
    for r in a.reasons:
        out.append(f"   · {r}")
    if a.final_rule:
        out.append("   final rule: " + "  ".join(f"{k}={'✓' if v else '✗'}" for k, v in a.final_rule.items()))
    if a.critic and a.critic.objections:
        for o in a.critic.objections:
            out.append(f"   critic [{o['severity']}] {o['code']}: {o['finding']}")
    if a.validation and a.validation.failures:
        out.append("   validation: " + "; ".join(f"{k}: {v}" for k, v in a.validation.failures.items()))
    if a.contradictions:
        out.append("   contradictions: " + "; ".join(a.contradictions))
    return "\n".join(out)


def legend(color: bool = True) -> str:
    items = []
    for st in (Status.SCANNING, Status.TREND_LEADER, Status.CORRECTION, Status.PIVOT_DETECTED,
               Status.RETEST_CONFIRMED, Status.LONG_READY, Status.INVALIDATED, Status.EXTENDED):
        name, ansi, _ = STATUS_COLORS[st]
        items.append(f"{ansi}{name} {st}{ANSI_RESET}" if color else f"{name}={st}")
    return "  ".join(items) + "\n* = trigger level (entry not active yet)"
