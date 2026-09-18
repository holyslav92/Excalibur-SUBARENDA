# Schema inputs — B26

topic_id: B26
article_dir: memory/blog/articles/B26-sobaka-doplata-posutochno
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/blogposting.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/sobaka-doplata-posutochno/`
   - `@id`: `{{SITE_BASE}}/blog/sobaka-doplata-posutochno/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — значок «можно с собакой» в карточке, доплата 2 500 ₽ за «крупную породу» при заезде в Тюмени; что уточнить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-18`
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
  "title": "«Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»",
  "h1": "«Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»",
  "slug": "sobaka-doplata-posutochno",
  "topic_id": "B26",
  "author_id": "dobry-dom",
  "date": "2026-09-18",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»

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

Гость забронировал жильё с лабрадором по отметке «можно с животными», оплатил 8 200 ₽ за две ночи — и у подъезда услышал доплату 2 500 ₽ за «крупную породу» плюс намёк на залог за шерсть. Разбор: значок разрешает приехать, но не называет итог; шесть вопросов в переписке до перевода; почему доплату называют у двери.

## FAQ in article.html

None — no h2 «Частые вопросы».
