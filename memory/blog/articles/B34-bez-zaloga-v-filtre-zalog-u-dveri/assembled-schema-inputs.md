# Schema inputs — B34

topic_id: B34
article_dir: memory/blog/articles/B34-bez-zaloga-v-filtre-zalog-u-dveri
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/bez-zaloga-v-filtre-zalog-u-dveri/`
   - `@id`: `{{SITE_BASE}}/blog/bez-zaloga-v-filtre-zalog-u-dveri/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — фильтр «без залога», требование 5 000 ₽ на личную карту у двери; как отличить раскрытый залог от «страховой»; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-23`
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
  "title": "В фильтре — «без залога». У двери попросили 5 000 ₽ на личную карту",
  "h1": "В фильтре — «без залога». У двери попросили 5 000 ₽ на личную карту",
  "slug": "bez-zaloga-v-filtre-zalog-u-dveri",
  "topic_id": "B34",
  "author_id": "dobry-dom",
  "date": "2026-09-23",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

В фильтре — «без залога». У двери попросили 5 000 ₽ на личную карту

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

Гость выбрал квартиру в Тюмени с фильтром «без залога», оплатил бронь, а у двери попросили перевести 5 000 ₽ «страховой» на личную карту до выдачи ключей. Разбор: чем раскрытый залог в карточке отличается от остатка за проживание и от нового платежа у порога; почему перевод мимо площадки хуже защищён; один вопрос и шаги без спешки.

## FAQ in article.html

None — no h2 «Частые вопросы».
