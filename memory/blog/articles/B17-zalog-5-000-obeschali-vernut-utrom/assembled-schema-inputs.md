# Schema inputs — B17

topic_id: B17
article_dir: memory/blog/articles/B17-zalog-5-000-obeschali-vernut-utrom
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-utrom/`
   - `@id`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-utrom/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — залог 5 000 ₽, обещали вернуть утром после выезда, вместо этого «после уборки» без даты; до перевода спросить день и способ возврата; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-11`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Залог 5 000 ₽ обещали вернуть утром. А потом — «после уборки»",
  "h1": "Залог 5 000 ₽ обещали вернуть утром. А потом — «после уборки»",
  "slug": "zalog-5-000-obeschali-vernut-utrom",
  "topic_id": "B17",
  "author_id": "dobry-dom",
  "date": "2026-09-11",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Залог 5 000 ₽ обещали вернуть утром. А потом — «после уборки»

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

Пара перевела 5 000 ₽ залога за две ночи в Тюмени; до оплаты обещали вернуть утром после выезда. Гости выехали вовремя, оставили чистую квартиру и отправили фото, но на следующее утро получили «залог вернём после уборки» — без даты, суммы и способа перевода. Фраза «после уборки» не заменяет заранее названный срок. До перевода залога нужно спросить день возврата и канал перевода.

## FAQ in article.html

None — no h2 «Частые вопросы».
