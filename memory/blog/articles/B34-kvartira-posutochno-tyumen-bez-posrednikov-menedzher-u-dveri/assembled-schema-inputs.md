# Schema inputs — B34

topic_id: B34
article_dir: memory/blog/articles/B34-kvartira-posutochno-tyumen-bez-posrednikov-menedzher-u-dveri
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kvartira-posutochno-tyumen-bez-posrednikov-menedzher-u-dveri/`
   - `@id`: `{{SITE_BASE}}/blog/kvartira-posutochno-tyumen-bez-posrednikov-menedzher-u-dveri/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — фильтр «от хозяев», менеджер у двери и доплата за «оформление» переводом на карту после оплаченной брони; что спросить до поездки; not duplicate headline verbatim.
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
  "title": "«От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту",
  "h1": "«От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту",
  "slug": "kvartira-posutochno-tyumen-bez-posrednikov-menedzher-u-dveri",
  "topic_id": "B34",
  "author_id": "dobry-dom",
  "date": "2026-09-23",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту

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

Гость искал квартиры посуточно без посредников с фильтром «от хозяев», оплатил две ночи через площадку, а у двери встретил менеджер с планшетом и потребовал 2 000 ₽ «за оформление» переводом на карту — суммы не было в брони. Разбор: чем отличается честный остаток и залог от давления у порога, какой вопрос задать в чате до оплаты и почему не переводить на личную карту.

## FAQ in article.html

None — no h2 «Частые вопросы».
