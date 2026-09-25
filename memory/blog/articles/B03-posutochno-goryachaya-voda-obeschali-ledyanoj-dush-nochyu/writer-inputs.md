# Writer inputs — B03 (full CASE, PR #52 voice)

## Output contract
- File: HTML fragment only → `drafts/writer.html`
- NO `<h1>`, NO markdown fences, NO `<figure>` (Sol adds images)
- Length: **1100–1800 words** (full CASE, not outline)
- Audience: **guest** booking a night in Tyumen — NOT host-operator plots

## H1 (fixed in title-brief — do not output h1)
Обещали горячую воду. В 23:40 душ выдал ледяную струю

## dzen_pattern
**2** — живой кейс: обещание в карточке vs ледяная струя первой ночи; контраст «есть» vs «готова сейчас»; бойлер/магистраль в теле.

## Voice (HARD) — PR #52
1. **Holyslav dense §1:** 1–2 full paragraphs (NOT chopped TG ladder). Must include:
   - date/time anchor (25 сентября 2026, 23:40 — from H1/research)
   - direct quote from chat or host («горячая вода есть» style)
   - figure: **₽** and/or **ночи** and/or **минут** (40–80 min heat wait from research — OK)
   - **illusion break** beat: e.g. «Обещание было…», «Так не заселяем», «Не наоборот»
2. **Host identity line** (early): «Я хост посуточной в Тюмени. Это «Добрый дом».» Mention Telegram · MAX once in identity or nearby.
3. **Klyshin mechanics** after §1: short blows, «вот где подставят», «Не X. Не Y. А Z.», refusal line, «Наш вывод простой.»
4. **Mid fight-question** (one block): rhetorical question that pushes reader to **TG or MAX** — not WP comments.
5. **Funnel ONCE at end** (single closing block): booking + phone + channel links — do NOT repeat full funnel mid-article except the one mid fight-question line.

## BANNED
ЕГРН, нотариус, суд, «я адвокат», «мы лучшие», бизнес-класс, WhatsApp, имя Клышин, realtor plots, «В этой статье разберём», TL;DR opener, numbered list as §1 opener.
Phone in text: only **+7 (993) 574-83-22**

## Facts — ONLY from research-notes.md
- Tyumen weather 25.09.2026: day to +14°C, midnight ~+9°C, wind to 6 m/s
- Three situations: city main off / house networks / apartment boiler off-empty-depleted
- Accumulator boiler: often 40–80 min after switch-on (scenario, not universal norm)
- Card may say «горячая вода есть» vs «при отключении ГВС работает бойлер»
- Flow vs storage heater difference
- USTEK check by address — does not prove apartment OK
- Rabfakovskaya 2 example: house boiler failure (weeks without hot water) — illustrates house vs city
- Questions guest can ask before payment (list in research)
- Do NOT invent guest name, exact apartment price, refund amount, or continuation of a specific guest story

## Comfort+ framing
Use realistic **minutes and one night** tension; if you use ₽, keep modest посуточно Tyumen comfort+ (e.g. one night prepaid feeling) — no invented luxury.

## Interlinks (HARD) — 3–4 `<a href="/blog/...">` total, HTTP 200 verified
Use **only** these live siblings (2 unique slugs — use 3–4 contextual anchors across body, may repeat slug in different sections):
- `/blog/beskontaktnoe-zaselenie-posutochno-tyumen/` — late check-in, codes, first minutes at door
- `/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/` — deposit / proof at check-in, what to document

## Structure (suggested H2)
1. Opening CASE §1 + identity (dense)
2. Где ломается обещание «вода есть»
3. Три причины ледяного крана (магистраль / дом / квартира)
4. Бойлер: почему «есть» ≠ «можно мыться сейчас»
5. Что спросить в переписке до оплаты (checklist AFTER moral — ul ok here)
6. Первая ночь в Тюмени осенью (local + seasonal)
7. **Mid fight-question** → TG/MAX (one paragraph)
8. Как у нас в «Добрый дом» (honest boiler wording before arrival)
9. Коротко + **single end funnel**: https://добрыйдом-72.рф/booking/ , https://t.me/Dobriy_dom_72 , https://max.ru/id660300569233_biz , tel +7 (993) 574-83-22

## Also write
`dzen-excerpt.json` in article dir: hook, first_screen, takeaway (for Dzen card later).

## Master prompt
Follow `shared/writer-master-prompt.md` + `shared/article-style.md` CASE rules.
