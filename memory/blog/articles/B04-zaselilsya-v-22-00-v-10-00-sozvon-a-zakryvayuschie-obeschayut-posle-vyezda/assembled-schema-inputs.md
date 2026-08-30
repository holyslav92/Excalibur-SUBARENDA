# Schema inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-zaselilsya-v-22-00-v-10-00-sozvon-a-zakryvayuschie-obeschayut-posle-vyezda
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zaselilsya-v-22-00-v-10-00-sozvon-a-zakryvayuschie-obeschayut-posle-vyezda/`
   - `@id`: `{{SITE_BASE}}/blog/zaselilsya-v-22-00-v-10-00-sozvon-a-zakryvayuschie-obeschayut-posle-vyezda/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — поздний заезд в 22:00, утренний видеосозвон и закрывающие документы для командировки в Тюмени; проверить стол, Wi‑Fi и пакет документов до оплаты; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-30`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда",
  "h1": "Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда",
  "slug": "zaselilsya-v-22-00-v-10-00-sozvon-a-zakryvayuschie-obeschayut-posle-vyezda",
  "topic_id": "B04",
  "author_id": "dobry-dom",
  "date": "2026-08-30",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда

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

Командированный заселяется в квартиру посуточно в Тюмени около 22:00, утром в 10:00 нужен видеосозвон, а закрывающие документы обещают только после выезда. До оплаты стоит письменно проверить рабочее место, скорость Wi‑Fi у стола и срок выдачи чека и акта — иначе авансовый отчёт за три рабочих дня может не успеть.

## FAQ in article.html

None — no h2 «Частые вопросы».
