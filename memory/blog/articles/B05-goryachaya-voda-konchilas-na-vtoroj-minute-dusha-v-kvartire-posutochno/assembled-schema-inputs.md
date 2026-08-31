# Schema inputs — B05

topic_id: B05
article_dir: memory/blog/articles/B05-goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno/`
   - `@id`: `{{SITE_BASE}}/blog/goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — бойлер в квартире посуточно не гарантирует горячую воду сразу после позднего заселения; проверить статус бака до душа; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-31`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Горячая вода была. На второй минуте душ — холод",
  "h1": "Горячая вода была. На второй минуте душ — холод",
  "slug": "goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno",
  "topic_id": "B05",
  "author_id": "dobry-dom",
  "date": "2026-08-31",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Горячая вода была. На второй минуте душ — холод

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

Гость после позднего заселения в квартиру посуточно в Тюмени получает две минуты тёплой воды, потом лёд из крана. «Бойлер есть» не равно «горячая вода сейчас»: бак мог быть пуст после предыдущих гостей, не прогрет после уборки или сломан. Хост должен заранее сообщить статус бойлера и время нагрева, а не прятать инструкцию в PDF.

## FAQ in article.html

None — no h2 «Частые вопросы».
