# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-napisali-s-detmi-mozhno-doplata-za-malysha
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/napisali-s-detmi-mozhno-doplata-za-malysha/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-s-detmi-mozhno-doplata-za-malysha/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — фраза «с детьми можно» не означает цену и кроватку; семья с трёхлеткой после оплаты ~7 900 ₽ узнаёт у двери о доплате 2 000 ₽; до перевода уточнить возраст, тариф, сумму и место для сна; not duplicate headline verbatim.
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
  "title": "«С детьми можно» в чате. У двери — 2 000 ₽ за трёхлетку",
  "h1": "«С детьми можно» в чате. У двери — 2 000 ₽ за трёхлетку",
  "slug": "napisali-s-detmi-mozhno-doplata-za-malysha",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«С детьми можно» в чате. У двери — 2 000 ₽ за трёхлетку

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

Семья бронирует квартиру посуточно на две ночи (~7 900 ₽) после обещания «с детьми можно». У двери хозяин просит 2 000 ₽ за трёхлетку — суммы не было в карточке и чате. Кроватка может оказаться люлькой для младенца, а ребёнку предлагают диван без бортиков. Фраза «можно» не отвечает на вопросы о тарифе, доплате и месте для сна — их нужно зафиксировать в переписке до оплаты.

## FAQ in article.html

None — no h2 «Частые вопросы».
