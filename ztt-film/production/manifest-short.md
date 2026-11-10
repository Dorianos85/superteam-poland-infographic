# MANIFEST SHORT 9:16 (32 s) — „ZTT — SHORT 9x16 — PL"
Data: 2026-11-10 · agent montażysta SHORT PL. Notatki przyrostowe.

## Plan (z SHORT-EDL + „OCENA I ★")
Obraz (V1, wyciszone): 1A 0–3,0 (src 5,0–8,0; tap ~0:01.8) · 2B r2 3,0–7,0 (src 0,3–2,5 + 5,95–7,75) · 4A 7,0–11,3 (src 2,2–6,5) · 7A 11,3–15,0 (src 1,5–5,2) · 7B r2 15,0–19,0 (src 4,0–8,0) · 9A 19,0–22,0 (src 1,6–4,6) · 10B wariant A 22,0–28,6 (src 0,15–6,75) · karta 28,6–32,0.
Audio: muzyka 0–32 s; alerty master 1,8 / 7,0 / 15,0 / 19,3 / 28,8, quiet 5,5; SFX 45 %: zamek 4,0 · plusk 10,8 · ruletka 11,3 · żetony 16,5 · powiadomienia 19,3; VO: VO_03 7,2 · FF Lena 11,8 · VO_06 15,3 · VO_09 23,0.

## Projekt
- **URL: https://elevenlabs.io/app/studio/XduwSmt6zo2EmQkCTTeJ** (ID `XduwSmt6zo2EmQkCTTeJ`), nazwa „ZTT — SHORT 9x16 — PL", format 9:16 (nagłówek edytora → selektor proporcji → „9:16 Tiktok, Reels, Shorts").
- Utworzony: Studio → „Nowy pusty projekt" → „Projekt wideo (Nowe)".

## V1 — OBRAZ (8 klipów = 7 ujęć, 2B z dwóch kawałków; wszystkie „Wycisz" WŁ.)
| Ujęcie | ID generacji (klucz kafelka) | Oś (ms) | Źródło (s) | Uwagi |
|---|---|---|---|---|
| 1A | jYxpZaD2EDwDt9WrL1Tm | 0–3000 | 5,064–8,064 | tap (src 6,8) ≈ 0:01.74 → alert na 0:01.8 |
| 2B r2 (a) | Afu8F5V9FTR4tvudebOw | 3000–5196 | 0,30–2,496 | zamek ~0:04.0 |
| 2B r2 (b) | Afu8F5V9FTR4tvudebOw | 5196–6996 | 5,953–7,753 | tarcza świeci ≈ 0:05.6 |
| 4A | Pvc07XunxfzHfo5tKNYk | 6996–11305 | 2,206–6,515 | zacięcie (src 6,0) ≈ 0:10.79 |
| 7A | U8aA3q4OuGt6G02dDgz9 | 11305–15002 | 1,50–5,197 | |
| 7B r2 | r7QcMceVsmI7AE77tKub | 15002–19109 | 3,957–8,064 (do końca pliku) | cięcie do 9A 0,11 s później niż EDL |
| 9A | jj3bweL1jm8LHlGXcCy8 | 19109–21990 | 1,722–4,603 | fala rozbłysku (src 1,9) ≈ 0:19.29 |
| 10B wariant A | xpL3rppnEkik17j7iHU0 | 21990–28616 | 0,0–6,626 | cięcie 10 ms przed 0:22.0 (klatka 660 = już 10B); początku 0,15 s nie dało się odciąć (Studio odmawia podziału tak blisko krawędzi); po 28,616 pusta oś = czerń |

