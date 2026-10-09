# 🎯 ZŁAP TREND — Multi-Agent PIVOT ENGINE

Autonomiczny moduł terminala ZŁAP TREND, który skanuje rynek futures, szuka coinów
silniejszych od BTC i prowadzi każdy z nich przez maszynę stanów:

```
SCANNING → TREND_LEADER → IMPULSE → CORRECTION → PIVOT_DETECTED → PIVOT_CONFIRMED
→ RETEST_WAIT → RETEST_CONFIRMED → LONG_READY → ACTIVE_POSITION → MANAGEMENT → EXIT
(ANY STATE → INVALIDATED)       (+ EXTENDED → WAIT_FOR_RETEST, NO_TRADE gdy RR < 2)
```

> **Przecięcie linii korekty = tylko `PIVOT_DETECTED`.** `LONG_READY` wymaga
> spełnienia całej FINAL LONG RULE, akceptacji krytyka i walidacji.
> Nigdy: *GREEN CANDLE = LONG*. Nigdy: *BREAK LINE = AUTOMATIC BUY*.

Czysty Python 3.10+, **zero zależności** (stdlib: `urllib`, `sqlite3`). Wykresy to
samodzielne SVG/HTML.

## Szybki start

```bash
cd zlap_trend

# Demo offline (deterministyczny rynek syntetyczny) + dashboard z wykresami
python -m pivot_engine scan --provider synthetic --html dashboard.html

# Live: Binance USDⓈ-M Futures (publiczne API, bez klucza)
python -m pivot_engine scan --html dashboard.html --alerts-file alerts.log
python -m pivot_engine watch --interval 15 --telegram     # pętla co 15 min + alerty

# Pełny raport wszystkich agentów dla jednego coina (JSON)
python -m pivot_engine detail PYTHUSDT --provider synthetic

# Walk-forward backtest → dziennik → propozycje optymalizacji
python -m pivot_engine backtest --provider synthetic-history --n-symbols 40 --history-days 180
python -m pivot_engine backtest --provider binance --symbols PYTHUSDT JUPUSDT --days 45
python -m pivot_engine optimize          # → SYSTEM_OPTIMIZATION_PROPOSAL.json
python -m pivot_engine journal

# Testy
python -m unittest discover -s tests
```

Alerty Telegram: zmienne `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`; webhook: `--webhook URL`.
Market cap (Binance go nie podaje): `--mcap-file caps.json` (`{"PYTHUSDT": 1.2e9}`).

## Architektura (16 agentów + Self-Improvement)

Żaden agent nie generuje sygnału samodzielnie — decyzję podejmuje **PIVOT ORCHESTRATOR**.

| # | Agent | Plik | Co robi |
|---|-------|------|---------|
| 1 | Market Scanner | `agents/scanner.py` | universe futures, płynność, spread, Return 4H/24H/3D/7D, **RS vs BTC**, volume score, momentum rank, unusual movers. `TREND_LEADER` gdy RS_3D > 0 i RS_7D > 0 |
| 2 | Trend Structure | `agents/structure.py` | 1D/4H/1H/15M: swingi, HH/HL/LH/LL, **BOS / CHoCH** (chronione minima – drobne korekty nie łamią trendu) |
| 3 | Impulse Detector | `agents/impulse.py` | ostatni pełny impuls 4H; High ponad strukturą, ruch ≥ 1.5×ATR_4H (pref. 2×), wolumen, czas |
| 4 | Correction Detector | `agents/correction.py` | lower highs po ImpulseHigh (≥2, pref. 3), głębokość %, czas, ATR, wolumen; ważna dopóki CorrectionLow > ImpulseLow |
| 5 | Trendline Engine | `agents/trendline.py` | linia trendu (4H swing lows, rosnące) i **linia korekty** `CorrectionLine(t)` — wybór obiektywny: żadne zamknięcie nie może przebić linii, max dotknięć, najdłuższy zasięg |
| 6 | Pivot Detector | `agents/pivot.py` | `PrevClose ≤ CL(prev) AND Close > CL(cur)`; 4H preferowany, 1H agresywny; false-breakout reset; 5 potwierdzeń |
| 7 | Volume & Momentum | `agents/volume.py` | Volume_1H vs Avg20 (1.2× / 1.5×), akceleracja, buy/sell (taker), RSI, momentum |
| 8 | Derivatives | `agents/derivatives.py` | funding (±0.10% crowding), OI, reżimy cena/OI, leverage buildup, squeeze |
| 9 | Retest | `agents/retest.py` | strefa retestu (CL, breakout, lokalny LH), `Low ≤ ZoneHigh AND Close > Zone`, defense, HL 15M/1H, trigger |
| 10 | Entry Engine | `agents/entry.py` | A AGGRESSIVE (score ≥ 80, 4/5), B STANDARD (break→retest→defense→trigger), C MOMENTUM (+break local high) |
| 11 | Risk Engine | `agents/risk.py` | SL strukturalny (15M HL / 1H swing low / correction low / 4H swing low), TP1 = ImpulseHigh, TP2 = 4H supply, TP3 = 1D supply, RR ≥ 2 |
| 12 | Extension / FOMO | `agents/extension.py` | Return_24H > 30% lub dystans od breakoutu > 2.5×ATR_4H → `EXTENDED` / `WAIT_FOR_RETEST` |
| 13 | Setup Scoring | `agents/scoring.py` | PIVOT SCORE 0–100 wg wag ze specyfikacji (RS 20, trend 15, impuls 10, korekta 10, break 15, wolumen 10, OI+funding 5, retest 10, RR 5) |
| 14 | Setup Critic | `agents/critic.py` | adwersarz: 12 pytań (rozciągnięcie, RS z jednej świecy, wolumen, OI, funding, false breakout, RR, supply, BTC, makro, korekta, tendencyjna linia) → `REJECT_SETUP` |
| 15 | Validation | `agents/validation.py` | DATA/STRUCTURE/TRENDLINE/CORRECTION/PIVOT/RR_VALID, NO_DUPLICATE_SIGNAL → `BLOCK_ALERT` |
| 16 | Pivot Orchestrator | `agents/orchestrator.py` | zbiera wyniki, wykrywa sprzeczności, **zleca ponowną analizę** (inna czułość swingów), odrzuca niespójne dane, nadaje status |
| SI | Self-Improvement | `agents/self_improvement.py` | win rate, expectancy, avg R, false breakouts, kubełki (depth, RS, volume, OI, funding, retest) → **tylko propozycje** |

