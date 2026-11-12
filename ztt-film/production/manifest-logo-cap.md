# MANIFEST LOGO-CAP — logo DORIANOS na przodzie czapki (test na 10B 16:9)
Data: 2026-11-12 · agent „logo-cap" (jedyny agent w ElevenLabs) · Historia → sekcja „12 lis", szukaj: `Add the DORIANOS logo from the reference image`
Wejście: ★ 10B 16:9 `GSu0wP38vIpQQoQoGbb8` (Seedance 2.5, 4K) + logo ★ LOGO_1x1 `xZwfWjE10ekpqVvJpttY` (podgląd 1024×1024, wgrany jako Odniesienie obrazu przez fetch → DataTransfer, nic z dysku; w ElevenLabs widoczny jako `dorianos-logo-1x1.webp`, asset `a7C5IynALF2fcBqufQx4`).
Prompt (identyczny dla A i B): `Add the DORIANOS logo from the reference image as an embroidered patch centered on the front panel of the man's black baseball cap, visible whenever the front of the cap faces the camera. Keep the man's face, identity, expression, hair, clothing, motion, lighting and background exactly unchanged.`
Ocena: contact sheet 5 klatek (1 / 2,5 / 4 / 5 / 6,5 s) oryginał vs edycja + zoom na czapkę i twarz (1,6 / 2,2 / 2,5 / 3 / 4 / 4,5 / 5,5 / 6 / 6,5 s) na pełnej rozdzielczości wyniku; twarz porównana z oryginałem 10B (5/5 wg zdjęć Dorian REAL).

## Wyniki
| Metoda | Model | Rozdz. | Koszt | (1) logo | (2) stabilność | (3) twarz | (4) realizm | ID | Werdykt |
|---|---|---|---|---|---|---|---|---|---|
| **A** | **Kling 4.0 Edit** (wideo przez „Więcej opcji → Użyj jako referencję" przy wybranym modelu; „Edytuj" na kafelku zawsze wymusza Seedance Edit) | 1080p (max dla modelu) → 1916×1080, 8,04 s, audio | **13 742** | **4** | **4** | **5** | **4** | **`LwtBiloVVfJQpqG8INZs`** (sesja `QZMgIB44f2eha2bQsleo`) | **★ ZALICZONE** |
| B | Seedance 2.5 Video Edit | 1080p (4K = 109 889 kr. — za drogo przy budżecie 150k) → 1920×1078 | 60 457 | 5 | 4–5 | **4** | 3,5 | `TTdpeiIW7ZdSA7ly4A0s` (sesja `8IFPlEdJadcBqCOgG15f`) | ODRZUT |
| C | Aleph 2.0 | — | 0 | — | — | — | — | — | nie uruchomiono (A zaliczyło) |
Iteracja (sam wordmark / biały haft): niepotrzebna.

### A — Kling 4.0 Edit ★
- Kadr, ruch, obrót, tap w zegarek, wygaszenie, tło — 1:1 z oryginałem. **Twarz nietknięta** (oczy, nos, usta, zarost identyczne jak w 10B przy 4,0 i 5,5 s) → 5/5.
- Na przodzie czapki ciemna prostokątna naszywka z cienką ramką: siatkowa głowa w czapce (zielono-cyjanowa, lekko świeci) nad napisem **DORIANOS** (pisownia poprawna, czytelna od ~2 s). Rozmiar typowy dla logo na czapce (górna część przedniego panelu).
- Wady: ikona głowy uproszczona/„rozmyta" (mniej detali siatki niż w logo), kolor ikony przechodzi z zielonego (2–3 s) w bardziej cyjanowy (5–6,5 s); naszywka wygląda bardziej na tkaną etykietę/nadruk niż haft 3D. Mała okrągła emblema z boku czapki zniknęła (OK). Na plecach (0–1 s) logo się nie pojawia ✔. W profilu (1–1,6 s) naszywka poprawnie w perspektywie.
- Zapisane: Zasoby → **„ZTT — prawdziwy Dorian"** (nazwa auto `video_kling-4…_Add the DORIANOS…`, 1916×1080). NOTATKA: **LOGO** — wersja 10B 16:9 z logo na czapce, podmienia `GSu0wP38…` w slocie 1:08.5–1:15.0 (trym 0–8 s jak dotąd; audio wyciszone).
- Uwaga: wynik jest 1080p (oryginał 4K) — OK, eksport 1080p.

