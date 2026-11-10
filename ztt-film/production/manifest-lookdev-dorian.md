# MANIFEST LOOK-DEV — BOHATER = DORIAN (Agent 00ZTT v2)
Data: 2026-11-09 · Agent: art director / look-dev · ElevenLabs → Obraz i wideo → zakładka **Obraz**

## Ustawienia wspólne
- Model **Nano Banana Pro**, 16:9, **4K** (5504×3072 PNG), auto-poprawianie promptu: **Wyłączone**.
- Koszt: 2 272 kr./obraz z referencją (9 090 za 4, 4 545 za 2).
- Źródła: zdjęcie Doriana = awatar „Agent 00ZTT” → styl **„photo_2026-09-23_19-37-07”** (czarna wzorzysta czapka, białe słuchawki, mikrofon);
  zestaw marki **DORIANOS** (3 zasoby: logo DORIANOS VIP w kole, obraz referencyjny „DORIANOS Wireframe Profile” — neonowa siatkowa głowa w czapce, opis marki). **Brak zdjęć Doriana w zestawie marki.**
- Brak wideo. Nic nie wgrywano z dysku (avatar zbudowany z obrazów już będących na koncie — patrz niżej).

| Zasób | Koszt |
|---|---|
| REF_DORIAN_HERO runda 1 (4×) | 9 090 |
| REF_DORIAN_HERO runda 2 (4×, poprawka nadgarstka) | 9 090 |
| REF_DORIAN_SILHOUETTE (4×) | 9 090 |
| REF_DORIAN_JAW (2×) | 4 545 |
| Awatar „Dorian 00ZTT” (Nano Banana Pro) | 3 045 |
| **Razem** | **≈ 34 860** (budżet 150 000) |

## Jak znaleźć w Historii
`https://elevenlabs.io/app/image-video` → **Historia** → sekcja **„9 lis”**. Kafelki grupy 2×2: **#1 lewy górny, #2 prawy górny, #3 lewy dolny, #4 prawy dolny**.
Kolejność od najnowszej: JAW → SILHOUETTE → HERO r2 → HERO r1. Szukaj polem „Szukaj generacji…” po fragmencie prompta.
UWAGA: historia ładuje się leniwie — przewiń w dół, żeby dociągnęły się dolne kafelki grup.

---

## ★ REF_DORIAN_HERO → **runda 2, wariant #2 (prawy górny)**
- Szukaj: `he raises his LEFT hand (on the right side of the image` (odróżnia r2 od r1; oba zaczynają się od `@photo_2026-09-23_19-37-07 @DORIANOS Cinematic medium close-up character portrait`).
- Referencje: zdjęcie Doriana (styl photo_… awatara Agent 00ZTT) + `@DORIANOS` (zestaw marki: logo + wireframe ref).
- Rozpoznasz: lekki 3/4, lewa dłoń przy musze, zegarek po prawej stronie kadru (= LEWY nadgarstek ✔), mała zielono-cyjanowa emblema na czapce, cyjanowy neon w kształcie „Γ/L” w prawym górnym rogu, złoty bokeh po lewej.
- **Podobieństwo: bardzo wysokie (najlepsze z 8).** Zgodne z jego zdjęciem: jasne niebiesko-szare oczy, szerokie kości policzkowe i pełniejszy owal, prosty nos, wąskie usta, ten sam kształt brwi, lekki zarost. Naturalny półuśmiech.
- Alternatywy: r2 #4 (prawy dolny — równie podobny, emblemat większy), r2 #3 (obie dłonie przy musze, emblemat duży). r2 #1 — zegarek na złym nadgarstku.
- Runda 1 (wszystkie 4 bardzo podobne do Doriana, ale zegarek wypadł na PRAWYM nadgarstku, dłoń w pięści przy klapie) → odrzucone tylko z powodu nadgarstka. Ocena podobieństwa r1: #2 i #4 najlepsze.
- Prompt (r2):
```
@photo_2026-09-23_19-37-07 @DORIANOS Cinematic medium close-up character portrait, chest up, of the real man from the reference photo - keep his exact face and identity: light blue-grey eyes, short dark brown hair, light stubble, defined jaw, the same face shape, nose, cheekbones, eyebrows and lips, around 40 years old, calm intense gaze. He wears a matte black baseball cap with a small embroidered, softly glowing green-cyan DORIANOS emblem on the front (only the small wireframe head-in-cap symbol from the DORIANOS brand logo, no large text), an impeccably tailored black tuxedo with black satin bow tie, crisp white shirt and white pocket square, luxury steel chronograph watch on his LEFT wrist: he raises his LEFT hand (on the right side of the image from the viewer) to adjust his bow tie, so the watch is clearly visible on the wrist at the right side of the frame; his right arm stays relaxed and mostly out of frame. Face fully visible, nearly frontal slight three-quarter view toward camera, composed confident slight half-smile, sharp focus on the face. Background: night city skyline in soft bokeh with distant gold and neon cyan lights, subtle emerald green rim light on his shoulder, warm golden key light from the side. Photorealistic. Shot on 35mm anamorphic lenses, horizontal anamorphic lens flares, deep crushed blacks, high contrast low-key lighting, cinematic color grade with gold, emerald green and neon cyan palette, shallow depth of field, premium spy-thriller film look, subtle film grain. No readable text, no subtitles, no captions, no watermarks, no brand logos other than the small DORIANOS emblem on the cap, no Ferrari logo, no red cap, no other brand logos, no headphones, no microphone, no text artifacts, no gibberish letters, no extra fingers, no deformed hands, no warped faces, no cartoon look, no oversaturated colors.
```
(r1 = to samo, ale fragment o zegarku brzmiał: `luxury steel chronograph watch clearly on his LEFT wrist as his left hand rests near his lapel.` i `Face fully visible in three-quarter view toward camera` — model i tak dawał prawy nadgarstek.)

