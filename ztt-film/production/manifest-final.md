# MANIFEST FINAL — ZTT: LICENCJA NA ZYSK (logo + SFX + eksport)
Data: 2026-11-10 · agent montażysta finalny · projekt Studio „ZTT — Licencja na zysk — MASTER"
https://elevenlabs.io/app/studio/DjVSb4OYp1RTmVVTZMBL

## 0. Stan zastany (WAŻNE)
- Na osi NIE było muzyki A3 (DOM: tylko ścieżki A1 + A2; 44 klipy). Plik „ZTT_muzyka_B1_montaz_78s.mp3" nie istniał w ElevenLabs (biblioteka Projekt/Przestrzeń robocza — brak).
- Plik był lokalnie: `ztt-film/assets/ZTT_muzyka_B1_montaz_78s.mp3` (78,528 s, identyczny z /mnt/attach/outputs/...).
  → Wgrany przez Biblioteka → „Prześlij media" i dodany od 0:00 na nową ścieżkę **A3: 0–78 500 ms**, głośność domyślna 100 %, bez cięcia/fade.
- Karta Studio koordynatora (otwarta ~77 min) cofała moje zmiany (toast „Zmiany zajmują więcej czasu niż oczekiwano") — zamknięta; praca w nowej karcie, tam zapisy działały.

## 1. LOGO (karta końcowa)
- Usunięto z osi „Badge Lockup" (klip 01a1c23d…, 75 008–78 508). Z biblioteki/zestawu nic nie usuwano.
- Dodano ★ LOGO_16x9 (Zasoby, `content_generation/YBnusd0bEQ9CD4v3acWx/YNUCEuBH7WvQhce0FA0r`) na V1: **74 996–78 506 ms** (klip 01a1c2b6…).
- Wygląd: Skala **50 %** (szer. obrazu = 50 % kadru), wycentrowane poziomo, środek obrazu na ~31 % wysokości (obraz 6–56 % H; właściwa treść logo ≈ 16–47 % H). Animacja: wejście Zanikanie 0,8 s.
- Napisy (bez zmian): „WKRÓTCE" ramka 50–73 % H, „Złap trend…" 69–87 % H → logo nad nimi, bez nachodzenia. Tło logo #000 + V1 pod napisami (napisy na V2/V3 rysują się nad nim).
- Ocena: podgląd WebGL w tym środowisku renderuje się na czarno (zrzuty puste) → kompozycja oceniona geometrycznie z ramek zaznaczenia. Do potwierdzenia na eksporcie (1:16,5).

## 2. SFX (wszystkie 11, głośność 45 %)
| SFX | ID ★ | Oś (ms) | Ścieżka |
|---|---|---|---|
| zamek pianki | ZCKZtI7VtY1nWejtMzrL | 11 494–16 494 | A4 |
| wibracja telefonu | E8Iji3o6TcOjrJR65BXp | 18 500–19 980 | A4 |
| plusk/wędka | tuDolNXzVJpzjLuzLv9q | 27 417–30 297 | A4 |
| uderzenie w tarczę | sOcr6AFkvGmkz1M01m1l | 29 961–32 441 | A2 (auto) |
| zatrzaski walizki | WG8gqHenuiqjEMcRCr2G | 32 034–34 914 | A4 |
| downshift V12 | eAlOHuQhIbeNZr8aj8mg | 35 991–40 991 | A4 |
| ruletka | uiMA0DpgJ2Y5iSPCX9vW | 42 963–47 963 | A4 |
| żetony | 7joXVPC8I6rxUghICbSH | 48 521–52 521 | A4 |
| setki powiadomień | 6SRq69uy31QhXnnfGZ7l | 59 262–64 262 | A4 |
| narastanie tłumu | MFfgdycfLOTfMyFRUN39 | 62 465–69 465 | A2 (auto) |
| shimmer | dkCcTH32ANLsCLSdL2Cg | 65 951–70 951 | A4 |
- Odchyłki ≤ 0,04 s. Nic po 1:14,6 (ostatni SFX kończy się 70,95 s).
- Studio samo wybiera ścieżkę przy „Dodaj do osi czasu": 2 SFX (tarcza, tłum) wylądowały w wolnych lukach A2 (między alertami) — nie kolidują z alertami; nie przenosiłem (ryzyko przesunięcia).
- Mechanika: Biblioteka → Przestrzeń robocza → SFX → wyszukaj fragment promptu → kafelek po React key = ID take'a → „Dodaj do osi czasu" (JS click). Zaznaczanie wąskich klipów: klik w górnej części klipu (środek zasłania uchwyt fade „cursor-ew-resize").

## 3. Weryfikacja po przeładowaniu (nowa karta)
- 56 klipów: V3 2 txt · V2 2 txt · V1 18 wideo + 1 logo · A1 11 (heartbeat + 10 VO) · A2 10 alertów + 2 SFX · A3 1 muzyka · A4 9 SFX. Max koniec 78 508 ms. Logo = nowy klip (model Nano Banana Pro).

## 4. Eksport
- Eksportuj → Typ mediów: Wideo · Jakość: Wysoka jakość (brak wyboru rozdzielczości w UI; format projektu 16:9) · Zakres: Cała oś czasu. Brak pokazanego kosztu kredytowego.
- Render ruszył od razu (toast „Renderowanie… 0%"), ~5 %/30 s, **zakończony po ok. 2 min** → status ✓ „MP4".
- Gdzie leży: Studio → projekt MASTER → przycisk **„Eksportuj" → zakładka „Historia"** → wpis „ZTT — Licencja na zysk — MASTER · MP4" z ikoną **„Pobierz"** (NIE pobierano na dysk). UI nie pokazuje linku podglądu, rozdzielczości ani długości pliku; oczekiwane: 16:9, „Wysoka jakość" (najwyższa dostępna), ~1:18,5 (78,5 s).
- Ustawień udostępniania projektu NIE zmieniano. Saldo kredytów nie było sprawdzane — UI eksportu nie pokazał kosztu.
- DO SPRAWDZENIA PRZEZ CZŁOWIEKA po pobraniu: kompozycja karty końcowej (1:15–1:18,5), czy SFX 45 % siedzą dobrze pod muzyką (bez odsłuchu), muzyka A3 100 % zgodnie z gotowym miksem.

---
# MASTER EN — „ZTT — License to Profit — MASTER EN"
Data: 2026-11-10 · agent montażysta EN
- **URL kopii:** https://elevenlabs.io/app/studio/piAXMakxMAbxvB9xyPCx (ID `piAXMakxMAbxvB9xyPCx`)
- Powstała przez: lista projektów Studio → „Opcje projektu" przy PL MASTER → „Duplikuj projekt" → nazwa zmieniona z „… (kopia)". Projektu PL nie edytowano.

## 1. Lektor EN (10 klipów, głośność 100 %, bez fade)
Usunięto z kopii 10 klipów PL z A1 (9 VO + FF Lena), od końca do początku. Heartbeat, alerty, SFX, muzyka i obraz bez zmian (pozycje identyczne jak w sekcjach 1–3 wyżej).
| Klip (plik w „ZTT License to Profit - VO EN") | Oś start–koniec (ms) | Start PL (ms) | Długość | Ścieżka |
|---|---|---|---|---|
| EN_VO_01_STAR | 9 987–13 958 | 9 987 | 3,971 s | A2 |
| EN_VO_02_STAR | 15 451–19 317 | 15 451 | 3,866 s | A1 |
| EN_VO_03_STAR | 23 460–27 248 | 23 460 | 3,788 s | A4 |
| EN_VO_04_STAR | 29 019–35 210 | 29 019 | 6,191 s | A1 |
| EN_VO_05_STAR | 38 534–42 008 | 38 534 | 3,474 s | A1 |
| EN_FF_STAR (Blondie) | 43 999–46 768 | 43 999 | 2,769 s | A2 |
| EN_VO_06_STAR | 48 333–51 415 | 48 333 | 3,082 s | A1 |
| EN_VO_07_STAR | 53 044–54 611 | 53 044 | 1,567 s | A4 |
| EN_VO_08_STAR | 62 560–65 721 | 62 560 | 3,161 s | A1 |
| EN_VO_09_STAR | 69 343–74 594 | 69 343 | 5,251 s | A1 |
- Odchyłka startu względem PL: 0 ms (wszystkie 10). Długości zgodne z ★ z manifest-vo-en.md, więc to właściwe pliki (FF = Blondie 2,769 s, nie Lena 2,847 s).
- Studio samo wybrało ścieżkę: 4 klipy trafiły w wolne luki A2 (VO_01, FF) i A4 (VO_03, VO_07). Nie nachodzą na alerty ani SFX. Klipy na A4 mają 100 % (głośność jest per klip, SFX obok mają 45 %). Nie przenosiłem.
- Głośność odczytana w popoverze „Audio" dla VO_01–04: Wolumen 100 %, Pojawienie 0 s, Zanikanie 0 s, Wycisz wył. Pozostałych 6 nie klikano (wartość domyślna).

## 2. Napisy EN (te same klipy, zmieniona tylko „Treść")
| Oś (ms) | Było | Jest |
|---|---|---|
| 66 014–70 014 | ZŁAP TREND TERMINAL | CATCH THE TREND TERMINAL |
| 67 543–70 043 | LICENCJA NA ZYSK | LICENSE TO PROFIT |
| 75 008–78 508 | WKRÓTCE | COMING SOON |
| 75 008–78 508 | Złap trend, zanim złapie Ciebie. | Catch the trend before it catches you. |
- Czcionka, kolor, rozmiar, pozycje, animacje i czasy nietknięte. **Rozmiaru nie zmniejszano.**
- ⚠ NIE SPRAWDZONO WIZUALNIE, czy „CATCH THE TREND TERMINAL" (24 znaki zamiast 19, rozmiar 100 %) mieści się w kadrze i nie łamie się na dwie linie. Podgląd był niedostępny (patrz pkt 5). Do obejrzenia na eksporcie w 1:06–1:10; jeśli wychodzi, zmniejszyć rozmiar i wyeksportować ponownie.

## 3. Weryfikacja po przeładowaniu (nowa karta)
- Kopia EN: **56 klipów** (18 wideo + 1 logo, 4 teksty, 33 audio), koniec 78 508 ms, tytuł „ZTT — License to Profit — MASTER EN", pozycje EN VO i 4 teksty EN jak w tabelach.
- Projekt PL (odczyt po eksporcie, bez klikania): tytuł „ZTT — Licencja na zysk — MASTER", 56 klipów, A1 = heartbeat + 10 VO PL w pozycjach z manifest-montaz-audio.md (9987–14036 … 69343–74672), teksty PL bez zmian.

## 4. Eksport EN
- Eksportuj → Typ mediów: Wideo · Jakość: Wysoka jakość · Zakres: Cała oś czasu. UI nie pokazał kosztu.
- Render ok. 2,5–3 min, zakończony. **Historia eksportu:** projekt EN → „Eksportuj" → zakładka „Historia" → wpis „ZTT — License to Profit — MASTER EN · MP4" z przyciskiem „Pobierz". NIE pobierano.
- Nikt nie odsłuchał ani nie obejrzał wyniku: do sprawdzenia przez człowieka wymowa EN klona, miks VO z muzyką/SFX, napisy.

## 5. Środowisko i mechanika (dla następnych agentów)
- Okno Chrome było zminimalizowane: `innerWidth = 0`, `outerWidth = 199`, `resize_window` nic nie zmienił. Zrzuty ekranu i prawdziwe kliknięcia nie działały; edytor przeszedł w układ mobilny, a listy wirtualizowane renderowały 0–2 elementy.
- Całość zrobiona skryptami JS (syntetyczne PointerEvent/MouseEvent):
  - Oś czasu: 50 px/s, klip widoczny w DOM dopiero po ustawieniu `scrollLeft` kontenera osi w jego okolicę.
  - Zaznaczenie klipu: zdarzenia na elemencie `[data-agent-clip-id]`, 6 px od góry. Usuwanie: przycisk „Usuń" w pasku klipu.
  - Kursor: klik w linijkę NIE działa na zdarzeniach syntetycznych. Działa klik w klip muzyki (A3, cała oś) w punkcie x = 64 + t·50 − scrollLeft; ustawia kursor co do 1 ms.
  - Biblioteka: lista kafelków ma wysokość 0, więc trzeba nadać kontenerowi listy i jego przewijanym potomkom `height: 3000px` w stylu inline; wtedy renderuje wszystkie 14 kafelków. Przewijanie tej listy ją psuje (znika do zmiany filtra).
  - W folderze EN są dwa kafelki o identycznym tekście „[sultry, amused, slow] What's... your game?": pierwszy = Lena ALT (2,847 s), ostatni = Blondie ★ (2,769 s). Rozróżnienie po długości klipu po dodaniu (Lena dodana omyłkowo i cofnięta „Cofnij").
  - Treść napisu: w układzie mobilnym pole „Treść" otwiera przycisk „Generuj" w pasku klipu tekstowego (jego onClick to tylko `view.open({type:"edit"})`, nie generacja). Dla klipów wideo/audio tego nie sprawdzałem.
- Karta agenta zamarzła raz (CDP timeout) w trakcie pracy; zamknięta i otwarta nowa, zapisy były na serwerze. Karta 974286823 z projektem PL (nie moja, zamrożona) została otwarta.
