# ZTT: LICENCJA NA ZYSK — Voiceover w ElevenLabs
## Plik 04 — skrypt VO + ustawienia (v1.0)

Głos: **sklonowany głos właściciela** (Professional Voice Clone w ElevenLabs).
Język: polski. Model docelowy: **Eleven v3** (audio tagi w nawiasach kwadratowych
są interpretowane przez model, nie są czytane na głos). Fallback: `eleven_multilingual_v2`
(wtedy tagi USUNĄĆ — v2 je przeczyta jako tekst).

---

## 1. Skrypt VO z timecode'ami (wersja pod Eleven v3 z audio tagami)

Konwencja: każda linia = osobna generacja. Tag na początku ustawia ton całej linii,
tagi w środku sterują mikro-dramaturgią. `[pause]` = krótkie zawieszenie.

---

### VO_01 — Scena 2, POD WODĄ (0:10–0:14)
```
[whispers] Są miejsca... [pause] do których nie dociera nic...
```
**Wskazówka aktorska:** bardzo wolno, półszeptem, jak zwierzenie w ciemności — zdanie ma wisieć w powietrzu, bo kończy je dopiero linia VO_02.

---

### VO_02 — Scena 3, JACHT (0:16–0:21)
```
[confident] ...do mnie dociera wszystko, [pause] co ważne.
```
**Wskazówka aktorska:** spokojna satysfakcja z półuśmiechem, głośniej niż VO_01, ale wciąż bez wysiłku — puenta, nie przechwałka.

---

### VO_03 — Scena 4, RYBY O ŚWICIE (0:24–0:28)
```
[calm][slow] Wykres mi nie ucieka. [pause] [confident] Nigdy.
```
**Wskazówka aktorska:** pierwsze zdanie jak stwierdzenie faktu przy porannej ciszy, „Nigdy" twardo i o pół tonu niżej — to jest tagline, musi siedzieć.

---

### VO_04 — Scena 5, WAR ROOM (0:29–0:36)
```
[serious] Widzę przepływy informacji. [pause] I kapitału. [pause] [intense] Widzę ataki, zanim nadejdą.
```
**Wskazówka aktorska:** rytm wyliczanki wywiadowczej — równe, chłodne frazy, a na „zanim nadejdą" lekkie przyspieszenie i napięcie w głosie.

---

### VO_05 — Scena 6, AUTO NOCĄ (0:38–0:42)
```
[confident][slow] Jestem uzbrojony... [pause] po zęby.
```
**Wskazówka aktorska:** niski rejestr, cień ironii, pauza przed „po zęby" jak zmiana biegu — linia leży na warkocie silnika, więc krótko i gęsto.

---

### VO_06 — Scena 7, KASYNO — dialog agenta (0:47–0:50)
```
[calm] Ja nie gram. [pause] [confident] Ja widzę.
```
**Wskazówka aktorska:** powiedziane prosto w oczy, cicho i bez pośpiechu — „widzę" z naciskiem, ale bez podnoszenia głosu; to flirt i groźba naraz.

---

### VO_07 — Scena 8, DOM TRADERÓW — dialog agenta (0:53–0:55)
```
[casual] Zrealizowane zyski?
```
**Wskazówka aktorska:** rzucone od niechcenia, jak hasło-odzew między swoimi; lekka intonacja pytająca w górę, zero teatru.

---

### VO_08 — Scena 9, EVENT (1:02–1:05)
```
[whispers][slow] Oni wszyscy... [pause] już wiedzą.
```
**Wskazówka aktorska:** szept nad morzem rozświetlonych telefonów — tajemniczo, prawie z podziwem, ostatnie słowo wyraźnie oddzielone.

---

### VO_09 — Scena 10, FINAŁ (1:08–1:14)
```
[serious] A Ty? [pause] [confident][slow] Złap trend — zanim złapie Ciebie.
```
**Wskazówka aktorska:** „A Ty?" wprost do widza, potem call-to-action wolno i z wagą — ostatnie słowo musi wybrzmieć przed finałowym ALERTEM w ciszy.

---

### Tagi — ściąga
| Tag | Działanie | Gdzie używamy |
|---|---|---|
| `[whispers]` | szept | VO_01, VO_08 |
| `[confident]` | pewność siebie | VO_02, VO_03, VO_05, VO_06, VO_09 |
| `[calm]` | spokój, niski puls | VO_03, VO_06 |
| `[serious]` / `[intense]` | powaga / napięcie | VO_04, VO_09 |
| `[slow]` | zwolnienie tempa | VO_03, VO_05, VO_08, VO_09 |
| `[pause]` | zawieszenie | wszędzie tam, gdzie montaż tnie na alert |

Uwaga: wielokropek `...` i myślnik `—` też wymuszają pauzy — używamy ich razem
z tagami. Jeśli model „połknie" tag albo zrobi z niego artefakt — regeneruj take,
to normalne w v3.

---

## 2. Ustawienia ElevenLabs dla klona głosu

### Wybór modelu
- **`eleven_v3`** — pierwszy wybór dla tego materiału: obsługuje audio tagi
  (szept, emocje, pauzy), świetna ekspresja, pełne wsparcie polskiego.
  Minus: mniej stabilny między take'ami (dlatego 3–5 take'ów na linię) i wymaga,
  żeby klon głosu był zweryfikowany/zoptymalizowany pod v3.
