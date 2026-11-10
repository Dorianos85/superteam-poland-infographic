# MANIFEST LOOK-DEV — ZTT: LICENCJA NA ZYSK
Data: 2026-11-07 · Agent: look-dev / art director · Narzędzie: ElevenLabs → Obraz i wideo → zakładka **Obraz**

## Ustawienia wspólne
- **Model:** Nano Banana Pro (opis w UI: „Kontrola jakości studyjnej, czytelny tekst, niesamowita spójność”).
  Wybrany zamiast GPT Image 2.x / Seedream / FLUX, bo ma najlepszy fotorealizm + trzymanie promptu i spójność postaci z referencji.
- **Proporcje:** 16:9 · **Rozdzielczość:** 4K (pliki 5504×3072 px, PNG ~17 MB) · **Generacje:** 4 na prompt · auto-poprawianie promptu: Wyłączone.
- **Koszt:** 1 818 kr./obraz bez referencji (7 272 kr. za 4), 2 272 kr./obraz z referencją (9 090 kr. za 4).
- **Łącznie wydane:** ok. **49 700 kredytów** (budżet 300 000). Zero wideo.

| Zasób | Koszt |
|---|---|
| REF_AGENT_HERO (4×) | 7 272 |
| Awatar „Agent 00ZTT” (Nano Banana Pro) | 2 436 |
| REF_AGENT_SILHOUETTE (4×, z ref.) | 9 090 |
| REF_FEMME (4×) | 7 272 |
| REF_CAR (4×) | 7 272 |
| REF_ZTT_UI (4×, z ref.) | ~9 090 (szac.) |
| REF_CANDLE_TUNNEL (4×) | 7 272 |

## Jak znaleźć obrazy w UI
`https://elevenlabs.io/app/image-video` → zakładka **Historia** (filtr Typ: Obraz) → sekcja **„7 lis”**.
Każdy prompt to jedna grupa 4 kafelków w układzie 2×2: **#1 = lewy górny, #2 = prawy górny, #3 = lewy dolny, #4 = prawy dolny**
(ta sama kolejność co strzałki → w podglądzie). Szukaj w polu „Szukaj generacji…” po początku promptu podanym niżej.
ElevenLabs nie nadaje obrazom tytułów — w podglądzie widać tylko „Podgląd generacji image o 7.11.2026” i prompt.

Kolejność grup w Historii (od najnowszej): TUNNEL → UI → CAR → FEMME → SILHOUETTE → HERO.

---

## ★ REF_AGENT_HERO → wariant **#4 (prawy dolny)**
- Szukaj: `Cinematic medium close-up character reference portrait`
- Rozpoznasz: tło z zielonymi i złotymi pionowymi neonami po lewej, cyjanowy neon w kształcie odwróconej litery L w prawym górnym rogu, woda na dole. Twarz w pełni widoczna, 3/4, lekki uśmiech.
- Jakość: najczystsza twarz (dobra jako referencja twarzy do 10B), gold + szmaragd + cyjan. Zastrzeżenie: zegarek wypadł na prawym nadgarstku (ręka przy muszce) — w promptach wideo pilnować „left wrist”.
- Alternatywa: #1 (najbardziej filmowy grade, ale ma czarne pasy po bokach).
- Prompt:
```
Cinematic medium close-up character reference portrait, chest up, of a fictional original man: a poised secret-agent type man, around 35-40 years old, athletic build, short dark hair neatly styled, strong jawline, light stubble, calm piercing eyes, wearing an impeccably tailored black tuxedo with black satin bow tie and crisp white shirt, white pocket square, luxury steel chronograph watch on left wrist visible as his left hand rests near his lapel, calm confident posture. Face fully visible in three-quarter view toward camera, composed slight smile, sharp focus on the face. Background: night city skyline in soft bokeh with distant gold and neon cyan lights, subtle emerald green rim light on his shoulder, warm golden key light from the side. Photorealistic. Shot on 35mm anamorphic lenses, horizontal anamorphic lens flares, deep crushed blacks, high contrast low-key lighting, cinematic color grade with gold, emerald green and neon cyan palette, shallow depth of field, premium spy-thriller film look, subtle film grain, 24fps motion cadence. Original invented person, not resembling any real actor or celebrity. No readable text, no subtitles, no captions, no watermarks, no brand logos, no text artifacts, no gibberish letters on screens, no extra fingers, no deformed hands, no warped faces, no cartoon look, no oversaturated colors, no camera shake unless specified.
```