## Mechanika (ta sesja; okno Chrome widoczne, zrzuty działają, podgląd WebGL czarny)
- Kafelki biblioteki (Przestrzeń robocza, „Wszystko", bez wybierania folderu — najnowsze są na górze): React key kafelka = ID generacji → `addByKey(id)` klika „Dodaj do osi czasu".
- Linijka: klik ustawia kursor z dokładnością do piksela (bez przyciągania). Zoom po 3× „Pomniejsz": x = 64 + t·33,66 px (≈30 ms/px).
- Dodawanie bez mikro-przerw: kursor ~1 s ZA końcem ostatniego klipu → dodaj → kliknij przerwę → „Usuń zaznaczoną przerwę" (ripple dosuwa idealnie).
- Przyciski paska klipu („Podzielony", „Usuń", „Audio") działają przez JS `.click()`; zaznaczanie klipu i linijka — prawdziwym kliknięciem.
- UWAGA: 4× szybkie „Powiększ" wywaliło edytor („Ups, coś poszło nie tak") i zamroziło kartę → nowa karta; zapis był na serwerze. Zoom klikać pojedynczo.

## AUDIO (stan po dodaniu; ms)
| Klip | Źródło / ID | Oś (ms) | Ścieżka | Głośność |
|---|---|---|---|---|
| Muzyka | upload „ZTT_muzyka_SHORT_32s.mp3" (Biblioteka → Projekt; wgrany skryptem fetch→File→input „Prześlij media", 1 282 605 B) | 0–32000 | A1 | 100 %, bez cięcia |
| ALERT master | SFX `ztTs5zD1xzfn8xTuqHpY` (887 ms) | 1813–2700 · 19315–20202 · 28795–29682 | A2 | 100 % |
| ALERT master | j.w. | 7013–7900 · 15007–15894 | A3 | 100 % |
| ALERT quiet | SFX `CLHfJvwSGhcb0ExbjevB` | 5497–6384 | A2 | 100 % |
| **VO_03 ★** | folder VO, kafelek „[calm, slow, low voice]…" (3788 ms) | **7191–10979** | A2 | 100 % |
| **FF Lena ★** | kafelek „[sultry, amused, slow] Na co... grasz?" — PIERWSZY z dwóch (2508 ms = Lena) | **11797–14305** | A2 | 100 % |
| **VO_06 ★** | kafelek „[calm] Ja nie gram. [pause] [confident] Ja widzę." (3004 ms) | **15304–18308** | A2 | 100 % |
| **VO_09 ★** | kafelek „[low, intimate] A Ty? [long pause]…" (5329 ms) | **23000–28329** | A2 | 100 % |
| SFX zamek | `ZCKZtI7VtY1nWejtMzrL` | 505–5505 | A4 | 45 %, zanik 0,3 s — PRZESUNIĘTY z 4,0 na 0,5: w tym pliku zdarzenie (zamek) jest ok. 3,4–3,7 s od początku (z waveformu), więc wypada na ~0:04.0 |
| SFX plusk | `tuDolNXzVJpzjLuzLv9q` | 10817–12005 (przycięty) | A3 | 45 %, zanik 0,3 s |
| SFX ruletka | `uiMA0DpgJ2Y5iSPCX9vW` | 11292–16292 | A4 | 45 %, zanik 0,3 s |
| SFX żetony | `7joXVPC8I6rxUghICbSH` | 16492–19107 (przycięty na cięciu do 9A) | A4 | 45 %, zanik 0,3 s |
| SFX powiadomienia | `6SRq69uy31QhXnnfGZ7l` | 19315–21990 (przycięty na 0:22.0) | A3 | 45 %, zanik 0,3 s |
- SFX/alerty: Biblioteka → Przestrzeń robocza → folder „Zasoby" (root!) → filtr SFX → szukaj fragmentu promptu („notification", „Roulette", „casino", „Fishing float", „harbor") → kafelek po React key = ID.
- Usuwanie klipu na ścieżkach audio NIE robi ripple (sprawdzone). Głośność: suwak 0–200 % w popoverze „Audio" (klik w suwak; ctrl+klik zaznacza wiele klipów).
- UWAGA: wpisywanie liter poza polem tekstowym odpala skróty edytora (pojawił się znacznik zakresu „Od 0:00 / Do 0:07" na linijce — przy eksporcie wybrać „Cała oś czasu").

