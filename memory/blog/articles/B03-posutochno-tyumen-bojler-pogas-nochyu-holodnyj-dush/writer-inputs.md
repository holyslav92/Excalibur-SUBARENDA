# Writer inputs B03 — case delivery PR#52

Read fully: research-notes.md, title-brief.json, shared/writer-master-prompt.md, shared/article-style.md, published-titles-only.md, memory/scout/scout-inputs-2026-09-27.md.

Output **ONLY** clean HTML fragment → `drafts/writer.html`. NO `<h1>`. NO markdown fences. NO ``` wrappers.

## Form (HARD PR#52)

- **1100–1800 Russian words** — full narrative case article, NOT bullet thesis / NOT telegraphic list-only piece. Use `<p>`, `<h2>`, `<h3>`, `<ul>` where natural; prose drives the story.
- **Pattern:** live case with sums (dzen_pattern 2) + fear→instruction in §1 (pattern 3) + contrast in opening (pattern 4). Tyumen supply, late September evening after road trip.
- **§1 opening:** 1–2 dense `<p>` paragraphs: concrete **date** (e.g. 26 сентября 2026 or «в субботу вечером»), **time** (23:10 from H1), **money in ₽** (realistic comfort+ Tyumen nightly rate + optional zalog from research context — e.g. 4 200 ₽/сутки, предоплата 8 400 ₽, залог 5 000 ₽ — illustrative case math, not a promise from «Добрый дом»). Short quoted chat line from bad host («мастер завтра»). Verdict/contrast early: promised shower vs ice water.
- **Immediately after §1**, standalone paragraph with **exact line** (keep punctuation and guillemets):
  `Я хост посуточной в Тюмени. Это «Добрый дом».`
- **Klyshin mechanics in body:** short paragraphs, direct **dialog** in «» — include at least once host refusal line **`Нет. Так не заселяем.`** (or very close). Show chat back-and-forth, «где подставят», checklist from title-brief `checks` (4 items). **NOT** legal hooks: no ЕГРН, нотариус, суд, «я адвокат», Pravoved as hero.
- **Mid-article:** ONE guest question as `<h3>` or bold Q — answer points to **https://t.me/Dobriy_dom_72** OR **https://max.ru/id660300569233_biz** — never «комментарии», never «напишите под постом».
- **After checklist block:** TG funnel line → `https://t.me/Dobriy_dom_72` («полный список» / channel).
- **Brand block «у нас так»:** how «Добрый дом» checks boiler before check-in, instruction before arrival — then MAX or manager link.
- **Ending (HARD):** paragraph starting **`Наш вывод простой.`** then **ONE** consolidated funnel `<p>` (single block) containing ALL: Telegram channel `https://t.me/Dobriy_dom_72`, MAX `https://max.ru/id660300569233_biz`, booking `https://добрыйдом-72.рф/booking/`, phone `<a href="tel:+79935748322">+7 (993) 574-83-22</a>`, manager `https://t.me/Dobriy_dom_Tyumen`. No second CTA dump after that.

## Interlinks (HARD)

Embed **3–4 unique** contextual `<a href="/blog/SLUG/">` links — different slugs, all live on site. Verified slugs (use these paths):

1. `/blog/goryachaya-voda-i-bojler-pri-zaselenii-posutochno/`
2. `/blog/goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno/`
3. `/blog/napisali-goryachaya-voda-est-ledyanoj-dush-migayushij-boiler/`
4. `/blog/instrukciya-zaseleniya-posutochno-ne-tot-podezd/` (late arrival / instruction angle)

Natural Russian anchors, not «читайте также» spam.

## Bans (HARD)

- Phones: **+7 922 001 65 05**, any WhatsApp, **t.me/klyshin**, Klyshin personal phone
- No invented «Добрый дом» SLA, no claim boiler broke in our real flat
- Separate city GVS shutdown (1540 objects news) from in-unit boiler failure — facts from research only
- No `<h1>`

## H1 promise (from title-brief)

H1: «В карточке был душ. В 23:10 бойлер погас — вода стала ледяной» — deliver the night boiler / cold shower story + title-brief checks in body.

## Facts

Only from research-notes.md + title-brief.json. Scenario 23:10 is illustrative model, not news claim about real guest.