## ★ AWATAR „Agent 00ZTT” (utworzony)
- Gdzie: Obraz i wideo → Odkrywaj → karuzela **Awatary** (pierwszy kafelek po „Nowe”) / „Zobacz wszystkie”.
- Źródło: ★ REF_AGENT_HERO #4 (kadr 2048 px) + crop twarzy 1400×1400 z tego samego obrazu. Typ: „Prześlij obrazy”, model Nano Banana Pro, bez domyślnego głosu.
- Styl wygenerowany automatycznie: **„Headshot”** (studyjny portret w smokingu). Można dodać kolejne style („Nowy styl”).
- Użycie w promptach — patrz sekcja PROCEDURY.

## ★ REF_AGENT_SILHOUETTE → wariant **#3 (lewy dolny)**
- Szukaj: `Same man as in the reference image - keep his exact face shape`
- Referencja: ★ HERO #4 (@Image 1).
- Rozpoznasz: widziany od tyłu, lekki pół-profil, stoi na samej krawędzi dachu BEZ szklanej balustrady, mokry beton z odbiciami cyan/zielonymi, panorama wieżowców.
- Alternatywa: #2 (pół-profil, poprawia mankiet, szklana balustrada) — też dobra. Odrzucić #4 (twarz za bardzo od przodu).
- Prompt:
```
Same man as in the reference image - keep his exact face shape, short dark hair, jawline and build, same black tuxedo, black bow tie, crisp white shirt, white pocket square and luxury steel chronograph watch on left wrist. A poised secret-agent type man, around 35-40 years old, athletic build, calm confident posture, face partially hidden - seen from behind in a three-quarter rear view, only the edge of his jaw visible in half-profile, never a full frontal face. Wide cinematic full-body shot: he stands alone at the edge of a skyscraper rooftop at night, looking out over a vast glittering night city far below, one hand casually adjusting his shirt cuff. Wet reflective rooftop concrete, low glass parapet, thin haze, distant gold city lights, neon cyan skyscraper accents, faint emerald green glow on the horizon, strong cool rim light outlining his silhouette and shoulders. Photorealistic. [STYLE BLOCK]. [NEGATIVE BLOCK]
```

## ★ REF_FEMME → wariant **#3 (lewy dolny)**
- Szukaj: `Cinematic medium shot of a fictional original femme fatale`
- Rozpoznasz: koło ruletki w prawym dolnym rogu, kryształowe żyrandole, anamorfowa flara przez kadr, patrzy przez ramię, czerwone usta, długie czarne rękawiczki.
- Prompt:
```
Cinematic medium shot of a fictional original femme fatale: an elegant, mysterious woman around 30-40 years old, sleek dark hair in a low chignon, subtle red lips, wearing a black floor-length silk evening gown with bare shoulders and long black satin gloves, holding a crystal champagne flute, standing beside a roulette table with emerald green felt and a spinning roulette wheel in a luxurious old-world casino. Warm golden light from crystal chandeliers, deep black and burgundy velvet drapes, polished brass and mahogany details, soft bokeh of other elegant guests in the background. She glances over her bare shoulder toward camera with a knowing half-smile. Original invented person, not resembling any real actress or celebrity. Photorealistic. [STYLE BLOCK]. [NEGATIVE BLOCK]
```

