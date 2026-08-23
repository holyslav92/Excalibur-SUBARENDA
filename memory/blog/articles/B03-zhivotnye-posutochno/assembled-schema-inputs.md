# Schema inputs — B03 «Добрый дом»

## Role

Сгенерируй **только** валидный JSON-LD (один объект BlogPosting), без markdown-обёртки и без пояснений.

## Правила (HARD)

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Site base: `{{SITE_BASE}}` — **никогда** литерал `[REDACTED]`, никогда `/blog/<slug>/`
4. Canonical URL: `{{SITE_BASE}}/v-obyavlenii-mozhno-s-kotom-v-pravilah-shtraf/`
5. `@id`: `{{SITE_BASE}}/v-obyavlenii-mozhno-s-kotom-v-pravilah-shtraf/#article`
6. `datePublished` и `dateModified`: `2026-08-23`
7. `inLanguage`: `ru-RU`
8. `headline`: из title-brief (H1)
9. `description`: 1–2 предложения — посуточная аренда с котом, 5 вопросов до оплаты, проверка правил и договора, штраф vs ущерб. Без выдуманных сумм «Доброго дома».
10. `author` и `publisher`: Organization «Добрый дом», `url`: `{{SITE_BASE}}/`
11. **FAQPage НЕ добавлять** — в article.html нет секции «Частые вопросы» (`theme_blocks.faq: skip`). Не включать `mainEntity` с FAQPage.
12. HowTo / Review — не нужны.

## article.meta.json

```json
{
  "topic_id": "B03",
  "slug": "v-obyavlenii-mozhno-s-kotom-v-pravilah-shtraf",
  "title": "Хозяин разрешил кота в объявлении. В договоре — штраф за шерсть",
  "h1": "Хозяин разрешил кота в объявлении. В договоре — штраф за шерсть",
  "author_id": "dobry-dom",
  "date": "2026-08-23"
}
```

## title-brief.json

```json
{
  "h1": "Хозяин разрешил кота в объявлении. В договоре — штраф за шерсть",
  "title": "Хозяин разрешил кота в объявлении. В договоре — штраф за шерсть",
  "slug": "v-obyavlenii-mozhno-s-kotom-v-pravilah-shtraf"
}
```

## research-context (datePublished)

- `today_iso`: `2026-08-23`

## author (authors-registry, id=dobry-dom)

- name: Добрый дом
- jobTitle: Апартаменты и квартиры посуточно в Тюмени
- url: `{{SITE_BASE}}/`

## dzen-excerpt (для description, не копировать дословно)

- hook: В объявлении «можно с животными», а в правилах — штраф за шерсть.
- takeaway: Пять вопросов до оплаты, письменное разрешение на животное, фото на заезде. Штраф и ущерб — разные вещи.

## FAQ check

`theme_blocks.faq: skip`. В HTML нет `<h2>Частые вопросы</h2>` и пар `<h3>+<p>`. **FAQPage omit.**

## Эталон структуры (B02 без FAQ — BlogPosting only)

См. соседние статьи: BlogPosting с `mainEntityOfPage`, без `mainEntity` если FAQ нет.
