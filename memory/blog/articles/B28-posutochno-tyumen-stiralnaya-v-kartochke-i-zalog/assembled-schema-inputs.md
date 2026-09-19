# Schema inputs — B28

topic_id: B28
article_dir: memory/blog/articles/B28-posutochno-tyumen-stiralnaya-v-kartochke-i-zalog
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-tyumen-stiralnaya-v-kartochke-i-zalog/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-tyumen-stiralnaya-v-kartochke-i-zalog/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — галочка «стиральная машина» в фильтре, сбой к третьей ночи, прачечная ~1 100 ₽ в Тюмени; что уточнить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-19`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).
14. **BAN** stuffing weak cluster «посуточная аренда тюмень» in description.

## article.meta.json

```json
{
  "title": "«Стиральная машина есть» в фильтре. К 3-й ночи — мокрое бельё, прачечная, 1 100 ₽",
  "h1": "«Стиральная машина есть» в фильтре. К 3-й ночи — мокрое бельё, прачечная, 1 100 ₽",
  "slug": "posutochno-tyumen-stiralnaya-v-kartochke-i-zalog",
  "topic_id": "B28",
  "author_id": "dobry-dom",
  "date": "2026-09-19",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Стиральная машина есть» в фильтре. К 3-й ночи — мокрое бельё, прачечная, 1 100 ₽

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

Гостья сняла квартиру в Тюмени на три ночи; в фильтре была стиральная машина, но к третьей ночи цикл остановился с водой в барабане — семья уехала в прачечную и потратила около 1 100 ₽. Разбор: галочка в карточке не гарантирует рабочий цикл; что спросить до перевода денег; как фиксировать поломку и чек.

## FAQ in article.html

None — no h2 «Частые вопросы».
