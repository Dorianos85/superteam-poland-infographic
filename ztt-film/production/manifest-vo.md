# MANIFEST VO — „ZTT: LICENCJA NA ZYSK" (ElevenLabs TTS)

Data sesji: 2026-11-07 · konto Doriana (Scale) · wszystko w **Text to Speech → Historia** + wybrane take'i w **Zasobach**.
Nic nie pobierano na dysk.

## 1. Model i ustawienia (jedne dla całego VO agenta)

| | |
|---|---|
| Głos agenta | **Dorian's Telegram** (klon, voice_id `ADCIBDDMDpyKxIQX0m8Y`) |
| Model | **Eleven v4** (`eleven_v4`). UI oznacza go jako „Zalecane dla Dorian's Telegram" |
| Stabilność | 0.50 (suwak Kreatywny–Solidny) |
| Podobieństwo | 0.80 |
| Speed / Style / Speaker boost | **v4 nie ma tych suwaków**. Tempo sterowane tagami `[slow]`, `[pause]`, wielokropkiem |
| Język | Polski · format MP3 44,1 kHz |
| Koszt | Dla klona historia pokazuje „Użyto 0 kredytów” na generację v4. Testy v3/v2 i femme fatale to łącznie poniżej ~2 tys. kredytów. Daleko od budżetu 150 tys. |

**Jak działa v4:** każde kliknięcie „Wygeneruj” daje **2 warianty**: `eleven_v4` (Generacja 1) oraz `eleven_v4_exp` (Generacja 2, eksperymentalny).
W Historii mają ten sam tekst. Rozróżnisz je filtrem „+ Model” albo po długości (tabela niżej).
v4 jest **deterministyczny**: ten sam tekst i ustawienia dają identyczny plik. Dlatego „take” = osobny wariant zapisu tagów (t1 = tagi z pliku 04, t2–t5 = opisowe tagi v4 albo inna interpunkcja).
Składnia sterowania w v4 to te same nawiasy kwadratowe co w v3. Edytor podświetla je na fioletowo jako tagi. Działają też tagi opisowe (np. `[calm, slow, low voice]`, `[brief pause]`).

### Test wizytówki VO_03 („Wykres mi nie ucieka. Nigdy.”, okno 4 s)
| Model | Długości | Uwagi |
|---|---|---|
| **Eleven v4** (tagi) | 3.63 / 3.40 · 3.47 / 3.63 (wpisany ręcznie) | stabilnie w oknie 4 s; tagi rozpoznane, długość nie sugeruje czytania tagów |
| Eleven v3 (tagi) | 5.25 / 3.32 · 5.72 / 4.28 · 3.87 / 5.07 (v3 / v3_dpo) | duży rozrzut, 3 z 6 przekracza 4 s; docs: klony PVC nie są w pełni zoptymalizowane pod v3 |
| Multilingual v2 (bez tagów, `Wykres mi nie ucieka... Nigdy.`, speed 0.92, stab 0.5, sim 0.8, style 0.2, boost ON) | 1.99 (2×, deterministycznie) | zbyt szybko i płasko, wielokropek ledwo działa |

**Wybór: Eleven v4.** Najstabilniejszy czas, poprawnie interpretuje tagi, rekomendowany przez UI i dokumentację dla PVC.
Uwaga: barwy klona nie oceniłem słuchem (brak odsłuchu). **Do potwierdzenia na słuchawkach.**

## 2. Linie agenta (długości zmierzone z dekodowanego pliku audio z Historii, w sekundach)

Format: `tN: v4 / v4_exp` · ★ = wybrany i zapisany w Zasobach · ID = ID generacji (widoczne w „Pokaż szczegóły”)

### VO_01 — POD WODĄ (okno ~4 s)
- t1 `[whispers] Są miejsca... [pause] do których nie dociera nic...` — 4.13 / 4.13
- t2 `[whispers, slow, intimate] … [brief pause] …` — 4.21 / 4.13
- **t3 ★** `[whispering in the dark] Są miejsca... do których... nie dociera nic...` — **4.05 (v4, ID RlDcSbmPutYBkQMjd9d2)** / 4.13

### VO_02 — JACHT (okno ~5 s)
- t1 `[confident] ...do mnie dociera wszystko, [pause] co ważne.` — 3.24 / 3.00
- **t2 ★** `[calm satisfaction, slight smile] ... [brief pause] co ważne.` — **3.71 (v4, ID ZFzaudbAd9IVes2bU557)** / 3.71
- t3 `[confident, relaxed] ...do mnie dociera wszystko... co ważne.` — 2.85 / 2.85