Pozostałe moduły: `data/` (Binance live, syntetyczny rynek, replay), `journal.py` (SQLite:
setupy, alerty, pozycje papierowe, MFE/MAE/max_R, propozycje), `alerts.py`
(PIVOT DETECTED / LONG READY; konsola, plik, Telegram, webhook; deduplikacja),
`terminal.py` (tabela z wszystkimi kolumnami + kolory statusów), `chart.py` (wykres:
świece, impulse low/high, linia trendu, linia korekty + LH, demand/supply, breakout, pivot,
retest, entry/SL/TP1/TP2), `backtest.py` (walk-forward bez look-ahead).

### FINAL LONG RULE (orchestrator)

```
TrendLeader ∧ Trend4H=BULLISH ∧ CorrectionDetected ∧ CorrectionLineValid ∧ CrossCorrectionLine
∧ PivotConfirmation ≥ 3/5 ∧ RS>0 ∧ RR ≥ 2 ∧ ¬TrendBroken ∧ ¬CriticRejected ∧ ValidationPassed
∧ EntryEngine.ready ∧ PivotScore ≥ 80                                       → LONG_READY
```

Potwierdzenia pivota (5): STRUCTURE (CHoCH/BOS 1H po linii lub HL po retescie), VOLUME,
DERIVATIVES (budowa pozycji/short covering, bez crowdingu longów), RS_4H > 0, HOLD (zamknięcia nad linią).

### Self-Improvement — zasady

Każdy setup od momentu `PIVOT_DETECTED` trafia do dziennika (także te odfiltrowane —
z listą filtrów, które je zablokowały), więc agent może zmierzyć, ile wart jest każdy filtr.
Wynik: `SYSTEM_OPTIMIZATION_PROPOSAL` z polami **OLD RULE / NEW RULE / BACKTEST RESULT /
EXPECTED IMPACT / RISK** i statusem `PENDING_HUMAN_REVIEW`. Agent **nigdy** nie zmienia
konfiguracji — wdrożenie = człowiek dopisuje `config_patch` do pliku `--config` JSON, np.:

```json
{"correction": {"max_depth_pct": 61.8}, "risk": {"min_rr": 2.5}}
```

Wszystkie progi i wagi: `pivot_engine/config.py`.

### Makro

Krytyk sprawdza nadchodzące wydarzenia z configu:
`{"macro_events": [{"time": "2026-10-15T12:30:00Z", "name": "US CPI"}], "macro_window_h": 12}`.

## Ograniczenia

* Dane syntetyczne służą do demo/testów — wyniki backtestu na nich **nie** mówią nic o
  skuteczności na realnym rynku. Rzetelną ocenę daje `backtest --provider binance`.
* Binance udostępnia historię OI tylko z ~30 dni; w starszym replayu agent derywatów
  raportuje `UNKNOWN` (neutralny wynik).
* Pozycje w dzienniku są papierowe (symulacja: SL przed TP na tej samej świecy, 50% na TP1,
  SL→BE, reszta na TP2 lub timeout). Moduł nie składa zleceń.
* To narzędzie analityczne, nie porada inwestycyjna.
