# MANIFEST — SUNO: muzyka do teasera „ZTT: LICENCJA NA ZYSK”

Data: 2026-11-09. Konto Suno Doriana (`dorianos`), zalogowany w Chrome.

## WYNIKI (wznowienie 2026-11-09, po weryfikacji Cloudflare przez Doriana)
- 3× Create (A, B, C) w osobnej karcie, bez CAPTCHY. Przed każdym Create sprawdzone przez DOM: v6, Duration Custom 1:30, Exclude styles, Styles, Lyrics (same meta-tagi), tytuł.
- Kredyty: **2 360 → 2 330** (−30, czyli 10 za Create i 2 utwory). Zużyte 3 z 8 dozwolonych Create.
- Wszystkie 6 utworów: model V6, prywatne (nieopublikowane), nic nie pobrano ani nie usunięto.
- Instrumental: opisy stylu w Suno kończą się „instrumental, ‑vocals, ‑singing, ‑rap, ‑spoken word, ‑choir lyrics”, a pole Lyrics zawiera tylko tagi. Z opisu nic nie wskazuje na wokal, więc nie robiłem dogenerowania z pustym Lyrics. **Do potwierdzenia uchem.**

| # | Tytuł | Kierunek | Długość | Link |
|---|---|---|---|---|
| A1 | ZTT — Licencja A (Spy Groove) | A | 1:30 | https://suno.com/song/13258ff3-b75e-42bf-bd5e-db377a7eb656 |
| A2 | ZTT — Licencja A (Spy Groove) | A | 1:29 | https://suno.com/song/04a93b7b-1557-4a07-ae12-33576672ea89 |
| B1 | ZTT — Licencja B (Hybrid Trailer) | B | 1:30 | https://suno.com/song/148cc72e-3dc4-4178-908c-a41d70337266 |
| B2 | ZTT — Licencja B (Hybrid Trailer) | B | 1:30 | https://suno.com/song/8e7ba2b6-908a-4961-8675-d1cd5db19b58 |
| C1 | ZTT — Licencja C (Noir Jazz) | C | 1:30 | https://suno.com/song/1ace7210-f872-4156-b701-fc947eab75d1 |
| C2 | ZTT — Licencja C (Noir Jazz) | C | 1:30 | https://suno.com/song/1feae4eb-c165-4b77-a88b-d6a3f04f46f0 |

Uwagi z opisów Suno (to nie jest odsłuch):
- B2 ma w opisie „rising orchestral crescendo and abrupt impact”, a C2 ma „one huge orchestral hit with sub drop”. To najlepsi kandydaci na hit z ciszą po nim.
- A1 ma featured vibraphone i plate reverb na brass (ze strony utworu).

## (Historia) STATUS z pierwszej próby: ZABLOKOWANE PRZEZ CAPTCHA
- Po kliknięciu **Create** (kierunek A, formularz w pełni wypełniony) Suno wyświetliło okno **Cloudflare „Potwierdź, że jesteś człowiekiem”** (checkbox Turnstile).
  Odczekałem ok. 20 s i okno samo nie zniknęło. Agent nie rozwiązuje CAPTCHY, więc nie kliknąłem checkboxa i zatrzymałem pracę.
- Na liście My Songs nie pojawił się żaden utwór „ZTT —”, więc kredyty prawdopodobnie nie zostały pobrane (sprawdź saldo po swojej stronie).
- Nic nie zostało opublikowane, usunięte ani pobrane. Nie zmieniałem ustawień konta ani planu.
- **Jak odblokować:** Dorian otwiera suno.com/create i sam klika checkbox Cloudflare (albo generuje 3 kierunki ręcznie z promptów poniżej, ok. 2 min).
  Potem można ponownie uruchomić agenta.

## Konto / plan (z suno.com/account)
- Plan: **Pro** (miesięczny, kupiony na Androidzie). Data końca okresu: 11.11.2026 (odnowienie).
- Kredyty: **2 360** z 2 500/mies. Pobrania: 23 pozostałe.
- Licencja: Pro ma **„Commercial use rights”**. Utwory wygenerowane na Pro można użyć komercyjnie w teaserze.
  Dwie uwagi:
  - (a) czysto AI-owa muzyka w praktyce nie jest chroniona prawem autorskim. Prawa komercyjne to nie to samo co własność.
  - (b) Suno nie daje indemnifikacji, a pozwy UMG/Sony wciąż trwają. Dlatego w promptach są wyłącznie ogólne opisy gatunku: zero nazw filmów, kompozytorów, „Bond” czy „007”.
  - Przy dystrybucji oznacz treść jako AI, jeśli platforma tego wymaga.
- Plan nie pozwala na Suno Studio (stemy zaawansowane/MIDI ma tylko Premier). Pro ma 2 typy separacji stemów, co wystarczy do montażu.

