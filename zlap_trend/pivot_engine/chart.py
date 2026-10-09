"""WYKRES: self-contained SVG/HTML charts of each setup (no external libraries)."""
from __future__ import annotations

import html
from datetime import datetime, timezone

from .models import HOUR_MS, STATUS_COLORS, Status
from .terminal import COLUMNS, row

W, H = 1040, 460
PAD_L, PAD_R, PAD_T, PAD_B = 8, 118, 30, 26


def _fmt(x: float) -> str:
    return f"{x:.5g}" if abs(x) < 1000 else f"{x:,.0f}"


def _ts(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def svg_chart(a) -> str:
    c1h = a.candles.get("1h") or []
    if not c1h:
        return ""
    imp, corr, tl, piv, ret, risk = a.impulse, a.correction, a.trendlines, a.pivot, a.retest, a.risk
    start_t = c1h[-1].t - 220 * HOUR_MS
    if imp is not None and imp.found:
        start_t = min(start_t, imp.impulse_low_t - 36 * HOUR_MS)
    view = [c for c in c1h if c.t >= max(start_t, c1h[-1].t - 480 * HOUR_MS)]
    t0, t1 = view[0].t, view[-1].close_time + 14 * HOUR_MS
    lo, hi = min(c.l for c in view), max(c.h for c in view)
    span = hi - lo
    levels = []
    if risk is not None and risk.sl is not None:
        for name, val, cls in (("ENTRY", risk.entry, "lv-entry"), ("SL", risk.sl, "lv-sl"),
                               ("TP1", risk.tp1, "lv-tp"), ("TP2", risk.tp2, "lv-tp2")):
            if val is not None and lo - 0.6 * span <= val <= hi + 0.6 * span:
                levels.append((name, val, cls))
                lo, hi = min(lo, val), max(hi, val)
    pad = (hi - lo) * 0.06
    lo, hi = lo - pad, hi + pad
    pw, ph = W - PAD_L - PAD_R, H - PAD_T - PAD_B

    def X(t):
        return PAD_L + (t - t0) / (t1 - t0) * pw

    def Y(p):
        return PAD_T + (hi - p) / (hi - lo) * ph

    out = [f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="{html.escape(a.symbol)} setup chart">']
    # grid
    for k in range(6):
        p = lo + (hi - lo) * k / 5
        out.append(f'<line x1="{PAD_L}" x2="{W - PAD_R}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" class="grid"/>'
                   f'<text x="{W - PAD_R + 6}" y="{Y(p) + 4:.1f}" class="axis">{_fmt(p)}</text>')
    # zones
    if risk is not None and risk.demand_zone and corr and corr.correction_low_t:
        zl, zh = risk.demand_zone
        x0 = X(max(t0, corr.correction_low_t))
        out.append(f'<rect x="{x0:.1f}" y="{Y(zh):.1f}" width="{W - PAD_R - x0:.1f}" '
                   f'height="{max(2, Y(zl) - Y(zh)):.1f}" class="zone-demand"/>'
                   f'<text x="{x0 + 4:.1f}" y="{Y(zl) + 12:.1f}" class="lbl demand">DEMAND</text>')
    if risk is not None and risk.supply_4h:
        zl, zh = risk.supply_4h
        if zl < hi:
            yt, yb = Y(min(zh, hi)), Y(zl)
            out.append(f'<rect x="{PAD_L}" y="{yt:.1f}" width="{pw:.1f}" height="{max(2, yb - yt):.1f}" '
                       f'class="zone-supply"/><text x="{PAD_L + 4}" y="{yt + 12:.1f}" class="lbl supply">4H SUPPLY</text>')
    if ret is not None and ret.zone_low is not None and piv is not None and piv.pivot_t:
        x0 = X(max(t0, piv.pivot_t))
        out.append(f'<rect x="{x0:.1f}" y="{Y(ret.zone_high):.1f}" width="{W - PAD_R - x0:.1f}" '
                   f'height="{max(2, Y(ret.zone_low) - Y(ret.zone_high)):.1f}" class="zone-retest"/>')
    # candles
    cw = max(1.5, pw / ((t1 - t0) / HOUR_MS) * 0.66)
    for c in view:
        x = X(c.t + HOUR_MS // 2)
        cls = "up" if c.c >= c.o else "dn"
        top, bot = Y(max(c.o, c.c)), Y(min(c.o, c.c))
        out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{Y(c.h):.1f}" y2="{Y(c.l):.1f}" class="wick {cls}"/>'
                   f'<rect x="{x - cw / 2:.1f}" y="{top:.1f}" width="{cw:.1f}" height="{max(0.8, bot - top):.1f}" class="body {cls}"/>')
    # lines
    end_t = view[-1].close_time + 10 * HOUR_MS
    if tl is not None and tl.trend_line is not None:
        ln = tl.trend_line
        ts = max(t0, ln.t1)
        out.append(f'<line x1="{X(ts):.1f}" y1="{Y(ln.value(ts)):.1f}" x2="{X(end_t):.1f}" y2="{Y(ln.value(end_t)):.1f}" '
                   f'class="trendline"/><text x="{X(end_t) - 70:.1f}" y="{Y(ln.value(end_t)) + 14:.1f}" class="lbl tl">TREND LINE</text>')
    if tl is not None and tl.correction_line is not None:
        ln = tl.correction_line
        ts = max(t0, ln.t1)
        out.append(f'<line x1="{X(ts):.1f}" y1="{Y(ln.value(ts)):.1f}" x2="{X(end_t):.1f}" y2="{Y(ln.value(end_t)):.1f}" '
                   f'class="corrline"/><text x="{X(end_t) - 96:.1f}" y="{Y(ln.value(end_t)) - 6:.1f}" class="lbl cl">CORRECTION LINE</text>')
        for n, s in enumerate(tl.correction_line_anchors, 1):
            if s.t >= t0:
                out.append(f'<circle cx="{X(s.t + HOUR_MS // 2):.1f}" cy="{Y(s.price):.1f}" r="3.5" class="anchor"/>'
                           f'<text x="{X(s.t + HOUR_MS // 2) - 8:.1f}" y="{Y(s.price) - 8:.1f}" class="lbl cl">LH{n}</text>')
    # markers
    def marker(t, price, label, cls, below=False):
        x, y = X(t + HOUR_MS // 2), Y(price)
        if below:
            out.append(f'<path d="M{x:.1f},{y + 4:.1f} l-6,10 h12 z" class="mk {cls}"/>'
                       f'<text x="{x:.1f}" y="{y + 27:.1f}" class="lbl {cls}" text-anchor="middle">{label}</text>')
        else:
            out.append(f'<path d="M{x:.1f},{y - 4:.1f} l-6,-10 h12 z" class="mk {cls}"/>'
                       f'<text x="{x:.1f}" y="{y - 18:.1f}" class="lbl {cls}" text-anchor="middle">{label}</text>')

    if imp is not None and imp.found:
        if imp.impulse_low_t >= t0:
            low_c = min((c for c in view if imp.impulse_low_t <= c.t < imp.impulse_low_t + 4 * HOUR_MS),
                        key=lambda c: c.l, default=None)
            if low_c:
                marker(low_c.t, low_c.l, "IMPULSE LOW", "imp", below=True)
        if corr is not None and corr.impulse_high_idx_1h is not None:
            hc = c1h[corr.impulse_high_idx_1h]
            if hc.t >= t0:
                marker(hc.t, hc.h, "IMPULSE HIGH", "imp")
    if piv is not None and piv.pivot_detected:
        pc = c1h[piv.pivot_idx_1h]
        x, y = X(pc.t + HOUR_MS // 2), Y(pc.c)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" class="mk-breakout"/>'
                   f'<path d="M{x:.1f},{Y(pc.l) + 6:.1f} l7,9 l-7,9 l-7,-9 z" class="mk pivot"/>'
                   f'<text x="{x:.1f}" y="{Y(pc.l) + 36:.1f}" class="lbl pivot" text-anchor="middle">PIVOT {piv.pivot_timeframe}</text>'
                   f'<text x="{x + 9:.1f}" y="{y - 9:.1f}" class="lbl brk">BREAKOUT</text>')
    if ret is not None and ret.retest_t is not None and ret.retest_t >= t0:
        marker(ret.retest_t, ret.retest_low, "RETEST", "retest", below=True)
    # levels
    for name, val, cls in levels:
        y = Y(val)
        out.append(f'<line x1="{PAD_L}" x2="{W - PAD_R}" y1="{y:.1f}" y2="{y:.1f}" class="lv {cls}"/>'
                   f'<rect x="{W - PAD_R + 2}" y="{y - 9:.1f}" width="{PAD_R - 4}" height="18" rx="3" class="tag {cls}"/>'
                   f'<text x="{W - PAD_R + 7}" y="{y + 4:.1f}" class="tagtxt">{name} {_fmt(val)}</text>')
    out.append(f'<text x="{PAD_L + 4}" y="{H - 8}" class="axis">{_ts(view[0].t)}</text>'
               f'<text x="{W - PAD_R - 4}" y="{H - 8}" class="axis" text-anchor="end">{_ts(view[-1].close_time)} · 1H</text>')
    out.append("</svg>")
    return "".join(out)


CSS = """
:root{--bg:#0b0e14;--panel:#121722;--line:#232a38;--text:#d6dbe6;--muted:#7d8597;--up:#22c55e;--dn:#ef4444;
--entry:#60a5fa;--sl:#f87171;--tp:#4ade80;--tp2:#86efac;--cl:#f59e0b;--tl:#38bdf8;--imp:#c084fc;--retest:#a3e635;
--demand:rgba(34,197,94,.10);--supply:rgba(239,68,68,.10);--zone:rgba(245,158,11,.10)}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f6f7fb;--panel:#ffffff;--line:#e3e6ee;
--text:#151a23;--muted:#5f6878;--cl:#d97706;--tl:#0284c7;--imp:#9333ea;--retest:#65a30d}}
:root[data-theme="dark"]{--bg:#0b0e14;--panel:#121722;--line:#232a38;--text:#d6dbe6;--muted:#7d8597}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);
font:13px/1.45 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
header{padding:20px 16px 8px;max-width:1240px;margin:0 auto}h1{font-size:20px;margin:0 0 4px;letter-spacing:.04em}
.sub{color:var(--muted)}main{max-width:1240px;margin:0 auto;padding:0 16px 40px}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--panel);margin:14px 0 22px}
table{border-collapse:collapse;width:100%;white-space:nowrap}th,td{padding:6px 9px;border-bottom:1px solid var(--line);text-align:left}
th{color:var(--muted);font-weight:600;font-size:11px;position:sticky;top:0;background:var(--panel)}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-weight:700;font-size:11px;color:#0b0e14}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px;margin:0 0 18px}
.card h2{font-size:15px;margin:0 0 6px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.reasons{color:var(--muted);margin:4px 0 8px;padding-left:18px}.chart{width:100%;height:auto;display:block}
.grid{stroke:var(--line);stroke-width:1}.axis{fill:var(--muted);font-size:10px}
.wick.up{stroke:var(--up)}.wick.dn{stroke:var(--dn)}.body.up{fill:var(--up)}.body.dn{fill:var(--dn)}
.trendline{stroke:var(--tl);stroke-width:2}.corrline{stroke:var(--cl);stroke-width:2;stroke-dasharray:7 4}
.anchor{fill:var(--cl)}.lbl{font-size:10px;font-weight:700}.lbl.cl{fill:var(--cl)}.lbl.tl{fill:var(--tl)}
.mk.imp{fill:var(--imp)}.lbl.imp{fill:var(--imp)}.mk.pivot{fill:#f97316}.lbl.pivot{fill:#f97316}
.mk-breakout{fill:none;stroke:#f97316;stroke-width:2}.lbl.brk{fill:#f97316}.mk.retest{fill:var(--retest)}.lbl.retest{fill:var(--retest)}
.zone-demand{fill:var(--demand)}.zone-supply{fill:var(--supply)}.zone-retest{fill:var(--zone)}
.lbl.demand{fill:var(--up)}.lbl.supply{fill:var(--dn)}
.lv{stroke-width:1.3;stroke-dasharray:4 3}.lv-entry{stroke:var(--entry);fill:var(--entry)}.lv-sl{stroke:var(--sl);fill:var(--sl)}
.lv-tp{stroke:var(--tp);fill:var(--tp)}.lv-tp2{stroke:var(--tp2);fill:var(--tp2)}.tagtxt{fill:#0b0e14;font-size:10px;font-weight:700}
.legend{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
pre{white-space:pre-wrap;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;margin:8px 0 0}
details summary{cursor:pointer;color:var(--muted)}
"""


def _badge(status: str, label: str | None = None) -> str:
    color = STATUS_COLORS.get(status, ("", "", "#888"))[2]
    return f'<span class="badge" style="background:{color}">{html.escape(label or status)}</span>'


def render_dashboard(analyses, title: str = "ZŁAP TREND — Pivot Engine", subtitle: str = "",
                     alerts: dict | None = None) -> str:
    alerts = alerts or {}
    rows_html = []
    for a in analyses:
        cells = row(a)
        cells[-1] = _badge(a.status, a.display_status)
        rows_html.append("<tr>" + "".join(f"<td>{c if i == len(cells) - 1 else html.escape(c)}</td>"
                                          for i, c in enumerate(cells)) + "</tr>")
    legend = "".join(_badge(s, f"{STATUS_COLORS[s][0]} · {s}") for s in (
        Status.SCANNING, Status.TREND_LEADER, Status.CORRECTION, Status.PIVOT_DETECTED,
        Status.RETEST_CONFIRMED, Status.LONG_READY, Status.INVALIDATED, Status.EXTENDED))
    cards = []
    for a in analyses:
        if a.impulse is None or not a.impulse.found:
            continue
        reasons = "".join(f"<li>{html.escape(r)}</li>" for r in a.reasons)
        crit = ""
        if a.critic and a.critic.objections:
            crit = "<details><summary>Setup Critic</summary><ul class='reasons'>" + "".join(
                f"<li>[{o['severity']}] {html.escape(o['question'])} — {html.escape(o['finding'])}</li>"
                for o in a.critic.objections) + "</ul></details>"
        alert = alerts.get(a.symbol)
        alert_html = f"<details open><summary>Alert</summary><pre>{html.escape(alert)}</pre></details>" if alert else ""
        score = f" · PIVOT SCORE {a.score.pivot_score:.0f}/100 ({a.score.label})" if a.score else ""
        cards.append(f'<section class="card"><h2>{html.escape(a.symbol)} {_badge(a.status, a.display_status)}'
                     f'<span class="sub">{score}</span></h2><ul class="reasons">{reasons}</ul>'
                     f'{svg_chart(a)}{crit}{alert_html}</section>')
    head = "".join(f"<th>{html.escape(h)}</th>" for h in COLUMNS)
    return (f"<!doctype html><html lang='pl'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'><title>ZŁAP TREND Pivot Engine</title>"
            f"<style>{CSS}</style></head><body><header><h1>🎯 {html.escape(title)}</h1>"
            f"<div class='sub'>{html.escape(subtitle)}</div><div class='legend'>{legend}</div></header><main>"
            f"<div class='tablewrap'><table><thead><tr>{head}</tr></thead><tbody>{''.join(rows_html)}</tbody></table></div>"
            f"{''.join(cards)}</main></body></html>")
