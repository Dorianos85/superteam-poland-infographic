# MANIFEST VO EN — „ZTT: LICENSE TO PROFIT" (ElevenLabs TTS)

Data sesji: 2026-11-10 · konto Doriana (Scale) · Text to Speech → Historia + wybrane take'i w **Zasobach → folder „ZTT License to Profit - VO EN"** (14 plików).
Nic nie pobierano na dysk. Projektu Studio nie ruszano.

## 1. Model i ustawienia

| | Dorian (EN_VO_01–09) | Femme fatale (EN_FF) |
|---|---|---|
| Głos | **Dorian's Telegram** (klon, `ADCIBDDMDpyKxIQX0m8Y`) | ★ **Blondie - Femme Fatale** (Voice Library, English/British). ALT: Lena - Velvety & Trustworthy (`d26eMDXtCFizSzBVHFFS`) |
| Model | **Eleven v4**. Każdy klik daje 2 warianty: Generacja 1 = `eleven_v4`, Generacja 2 = `eleven_v4_exp` | Eleven v4 |
| Stabilność / Podobieństwo | 0.50 / 0.80 | 0.45 / 0.75 (jak FF w PL) |
| Język (nadpisanie) | **Angielski** | Angielski |
| Format | MP3 44,1 kHz 128 kbps, bez efektów audio, bez „Automatycznego tagowania” | to samo |

**Koszt:** licznik kredytów spadł z 4 092 000 do 4 089 076, czyli **ok. 2,9 tys. kredytów** za 37 generacji (74 warianty). Szczegóły w Historii pokazują „Użyto 0 kredytów”. Budżet 50 tys. nienaruszony.

**Pomiar długości:** każdy wariant zdekodowany w przeglądarce (`decodeAudioData` na pliku MP3 z odtwarzacza), w sekundach. Każdy ★ dodatkowo zweryfikowany po otwarciu go w Historii („Pokaż szczegóły” → Odtwórz → dekodowanie). Rozmiar pliku w Zasobach zgadza się z długością (≈16,9 kB + 16 kB/s).
**Uwaga do v4 vs v4_exp w Historii:** panel szczegółów pokazuje dla obu „Eleven v4”, a kolejność na liście nie jest stała. Warianty rozróżniałem **po długości i ID generacji** (tabela niżej).

### Dlaczego FF to nie Lena
Lena ma zweryfikowane języki: PL, FR, NO, HR, MS, SK, BG, VI, SV, AR, EL, DA, HU, UK, TR, ES, PT, NL, ZH, KO, DE. **Angielskiego na liście nie ma**, a UI przy jej wyborze pokazuje „Najlepsze rezultaty uzyskasz, używając głosu w języku Angielski”. Jej take'i nie są podejrzanie długie (1.72–2.85 s), ale akcent jest ryzykowny. Dlatego z Voice Library (filtry: English, Brytyjski, Kobieta, fraza „sultry”) wybrałem:
**Blondie - Femme Fatale**, opis z Biblioteki: „Sultry, captivating female voice — ideal for romantic-seductive content and intimate narrations.” Akcent brytyjski, notice period 2 lata, ok. 11 tys. użyć, bez ikony dopłaty ($). Na płatnym planie (Scale) głosy z Voice Library można używać komercyjnie.
Lena została zapisana jako ALT, jeśli w EN ma brzmieć ta sama kobieta co w PL.

## 2. ★ (dokładne długości do przeliczenia ściszania muzyki)

| ID | Max len | ★ długość [s] | Wariant | ID generacji | Plik w Zasobach | Tekst (z tagami) |
|---|---|---|---|---|---|---|
| EN_VO_01 | 4.5 | **3.97** (3.971) | v4 | M9Ct6BerfqOKZF0HIXhF | EN_VO_01_STAR | `[whispering in the dark, slow] There are places... [pause] nothing can reach.` |
| EN_VO_02 | 4.5 | **3.87** (3.866) | v4/v4_exp (identyczna długość) | MKktELyDRDu4qhnvKIao | EN_VO_02_STAR | `[calm satisfaction, slow] ...yet everything... that matters... reaches me.` |
| EN_VO_03 | 4.0 | **3.79** (3.788) | v4/v4_exp (identyczna długość) | 6srk1dbL7OVqW0J39LIv | EN_VO_03_STAR | `[calm, slow, low voice] The chart never runs from me. [brief pause] [low, final] Ever.` |
| EN_VO_04 | 6.5 | **6.19** (6.191) | v4 | (Historia: „[serious] I see the flow”) | EN_VO_04_STAR | `[serious] I see the flow of information. [pause] And capital. [pause] [intense] I see attacks before they come.` |
| EN_VO_05 | 3.8 | **3.47** (3.474) | v4_exp | HP5HucpM1t8QQfkLGrsa | EN_VO_05_STAR | `[confident, low register, slow] I'm armed... [long pause] to the teeth.` |
| EN_FF | 3.0 | **2.77** (2.769) | v4_exp | Afl9t3n5M2Mh5OY7eE2x | EN_FF_STAR (Blondie) | `[sultry, amused, slow] What's... your game?` |
| EN_VO_06 | 3.5 | **3.08** (3.082) | v4_exp | 6czvfOXoGPM5dDuyIA2J | EN_VO_06_STAR | `[calm] I don't play. [pause] [confident] I see.` |
| EN_VO_07 | 2.0 | **1.57** (1.567) | v4/v4_exp (identyczna długość) | XieqP1rQWxNCyxLg8oSO | EN_VO_07_STAR | `[casual] Profits locked in?` |
| EN_VO_08 | 3.2 | **3.16** (3.161) | v4 | fH3fUYru4VlQ6UcCX8A3 | EN_VO_08_STAR | `[whispers][slow] They all... [pause] already know.` |
| EN_VO_09 | 5.4 | **5.25** (5.251) | v4 | 7dwGxbhTnI0ksaonFjWA | EN_VO_09_STAR | `[low, intimate] And you? [long pause] [confident] Catch the trend — before it catches YOU.` |

