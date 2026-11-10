# MANIFEST WIDEO PIONOWE 9:16 — SHORT 32 s (1A, 2B, 4A, 7A, 7B, 9A, 10B)
Data: 2026-11-10 · agent „wideo vertical"
Narzędzie: ElevenLabs → Obraz i wideo → Historia (`https://elevenlabs.io/app/image-video/history?modality=video`), sekcja **„10 lis"**.
Wszystkie: 9:16 · 1080p · 8 s · audio WŁ. (bez mowy). Godziny = UTC.
Koszt jednostkowy (podpowiedź przy „Pozostało N"): Seedance 2.5 9:16 1080p 8 s = **50 121 kr.** („81 wideo left in your plan" ≈ 4,06 mln kr. salda).
Każdy prompt = sprawdzony prompt 16:9 (odtworzony z Historii przez „Więcej opcji → Odtwórz", razem z referencjami) + na początku:
`Vertical 9:16 composition, subject and key action centered in the middle of the frame, keep the top 12% and bottom 20% of the frame free of faces, hands and screens.`
Szukaj wszystkich: pole „Szukaj generacji…" → `Vertical 9:16 composition`.

## Generacje (przyrostowo)
| # | Ujęcie | Model | Refy | Liczba | Start (UTC) | Szukaj (fragment prompta) | Koszt |
|---|---|---|---|---|---|---|---|
| V1 | 1A | Seedance 2.5 | REF_DORIAN_SILHOUETTE #4 (@Image 1) | 1 | 01:26 | `Vertical 9:16` + `spiraling like an abstract vortex` | 50 121 |
| V2 | 2B | Seedance 2.5 | awatar Headshot (@Image 1) + REF_ZTT_UI #4 (@Image 2) | 1 | 01:28:05 | `Vertical 9:16` + `no cap in this shot (wet short dark brown hair)` | 50 121 |
| V3 | 4A | Seedance 2.5 | awatar Headshot (@Image 1) + REF_ZTT_UI #4 (@Image 2) | 1 | 01:28:34 | `Vertical 9:16` + `seated on a wooden jetty with a fishing rod` | 50 121 |
| V4 | 7A | Seedance 2.5 | awatar Headshot (@Image 1) + REF_FEMME #3 (@Image 2) | 1 | 01:33:08 | `Vertical 9:16` + `softly whispers a question with a knowing smile` | 50 121 |
| V5 | 7B | Seedance 2.5 | REF_DORIAN_JAW #2 (@Image 1) + REF_FEMME #3 (@Image 2) + REF_ZTT_UI #4 (@Image 3) | 1 | 01:33:35 | `Vertical 9:16` + `the top edge of the frame cuts across his nose, his eyes and cap` | 50 121 |
| V6 | 10B | Seedance 2.5 | REF_DORIAN_HERO r2 #2 (@Image 1) + awatar Headshot (@Image 2) | 2 (jedna grupa, 2 kafelki) | 01:34:02 | `Vertical 9:16` + `His face looks exactly like @Image 1` | 100 242 |
| V7 | 9A | **Veo 3.1** | brak (jak 16:9) | 1 | 01:36:54 | `Vertical 9:16` + `High wide crane shot over a packed conference hall` | 19 391 |

Wszystkie 8 klipów: status completed, 1080×1920, 8,06 s (Veo 8,00 s), has_audio = true. Brak nieudanych generacji.

## !!! WAŻNE — BRAK OCENY WIZUALNEJ (do zrobienia przez człowieka / następnego agenta)
Okno Chrome było przez całą sesję **zminimalizowane** (screenX = −32000, viewport 0×0) → każdy zrzut ekranu kończył się timeoutem CDP
(`Page.captureScreenshot timed out`), `resize_window` nie przywraca okna, a filtr narzędzia blokuje przekazanie pikseli z canvas (base64).
Nie widziałem ANI JEDNEJ klatki. **Nie oceniono:** podobieństwa do Doriana, czapki/emblematu, strony nadgarstka, bełkotu tekstowego, kadrowania/safe area.
Dlatego: (a) ★ poniżej są **PROWIZORYCZNE** (jedyna generacja danego ujęcia), (b) nie robiłem dodatkowych prób (nie da się stwierdzić „słabe"), (c) 10B — zapisane OBA warianty, ★ do wyboru okiem.
Jedyna „ocena" to liczby policzone w przeglądarce z podglądu (co 0,5 s: średnia jasność, % zielonych pikseli, % pikseli w tonie skóry) — dają cięcia montażowe i wygaszenia, nic o jakości.

## Klipy (Historia „10 lis", szukaj `Vertical 9:16 composition`; kolejność od góry = od najnowszego)
| Ujęcie | ID generacji | Start→gotowe (UTC) | Status ★ | Co wynika z liczb (NIE z obrazu) | Sugerowany wycinek pod SHORT-EDL (do weryfikacji okiem) |
|---|---|---|---|---|---|
| 9A | `jj3bweL1jm8LHlGXcCy8` (Veo) | 01:36:56→01:38:57 | ★ prowiz. | ciemna hala 0–1,5 s; zieleń narasta 1,75→3,25 s (3%→32% kadru), potem stabilnie ~38–42% do końca; rozbłysk raczej narastający niż „w jednej klatce" | 3 s: ~1,5–4,5 s (rozbłysk ~0,3 s po cięciu) |
| 10B wariant A | `xpL3rppnEkik17j7iHU0` (pierwszy kafelek grupy) | 01:34:03→01:41:19 | do wyboru | jasność i udział skóry rosną płynnie (najazd na twarz) do ~6,25 s; czerń od ~6,5–6,75 s | 6,6 s: 0,2–6,8 s (+ dociągnąć czerń stopklatką) |
| 10B wariant B | `fIbjaPmu9GY74KgwnsNp` (drugi kafelek grupy) | 01:34:03→01:38:06 | do wyboru (liczbowo lepszy: dłuższa akcja, bliższy plan twarzy — skóra do 21% kadru) | najazd do ~6,75 s; czerń od ~7,0 s | 6,6 s: 0,6–7,2 s |
| 7B | `N6rM2l2aqSRJwvDWl2Pz` | 01:33:35→01:37:36 | ★ prowiz. | jedno ujęcie bez cięć; dół kadru mocno jaśnieje 3,5–5,5 s (ekran telefonu / żetony wchodzą w dolną część — sprawdzić safe area dolne 20%) | 4 s: ~3,0–7,0 s |
| 7A | `U8aA3q4OuGt6G02dDgz9` | 01:33:08→01:37:12 | ★ prowiz. | statyczne, równe ujęcie bez cięć, brak zieleni | 3,7 s: ~1,5–5,2 s (dobrać po ruchu ust kobiety) |
| 4A | `Pvc07XunxfzHfo5tKNYk` | 01:28:34→01:32:28 | ★ prowiz. | 0–3,5 s jasny szeroki kadr (świt, mgła), cięcie ~3,5 s na insert; zielona poświata śladowa (≤1%) — sprawdzić, czy zegarek w ogóle świeci | 4,3 s: ~3,5–7,8 s (zacięcie przy końcu) lub 2,0–3,5 + 5,0–7,8 |
| 2B | `594UvUVwcTmHd0aqGmmc` | 01:28:05→01:32:18 | ★ prowiz. | 0–2,5 s ciemno, jasna strefa u GÓRY kadru (księżyc/niebo — górne 12%); przejście ~2,75–3,25 s, potem stabilny plan; zieleń ≤1% | 4 s: ~3,0–7,0 s |
| 1A | `jYxpZaD2EDwDt9WrL1Tm` | 01:26:54→01:30:17 | ★ prowiz. | zielony tunel 0–5 s (11–16% kadru), po ~5,5 s zieleń gaśnie i od ~6,75 s pojawia się skóra (bohater bliżej/frontalnie) — jak w 16:9, tap najpewniej ~5,5–7 s, NIE na początku | 3 s: ~4,8–7,8 s (tap ~1,5 s po cięciu — potwierdzić okiem) |

## Zapisane do Zasoby → NOWY folder **„ZTT Short - wideo 9x16"** (utworzony 10 lis; 8 plików, komunikat „Zapisano do zasobów" przy każdym)
1A, 2B, 4A, 7A, 7B, 9A oraz OBA warianty 10B. Nazwy auto (`video_seedance-2-5_Vertical 9:1..._2026-11-10T01:..` / `video_veo-3-1_...`); rozróżniać po miniaturze i godzinie.

## KOSZTY
Seedance 2.5: 7 klipów × 50 121 = 350 847 kr. (1A, 2B, 4A, 7A, 7B, 10B ×2) + Veo 3.1: 19 391 → **≈ 370 238 kr.** (budżet 550 000; pojedyncza generacja max 100 242 = 10B ×2; saldo przed startem ≈ 4,06 mln).
Niewykorzystane ~180 000 kr. zostawione na ewentualne powtórki po obejrzeniu.

## UWAGI TECHNICZNE (dla następnego agenta)
- **„Więcej opcji → Odtwórz"** na kafelku wideo w Historii ładuje do kompozytora prompt + referencje + model + ustawienia tej generacji (nic nie generuje). Potem wystarczy zmienić proporcje i dopisać prefiks. Uwaga: przy 1A pierwszy kafelek wyników to zapas Veo — brać kafelek Seedance.
- Praca w 100% przez DOM/JS działa także przy zminimalizowanym oknie: menu Radix otwiera `pointerdown`; listy wyboru w „Ustawieniach modelu" — klik w combobox, potem klik + Enter na `[role=option]`; tekst na początek prompta — zakres na początku `.ProseMirror` + `execCommand('insertText')`.
- Dane generacji (id, status, file_properties, adresy podglądu) są w propsach Reacta kafelka (`asset.generation`).
- Statusy „Prawie gotowe…" odświeża ponowne wpisanie frazy w wyszukiwarkę (bez przeładowania strony, kompozytor się nie resetuje).
- Podpowiedź kosztu przy „Pozostało N" pojawia się na `pointerenter`/`mouseover`; dla Veo nie pokazała się drugi raz — koszt 19 391 przyjęty z „Pozostało 203" (≈ saldo/203) i manifestu B.
- Kompozytor zostawiony pusty (Veo 3.1, 9:16, 1080p, 8 s). Karta zamknięta.

---

## OCENA I ★ (kontrola jakości okiem — 10 lis, agent „reżyser/QC"; zastępuje „★ prowiz." i sugerowane wycinki z tabeli wyżej)
Metoda: contact sheet (6 klatek/klip: 0,5 / 2 / 3,5 / 5 / 6,5 / 7,7 s + dogęszczenia przy akcji, powiększenia 4 klatek), porównanie 10B z REF_DORIAN_HERO r2 #2.
Wszystkie ★ leżą w Zasobach → „ZTT Short - wideo 9x16" (teraz 10 plików: 8 starych + 2 powtórki). Czasy wycinków = sekundy ŹRÓDŁA.

| Ujęcie (czas w EDL) | ★ (ID · jak rozpoznać) | Wycinek [s] | Uwagi |
|---|---|---|---|
| 1A tunel (3,0 s) | `jYxpZaD2EDwDt9WrL1Tm` · prompt `Vertical 9:16 composition, subject and key action…` + `spiraling like an abstract vortex` · miniatura: zielony spiralny tunel | **5,3–8,06** (2,76 s) + stopklatka ostatniej klatki ~0,25 s → tap dokładnie 0:01.5. Alternatywa bez stopklatki: 5,0–8,0 (tap ~0:01.8 → przesuń ALERT z 0:01.5 na 0:01.8) | Sylwetka w tunelu, twarz w cieniu ✔, czapka w konturze ✔. Ręka idzie w górę 5,8 s, palec w kamerę 6,2–6,6, **tap (fala) ≈ 6,8 s**, rosnąca linia ze strzałką 7,2–8,0. Zegarek na lewym ✔. Bez tekstu. Strzałka sięga górnych ~12% (nie twarz/ekran — OK). |
| 2B pianka→smoking (4,0 s) | **POWTÓRKA** `Afu8F5V9FTR4tvudebOw` (03:02 UTC) · prompt zaczyna się `Vertical 9:16 composition. Headless framing: tight medium shot at chest height` (szukaj `Headless framing`) · miniatura: tors w piance, kadr ucięty pod nosem | **0,3–2,5** (2,2 s: rozpięcie, zamek ~1,0 s po cięciu = SFX 0:04.0) **+ 5,95–7,75** (1,8 s: mankiet → tarcza zapala się na zielono ≈ 6,4 s źródła = 0:05.6, pod Quiet 0:05.5). Jednym ujęciem: 0,4–6,8 przyspieszone ×1,6 | Kadr przez cały klip poniżej nosa ✔ (oczu nigdy nie widać), pianka gładka bez napisów ✔, smoking + mucha + poszetka ✔, zegarek na LEWYM ✔, dłonie czyste ✔, brak tekstu ✔. Uwaga: tarcza zegarka dość duża w kadrze (chronograf „w typie" luksusowej marki) — nie powiększać w montażu. |
| ~~2B pierwsza wersja~~ | `594UvUVwcTmHd0aqGmmc` · `no cap in this shot (wet short dark brown hair)` | ODRZUT | Od ~4,3 s pełna, oświetlona twarz frontalnie (spoiler finału), długie zaczesane włosy niepodobne do Doriana, bełkot liter na piance („…RG"), twarz w górnych 12%, UI jako hologram na piersi. |
| 4A ryby (4,3 s) | `Pvc07XunxfzHfo5tKNYk` · `seated on a wooden jetty with a fishing rod` · miniatura: jasny świt, sylwetka na pomoście + czerwony spławik | **2,2–6,5** (zacięcie ≈ 6,0 s źródła = 0:10.8 ✔) | 0–3,5 szeroki plan z odbiciem, ~3,5 s cięcie wewnętrzne na bliższy plan, zegarek zapala się ~4,2 s (lewy ✔), spławik znika 5,8, **podcięcie wędki 5,9–6,1**, plusk do 7,7. Twarz zasłonięta daszkiem ✔, czapka czarna z ciemnozielonym emblematem ✔. Nad zegarkiem drobny hologram z mikro-znaczkami (nieczytelne, akceptowalne). Spławik/plusk w dolnych 20% — to nie twarz/ekran, OK. |
| 7A kasyno (3,7 s) | `U8aA3q4OuGt6G02dDgz9` · `softly whispers a question with a knowing smile` · miniatura: ruletka na dole, kobieta w czarnej sukni z kieliszkiem, bohater w czapce | **1,5–5,2** (pochylenie 1,5–3,5, szept przy uchu 3,5–5,2; FF „Na co grasz?" 0:11.8 = 2,0 s źródła) | Bohater patrzy w dół — oczy pod daszkiem, widać tylko profil nosa/ust ✔; czapka czarna, mały cyjanowy emblemat ✔; zegarek na nadgarstku przy lewej krawędzi — najpewniej lewa ręka (skrzyżowane przedramiona), bez zastrzeżeń. Kobieta zgodna z REF_FEMME, twarze i dłonie czyste, brak tekstu. |
| 7B telefon + żetony (4,0 s) | **POWTÓRKA** `r7QcMceVsmI7AE77tKub` (03:04 UTC) · prompt zaczyna się `Vertical 9:16 composition, key action centered in the middle of the frame, keep the bottom 20%` (szukaj `no floating head`) · miniatura: smoking od nosa w dół, kobieta przy prawym ramieniu, telefon z zielonym wykresem, żyrandol | **4,0–8,0** (telefon już w górze, rękawiczki krupiera wjeżdżają ~5,0, stos żetonów stoi 6,0 = SFX żetony 0:16.5–0:17.0). Wariant z obrotem telefonu: 1,0–2,5 + 5,0–7,5 | Poprawna przestrzeń: kobieta OBOK (prawa strona kadru), pochylona do ramienia ✔; kadr przez nos ✔; ekran: wykres świecowy + „ZTT" ✔ (mikro-napis na przycisku nieczytelny); telefon w środkowej strefie ✔; zegarek widoczny tylko 0,5–1,2 s (strona niejednoznaczna — poza wycinkiem). Twarz kobiety częściowo w górnych 12% i przy 6,8 s lekko ucięta prawą krawędzią — akceptowalne. |
| ~~7B pierwsza wersja~~ | `N6rM2l2aqSRJwvDWl2Pz` · `the top edge of the frame cuts across his nose, his eyes and cap` | ODRZUT | Głowa kobiety „wklejona" w klatkę piersiową bohatera (niemożliwa przestrzeń), przy 6,5 s zdeformowana twarz kobiety, żetony zasłaniają dół kadru. |
| 9A morze telefonów (3,0 s) | `jj3bweL1jm8LHlGXcCy8` (Veo 3.1) · `High wide crane shot over a packed conference hall` · miniatura: tłum w zielonym świetle, reflektor u góry | **1,6–4,6** (pierwsze zielone ekrany od razu, fala rozbłysku 1,9–2,6 = 0:19.3–0:20.0) | Ciemna sala → fala zielonych telefonów → cała sala zielona; rozbłysk narasta ~0,7 s (nie jedna klatka). Brak czytelnego tekstu (identyfikatory/telebim u góry bez liter). Twarze tłumu drobne, bez rażących deformacji. Telebim w górnych 12% — tło, OK. |
| 10B FINAŁ (6,6 s) | **★ wariant A** `xpL3rppnEkik17j7iHU0` (PIERWSZY kafelek grupy 01:34) · `His face looks exactly like @Image 1` · miniatura: plan średni, cała sylwetka od tyłu na tarasie; w końcówce pozioma ręka z zielono świecącym zegarkiem | **0,15–6,75** (od tyłu 0,15 → obrót 1,0–2,7 → spojrzenie + półuśmiech 2,7–5,6 → tap 6,0–6,6 → twarde wejście czerni ≈ 6,75 = 0:28.6) | Podobieństwo do REF_DORIAN_HERO bardzo dobre (jasne oczy, zarost, owal, półuśmiech), mimika naturalna; czapka czarna z małym cyjanowym emblematem ✔ bez Ferrari; **pełna akcja: obrót + prawdziwy tap prawym palcem w zegarek na LEWYM nadgarstku + zielony rozbłysk + czerń** ✔; twarz i zegarek w środkowej strefie ✔; brak tekstu. |
| 10B wariant B (zapas) | `fIbjaPmu9GY74KgwnsNp` (drugi kafelek) · miniatura: ciasne zbliżenie twarzy, pięść z zegarkiem na dole | zapas: 0,6–7,2 | Twarz równie podobna i ładniej oświetlona, ale: brak tapnięcia (pięść, zegarek zapala się sam), twarz ucięta prawą krawędzią i daszek w górnych 12%, zegarek w dolnych 20% (pod UI), makro na tarczę chronografu (ryzyko skojarzenia z marką), emblemat duży. Tylko jako wstawka zbliżenia 3,5–5,5 s, jeśli montaż będzie chciał. |

### Powtórki (2 × Seedance 2.5, 9:16, 1080p, 8 s, audio wł.; te same referencje co oryginały przez „Odtwórz")
- **2B r2** — poprawki prompta: „Headless framing… top edge of the frame cuts just below his nose for the whole shot… camera locked at chest height, never tilts up", pianka „plain matte black, no text, no logos", akcja rozpisana (zamek w pierwszych 2 s → lewy mankiet → tarcza świeci, „no floating hologram"), negatywy „no eyes visible, no full face, no long hair".
- **7B r2** — poprawki: „Physically correct staging with clear depth: the man sits in the center… the woman sits right NEXT to him, shoulder to shoulder… never in front of him, her head never overlaps his chest", telefon odwracany do kamery w środku kadru, żetony „stopping beside the phone without covering it", negatywy „no overlapping heads, no floating head, no merged bodies, no distorted female face".
- Koszt powtórek: 2 × 50 121 = **100 242 kr.** (limit 180 000). Łącznie pion: ≈ 470 480 kr. Bez nieudanych generacji. 10B, 1A, 4A, 7A, 9A — bez powtórek (używalne).
- Zapis: oba przez „Więcej opcji → Zapisz do zasobów" → folder „ZTT Short - wideo 9x16" (komunikat „Zapisano do zasobów" ×2). Odrzutów z folderu NIE usuwałem — w folderze są też stare 2B (01:28) i 7B (01:33) oraz 10B wariant B; brać pliki z godziną **03:02 (2B)** i **03:04 (7B)**.

### Uwagi do SHORT-EDL
- 1A: tap jest pod koniec źródła (6,8 s) — stąd stopklatka 0,25 s albo przesunięcie ALERTU na 0:01.8.
- 2B: ujęcie składane z dwóch kawałków (skok w ruchu maskuje cięcie na akcji: rozchylona pianka → mankiet).
- 9A: rozbłysk to fala ~0,7 s; ALERT 0:19.3 trafia w jej początek.
- Technika: po zmianie wysokości okna (pasek u góry) współrzędne kliknięć się rozjeżdżają — menu kafelka pewniej otwierać z DOM (`pointerdown` na przycisku „Więcej opcji" przy kafelku, potem `click()` na `[role=menuitem]`). Kompozytor zostawiony pusty, karta zamknięta.