## NAPISY I KARTA KOŃCOWA (klipy tekstowe; pozycje = ramka zaznaczenia w % kadru 9:16)
Styl wspólny podpisów: Barlow Condensed, Pogrubienie, biały #FFFFFF, Rozmiar 170 %, Efekty: Cień tekstu WŁ. (#000 50 %, rozmycie 4, przesunięcie 2/2) + Kontur tekstu WŁ. (#000 100 %, szer. 2). Bez animacji.
| Tekst (pole „Treść") | Oś (ms) | Ścieżka | Styl | Ramka x | Ramka y |
|---|---|---|---|---|---|
| Wykres mi nie ucieka. Nigdy. | 7191–10981 | V2 | wspólny | 11,2–88,8 % | 64,5–75,4 % |
| Na co grasz? | 11797–14307 | V2 | wspólny + Styl: **Kursywa** | 31–69 % | 64,5–75,4 % |
| Ja nie gram. Ja widzę. | 15304–18304 | V2 | wspólny | 19–81 % | 64,5–75,4 % |
| A Ty? Złap trend —⏎zanim złapie Ciebie. (2 linie, Enter w polu) | 23000–28330 | V2 | wspólny | 21,7–78,3 % | 62,2–77,7 % |
| ZŁAP TREND TERMINAL | 24516–28306 | V3 | wspólny, kolor **#D4AF37** | 18,7–81,3 % | 13,1–24,0 % |
| WKRÓTCE | 28616–31996 | V1 (za 10B) | kolor #D4AF37, Rozmiar 280 % | 26,4–73,6 % | 52,5–68,6 % |
| Złap trend, zanim złapie Ciebie. | 28616–31996 | V2 | biały, Waga Normalny, Rozmiar 120 % | 21,3–78,7 % | 69,7–78,2 % |
| LOGO „DORIANOS Clean Neon Logo" (Zestawy marki → DORIANOS → Logotypy) | 28616–31996 | V3 (obraz) | Wygląd: Skala 72 % | 14–86 % | 12,8–53,3 % |
- Wszystko mieści się w kadrze (najszersza ramka 11,2–88,8 %), nic nie wchodzi w dolne 20 % (najniższa krawędź 78,2 %) ani w górne 12 % (tytuł od 13,1 %; logo od 12,8 % — obraz ma własny czarny margines).
- Podgląd WebGL na zrzutach jest czarny → kompozycja oceniona po ramkach zaznaczenia (klik w element na podglądzie przy zwiniętej osi czasu; `.border-blue-500`). Samych liter nie widziałem.
- Mechanika: pierwszy napis utworzony przyciskiem „Tekst" (pusty panel), kolejne = ⋮ „Kopiuj" + klik w linijkę + Cmd+V (wkleja w miejscu kursora z tym samym stylem i pozycją), potem zmiana „Treść" (klik w pole, Ctrl+A, wpisz) i „Czas trwania" (pole w s). Pozycja: przeciąganie ramki na podglądzie działa tylko zdarzeniami syntetycznymi (PointerEvent down/move/up na `.border-blue-500`), zwykły drag narzędzia nie przesuwa. Rozmiar/Skala: suwak 0–500 % (klik w suwak). Kolor: pole hex → Ctrl+A → wpisz → Enter.
- Escape zamyka popover I odznacza klip.

## Status
- [x] projekt utworzony, 9:16, nazwany
- [x] obraz V1 ułożony i wyciszony
- [x] muzyka, VO PL, alerty, SFX
- [x] napisy + tytuł + karta końcowa
- [x] weryfikacja po przeładowaniu: 32 klipy (8 wideo, 7 tekstów, 1 logo, 16 audio: 1 muzyka + 6 alertów + 4 VO + 5 SFX), koniec osi 32000 ms (0:32), muzyka na A1 0–32000
- [x] EKSPORT: Eksportuj → Typ mediów: Wideo · Jakość: „Wysoka jakość" (najwyższa; druga opcja to „Szybki eksport") · Zakres: **Cała oś czasu** (domyślnie było zaznaczone „Zakres od–do" 0:00–0:07:06 — przełączone ręcznie). Koszt nie był pokazany. Render ok. 1 min → ✓ „ZTT — SHORT 9x16 — PL · MP4" w Eksportuj → zakładka „Historia" (ikona „Pobierz"). NIE pobierano.

## DO SPRAWDZENIA PRZEZ CZŁOWIEKA (nikt nie obejrzał ani nie odsłuchał wyniku)
- Podgląd był czarny: wygląd liter (rozmiar 170 % na tle jasnego świtu w 4A), kolizja tytułu z twarzą w 10B (tytuł 13–24 % wysokości), karta końcowa.
- SFX zamka przesunięty wg waveformu (zdarzenie ~0:04.0); SFX 45 % pod muzyką; plusk przycięty do 1,2 s.
- 10B bez odcięcia pierwszych 0,15 s; ostatnie ~16 ms 10B po 0:28.6.
- Na linijce został znacznik zakresu „Od 0:00 / Do 0:07" (przypadkowy skrót klawiszowy) — nie wpływa na oś, ale ustawia domyślny zakres eksportu.

