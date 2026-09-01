# Schema inputs — B06

topic_id: B06
article_dir: memory/blog/articles/B06-vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/`
   - `@id`: `{{SITE_BASE}}/blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — выезд в полдень, поезд через несколько часов, куда деть чемоданы между сдачей ключей и отправлением в Тюмени; договориться о багаже заранее или вокзальная камера хранения; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-01`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда",
  "h1": "Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда",
  "slug": "vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu",
  "topic_id": "B06",
  "author_id": "dobry-dom",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда

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

Гость сдаёт квартиру в полдень, а поезд только к половине пятого — 4,5 часа между ключами и отправлением. Посуточная квартира не отель: без договорённости с хостом багаж после выезда не хранят; чемоданы у подъезда — риск. Рабочий маршрут: заранее спросить менеджера или сдать вещи в камеру хранения на вокзале Тюмени с запасом по времени.

## FAQ in article.html

None — no h2 «Частые вопросы».
