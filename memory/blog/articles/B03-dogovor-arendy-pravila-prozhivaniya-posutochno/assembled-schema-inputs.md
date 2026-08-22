# Schema assembled inputs — B03 «Добрый дом»

OUTPUT: **ONLY** valid `schema.jsonld` JSON (no markdown fences, no commentary).

## Site base (HARD)

- Use placeholder `{{SITE_BASE}}` for all URLs — never literal host, never `[REDACTED]`.
- Canonical article URL: `{{SITE_BASE}}/dogovor-arendy-pravila-prozhivaniya-posutochno/` — **no** `/blog/` prefix.

## article.meta.json

```json
{
  "title": "Перевёл предоплату — потом прочитал 7 запретов в договоре",
  "h1": "Перевёл предоплату — потом прочитал 7 запретов в договоре",
  "slug": "dogovor-arendy-pravila-prozhivaniya-posutochno",
  "topic_id": "B03",
  "author_id": "dobry-dom",
  "date": "2026-08-22"
}
```

## research-context (datePublished)

- today_iso: **2026-08-22**
- datePublished and dateModified: **2026-08-22**

## Author (from shared/authors-registry.json, id dobry-dom)

- name: **Добрый дом**
- Use `@type`: **Organization** (same as B01/B02 sibling schemas)
- url: `{{SITE_BASE}}/`

## Description (for BlogPosting.description)

Как не попасть в ловушку договора посуточной аренды: читать правила до перевода предоплаты, семь пунктов оферты, акцепт оплатой и что проверить за три минуты в Тюмени.

## FAQ section (visible in article.html — include FAQPage as mainEntity)

Section `<h2>Частые вопросы</h2>`. **Only** pairs `<h3>question</h3><p>first answer paragraph</p>`.
**Do NOT** include the CTA `<p>` after FAQ (booking link, phone) — it is not part of FAQPage.

1. **Q:** Если я перевёл предоплату, значит, согласился со всеми правилами?
   **A:** Не обязательно. Оплата может считаться согласием, если условия были доступны вам до перевода. Если правила показали только после оплаты, ситуация другая.

2. **Q:** Можно передать код от квартиры другу или коллеге?
   **A:** Сначала проверьте правила. Во многих объектах передавать ключи и коды третьим лицам нельзя.

3. **Q:** Ранний заезд можно считать включённым?
   **A:** Нет. Его лучше согласовать заранее и сохранить договорённость в переписке.

4. **Q:** Когда вернут обеспечительный платёж?
   **A:** Это зависит от условий брони: заранее посмотрите сумму, срок возврата и причины возможного удержания.

`acceptedAnswer.text` = **exact plain text** of first `<p>` after each `<h3>` (no HTML).

## Schema structure (match sibling B01/B02)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{SITE_BASE}}/dogovor-arendy-pravila-prozhivaniya-posutochno/#article",
  "url": "{{SITE_BASE}}/dogovor-arendy-pravila-prozhivaniya-posutochno/",
  "headline": "...",
  "description": "...",
  "inLanguage": "ru-RU",
  "datePublished": "2026-08-22",
  "dateModified": "2026-08-22",
  "author": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "{{SITE_BASE}}/dogovor-arendy-pravila-prozhivaniya-posutochno/" },
  "publisher": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" },
  "mainEntity": { "@type": "FAQPage", "mainEntity": [ ... ] }
}
```

No HowTo. No Review.