## ★ REF_CAR → wariant **#4 (prawy dolny)**
- Szukaj: `Cinematic wide tracking shot of a classic 1960s-style grand tourer`
- Rozpoznasz: auto jedzie na kamerę z zapalonymi reflektorami, w tle zatoka w stylu Monako z jachtami, cyjanowe i złote odbicia, motion blur.
- Brak emblematów i tekstu na tablicy (sprawdzone w zbliżeniu). UWAGA prawna: sylwetka mocno przypomina Jaguara E-Type (#1, #2, #4); #3 przypomina Mustanga fastback. Bez logo jest OK jako „estetyka gatunku”, ale w wideo nie robić zbliżeń na grill.
- Prompt:
```
Cinematic wide tracking shot of a classic 1960s-style grand tourer sports coupe of original unbranded design: long sculpted hood, smooth curved fastback body, round chrome-ringed headlights glowing, chrome wire-spoke wheels, gunmetal grey metallic paint. Absolutely zero logos, zero emblems, zero badges, plain grille, blank license plate. The car drives fast along a winding coastal serpentine mountain road at night high above a bay; far below, a luxury harbor town glows with gold and neon cyan lights reflected in the dark water, yachts in the marina, faint emerald green accent lights. Wet asphalt with gold and cyan reflections, headlight beams cutting through light sea haze, subtle motion blur on the road edges, cliffs and stone guard wall. Photorealistic. [STYLE BLOCK]. [NEGATIVE BLOCK]
```

## ★ REF_ZTT_UI → wariant **#4 (prawy dolny)**
- Szukaj: `Extreme close-up macro shot of a man's left wrist`
- Rozpoznasz: lewy nadgarstek z mankietem i spinką, stalowy chronograf, palec dotyka smartfona; na ekranie zielone świece, pulsujący dzwonek alertu i czytelny monogram „ZTT” (sprawdzone w zbliżeniu). Zielona poświata na dłoni.
- Referencje: ★ HERO #4 + PRZYPADKIEM również ★ FEMME #3 (pozostałość z testu przycisku „Odniesienie”) — w wynikach to nie przeszkadza (kasynowe bokeh w tle), ale warto wiedzieć.
- Uwaga: tarcza zegarka przypomina klasyczny chronograf luksusowej marki (bez logo). #2 i #3 mają „ZTT/ZIT” mniej czytelne.
- Prompt:
```
Extreme close-up macro shot of a man's left wrist and hand: black tuxedo sleeve, crisp white shirt cuff with a silver cufflink, and the same luxury steel chronograph watch as worn by the man in the reference image. In the same hand he holds a sleek black smartphone tilted toward camera. The smartphone screen shows a sleek trading terminal UI with glowing green candlestick chart and a pulsing alert notification, minimal interface, only a small "ZTT" monogram visible. The screen casts a soft emerald green glow onto his fingers, the shirt cuff and the watch crystal. Dark background with deep shadows and faint gold bokeh of a night casino. Photorealistic. [STYLE BLOCK]. No readable text other than the small ZTT monogram, [reszta NEGATIVE BLOCK]
```

## ★ REF_CANDLE_TUNNEL → wariant **#2 (prawy górny)**
- Szukaj: `Symmetrical one-point perspective shot looking straight down a long circular tunnel`
- Rozpoznasz: najbardziej symetryczna spirala zielono-czerwonych świec, mała czarna sylwetka w smokingu w jasnym kole, uniesiony palec.
- Bez referencji (sylwetka to czysty kontur — referencja twarzy zbędna).
- Alternatywa: #4 (bardziej dynamiczne smugi). UWAGA prawna: biały krąg + stojąca sylwetka kojarzy się z „gun barrel” — przy montażu/wideo zabarwić krąg na zielono/cyjan i trzymać tunel ze świec (nie gwintowanie lufy).
- Prompt:
```
Symmetrical one-point perspective shot looking straight down a long circular tunnel whose walls are built entirely from glowing green and red candlestick chart bars, arranged in spiral rifling grooves like the inside of a slowly spinning rifled barrel, subtle rotational motion blur, the candlestick bars emit volumetric emerald green and crimson light into a pure black void. At the far end of the tunnel, inside a small bright circle of soft white light, stands a tiny pure black silhouette of a man in a tailored tuxedo facing the camera, one arm slightly raised with a single finger extended as if about to tap an invisible glass screen. Abstract, graphic, elegant, original design that does not copy any existing film title sequence or logo. Photorealistic render quality. [STYLE BLOCK]. [NEGATIVE BLOCK]
```

---

## PROCEDURY DLA AGENTÓW WIDEO

### A. Podpięcie obrazu z Historii jako „Odniesienia obrazów” (tryb Wideo) — NAJPEWNIEJSZA DROGA
1. `https://elevenlabs.io/app/image-video` → w kompozytorze kliknij zakładkę **Wideo** (kompozytor wideo ma sloty: Początkowa klatka · Klatka końcowa · Odniesienia obrazów · Odniesienia wideo · Odniesienia audio).
2. Przejdź do zakładki **Historia** strony (kompozytor zostaje na dole).
3. Znajdź grupę (pole „Szukaj generacji…” + początek promptu z tego manifestu) i właściwy kafelek (#1–#4 jak wyżej).
4. Pod kafelkiem są przyciski **Edytuj · Wideo · Odniesienie**:
   - **„Odniesienie”** → dodaje obraz do slotu **Odniesienia obrazów** jako chip `@Image 1` (kolejne: `@Image 2`…). W prompcie można się do nich odwołać pisząc `@Image 1`.
   - **„Wideo”** → wstawia obraz jako **Początkowa klatka** (image-to-video). UWAGA: potrafi też wkleić ostatni prompt do pola — sprawdź tekst przed generacją.
5. Alternatywnie: kliknij kafelek → otwiera się podgląd (pełne 5504×3072) → przycisk **„Użyj jako odniesienie”** (w trybie Obraz dodaje @Image N; tam są też „Powiększ obraz”, „Odtwórz”, „Utwórz wideo”).
6. Usuwanie referencji: najedź na chip → przycisk „Usuń”.

### B. Inne źródła w slocie „Odniesienia obrazów”
- Kliknięcie samego kafelka slotu = **upload z dysku** (otwiera systemowe okno plików — w automatyzacji Chrome tego NIE klikać, bo zawiesza kartę).
- Ikona **⋮ (Więcej opcji)** przy slocie → menu: **„Wybierz awatar”** | „Prześlij obraz”.
  „Wybierz awatar” otwiera okno „Wybierz avatara” — **Agent 00ZTT (1 styl)** jest na pierwszej pozycji.
- `@` → „Wszystkie moje zasoby” pokazuje foldery/projekty (np. „Coach FI — Marketing EN”), NIE historię generacji — obrazy z look-devu bierz z Historii.

### C. Awatar „Agent 00ZTT” w promptach (@)
1. W polu promptu wpisz `@` → menu: Zestawy marki (DORIANOS, Coach FI) · Zasoby: **Moje awatary**, Moje flow, Wszystkie moje zasoby.
2. Wpisz dalej `Agent` → pojawia się **„Agent 00ZTT”** → kliknij.
3. Wyskakuje okienko „Wybierz jeden ze stylów Agent 00ZTT”: **„Użyj 2 obrazów źródłowych”** (zalecane — smoking + nocne miasto, twarz ★) albo styl **„Headshot”** → „Użyj stylu”.
4. W trybie Wideo to samo przez slot Odniesienia obrazów → ⋮ → „Wybierz awatar” → Agent 00ZTT.
5. W ujęciach „twarz ukryta” i tak dopisuj w prompcie: seen from behind / silhouette / framed below the eyes.

### D. Pułapki zaobserwowane w UI (ważne dla agentów równoległych)
- Stan kompozytora (model, rozdzielczość, tekst, referencje) potrafi się **samoczynnie zresetować** do GPT Image 2.6 / 1K i wyczyścić tekst (prawdopodobnie synchronizacja między kartami). Ustawiaj model/rozdzielczość/tekst **bezpośrednio przed** kliknięciem Generuj i sprawdź je jeszcze raz.
- Referencje dodane w trybie Wideo przenoszą się do trybu Obraz i odwrotnie — przed generacją sprawdź, ile chipów `@Image N` jest w kompozytorze.
- Koszt widać po najechaniu na „Pozostało N” obok przycisku Generuj (tooltip: „4 generacje będzie kosztować X kredytów”).
- Karta w tle często nie odświeża zrzutów ekranu — podgląd obrazów działa po otwarciu kafelka (lightbox).
