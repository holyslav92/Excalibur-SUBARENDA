# Writer inputs B43 — full CASE (PR#52 voice, gate-safe)

Read: research-notes.md, title-brief.json, shared/writer-master-prompt.md, shared/article-style.md, shared/dobry-dom-voice-reset-v1.md, published-titles-only.md (anti-dup only).

**Output:** ONLY clean HTML fragment → `drafts/writer.html`. NO `<h1>`. NO markdown fences. NO wrapper `<html>`.

Also write `dzen-excerpt.json` in article dir: `{ "hook", "first_screen", "takeaway" }` (Russian, no duplicate H1 verbatim).

## H1 (title-brief — do not repeat as h1)
«Детская кроватка» в фильтре посуточно — в чате: завтра за 2 500 ₽

## Length
**1100–1800 words** of visible Russian text — full narrative CASE for Sol, dense prose now (not outline).

## PR#52 voice (current manner canon — MUST PASS gate)
1. **Holyslav smooth lead:** 1–2 dense `<p>` in §1. Quote-first + **2 500 ₽** (and/or nights) in first block. Contrast: filter «детская кроватка» vs empty corner / «завтра». Short spoken words in first 2 sentences (no 14+ letter monsters).
2. **No duty-log in §1:** NO weekday, NO calendar date, NO `HH:MM` clock in opening §1 (time «вечером после дороги» OK; **21:40** only later in body, max 1–2 clock mentions total — avoid timeline spine).
3. **Identity (early, once):** «Я хост посуточной в Тюмени. Это «Добрый дом».» + mention Telegram · MAX briefly.
4. **Illusion break** after a quote — own words. **BAN** exact stamps: «Нет. Так не заселяем.», «Наш вывод простой.», «Так не заселяем.» Use refusal tone without those strings (e.g. «Кроватку не обещаем “завтра за доплату” — сон ребёнка не переносим.»).

## dzen_pattern
Live **case with sums** (pattern 2) + **filter vs fact** (pattern 4). §1: fear — первая ночь с годовалым без безопасного места для сна → что спросить до оплаты.

## Facts (ONLY research-notes.md)
- Composite editorial case: **2 500 ₽**, «завтра», вечернее сообщение в чате — **не** тариф «Добрый дом», не средняя по Тюмени.
- Суточно.ру: «дети» и «детская кроватка» — **разные** настройки; фильтр = поиск удобств, не единый тариф/срок доставки.
- Хозяин раскрывает доплаты (уборка, гости, депозит); платная кроватка встречается (пример **2 000 ₽** в Краснодаре — **не** Тюмень).
- Уточнять до оплаты: стоит ли уже в квартире, входит в цену, матрас/детское бельё, срок установки, кто отвечает если не готово.
- Wordstat weave once naturally: «квартиры посуточно тюмень» / «квартира посуточно с детской кроваткой» — no stuffing.
- **BAN** weak seed «посуточная аренда тюмень».
- Do NOT present composite as verified guest review of «Добрый дом».

## Interlink — **4** contextual `<a href="/blog/.../">` (unique slugs from ledger)
1. `/blog/bez-zaloga-v-filtre-zalog-u-dveri/` — галочка в фильтре vs факт у заселения
2. `/blog/mozhno-s-detmi-doplata-za-rebenka/` — «можно с детьми» ≠ готовое спальное место
3. `/blog/dve-krovati-na-foto-posutochno-nochyu-divan-i-skladnoj-matras/` — обещанное спальное место vs реальность
4. `/blog/posutochno-tyumen-v-filtre-ot-odnoj-nochi-u-domofona-minimum-dvoe-sutok/` — другой фильтр, та же ловушка ожиданий

## Mid-article fight-question (HARD)
One block: bold question from tired parent guest → **answer only** in messenger: **https://t.me/Dobriy_dom_72** OR **https://max.ru/id660300569233_biz** (one channel for that block). Never WP comments.

## Structure
- 6–8 `<h2>` with **different** headings (not «Мой вывод как практика»). One H2 = conclusion («Короче», «Если одной фразой», etc.).
- Body: «Не X. Не Y. А Z.», «Сначала проверка. Потом перевод.»
- Optional checklist `<ul>` **after** conclusion — new checks only.
- **One** consolidated CTA `<p>` at end: booking https://добрыйдом-72.рф/booking/ , tel `<a href="tel:+79935748322">+7 (993) 574-83-22</a>` (only phone), TG + MAX once.

## Bans
ЕГРН, нотариус, суд, «я адвокат», WhatsApp, Klyshin name, **+7 922 001 65 05**, host-operator (загрузка %), invented «Добрый дом» crib price.

## Audience
Tired **guest** with small child booking посуточно in Tyumen — NOT host business tips.
