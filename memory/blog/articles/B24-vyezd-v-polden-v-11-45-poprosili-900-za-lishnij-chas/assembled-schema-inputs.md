# Schema inputs — B24

topic_id: B24
article_dir: memory/blog/articles/B24-vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas/`
   - `@id`: `{{SITE_BASE}}/blog/vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — уборщица пришла до полудня, гостю предложили 900 ₽ за «лишний час» при выезде в 12:00; приход клинера не сдвигает оплаченное время; что проверить в брони до перевода; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-15`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»",
  "h1": "Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»",
  "slug": "vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas",
  "topic_id": "B24",
  "author_id": "dobry-dom",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»

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

Гость с двумя ночами по 8 400 ₽ и выездом в полдень получил в 11:45 сообщение «900 ₽ за каждый лишний час — уборщица уже ждёт». Разбор: приход уборки не переносит границу оплаченного времени; поздний выезд считается только после согласованного часа; доплата честна, если тариф и момент начисления были заранее в брони.

## FAQ in article.html

None — no h2 «Частые вопросы».
