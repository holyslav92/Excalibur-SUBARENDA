# Schema inputs — B10

**OUTPUT:** ONLY valid JSON for schema.jsonld (single JSON object). No markdown fences, no commentary.

## Article

- topic_id: B10
- slug: hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400
- headline (from article.meta.json h1): Хозяин сказал «всё включено». В такси доплатили 2 400 ₽
- datePublished: 2026-09-05
- dateModified: 2026-09-05
- inLanguage: ru-RU
- city/local intent: Тюмень (посуточная аренда)

## URLs (HARD)

Use placeholder `{{SITE_BASE}}` only — never literal host or [REDACTED].
Canonical article URL: `{{SITE_BASE}}/blog/hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400/`
BlogPosting url, @id, mainEntityOfPage.@id must all use `/blog/<slug>/` path.

## Author / publisher (HARD)

- Author = Organization «Добрый дом» from shared/authors-registry.json (id: dobry-dom)
- NEVER mention Святослав Шакин / The Риэлтор
- Include Organization node with NAP: name «Добрый дом», addressLocality «Тюмень», addressCountry «RU», telephone «+7 (993) 574-83-22»
- Prefer @graph pattern like B09 schema (Organization + BlogPosting)

## FAQ

NO FAQPage — article has no «Частые вопросы» section (theme_blocks.faq=skip). BlogPosting only.

## Description hint

Opening pain: хозяин обещал «всё включено», гость уже в такси получил список доплат на 2 400 ₽ (уборка, коммуналка, сервис, полотенца) перед заселением.

## BAN

- Do not stuff «посуточная аренда тюмень» as SEO keyword dump
- No FAQPage without visible FAQ h3 pairs

## Reference files

- article.html: memory/blog/articles/B10-hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400/article.html
- article.meta.json: same dir
- authors-registry: shared/authors-registry.json
