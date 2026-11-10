# MANIFEST WIDEO — BOHATER = DORIAN — część 2 (7A, 7B, 8A, 8B, 10A, 10B)
Data: 2026-11-09 · agent wideo „Dorian część 2"
Narzędzie: ElevenLabs → Obraz i wideo → Historia (`https://elevenlabs.io/app/image-video/history?modality=video`), sekcja „9 lis".
Domyślnie: Seedance 2.5, 16:9 · 1080p · 8 s · audio WŁ. Godziny = UTC.
Prompty: bloki z video-prompts-expanded.md, stary opis bohatera → CHARACTER BLOCK v2 + linia o ukrytej twarzy (10B: odsłonięta);
na początku „The man is @Image 1 (keep his exact face)."; w negatywach „no Ferrari logo, no red cap, no other brand logos, no headphones, no microphone, watch on his LEFT wrist".
Z promptów usunięto mówienie (7B „he speaks one calm line", 8A „asks one short question").

## Generacje (przyrostowo)
| # | Ujęcie | Model | Refy | Liczba | Start (UTC) | Szukaj (fragment prompta) | Koszt |
|---|---|---|---|---|---|---|---|
| G1 | 7A | Seedance 2.5 | awatar Headshot (@Image 1) + REF_FEMME #3 (@Image 2) | 1 | 18:38 | `softly whispers a question with a knowing smile` | 50 121 |
| G2 | 7B | Seedance 2.5 | REF_DORIAN_JAW #2 (@Image 1) + REF_FEMME #3 (@Image 2) + REF_ZTT_UI #4 (@Image 3) | 1 | 18:40 | `the top edge of the frame cuts across his nose, his eyes and cap` | 50 121 |
| G3 | 8A | Seedance 2.5 | awatar Headshot (@Image 1) + REF_DORIAN_SILHOUETTE #4 (@Image 2) | 1 | 18:42 | `his back to the camera. [Scene/lighting] Night interior` | 50 121 |
| G4 | 8B | Seedance 2.5 | awatar Headshot (@Image 1) + REF_ZTT_UI #4 (@Image 2) | 1 | 18:44 | `raising his LEFT wrist and glancing at his steel chronograph` | 50 121 |
| G5 | 10A | Seedance 2.5 | REF_DORIAN_SILHOUETTE #4 (@Image 1) | 2 | 18:49 | `the man never turns around` | 100 241 |
| G6 | 10B | Seedance 2.5 | REF_DORIAN_HERO r2 #2 (@Image 1, dodany z miniatury referencji przy JAW) + awatar Headshot (@Image 2) | 3 | 18:57 | `His face looks exactly like @Image 1` | 150 363 |
| G7 | 8A (próba 2) | **Veo 3.1** | REF_DORIAN_SILHOUETTE #4 (@Image 1) + awatar Headshot (@Image 2) | 1 | 19:05 | `the man always wears the black baseball cap` | 19 391 |

