"""All thresholds and weights of the Pivot Engine.

The Self-Improvement agent may only *propose* changes to these values
(SYSTEM_OPTIMIZATION_PROPOSAL); it never writes them. A human applies a
proposal by putting the new value in a JSON override file passed with
``--config``.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, fields, is_dataclass


@dataclass
class ScannerCfg:
    quote_asset: str = "USDT"
    min_quote_volume_24h: float = 20_000_000.0
    max_spread_pct: float = 0.15
    max_symbols: int = 120  # most liquid symbols analysed per scan
    require_rs_4h: bool = False  # RS_4H > 0 is preferred, not required
    unusual_volume_mult: float = 2.0  # 24h vol vs 7d avg daily vol


@dataclass
class StructureCfg:
    swing_1d: int = 2
    swing_4h: int = 4  # major 4H swings for the trend
    swing_1h: int = 3
    swing_15m: int = 2


@dataclass
class ImpulseCfg:
    swing_4h: int = 3
    atr_period: int = 14
    min_atr_mult: float = 1.5
    preferred_atr_mult: float = 2.0
    structure_lookback_bars: int = 60  # impulse high must exceed swing highs of the last N 4H bars


@dataclass
class CorrectionCfg:
    swing_1h: int = 3
    min_lower_highs: int = 2
    preferred_lower_highs: int = 3
    min_depth_pct: float = 15.0
    max_depth_pct: float = 78.6
    ideal_depth_low: float = 30.0
    ideal_depth_high: float = 61.8


@dataclass
class TrendlineCfg:
    touch_tol_atr: float = 0.35  # touch tolerance as a fraction of ATR
    min_touches: int = 2
    preferred_touches: int = 3
    max_swing_lows: int = 8
    broken_tol_atr_4h: float = 0.5


@dataclass
class PivotCfg:
    preferred_tf: str = "4h"
    aggressive: bool = True  # allow 1H crosses
    max_bars_since_pivot_1h: int = 72
    hold_bars_1h: int = 2
    false_break_tol_atr: float = 0.25
    min_confirmations: int = 3  # of 5


@dataclass
class VolumeCfg:
    avg_period: int = 20
    desired_mult: float = 1.2
    strong_mult: float = 1.5


@dataclass
class DerivativesCfg:
    funding_long_crowded_pct: float = 0.10
    funding_short_crowded_pct: float = -0.10
    oi_window_h: int = 24
    oi_extreme_pct: float = 25.0
    flat_pct: float = 0.5


@dataclass
class RetestCfg:
    zone_below_atr: float = 0.3
    zone_above_atr: float = 0.6
    local_high_max_atr: float = 1.0  # include broken LH in zone if this close


@dataclass
class EntryCfg:
    aggressive_min_score: float = 80.0
    aggressive_min_confirmations: int = 4
    aggressive_max_bars_since_pivot: int = 6


@dataclass
class RiskCfg:
    min_rr: float = 2.0
    rr_target: str = "TP1"  # RR measured to TP1 (conservative)
    sl_buffer_atr: float = 0.1
    min_sl_atr: float = 0.5  # SL closer than this (ATR_1H) is noise
    tp1_partial: float = 0.5  # fraction closed at TP1 (journal R calc)
    max_hold_bars_1h: int = 120


@dataclass
class ExtensionCfg:
    max_return_24h_pct: float = 30.0
    max_dist_atr_4h: float = 2.5


@dataclass
class ScoringCfg:
    w_rs: float = 20
    w_trend: float = 15
    w_impulse: float = 10
    w_correction: float = 10
    w_line_break: float = 15
    w_volume: float = 10
    w_derivatives: float = 5
    w_retest: float = 10
    w_rr: float = 5
    rs_target_4h: float = 2.0
    rs_target_3d: float = 8.0
    rs_target_7d: float = 12.0
    a_plus: float = 90
    long_ready: float = 80
    retest_wait: float = 70
    watch: float = 60


@dataclass
class CriticCfg:
    max_major_objections: int = 2
    one_candle_rs_share: float = 0.7
    supply_within_r: float = 1.0
    min_correction_depth_pct: float = 15.0


@dataclass
class ValidationCfg:
    min_candles_1h: int = 200
    min_candles_4h: int = 120
    max_data_age_bars: int = 2
    duplicate_cooldown_h: int = 24


@dataclass
class SelfImprovementCfg:
    min_samples: int = 30
    min_bucket: int = 15
    min_expectancy_gain_r: float = 0.05


@dataclass
class Config:
    scanner: ScannerCfg = field(default_factory=ScannerCfg)
    structure: StructureCfg = field(default_factory=StructureCfg)
    impulse: ImpulseCfg = field(default_factory=ImpulseCfg)
    correction: CorrectionCfg = field(default_factory=CorrectionCfg)
    trendline: TrendlineCfg = field(default_factory=TrendlineCfg)
    pivot: PivotCfg = field(default_factory=PivotCfg)
    volume: VolumeCfg = field(default_factory=VolumeCfg)
    derivatives: DerivativesCfg = field(default_factory=DerivativesCfg)
    retest: RetestCfg = field(default_factory=RetestCfg)
    entry: EntryCfg = field(default_factory=EntryCfg)
    risk: RiskCfg = field(default_factory=RiskCfg)
    extension: ExtensionCfg = field(default_factory=ExtensionCfg)
    scoring: ScoringCfg = field(default_factory=ScoringCfg)
    critic: CriticCfg = field(default_factory=CriticCfg)
    validation: ValidationCfg = field(default_factory=ValidationCfg)
    self_improvement: SelfImprovementCfg = field(default_factory=SelfImprovementCfg)
    # Macro events: [{"time": "2026-10-10T12:30:00Z", "name": "US CPI"}]
    macro_events: list = field(default_factory=list)
    macro_window_h: int = 12

    def to_dict(self) -> dict:
        return asdict(self)

    def get(self, path: str):
        obj = self
        for part in path.split("."):
            obj = getattr(obj, part)
        return obj

    def with_value(self, path: str, value) -> "Config":
        """Return a copy with one dotted-path value replaced (used for what-if tests)."""
        new = Config.from_dict(self.to_dict())
        *head, last = path.split(".")
        obj = new
        for part in head:
            obj = getattr(obj, part)
        setattr(obj, last, value)
        return new

    @classmethod
    def from_dict(cls, data: dict) -> "Config":
        return _build(cls, data)

    @classmethod
    def load(cls, path: str | None) -> "Config":
        if not path:
            return cls()
        with open(path, encoding="utf-8") as fh:
            return cls.from_dict(json.load(fh))


def _build(dc_type, data: dict):
    kwargs = {}
    for f in fields(dc_type):
        if f.name not in data:
            continue
        value = data[f.name]
        default = f.default_factory() if callable(f.default_factory) else f.default  # type: ignore[misc]
        if is_dataclass(default) and isinstance(value, dict):
            kwargs[f.name] = _build(type(default), value)
        else:
            kwargs[f.name] = value
    return dc_type(**kwargs)
