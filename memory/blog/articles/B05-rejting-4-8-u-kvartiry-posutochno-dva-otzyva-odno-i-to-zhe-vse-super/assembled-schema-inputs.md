# Schema inputs — B05

topic_id: B05
article_dir: memory/blog/articles/B05-rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/`
   - `@id`: `{{SITE_BASE}}/blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — рейтинг 4,8 и два одинаковых отзыва «всё супер» перед бронью посуточной квартиры в Тюмени; проверить текст отзывов до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-01`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом",
  "h1": "Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом",
  "slug": "rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super",
  "topic_id": "B05",
  "author_id": "dobry-dom",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом

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

Гость в Тюмени видит квартиру за 3 900 ₽ с рейтингом 4,8, но два свежих отзыва слово в слово «всё супер» — без деталей о заселении, чистоте и фотографиях. Рейтинг не заменяет чтение отзывов: важно проверить даты, отметку о проживании и конкретику до предоплаты.

## FAQ in article.html

None — no h2 «Частые вопросы».