### VO_01+02 sklejka (zapas, jeden request)
- `[whispers] Są miejsca... [pause] do których nie dociera nic... [confident] do mnie dociera wszystko, [pause] co ważne.` — **7.00 (v4, ID jUnSLca3d1M6vxrjOvax)** / 7.00 (v4_exp, yoiGSyiDTNWcdRBEVkbt)

### VO_03 — RYBY O ŚWICIE (okno ~4 s) — kluczowa
- t1 `[calm][slow] Wykres mi nie ucieka. [pause] [confident] Nigdy.` — 3.63 / 3.40 (dwa identyczne requesty + test ręczny 3.47 / 3.63)
- **t2 ★** `[calm, slow, low voice] Wykres mi nie ucieka... [brief pause] [confident, firm] Nigdy.` — **3.79 (v4, ID m7GFO4UwypINXIeSpbKO)** / 3.71
- t3 `[calm, morning quiet] … [pause] [low, firm] Nigdy.` — 3.24 / 3.47
- t4 `[calm][slow] Wykres mi nie ucieka... [confident] NIGDY.` — 3.40 / 3.16
- t5 (ALT w Zasobach) `[low, steady voice] … [long pause] [confident, deeper] Nigdy.` — 4.05 / **3.97 (v4_exp, ID zmGDsz55VFsoH5Ufmvbx)**

### VO_04 — WAR ROOM (okno ~7 s)
- t1 `[serious] Widzę przepływy informacji. [pause] I kapitału. [pause] [intense] Widzę ataki, zanim nadejdą.` — 5.88 / 6.11
- **t2 ★** `[cold, measured intelligence briefing] … [brief pause] … [rising tension] Widzę ataki, zanim nadejdą.` — **6.27 (v4, ID djYKi58NGMUcq1ro5uWM)** / 6.19
- t3 `[serious, low] … I kapitału... [intense, slightly faster] Widzę ataki — zanim nadejdą.` — 5.64 / 5.64

### VO_05 — AUTO NOCĄ (okno ~4 s)
- **t1 ★** `[confident][slow] Jestem uzbrojony... [pause] po zęby.` — 3.16 / **3.63 (v4_exp, ID xAT59yyGHNwrWuOCs7Lg)**
- t2 `[low, dry irony] Jestem uzbrojony... [brief pause] po zęby.` — 3.16 / 3.40
- t3 `[confident, low register] Jestem uzbrojony... po zęby.` — 2.69 / 2.85

### VO_06 — KASYNO, dialog (okno ~3 s) — kluczowa
- **t1 ★** `[calm] Ja nie gram. [pause] [confident] Ja widzę.` — 3.08 / **3.00 (v4_exp, ID Wg8uWat3cRUzkJQ0HuYE)**
- t2 (ALT w Zasobach) `[quiet, intimate, unhurried] Ja nie gram. [brief pause] [firm, low] Ja widzę.` — 3.08 / **2.93 (v4_exp, ID U6rrJlm5DT5smntJW5Zr)**
- t3 `[calm] Ja nie gram... [confident] Ja WIDZĘ.` — 2.59 / 2.59
- t4 `[soft, flirtatious yet dangerous] Ja nie gram. [pause] Ja widzę.` — 3.16 / 3.08
- t5 `[calm, low voice] Ja nie gram. Ja widzę.` — 2.35 / 2.59

### VO_07 — DOM TRADERÓW, dialog (okno ~2 s)
- **t1 ★** `[casual] Zrealizowane zyski?` — **1.72 (v4, ID PnF3sJ32B3qg1kdJtmFu)** / 1.72
- t2 `[offhand, slight smile] Zrealizowane zyski?` — 2.51 / **3.71 ⚠** (v4_exp podejrzanie długi: możliwy śmiech albo artefakt, sprawdzić)
- t3 `[casual, light rising intonation] Zrealizowane... zyski?` — 2.77 / 2.59

### VO_08 — EVENT (okno ~3 s)
- t1 `[whispers][slow] Oni wszyscy... [pause] już wiedzą.` — 3.32 / 3.47
- t2 `[whispering in awe] Oni wszyscy... [brief pause] już wiedzą.` — 3.40 / 3.40
- **t3 ★** `[whispers, mysterious] Oni wszyscy... już... wiedzą.` — **3.08 (v4, ID UGC0vRtGYt90RUlt23M0)** / 3.24