## ★ REF_DORIAN_SILHOUETTE → **wariant #4 (prawy dolny)**
- Szukaj: `Same man as in @Image 1 - keep his exact face shape, short dark brown hair`
- Referencja: ★ HERO r2 #2 (@Image 1, dodane przyciskiem „Odniesienie” pod kafelkiem).
- Rozpoznasz: cała sylwetka od tyłu, stoi na krawędzi mokrego dachu, czapka wyraźnie w konturze, panorama z cyjanowymi neonami i zielonym horyzontem, flara anamorfowa po lewej.
- Alternatywa: #2 (prawy górny — 3/4 od tyłu, plan średni, widać krawędź szczęki, dłonie z zegarkiem; emblemat wypadł na boku czapki). Odrzucone: #1 (pełny profil — twarz zbyt widoczna), #3 (twarz od przodu).
- Prompt:
```
Same man as in @Image 1 - keep his exact face shape, short dark brown hair, jawline and build, same matte black baseball cap with the small glowing green-cyan DORIANOS emblem on the front, same black tuxedo, black bow tie, crisp white shirt, white pocket square and luxury steel chronograph watch on his LEFT wrist. Around 40 years old, calm confident posture, face mostly hidden - seen from behind in a three-quarter rear view, only the edge of his jaw and cheek visible in half-profile, never a full frontal face. The baseball cap is clearly readable in his silhouette, its brim outlined by rim light. Wide cinematic full-body shot: he stands alone at the very edge of a skyscraper rooftop at night, looking out over a vast glittering night city far below, his left hand casually adjusting his shirt cuff. Wet reflective rooftop concrete, thin haze, distant gold city lights, neon cyan skyscraper accents, faint emerald green glow on the horizon, strong cool rim light outlining his silhouette, shoulders and cap. Photorealistic. [STYLE BLOCK bez „24fps motion cadence”]. No readable text, no subtitles, no captions, no watermarks, no brand logos other than the small DORIANOS emblem on the cap, no Ferrari logo, no red cap, no other brand logos, no headphones, no microphone, no text artifacts, no gibberish letters, no extra fingers, no deformed hands, no warped faces, no cartoon look, no oversaturated colors.
```

