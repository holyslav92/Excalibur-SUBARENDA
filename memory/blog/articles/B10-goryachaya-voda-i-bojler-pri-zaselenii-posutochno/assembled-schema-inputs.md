# Schema inputs — B10

topic_id: B10
article_dir: memory/blog/articles/B10-goryachaya-voda-i-bojler-pri-zaselenii-posutochno
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — `@graph` with Organization + BlogPosting. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. Organization **Добрый дом** with `@id` `{{SITE_BASE}}/#organization`, telephone `+7 (993) 574-83-22`, addressLocality Тюмень, addressCountry RU
3. BlogPosting canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/goryachaya-voda-i-bojler-pri-zaselenii-posutochno/`
   - `@id`: `{{SITE_BASE}}/blog/goryachaya-voda-i-bojler-pri-zaselenii-posutochno/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «горячая вода есть» не значит готовый душ; бойлер может быть выключен и нагрев ~40 минут; уточнить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-04`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
11. **NO HowTo** — not required for this archetype.

## article.meta.json

```json
{
  "title": "«Горячая вода есть». Включили душ — лёд и 40 минут нагрева",
  "h1": "«Горячая вода есть». Включили душ — лёд и 40 минут нагрева",
  "slug": "goryachaya-voda-i-bojler-pri-zaselenii-posutochno",
  "topic_id": "B10",
  "author_id": "dobry-dom",
  "date": "2026-09-04",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B10",
  "h1": "«Горячая вода есть». Включили душ — лёд и 40 минут нагрева",
  "title": "Квартиры посуточно в Тюмени: «горячая вода есть» — а душ ледяной",
  "subject": "Горячая вода и выключенный бойлер при заселении в квартиру посуточно"
}
```

## H1 (exact headline)

«Горячая вода есть». Включили душ — лёд и 40 минут нагрева

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

Гость после дороги видит «горячая вода есть», включает душ — вода ледяная. Бойлер выключен, нагрев около 40 минут, в сообщении нет инструкции. «Есть» описывает оборудование, а не готовность. До оплаты спросить: где бойлер, кто включает, сколько ждать нагрева.

## FAQ in article.html

None — no h2 «Частые вопросы».
