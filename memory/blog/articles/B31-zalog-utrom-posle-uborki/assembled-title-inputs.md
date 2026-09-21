# Assembled title inputs — B31

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night: promised deposit return window → shifted to «после уборки»
- MUST include figure: **5 000 ₽** (scenario anchor from scout)
- BAN **HH:MM in H1** (scout scene has 11:00 — use words «утром», «до обеда», not clock)
- BAN: «что проверить», «как снять», «разберём», «N советов», topic labels
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: Tyumen short-term guest; deposit return timing moved after keys
- ~40–85 chars in h1
- klyshin_title_shape: **2** — sum + deadline shift (dzen pattern 2)
- dzen_pattern: **2**
- wordstat_p0: «залог посуточно»

## Scout handoff

- topic_id: B31
- slug: zalog-utrom-posle-uborki
- title_draft calibration: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- klyshin_hook: deposit_return_sliding_window | rhythm: «Сначала проверка. Потом перевод. Не наоборот.» — do not paste Klyshin name
- angle: NOT B02 chip damage; NOT B23 cleaning fee 1800; NOT B30 card charge after extension

## Anti-dup H1 (published)

NOT B02 «Залог не вернули — нашли скол на плите»
NOT B23 «уборка включена» / 1 800 ₽ простыни
NOT B30 «После сдачи ключей с карты списали 1 800 ₽»

## JSON schema

```json
{
  "topic_id": "B31",
  "h1": "...",
  "title": "...",
  "slug": "zalog-utrom-posle-uborki",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "залог посуточно",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title",
  "verdict": "PASS"
}
```