### ALT (też w folderze)
| Plik | Długość [s] | Wariant / ID | Tekst |
|---|---|---|---|
| EN_VO_03_ALT | **3.55** (3.553) | v4 | `[calm][slow] The chart never runs from me. [pause] [confident] Ever.` |
| EN_VO_06_ALT | **3.00** (3.004) | v4 · OfCgcssJfkansuAfgr1t | `[quiet, intimate, unhurried] I don't play. [brief pause] [firm, low] I see.` |
| EN_VO_09_ALT | **4.99** (4.989) | v4 · 7SbQFHmNrwo31ySZfftE | `[direct, to camera] And you? [brief pause] [slow, weighty, confident] Catch the trend — before it catches you.` |
| EN_FF_Lena_ALT | **2.85** (2.847) | v4/v4_exp (identyczna długość) · 2bFmwJR1aC8vc44oipsb | Lena: `[sultry, amused, slow] What's... your game?` |

## 3. Wszystkie take'i (`tN: v4 / v4_exp`, sekundy)

**EN_VO_01** (max 4.5)
- t1 `[whispering in the dark] There are places... nothing can reach.` — 2.93 / 3.16
- t2 `[whispers, slow, intimate] There are places... [brief pause] nothing can reach.` — 3.71 / 3.71
- t3 `[whispering, confiding] There are places... nothing... can reach.` — 3.24 / 3.40
- **t4 ★** `[whispering in the dark, slow] There are places... [pause] nothing can reach.` — **3.97** / 3.79
- (t1–t3 wygenerowane 2× przez błąd pomiaru, więc w Historii są duplikaty)

**EN_VO_02** (max 4.5)
- t1 `[calm satisfaction, slight smile] ...yet everything that matters reaches me.` — 3.16 / 3.08 (2×)
- t2 `[confident] ...yet everything that matters... [brief pause] reaches me.` — 3.24 / 3.16
- t3 `[calm, relaxed, slight smile] ...yet everything that matters reaches me.` — 3.08 / 3.16
- **t4 ★** `[calm satisfaction, slow] ...yet everything... that matters... reaches me.` — **3.87** / 3.87

**EN_VO_03** (max 4.0)
- **t1 ★** `[calm, slow, low voice] The chart never runs from me. [brief pause] [low, final] Ever.` — **3.79** / 3.79
- t2 (ALT) `[calm][slow] The chart never runs from me. [pause] [confident] Ever.` — **3.55** / 3.47
- t3 `[calm, low voice] The chart never runs from me... [confident, deeper] Ever.` — 3.32 / 3.16
- t4 `[low, steady voice] The chart never runs from me. [long pause] [lower, final] Ever.` — 4.13 ⚠ / 4.36 ⚠ (za długie)
- t5 `[calm, morning quiet] The chart never runs from me... [firm, low] Ever.` — 3.32 / 3.08

**EN_VO_04** (max 6.5)
- t1 `[cold, measured intelligence briefing] I see the flow of information. [brief pause] And capital. [rising tension] I see attacks before they come.` — 5.72 / 5.80
- **t2 ★** `[serious] I see the flow of information. [pause] And capital. [pause] [intense] I see attacks before they come.` — **6.19** / 5.88
- t3 `[serious, low] I see the flow of information... And capital... [intense, slightly faster] I see attacks — before they come.` — 5.49 / 5.64

**EN_VO_05** (max 3.8)
- t1 `[confident][slow] I'm armed... [pause] to the teeth.` — 2.69 / 2.85
- t2 `[low, dry irony] I'm armed... [brief pause] to the teeth.` — 2.77 / 2.93
- **t3 ★** `[confident, low register, slow] I'm armed... [long pause] to the teeth.` — 3.24 / **3.47**

