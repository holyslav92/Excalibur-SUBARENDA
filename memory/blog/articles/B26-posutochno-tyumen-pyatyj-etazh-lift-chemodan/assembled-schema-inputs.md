# Schema inputs — B26

topic_id: B26
article_dir: memory/blog/articles/B26-posutochno-tyumen-pyatyj-etazh-lift-chemodan
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief, NOT article-dir suffix):
   - `url`: `{{SITE_BASE}}/blog/posutochno-tyumen-pyatyj-etazh-lift-chemodan/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-tyumen-pyatyj-etazh-lift-chemodan/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — галочка «лифт» не отвечает на вопрос о работе кабины сегодня; гость с чемоданом у подъезда, квартира на пятом этаже после оплаты; до перевода спросить этаж и статус лифта письменно; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-17`
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
  "title": "Квартира на пятом этаже. Лифт встал — 2 ночи, чемодан внизу",
  "h1": "Квартира на пятом этаже. Лифт встал — 2 ночи, чемодан внизу",
  "slug": "posutochno-tyumen-pyatyj-etazh-lift-chemodan",
  "topic_id": "B26",
  "author_id": "dobry-dom",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Квартира на пятом этаже. Лифт встал — 2 ночи, чемодан внизу

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

Гость перевёл 8 400 ₽ за две ночи, приехал с чемоданом — у подъезда табличка «лифт не работает», квартира на пятом этаже. В карточке была галочка «лифт», но этаж и актуальный статус кабины не проговорили до оплаты. Разбор: спросить этаж и «лифт работает сегодня?» письменно до перевода; табличка у подъезда — повод уточнить у хоста, а не тащить багаж наверх.

## FAQ in article.html

None — no h2 «Частые вопросы».
