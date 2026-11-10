# BRIEF DLA AGENTÓW PRODUKCYJNYCH — ZTT: LICENCJA NA ZYSK

Pakiet kreatywny: /home/claude/superteam-poland-infographic/ztt-film/ (01–06). Czytaj tylko to, czego potrzebujesz.

## Środowisko (WAŻNE)
- Pracujesz w Chrome właściciela (Dorian), zalogowany do ElevenLabs, plan **Scale**, ~4,5 mln kredytów. UI jest PO POLSKU.
- Narzędzia: `mcp__claude-in-chrome__*`. Są odroczone — załaduj je JEDNYM wywołaniem ToolSearch:
  `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__find,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__tabs_close_mcp`
- **Kilku agentów pracuje równolegle w tym samym Chrome.** Zrób `tabs_context_mcp`, potem `tabs_create_mcp` i pracuj WYŁĄCZNIE w swojej nowej karcie (zawsze podawaj jej tabId). Nie dotykaj innych kart. Na koniec zamknij swoją kartę (`tabs_close_mcp`).
- `navigate` wywołuj osobno (nie w batchu), resztę akcji na załadowanej stronie batchuj (`browser_batch`).
- Preferuj `find` / `read_page` / `get_page_text` (DOM) zamiast zrzutów ekranu — screenshoty na kartach w tle potrafią się zawieszać (timeout). Zrzut tylko gdy naprawdę musisz zobaczyć układ (scale 0.5–0.6).
- Długie prompty wpisuj przez kliknięcie w pole + `computer` type, albo `form_input`. Po wpisaniu sprawdź, że tekst się zgadza.
- Generacje trwają (wideo 1–5 min). Czekaj `wait` max 10 s na raz, sprawdzaj stan przez get_page_text/find. Możesz kolejkować kilka generacji naraz (limit planu: 15 równoległych żądań na całe konto — Ty używaj max 4).

## Twarde zasady
- NIE wylogowuj, NIE zmieniaj planu/ustawień konta, NIE kupuj niczego, NIE usuwaj cudzych zasobów.
- Przed każdą generacją sprawdź koszt pokazany przy przycisku generowania. Jeśli pojedyncza generacja > 120 000 kredytów — zatrzymaj się i zgłoś w raporcie zamiast generować.
- Prawo: żadnych słów „James Bond", „007", „Bond theme", logotypów marek. Własny motyw.
- Treści na ekranach w wideo: tylko krótkie „ZTT" — reszta napisów w montażu.
- Jeśli coś w UI blokuje (captcha, okno płatności, dziwny dialog) — nie obchodź, opisz w raporcie.

## Raport
Na koniec ZAPISZ (narzędziem Write) swój manifest do pliku wskazanego w zadaniu: lista wygenerowanych zasobów z:
nazwa robocza (np. `VO_03`), gdzie leży w ElevenLabs (strona/historia/tytuł/fragment prompta po którym go znaleźć),
wybrany take (★), ustawienia, koszt, uwagi jakościowe. Zwróć zwięzłe podsumowanie (max 25 linii), po polsku.
