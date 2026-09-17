# Schema inputs — B26

topic_id: B26
article_dir: memory/blog/articles/B26-kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi/`
   - `@id`: `{{SITE_BASE}}/blog/kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — квартира посуточно в Тюмени кажется дешевле отеля за ночь, но итог за две ночи 13 400 ₽ после уборки, белья и сборов; как сравнивать полный счёт, not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-17`
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
  "title": "Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽",
  "h1": "Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽",
  "slug": "kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi",
  "topic_id": "B26",
  "author_id": "dobry-dom",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽

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

Гость видит квартиру за 4 200 ₽ за ночь и отель за 4 800 ₽ — в уме квартира выигрывает. Но финальный экран показывает 13 400 ₽ за две ночи: база 8 400 ₽ плюс уборка, бельё, сервисный сбор. Разбор: почему цена за ночь не равна итогу поездки; как отделить залог от расходов; как сравнивать квартиру и отель на одинаковые даты в Тюмени.

## FAQ in article.html

None — no h2 «Частые вопросы».
