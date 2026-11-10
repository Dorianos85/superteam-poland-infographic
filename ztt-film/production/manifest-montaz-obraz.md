# MANIFEST MONTAŻ — OBRAZ + NAPISY (ElevenLabs Studio)
Data: 2026-11-09 · agent montażu obrazu. Notatki przyrostowe.

## Projekt
- Nazwa: **ZTT — Licencja na zysk — MASTER** (nadana ręcznie, klik w tytuł w lewym górnym rogu edytora → wpisz → Enter)
- URL: https://elevenlabs.io/app/studio/DjVSb4OYp1RTmVVTZMBL  (ID projektu: `DjVSb4OYp1RTmVVTZMBL`)
- Utworzony: Studio → „Nowy pusty projekt" → „Projekt wideo (Nowe) — Rozpocznij pusty projekt wideo" (druga opcja „Projekt wideo — wróć do poprzedniej wersji Studio" = stary edytor, NIE używana). Format w nagłówku: 16:9.

## UI edytora (nowe Studio)
- Lewa kolumna ikon: Biblioteka, Zestawy marki, Skrypt, Napisy.
- Biblioteka: zakładki Projekt / Przestrzeń robocza / Odkrywaj; filtry Wszystko/Głos/Wideo/Obraz/Muzyka/SFX/Mowa.
  W „Przestrzeń robocza" pod filtrami jest selektor folderów (domyślnie „Zasoby") → rozwiń → Pliki →
  „ZTT Teaser - wideo" (24 pliki), „ZTT Licencja na zysk - VO" (15), „Coach FI — Mark…" (8).
  Kafelki w folderze pokazują fragment PROMPTU (nie nazwę pliku z datą) — identyfikacja po prompcie/miniaturze.
- Środek: podgląd; prawa kolumna: Czat (Studio Agent, Alpha) / Komentarze.
- Dół: oś czasu (play, undo/redo, zoom −/+, pełny ekran). Nagłówek: 16:9, Udostępnij, **Eksportuj**.

