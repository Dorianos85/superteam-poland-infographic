"""ALERT SYSTEM: PIVOT DETECTED and LONG READY alerts + delivery sinks."""
from __future__ import annotations

import json
import os
import urllib.request

from .models import Status


def _p(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x:.6g}" if abs(x) < 1000 else f"{x:,.2f}"


def _pp(x: float | None) -> str:
    return "—" if x is None else f"{x:+.1f}pp"


def _ok(flag: bool) -> str:
    return "✅" if flag else "❌"


def format_pivot_alert(a) -> str:
    s = a.scan
    tl, piv = a.trendlines, a.pivot
    waiting = []
    if a.retest.status != "RETEST_CONFIRMED":
        waiting.append("RETEST")
    if not a.volume.volume_confirmation:
        waiting.append("VOLUME")
    if not piv.confirmations.get("STRUCTURE"):
        waiting.append("STRUCTURE")
    return "\n".join([
        "🟡 ZŁAP TREND — PIVOT DETECTED",
        "",
        a.symbol,
        "",
        "Trend:",
        f"4H {a.structure.trend_4h.lower()}",
        "",
        "RS vs BTC:",
        f"4H {_pp(s.rs_4h)}",
        f"3D {_pp(s.rs_3d)}",
        f"7D {_pp(s.rs_7d)}",
        "",
        "Correction line:",
        _p(piv.correction_line),
        "",
        "Breakout:",
        f"{_p(piv.breakout_price)} ({piv.pivot_timeframe})",
        "",
        "Status:",
        "PIVOT DETECTED",
        "",
        "Waiting for:",
        " / ".join(waiting or ["ENTRY TRIGGER"]),
    ])


def _funding_label(d) -> str:
    return {"LONG_CROWDED": "LONG CROWDED", "SHORT_CROWDED": "SHORT CROWDED",
            "NEUTRAL": "NEUTRAL"}.get(d.funding_state, "N/A")


def _oi_label(d) -> str:
    if d.oi_change is None:
        return "N/A"
    return "RISING" if d.oi_change > 0.5 else "FALLING" if d.oi_change < -0.5 else "FLAT"


def format_long_ready_alert(a) -> str:
    s, st, r = a.scan, a.structure, a.risk
    beaten = [tf for tf, v in (("4H", s.rs_4h), ("3D", s.rs_3d), ("7D", s.rs_7d)) if (v or 0) > 0]
    header = "🔥 ZŁAP TREND — LONG READY" + (" (A+ SETUP)" if a.score.label == "A+ SETUP" else "")
    return "\n".join([
        header, "", a.symbol, "",
        "PIVOT SCORE:", f"{a.score.pivot_score:.0f}/100", "",
        "Trend:", f"1D {_ok(st.trend_1d == 'BULLISH')}", f"4H {_ok(st.trend_4h == 'BULLISH')}", "",
        "Relative Strength:", f"BTC beaten on {' / '.join(beaten) or '—'}", "",
        "Correction:", "COMPLETE", "",
        "Pivot:", "CONFIRMED" if a.pivot.pivot_confirmed else "DETECTED", "",
        "Retest:", "CONFIRMED" if a.retest.status == "RETEST_CONFIRMED" else "NOT REQUIRED (A)", "",
        "Volume:", f"{a.volume.volume_score:.0f}/100", "",
        "Funding:", _funding_label(a.derivatives), "",
        "OI:", _oi_label(a.derivatives), "",
        "ENTRY:", f"{_p(r.entry)} ({a.entry.mode})", "",
        "SL:", f"{_p(r.sl)} ({r.sl_basis})", "",
        "TP1:", _p(r.tp1), "",
        "TP2:", _p(r.tp2), "",
        "RR:", f"{r.rr:.1f}", "",
        "STATUS:", "🔥 LONG READY",
    ])


class AlertDispatcher:
    """Decides which alerts fire (deduplicated through the journal) and delivers them."""

    def __init__(self, journal=None, sinks: list | None = None):
        self.journal = journal
        self.sinks = sinks if sinks is not None else [ConsoleSink()]

    def process(self, analyses) -> list[tuple[str, str, str]]:
        sent = []
        for a in analyses:
            if a.block_alert or not a.setup_id or a.status == Status.INVALIDATED:
                continue
            if a.status == Status.LONG_READY:
                kind, text = "LONG_READY", format_long_ready_alert(a)
            elif a.pivot is not None and a.pivot.pivot_detected and a.status in (
                    Status.PIVOT_DETECTED, Status.PIVOT_CONFIRMED, Status.RETEST_WAIT, Status.RETEST_CONFIRMED):
                kind, text = "PIVOT_DETECTED", format_pivot_alert(a)
            else:
                continue
            if self.journal is not None:
                if self.journal.alert_sent(a.setup_id, kind):
                    continue
                self.journal.add_alert(a.setup_id, a.symbol, kind, a.timestamp, text)
            for sink in self.sinks:
                sink.send(kind, text)
            sent.append((a.symbol, kind, text))
        return sent


class ConsoleSink:
    def send(self, kind: str, text: str) -> None:
        print("\n" + text + "\n" + "─" * 40)


class FileSink:
    def __init__(self, path: str = "alerts.log"):
        self.path = path

    def send(self, kind: str, text: str) -> None:
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(text + "\n" + "─" * 40 + "\n")


class TelegramSink:
    """Uses TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID environment variables."""

    def __init__(self, token: str | None = None, chat_id: str | None = None):
        self.token = token or os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or os.environ.get("TELEGRAM_CHAT_ID")

    def send(self, kind: str, text: str) -> None:
        if not (self.token and self.chat_id):
            return
        body = json.dumps({"chat_id": self.chat_id, "text": text}).encode()
        req = urllib.request.Request(f"https://api.telegram.org/bot{self.token}/sendMessage", data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=10).read()
        except Exception as exc:  # alert delivery must never crash the scan
            print(f"[telegram] delivery failed: {exc}")


class WebhookSink:
    def __init__(self, url: str):
        self.url = url

    def send(self, kind: str, text: str) -> None:
        body = json.dumps({"kind": kind, "text": text}).encode()
        req = urllib.request.Request(self.url, data=body, headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=10).read()
        except Exception as exc:
            print(f"[webhook] delivery failed: {exc}")