## ★ REF_DORIAN_JAW → **wariant #2 (prawy)**
- Szukaj: `Same man as in the reference image - same light skin, light stubble`
- Referencja: ★ HERO r2 #2. 2 generacje (grupa 1×2: #1 lewy, #2 prawy).
- Rozpoznasz: kadr od nosa w dół, półuśmiech, mucha, prawa dłoń poprawia lewy mankiet, stalowy chronograf na LEWYM nadgarstku ✔, żyrandole i zielone stoły kasyna w tle.
- Alternatywa: #1 (lewa pięść uniesiona przy brodzie — trochę sztuczna poza). UWAGA prawna: tarcza zegarka przypomina klasyczny chronograf luksusowej marki — w wideo nie robić makro na tarczę.
- Prompt:
```
Same man as in the reference image - same light skin, light stubble, jawline and build, same black tuxedo, black satin bow tie, crisp white shirt, white pocket square and the same luxury steel chronograph watch on his LEFT wrist. Around 40 years old, calm confident posture. Tight cinematic close-up framed strictly below the eyes - face mostly hidden, only his jaw with light stubble, a composed slight half-smile on his lips, the black bow tie, and his LEFT hand raised near his chin adjusting his shirt cuff, the steel chronograph clearly visible on the LEFT wrist, white shirt cuff with a silver cufflink. Setting: a luxurious old-world night casino, warm golden light from crystal chandeliers, emerald green felt of a card table and soft gold bokeh in the background, subtle emerald green and neon cyan accent reflections on the watch crystal. Photorealistic. [STYLE BLOCK bez „24fps”]. No eyes visible, no readable text, no subtitles, no captions, no watermarks, no brand logos, no logos on the watch dial, no Ferrari logo, no red cap, no other brand logos, no headphones, no microphone, no text artifacts, no gibberish letters, no extra fingers, no deformed hands, no warped faces, no cartoon look, no oversaturated colors.
```

---

## ★ AWATAR „Dorian 00ZTT” (utworzony; stary „Agent 00ZTT” nietknięty)
- Gdzie: Obraz i wideo → Odkrywaj → karuzela **Awatary** (pierwszy kafelek po „Nowe”) / Zasoby → Moje awatary.
- Typ „Prześlij obrazy”, model **Nano Banana Pro**, bez głosu. **Obrazy źródłowe (3):**
  1. ★ HERO r2 #2 przeskalowany do 2048 px (JPEG),
  2. crop twarzy 1400×1400 z tego samego obrazu,
  3. zdjęcie Doriana (styl photo_… z awatara Agent 00ZTT, 1024 px).
  Pliki wzięte z obrazów już na koncie (fetch w karcie → DataTransfer do pola uploadu) — nic z dysku.
- Styl wygenerowany automatycznie: **„Headshot”** (studyjny portret w smokingu i czarnej czapce z emblematem; twarz zgodna z Dorianem).
- UWAGA: obraz źródłowy nr 3 ma słuchawki i mikrofon — przy opcji „Użyj N obrazów źródłowych” dopisywać `no headphones, no microphone`; bezpieczniej wybierać styl **„Headshot”**.

### Jak użyć w trybie Wideo
1. Kompozytor → zakładka **Wideo** → slot **Odniesienia obrazów** → ikona **⋮ (Więcej opcji)** → **„Wybierz awatar”** → **Dorian 00ZTT** → wybierz styl **„Headshot”** (lub „Użyj obrazów źródłowych”) → „Użyj stylu”.
   (Kafelka slotu NIE klikać — otwiera systemowe okno plików. Przy modelu Seedance sloty bywają chwilowo nieaktywne — wtedy przełącz model / użyj drogi 2.)
2. Albo w polu prompta wpisz `@Dorian` → sekcja **Zasoby → Dorian 00ZTT** (sprawdzone, działa w trybie Wideo) → wybór stylu.
3. Alternatywa: Historia → kafelek ★ HERO r2 #2 → przycisk **„Odniesienie”** (dodaje @Image N) lub **„Wideo”** (początkowa klatka).
- Pułapka: klik w awatar na Odkrywaj przełącza kompozytor na „Synchronizacja ust”/HeyGen — wróć na Wideo/Obraz i sprawdź model.
- Kompozytor zostawiony czysty (bez referencji i tekstu).
