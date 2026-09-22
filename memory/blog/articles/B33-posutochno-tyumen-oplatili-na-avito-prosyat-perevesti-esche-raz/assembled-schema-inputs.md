# Schema inputs — B33

topic_id: B33
article_dir: memory/blog/articles/B33-posutochno-tyumen-oplatili-na-avito-prosyat-perevesti-esche-raz
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-tyumen-oplatili-na-avito-prosyat-perevesti-esche-raz/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-tyumen-oplatili-na-avito-prosyat-perevesti-esche-raz/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — оплата брони на Avito, просьба повторно перевести на карту; как отличить нормальный остаток при заселении от двойной оплаты; not duplicate headline verbatim.
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
  "title": "Бронь на Авито уже оплачена. В чате: второй перевод на карту",
  "h1": "Бронь на Авито уже оплачена. В чате: второй перевод на карту",
  "slug": "posutochno-tyumen-oplatili-na-avito-prosyat-perevesti-esche-raz",
  "topic_id": "B33",
  "author_id": "dobry-dom",
  "date": "2026-09-22",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Бронь на Авито уже оплачена. В чате: второй перевод на карту

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

Гостья оплатила бронь на Avito (часть суммы через площадку, остаток при заселении), после статуса «оплачено» в чате попросили продублировать предоплату на карту или отменить заказ и перевести всю сумму напрямую. Разбор: почему это не залог и не «вторая предоплата», что проверить в заказе и почему не стоит выходить из защищённой брони.

## FAQ in article.html

None — no h2 «Частые вопросы».