## Identyfikacja plików w folderze „ZTT Teaser - wideo" (pierwsze 6 kafelków = najnowsze, 9.11 wieczór)
ID = `content_generation/<genId>/<itemId>` z URL miniatury (storage.googleapis.com/xi-backend/...). Przypisanie po treści promptu (do potwierdzenia podglądem):
| Kafelek | genId (początek) | Początek promptu | Prawdopodobnie |
|---|---|---|---|
| 1 | LtY1vWsx | „The man is @Image 2 (keep his exact face); his silhouette from behind - black baseball cap…" | 8A (Veo, T19:07:02) |
| 2 | xbS34BCl | „…His face looks exactly like @Image 1: light blue-grey eyes…" | 10B (T19:03:23) |
| 3 | nLFnw5QB | „…The monitor UI looks like the screen in @Image 2…" | 8B (wnętrze/monitor) |
| 4 | Tjdw5QA2 | „The man is @Image 1 (same jaw, light stubble… The phone screen looks like @Im…" | 7B (T18:49:44) |
| 5 | vS0kRbJj | „…The woman is @Image 2 (same black evening gown…) Slow dolly-in" | 7A (T18:43:50) |
| 6 | jNzlhIMP | „(same silhouette… standing at the rooftop edge) Slow rising wide shot" | 10A (dach) |
| 7 | GCyfC1Ic | „(keep his exact jaw, stubble and lip…" | 3B (G7) — nie potwierdzone |
Kolejne kafelki (2A, 5B, 6A, 6B, 9A, 9B, 1A, 2B, 3A, 4A, 5A) — nie zmapowane (przerwa).
Lista jest wirtualizowana (renderuje ~6 kafelków naraz) — przewijać kontener listy.

## Status
- [x] projekt utworzony i nazwany (pusty, 16:9)
- [ ] klipy na osi — NIE ROZPOCZĘTE
- PRZERWA: ok. 20:30 UTC rozszerzenie Claude w Chrome rozłączyło się (list_connected_browsers = []), brak połączenia przez ~15 min mimo kilku prób. Karta agenta (tabId 974286775) mogła zostać otwarta na projekcie — zamknąć ją przy wznowieniu.
- Następny krok: otworzyć URL projektu, Biblioteka → Przestrzeń robocza → folder „ZTT Teaser - wideo", ustalić sposób dodawania na oś (drag / „+") i przycinania.

## WZNOWIENIE (agent montażu obrazu #2, 9.11 ~wieczór)
### Pełne mapowanie folderu „ZTT Teaser - wideo" (24 kafelki, kolejność od góry; wiersz.kolumna; genId z URL miniatury)
| Poz. | genId | Prompt (charakterystyczny fragment) | Ujęcie | Użyć? |
|---|---|---|---|---|
| 0.0 | LtY1vWsx | „@Image 2… silhouette from behind - black baseball cap" | 8A (Veo, DORIAN) | ★ |
| 0.1 | xbS34BCl | „His face looks exactly like @Image 1: light blue-grey eyes" | 10B (DORIAN) | ★ |
| 1.0 | nLFnw5QB | „The monitor UI looks like the screen in @Image 2" | 8B (DORIAN) | ★ |
| 1.1 | Tjdw5QA2 | „(same jaw, light stubble…) The woman is @…" | 7B (DORIAN) | ★ |
| 2.0 | vS0kRbJj | „The woman is @Image 2 (same black evening gown…) Slow dolly-in on a roulette" | 7A (DORIAN) | ★ |
| 2.1 | jNzlhIMP | „(same silhouette… standing at the rooftop edge)" | 10A (DORIAN) | ★ |
| 3.0 | GCyfC1Ic | „(keep his exact jaw, stubble and lips); framed exactly like @Image 2" | 3B (DORIAN G7) | ★ |
| 3.1 | ace4QMi4 | „Slow push-in and gentle half-orbit that always stays behind" | 5A (DORIAN) | ★ |
| 4.0 | bmftfPOC | „@Image 1… Slow push-in through a rotating tunnel" | 1A (DORIAN) | ★ |
| 4.1 | LMrPL0y8 | „@Image 1… Low-angle medium shot on a wooden pier at night" | 2B (DORIAN) | ★ |
| 5.0 | qu6pibUP | „@Image 1… Static wide-to-medium shot across a mist-covered lake" | 4A (DORIAN) | ★ |
| 5.1 | FD5osvmH | „@Image 1… Sweeping slow aerial-to-deck crane shot over a luxury yacht" | 3A (DORIAN) | ★ |
| 6.0 | 31qNQkQo | „[Shot/camera] Interior cockpit shot from the back seat, behind the driver" | 6B (9.11 rano) | ★ |
| 6.1 | dHTHyjUA | „Natural realistic hands with five fingers" | 9B (9.11 rano) | ★ |
| 7.0 | 0k2PBIq4 | „[Shot/camera] High wide crane shot over a packed conference hall" | 9A (9.11 rano) | ★ |
| 7.1 | lA9QLWOr | „The car is the car from reference…" | 6A (9.11 rano) | ★ |
| 8.0 | WXXUGfrl | „The man is the man from reference… wooden pier at night" | 2B stary (7.11) | — |
| 8.1 | dLURKZP8 | „The man is the man from reference… Smooth underwater tracking shot alongside a scuba" | 2A (7.11) | ★ |
| 9.0 | iyrNZpyd | „…Tight insert shot: a phone on a teak side table" | 3B stary | — |
| 9.1 | t8JPdaT9 | „…mist-covered lake" (stary) | 4A stary | — |
| 10.0 | E5geMsnH | „…aerial-to-deck crane shot… yacht" (stary) | 3A stary | — |
| 10.1 | rG9pO7ep | „…Slow orbital dolly behind the man around a large h(ologram)" | 5A stary | — |
| 11.0 | Ainsah9e | „The man's tuxedo silhouette… rotating tunnel" | 1A stary | — |
| 11.1 | 0MFFrI8h | „The hands and tuxedo… Top-down overhead shot… briefcase" | 5B (7.11) | ★ |
Uwaga: wcześniejsza tabela (kafelki 1–7) miała 8B/7B/7A/10A przypisane trochę inaczej — powyższa (po pełnym tekście promptu) jest właściwa.
Kafelki „Twórca: Ja" bez folderu = cała historia; folder wybiera się selektorem „Zasoby" → Pliki → „ZTT Teaser - wi…".

### Mechanika edycji (ustalona, nowe Studio)
- Dodanie klipu: Biblioteka → najechać kafelek → przycisk „Dodaj do osi czasu" (aria-label). Klip ląduje W MIEJSCU KURSORA (playhead). Jeśli playhead jest wewnątrz istniejącego klipu → tworzy NOWĄ ścieżkę (V2). Więc najpierw kliknąć linijkę (ruler) tuż za końcem ostatniego klipu.
- Kliknięcie linijki zostawia mikro-przerwę (10–80 ms) → przerwę zaznacza się zwykłym kliknięciem na nią (przy dużym zoomie) i usuwa przyciskiem „Usuń zaznaczoną przerwę" (ikona kosza przy Cofnij/Ponów). Magnetyczna oś czasu WŁ. (domyślnie) → usuwanie klipów/przerw robi ripple.
- Przycinanie: zaznacz klip (klik na klipie) → klik na linijce w punkcie cięcia → przycisk „Podzielony" (nożyczki w pasku pod podglądem) → zaznacz zbędny kawałek → „Usuń" (kosz w tym samym pasku). Strzałki ←/→ = ±1 klatka. Skróty S/Delete z klawiatury NIE działały przez automatyzację.
- Pasek klipu (pod podglądem): Wyodrębnij · Prędkość · Audio (Wolumen %, Pojawienie s, Zanikanie s, przełącznik „Wycisz") · Wygląd (Skala, Rotacja, Krycie, „Odwróć w poziomie", „Odwróć w pionie") · Animacja · Podzielony · Usuń · ⋮ (Kopiuj, Przesuń do przodu/tyłu, Komentarz, Pobierz, Skróty klawiszowe, Usuń).
- UWAGA: lewy panel po zaznaczeniu klipu wideo pokazuje formularz „Generuj" (regeneracja) — NIE klikać „Generuj".
- Puste miejsce: lewy panel „Albo utwórz nowy klip w miejscu kursora": Obraz / Wideo / Tekst / Mowa / Muzyka / SFX.
- Odczyt pozycji: DOM `[data-agent-clip-id]` ma data-agent-clip-start/end (ms).

### Postęp V1 (start-koniec na osi w ms, przed usunięciem mikro-przerw)
1A 0–6048 (src 2.0–8.0) · 2A 6060–10060 (src 1.0–5.0) · 2B 10060–14087 (src 3.5–7.5) · 3A 14128–18033 (src ~4.15–8.06) · 3B 18089–22116 (src 2.0–6.0) · 4A 22183–28201 (src ~2.07–8.06) · 5A 28256–32284 (src 3.0–7.0)

### V1 — STAN PO UŁOŻENIU 18 klipów (mikro-przerwy usunięte; pozostała tylko 12 ms przerwa 6.048–6.060, za wąska do kliknięcia — pomijalna)
| # | Ujęcie | Oś (s) | Źródło (s) |
|---|---|---|---|
| 1 | 1A | 0.000–6.048 | 2.0–8.06 |
| 2 | 2A | 6.060–10.060 | 1.0–5.0 |
| 3 | 2B | 10.060–14.087 | 3.5–7.5 |
| 4 | 3A | 14.087–17.992 | ~4.15–8.06 |
| 5 | 3B | 17.992–22.019 | 2.0–6.0 |
| 6 | 4A | 22.019–28.037 | ~2.05–8.06 |
| 7 | 5A | 28.037–32.065 | 3.0–7.0 |
| 8 | 5B | 32.065–36.026 | ~3.05–7.0 |
| 9 | 6A | 36.026–39.987 | 0.0–3.96 |
| 10 | 6B | 39.987–43.024 | 0.46–3.5 |
| 11 | 7A | 43.024–47.513 | 2.0–6.47 |
| 12 | 7B (ODBITY POZIOMO) | 47.513–52.002 | 1.5–6.0 |
| 13 | 8A | 52.002–55.501 | 2.0–5.48 |
| 14 | 8B | 55.501–59.010 | ~4.55–8.06 |
| 15 | 9A | 59.010–62.509 | 1.0–4.49 |
| 16 | 9B | 62.509–66.005 | 2.0–5.48 |
| 17 | 10A | 66.005–68.507 | ~5.56–8.06 |
| 18 | 10B | 68.507–74.943 | 0.7–7.15 |
Odchyłki od EDL ≤ 0,09 s. 7B: Wygląd → „Odwróć w poziomie" WŁ. (UWAGA: na telefonie w 7B jest drobny napis „ZTT" — po odbiciu będzie lustrzany; do oceny przez człowieka, ew. wyłączyć flip).

### Audio klipów wideo
Wszystkie 18 klipów V1: Audio → „Wycisz" WŁ. (zaznaczenie zakresu: klik pierwszy klip + Shift+klik ostatni → Audio → Wycisz działa na wiele naraz). Sprawdzone punktowo (1A, 2A, 10B).

### NAPISY (zrobione)
- V2: tekst „ZŁAP TREND TERMINAL" 66.014–70.014 (4 s), Barlow Condensed, Normalny, kolor #D4AF37 (złoty), rozmiar 100%, wejście Zanikanie 1 s, wyjście Zanikanie 0,8 s, pozycja: środek, lekko w górę (~43% wysokości kadru).
- V3: tekst „LICENCJA NA ZYSK" 67.543–70.043 (2,5 s), Barlow Condensed, Normalny, #D4AF37, rozmiar 60%, wejście Zanikanie 1 s, wyjście 0,8 s, pozycja pod tytułem (~66% wysokości).
- Interpretacja EDL: zapis „1:06.0–1:15.0 (nad 10A, potem nad 10B do 1:10.0)" jest sprzeczny — przyjęto koniec tytułu 1:10.0 (twarz w 10B od ~1:10 zostaje czysta).
- Mechanika tekstu: pusty panel (nic nie zaznaczone) → „Tekst" tworzy klip 5 s w miejscu kursora (na nowej ścieżce, jeśli koliduje). Pasek: Tekst (Kolor hex, Czcionka, Waga, Styl, Rozmiar %) · Efekty · Wygląd (Rotacja, Krycie, odbicia) · Animacja (Animuj wejście/wyjście + czas) · Czas trwania (pole „s"). Treść = pole „Treść" w lewym panelu. Pozycję zmienia się przeciągnięciem ramki tekstu na podglądzie.

