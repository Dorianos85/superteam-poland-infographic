# ZTT: LICENCJA NA ZYSK — Muzyka i SFX (ElevenLabs)
## Plik 05 — prompty Music + SFX + mix notes (v1.0)

> **PRAWNIE KRYTYCZNE:** żadnych nawiązań do melodii z Jamesa Bonda (temat
> Monty'ego Normana / aranże Johna Barry'ego są chronione). W promptach NIE
> używamy słów „James Bond", „007", „Bond theme". Zamawiamy **własny motyw**
> w estetyce gatunku spy-thriller — to jest bezpieczne; cytat melodyczny nie jest.
> Po wygenerowaniu odsłuchaj: jeśli coś brzmi jak znany riff gitarowy z Bonda —
> odrzuć take i regeneruj.

---

## 1. ElevenLabs Music — główny utwór (75 s)

Struktura pod scenariusz (02): 0:00 tension intro → build od 0:14 →
0:43 casino swagger → 0:59 crowd swell → 1:06 finale hit → outro w ciszy
z pojedynczym alertem (alert dodajemy w montażu, muzyka ma zostawić ciszę).

### Prompt PEŁNY
```
Original cinematic spy-thriller trailer cue, 75 seconds, orchestral-electronic
hybrid "spy groove". Dark, luxurious, confident — Monte Carlo at night, not action
chaos. Instrumentation: low pulsing synth bass, ticking percussive clock/market-tick
rhythm, tense staccato strings, brooding brass swells, vibraphone and muted-guitar
accents, modern cinematic drums.

Structure:
0:00–0:06 tension intro — near-silent heartbeat pulse and ticking clock, low drone,
single bass note hits;
0:06–0:28 slow build — strings enter, groove assembles, understated and elegant;
0:28–0:43 rising intensity — driving percussion, brass stabs, cyber-tension arpeggios;
0:43–0:59 casino swagger — confident mid-tempo groove with jazzy vibraphone,
upright-bass feel, sly and seductive;
0:59–1:06 crowd swell — orchestra and choir-like pads rise rapidly, anticipation;
1:06–1:08 single massive finale hit (full orchestra + sub drop);
1:08–1:15 outro — abrupt near-silence, only a faint airy drone tail, leaving room
for a single notification sound.

Instrumental only, no vocals. Key: minor. Tempo around 100–110 BPM.
IMPORTANT: a fully original melody and theme — do NOT reference, quote or imitate
any existing film franchise theme or any copyrighted spy movie melody.
```

### Prompt KRÓTKI
```
75s original cinematic spy-thriller trailer cue, orchestral-electronic hybrid groove:
ticking-clock tension intro, slow elegant build, confident jazzy casino swagger at
0:43, rapid orchestral swell at 0:59, one massive hit at 1:06, then abrupt silence
with airy drone outro. Dark, luxurious, minor key, ~105 BPM, instrumental, fully
original theme — no reference to any existing spy franchise melody.
```

### Praktyka
- Generuj 3–4 warianty pełnego prompta; wybierz ten z najczystszym hitem na 1:06.
- Jeśli timing sekcji nie trafia co do sekundy — tnij w DaVinci/CapCut na alertach
  (muzyka hybrydowa dobrze znosi cięcia na transjentach).
- Zamów też wariant „no percussion intro" jako zapas pod cut-downy 30 s / 15 s.

---

## 2. Firmowy ALERT ZTT (sound branding)

Jeden dźwięk, <1 s, powtarzany w całym filmie i docelowo w aplikacji.
Charakter: „odbezpieczenie broni + tick rynku" — metaliczno-cyfrowy, elegancki,
czytelny na głośniku telefonu. Generuj w ElevenLabs SFX (duration ~0.7–1.0 s,
prompt influence wysoki), po 5–10 take'ów na prompt.

### Prompt A (główny)
```
Short premium notification sound, under 1 second: a crisp metallic mechanical
click like a precision weapon being cocked, instantly followed by a clean digital
market-ticker blip, subtle rising pitch, glassy hi-tech tail, tight and punchy,
no reverb wash.
```