### VO_09 — FINAŁ (okno ~6 s; ostatnie słowo musi wybrzmieć przed ALERTEM) — kluczowa
- t1 `[serious] A Ty? [pause] [confident][slow] Złap trend — zanim złapie Ciebie.` — 4.60 / 4.60
- t2 (ALT w Zasobach) `[direct, to camera] A Ty? [brief pause] [slow, weighty, confident] Złap trend — zanim złapie Ciebie.` — **5.15 (v4, ID eDSligjmjiDtyytLR5ze)** / 4.91
- t3 `[serious] A Ty? [pause] [confident][slow] Złap trend... zanim złapie Ciebie.` — 4.75 / 4.83
- **t4 ★** `[low, intimate] A Ty? [long pause] [confident] Złap trend — zanim złapie CIEBIE.` — **5.33 (v4, ID 72LXD6z3Iu04e3kJeBfb)** / 5.25
- t5 `[serious, low voice] A Ty? [pause] [slow, final, resolute] Złap trend — zanim złapie Ciebie.` — 4.91 / 4.99

Kontrola tagów: żaden take nie ma długości sugerującej przeczytanie tagu na głos (np. długi tag opisowy w VO_04 t2 dodał tylko ~0.3 s względem t1).
Jedyny podejrzany wariant to VO_07 t2 v4_exp (3.71 s). UI nie pokazał ostrzeżeń.
★ wybrane **wyłącznie po dopasowaniu czasu**. Przed montażem odsłuchaj na słuchawkach (połknięte tagi, wymowa, clipping).

## 3. Femme fatale — „Na co grasz?” (ten sam model v4; stab 0.45, sim 0.75)

Voice Library → filtr **Polish + female**, fraza „velvety”. Obie kandydatki to Professional Voice Clone, notice 730 dni, rate ×1 (bez dopłat). Na płatnym planie (Scale) można ich używać komercyjnie. Obie **dodane do „Moich głosów”**.
- **Lena – Velvety & Trustworthy** (`d26eMDXtCFizSzBVHFFS`, middle-aged, opis: „deep, calm and velvety… naturally sensual”)
- **Maja – Velvety Polish • Luxury Narration** (`tWVHsc0fuVfAZWfScX9a`, 25–35, „deep, velvety, sophisticated”)

| Take | Lena (v4 / v4_exp) | Maja (v4 / v4_exp) |
|---|---|---|
| t1 `[sultry][slow] Na co grasz?` | 1.72 / 1.65 | 1.80 / 1.88 |
| t2 `[low, velvety, seductive voice] Na co grasz?` | 1.65 / 1.57 (+ duplikat 1.57 / 1.57) | 1.57 / 1.65 |
| t3 `[sultry, amused, slow] Na co... grasz?` | **★ 2.51 (v4, ID ZPiMX0CMoi4B9nlPj1HD)** / 2.59 | 2.69 / **2.43 (v4_exp, ID 0ayiHEDzSavkBbs8ipE7, ALT)** |

★ Lena t3: profil (dojrzała, niska, „sensual”) najbliższy briefowi, a fraza się ciągnie (~2.5 s). „Lily” nie była potrzebna.

## 4. Gdzie to leży

**Zasoby → folder „ZTT Licencja na zysk - VO”** (15 plików, nazwy już przemianowane):
`VO_01_podwoda_t3_STAR`, `VO_02_dociera_t2_STAR`, `VO_0102_sklejka_ZAPAS`, `VO_03_wykres_t2_STAR`, `VO_03_wykres_t5_ALT`,
`VO_04_widze_t2_STAR`, `VO_05_uzbrojony_t1_STAR`, `VO_06_niegram_t1_STAR`, `VO_06_niegram_t2_ALT`, `VO_07_zyski_t1_STAR`,
`VO_08_oniwiedza_t3_STAR`, `VO_09_aTy_t4_STAR`, `VO_09_aTy_t2_ALT`, `FF_01_nacograsz_Lena_t3_STAR`, `FF_01_nacograsz_Maja_t3_ALT` (wszystkie .mp3).
W ElevenLabs Studio wstawia się je przez import z Zasobów.

**Pozostałe take'i są tylko w Historii TTS** (Text to Speech → zakładka Historia, 7 lis). Generacje nie trafiają do Zasobów automatycznie.
Jak znaleźć: wpisz fragment tekstu w „Historia wyszukiwania…” (np. „Wykres mi nie ucieka”), a warianty v4 i v4_exp rozróżnisz filtrem „+ Model”.
Jak przenieść: „Pokaż szczegóły” (ikona ≡) → **„Zapisz do zasobów”** → folder ZTT. ID generacji widać w szczegółach.

## 5. Uwagi
- W UI v4 nie ma suwaka speed ani speaker boost, więc ustawień 0.9–0.95 / boost z pliku 04 nie da się zastosować. Tempo robią tagi.
- Eksport: Historia zapisuje MP3 44,1 kHz 128 kbps (domyślne). Jeśli montaż potrzebuje WAV, trzeba to zrobić przy eksporcie ze Studio albo zregenerować z innym formatem wyjściowym.
- Wymowy „ZTT” nie testowano, bo w liniach VO jej nie ma.
