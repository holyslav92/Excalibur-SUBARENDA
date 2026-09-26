# schema inputs B03

Output ONLY valid JSON-LD for schema.jsonld (single JSON object, no markdown fences).

## Site base

Use placeholder `{{SITE_BASE}}` for all URLs. Canonical article URL: `{{SITE_BASE}}/zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit/` — NO `/blog/` in path.

## Article meta

- topic_id: B03
- slug: zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
- headline (h1): Заселился на ночь. Бойлер не нагрел воду — душ ждал 90 минут
- datePublished: 2026-09-26
- dateModified: 2026-09-26
- author_id: dobry-dom
- inLanguage: ru-RU
- article_mode: B (troubleshooting, NOT HowTo archetype)

## Author (from authors-registry)

- name: Добрый дом
- jobTitle: Апартаменты и квартиры посуточно в Тюмени
- @type for author in BlogPosting: Organization (match B01/B02 pattern)
- url: {{SITE_BASE}}/
- Do NOT include `/blog/` anywhere in schema.jsonld (gate rejects any `{{SITE_BASE}}/blog/` substring).

## FAQ

theme_blocks.faq = skip. NO FAQ section «Частые вопросы» in article.html. Do NOT include FAQPage or mainEntity FAQPage. BlogPosting only.

## Description for schema

Write a concise Russian meta description (1–2 sentences, ~150–200 chars) summarizing buyer value: cold shower after check-in, boiler wait time, what to ask before payment in Tyumen short-term rental. Not duplicate of headline verbatim.

## Reference structure (B01 BlogPosting without inventing FAQ)

@context, @type BlogPosting, @id, url, headline, description, inLanguage, datePublished, dateModified, author Organization, mainEntityOfPage WebPage, publisher Organization.

## article.html (full body for context)

<p>«Вода холодная. Совсем холодная. Бойлер у вас включён вообще?» — такое сообщение гость отправил через восемь минут после входа в квартиру. Он ехал полдня, поставил сумку и пошёл в душ. Из крана шла вода, от которой немеют руки.</p>

<p>В объявлении было написано: «горячая вода есть». В переписке это подтвердили: «есть, бойлер». Но душ пришлось отложить на 90 минут — пока пятидесятилитровый бак нагреет воду с нуля.</p>

<p>90 минут — не обязательно наглость хозяина и не обязательно поломка. Это физика накопительного водонагревателя. Проблема в том, что гостю заранее не объяснили, откуда берётся горячая вода и будет ли она готова сразу.</p>

<p>Я хост посуточной в Тюмени. Это «Добрый дом».</p>

(article continues: boiler types, 50L heat time 90-120 min, questions before payment, what to save in chat, malfunction vs wait, host practices — no FAQ H2 section)
