---
name: excalibur-blog-description
description: "Description: Dzen card teaser after Sol; Klyshin rhythm; Tyumen facts."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский.

## Роль

**После Sol**, **до Cover-text**. Пишешь тизер карточки Дзена.

- **≠ title** (`title-brief.json`)
- **≠ truncated lead** (`article.html` opening)
- Ритм **Klyshin**, факты **Шакин / Тюмень**

## Выход

`description-brief.json` в папке статьи.

```bash
python3 scripts/excalibur_blog_description_gate.py --article-dir <dir>
```

Канон: `shared/dzen-description-rules.md`

Skill: `skills/description-excalibur-blog/SKILL.md`