### Prompt B (bardziej cyfrowy)
```
Ultra-short UI alert, 0.8 seconds: polished steel click-clack transient merged
with a single sonar-like digital ping that bends slightly upward, minimal,
expensive-sounding, dark undertone, clean ending.
```

### Prompt C (wariant „cichy" do Sceny 1 i finału)
```
Very quiet, intimate version of a metallic-digital notification: soft weapon-safety
click plus faint electronic tick, whisper-level, short decay, tense and discreet.
```

- Wybierz JEDEN take jako kanoniczny (`ALERT_ZTT_master.wav`); wariant cichy
  (Prompt C) używany tylko na 0:00 i w outro — ma być tym samym motywem, więc
  jeśli C brzmi inaczej niż A, zrób wersję cichą przez obniżenie gainu A o 12–15 dB
  + filtr LPF 8 kHz zamiast osobnego dźwięku.
- Test obowiązkowy: odsłuch na głośniczku telefonu — alert ma być czytelny i tam.

---

## 3. SFX scena po scenie (ElevenLabs SFX)

Format: PL opis → prompt EN. Generuj 2–3 take'y, duration dobieraj do ujęcia.

| # | Scena (timecode) | PL opis | Prompt EN |
|---|---|---|---|
| 1 | Lufa ze świec (0:00–0:06) | Puls serca + tykanie zegara rynku; „cyfrowa fala" po tapnięciu | `Slow tense heartbeat mixed with a ticking clock, dark cinematic ambience, building suspense` oraz `Smooth digital ripple whoosh, glassy energy wave expanding, sci-fi interface sound` |
| 2 | Pod wodą (0:06–0:14) | Ambient podwodny, bąbelki, stłumiona głębia; wyjście na pomost nocą, rozpinanie pianki | `Deep underwater ambience, muffled low rumble, slow bubbles, scuba breathing through regulator` oraz `Night harbor ambience, gentle waves against wooden dock, wet footsteps, zipper being unzipped` |
| 3 | Jacht (0:14–0:22) | Pokład jachtu o zachodzie: fale, mewy, śmiech i kieliszki; wibracja telefonu na stoliku | `Luxury yacht deck ambience at sunset, gentle sea waves, distant seagulls, soft laughter and clinking glasses` oraz `Phone vibrating once on a glass table, short buzz` |
| 4 | Ryby o świcie (0:22–0:28) | Mgła nad jeziorem — cisza, pojedyncze ptaki; plusk spławika i świst podcięcia | `Calm misty lake at dawn, sparse birdsong, near silence, subtle water lapping` oraz `Fishing float splash, sharp rod whip swish, reel click, water droplets` |
| 5 | War room (0:28–0:36) | Szum serwerowni / sali operacyjnej; hologram, uderzenie cyberataku o tarczę; otwarcie walizki | `Server room hum, low electronic ambience, quiet data-center fans, occasional soft beeps` oraz `Holographic interface glitch impact, energy shield deflection hit, deep digital thud` oraz `Aluminum briefcase latches clicking open, smooth mechanical unfolding` |
| 6 | Auto nocą (0:36–0:43) | Gran turismo na serpentynach: silnik V8/V12, redukcja biegu, opony; subtelny „szum" HUD | `Classic grand tourer V12 engine on winding road at night, aggressive downshift, throaty exhaust, tires gripping asphalt` oraz `Soft futuristic HUD projection hum, subtle interface whir` |
| 7 | Kasyno (0:43–0:52) | Kulka ruletki, żetony, gwar eleganckiego kasyna | `Roulette ball spinning and rattling into pocket, casino wheel clicks` oraz `Elegant casino ambience, quiet murmur, poker chips stacking and sliding across felt` |
| 8 | Dom traderów (0:52–0:59) | Biurowy gwar trading house: klawiatury, ciche piknięcia, obracany monitor | `Modern trading floor ambience, mechanical keyboards typing, quiet notification pings, office room tone` oraz `Computer monitor being swiveled on its stand, soft plastic creak` |
| 9 | Event (0:59–1:06) | Hala konferencyjna — tłum; setki telefonów naraz (warstwa alertów); narastający szum tłumu | `Large conference hall crowd murmur, spacious reverb, anticipation` oraz `Hundreds of phone notifications going off in a crowd, layered chimes rising` (warstwowo pod ALERT_ZTT) oraz `Crowd murmur swelling into excited chatter and gasps` |
| 10 | Finał (1:06–1:15) | Wiatr na dachu wieżowca, miasto nocą w oddali; „złożenie się" świateł w logo (cyfrowy shimmer); cięcie do czerni | `Rooftop wind at night, distant city traffic hum, high altitude ambience` oraz `Magical digital shimmer, city lights assembling into a logo, soft crystalline whoosh resolving into silence` |

