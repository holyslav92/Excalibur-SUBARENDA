# Schema inputs — B03

Output ONLY valid JSON-LD (single JSON object). No markdown fences, no commentary.

## Site base

Use placeholder `{{SITE_BASE}}` for all URLs. Never use `[REDACTED]` or live host literals.
Canonical article URL: `{{SITE_BASE}}/pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti/`
Never use `/blog/` in article URLs.

## Article meta

- topic_id: B03
- slug: pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti
- headline: Перевели предоплату. В правилах мелким: вечеринки и лишние гости
- datePublished: 2026-08-22
- dateModified: 2026-08-22
- inLanguage: ru-RU
- author_id: dobry-dom

## Author (from shared/authors-registry.json)

- name: Добрый дом
- jobTitle: Апартаменты и квартиры посуточно в Тюмени
- worksFor: Добрый дом
- url: {{SITE_BASE}}/
- sameAs: ["{{SITE_BASE}}/", "{{SITE_BASE}}/blog/"]

Use @type Organization for author and publisher (match sibling articles B01/B02).

## Description (for BlogPosting.description)

Семь пунктов в правилах посуточной аренды, которые лучше проверить до предоплаты: гости, вечеринки, курение, время заезда и выезда, залог и последствия нарушений в Тюмени.

## FAQ section (visible in article.html — include FAQPage as mainEntity)

Extract acceptedAnswer.text from FIRST <p> after each <h3> only (plain text, no HTML):

1. Q: Друг зашёл на два часа — это лишний гость?
   A: Чаще всего да, если в правилах запрещены посещения третьими лицами. Лучше согласовать заранее в переписке. Обычно предупредить проще, чем объясняться ночью.

2. Q: Я не читал правила. Они всё равно действуют?
   A: Если правила прислали до оплаты, а после этого вы перевели деньги, хозяин считает это согласием. Две минуты чтения обычно дешевле залога.

3. Q: Можно договориться на день рождения?
   A: Иногда можно, за отдельную доплату и с увеличенным залогом. Но обсуждать это нужно до брони. Скрытая вечеринка часто заканчивается ночным выездом.

4. Q: Что делать, если хозяин не даёт правил?
   A: Попросите хотя бы текстом про гостей, тишину, курение и залог. Если прислать не готовы, лучше поискать другую квартиру.

## Schema structure (match B01/B02 pattern)

- @context: https://schema.org
- @type: BlogPosting
- @id: {{SITE_BASE}}/pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti/#article
- url, headline, description, inLanguage, datePublished, dateModified
- author: Organization (Добрый дом)
- publisher: Organization (Добрый дом)
- mainEntityOfPage: WebPage
- mainEntity: FAQPage with mainEntity array of Question/Answer pairs (exact text from FAQ above)
