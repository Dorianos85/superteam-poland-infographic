# MANIFEST MONTAŻ — AUDIO (ElevenLabs Studio, projekt „ZTT — Licencja na zysk — MASTER")
Data: 2026-11-09 · agent audio. Notatki przyrostowe.
Projekt: https://elevenlabs.io/app/studio/DjVSb4OYp1RTmVVTZMBL

## Mechanika (ustalona)
- Biblioteka → Przestrzeń robocza → filtr „Wszystko" (filtr „Głos" pokazuje GŁOSY, nie pliki) → selektor folderu → „ZTT Licencja na zysk - VO". Kafelki = tekst promptu (nie nazwa pliku). Lista wirtualizowana.
- FF Lena vs Maja mają identyczny tekst — rozróżnione po „Rozwiń": Lena 56 KB (2,51 s), Maja 54 KB. Na osi FF ma 2508 ms = Lena ✓.
- Ruler: x = 64 + t[s]·10,61 px (zoom domyślny, okno 1536 px); klik w linijkę y≈462, potem „Dodaj do osi czasu" (JS click na przycisku kafelka). Precyzja ±60 ms.

## A. LEKTOR — ścieżka audio A1 (wszystko na jednej ścieżce)
| Klip | Plik (prompt) | Oś start–koniec (ms) | Cel EDL |
|---|---|---|---|
| VO_01 ★ t3 | [whispering in the dark] | 9987–14036 | 0:10.0 |
| VO_02 ★ t2 | [calm satisfaction, slight smile] | 15451–19160 | 0:15.5 |
| VO_03 ★ t2 | [calm, slow, low voice] | 23460–27248 | 0:23.5 |
| VO_04 ★ t2 | [cold, measured intelligence briefing] | 29019–35288 | 0:29.0 |
| VO_05 ★ t1 | [confident][slow] Jestem uzbrojony | 38534–42165 | 0:38.5 |
| FF Lena ★ t3 | [sultry, amused, slow] Na co... grasz? | 43999–46507 | 0:44.0 |
| VO_06 ★ t1 | [calm] Ja nie gram… | 48333–51337 | 0:48.3 |
| VO_07 ★ t1 | [casual] Zrealizowane zyski? | 53044–54768 | 0:53.0 |
| VO_08 ★ t3 | [whispers, mysterious] | 62560–65642 | 1:02.5 |
| VO_09 ★ t4 | [low, intimate] A Ty? | 69343–74672 | 1:09.3 |
Odchyłki ≤ 60 ms. Głośność: domyślna (100%).