## Oceny (klatki ~0,5 / 3,0 / 5,5 / 7,8 s)
- **7A G1:** kasyno, ruletka na 1. planie, Dorian w CZARNEJ czapce z małą zielono-cyjanową emblemą, siedzi przy stole w 3/4 z boku, wzrok w dół, oczy w cieniu daszka; kobieta w czarnej sukni (zgodna z REF_FEMME) pochyla się do jego ramienia z kieliszkiem i szepcze, półuśmiech. Szczęka/zarost zgodne. Zegarek widoczny przy splecionych dłoniach — strona nadgarstka niejednoznaczna (raczej prawy). **★ 7A**, całość lub 2–8 s. Zapisane do folderu.
- **7B G2:** kadr poniżej oczu (usta/zarost, półuśmiech), dłoń odwraca telefon z zielonymi świecami (bez napisów), krupier w białych rękawiczkach przesuwa wieżę żetonów, kobieta w tle (brew słabo zaznaczona). Zegarek na PRAWYM nadgarstku (ręka wchodzi z lewej, bohater przodem) → w montażu można odbić poziomo (brak czytelnych napisów; w tle rozmyte szyldy automatów). Tarcza zegarka przypomina luksusowy chronograf — bez makro. **★ 7B**, całość. Zapisane.
- **8A G3:** steadicam od tyłu → szeroki kadr willi z monitorami i czwórką traderów, nocne miasto za oknami. Bohater cały czas tyłem ✔, ALE czapka nieczytelna — sylwetka głowy wygląda na krótkie włosy (brak daszka w konturze). Traderzy słabo odwracają głowy. → zapas; próba 2 (Veo 3.1, tańsza) — patrz niżej.
- **8B G4:** monitor z zieloną UI („ZTT” u góry ✔ + drobne pseudo-etykiety na dole), Dorian w czapce za monitorem — 0–3 s twarz widoczna frontalnie (mała, oczy spuszczone) ✗; ~5 s podnosi nadgarstek i patrzy na zegarek, ~7–8 s profil w cieniu, odchodzi ✔. Monitor nie jest wyraźnie „obracany”. **★ 8B**, trym ~4,5–8 s (+ ew. insert monitora 0–3 s z kadrowaniem bez twarzy). Zapisane.
- **10A G5 lewy kafelek:** szeroki kadr od tyłu na krawędzi mokrego dachu, czapka z daszkiem czytelna w konturze ✔ → kamera wznosi się do tyłu głowy; okna układają się w zielono-czerwone słupki ✔; ALE ~5–8 s na tylnym pasku czapki świeci duży napis „DORIANOS” (poprawna pisownia — branding, ale to tekst). Zapas.
- **10A G5 prawy kafelek:** od zbliżenia tyłu czapki (podświetlony pasek) → odjazd do szerokiego planu na krawędzi dachu; miasto w pełni zamienia się w zielono-czerwone świece pod księżycem — najlepszy finalny kadr, brak tekstu. W szerokich planach czapka mało czytelna (mała). **★ 10A**, trym 3–8 s (lub całość). Zapisane.
- **10B G6 (3 kafelki: #1 lewy górny, #2 prawy górny, #3 lewy dolny):**
  - **#1 (lewy górny) ★ 10B:** 0–1,5 s od tyłu na dachu (czapka czytelna), obrót głowy przez ramię → ~2,5–5 s twarz w pełni do kamery, spokojny znaczący półuśmiech, bardzo podobny do Doriana (jasne niebiesko-szare oczy, szerokie kości policzkowe, zarost, kształt ust jak w REF_DORIAN_HERO), naturalna mimika, bez deformacji; ~6–6,5 s unosi nadgarstek (po lewej stronie kadru = LEWY, bo patrzy przez lewe ramię) ze świecącym zielono zegarkiem i stuka palcem wskazującym; ~7,2 s kadr wygasa do czerni ✔. Emblemat na czapce zielono-cyjanowy (średniej wielkości, bez Ferrari). Trym: całość (0–8 s). Zapisane do folderu.
  - #3 (lewy dolny) — zapas 1: prawie identyczny przebieg, twarz równie podobna, ale tarcza zegarka nie świeci na zielono przy tapnięciu.
  - #2 (prawy górny) — zapas 2: obraca się całym ciałem (nie samą głową), potem frontalny, statyczny portret; większa emblema; zegarek na lewym nadgarstku świeci zielono. Mniej filmowy.
  - Dodatkowe próby niepotrzebne.
- **8A G7 (Veo 3.1, próba 2):** od tyłu przez drzwi → szeroki kadr willi, czapka z daszkiem wyraźnie czytelna ✔, na tyle czapki mała zielona emblema + napis „DORIANOS" (czytelny, poprawny — branding), czwórka traderów przy biurkach z zielonymi wykresami, część odwraca głowy ✔, twarz ukryta cały czas ✔. Jaśniejszy, mniej „low-key" niż Seedance. **★ 8A**, całość lub 2–8 s. Zapisane. (G3 Seedance = zapas, bez czytelnej czapki.)

## ★ PODSUMOWANIE
| Ujęcie | ★ (Historia 9 lis) | Plik w „ZTT Teaser - wideo" (nazwa auto) | Trym | Zapas |
|---|---|---|---|---|
| 7A | G1 (Seedance) | `video_seedance-2-5_The man is @..._2026-11-09T18:43:50.mp4` | całość / 2–8 s | — |
| 7B | G2 (Seedance) | `…T18:49:44.mp4` | całość (zegarek na prawym → ew. flip poziomy) | — |
| 8A | G7 (**Veo 3.1**) | `video_veo-3-1_The man is @..._2026-11-09T19:07:02.mp4` | 2–8 s | G3 Seedance (czapka nieczytelna) |
| 8B | G4 (Seedance) | `…T18:56:15.mp4` lub `…T18:56:21.mp4` (jeden z dwóch) | 4,5–8 s (0–3 s twarz frontalnie) | — |
| 10A | G5 prawy kafelek (Seedance) | drugi z pary `…T18:56:xx.mp4` | 3–8 s / całość | G5 lewy (duży napis DORIANOS z tyłu czapki) |
| 10B | G6 kafelek #1 lewy górny (Seedance) | `…T19:03:23.mp4` | całość 0–8 s | #3 lewy dolny, #2 prawy górny |
Rozróżnienie 8B/10A w folderze: 8B = wnętrze z monitorem, 10A = dach nocą (podgląd miniatury).

## KOSZTY
Seedance 2.5 1080p 8 s: 9 × 50 121 = 451 089 kr. (7A, 7B, 8A, 8B, 10A ×2, 10B ×3) + Veo 3.1 1080p 8 s: 19 391 → **≈ 470 480 kr.** (budżet ~500 000; żadna pojedyncza generacja > 120 000).

## UWAGI TECHNICZNE (dla następnego agenta)
- Wyszukiwarka Historii NIE znajduje promptów zaczynających się od @wzmianek (np. REF_DORIAN_HERO „@photo_… @DORIANOS …"). HERO podpięte przez kliknięcie miniatury referencji przy kafelku JAW (szukaj `same light skin, light stubble`, tryb Obraz; potem przełącz na Wideo — referencja zostaje).
- Kafelki pod kompozytorem: video tworzy się przez JS dispatch `pointerover/mouseover` na <img> kafelka; menu „Więcej opcji" otwiera sekwencja pointerdown/mouseup/click z JS.
- Statusy „Prawie gotowe…" nie odświeżają się bez przeładowania; przeładowanie resetuje kompozytor (720p/5 s, bez referencji).
- Zrzuty ekranu/zoom co jakiś czas timeoutują — wystarczy powtórzyć.
