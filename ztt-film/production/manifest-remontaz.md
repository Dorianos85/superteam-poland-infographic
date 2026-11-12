# MANIFEST REMONTAŻ — podmiana ujęć na PRAWDZIWEGO Doriana (16:9 PL)
Data: 2026-11-12 · agent montażysta (remontaż 16:9). Notatki przyrostowe. Wzorzec dla wersji EN.
Projekty: MASTER PL https://elevenlabs.io/app/studio/DjVSb4OYp1RTmVVTZMBL · NAPISY PL https://elevenlabs.io/app/studio/vh0tGkEI68hZtL4wBVhQ

## Status
- [x] MASTER — 10 slotów podmienionych, zweryfikowane po przeładowaniu, wyeksportowane (Historia eksportu, 12 lis)
- [x] NAPISY PL — 10 slotów podmienionych identycznie, zweryfikowane, wyeksportowane (Historia eksportu, 12 lis)

## Analiza źródeł (contact sheets z preview_content 852×480, co 0,4 s + dogęszczenia; czasy w s źródła)
- 1A nloIWPF7…: tunel 0–3,6 · sylwetka 2,4–4,4 · frontalnie 4,8+ · palec 5,6–6,7 · **TAP ≈ 6,75** (pierścień 6,77) · strzałka 7,1–8,0
- 2B E6bjdWZ…: wynurzenie 0,4–1,6 · twarz frontalnie 1,6–4,4 · rozpinanie ≈ 4,4–4,8 · smoking od ≈ 5,0 · zegarek świeci ≈ 7,6
- 3A oYQuJo…: przelot 0–3,6 · pokład 4,0+ · twarz 3/4→frontalnie 5,6–8,0
- 3B N8Cf78…: **ekran telefonu zapala się ≈ 0,9–1,2** · insert dłoń/telefon do 4,4 · tilt po smokingu 4,8–7,0 · **półuśmiech (dolna połowa twarzy) 7,2–8,0**
- 4A rx3M13…: szeroki plan pomost 0–4,9 · cięcie na insert 5,0 · zegarek zielony 5,6–7,4 · **zacięcie (szarpnięcie wędki) ≈ 7,47**, rozprysk 7,6
- 7A JGbdj8…: kobieta podchodzi 0–1,2 · szept 1,6–8 · półuśmiech 5,2–8,0
- 7B zrivtq…: dłoń bierze telefon 0–1,6 · **ekran zapala się/obrót ≈ 1,6–2,0** · telefon pokazany kobiecie 2,4–6 · żetony krupiera od ≈ 5,6
- 8A 40QM7N…: wejście przez drzwi 0–1,6 · od tyłu do sali 2–4,4 · traderzy odwracają się ≈ 6,0–7,2
- 8B 0TxKfc…: trader obraca monitor 0–1,6 · Dorian 3/4 1,6–2,8 · unosi nadgarstek 2,8 · **zegarek rozbłyska ≈ 3,75** · patrzy na zegarek do ≈ 6,0 · cięcie ≈ 6,2 (inne ujęcie)
- 10B GSu0wP…: od tyłu 0–0,8 · obrót 0,8–2,4 · frontalnie 2,4–5,0 · zegarek/tap 5,2–6,9 · **twarde cięcie do czerni ≈ 6,97** (nie płynne wygaszenie)

