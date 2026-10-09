"""Core data types shared by all agents."""
from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from typing import Any

INTERVAL_MS = {
    "15m": 15 * 60_000,
    "1h": 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "1d": 24 * 60 * 60_000,
}
HOUR_MS = INTERVAL_MS["1h"]


@dataclass(slots=True)
class Candle:
    t: int  # open time, ms
    o: float
    h: float
    l: float
    c: float
    v: float  # base volume
    buy_v: float = 0.0  # taker buy base volume
    interval_ms: int = HOUR_MS

    @property
    def close_time(self) -> int:
        return self.t + self.interval_ms

    @property
    def body_top(self) -> float:
        return max(self.o, self.c)

    @property
    def body_bottom(self) -> float:
        return min(self.o, self.c)


@dataclass(slots=True)
class Swing:
    idx: int
    t: int  # open time of the swing candle
    price: float
    kind: str  # "H" or "L"
    label: str = ""  # HH / LH / HL / LL

    @property
    def mid_time(self) -> int:
        return self.t


@dataclass(slots=True)
class Line:
    """Straight line in (time ms, price) space."""

    t1: int
    p1: float
    t2: int
    p2: float

    @property
    def slope_per_hour(self) -> float:
        if self.t2 == self.t1:
            return 0.0
        return (self.p2 - self.p1) / ((self.t2 - self.t1) / HOUR_MS)

    def value(self, t: int) -> float:
        if self.t2 == self.t1:
            return self.p1
        return self.p1 + (self.p2 - self.p1) * (t - self.t1) / (self.t2 - self.t1)

    def to_dict(self) -> dict:
        return {"t1": self.t1, "p1": self.p1, "t2": self.t2, "p2": self.p2,
                "slope_per_hour": self.slope_per_hour}


class Status:
    SCANNING = "SCANNING"
    TREND_LEADER = "TREND_LEADER"
    IMPULSE = "IMPULSE"
    CORRECTION = "CORRECTION"
    PIVOT_DETECTED = "PIVOT_DETECTED"
    PIVOT_CONFIRMED = "PIVOT_CONFIRMED"
    RETEST_WAIT = "RETEST_WAIT"
    RETEST_CONFIRMED = "RETEST_CONFIRMED"
    LONG_READY = "LONG_READY"
    ACTIVE_POSITION = "ACTIVE_POSITION"
    MANAGEMENT = "MANAGEMENT"
    EXIT = "EXIT"
    INVALIDATED = "INVALIDATED"
    EXTENDED = "EXTENDED"
    NO_TRADE = "NO_TRADE"

    # Order in the state machine (used to find "furthest state reached").
    ORDER = [SCANNING, TREND_LEADER, IMPULSE, CORRECTION, PIVOT_DETECTED,
             PIVOT_CONFIRMED, RETEST_WAIT, RETEST_CONFIRMED, LONG_READY,
             ACTIVE_POSITION, MANAGEMENT, EXIT]


# Status colours (name, ANSI escape, hex) — see spec "KOLORY STATUSÓW".
STATUS_COLORS: dict[str, tuple[str, str, str]] = {
    Status.SCANNING: ("GRAY", "\033[90m", "#8b8f98"),
    Status.TREND_LEADER: ("BLUE", "\033[94m", "#3b82f6"),
    Status.IMPULSE: ("BLUE", "\033[94m", "#3b82f6"),
    Status.CORRECTION: ("YELLOW", "\033[93m", "#eab308"),
    Status.PIVOT_DETECTED: ("ORANGE", "\033[38;5;208m", "#f97316"),
    Status.PIVOT_CONFIRMED: ("ORANGE", "\033[38;5;214m", "#fb923c"),
    Status.RETEST_WAIT: ("ORANGE", "\033[38;5;214m", "#fbbf24"),
    Status.RETEST_CONFIRMED: ("LIGHT GREEN", "\033[38;5;120m", "#86efac"),
    Status.LONG_READY: ("GREEN", "\033[92m", "#22c55e"),
    Status.ACTIVE_POSITION: ("GREEN", "\033[92m", "#16a34a"),
    Status.MANAGEMENT: ("GREEN", "\033[92m", "#15803d"),
    Status.EXIT: ("GRAY", "\033[90m", "#6b7280"),
    Status.INVALIDATED: ("RED", "\033[91m", "#ef4444"),
    Status.EXTENDED: ("PURPLE", "\033[95m", "#a855f7"),
    Status.NO_TRADE: ("RED", "\033[31m", "#b91c1c"),
}
ANSI_RESET = "\033[0m"


def score_label(score: float, cfg) -> str:
    th = cfg.scoring
    if score >= th.a_plus:
        return "A+ SETUP"
    if score >= th.long_ready:
        return "LONG_READY"
    if score >= th.retest_wait:
        return "RETEST_WAIT"
    if score >= th.watch:
        return "WATCH"
    return "IGNORE"


def to_jsonable(obj: Any) -> Any:
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if is_dataclass(obj):
        return {k: to_jsonable(v) for k, v in asdict(obj).items()}
    if isinstance(obj, dict):
        return {k: to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, float):
        return round(obj, 10)
    return obj


class JsonMixin:
    """Mixin for agent result dataclasses."""

    def to_dict(self) -> dict:
        return {k: to_jsonable(v) for k, v in self.__dict__.items()}
