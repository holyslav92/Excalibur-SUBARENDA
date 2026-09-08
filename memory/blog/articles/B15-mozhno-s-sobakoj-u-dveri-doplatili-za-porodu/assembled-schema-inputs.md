# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-mozhno-s-sobakoj-u-dveri-doplatili-za-porodu
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/mozhno-s-sobakoj-u-dveri-doplatili-za-porodu/`
   - `@id`: `{{SITE_BASE}}/blog/mozhno-s-sobakoj-u-dveri-doplatili-za-porodu/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «можно с собакой» в чате не фиксирует условия; у двери появляется доплата 3 000 ₽ за «крупную породу» или удвоенный залог; до оплаты уточнить вес, сумму и залог письменно; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-08`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "«С собакой можно» — у двери крупная порода стоила 3 000 ₽",
  "h1": "«С собакой можно» — у двери крупная порода стоила 3 000 ₽",
  "slug": "mozhno-s-sobakoj-u-dveri-doplatili-za-porodu",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-08",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«С собакой можно» — у двери крупная порода стоила 3 000 ₽

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

Гость бронирует квартиру на две ночи около 6 800 ₽, в чате слышит «с собакой можно», приезжает с питомцем — и у двери хост называет собаку крупной породой и требует 3 000 ₽ или удвоенный залог «за шерсть». Проблема не в самой доплате, а в том, что условие появляется в момент, когда отказаться дороже всего. До перевода нужно письменно согласовать породу, вес, сумму, тип залога и момент оплаты.

## FAQ in article.html

None — no h2 «Частые вопросы».
