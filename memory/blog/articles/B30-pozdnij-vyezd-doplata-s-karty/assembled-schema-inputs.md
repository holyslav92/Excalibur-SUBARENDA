# Schema inputs — B30

topic_id: B30
article_dir: memory/blog/articles/B30-pozdnij-vyezd-doplata-s-karty
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/pozdnij-vyezd-doplata-s-karty/`
   - `@id`: `{{SITE_BASE}}/blog/pozdnij-vyezd-doplata-s-karty/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — продление до 14:00 согласовали, ключи сдали, с карты списали 1 800 ₽; как фиксировать цену продления и отличить холд от списания; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-20`
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
  "title": "Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽",
  "h1": "Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽",
  "slug": "pozdnij-vyezd-doplata-s-karty",
  "topic_id": "B30",
  "author_id": "dobry-dom",
  "date": "2026-09-20",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽

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

Гость согласовал выезд до 14:00, сдал ключи позже и увидел списание 1 800 ₽. Разбор: что зафиксировать в чате до продления (время, цена, тариф опоздания), чем холд отличается от списания и какие доказательства сохранить при споре.

## FAQ in article.html

None — no h2 «Частые вопросы».