## Ustawienia formularza (zweryfikowane w UI)
- Songs → **Advanced**, model **v6** (Pro; opis w UI: „Our best model yet”). Do wyboru są jeszcze v6-wild i v6-mini.
- **Duration: Custom = 1:30.** Suno v6 pozwala ustawić długość: suwak plus pole tekstowe. Wpisanie „1:30” zadziałało.
- **Instrumental:** UI v6 **nie ma przełącznika Instrumental**. Placeholder mówi: „Leave this empty for an instrumental”.
  Dlatego pole Lyrics zawiera wyłącznie meta-tagi w [nawiasach kwadratowych], bez zwykłych linii tekstu i bez nawiasów okrągłych (te Suno śpiewa jako chórki).
  Dodatkowo „instrumental” jest na początku Styles, a Exclude styles to: `vocals, singing, rap, spoken word, choir lyrics`.
  Wariant awaryjny: jeśli wyjdą wokale, wygeneruj ten sam Styles z **pustym** polem Lyrics (czysty tryb instrumentalny, ale bez kontroli struktury).
- Pozostałe opcje domyślne: Weirdness 50%, Style Influence 50%, Variety Normal, Max Mode Off, Personalize Off. Vocal Gender nieustawione.
- Prywatność: utwory Suno są prywatne, dopóki nie klikniesz „Publish”. Nie publikować.

## Prompty (do wklejenia 1:1)

### A — „ZTT — Licencja A (Spy Groove)” — orkiestrowo-elektroniczny spy groove
Styles (194 zn.):
```
instrumental cinematic spy thriller trailer, orchestral-electronic hybrid, dark luxurious, minor key, 105 BPM, staccato strings, brass stabs, synth pulse, ticking clock, vibraphone, upright bass
```
Lyrics / struktura:
```
[Intro: heartbeat pulse, ticking clock, low drone, single bass hits]
[Build: staccato strings enter, synth pulse, elegant and restrained]
[Rising: driving cinematic drums, brass stabs, cyber arpeggios]
[Groove: casino swagger, vibraphone, upright bass, muted guitar]
[Swell: fast orchestral crescendo]
[Hit: one massive orchestral hit with sub drop]
[Break: sudden silence]
[Outro: faint airy drone fading out]
[End]
```

### B — „ZTT — Licencja B (Hybrid Trailer)” — dark trap / hybrid trailer
Styles (192 zn.):
```
instrumental dark hybrid trailer, cinematic trap, minor key, 100 BPM, deep 808 bass, trailer hits, braams, cyber synth arpeggios, elegant piano and string melody, sub drop, tense and confident
```
Lyrics / struktura:
```
[Intro: ticking clock, dark drone, heartbeat sub pulse]
[Build: elegant piano motif, low strings, filtered 808]
[Rising: trap hi-hats, braams, cyber arpeggios, trailer drums]
[Drop: confident dark trap groove, 808 slides, string stabs]
[Swell: riser, accelerating percussion, orchestral crescendo]
[Hit: massive trailer impact with sub drop]
[Break: sudden silence]
[Outro: fading airy drone]
[End]
```

### C — „ZTT — Licencja C (Noir Jazz)” — noir jazz-electronica
Styles (187 zn.):
```
instrumental noir jazz electronica, smoky casino lounge, seductive minor groove, 100 BPM, upright bass, brushed drums, vibraphone, muted guitar, cold synths, ending on huge orchestral hit
```
Lyrics / struktura:
```
[Intro: smoky room tone, ticking clock, lone upright bass notes]
[Build: brushed drums, cold synth pads, muted guitar]
[Rising: tighter drums, vibraphone runs, pulsing synth bass]
[Groove: seductive casino swagger, upright bass walk, vibraphone, brushes]
[Swell: strings and brass rise fast, crescendo]
[Hit: one huge orchestral hit with sub drop]
[Break: sudden silence]
[Outro: fading cold synth drone]
[End]
```
Wspólne dla A/B/C: Exclude styles `vocals, singing, rap, spoken word, choir lyrics`, Duration Custom 1:30, model v6.

## Utwory
| Tytuł | Kierunek | Długość | Link |
|---|---|---|---|
| — | A | — | nie wygenerowano (CAPTCHA) |
| — | B | — | nie wygenerowano |
| — | C | — | nie wygenerowano |

## Uwagi do odsłuchu (gdy powstaną)
- Szukać take'u z wyraźnym pojedynczym hitem i ciszą po nim. Hit da się przesunąć w montażu tak, żeby wypadł na 1:06 (cięcie na transjencie).
- Suno nie trzyma się timecode'ów co do sekundy. Tagi ustalają kolejność sekcji, nie ich dokładny czas.
- Odrzucić każdy take, w którym pojawia się wokal albo coś przypomina znany motyw szpiegowski (riff gitarowy itp.).
- Zapas już istnieje w ElevenLabs: ★ MUS_MAIN „Midnight Ledger” (zob. manifest-music.md).
