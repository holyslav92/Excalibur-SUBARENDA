# Schema inputs — B23

topic_id: B23
article_dir: memory/blog/articles/B23-napisali-uborka-vklyuchena-na-vyezde-1800-za-gryaznye-prostyni
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/napisali-uborka-vklyuchena-na-vyezde-1800-za-gryaznye-prostyni/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-uborka-vklyuchena-na-vyezde-1800-za-gryaznye-prostyni/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «уборка включена», три ночи в Тюмени, на выезде фото простыни и доплата 1 800 ₽ без заранее показанного правила; что уточнить до брони; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-14`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "В карточке: «уборка включена» — 3 ночи. Выезд: фото простыни — 1 800 ₽",
  "h1": "В карточке: «уборка включена» — 3 ночи. Выезд: фото простыни — 1 800 ₽",
  "slug": "napisali-uborka-vklyuchena-na-vyezde-1800-za-gryaznye-prostyni",
  "topic_id": "B23",
  "author_id": "dobry-dom",
  "date": "2026-09-14",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

В карточке: «уборка включена» — 3 ночи. Выезд: фото простыни — 1 800 ₽

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

Гость снял квартиру в Тюмени на три ночи по 10 800 ₽ с обещанием «уборка включена в цену». На выезде хост показал фото использованной простыни и потребовал 1 800 ₽ — без ссылки на правила и без сравнения с состоянием при заселении. Разбор: обычное использование белья ≠ порча; «уборка включена» нужно расшифровать до брони (полы, санузел, смена белья, стирка); фотофиксация при заезде снимает спор на выходе.

## FAQ in article.html

None — no h2 «Частые вопросы».
