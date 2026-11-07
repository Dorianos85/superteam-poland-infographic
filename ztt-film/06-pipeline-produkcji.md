# ZTT: LICENCJA NA ZYSK — Pipeline produkcji krok po kroku

Cel: od tego pakietu do gotowego teasera 75 s w ~2–4 dni robocze, solo lub z montażystą.

---

## KROK 1 — Wygeneruj ujęcia wideo (dzień 1–2)

Narzędzia: **Veo 3.1** (Gemini/Flow — najlepsze audio+ruch), zapas: **Kling 2.x**, **Runway Gen-4**.

1. Otwórz `03-prompty-wideo.md`. Każdy prompt wklejasz 1:1 (CHARACTER BLOCK + STYLE
   BLOCK są już wbudowane w prompty — to one trzymają spójność bohatera).
2. Generuj w kolejności z sekcji „Kolejność generowania" — najpierw ujęcia
   najtrudniejsze (woda, tłum telefonów), żeby wiedzieć, ile masz budżetu prób.
3. Na każde ujęcie zrób 2–4 warianty; wybieraj te, gdzie bohater wygląda tak samo.
4. Zapisuj pliki jako `S02_U1_v3.mp4` (scena_ujęcie_wariant) — ułatwi montaż.
5. **Nie próbuj** generować napisów ani UI z długim tekstem — tekst i ekrany
   terminala nakładamy w montażu (patrz KROK 4).

## KROK 2 — Nagraj voiceover (dzień 2, ~1–2 h)

Narzędzie: **ElevenLabs** + Twój sklonowany głos.

1. Otwórz `04-voiceover-elevenlabs.md` — skrypt ma już wplecione audio tagi
   i ustawienia (model, stability, style).
2. Każdą linię generuj OSOBNO, 3–5 take'ów; wybieraj najspokojniejszy —
   teaser szeptem sprzedaje lepiej niż krzykiem.
3. Kwestię femme fatale („Na co grasz?") zrób osobnym głosem z Voice Library
   (wytyczne doboru w pliku 04).

## KROK 3 — Muzyka i SFX (dzień 2–3, ~2 h)

Narzędzie: **ElevenLabs Music** + **ElevenLabs SFX**.

1. Utwór główny 75 s: prompt w `05-muzyka-sfx.md` (struktura zsynchronizowana
   z timecode'ami scenariusza). Wygeneruj 3–4 warianty, wybierz ten z najmocniejszym
   uderzeniem na 1:06 (finał).
2. **Dźwięk ALERTU ZTT** — najważniejszy asset brandingowy: wygeneruj z promptów
   w pliku 05, wybierz JEDEN i używaj go wszędzie (film, apka, kolejne spoty).
3. Wygeneruj SFX scena po scenie z listy w pliku 05.

## KROK 4 — Montaż (dzień 3–4)

Narzędzie: **DaVinci Resolve** (darmowy) lub CapCut.

1. Ułóż ujęcia wg timecode'ów z `02-scenariusz.md`. Zasada rytmu:
   **luksus = długie ujęcia, alert = cięcie w klatkę dźwięku alertu**.
2. Nałóż grafiki ekranów/alertów (mockup UI ZTT: zielona świeca + `ZTT ▲
   KONTYNUACJA TRENDU`) jako overlay z lekkim glow — na zegarek, telefon, szybę.
3. Napisy końcowe: `ZŁAP TREND TERMINAL` → `LICENCJA NA ZYSK` → `WKRÓTCE` + QR.
   Font: wąski, elegancki sans (np. Archivo/Michroma), złoto na czerni.
4. Audio: VO na wierzchu, muzyka duckowana −6…−9 dB pod VO, alert zawsze czytelny.
   Master: −14 LUFS (YouTube). Szczegóły w pliku 05.
5. Kolor: lekki teal&gold grade, winieta, ziarno 35 mm — skleja ujęcia z różnych
   generatorów w jeden film.

## KROK 5 — Wersje i publikacja

| Wersja | Format | Długość | Zawartość |
|---|---|---|---|
| Master | 16:9 4K | 75 s | pełny teaser |
| Reels/TikTok/Shorts | 9:16 | 30 s | sceny wg sekcji „Cut-downy" w pliku 03 |
| Feed | 1:1 | 15 s | kasyno + finał |
| Bumper | 16:9 | 6 s | lufa ze świec + alert + logo |

Hook pierwszych 2 sekund wersji pionowej: alert + „Ja nie gram. Ja widzę."

## Checklist przed publikacją

- [ ] Zero odniesień do „James Bond"/„007"/melodii z Bonda (szczegóły: 01-koncepcja, pkt 6)
- [ ] Ten sam dźwięk alertu w całym filmie
- [ ] Bohater spójny wizualnie między ujęciami
- [ ] QR / link działa
- [ ] Wersja z napisami PL (80% widzów mobile ogląda bez dźwięku)
