# Schema inputs — B17

topic_id: B17
article_dir: memory/blog/articles/B17-posutochno-v-tyumeni-napisali-teplo-est-batarei-holodnye
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-v-tyumeni-napisali-teplo-est-batarei-holodnye/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-v-tyumeni-napisali-teplo-est-batarei-holodnye/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «тепло есть» в объявлении, +6 °C за окном, холодные батареи на две оплаченные ночи; до перевода спросить, греют ли радиаторы сегодня вечером; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-12`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Написали «тепло есть». За окном +6 °C — батареи холодные на 2 ночи",
  "h1": "Написали «тепло есть». За окном +6 °C — батареи холодные на 2 ночи",
  "slug": "posutochno-v-tyumeni-napisali-teplo-est-batarei-holodnye",
  "topic_id": "B17",
  "author_id": "dobry-dom",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «тепло есть». За окном +6 °C — батареи холодные на 2 ночи

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

Гость перевёл 6 800 ₽ за две ночи в Тюмени после обещания «тепло есть» в карточке и чате. Вечером за окном около +6 °C, в комнате 16–17 °C, батарея и стояк холодные. Хозяин отвечает «сезон ещё не начался» и предлагает плед. До оплаты нужно спросить: батареи в этой квартире греют сегодня вечером или отопление только после старта сезона.

## FAQ in article.html

None — no h2 «Частые вопросы».
