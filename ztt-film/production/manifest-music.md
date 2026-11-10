# MANIFEST — MUZYKA + ALERT ZTT (sekcje 1 i 2 z pliku 05)

Data: 2026-11-07, ok. 16:07–16:35 (czas PL). Konto ElevenLabs Doriana (plan Scale).
Ocena bez odsłuchu, tylko po UI: długość, plan sekcji (composition plan) i miniatury waveform (wysokości słupków odczytane z DOM).
**Przed montażem trzeba odsłuchać ★**: sprawdzić, czy nic nie brzmi jak znany motyw szpiegowski, i czy alert jest czytelny na głośniku telefonu.
Nic nie było pobierane na dysk.

## Gdzie to leży
- Muzyka: ElevenLabs → Muzyka → **Generacje** (`/app/music/history`). Każdy wiersz to projekt. Wejście przez „Edytuj utwór” pokazuje plan sekcji i panel „Historia” z wariantami.
  ★ i zapas są oznaczone gwiazdką → filtr **Ulubione**.
- Alert: ElevenLabs → Sound Effects → **Historia** (`/app/sound-effects/history`). Wiersz = prompt, w nim take'i #1–#4. ★ są oznaczone gwiazdką → zakładka **Ulubione** (`/app/sound-effects/favorites`).
- **„Zasoby” (`/app/files`) NIE pokazuje tych generacji.** Są tam tylko foldery (awatary, flow, przesłane pliki, „Coach FI”). Wyszukanie „Midnight” nic nie zwraca.
  Montażysta weźmie pliki z historii narzędzia albo przez import w Studio. Nie sprawdzałem, czy dialog importu w Studio widzi historię Music/SFX.

## Ustawienia
- Music v2.5, czas 1:15 (Niestandardowy), tryb „Instrumentalny”, auto-poprawianie prompta WYŁĄCZONE, bez finetune'u. Prompty wklejone 1:1 z pliku 05.
- Auto-plan ElevenLabs rozpisał sekcje zgodnie z timecode'ami: Intro 6 s / Build 22 s / Rising 15 s / Casino Swagger 16 s / Crowd Swell 7 s / Final Hit / Outro.
  **Błąd planera:** dla „1:06–1:08 hit” wpisywał zwykle **Final Hit = 20 s**, więc utwór miał **1:33**. Tak wyszło w 5 z 6 wariantów pełnego prompta.
  Poprawka: w edytorze projektu ustawiłem Final Hit = 3 s i Outro = 6 s, potem regeneracja. Edytor generuje wtedy tylko zmienione sekcje, a reszta utworu zostaje.
  Minimalna długość sekcji to 3 s, więc hit ma 3 s (1:06–1:09) zamiast 2 s.
- Koszt: 6 żądań × 3 warianty × 1 125 kr ≈ **20 250 kr**. Wartości z przycisku generowania: 3 375 kr na żądanie (900 kr/min × 1,25 min × 3).

## MUZYKA — warianty

| Nazwa robocza | Tytuł ElevenLabs / ID projektu | Prompt | Czas | Uwagi (waveform) |
|---|---|---|---|---|
| **★ MUS_MAIN** | **„Midnight Ledger”**, projekt `HeB2BBQ2GSr3nY99SWTt`, Historia → grupa z ~16:07 → **Wariant 1** (song `L5pcMs3v8Lqp4BilgD6t`). Ustawiony jako „obecny”, w Ulubionych | PEŁNY | 1:15 | Jedyny z pierwszej serii, który od razu dostał plan 75 s. Intro z wyraźnymi przerwami (pojedyncze uderzenia basu nad ciszą), build pulsujący co ~4–5 s, narastanie od ~0:58. **Jeden wyraźnie najwyższy słupek ok. 1:05–1:07**, potem gwałtowny spadek i **cisza od ~1:08–1:09** do końca |
| MUS_ALT_noPercIntro (zapas do cut-downów) | ten sam projekt `HeB2…`, Historia → grupa z ~16:20 → **Wariant 1** (W2 i W3 prawie identyczne) | PEŁNY + edycja sekcji Intro: usunięte „heartbeat pulse” i „ticking clock rhythm”; include: „no percussion”, „no drums”, „sustained dark synth pad and low strings”; exclude: „drums”, „percussion”, „ticking clock” | 1:15 | Przegenerowane tylko Intro 0:00–0:06, reszta identyczna z ★, więc da się podmienić samo intro. W intro nadal widać 2 piki (sub-bass note hits z planu): sprawdzić na słuch, czy nie brzmią jak perkusja |
| **zapas ★ MUS_BACKUP** | **„Midnight Brief”**, projekt `essPci1cGoitRTNYQBBB`, wariant „obecny” po poprawce (grupa ~16:27). W Ulubionych | PEŁNY (2. seria) + poprawka Final Hit 3 s / Outro 6 s | 1:15 | Cichy początek, ładna dynamika buildu. Hit pada później, **ok. 1:07–1:08**, cisza od ~1:10. Przy podkładaniu przesunąć o ~1–2 s albo ciąć na alercie |
| MUS_V2 | „Midnight Ledger”, projekt `IjbnOWj0VA1hHoSoeSIB` (grupa ~16:21, 3 warianty po poprawce) | PEŁNY + poprawka | 1:15 | Gęsty i głośny od pierwszej sekundy, bez cichego intro. Koniec: plateau zamiast pojedynczego hitu. Słabszy |
| MUS_V3 / V4 / V5 (nieużywane) | „Midnight Cover” `h2Zva95Rm8Z2WywNvGEo`, „Monte Carlo After Dark” `BZffRySXyTytH2jPd0qQ`, „Nocturne Briefing” `gdQlwjlWjyWpu9OYsdYM` | PEŁNY | **1:33** | Błąd planera (Final Hit 20 s). Nie poprawiałem. Można naprawić tak samo w edytorze (Final Hit → 3 s, Outro → 6 s) |
| MUS_SHORT_1..3 | „Clockwork Coup” `6kICuAxvlespmD7qR7sJ` (1:15), „Midnight File” `Kc9cXf0N4kMY5BoM91nq` (1:15), „Midnight Ledger” `F7rHScilEAjorf6cVJSR` (1:20); seria ~16:29 | KRÓTKI | 1:15 / 1:20 | Płaskie: brak prawie cichego intro, crescendo bez wyraźnego pojedynczego hitu. Cisza dopiero ~1:10. Gorsze od pełnego prompta |