**EN_VO_06** (max 3.5)
- **t1 ★** `[calm] I don't play. [pause] [confident] I see.` — 2.93 / **3.08**
- t2 (ALT) `[quiet, intimate, unhurried] I don't play. [brief pause] [firm, low] I see.` — **3.00** / 2.93
- t3 `[calm] I don't play... [confident] I SEE.` — 3.00 / 2.77
- t4 `[calm, low voice] I don't play. I see.` — 2.51 / 2.51
- t5 `[calm, cool] I don't play. [long pause] [confident, deliberate] I see.` — 4.13 ⚠ / 4.36 ⚠ (za długie)

**EN_VO_07** (max 2.0)
- **t1 ★** `[casual] Profits locked in?` — **1.57** / 1.57
- t2 `[casual, tossed off, rising intonation] Profits locked in?` — 1.49 / 1.57
- t3 `[offhand] Profits... locked in?` — 2.12 ⚠ / 2.12 ⚠ (ponad okno)

**EN_VO_08** (max 3.2)
- t1 `[whispers, mysterious] They all... already know.` — 2.59 / 2.77
- **t2 ★** `[whispers][slow] They all... [pause] already know.` — **3.16** / 3.32 ⚠
- t3 `[whispering in awe] They all... [brief pause] already... know.` — 3.47 ⚠ / 3.71 ⚠
- t4 `[whispers, mysterious, slow] They all... already... know.` — 3.32 ⚠ / 3.40 ⚠

**EN_VO_09** (max 5.4)
- **t1 ★** `[low, intimate] And you? [long pause] [confident] Catch the trend — before it catches YOU.` — **5.25** / 5.15
- t2 (ALT) `[direct, to camera] And you? [brief pause] [slow, weighty, confident] Catch the trend — before it catches you.` — **4.99** / 4.83
- t3 `[serious] And you? [pause] [confident][slow] Catch the trend — before it catches you.` — 4.99 / 4.99
- t4 `[low, intimate] And you? [pause] [slow, final, resolute] Catch the trend... before it catches you.` — 4.99 / 4.75
- t5 `[serious, low voice] And you? [brief pause] [confident] Catch the trend — before it catches you.` — 4.13 / 4.13

**EN_FF „What's your game?”** (max 3.0)
| Take | Lena (v4 / v4_exp) | Blondie (v4 / v4_exp) |
|---|---|---|
| t1 `[sultry][slow] What's your game?` | 1.96 / 2.04 | 2.19 / 2.12 |
| t2 `[low, velvety, seductive voice] What's your game?` | 1.72 / 1.72 | 1.80 / 1.72 |
| t3 `[sultry, amused, slow] What's... your game?` | **2.85 / 2.85 (ALT)** | 3.00 ⚠ (3.004, minimalnie ponad) / **2.77 ★** |
| t4 `[sultry, amused] What's your... game?` | 2.59 / 2.69 | 2.59 / 2.69 |

Kontrola tagów: żaden take nie ma długości sugerującej przeczytanie tagu na głos. Najdłuższe nadwyżki (VO_03 t4, VO_06 t5) wynikają z `[long pause]`. Opisowe tagi (np. VO_04 t1) nie wydłużają linii.
★ wybrane **wyłącznie po czasie** (mieści się w Max len, możliwie blisko). Nie odsłuchałem ich, więc przed montażem trzeba sprawdzić na słuchawkach wymowę EN klona i połknięte tagi.

## 4. Gdzie to leży
- **Zasoby → „ZTT License to Profit - VO EN”** (14 plików .mp3): `EN_VO_01_STAR`, `EN_VO_02_STAR`, `EN_VO_03_STAR`, `EN_VO_03_ALT`, `EN_VO_04_STAR`, `EN_VO_05_STAR`, `EN_VO_06_STAR`, `EN_VO_06_ALT`, `EN_VO_07_STAR`, `EN_VO_08_STAR`, `EN_VO_09_STAR`, `EN_VO_09_ALT`, `EN_FF_STAR` (Blondie), `EN_FF_Lena_ALT`.
- Pozostałe take'i są w **Text to Speech → Historia** (10 lis). Szukaj po fragmencie tekstu (np. „The chart never runs”). Warianty v4 i v4_exp rozróżnisz po długości z tabeli wyżej.

## 5. Uwagi
- Klon „Dorian's Telegram” to głos polski. Przy angielskim UI pokazuje „Najlepsze rezultaty uzyskasz, używając głosu w języku Angielski”. Akcent PL w EN może być OK, bo bohater mówi własnym głosem, ale trzeba to ocenić na słuch.
- Stan edytora TTS się zmienił. Wcześniej był tam tekst Doriana „Zaczyna się od darmowego Money Health Check…” (CoachFi, głos Dorian's Telegram, Multilingual v2, język Polski). Teraz edytor ma tekst FF, głos Blondie, Eleven v4 i angielski. Ten tekst jest prawdopodobnie w Historii TTS, a jeśli nie, trzeba go wpisać ponownie.
- Głos Blondie został użyty z poziomu wyboru głosu (Odkrywaj). Mógł się przez to dodać do „Moich głosów”.