Nazewnictwo: `SFX_<scena>_<slug>_t<take>.wav`, np. `SFX_06_downshift_t2.wav`.
Ambienty generuj w max długości i loopuj w montażu; pojedyncze zdarzenia
(plusk, walizka, ruletka) jako krótkie one-shoty z wysokim prompt influence.

---

## 4. Mix notes

### Hierarchia (od góry)
1. **ALERT ZTT** — zawsze czytelny, nic go nie maskuje. Każde wystąpienie na tym
   samym poziomie (szczyt ok. **-8 dBFS**, wyjątki: cichy wariant 0:00 i outro).
   Jeśli muzyka gra — sidechain/duck muzyki o 3–4 dB na 0,5 s wokół alertu.
2. **VO** — ok. **-6 dB głośniej niż muzyka** w momentach narracji. Technicznie:
   VO szczyty ok. -6 dBFS, muzyka pod VO zduckowana do ok. -18 ÷ -20 dBFS RMS.
   Ducking automatyczny (sidechain kompresor na busie muzyki, key = VO; attack
   ~10 ms, release ~300–400 ms) albo ręczne keyframe'y w CapCut.
3. **Muzyka** — prowadzi tam, gdzie nie ma VO (intro, 0:43 swagger, finale hit).
   Finale hit 1:06 może sięgnąć pełnej głośności — potem CAŁKOWITA cisza przed
   ostatnim alertem (to jest puenta dźwiękowa filmu).
4. **SFX/ambienty** — podłoga: -25 ÷ -35 dBFS, one-shoty (plusk, downshift,
   ruletka) punktowo wyżej, ale nigdy nad VO ani alertem.

### EQ / porządki
- Muzyka: lekki notch 2–4 kHz (pasmo zrozumiałości VO) podczas narracji.
- VO: HPF 80–100 Hz, de-esser jeśli klon syczy; zero ciężkiego reverbu —
  narrator jest „w głowie widza", nie w pokoju.
- Alert: zostaw mu wolne 3–6 kHz w miksie — tam siedzi jego czytelność.

### Mastering / delivery
- **YouTube (master 16:9):** głośność integralna **-14 LUFS**, true peak **-1 dBTP**
  (limiter na końcu łańcucha). Nie wyżej — YouTube i tak znormalizuje w dół,
  a straci dynamika ciszy w outro.
- **TikTok / Reels / Shorts (cut-downy 9:16):** głośniej i gęściej — cel ok.
  **-11 ÷ -12 LUFS**, true peak -1 dBTP, mocniejsza kompresja busa (gęsty miks
  wygrywa na głośniku telefonu). Sprawdź cały miks w mono — telefony tną stereo.
- Eksport: WAV 48 kHz/24-bit do mastera wideo (standard filmowy); audio
  generowane w 44.1 kHz konwertuj raz, na końcu, nie per plik.
- Finalny test: odsłuch na (1) słuchawkach, (2) głośniku telefonu, (3) laptopie.
  Kryterium zaliczenia: każda linia VO zrozumiała, każdy alert słyszalny,
  cisza w outro naprawdę cicha.
