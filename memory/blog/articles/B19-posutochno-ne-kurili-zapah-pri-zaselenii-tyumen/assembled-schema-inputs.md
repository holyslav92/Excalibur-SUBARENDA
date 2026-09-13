# Schema inputs — B19

topic_id: B19
article_dir: memory/blog/articles/B19-posutochno-ne-kurili-zapah-pri-zaselenii-tyumen
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief, NOT article-dir suffix):
   - `url`: `{{SITE_BASE}}/blog/napisali-ne-kurili-v-spalne-zapah-i-okno-na-zamke/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-ne-kurili-v-spalne-zapah-i-okno-na-zamke/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — в карточке «не курили», в спальне табачный запах и окно на детском замке без ключа; семья 35 минут в прихожей в Тюмени; проверка до принятия ночи; not duplicate headline verbatim.
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
  "title": "Написали «не курили». В спальне — запах и окно на замке: 35 минут ожидания ключа",
  "h1": "Написали «не курили». В спальне — запах и окно на замке: 35 минут ожидания ключа",
  "slug": "napisali-ne-kurili-v-spalne-zapah-i-okno-na-zamke",
  "topic_id": "B19",
  "author_id": "dobry-dom",
  "date": "2026-09-13",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «не курили». В спальне — запах и окно на замке: 35 минут ожидания ключа

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

Семья приехала на посуточное заселение в Тюмени: в карточке «не курили», в спальне — стойкий табачный запах, окно на детской защите без ключа в квартире. 35 минут в прихожей с ребёнком, пока ждали ответ. Разбор: фиксировать запах и невозможность проветрить до принятия ночи; не разбирать фурнитуру самостоятельно; ключ, замена или отмена — зона хозяина.

## FAQ in article.html

None — no h2 «Частые вопросы».