- **`eleven_multilingual_v2`** — fallback: najbardziej przewidywalny i wierny
  klonowi, dobry polski. Minus: NIE rozumie audio tagów (przeczyta je!) — wtedy
  dramaturgię robimy wyłącznie interpunkcją (wielokropki, myślniki) i ustawieniem style.
- Zasada: **polski tekst tylko na v3 albo multilingual_v2** — nigdy na modelach
  „english" (flash/turbo english nie wspierają PL i zepsują akcent klona).

### Wartości startowe (suwaki)
| Parametr | v3 | multilingual_v2 | Dlaczego |
|---|---|---|---|
| Stability | **Natural (~0.5)** | **0.45–0.55** | Teaser wymaga ekspresji; zbyt wysoka stability spłaszcza szept i groźbę. Na v3 tryb „Creative" tylko jeśli Natural wyjdzie zbyt sztywno. |
| Similarity | **0.75–0.85** | **0.75–0.85** | Wysoko, bo to klon właściciela — ma brzmieć jak on. Powyżej 0.9 ryzyko przenoszenia artefaktów z nagrań źródłowych. |
| Style (exaggeration) | n/d (robią to tagi) | **0.15–0.3** | Na v2 odrobina stylu dodaje „filmowości"; powyżej 0.4 głos zaczyna dryfować od klona. |
| Speed | **0.9–0.95** | **0.9–0.95** | Spy-teaser = wolna, ciężka narracja; resztę tempa robi `[slow]` / interpunkcja. Dialogi (VO_06, VO_07) mogą iść na 1.0. |
| Speaker boost | ON | ON | Podbija podobieństwo do klona przy minimalnym koszcie. |

Praktyka: najpierw wygeneruj VO_03 („Wykres mi nie ucieka...") na obu modelach
z tymi ustawieniami — to najkrótsza linia-wizytówka. Wybierz model, który lepiej
trzyma barwę właściciela, i trzymaj się go dla całego filmu (spójność > pojedynczy
ładny take).

---

## 3. Femme fatale — „Na co grasz?" (Scena 7, ~0:45)

Osobny głos z **Voice Library** (nie klonujemy nikogo — gotowy głos z biblioteki,
koniecznie z dopuszczeniem do użytku komercyjnego).

### Jak szukać w Voice Library
- Filtr języka: **Polish** (jeśli mało wyników — głosy multilingual/English działają
  z v3/multilingual_v2 po polsku, ale sprawdź akcent na tej jednej frazie).
- Frazy do wyszukiwarki/tagów: `female, sultry, seductive, low, husky, velvet,
  smooth, mature, mysterious, narration/conversational`.
- Profil: kobieta 30–45, niski/średni rejestr, aksamitna barwa, powolna fraza.
  Unikać głosów „commercial/upbeat" i „young/bright" — to ma być Monako, nie reklama.

### Tekst i ustawienia
```
[sultry][slow] Na co grasz?
```
- Model: ten sam co VO agenta (spójność pipeline'u).
- Stability: **0.4–0.5** (trochę niżej niż u agenta — chcemy zmysłowej nieregularności).
- Similarity: 0.75. Style (v2): 0.3–0.4. Speed: **0.85–0.9** — fraza ma się ciągnąć.
- Wygeneruj 5 take'ów na 2–3 kandydatkach z biblioteki i wybierz do obrazu;
  to jedyna kobieca kwestia, więc decyduje chemia z ujęciem, nie metryki.

---

## 4. Praktyka produkcyjna

1. **Każda linia osobno.** Nigdy nie generuj całego skryptu jednym requestem —
   osobne pliki = pełna kontrola w montażu i tańsze poprawki.
2. **3–5 take'ów na linię** (v3 bywa loteryjne). Odsłuchuj na słuchawkach,
   wybieraj take pod obraz, nie „najładniejszy" solo.
3. **Nazewnictwo plików:** `VO_<nr>_<slug>_t<take>.<ext>`
   - `VO_01_podwoda_t1.mp3`, `VO_03_wykres_t2.mp3`, `VO_06_niegram_t4.mp3`,
     `FF_01_nacograsz_t3.mp3` (femme fatale z prefiksem FF).
   - Wybrane take'y kopiujesz do folderu `SELECTS/` bez zmiany nazwy.
4. **Format eksportu:** do montażu najlepiej **WAV 44.1 kHz** (PCM; dostępny
   na planach Pro+), minimum **MP3 44.1 kHz / 192–320 kbps**. Nie używaj
   domyślnego 128 kbps — po duckingu i masteringu artefakty wyłażą.
5. **Jeden „seed sesji":** generuj wszystkie linie w jednej sesji, tymi samymi
   ustawieniami; jeśli zmieniasz suwak dla jednej linii — zanotuj w nazwie folderu.
6. **Kontrola jakości:** każdy take sprawdź pod kątem (a) połkniętych/przeczytanych
   tagów, (b) złej wymowy „ZTT" — jeśli model czyta krzywo, zapisz fonetycznie
   „zet-te-te" w tekście, (c) clippingu na początku pliku.
7. **Timing:** linie VO_01/VO_02 to jedno zdanie przecięte montażem — wygeneruj
   też wariant sklejony w jednym requeście jako zapas, gdyby intonacja się nie spinała.
