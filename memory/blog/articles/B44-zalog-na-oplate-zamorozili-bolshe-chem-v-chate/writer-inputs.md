# Writer inputs B44 — full CASE (dobry_dom_voice_reset_v1)

Read: research-notes.md, title-brief.json, shared/writer-master-prompt.md, shared/article-style.md, shared/dobry-dom-voice-reset-v1.md, published-titles-only.md (anti-dup only).

**Output:** ONLY clean HTML fragment → `drafts/writer.html`. NO `<h1>`. NO markdown fences. NO wrapper `<html>`.

Also write `dzen-excerpt.json` in article dir: `{ "hook", "first_screen", "takeaway" }` (Russian, no duplicate H1 verbatim).

## H1 (title-brief — do not repeat as h1)
В чате посуточно: залог 3 000 ₽ — на оплате заморозка 11 400, кода нет

## Length
**1100–1250 words** of visible Russian text — full narrative CASE for Sol, dense prose (not outline). Stay ≤1300 words hard ceiling for downstream Sol gate.

## PR#52 / dobry_dom_voice_reset_v1 (MUST PASS writer gate)
1. **Holyslav smooth §1:** 1–2 dense `<p>` before or after first H2 — quote-first + **3 000 ₽** and **11 400 ₽** in opening block. Short spoken words in first 2 sentences.
2. **No duty-log in §1:** NO weekday, NO calendar date, NO `HH:MM` in opening §1.
3. **Identity (early, once):** «Я хост посуточной в Тюмени. Это «Добрый дом».» + Telegram · MAX briefly — host line **after** lead paragraph(s).
4. **Illusion break** after a quote — own words. **BAN** exact stamps: «Нет. Так не заселяем.», «Наш вывод простой.», «Так не заселяем.»
5. **Klyshin mechanics** (not name): weave «Сначала проверка. Потом перевод. Не наоборот.» as order-moral in body.

## dzen_pattern
**2** — live case with sums. Scene: chat promises small zalog, payment screen shows large hold, **код заселения ещё не прислали**.

## Facts (ONLY research-notes.md)
- Composite editorial CASE (Scout hook deposit_before_keys), **not** verified booking at «Добрый дом» or named platform.
- Chat: залог **3 000 ₽**; payment screen: hold/block **11 400 ₽**; access code not sent yet.
- **11 400** is headline anchor — not proven formula; one authorization may bundle nights, cleaning, service line, insurance deposit (channel-dependent).
- **Hold ≠ capture** — temporary reserve; not necessarily money to host yet. Yandex Pay / industry explainers only — no specific bank tariff or guaranteed unblock days.
- Sutochno.ru rules (platform model): full sum at booking; guest commission model; deposit/cleaning in listing — **do not** claim incident on Sutochno/Avito by name as fact.
- Do NOT say 11 400 is «only zalog» or already captured/charged.
- Wordstat weave once naturally: «квартира посуточно залог» / «квартиры посуточно тюмень» — no stuffing. **BAN** weak seed «посуточная аренда тюмень».
- Separate from B34 (cash at door), B02 (return after damage), B32 (price stack), B40 (transfer before code), B30 (charge after checkout).

## Interlink — **4** contextual `<a href="/blog/.../">` (published siblings)
1. `/blog/v-kartochke-3400-za-noch-na-oplate-8816-za-dve/` — цена в карточке vs итог на экране оплаты
2. `/blog/posutochno-tyumen-v-filtre-bez-predoplaty-perevod-do-koda/` — деньги до кода
3. `/blog/pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate/` — 3 000 ₽ в переписке и тишина после
4. `/blog/posutochno-tyumen-stiralnaya-v-kartochke-i-zalog/` — залог в карточке vs у двери

## Mid-article fight-question (HARD)
One block: bold question from panicked guest seeing 11 400 hold with no code → **answer only** in messenger: **https://t.me/Dobriy_dom_72** OR **https://max.ru/id660300569233_biz** (pick one channel for that block). Never WP comments.

## Structure
- 6–8 `<h2>` with **different** headings (not «Мой вывод как практика»). One H2 = conclusion («Короче», «Если одной фразой», etc.).
- Body: «Не X. Не Y. А Z.», hold vs списание, разложить строки на экране оплаты.
- Optional checklist `<ul>` **after** conclusion — new checks only (screenshots, hold vs capture in app, ask host before confirm).
- **One** consolidated CTA `<p>` at end: booking https://добрыйдом-72.рф/booking/ , tel `<a href="tel:+79935748322">+7 (993) 574-83-22</a>` (only phone), TG + MAX once.

## Bans
ЕГРН, нотариус, суд, «я адвокат», WhatsApp, Klyshin name, **+7 922 001 65 05**, host-operator (загрузка %), invented verified guest at «Добрый дом», exact bank unblock guarantees.

## Audience
Tired **guest** booking посуточно in Tyumen — NOT host PMS tips.