Link do ★: `elevenlabs.io/app/music/project/HeB2BBQ2GSr3nY99SWTt?selectedSongId=L5pcMs3v8Lqp4BilgD6t`
Ostrzeżenie: kliknięcie innego wariantu w panelu Historia zmienia wersję „obecną”. Ta wersja pokazuje się w liście Generacje i w Ulubionych.

## ALERT ZTT — Sound Effects v3
Ustawienia: model v3, Pętla wyłączona, Wpływ promptu **90%**, auto-poprawianie wyłączone. Jedno kliknięcie daje 4 take'i (12 kr na generację).
Na stronie SFX jest dopisek, że generacje mogą być udostępniane w Explore innym użytkownikom (przełącznik „Wyłącz”). **Nie zmieniałem ustawień konta.** Do decyzji Doriana, bo to dźwięk marki.

| Prompt | Czas | Godz. | Take'i (kształt waveformu) |
|---|---|---|---|
| A (główny) „Short premium notification sound, under 1 second: a crisp metallic mechanical click…” | 0.9 s | ~16:31 | #1 i #2: seria powtarzanych tyknięć (ticker), nie ten charakter. #3: pojedynczy, bardzo krótki transjent, ogon niewidoczny (najbardziej minimalny). **#4: czysty klik z ciszy → dwa krótkie „blipy” w ~0,15–0,25 s, potem cisza (klik + blip, zgodnie z promptem)** |
| B (cyfrowy) „Ultra-short UI alert, 0.8 seconds: polished steel click-clack…” | 0.8 s | ~16:32 | #1: atak + ~0,3 s ciała. #2: długi, nieczysty, szczyt późno (odrzucić). #3: czysty atak + gładki zanik ~0,4 s (klasyczny ping). #4: pre-klik, uderzenie, drugi ping |
| C (cichy) „Very quiet, intimate version of a metallic-digital notification…” | 0.9 s | ~16:33 | Wszystkie 4 to pojedyncze krótkie transjenty. **#2: jeden słupek i cisza, najczystszy.** #1, #3, #4 mają 2 słupki |

- **★ ALERT_ZTT_master = Prompt A, take #4** (Historia SFX → wiersz „Short premium notification sound…”, ~16:31, #4, 0.9 s). W Ulubionych.
  Wybrałem #4, bo ma czysty transjent i najbardziej zwartą formę „odbezpieczenie + tick”. Alternatywa minimalistyczna: A #3 (sam klik). Jeśli A #4 na telefonie brzmi zbyt „klikowo”, zamiennik: B #3.
- **★ ALERT_ZTT_quiet = Prompt C, take #2** (wiersz „Very quiet, intimate version…”, ~16:33, #2). W Ulubionych.
  Zalecenie z pliku 05: jeśli C #2 brzmi jak inny motyw niż master, użyć mastera −12…−15 dB + LPF 8 kHz.

## Budżet
Łącznie ok. **20 300 kredytów** (muzyka ~20 250 + SFX ~36–150), limit 250 000. Żadna pojedyncza generacja nie przekroczyła 120 000.
