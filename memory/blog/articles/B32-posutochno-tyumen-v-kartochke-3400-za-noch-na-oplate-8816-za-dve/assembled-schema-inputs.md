# Schema inputs — B32

topic_id: B32
article_dir: memory/blog/articles/B32-posutochno-tyumen-v-kartochke-3400-za-noch-na-oplate-8816-za-dve
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/v-kartochke-3400-za-noch-na-oplate-8816-za-dve/`
   - `@id`: `{{SITE_BASE}}/blog/v-kartochke-3400-za-noch-na-oplate-8816-za-dve/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — ставка 3 400 ₽ за ночь vs итог 8 816 ₽ на оплате; сервис, уборка, сравнение с отелем по полной сумме; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-22`
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
  "title": "В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две ночи",
  "h1": "В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две ночи",
  "slug": "v-kartochke-3400-za-noch-na-oplate-8816-za-dve",
  "topic_id": "B32",
  "author_id": "dobry-dom",
  "date": "2026-09-22",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две ночи

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

Гость видит 3 400 ₽ за ночь в карточке, считает 6 800 ₽ за две ночи, а на кнопке оплаты — 8 816 ₽ из‑за сервисного сбора и разовой уборки. Разбор: сравнивать квартиру с отелем по полному итогу за даты и гостей, а не по витринной ставке.

## FAQ in article.html

None — no h2 «Частые вопросы».