### KARTA KOŃCOWA (zrobiona)
- V1: logo „Badge Lockup" z Zestawu marki DORIANOS (lewa kolumna → Zestawy marki → selektor zestawu (przycisk z nazwą, domyślnie był „Coach FI") → DORIANOS → Logotypy → „Dodaj do osi czasu"). 75.008–78.508, Wygląd: Skala 45%, przesunięte do góry kadru; wejście Zanikanie 0,8 s. (Drugi zasób zestawu: Obrazy → „Wireframe Profile Illustration" — nieużyty.)
- V2: „WKRÓTCE" 75.008–78.508, Barlow Condensed, Pogrubienie, #D4AF37, 100%, pod logo; wejście Zanikanie 1,0 s.
- V3: „Złap trend, zanim złapie Ciebie." 75.008–78.508, Barlow Condensed, Normalny, biały, 55%, pod „WKRÓTCE"; wejście Zanikanie 1,2 s.
- Tło = czerń (pusty kadr po 10B). 74.943–75.008 = 65 ms czerni (pomijalne).
- **Łączna długość projektu: 1:18,5 (78.508 s)** — zgodnie z EDL.

### STATUS (koniec etapu OBRAZ + NAPISY)
- [x] 18 klipów V1 wg EDL, wyciszone; 7B odbity poziomo
- [x] napisy 1:06–1:10 + karta końcowa 1:15–1:18,5
- [ ] NIE eksportowano (zgodnie z zadaniem). Korekcja koloru — pominięta (brak filtra koloru w pasku klipu; jest tylko „Efekty" dla tekstu).
- DO WERYFIKACJI PRZEZ CZŁOWIEKA (podgląd): (1) 7B — na ekranie telefonu może być drobny napis „ZTT"; po odbiciu byłby lustrzany → jeśli widać, wyłącz: zaznacz 7B (0:47.5–0:52) → Wygląd → „Odwróć w poziomie" OFF. (2) Czy napisy renderują się w podglądzie (po przeładowaniu jeden zrzut z 1:08 nie pokazał tekstu — prawdopodobnie fonty jeszcze się ładowały; dane klipów tekstu są zapisane poprawnie).
- Uwaga techniczna: zrzuty ekranu edytora często timeoutują (podgląd WebGL); dane czytać z DOM `[data-agent-clip-id]` (start/end w ms, typ video/text/image). Projekt zapisuje się na bieżąco (Firestore) — po przeładowaniu wszystko jest.

## INSTRUKCJE UI DLA AGENTA AUDIO (Studio, ten sam projekt)
1. Dodawanie audio: lewa kolumna „Biblioteka" → zakładka „Przestrzeń robocza" → filtr Głos / Muzyka / SFX (lub Wszystko) → selektor folderu (domyślnie „Zasoby") → Pliki → „ZTT Licencja na zysk - VO" (15 plików VO). Muzyka/SFX: sprawdź ten sam selektor oraz zakładkę „Projekt"/filtry Muzyka i SFX (generacje „Midnight Ledger", SFX z Ulubionych — jeśli nie ma ich w Zasobach, w Studio może ich nie być; wtedy panel pusty → opisz ograniczenie).
2. Najedź kafelek → „Dodaj do osi czasu" (aria-label). Klip ląduje w MIEJSCU KURSORA: najpierw kliknij linijkę czasu w docelowym momencie (np. 0:10.0 dla VO_01) — linijka jest nad ścieżkami (y zmienia się wraz z liczbą ścieżek; ±1 klatka strzałkami ←/→). Jeśli w tym miejscu jest już klip na tej samej ścieżce audio, Studio samo tworzy nową ścieżkę.
3. Precyzja: odczyt `[data-agent-clip-id]` → data-agent-clip-start/end (ms). Czas kursora: element tekstowy w formacie m:ss:ff (30 kl/s) obok przycisku Play.
4. Głośność/fade: zaznacz klip → pasek pod podglądem → „Audio": Wolumen (%), Pojawienie (s), Zanikanie (s), „Wycisz". Keyframe'ów/duckingu w tym popoverze NIE widziałem — ducking muzyki pod VO zrobić przez pocięcie muzyki („Podzielony" w momentach VO) i obniżenie Wolumenu na kawałkach pod VO (np. 40–50% ≈ −6…−8 dB) + krótkie Pojawienie/Zanikanie na granicach. Sprawdź też ⋮ „Więcej działań" i prawy czat „Studio Agent".
5. Przycinanie audio: tak jak wideo — zaznacz klip, klik w linijkę w punkcie cięcia, „Podzielony", zaznacz zbędny kawałek, „Usuń". Magnetyczna oś czasu jest WŁ. (usunięcie robi ripple na tej samej ścieżce — uważaj na ścieżce muzyki!). Mikro-przerwę zaznacza się kliknięciem i usuwa przyciskiem „Usuń zaznaczoną przerwę".
6. NIE klikać „Generuj" w lewym panelu po zaznaczeniu klipu (to regeneracja za kredyty).
7. Eksport: przycisk „Eksportuj" w prawym górnym rogu (obok „Udostępnij"); format 16:9 w nagłówku. Okna eksportu nie otwierałem.