### B — Seedance 2.5 Video Edit (odrzut)
- Logo bardzo wierne (ikona + DORIANOS, pisownia OK), ale ogromne (cały przedni panel) i świecące jak ekran, nie haft.
- Model **przebudował czapkę** (wyższa „trucker" z siateczką z tyłu, daszek niżej) → **oczy w cieniu daszka 3,5–6,5 s** (w oryginale wyraźne niebiesko-szare oczy) → twarz 4/5 (dolna połowa zgodna, ale kluczowy moment rozpoznawalności stracony). Lekko zmieniony kadr (1078 px, przesunięcie w pionie). Niezapisane.

## Wnioski
- **Kling 4.0 Edit wygrywa**: tani (≈13,7k / 8 s 1080p), zachowuje twarz i kadr piksel w piksel, dokłada naszywkę ikona+napis. Seedance Edit „regeneruje" całą głowę/czapkę → ryzyko dla twarzy.
- Ikona+napis zadziałały w A (napis czytelny, ikona uproszczona). Wersji „sam napis" nie testowano — jeśli właściciel zechce ostrzejszy znak, następny krok: Kling 4.0 Edit z samym wordmarkiem lub z wycinkiem ikony w większej rozdzielczości jako referencją.
- Procedura A: kafelek źródła → „Więcej opcji" → „Użyj jako referencję" (gdy w kompozytorze wybrany Kling 4.0 Edit) → Odniesienia obrazów = logo → prompt → 1080p → Generuj. Cenę zwraca `POST /v1/content/generations/price`.

## Koszty
B 60 457 + A 13 742 = **74 199 kr.** (budżet 150 000 ✔; max pojedyncza 60 457 < 120 000). Saldo po: wykorzystane ≈ 4 087 912 / 5 400 000 → pozostało ≈ 1 312 088.

## Kandydaci do poprawki — ujęcia z widocznym PRZODEM czapki (wg manifest-identity.md + obejrzane klatki)
| Format | Ujęcie | ★ ID | Co widać na przodzie czapki teraz | Priorytet |
|---|---|---|---|---|
| 16:9 | 10B | `GSu0wP38vIpQQoQoGbb8` → **ZROBIONE: `LwtBiloVVfJQpqG8INZs`** | — | — |
| 9:16 | 10B | `vHXkX7i3HarOZnQY5Tk0` | frontalny najazd 2–5,5 s, czapka bez napisu, emblema z boku | **wysoki** (ten sam przypadek co 16:9) |
| 16:9 | 1A | `nloIWPF7hiZKWDSvt15O` | frontalnie 4,5–8 s, mała okrągła świecąca emblema | wysoki |
| 9:16 | 1A | `eS3t2ntSFOn1u39H4skX` | frontalnie 6–8 s, okrągła cyjanowa emblema „D" | wysoki |
| 16:9 | 3A | `oYQuJo03SZO1Ynpxe20b` | 3/4 → prawie frontalnie 5,5–8 s, mała zielona emblema | średni |
| 16:9 | 4A | `rx3M13WjFVAZS9Fd32nM` | frontalny szeroki plan 0–5 s, mała świecąca emblema (czapka mała w kadrze) | średni/niski |
| 9:16 | 4A | `h2PCZzju3v4nDRZsT88X` | frontalnie 0–4 s, szeroki plan, czapka mała | niski |
| 16:9 | 8B | `0TxKfcY63L0ma18Xs8xI` | z przodu już napis „DORIANOS" (sam tekst, bez ikony) | niski (ew. ujednolicenie z ikoną) |
| 16:9 | 7A | `JGbdj8Zw8BTanmeafqdQ` | 3/4 z boku, mała zielona emblema — przód częściowo | niski |
| 9:16 | 7A | `mJxdfuUJ3GdkyCv9gc1e` | 3/4; emblema „D" z boku + drobny napis DORIANOS z przodu | niski |
| 16:9 | 8A | `40QM7NMbfufK9mIcYKzk` | od tyłu — przód niewidoczny; uwaga: świecąca emblema na TYLE czapki | — (ew. edycja „usuń emblemat z tyłu") |
Bez czapki / czapka poza kadrem: 2B (16:9 i 9:16), 3B, 7B (16:9 i 9:16).

## 6B — kokpit (nowe zadanie koordynatora) — NIE WYGENEROWANO
- Przygotowano w kompozytorze (karta zamknięta, stan nie jest trwały): Seedance 2.5, 16:9, 4K, 8 s, audio WŁ., refy: REF_ZTT_UI (@Image 1, z „Odtwórz" na 8B ★ `0TxKfcY63L0ma18Xs8xI`) + awatar **Dorian REAL → „Użyj obrazów źródłowych"** (@Image 2 z Odtwórz usunięty). Oczekiwany koszt 88 587 kr.
- **Kliknięcie „Generuj" zostało zablokowane przez system uprawnień (auto-mode classifier)** — nie obchodziłem blokady; 0 kr., brak wyniku, brak wycinka. Wymaga decyzji/zgody właściciela.
- Prompt gotowy do wklejenia (blok twarzy B2 + akcja starego 6B + lusterko):
```
The man is the real person from the reference photos (Dorian REAL). Keep his exact real face and identity, as in an unretouched photograph of him: around 40 years old, broad oval face with full cheeks, light blue-grey slightly wide-set eyes, straight fairly broad nose, thin lips with a slightly asymmetric half-smile, light stubble, short dark brown hair, fair skin. Not a model, not younger, no sharpened jawline, no sculpted cheekbones. From the photos take only his face; ignore their caps, headphones and microphone. [Shot/camera] Interior cockpit shot from the back seat, behind the driver, close on the windshield, the rear-view mirror and his gloved hands on the wheel, subtle handheld energy. The back of his head is a dark out-of-focus silhouette at the frame edge; his face is seen only as a reflection in the rear-view mirror. [Subject] The cabin of a classic 1960s grand touring sports car of original unbranded design: thin wooden-rim steering wheel with polished metal spokes; the center hub of the wheel is a plain smooth black disc with nothing on it, no badge, no crest, no emblem; vintage round analog gauges. The driver is the man: matte black baseball cap with a small embroidered DORIANOS logo patch on the front, black tuxedo, crisp white shirt cuffs and black leather driving gloves. His LEFT hand grips the wheel at the nine o'clock position on the left side of the frame, and the luxury steel chronograph watch is on that LEFT wrist, clearly visible between the glove and the cuff; his RIGHT wrist has no watch. [Action] On the windshield glass itself a translucent green holographic HUD in the style of the green trading interface in the first reference image draws a rising trend line that runs parallel to the curving mountain road ahead, with a small pulsing alert dot and a tiny ZTT monogram in the corner (the only symbol on the glass); his gloved hands make one precise steering correction. From about the third to the fifth second his eyes glance up into the rear-view mirror: the mirror clearly shows his real eyes, eyebrows and the upper half of his face under the brim of the black cap, sharp and well lit by the green HUD glow and the warm gauge light, instantly recognizable as him. [Scene/lighting] Dark cabin, warm gauge glow, neon city lights of a bay streaking past outside at night on a winding coastal mountain road, green HUD light reflecting on the gloves, the watch crystal and on his face in the mirror. [Style] Photorealistic, real camera footage look, shot on ARRI Alexa with 35mm anamorphic lenses, natural skin texture with visible pores and light stubble, no skin smoothing, natural eyes with light reflections, horizontal anamorphic lens flares, deep blacks, cinematic grade with gold, emerald green and neon cyan accents, shallow depth of field, subtle film grain, 24fps motion cadence. no readable text other than the tiny ZTT monogram, no subtitles, no captions, no watermarks, no car brand logos, no car emblems, no badge on the steering wheel, no numbers, no gibberish letters, no extra fingers, no deformed hands, no warped faces, no beauty filter, no cartoon look, no oversaturated colors, no Ferrari logo, no red cap, no headphones, no microphone, no earring, no passengers, watch only on his LEFT wrist, never on the right wrist. [Audio] Muffled vintage engine from inside the cabin, leather glove creak on the wheel, soft HUD interface tick. No dialogue, no voiceover, no speech.
```
- Uwaga do 6B: w lusterku napis na czapce będzie lustrzanie odwrócony (fizycznie poprawne, ale może razić) — ewentualnie po generacji Kling 4.0 Edit tylko jeśli przód czapki jest wyraźny.
- Do zrobienia: wygenerować (1 próba + max 1 powtórka, ≤ 180 000), ocenić twarz w lusterku (≥ 4,5) i realizm (≥ 4), ★ do „ZTT — prawdziwy Dorian", wycinek 3 s pod slot 0:40.0–0:43.0 (moment lusterka ~3–5 s źródła).

## Uwagi techniczne
- Okno Chrome poza ekranem (screenX −25600) — zrzuty działały, raz timeout.
- Klatki do oceny: `fetch(content_url)` → blob → `<video>` → seek + 400 ms opóźnienia → canvas (bez opóźnienia canvas potrafi złapać starą klatkę). Pełne `content_url` z `GET /v1/content/generations/{id}` (nagłówki autoryzacji przechwycone z fetch aplikacji).
- Po zapisie do zasobów wyskoczył baner „Pozostało tylko 24% miesięcznych kredytów" z ofertą ulepszenia planu — zamknięty krzyżykiem, nic nie kupiono.

## POPRAWKI LOGO + 6B (agent „logo+6B", 12 lis; zgoda właściciela na ≤ 350 000 kr. przekazana przez koordynatora)
Procedura: Historia → szukaj `Add the DORIANOS logo from the reference image` → ★ 10B Kling (`LwtBilo…`) → Więcej opcji → **Odtwórz** (przywraca Kling 4.0 Edit, 1080p, prompt, logo @Image 1) → usuń @Video → wyszukaj ujęcie → Więcej opcji → Użyj jako referencję (gdy brak @Video staje się @Video; gdy jest — dodaje się jako @Image 2!). Koszt ≈ 13,8k / 8 s („Pozostało 95").
Ocena widoczności przodu czapki: seek wideo kafelka (preview 852 px) + zoom.
| Ujęcie | Przód czapki w wycinku? | Start (UTC) | ID nowego | logo/stab./twarz/realizm | Koszt | Wycinek | Werdykt |
|---|---|---|---|---|---|---|---|
| 10B 9:16 | TAK (frontalny najazd 1,7–5,3 s) | ~10:03 | **`38qlyAIYF6rIUOV08pOX`** | 5 / 4,5 / 5 (twarz 1:1 z oryginałem przy 3,5 s) / 4,5 | ~13,8k | jak oryginał: 0,478–7,104 (8,125 s jak źródło) | ★ (zapis do folderu — patrz niżej) |
| 1A 16:9 | TAK (5 s i 7 s: frontalnie, emblema na przodzie) | ~10:05 | **`WmWWAOwBdVhlVFvQVvQ1`** | 4,5 / 4 / 5 (sylwetka, dolna twarz bez zmian) / 4 | ~13,8k | jak oryginał: 1,93–7,99 (8,125 s) | ★ |
| 1A 9:16 | TAK (6–8 s frontalnie, emblema „D") | ~10:06 | **`CjJB9hYCJSzsUzVkY3lG`** | 4,5 / 4,5 / 5 (sylwetka, oczy pod daszkiem — bez zmian) / 4,5 | ~13,8k | jak oryginał: 5,0–8,0 (8,125 s) | ★ |
| 3A 16:9 | TAK (5,5 i 7,5 s: 3/4→frontalnie) | ~10:08 | **`AtDg8fuZ6jbZuzTR4OOp`** | 4,5 / 4,5 / 5 (porównanie 6,5/7,1/7,9 s z oryginałem — identyczna mimika, mrużenie oczu jest w oryginale) / 4,5 | ~13,8k | jak oryginał: 4,10–8,00 (8,125 s) | ★ |
| 4A 16:9 | TAK (2,5 s: frontalnie, czapka wyraźna) | ~10:10 | **`0Pian0h5q5o0k0TUNdNK`** | 4,5 / 4,5 / 5 / 4,5 (insert z zegarkiem 6 s bez zmian) | ~13,8k | jak oryginał: 2,02–8,04 (8,125 s) | ★ |
| 7A 16:9 | TAK (2,5 i 5,5 s: 3/4, emblema na przednim panelu) | ~10:15 | **`dIG6ClmrEWvrw1csGOWN`** | 4,5 / 4,5 / 5 (profil 3/4 identyczny jak oryginał przy 2,5/5,5 s) / 4,5 | ~13,8k | jak oryginał: 1,50–5,99 (8,125 s) | ★ |
| 7A 9:16 | TAK (4 i 6,8 s: drobny napis z przodu + „D" z boku) | ~10:16 | **`819V9NQJfPnNqHRcusmb`** | 4,5 / 4,5 / 5 / 4,5 (boczna emblema „D" znikła, naszywka dość duża) | ~13,8k | jak oryginał: 3,5–7,2 (8,125 s) | ★ |
| 8B 16:9 | TAK (2,2 s: 3/4, napis DORIANOS) | ~10:19 | **`DH48L2iqs9XjPeVa23JC`** | 4 (mała naszywka ikona+napis) / 4,5 / 5 / 4,5 | ~13,8k | jak oryginał: 1,70–5,21 (8,125 s) | ★ |
| 4A 9:16 | NIE — w wycinku 3,7–8,0 szeroki plan tylko ~0,3 s, czapka ciemna pod światło bez widocznej emblemy, potem insert zegarka | — | bez zmian | — | 0 | 3,7–8,0 | pominięte |
| 8A 16:9 (usuń emblemat z TYŁU) | emblema z tyłu czapki widoczna w wycinku 4,5–8 s | ~10:22 | **`EGuKAVaA9TePboQC20he`** | usunięcie 5 / 4,5 / n.d. (od tyłu) / 4,5 (czapka gładka czarna; tło, traderzy, ruch 1:1) | ~13,8k | jak oryginał: 4,50–8,00 (8,125 s) | ★ |

Prompt 8A: `Remove the glowing emblem from the back of the man's black baseball cap, so the back of the cap is plain matte black. Keep everything else unchanged: the man, his clothing, motion, the room, the traders, the monitors, lighting and camera movement exactly as in the original video.` (Kling 4.0 Edit, 1080p, bez logo w refach).
Długość: wszystkie wyniki Kling Edit mają w podglądzie 8,125 s — tak samo jak źródła (podgląd źródeł też 8,125 s) → wycinki bez zmian. Rozdzielczość wyników 1080p (16:9 ≈1916×1080, 9:16 ≈1080×1916) zamiast 4K.

### 6B — Seedance 2.5, 16:9, 4K, 8 s, audio WŁ.; refy @Image 1 = REF_ZTT_UI (z Odtwórz na 8B ★) + @Dorian REAL (Obrazy źródłowe); prompt z sekcji 6B; start ~10:25 UTC; szukaj `Interior cockpit shot from the back seat`
| Ujęcie | ID ★ | Twarz w lusterku | Realizm | Koszt | Wycinek | Uwagi |
|---|---|---|---|---|---|---|
| 6B 16:9 4K | **`tSzbA0iOTusJSSfHPmzQ`** (3840×2160, 8,04 s, audio) | **4,5** (ocena na pełnym 4K, 3/4/5 s: jasne niebiesko-szare oczy, szeroka twarz, pełne policzki, prosty szeroki nos — jak na prawdziwych zdjęciach) | 4,5 | ~88 600 | **2,5–5,5 s** pod slot 0:40.0–0:43.0 (spojrzenie w lusterko + rosnąca linia HUD z kropką alertu) | twarz w lusterku widoczna praktycznie cały klip (nie tylko 1–2 s); w lusterku widać tylko daszek czapki — przód z logo niewidoczny → Kling Edit niepotrzebny; piasta kierownicy gładka ✔; zegarek na LEWYM nadgarstku (lewa krawędź kadru) ✔; HUD z „ZTT" + drobne nieczytelne cyfry osi; z przodu-lewej rozmyta sylwetka głowy z czapką (profil w zielonym świetle). Powtórka niepotrzebna. |

### ZAPIS
Wszystkie ★ (10B 9:16, 1A 16:9, 1A 9:16, 3A, 4A 16:9, 7A 16:9, 7A 9:16, 8B, 8A, 6B) zapisane: Zasoby → „ZTT — prawdziwy Dorian" (nazwy auto `video_kling-4…_Add the DORIANOS…` / `…_Remove the glowing…` / `video_seedance-2-5_The man is the real…`). Stare wersje bez logo zostają jako zapas.
Do montażu: podmienić klipy na te same pozycje i wycinki (Kling Edit zachowuje czas; wyniki 1080p zamiast 4K).

### KOSZTY
10 × Kling 4.0 Edit 1080p 8 s ≈ 10 × 13 750 ≈ 137 500 + 6B Seedance 4K 88 600 = **≈ 226 000 kr.** (budżet 350 000 ✔; max pojedyncza 88 600 < 120 000). Powtórki: 0. Banerów zakupu nie było.
Uwaga: „Powiększ" w menu kafelka to upscale (płatne) — nie klikać przy ocenie; pełne 4K do oceny daje kliknięcie w kafelek (podgląd/modal, `content.mp4`).
