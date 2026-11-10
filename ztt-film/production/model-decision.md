# DECYZJA MODELU WIDEO — ZTT: LICENCJA NA ZYSK
Data: 2026-11-07 · Agent: wideo sceny 1–5 · Narzędzie: ElevenLabs → Obraz i wideo → Wideo

## Mini-test na ujęciu 2B (pianka → smoking, pomost nocą)
Ten sam prompt (2B + dopisek o referencjach + "watch on his LEFT wrist"), 16:9, 1080p, 8 s, audio WŁ.,
referencje: awatar „Agent 00ZTT" (obrazy źródłowe, @Image 1) + ★ REF_ZTT_UI #4 (@Image 2).

| | Seedance 2.5 | Veo 3.1 |
|---|---|---|
| Koszt (1080p, 8 s) | **50 121 kr.** | **19 391 kr.** |
| Czas generacji | ~9–10 min | ~2 min |
| Referencje | przyjmuje (do 50 ref. obraz/wideo/audio) | przyjmuje obrazy (w trybie ref. długość zablokowana na 8 s) |
| Akcja | wychodzi z wody, **realnie rozpina piankę** (zamek), pod spodem smoking, poprawia mankiet, zegarek świeci na zielono — pełny beat dramaturgiczny | nogi w piance idą po pomoście → **morf/przenikanie** w smoking (bez rozpinania), potem zapina marynarkę i patrzy na świecący zegarek |
| Postać | szczęka, zarost, usta zgodne z awatarem; twarz kadrowana poniżej oczu | twarz praktycznie poza kadrem (sam podbródek) — mniej materiału do oceny zgodności |
| Zegarek | głównie lewy nadgarstek; w końcówce poza kadrem pozycja dwuznaczna | konsekwentnie lewy nadgarstek |
| Realizm / look | bardzo wysoki, piękny bokeh marina, anamorficzne flary | wysoki, nieco bardziej „reklamowy" |
| Tekst / bełkot | brak; drobne logo-podobne wytłoczenie na piersi pianki | brak |

## DECYZJA
- **Model wiodący dla ujęć z bohaterem (akcja aktorska, gest, identyfikacja postaci): Seedance 2.5** — lepiej wykonuje
  akcję opisaną w prompcie i trzyma postać z referencji. Koszt 2,6× wyższy, generacja ~10 min (kolejkować równolegle).
- **Veo 3.1 = zapas oraz wybór dla ujęć abstrakcyjnych / bez twarzy / „gadżetowych"** (tunel, hologram, walizka, auto, HUD) —
  3× tańszy, szybki, stabilny, dobrze trzyma lewy nadgarstek. Jeśli Seedance przekłamie akcję — dorób wariant w Veo.
- Wskazówki techniczne dla obu: patrz manifest-video-A.md (procedura referencji, helpery JS, pułapki).

## Dla agenta scen 6–10
- 6A (auto), 6B (HUD w kokpicie): Veo 3.1 (taniej, geometria auta stabilna); referencja REF_CAR #4 dla 6A.
- 7A/7B (kasyno), 8A/8B (traderzy), 10A/10B: Seedance 2.5 + awatar Agent 00ZTT (+ REF_FEMME #3 w 7A/7B, REF_ZTT_UI #4 przy telefonie/zegarku).
- 10B (jedyne pełne odsłonięcie twarzy) — koniecznie Seedance + awatar; to tam zgodność twarzy jest krytyczna.
- 9A/9B (tłum): zacznij od Veo 3.1 (tanio, dużo prób), Seedance tylko jeśli Veo gubi anatomię.
