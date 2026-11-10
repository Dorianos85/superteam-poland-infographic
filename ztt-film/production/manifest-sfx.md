# MANIFEST SFX — ZTT: LICENCJA NA ZYSK (foley / ambience)

Źródło: `05-muzyka-sfx.md`, sekcja 3 (tabela 10 scen). Prompty EN wklejone 1:1.
Data: 2026-11-07. Narzędzie: ElevenLabs → Sound Effects, model **v3**.
Muzyka i ALERT_ZTT — poza zakresem (inny agent).

## Gdzie to leży
- **Sound Effects → Ulubione** (`elevenlabs.io/app/sound-effects/favorites`) — tam jest **24 wybranych take'ów ★** (każdy ★ oznaczony gwiazdką w historii).
- **Sound Effects → Historia** (`/app/sound-effects/history`) — wszystkie generacje (każda = 4 take'i #1–#4). Wyszukiwarka „Szukaj historii efektów dźwiękowych…” — szukaj po fragmencie prompta.
- **Zasoby (menu boczne) — SFX NIE pojawiają się tam automatycznie** (wyszukiwanie „underwater” w Zasobach: „Nie znaleziono plików ani folderów”). W wierszu take'a są tylko: Odtwórz / Użyj podpowiedzi / Pobierz (menu) / Gwiazdka — brak opcji „dodaj do Zasobów”. Montażysta: brać z Ulubionych SFX (lub pobrać ★ i wgrać do Studio). Nic nie było pobierane na dysk.

## Ustawienia
- Auto-poprawianie promptu: **Wyłączone** (prompt 1:1).
- Ambienty: **30.0 s (max)**, **Pętla: włączona**, prompt influence 30%.
- Półambienty: HUD 10 s pętla / 30%; heartbeat 8 s bez pętli / 30%.
- One-shoty: pętla wyłączona, **prompt influence 80%**, długość pod zdarzenie.
- Każda generacja daje 4 take'i. Koszt wg UI: 30 s = 400 kr., 10 s = 132, 8 s = 108, 7 s = 92, 5 s = 68, 1.5 s ≈ 24.
- **Koszt łączny: ok. 5 400 kredytów** (budżet 200 000). Saldo konta w trakcie: ~4,54 mln.

## Lista (★ = wybrany take, ID = data-testid `sfx-play-<ID>` w Ulubionych)

| Nazwa robocza | Prompt (początek) | Dł. | Pętla | ★ | ID ★ | Alt | Uwagi (waveform w UI) |
|---|---|---|---|---|---|---|---|
| SFX_01_heartbeat | Slow tense heartbeat mixed with a ticking clock… | 8.0s | nie | #2 | C65Nj36VnpHihKkhCK4K | #4 | narasta do końca (tail > head) — pasuje do „building” |
| SFX_01_ripple | Smooth digital ripple whoosh, glassy energy wave… | 2.5s | nie | #1 | IjXHn6ynP7uKcmmSE7Wu | #4 | narasta do środka, czyste wygaszenie, bez przerw |
| SFX_02_underwater | Deep underwater ambience, muffled low rumble… | 30s | tak | #1 | BRo2j1pRoFGEwpYn828k | #4 | równy poziom, start≈koniec (szew pętli) |
| SFX_02_harbor | Night harbor ambience, gentle waves… zipper being unzipped | 30s | tak | #4 | TYHyqw26NsZhgfTJzNeC | #2 | najrówniejszy bed z wydarzeniami |
| SFX_02_zipper (one-shot) | (ten sam prompt harbor) | 5.0s | nie | #4 | ZCKZtI7VtY1nWejtMzrL | #1 | wersja krótka, influence 80% — wyraźne zdarzenie w 2. połowie |
| SFX_03_yacht | Luxury yacht deck ambience at sunset… | 30s | tak | #3 | gUf6u4LWZnq1rWr0FEG2 | #2 | najrówniejszy, start≈koniec |
| SFX_03_phone_buzz | Phone vibrating once on a glass table, short buzz | 1.5s | nie | #1 | E8Iji3o6TcOjrJR65BXp | #4 | wygasa do ciszy (#3 ucięty na końcu — odrzucić) |
| SFX_04_lake | Calm misty lake at dawn, sparse birdsong… | 30s | tak | #4 | maoVCbsf7l9DTeu2C0hc | #3 | start=koniec, umiarkowany poziom |
| SFX_04_float_splash | Fishing float splash, sharp rod whip swish… | 2.9s | nie | #4 | tuDolNXzVJpzjLuzLv9q | — | jedyny z pełną treścią; #1–#3 prawie cisza |
| SFX_05_server | Server room hum, low electronic ambience… | 30s | tak | #3 | aI8pWjKBDHXcCek1gMXa | #4 | bardzo stabilny hum |
| SFX_05_shield_hit | Holographic interface glitch impact, energy shield… | 2.5s | nie | #3 | sOcr6AFkvGmkz1M01m1l | #4 | uderzenie na starcie, czysty ogon |
| SFX_05_briefcase | Aluminum briefcase latches clicking open… | 2.9s | nie | #1 | WG8gqHenuiqjEMcRCr2G | #3 | czyste zakończenie; #3 dłuższe „unfolding” |
| SFX_06_downshift | Classic grand tourer V12 engine on winding road… | 5.0s | nie | #3 | eAlOHuQhIbeNZr8aj8mg | #1 | najmocniejszy, ciągły, bez dziur |
| SFX_06_hud_hum | Soft futuristic HUD projection hum, subtle interface whir | 10s | tak | #1 | D57izEomMfl7ZGqvHEti | #3 | najrówniejszy z 4 |
| SFX_07_roulette | Roulette ball spinning and rattling into pocket… | 5.0s | nie | #3 | uiMA0DpgJ2Y5iSPCX9vW | #4 | startuje w ruchu, cichnie na końcu |
| SFX_07_casino | Elegant casino ambience, quiet murmur, poker chips… | 30s | tak | #1 | 0PZN3jEXcfazZXTTYFbB | #2 | najrówniejszy bed |
| SFX_07_chips (one-shot) | (ten sam prompt casino) | 4.0s | nie | #1 | 7joXVPC8I6rxUghICbSH | #4 | krótka wersja, influence 80% |
| SFX_08_trading_floor | Modern trading floor ambience, mechanical keyboards… | 30s | tak | #2 | C1lJFDccbjzfR9aguph3 | #1 | #3 prawie cichy — odrzucić; #4 gaśnie na końcu |
| SFX_08_monitor_swivel | Computer monitor being swiveled on its stand… | 1.5s | nie | #2 | FX0pVpwbces6ToxApeOa | — | jedyny z treścią; #1/#3/#4 głównie cisza |
| SFX_09_hall | Large conference hall crowd murmur, spacious reverb… | 30s | tak | #4 | zME6bCnAAlc6RYwSAavD | #3 | z 2. generacji (najnowsza w historii) |
| SFX_09_notifications | Hundreds of phone notifications going off in a crowd… | 5.0s | nie | #1 | 6SRq69uy31QhXnnfGZ7l | #2 | pod ALERT_ZTT; gęsto na starcie, wygasa |
| SFX_09_crowd_swell | Crowd murmur swelling into excited chatter and gasps | 7.0s | nie | #1 | MFfgdycfLOTfMyFRUN39 | #3 | UWAGA: we wszystkich take'ach szczyt wcześnie (~1 s) — „swell” zrobić fade-inem w montażu lub dogenerować |
| SFX_10_rooftop | Rooftop wind at night, distant city traffic hum… | 30s | tak | #4 | oSJgeqzWqZuunK3OokFM | #3 | bardzo równy, start=koniec |
| SFX_10_logo_shimmer | Magical digital shimmer, city lights assembling into a logo… | 5.0s | nie | #2 | dkCcTH32ANLsCLSdL2Cg | #1 | cichy start → build → cisza na końcu |

Nazwa pliku przy eksporcie: `SFX_<scena>_<slug>_t<take>.wav`, np. `SFX_06_downshift_t3.wav`.

## Anomalie
- **Large conference hall — 1. generacja** (starsza, ~13 min przed końcem sesji) nie ma waveformu w UI (prawdopodobnie wadliwa) → wygenerowano ponownie; ★ z nowej.
- **Rooftop wind** — wygenerowany 2× (podwójne kliknięcie przy zawieszeniu przeglądarki); ★ z górnej (nowszej) grupy, drugą ignorować.
- Pierwsza próba „Hundreds of phone notifications” nie zapisała się w historii (reload strony) → wygenerowana ponownie.
- Strona SFX samoczynnie przeładowywała się kilka razy w tle — bez wpływu na wyniki.
- Pod promptem widnieje informacja „Generacje mogą być udostępnione na stronie Explore … Wyłącz” — NIE ruszałem (ustawienie konta); do decyzji Doriana.
- Wybór ★ oparty na długości i kształcie waveformu w UI (poziom, równość, szew pętli, ogon) — **bez odsłuchu**. Przed montażem odsłuchać ★ i alt.