## Plan cięć 16:9 (oś ms ← źródło s)
| Slot | Oś (ms) | ★ ID | Źródło in–out (s) | Zgranie |
|---|---|---|---|---|
| 1A | 0–6048 | nloIWPF7hiZKWDSvt15O | 1,95–8,00 | tap 6,75 → 0:04.80 (alert quiet 4805) |
| 2B | 10060–14087 | E6bjdWZadOXmmMDXnlD5 | 3,75–7,78 | rozpięcie ≈ 0:11.1, zegarek ≈ 0:13.9 |
| 3A | 14087–17992 | oYQuJo03SZO1Ynpxe20b | 4,10–8,00 | twarz od ≈ 0:15.6 |
| 3B | 17992–22019 | N8Cf78I97yxs8RGrQMVc | 2 kawałki: 0,00–2,00 (17992–19992) + 6,00–8,03 (19992–22019) | telefon ≈ 0:18.95 (alert 19039), półuśmiech ≈ 0:21.2 |
| 4A | 22019–28037 | rx3M13WjFVAZS9Fd32nM | 2,02–8,04 | zacięcie 7,47 → 0:27.47 (alert 27417, +50 ms; koniec pliku nie pozwala wcześniej) |
| 7A | 43024–47513 | JGbdj8Zw8BTanmeafqdQ | 1,50–5,99 | szept pod „Na co grasz?", półuśmiech na końcu |
| 7B | 47513–52002 | zrivtqZhZRRo76t8tjU5 | 1,45–5,94, BEZ flipa | obrót telefonu ≈ 0:48.05 (alert 48050), żetony wchodzą ≈ 0:51.7 |
| 8A | 52002–55501 | 40QM7NMbfufK9mIcYKzk | 4,50–8,00 | traderzy odwracają się ≈ 0:53.5 (pod „Zrealizowane zyski?") |
| 8B | 55501–59010 | 0TxKfcY63L0ma18Xs8xI | 1,70–5,21 | zegarek 3,75 → 0:57.55 (alert 57566) |
| 10B | 68507–74943 | GSu0wP38vIpQQoQoGbb8 | 0,55–6,99 + animacja wyjścia Zanikanie ~0,8 s | tap ≈ 1:13.2–1:14.0, czerń przed 1:15.0 |

## Mechanika (sprawdzona 12 lis, MASTER)
- **NAJPIERW wyłącz „Magnetyczna oś czasu" i „Połączone klipy"** (ikony przy Cofnij/Odtwórz, aria-label). Z włączonymi usunięcie klipu V1 przesuwa WSZYSTKIE ścieżki (tekst, audio) — sprawdzone i cofnięte („Cofnij").
- Usuń stary klip (zaznacz górną częścią klipu → kosz w pasku pod podglądem) → zostaje luka na V1.
- Kursor w miejscu (klik w linijkę + strzałki ←/→ = 1 klatka 33 ms; czas: 0:SS:FF, 30 kl/s) → Biblioteka → Przestrzeń robocza → folder „ZTT — prawdziwy Dorian" → kafelek (img src zawiera ID generacji) → „Dodaj do osi czasu": nowy klip (8,04 s) ląduje na WOLNYM miejscu wyższej ścieżki (V2/nowa), nie na V1.
- Przycięcie: „Podzielony" (nożyczki) w kursorze + usuń zbędny kawałek; albo przeciągnięcie uchwytu krawędzi (element `cursor: ew-resize` tuż za krawędzią klipu, widoczny po zaznaczeniu) — z „Przyciąganiem" krawędź przykleja się do krawędzi sąsiedniego klipu na V1 (dokładnie co do ms). Przesunięcie klipu: syntetyczny drag (pointerdown/move/up) na elemencie `[data-agent-clip-id]` — przykleja się do 0/krawędzi.
- Na V1: ⋮ „Więcej działań" → **„Przesuń do tyłu"** przenosi klip na ścieżkę niżej (V1), bez zmiany czasu.
- Wyciszenie: pasek klipu → Audio → „Wycisz" (switch aria-checked=true).
- Kontrola: `[data-agent-clip-id]` start/end (ms); oś wirtualizowana — czytać przewijając kontener osi.

## Wykonane — MASTER
| Slot | ★ ID | Źródło in–out (s) | Oś (ms) | Uwagi |
|---|---|---|---|---|
| 1A | nloIWPF7hiZKWDSvt15O | 1,933–7,993 | 0–6060 | wyciszony; tap ≈ 0:04.84 (alert 4805); usunięta stara mikro-przerwa 6048–6060 (koniec 1A = start 2A) |
| 2B | E6bjdWZadOXmmMDXnlD5 | 3,750–7,777 | 10060–14087 | wyciszony |
| 3A | oYQuJo03SZO1Ynpxe20b | 4,100–8,005 | 14087–17992 | wyciszony |
| 3B (a) | N8Cf78I97yxs8RGrQMVc | 0,000–2,000 | 17992–19992 | wyciszony; ekran telefonu zapala się ≈ 0:18.95 (alert 19039) |
| 3B (b) | N8Cf78I97yxs8RGrQMVc | 6,000–8,027 | 19992–22019 | wyciszony; półuśmiech ≈ 0:21.2–22.0 → +1 klip na V1 (57 zamiast 56) |
Szybka procedura (JS, skrypty < 20 s): zaznaczenie = syntetyczny klik 6 px od góry klipu (ustawia też kursor w miejscu kliku → „zaznacz w punkcie T" + „Podzielony" = cięcie co do ms); kursor co do ms = syntetyczny klik w klip muzyki A3 w x(T); klik w ikonę „Biblioteka" musi być PRAWDZIWY (JS nie otwiera panelu). Trik: kursor na (start slotu − in źródła) → „Dodaj do osi czasu" → przycięcie lewej krawędzi do startu slotu (przyklejenie) → in źródła wychodzi sam co do ms.
| 4A | rx3M13WjFVAZS9Fd32nM | 2,020–8,038 | 22019–28037 | wyciszony; zacięcie (szarpnięcie) ≈ 0:27.47 (alert 27417, +50 ms — dalej się nie da, koniec pliku 8,04) |
| 7A | JGbdj8Zw8BTanmeafqdQ | 1,500–5,989 | 43024–47513 | wyciszony; szept pod „Na co grasz?", półuśmiech ≈ 0:46.7–47.5 |
| 7B | zrivtqZhZRRo76t8tjU5 | 1,450–5,939 | 47513–52002 | wyciszony; BEZ odbicia (nowy klip, flip domyślnie wył.); obrót telefonu ≈ 0:48.05 |
| 8A | 40QM7NMbfufK9mIcYKzk | 4,500–7,999 | 52002–55501 | wyciszony; traderzy odwracają się ≈ 0:53.5 |
| 8B | 0TxKfcY63L0ma18Xs8xI | 1,700–5,209 | 55501–59010 | wyciszony; zegarek rozbłyska ≈ 0:57.55 (alert 57566) |
| 10B | GSu0wP38vIpQQoQoGbb8 | 0,500–6,989 | 68507–**74996** | wyciszony; Animacja → Animuj wyjście: Zanikanie, Czas trwania 0,8 s (fade 1:14.2–1:15.0); prawa krawędź przykleiła się do startu logo 74996 (było 74943 + 53 ms czerni) = koniec dokładnie 1:15.0. Nowy klip trafił na nową ścieżkę na górze → ⋮ „Przesuń na spód" przeniósł go na V1 (pusta ścieżka zniknęła) |
Po podmianie MASTER: 57 klipów (56 + drugi kawałek 3B); wszystkie audio/tekst/logo bez zmian pozycji i ścieżek (porównanie z odczytem sprzed zmian).
- Kontrola zgrań (podgląd w edytorze): 0:18.96 ekran telefonu zapalony ✔ · 0:27.47 dłoń z zielonym zegarkiem tuż przed szarpnięciem ✔ · 0:48.06 telefon obracany ✔ · 0:57.57 zegarek świeci ✔ · tap 1A ≈ 0:04.84 ✔.
- Po przeładowaniu: 57 klipów, V1 = 0–6060 · 6060–10060 · 10060–14087 · 14087–17992 · 17992–19992 · 19992–22019 · 22019–28037 · … · 66005–68507 · 68507–74996 · logo 74996–78506; audio/tekst identyczne jak przed zmianą; animacja 10B (Zanikanie 0,8 s) zapisana. Podgląd twarzy: 0:16 (3A, pokład, twarz frontalnie), 0:45 (7A, profil 3/4 z kobietą), 1:12 (10B, frontalny portret) — prawdziwy Dorian ✔. Podgląd edytora nie pokazuje animacji wyjścia (do sprawdzenia na eksporcie).
- „Magnetyczna oś czasu" i „Połączone klipy" przywrócone na WŁ. po pracy.
- Eksport MASTER: Eksportuj → Wideo · Wysoka jakość · Cała oś czasu (aria-checked) → render wystartował ~(12 lis).
- **Eksport MASTER zakończony** (~5 min renderu): projekt MASTER → „Eksportuj" → zakładka „Historia" → najnowszy wpis „ZTT — Licencja na zysk — MASTER · MP4" (12 lis, nad dwoma wpisami z 10 lis). NIE pobierano. Karta MASTER zamknięta.

## NAPISY PL (https://elevenlabs.io/app/studio/vh0tGkEI68hZtL4wBVhQ) — stan przed: 67 klipów, V1 identyczne jak stary MASTER; stary 10B bez animacji wyjścia
- W tym projekcie ścieżki tekstu V2–V4 mają podpisy na całej długości → nowy klip ląduje na nowej ścieżce na górze; na V1 przenosi go ⋮ **„Przesuń na spód"** (używać zamiast „Przesuń do tyłu").
- Okno karty niższe (639 px): klik w muzykę A3 do ustawiania kursora trzeba robić w widocznej części klipu (górna część, ok. 12 px nad dolną krawędzią kontenera osi).
| Slot | ★ ID | Źródło in–out (s) | Oś (ms) | Uwagi |
|---|---|---|---|---|
| 1A | nloIWPF7hiZKWDSvt15O | 1,934–7,994 | 0–6060 | wyciszony (in +1 ms vs MASTER) |
| 2B | E6bjdWZadOXmmMDXnlD5 | 3,750–7,777 | 10060–14087 | wyciszony |
| 3A | oYQuJo03SZO1Ynpxe20b | 4,100–8,005 | 14087–17992 | wyciszony |
| 3B (a) | N8Cf78I97yxs8RGrQMVc | 0,000–2,000 | 17992–19992 | wyciszony |
| 3B (b) | N8Cf78I97yxs8RGrQMVc | 6,000–8,027 | 19992–22019 | wyciszony |
| 4A | rx3M13WjFVAZS9Fd32nM | 2,020–8,038 | 22019–28037 | wyciszony |
| 7A | JGbdj8Zw8BTanmeafqdQ | 1,500–5,989 | 43024–47513 | wyciszony |
| 7B | zrivtqZhZRRo76t8tjU5 | 1,450–5,939 | 47513–52002 | wyciszony, bez flipa |
| 8A | 40QM7NMbfufK9mIcYKzk | 4,500–7,999 | 52002–55501 | wyciszony |
| 8B | 0TxKfcY63L0ma18Xs8xI | 1,700–5,209 | 55501–59010 | wyciszony |
| 10B | GSu0wP38vIpQQoQoGbb8 | 0,500–6,989 | 68507–74996 | wyciszony; wyjście Zanikanie 0,8 s |
- Po przeładowaniu NAPISY PL: 68 klipów (67 + kawałek 3B) = 19 wideo + 1 logo + 15 tekstów + 33 audio; 8 ścieżek jak przed; wszystkie teksty i audio na tych samych pozycjach (porównanie start/end z odczytem sprzed zmian). Podgląd 0:16.5 / 0:45 / 1:12 — nowe ujęcia z prawdziwym Dorianem. Przełączniki „Magnetyczna oś czasu"/„Połączone klipy" przywrócone na WŁ.
- **Eksport NAPISY PL zakończony** (~3 min): projekt NAPISY PL → „Eksportuj" → „Historia" → najnowszy wpis „ZTT — Licencja na zysk — NAPISY PL · MP4" (12 lis). NIE pobierano. Karta zamknięta.
- Uwaga środowiskowa: po zamknięciu karty MASTER grupa kart Claude zniknęła; stara karta NAPISY (tabId 974287237) mogła zostać w Chrome POZA grupą (nie dało się jej zamknąć narzędziem) — jeśli jest otwarta, zamknąć ręcznie. Prace dokończone w nowej karcie; stan po przeładowaniu poprawny.

## Wskazówki dla wersji EN (MASTER EN, SUBTITLES EN)
- Te same wycinki i pozycje co wyżej (EN ma identyczną oś obrazu jak PL). Kolejność: wyłącz magnes + połączone klipy → dla każdego slotu: usuń stary → kursor na (start − in) → Dodaj do osi czasu → przytnij L do startu, R do końca (przyklejenie) → Wycisz → ⋮ „Przesuń na spód". 3B: wstaw na 17992, wycisz, podziel w 19992 i 23992, usuń środek, przesuń resztę na 19992, przytnij do 22019. 10B: prawa krawędź przyklei się do 74996 (start logo) + Animacja wyjścia Zanikanie 0,8 s. Na koniec przywróć przełączniki, przeładuj, sprawdź liczbę klipów (+1), eksport „Cała oś czasu".

---
# EN (MASTER EN, SUBTITLES EN) — remontaż 12 lis, agent montażysta EN
## MASTER EN (https://elevenlabs.io/app/studio/piAXMakxMAbxvB9xyPCx)
- Stan przed: 56 klipów; V1 identyczne jak stary MASTER PL (1A 0–6048 … 10B 68507–74943, logo 74996–78506); teksty EN 66014–70014 / 67543–70043 / 2× 75008–78508; VO EN na A1/A2/A4 wg manifest-final.md (sygnatura start–koniec+ścieżka wszystkich 37 klipów nie-wideo zapisana przed zmianą).
| Slot | ★ ID | Źródło in–out (s) | Oś (ms) | Uwagi |
|---|---|---|---|---|
| 1A | nloIWPF7hiZKWDSvt15O | 1,933–7,993 | 0–6060 | wyciszony; dodany na 0, podział 1933, przesunięty na 0, R przyklejony do 6060 |
| 2B | E6bjdWZadOXmmMDXnlD5 | 3,750–7,777 | 10060–14087 | wyciszony |
| 3A | oYQuJo03SZO1Ynpxe20b | 4,100–8,005 | 14087–17992 | wyciszony |
| 3B (a) | N8Cf78I97yxs8RGrQMVc | 0,000–2,000 | 17992–19992 | wyciszony |
| 3B (b) | N8Cf78I97yxs8RGrQMVc | 5,999–8,026 | 19992–22019 | wyciszony (podział wypadł 1 ms wcześniej niż 6,000) |
| 4A | rx3M13WjFVAZS9Fd32nM | 2,020–8,038 | 22019–28037 | wyciszony |
| 7A | JGbdj8Zw8BTanmeafqdQ | 1,501–5,990 | 43024–47513 | wyciszony (in +1 ms) |
| 7B | zrivtqZhZRRo76t8tjU5 | 1,451–5,940 | 47513–52002 | wyciszony; Odwróć w poziomie = WYŁ. (sprawdzone po przeładowaniu) |
| 8A | 40QM7NMbfufK9mIcYKzk | 4,501–8,000 | 52002–55501 | wyciszony (in +1 ms) |
| 8B | 0TxKfcY63L0ma18Xs8xI | 1,701–5,210 | 55501–59010 | wyciszony (in +1 ms) |
| 10B | GSu0wP38vIpQQoQoGbb8 | 0,501–6,990 | 68507–74996 | wyciszony; Animuj wyjście: Zanikanie, 0.8s (sprawdzone po przeładowaniu) |
- Po przeładowaniu: **57 klipów**; V1 = 0–6060 · 6060–10060 · 10060–14087 · 14087–17992 · 17992–19992 · 19992–22019 · 22019–28037 · … · 66005–68507 · 68507–74996 · logo 74996–78506. Wszystkie 37 klipów nie-wideo (VO EN, alerty, SFX, muzyka, teksty, logo) — start/koniec i ścieżka identyczne z odczytem sprzed zmian (porównanie automatyczne: zgodne). Wyciszenie potwierdzone dla wszystkich nowych klipów. Przełączniki „Magnetyczna oś czasu"/„Połączone klipy" przywrócone na WŁ.
- Podgląd: 0:16 (3A, pokład, Dorian w smokingu), 1:12 (10B, frontalny portret) — prawdziwy Dorian ✔.
- Mechanika EN (różnice vs PL): kafelki „Dodaj do osi czasu" pojawiają się dopiero po PRAWDZIWYM najechaniu (hover) na kafelek; panel Biblioteki zastępowany panelem właściwości po zaznaczeniu klipu (trzeba ponownie kliknąć ikonę Biblioteka); filtr „Zasoby" → folder „ZTT — prawdziwy Dorian" (20 pozycji). „Podzielony" nie dzieli < ~50 ms od krawędzi → końcówki 4–43 ms przycinane uchwytem z przyklejeniem (drag z „rozbiegiem" 25 px). Suwak czasu animacji: prawdziwy klik w pozycję 0.8 (lub ←/→ krok 0,1 — ale popover się zamyka po każdym kroku). Raz usunięcie zaraz po podziale skasowało zły kawałek — cofnięte „Cofnij", powtórzone z dłuższym odczekaniem.
- Eksport MASTER EN: Eksportuj → Wideo · Wysoka jakość (najwyższa dostępna; druga opcja to „Szybki eksport") · Cała oś czasu → render wystartował.
- **Eksport MASTER EN zakończony**: projekt MASTER EN → „Eksportuj" → „Historia" → najnowszy wpis „ZTT — License to Profit — MASTER EN · MP4" (12 lis, nad wpisem z 10 lis). NIE pobierano.

## SUBTITLES EN (https://elevenlabs.io/app/studio/kSWZiRAgS9pjgiuwt2gy)
- Stan przed: 67 klipów (19 wideo/obraz, 15 tekstów na V2–V4, 33 audio); V1 jak stary MASTER; sygnatura wszystkich klipów nie-wideo zapisana.
- Podmiany IDENTYCZNE jak w MASTER EN (te same ID, wycinki i pozycje z tabeli wyżej, w tym 3B (b) 5,999–8,026 i +1 ms in dla 7A/7B/8A/8B/10B; 1A 1,933–7,993). Nowe klipy lądowały na nowej ścieżce na górze → ⋮ „Przesuń na spód" na V1. Wszystkie wyciszone; 7B bez odbicia; 10B Zanikanie 0.8s.
- Po przeładowaniu: **68 klipów**; V1 = 0–6060 · 6060–10060 · 10060–14087 · 14087–17992 · 17992–19992 · 19992–22019 · 22019–28037 · … · 68507–74996 · logo 74996–78506. Wszystkie 48 klipów nie-wideo (11 podpisów EN + 4 tytuły, VO EN, alerty, SFX, muzyka, logo) — pozycje i ścieżki identyczne z odczytem sprzed zmian (porównanie automatyczne: zgodne). Wyciszenie 11 nowych klipów, flip 7B = wył., animacja 10B = Zanikanie 0.8s — potwierdzone po przeładowaniu. Przełączniki przywrócone na WŁ.
- Podgląd: 0:16 (3A, pokład), 1:12 (10B, frontalny portret, podpis EN widoczny) — prawdziwy Dorian ✔.
- Okno karty 639 px: lista Biblioteki ma tylko ~56 px wysokości, kafelek trzeba przewinąć skryptem i najechać prawdziwym hoverem (y ≈ 245). Pierwszy odczyt listy zaraz po otwarciu Biblioteki zwraca pustkę — drugi działa.
- **Eksport SUBTITLES EN zakończony** (~2 min): Wideo · Wysoka jakość · Cała oś czasu → „Eksportuj" → „Historia" → najnowszy wpis „ZTT — License to Profit — SUBTITLES EN · MP4" (12 lis). NIE pobierano.
- Odchyłki EN vs wzorzec PL: in-pointy ±1 ms (dodanie w kursorze wypadło 1 ms wcześniej dla 7A/7B/8A/8B/10B; podział 3B w 23991 zamiast 23992). Pozycje na osi co do ms zgodne z PL.
- Środowisko: karta MASTER EN w trakcie renderu zmieniła ID (974287241 → 974287244) i przestała odpowiadać na skrypty; zamknięta, eksport sprawdzony po ponownym otwarciu projektu (jedna karta na projekt naraz). Wszystkie karty agenta zamknięte.

---
# SHORTY 9:16 — remontaż 12 lis (agent montażysta 9:16)
Projekty: SHORT PL https://elevenlabs.io/app/studio/XduwSmt6zo2EmQkCTTeJ · SHORT EN https://elevenlabs.io/app/studio/hRMymJzfGChQAQjI3FJl
Stan przed (PL): 32 klipy (8 wideo V1, 7 tekstów, 1 logo, 16 audio) — dokładnie jak w manifest-short.md.

## Analiza źródeł w podglądzie edytora (czasy w s źródła / na osi)
- 1A eS3t…: palec uniesiony ~6,5; **pierścień tapu pojawia się ≈ 6,93–6,96** → przy in 5,0 = 0:01.93–0:01.96.
- 4A h2PC…: zegarek z wykresem ok. 5,0; spławik ~6,4; **zanurzenie + pierwsze krople ≈ 6,9–6,97** (0:09.9–0:09.97), pełny słup rozprysku 7,05–7,5 (0:10.05–0:10.5).
- 7B UUmf…: rękawiczka krupiera wchodzi z prawej ≈ 5,6; **stos żetonów dosunięty ≈ 5,8–6,0** (0:17.3–0:17.5), dalej statycznie.
- 10B vHXk…: 0–0,9 od tyłu, obrót 0,9–1,7, frontalnie 1,7–5,3, nadgarstek/zegarek 5,7–7,5; **twarde cięcie do czerni ≈ 7,6–7,7** (nie wygaszenie) → w montażu Zanikanie.

## Wykonane — SHORT PL (V1; wszystkie nowe klipy wyciszone; 7B bez flipa)
| Slot | ★ ID | Źródło in–out (s) | Oś (ms) | Uwagi |
|---|---|---|---|---|
| 1A | eS3t2ntSFOn1u39H4skX | 5,000–8,000 | 0–3000 | tap ≈ 0:01.95 |
| 2B (a) | myAhBZZta9VmpQRgT2Ww | 0,500–2,696 | 3000–5196 | rozpinanie pianki |
| 2B (b) | myAhBZZta9VmpQRgT2Ww | 5,500–7,300 | 5196–6996 | smoking, mankiet, tarcza zielona (bez „morphu" 3,5–4,5) |
| 4A | h2PCZzju3v4nDRZsT88X | 3,700–8,009 | 6996–11305 | rozprysk ≈ 0:09.95 |
| 7A | mJxdfuUJ3GdkyCv9gc1e | 3,500–7,197 | 11305–15002 | szept → półuśmiech |
| 7B | UUmfIyBX3mDCthCRBInH | 3,500–7,607 | 15002–19109 | żetony ≈ 0:17.3–17.5 |
| 10B | vHXkX7i3HarOZnQY5Tk0 | 0,478–7,104 | 21990–28616 | Animuj wyjście: Zanikanie 0,8 s (28,6 = czerń przed kartą; źródło tnie do czerni twardo ≈ 7,6) |
9A (19109–21990) bez zmian. Cięcie do 10B = 21990 (jak dotąd, 10 ms przed 0:22.0; klatka 660 = już 10B), koniec 10B = 28616 (0:28.6).

## Przesunięte klipy audio (tylko te; reszta bez zmian — porównanie start/koniec wszystkich klipów przed/po)
| Klip | Było (ms) | Jest (ms) | Ścieżka | Uwagi |
|---|---|---|---|---|
| ALERT master (pierwszy) | 1813–2700 | **1967–2854** | A2 | pod tap 1A (≈ 0:01.95) |
| SFX plusk | 10817–12005 | **9934–11122** | A3 | pod zanurzenie/rozprysk 4A (≈ 0:09.95); 45 %, zanik 0,3 s bez zmian |
| SFX żetony | 16492–19107 | **17298–19109** | A4 | pod dosunięcie żetonów (≈ 0:17.3; podgląd pokazał żetony wcześniej niż szacunek 0:18.0 z contact sheet); koniec ponownie przycięty na cięciu do 9A (jak w oryginale), 45 %, zanik 0,3 s |

## Mechanika 9:16 (różnice vs 16:9)
- Wyłączone „Magnetyczna oś czasu" + „Połączone klipy" na czas pracy, po pracy WŁ. (sprawdzone po przeładowaniu).
- Nowy klip (8,04 s) ląduje na V3 (obok tytułu/logo) albo na nowej ścieżce na górze → ⋮ „Przesuń na spód" (menu ⋮ otwiera tylko PRAWDZIWY klik; pozycję menu klikamy JS-em).
- Kursor co do ms: syntetyczny klik w klip muzyki A1 w x(T). Podział „Podzielony" bywa ±1 ms. Przycinanie krawędzi z „Przyciąganiem" może przykleić się do sąsiedniego klipu audio (4A przykleił się do 11292 = start ruletki) → przycinać z WYŁ. przyciąganiem i ułamkowym x (≈ 26 px/s, wynik co do ms).
- Przesuwanie klipów audio: syntetyczny drag z „rozbiegiem" (próg ~4 px), dokładność ±25 ms.
- Po przeładowaniu SHORT PL: **32 klipy** (8 wideo, 7 tekstów, 1 logo, 16 audio — liczba bez zmian, 2B nadal z 2 kawałków); V1 = 0–3000 · 3000–5196 · 5196–6996 · 6996–11305 · 11305–15002 · 15002–19109 · 19109–21990 · 21990–28616; teksty, logo, muzyka, VO, pozostałe alerty/SFX — start/koniec identyczne jak przed (porównanie automatyczne), różnią się tylko 3 przesunięte klipy audio. Wyciszenie wszystkich klipów V1 i Zanikanie 0.8s na 10B potwierdzone po przeładowaniu. Przełączniki WŁ.
- Podgląd twarzy: 0:13 (7A, kobieta szepcze, Dorian 3/4) · 0:25 (10B, frontalny portret nad nocnym miastem) — prawdziwy Dorian ✔.
- **Eksport SHORT PL zakończony** (~2 min): Wideo · Wysoka jakość · Cała oś czasu → ✓ „ZTT — SHORT 9x16 — PL · MP4" (Eksportuj → Historia, 12 lis). NIE pobierano.

## SHORT EN — identycznie jak PL
- Stan przed: 32 klipy, V1 jak stary PL; VO EN 7181–10969 (A4) / 11790–14559 / 15323–18405 / 23003–28254 (A4), teksty EN wg manifest-short.md — sygnatura zapisana przed zmianą.
- V1: te same ID, wycinki i pozycje co PL (1A 5,000–8,000; 2B 0,500–2,696 + 5,500–7,300; 4A 3,700–8,009; 7A 3,500–7,197; 7B 3,500–7,607; 10B 0,478–7,104 + Zanikanie 0.8s), wszystkie wyciszone.
- Audio przesunięte identycznie: ALERT 1813→**1967**, plusk 10817→**9934**, żetony 16492→**17298–19109** (45 %, zanik 0,3 s zachowane).
- Po przeładowaniu: **32 klipy**; poza 3 przesuniętymi klipami audio wszystkie klipy nie-wideo (VO EN, teksty EN, logo, muzyka, alerty, SFX) na tych samych pozycjach; wyciszenie V1 + Zanikanie 10B potwierdzone; przełączniki WŁ. Podgląd 0:13 / 0:25 — prawdziwy Dorian ✔.
- **Eksport SHORT EN zakończony** (~1,5 min): Wideo · Wysoka jakość · Cała oś czasu → ✓ „ZTT — SHORT 9x16 — EN · MP4" (Historia, 12 lis). NIE pobierano. Karta agenta zamknięta.

## Do sprawdzenia przez człowieka
- Zgranie SFX na eksporcie (plusk 0:09.93, żetony 0:17.3, alert 0:01.97) — w SFX plusk/żetony zdarzenie zakładane na początku pliku (jak w oryginalnej układance).
- 10B: Zanikanie 0.8s (0:27.8–0:28.6) nachodzi na końcówkę gestu z zegarkiem; podgląd edytora nie pokazuje animacji wyjścia.
