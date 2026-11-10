# MANIFEST WIDEO — BOHATER = DORIAN — część 1 (1A, 2B, 3A, 3B, 4A, 5A)
Data: 2026-11-09 · agent wideo „Dorian część 1"
Narzędzie: ElevenLabs → Obraz i wideo → Historia (`https://elevenlabs.io/app/image-video/history?modality=video`), sekcja „9 lis" (na górze).
Wszystkie: Seedance 2.5 (o ile nie zaznaczono), 16:9 · 1080p · 8 s · audio WŁ. Godziny = UTC (czas PL = +1 h).
Prompty: bloki z video-prompts-expanded.md, stary opis bohatera podmieniony na CHARACTER BLOCK v2 + linia o ukrytej twarzy;
na początku „The man is @Image 1 (keep his exact face)."; na końcu negatywów „no Ferrari logo, no red cap, no other brand logos, no headphones, no microphone, watch on his LEFT wrist".
Awatar podpinany: slot „Odniesienia obrazów" → ⋮ → Wybierz awatar → Dorian 00ZTT → styl „Headshot" (chip „@Headshot" = obraz 1).

## Generacje (przyrostowo)
| # | Ujęcie | Refy | Liczba | Start (UTC) | Szukaj (fragment prompta) |
|---|---|---|---|---|---|
| G1 | 1A | REF_DORIAN_SILHOUETTE #4 (@Image 1) | 2 (prawy kafelek: „Generowanie nie powiodło się”, bez opłaty) | 17:58 | `spiraling like an abstract vortex` |
| G2 | 2B | awatar Headshot (@Image 1) + REF_ZTT_UI #4 (@Image 2) | 2 | 18:00 | `no cap in this shot (wet short dark brown hair)` |
| G3 | 3A | awatar Headshot | 1 | 18:03 | `ending in a wide shot of the aft deck with the man in the foreground` |
| G4 | 3B | awatar Headshot + REF_DORIAN_JAW #2 (@Image 2) | 1 | 18:09 | `his jaw, half-smile and close framing below the eyes like @Image 2` |
| G5 | 4A | awatar Headshot + REF_ZTT_UI #4 (@Image 2) | 1 | 18:11 | `seated on a wooden jetty with a fishing rod` |
| G6 | 5A | REF_DORIAN_SILHOUETTE #4 (@Image 1) | 1 | 18:13 | `gentle half-orbit that always stays behind the man` |
| G7 | 3B (próba 2) | awatar Headshot + REF_DORIAN_JAW #2 | 1 | 18:19 | `the top edge of the frame cuts across his nose` |
| G8 | 1A zapas | **Veo 3.1** + REF_DORIAN_SILHOUETTE #4 | 1 | 18:30 | ten sam prompt co G1 (`spiraling like an abstract vortex`), chip Veo 3.1 |

## Oceny (klatki ~0,5 / 2,7 / 5,0 / 7,6 s + dodatkowe)
- **1A G1 klip lewy:** szmaragdowo-zielony tunel ze świec (spirala), BRAK białego koła (tylko ciepła złota poświata za sylwetką ~5 s). 0–5 s czarna sylwetka (czapka słabo czytelna w konturze), ~5,5 s+ bohater frontalnie w czapce, oczy w cieniu daszka, tap palcem, rosnąca zielona linia, zegarek na LEWYM nadgarstku ✔. Na czapce zielony napis typu „DORIANOS" (mały; sprawdzić w pełnej rozdz.). Bardzo dobry.
- **2B G2 prawy kafelek:** wychodzi z wody (0–3 s twarz widoczna, wzrok w dół, bez czapki), gest rozpinania pianki ~4–5 s → cięcie/przejście w smoking, potem patrzy na świecący zielono zegarek na LEWYM nadgarstku ✔, twarz poniżej oczu. **★ 2B, trym ~3,5–8 s.**
- **2B G2 lewy kafelek:** twarz w pełni frontalnie (wyjście z wody i w smokingu) — łamie zasadę ukrytej twarzy; zapas tylko na końcówkę (zegarek, ~7–8 s).
- **3A G3:** przelot z powietrza nad dziobem jachtu (0–4 s) → pokład o zachodzie: bohater w CZARNEJ czapce na 1. planie z profilu, z kieliszkiem, rozmawia z gościem; kobieta w SZMARAGDOWEJ sukni przy relingu, palmy na horyzoncie. Twarz z profilu (nie frontalnie). **★ 3A**, trym ~4–8 s (pokład) lub pełne 8 s z przelotem.
- **3B G4:** telefon z zieloną UI na stole, zegarek, potem ~4–8 s PEŁNA TWARZ w czapce (oczy spuszczone), na końcu profil — łamie „kadr poniżej oczu”; zegarek prawdopodobnie na PRAWYM nadgarstku. Odrzut (ew. 0–3 s jako insert telefonu). → próba 2 (G7) z kadrem cięty na nosie.
- **4A G5:** 0–5 s szeroki statyczny kadr: bohater w CZARNEJ czapce siedzi na pomoście nad zamgloną taflą o świcie, twarz ukryta pod daszkiem (patrzy w dół), wędka z czerwonym szczytówką; ~5,3 s cięcie na insert poniżej oczu (ciemna marynarka/płaszcz na koszuli od smokingu z muchą) → ~7 s zegarek na LEWYM nadgarstku świeci zielono, szczytówka się ugina → 8 s zacięcie wędką w górę. Pływaka w kadrze brak (zamiast niego czerwona szczytówka). Strój bardziej marynarka niż płaszcz. **★ 4A**, trym 0–2 s + 5–8 s (albo 3–8 s).
- **5A G6:** cały czas od tyłu, ręce za plecami, czarna czapka czytelna w konturze (z tyłu na pasku drobny zielony napis/łatka — mały), czerwone linie ataku rozbijają się o szmaragdową tarczę ~4–6 s, złote przepływy. Bohater się NIE odwraca. Na bokach konsolki z drobną pseudo-UI (nieczytelne). **★ 5A**, dowolne 4 s (najlepiej 3–7 s z tarczą).

## Zapisane do Zasoby → „ZTT Teaser - wideo" (UI nie pozwala nadać nazwy; nazwa auto `video_seedance-2-5_The man is @..._2026-11-09T…`)
- 3A (G3), 4A (G5), 2B (G2 prawy), 1A (G1 lewy), 5A (G6) — zapisane ok. 18:22–18:25 UTC (komunikat „Zapisano do zasobów"). Wersja „DORIAN" = wszystkie pliki z datą 2026-11-09T18:0x w nazwie (stare ★ mają daty 11-07).
- **3B G7 (próba 2):** telefon z zieloną UI na stole + dłoń z zegarkiem (0–3 s) → tilt na muchę → szczęka z zarostem i półuśmiech, kadr cięty na nosie (oczy/czapka poza kadrem ✔), złoty bokeh. Strona nadgarstka niejednoznaczna (ręka wchodzi z lewej). **★ 3B**, pełne 8 s lub 0,5–5 s. Zapisane do folderu.
- **1A G8 Veo 3.1 (zapas):** szmaragdowo-cyjanowy tunel, BEZ białego koła; ale bohater od początku frontalnie, twarz w półcieniu (oczy częściowo widoczne), duża emblema na czapce, podnosi PRAWĄ dłoń, rosnąca zielona linia. Gorszy od G1 → **zapas 1A** (tylko 0–3 s). NIE zapisany do folderu.

## ★ PODSUMOWANIE
| Ujęcie | ★ (Historia 9 lis) | Trym | Zapas |
|---|---|---|---|
| 1A | G1 lewy kafelek (Seedance) | 0–5 s sylwetka lub całość (od ~5,5 s frontalnie, oczy w cieniu daszka) | G8 Veo (0–3 s); stare ★ z 7 lis |
| 2B | G2 prawy kafelek (Seedance) | ~3,5–8 s | G2 lewy (tylko 7–8 s, twarz frontalnie) |
| 3A | G3 (Seedance) | 4–8 s pokład (lub całość z przelotem) | N2 Veo z manifest-video-A (stara twarz) |
| 3B | G7 próba 2 (Seedance) | 0,5–8 s | G4 (tylko 0–3 s insert telefonu) |
| 4A | G5 (Seedance) | 0–2 s + 5–8 s (lub 3–8 s) | — |
| 5A | G6 (Seedance) | 3–7 s | — |
Zapisane do Zasoby → „ZTT Teaser - wideo": 1A, 2B, 3A, 3B, 4A, 5A (6 plików, nazwy auto z datą 2026-11-09T18:..; „DORIAN" = daty 9.11 18:xx UTC).

## KOSZTY
Seedance 2.5 1080p 8 s: 8 naliczonych × 50 121 = 400 968 kr. (1A ×1 [2. klip nie powiódł się — bez opłaty], 2B ×2, 3A, 3B ×2, 4A, 5A) + Veo 3.1: 19 391 → **≈ 420 359 kr.** (budżet ~450 000; żadna generacja > 120 000).
Czas generacji Seedance dziś ~5–10 min; statusy „Prawie gotowe…” w UI odświeżają się dopiero po przeładowaniu/zmianie wyszukiwania.

## UWAGI TECHNICZNE
- Zmiana modelu (Seedance → Veo) usuwa referencje z kompozytora; ponowne „Odniesienie” potrafi dodać duplikat — sprawdzaj miniatury.
- Po przeładowaniu strony kompozytor wraca do 720p / 5 s — ustawiaj ponownie.
- Zapis do folderu: kafelek → „Więcej opcji” → „Zapisz do zasobów” → klik „ZTT Teaser - wideo” (tytuł okna zmienia się na „Zapisz do ZTT Teaser - wideo”) → Zapisz. Nadać nazwy nie można.
