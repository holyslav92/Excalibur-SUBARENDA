# Schema inputs — B17

topic_id: B17
article_dir: memory/blog/articles/B17-kommunalka-vklyuchena-schet-1840-na-vyezde
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kommunalka-vklyuchena-schet-1840-na-vyezde/`
   - `@id`: `{{SITE_BASE}}/blog/kommunalka-vklyuchena-schet-1840-na-vyezde/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «коммуналка включена», три ночи в Тюмени, на выезде фото счётчиков и доплата 1 840 ₽ без стартовых показаний при заезде; один вопрос до перевода; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-12`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "«Коммуналка включена». На выезде — счётчики и 1 840 ₽",
  "h1": "«Коммуналка включена». На выезде — счётчики и 1 840 ₽",
  "slug": "kommunalka-vklyuchena-schet-1840-na-vyezde",
  "topic_id": "B17",
  "author_id": "dobry-dom",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Коммуналка включена». На выезде — счётчики и 1 840 ₽

## authors-registry (dobry-dom)

```json
{
  "id": "dobry-dom",
  "name": "Добрый дом",
  "jobTitle": "Апартаменты и квартиры посуточно в Тюмени",
  "url": "{{SITE_BASE}}/",
  "sameAs": ["{{SITE_BASE}}/", "{{SITE_BASE}}/blog/"]
}
```

## Article summary (for description only)

Гость снял однушку в Тюмени на три ночи по 3 200 ₽ с обещанием «коммуналка включена». На выезде прислали фото счётчиков и попросили доплатить 1 840 ₽ «по факту» — без стартовых показаний при заселении. Разбор: 429 кВт·ч за три ночи нереалистичны для обычного проживания; нормальный расход — 150–320 ₽. Один вопрос до перевода: коммуналка в цене или по счётчикам — и письменное подтверждение условий.

## FAQ in article.html

None — no h2 «Частые вопросы».
