# MANIFEST LOGO — ZTT: LICENCJA NA ZYSK (karta końcowa)
Data: 2026-11-10, ok. 23:20–23:35 UTC (w Historii sekcja **„10 lis”**) · Agent: brand designer · ElevenLabs → Obraz i wideo → zakładka **Obraz**

## Krok 1 — ocena Zestawu marki DORIANOS (przed zmianą: 3 zasoby)
- **Logotypy:** „Badge Lockup” (Podstawowy, PNG) — okrągły ciemny medal, siatkowa głowa, napis „DORI|ANOS” rozbity świecą, złoty medal „VIP”. → nie nadaje się (VIP + okrąg).
- **Obrazy referencyjne:** „Wireframe Profile Illustration” — tylko 311×322 px (rozmyty), sama głowa BEZ napisu DORIANOS, tło granatowo-czarne (nie #000), w prawym dolnym rogu małe świece. → **NIE spełnia** wymagań (brak wordmarku, niska rozdzielczość).
- **Opis marki:** wprost wspomina „rich metallic gold VIP emblems” — dlatego NIE używałem czipa `@DORIANOS` (wciągnąłby VIP).

## Ustawienia generacji
- Model **Nano Banana Pro**, rozdzielczość **4K**, 4 generacje, auto-poprawianie: Wyłączone.
- Referencje (slot „Odniesienia obrazów”, wgrane z podglądów zestawu marki przez fetch → DataTransfer, nic z dysku):
  `@Image 1` = Wireframe Profile (plik `dorianos-wireframe-profile.webp`), `@Image 2` = Badge Lockup 640 px (`dorianos-badge-lockup.webp`) — tylko jako wzór liternictwa.
- Koszt: **10 908 kr. za 4 obrazy** (2 727/obraz). **Łącznie wydane: 32 724 kr.** (3 grupy, w tym 1 przypadkowa — patrz niżej). Zero wideo.

Prompt (identyczny dla 16:9 i 1:1):
```
Clean minimalist brand logo on a pure solid black background (#000000). Recreate the exact same glowing neon green-to-cyan wireframe low-poly head wearing a baseball cap in side profile (facing right) from the first reference image, with the same small radiating light dots and thin rays around it. Directly below the head, the wordmark DORIANOS written as one continuous word with exactly eight letters D-O-R-I-A-N-O-S, in bold white geometric sans-serif capitals with a subtle soft glow, letter style like the white lettering in the second reference image but WITHOUT the candlestick between the letters. Centered composition with generous empty black space around the logo. From the second reference image take only the lettering style: do NOT copy its circular badge, dark circle background or gold VIP medal. No VIP badge, no medal, no gold coin, no gold, no frame, no border, no square, no circle, no ring, no background shapes, no background gradient, no candlestick chart, no candles, no extra text, no tagline, no misspelled letters. Flat clean vector-like neon style, high detail, crisp sharp edges, premium tech brand identity.
```

## Jak znaleźć w Historii
`https://elevenlabs.io/app/image-video` → **Historia** → „10 lis” (na samej górze) → szukaj: `Clean minimalist brand logo on a pure solid black`.
Kolejność grup od najnowszej: **[A] 1:1 przypadkowa** → **[B] 1:1** → **[C] 16:9**. Grupy 1:1 = 4 kafelki w rzędzie (#1–#4 od lewej); grupa 16:9 = 2×2 (#1 lewy górny, #2 prawy górny, #3 lewy dolny, #4 prawy dolny).

## ★ LOGO_16x9 → grupa [C] 16:9, **wariant #4 (prawy dolny)** — 5504×3072 px
- ID: `content_generation/YBnusd0bEQ9CD4v3acWx/YNUCEuBH7WvQhce0FA0r`
- Rozpoznasz: najmniejsze logo w grupie, dużo czarnego marginesu dookoła (treść zajmuje ~19–82% wysokości kadru), napis DORIANOS mniejszy niż w #1–#3.
- Kontrola: litery D-O-R-I-A-N-O-S poprawne, ciągłe, bez świecy; brak VIP/medalu/ramki/okręgu; tło: piksele w rogach i na krawędziach = 0 (czyste #000), 86% kadru czarne.
- Alternatywy: #2 (prawy górny — większe logo, ok). #1 i #3 — napis za blisko dolnej krawędzi.

## ★ LOGO_1x1 → grupa [B] 1:1, **wariant #4 (skrajny prawy)** — 4096×4096 px
- ID: `content_generation/zsKfTnEE04XGWm8DktDL/xZwfWjE10ekpqVvJpttY`
- Rozpoznasz: najwęższy napis w rzędzie, równe marginesy boczne (~14%), głowa w czapce nad napisem.
- Kontrola: pisownia poprawna, czarne tło (rogi = 0), brak VIP/ramki. Alternatywa: #3. Odrzucone: #1 (napis przy krawędzi), #2 (napis prawie dotyka boków).

## Zapisane
- **Zasoby → folder „ZTT Teaser - wideo”**: ★ LOGO_16x9 i ★ LOGO_1x1 (opcja ⋮ → „Zapisz do zasobów”). W bibliotece Studio kafelki pokazują fragment promptu „Clean minimalist brand logo on a pure solid black…” (16:9 vs 1:1 rozróżnisz po kształcie miniatury). Nie weryfikowałem widoku folderu w Studio (strona /app/files zawiesiła moją kartę).
- **Zestaw marki DORIANOS → Logotypy**: dodane nowe logo **„DORIANOS Clean Neon Logo”** (★ 1:1 przeskalowane do 2048×2048 PNG, rola: brak, z opisem „no VIP, no badge, no frame…”). Badge Lockup pozostał jako Podstawowy — nic nie usunięto. Zestaw ma teraz 4 zasoby.

## Uwagi
- **Grupa [A] (1:1, najnowsza) = przypadkowa generacja** (niezamierzone kliknięcie podczas zamykania okna zestawu marki; +10 908 kr.). NIE UŻYWAĆ: #1 ma „DORI ANOS” z przerwą, #2 ma czarny kształt „kopuły” za głową.
- W Historii pojawiły się też 2 wpisy uploadu referencji (`dorianos-wireframe-profile.webp`, `dorianos-badge-lockup.webp`) — to tylko kopie zasobów zestawu.
- Do montażu: na czarnej karcie końcowej (#000) używaj ★ LOGO_16x9 pełnoekranowo — tło zleje się bez krawędzi.
- Kompozytor zostawiony czysty (bez promptu i referencji; model Nano Banana Pro, 1:1, 4K).
