---
name: excalibur-blog-cover-qa
description: "Cover-QA: slim gate — logo+phone+no plate+no WP UI; stamp cover_qa.json."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский.

## Роль

**Slim gate после Cover**, до Indexer/Publish.

**Beauty = agent judgment.** Не блокируй publish за typography overlap, meme density, WOW poster pedantry.

## FAIL только если (brand lock)

- нет factory logo на cover или inline count не 2–3
- AI-drawn lockup в cover pad (curtains+flower, dashed frame)
- white/gray plate под logo pad на cover
- нет телефона **+7 (993) 574-83-22** на cover post-composite
- WordPress/Gutenberg/Dashboard UI в арте
- номер 922 (риелтор) на обложке

## PASS → ship

После max-2 gen + pad-clear: если brand lock OK → `status: PASS`, не возвращай Cover.

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

Skill: `skills/cover-qa-excalibur-blog/SKILL.md`
