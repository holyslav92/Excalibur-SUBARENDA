Ты генерируешь один файл schema.jsonld для WordPress. Ответ — ТОЛЬКО валидный JSON (без markdown, без ```, без пояснений до или после).

Правила:
- @context https://schema.org
- @type BlogPosting (единственный корневой объект или @graph с BlogPosting)
- НЕ добавляй FAQPage: в article.html нет секции h2 «Частые вопросы» с парами h3+p
- Все URL: {{SITE_BASE}}/posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz/ — без /blog/
- @id: {{SITE_BASE}}/posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz/#article
- headline: В фильтре — «с собакой». У двери крупного пса не пустили без 3 000 ₽
- description: 1–2 предложения по смыслу статьи (фильтр pet-friendly vs условия для крупной собаки, что уточнить до оплаты в Тюмени) — не дублируй headline дословно
- inLanguage: ru-RU
- datePublished и dateModified: 2026-09-25
- author и publisher: Organization «Добрый дом», url {{SITE_BASE}}/
- mainEntityOfPage: WebPage @id {{SITE_BASE}}/posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz/
- Не используй литерал [REDACTED]

Контекст статьи (смысл description):
Гостья забронировала посуточное жильё в Тюмени по фильтру «можно с животными», приехала с псом 32 кг; у двери хозяин потребовал 3 000 ₽ доплаты. Текст объясняет, почему галочка в каталоге не равна согласованию по весу/породе, что спросить в чате до оплаты и как зафиксировать условия.