## WSKAZÓWKI DLA AGENTA EN („ZTT — SHORT 9x16 — EN")
1. Lista projektów Studio → „Opcje projektu" przy „ZTT — SHORT 9x16 — PL" → „Duplikuj projekt" → zmień nazwę kopii. Projektu PL nie edytuj i nie trzymaj go otwartego w drugiej karcie.
2. VO (ścieżka A2) — usuń 4 klipy PL i wstaw EN z folderu „ZTT License to Profit - VO EN" w TYCH SAMYCH startach (ms): **7191** EN_VO_03 ★ · **11797** EN_FF ★ (Blondie 2,769 s — OSTATNI z dwóch kafelków „What's... your game?"; pierwszy to Lena ALT 2,847 s) · **15304** EN_VO_06 ★ · **23000** EN_VO_09 ★. Długości ★ EN wg manifest-vo-en.md: VO_03 3,788 · FF 2,769 · VO_06 3,082 · VO_09 5,251 s. Alert 28795 jest po końcu VO_09 (EN kończy się ~28251) — OK. Usuwanie na ścieżkach audio nie przesuwa innych klipów.
3. Napisy — zmień tylko „Treść" i „Czas trwania" (start bez zmian):
   - 7191: „The chart never runs from me. Ever." (3,79 s) — 35 znaków zamiast 28 przy 170 % → ramka wyjdzie ok. 2–98 % szerokości: **zmniejsz Rozmiar do ~140 %** albo złam na 2 linie („The chart never runs⏎from me. Ever.").
   - 11797: „What's your game?" kursywa (2,77 s)
   - 15304: „I don't play. I see." (3,08 s)
   - 23000: „And you? Catch the trend —⏎before it catches you." (5,25 s; 2 linie; 1. linia 26 znaków — sprawdź ramkę, ew. Rozmiar 150 %)
   - 24516: „CATCH THE TREND TERMINAL" (24 znaki zamiast 19 → przy 170 % ok. 79 % szerokości; sprawdź ramkę, ma zostać w 10–90 %)
   - 28616 (V1): „COMING SOON" (11 znaków zamiast 7 przy 280 % → ok. 74 % szerokości, OK) · 28616 (V2): „Catch the trend before it catches you." (38 znaków przy 120 % → ok. 68 %, OK)
   Ramkę sprawdzisz: zwiń oś czasu („Zwiń oś czasu"), ustaw kursor w czasie napisu, kliknij napis na podglądzie i odczytaj `.border-blue-500` względem canvasu.
4. Obraz, muzyka, alerty, SFX, logo — bez zmian.
5. Eksport: w oknie eksportu KONIECZNIE przełącz Zakres na „Cała oś czasu" (domyślnie wskakuje „Zakres od–do" 0–7 s).
6. Nie wpisuj liter, gdy fokus nie jest w polu tekstowym (skróty edytora). Zoom osi klikaj pojedynczo (seria kliknięć „Powiększ" wywala edytor).

# SHORT EN — „ZTT — SHORT 9x16 — EN"
Data: 2026-11-10 · agent montażysta SHORT EN
- **URL: https://elevenlabs.io/app/studio/hRMymJzfGChQAQjI3FJl** (ID `hRMymJzfGChQAQjI3FJl`), 9:16.
- Powstał przez: lista projektów Studio → „Opcje projektu" przy PL → „Duplikuj projekt" → „… (kopia)" → nazwa zmieniona w nagłówku edytora (klik w tytuł, Ctrl+A, wpisz, Enter). Projektu PL nie edytowano.

## VO EN (4 klipy, 100 %, bez fade; usunięto 4 klipy PL z A2)
| Klip (folder „ZTT License to Profit - VO EN") | Klucz kafelka | Oś (ms) | Start PL | Odchyłka | Długość | Ścieżka |
|---|---|---|---|---|---|---|
| EN_VO_03 ★ | DgKtN18AU7Vwm2HF6ei0 | 7181–10969 | 7191 | −10 ms | 3,788 s | A4 |
| EN_FF ★ Blondie (OSTATNI kafelek „What's... your game?") | LabgRfTohh4ZTHbDISj6 | 11790–14559 | 11797 | −7 ms | 2,769 s | A2 |
| EN_VO_06 ★ | Z2gIKmTr9DsHWHeEhdPR | 15323–18405 | 15304 | +19 ms | 3,082 s | A2 |
| EN_VO_09 ★ | Mk3KXrDk5HDScGX8VNzr | 23003–28254 | 23000 | +3 ms | 5,251 s | A4 |
- Długości zgodne z ★ z manifest-vo-en.md (FF 2,769 s = Blondie, nie Lena 2,847 s). Odchyłki wynikają z rozdzielczości linijki (26 px/s ≈ 38 ms/px), mieszczą się w ±50 ms.
- Studio samo wstawiło VO_03 i VO_09 na A4 (wolne luki; nie nachodzą na SFX: zamek 505–5505, ruletka 11292–16292, żetony 16492–19107). Głośność jest per klip (domyślne 100 %); popovera „Audio" nie otwierano. Nie przenoszono.
- Muzyka, alerty, SFX, obraz, logo: pozycje identyczne jak w PL (odczyt po przeładowaniu).

## Napisy EN (te same klipy; zmieniona „Treść", w 3 podpisach „Czas trwania", w 1 „Rozmiar")
| Tekst | Oś (ms) | Rozmiar | Ramka x | Ramka y |
|---|---|---|---|---|
| The chart never runs from me. Ever. | 7191–10981 (bez zmian, 3,79 s) | **135 %** (było 170 %; przy 170 % ramka wychodziła poza kadr) | 11,8–88,2 % | 65,5–74,4 % |
| What's your game? (Kursywa zachowana) | 11797–14567 (2,77 s) | 170 % | 24–76 % | 64,7–75,3 % |
| I don't play. I see. | 15304–18404 (3,10 s — do końca VO) | 170 % | 25,5–74,5 % | 64,7–75,3 % |
| And you? Catch the trend —⏎before it catches you. (2 linie) | 23000–28250 (5,25 s) | 170 % | 13,2–86,7 % | 62,4–77,5 % |
| CATCH THE TREND TERMINAL (#D4AF37) | 24516–28306 | 170 % | 12,2–87,8 % | 13,2–23,8 % |
| COMING SOON (#D4AF37) | 28616–31996 | 280 % | 19,3–80,7 % | 52,6–68,4 % |
| Catch the trend before it catches you. | 28616–31996 | 120 % | 16,7–83,3 % | 69,9–78,0 % |
- Wszystkie ramki w 8–92 % szerokości, najniższa krawędź 78 % (nic w dolnych 20 %). Pozycje, czcionka, kolory, efekty bez zmian. Ramki mierzone przy zwiniętej osi czasu (podgląd 270 px szer., dokładność ok. ±0,4 %).

## Weryfikacja po przeładowaniu
- EN: 32 klipy (8 wideo, 7 tekstów, 1 logo, 16 audio), koniec 32000 ms (0:32), teksty i VO EN jak w tabelach; Rozmiar 135 % (podpis 1) i Kursywa (podpis 2) odczytane z popovera „Tekst".
- PL (odczyt po eksporcie, bez klikania): tytuł „ZTT — SHORT 9x16 — PL", 32 klipy, 7 tekstów PL i 4 VO PL w pozycjach 7191–10979 / 11797–14305 / 15304–18308 / 23000–28329 — bez zmian.

## Eksport EN
- Eksportuj → Wideo · „Wysoka jakość" · Zakres „Cała oś czasu" (w kopii było już zaznaczone; kliknięte dla pewności). Koszt nie był pokazany. Render ok. 1 min → ✓ „ZTT — SHORT 9x16 — EN · MP4" w Eksportuj → „Historia" (ikona „Pobierz"). NIE pobierano.

## Uwagi / do sprawdzenia przez człowieka
- Podgląd WebGL czarny, nikt nie obejrzał ani nie odsłuchał: wymowa EN, miks VO z muzyką, wygląd liter (podpis 1 mniejszy niż pozostałe: 135 % vs 170 %).
- Po drodze drugi podpis dostał na chwilę tekst trzeciego (klik w klip przed końcem animacji rozwijania osi nie zmienił zaznaczenia) — poprawione i potwierdzone po przeładowaniu. Wniosek: po „Zwiń/Rozwiń oś czasu" czekać ~2 s i sprawdzać `document.activeElement.value` przed pisaniem.
- Platforma to Windows: zaznacz wszystko = Ctrl+A (Cmd+A wpisuje literę „a").
- Klipy mają w DOM `data-agent-clip-type/-start/-end` (ms) — szybki odczyt całej osi bez klikania.
