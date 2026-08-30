# Schema inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-perevel-predoplatu-utrom-kvartira-uzhe-zanyata
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/perevel-predoplatu-utrom-kvartira-uzhe-zanyata/`
   - `@id`: `{{SITE_BASE}}/blog/perevel-predoplatu-utrom-kvartira-uzhe-zanyata/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — отличить мошенничество от конфликта брони при предоплате за посуточную квартиру в Тюмени; проверить получателя, канал оплаты и подтверждение брони; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-29`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Перевёл предоплату за квартиру посуточно. Утром её уже сдали",
  "h1": "Перевёл предоплату за квартиру посуточно. Утром её уже сдали",
  "slug": "perevel-predoplatu-utrom-kvartira-uzhe-zanyata",
  "topic_id": "B04",
  "author_id": "dobry-dom",
  "date": "2026-08-29",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Перевёл предоплату за квартиру посуточно. Утром её уже сдали

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

Гость переводит предоплату за квартиру посуточно в Тюмени, а утром узнаёт, что жильё уже занято. Разница между мошенничеством (оплата вне площадки) и конфликтом брони (двойное бронирование на сервисах). До оплаты — проверить ФИО получателя, канал платежа, тариф отмены и наличие брони в личном кабинете.

## FAQ in article.html

None — no h2 «Частые вопросы».
