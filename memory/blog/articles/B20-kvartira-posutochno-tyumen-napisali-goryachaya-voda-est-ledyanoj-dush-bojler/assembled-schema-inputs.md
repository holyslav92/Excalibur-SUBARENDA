# Schema inputs — B20

topic_id: B20
article_dir: memory/blog/articles/B20-kvartira-posutochno-tyumen-napisali-goryachaya-voda-est-ledyanoj-dush-bojler
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief, NOT article-dir suffix):
   - `url`: `{{SITE_BASE}}/blog/napisali-goryachaya-voda-est-ledyanoj-dush-migayushij-boiler/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-goryachaya-voda-est-ledyanoj-dush-migayushij-boiler/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — в карточке «горячая вода есть», ночью ледяной душ и мигающий бойлер; накопительный бак и 80 минут до тепла; проверка при заселении; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-13`
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
  "title": "Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла",
  "h1": "Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла",
  "slug": "napisali-goryachaya-voda-est-ledyanoj-dush-migayushij-boiler",
  "topic_id": "B20",
  "author_id": "dobry-dom",
  "date": "2026-09-13",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла

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

Гость заселился вечером: в карточке «горячая вода есть», в душе — ледяная вода, на бойлере мигает индикатор. Накопительный бак 50 л после расхода предыдущих гостей догревается 80–160 минут. Разбор: спросить объём бойлера до оплаты, проверить кран при заселении, не крутить настройки самостоятельно — писать администратору с фото.

## FAQ in article.html

None — no h2 «Частые вопросы».