## B. MUZYKA — ustalenia
- Studio → Przestrzeń robocza → filtr Muzyka pokazuje generacje Music (1 pozycja na projekt = najnowsza piosenka projektu). Dla projektu „Midnight Ledger" HeB2… widoczna jest piosenka `IFfMLRKaBQkbDyDaVZ6b` = edycja ★ (source_song_id = L5pcMs3v8Lqp4BilgD6t) = MUS_ALT_noPercIntro (inne tylko intro 0–6 s; waveform: hit 66,0–67,3 s, cisza od ~69 s → hit trafia w 1:06,0 bez przesuwania).
- Oryginalny ★ L5pc nie występuje w bibliotece Studio. Edytowane piosenki (song_length_ms = null: IFfM, 5r43, Midnight Brief) NIE dają się dodać: toast „Ten plik multimedialny nadal się ładuje…" (wielokrotnie, także po odtworzeniu podglądu). Piosenki nieedytowane (np. Clockwork Coup) dodają się od razu (test + Cofnij).
- Music → Generacje → Ulubione → wiersz „Midnight Ledger" → ⋮ Więcej → „Zapisz do zasobów" → folder Zasoby (root) → Zapisz (wykonane ~21:40 UTC). Wynik do sprawdzenia w bibliotece Studio.
- WYNIK „Zapisz do zasobów": w Zasobach (root, „Pliki") powstał wpis „Midnight Ledger.mp4" (typ Utwór, 9 lis) — ale w Studio to TA SAMA piosenka IFfM… i nadal „nadal się ładuje" → nie da się dodać.
- Studio Agent (czat, Alpha) poproszony o dodanie IFfM… od 0:00 → odmówił („ID nie jest dostępny w tym projekcie… system odpowiedział, że go nie ma"), niczego nie zmienił. Licznik w czacie: „1,694 kredytów używane przez agenta".
- DECYZJA: muzyki NIE dodano (nie podmieniałem ★ na inny utwór bez zgody). Kandydaci, które DA SIĘ dodać (nieedytowane): Clockwork Coup (L5iOEn…, crescendo 54–66 s, spadek po ~69 s), Nocturne Briefing / Monte Carlo After Dark / Midnight Cover (1:33). Jak dodać ★: pobrać L5pc z Music → w Studio „Prześlij media" → wstawić od 0:00 (hit wypada na 1:06,0 bez przesuwania; waveform ALT/★: szczyt 62–67 s, cisza od ~69 s).
- ID alertów (data-testid w SFX → Ulubione): ALERT master (A #4) = `ztTs5zD1xzfn8xTuqHpY`; ALERT quiet (C #2) = `CLHfJvwSGhcb0ExbjevB`.
- SFX: Studio → Przestrzeń robocza → filtr SFX pokazuje historię SFX; klucz kafelka = ID take'a z manifest-sfx (np. ZCKZtI7V… = zipper ★, dkCcTH32… = shimmer ★) → dodawanie po ID.
- Środowisko: przeglądarka współdzielona (inna karta Suno); karty w tle zamarzają (timeouty CDP), karta Studio była 2× podmieniana/przeładowywana. VO przetrwało przeładowanie (10 klipów A1).

## Status
- [x] A. Lektor
- [ ] B. Muzyka
- [ ] C. Alert ZTT
- [ ] D. SFX
- [ ] E. Weryfikacja
- [ ] F. Eksport

## SESJA 2 (agent audio #2, 2026-11-10) — muzyka B1 + alerty + SFX + eksport
- Start sesji. Zadanie: A muzyka „ZTT_muzyka_B1_montaz_78s" od 0:00 · B 10 alertów · C SFX · D weryfikacja · E eksport MP4 1080p.
- A. MUZYKA — STOP: pliku „ZTT_muzyka_B1_montaz_78s" NIE MA. Sprawdzone (2× po przeładowaniu): Studio → Biblioteka → Projekt (Wszystko/Audio — tylko heartbeat, alerty, VO, wideo, logo); Przestrzeń robocza (Wszystko — pełne przewinięcie listy, filtr Audio, Muzyka, wyszukiwarka „ZTT_muzyka"/„ZTT"/„muzyka"/„B1" → brak); /app/files (root: foldery ZTT Teaser - wideo, ZTT Licencja na zysk - VO, Coach FI, „Midnight Ledger.mp4") oraz „Przesłane pliki" (tylko obrazy; ostatni audio-upload w Studio = stary aokigahara-vo-12s.mp3). Na osi NIE ma żadnej muzyki (Midnight Ledger nie był dodany) — nic nie usuwano.
- Uwaga: w Studio filtr „Audio" (8. chip, za „Mowa") pokazuje utwory Music + uploady audio; uploady wyświetlają się z nazwą pliku (np. „aokigahara-vo-12s.mp3").
- B. ALERT ZTT — już na osi (ścieżka A2, ułożył poprzedni agent): 4805 quiet (prompt „Very quiet, intimate…", 100%) · 7537 master 50% · 19039 · 27417 · 35048 · 41078 · 48050 · 57566 · 59356 · 75279 (master „Short premium notification sound…"). Odchyłki ≤ 0,08 s. Głośność sprawdzona: #1 100%, #2 50%, #3 100%, #10 100% (pozostałe nie klikane).
- C. SFX — na osi jest tylko heartbeat 0–8000 ms (na ścieżce A1 razem z VO). Reszty SFX NIE dodawano (zatrzymanie po A zgodnie z zadaniem).
- E. Eksport — ODWOŁANY przez koordynatora (wymiana logo na karcie końcowej). Nie uruchamiano.
- Środowisko: karta Studio zamarzała (CDP timeout 45 s po długim przewijaniu biblioteki w JS) — pomogło zamknięcie karty i nowa. Pętle JS trzymać < ~20 s.
