# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon/`
   - `@id`: `{{SITE_BASE}}/blog/pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — обещание «рабочий стол» и «быстрый интернет» не отвечает на созвон; гость за 11 400 ₽ получил журнальный столик, розетку за диваном и Wi‑Fi ~8 Мбит; до перевода проверить стол, связь и закрывающие; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-10`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "«Рабочий стол» обещали. За 11 400 ₽ — журнальный столик",
  "h1": "«Рабочий стол» обещали. За 11 400 ₽ — журнальный столик",
  "slug": "pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Рабочий стол» обещали. За 11 400 ₽ — журнальный столик

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

Командировочный гость переводит 11 400 ₽ за три ночи после обещания «всё есть, быстрый интернет, справку пришлём». После позднего заселения оказывается журнальный столик вместо рабочего места, розетка за диваном, Wi‑Fi около 8 Мбит не тянет видеосозвон, а закрывающие обещают «после выезда». До оплаты нужно проверить стол с розеткой, связь из точки работы и список документов со сроком.

## FAQ in article.html

None — no h2 «Частые вопросы».
