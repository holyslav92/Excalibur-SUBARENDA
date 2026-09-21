# Schema inputs — B31

topic_id: B31
article_dir: memory/blog/articles/B31-posutochno-tyumen-oplatili-3-nochi-vnutri-chuzhie-chemodany
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-tyumen-oplatili-3-nochi-vnutri-chuzhie-chemodany/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-tyumen-oplatili-3-nochi-vnutri-chuzhie-chemodany/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — оплатили 3 ночи, при заезде в квартире чужие чемоданы и гости; что спросить до оплаты, как действовать у двери и зафиксировать замену или возврат; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-21`
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
  "title": "Оплатили 3 ночи. Открыли дверь — внутри чужие чемоданы",
  "h1": "Оплатили 3 ночи. Открыли дверь — внутри чужие чемоданы",
  "slug": "posutochno-tyumen-oplatili-3-nochi-vnutri-chuzhie-chemodany",
  "topic_id": "B31",
  "author_id": "dobry-dom",
  "date": "2026-09-21",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Оплатили 3 ночи. Открыли дверь — внутри чужие чемоданы

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

Гость оплатил три ночи, приехал по адресу и обнаружил в квартире других людей с вещами. Разбор: почему оплата не гарантирует заселение, что делать в первые минуты у двери, какие вопросы задать до перевода (адрес, даты, план Б при занятой квартире).

## FAQ in article.html

None — no h2 «Частые вопросы».
