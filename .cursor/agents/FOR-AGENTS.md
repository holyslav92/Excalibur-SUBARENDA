# Excalibur-2-Cloud — субагенты

Карта: [shared/pipeline-task-map.md](../shared/pipeline-task-map.md)

**Всего 18 ролей** (16 прежних + `description` + `cover-qa`).

## Директор и Setup (не Task)

| Роль | Файл | Skill |
|------|------|-------|
| Setup (первый запуск) | `excalibur-blog-setup.md` | `setup-excalibur-blog` |
| Директор (пайплайн) | `excalibur-blog-director.md` | `director-excalibur-blog` |

## Setup Task trio

| Task | Роль |
|------|------|
| setup-voice | SOUL + examples + article-style |
| setup-visual | cover configs + assets |

## Субагенты пайплайна (Task)

| # | Task | Роль |
|---|------|------|
| 🔍 | scout | Klyshin × Wordstat тема |
| ① | research | Facts |
| ①b | title | H1 |
| ② | writer | Смысл → `drafts/writer.html` |
| ②b | **sol** | **Финал `article.html` (слог SOUL)** |
| ②c | **description** | **Дзен-карточка → `description-brief.json`** |
| ④a | cover-text | RU надписи |
| ④b | schema | JSON-LD |
| ④c | cover | Image API + figures |
| ④d | **cover-qa** | **Визуальный gate → `cover/cover_qa.json`** |
| ⑤ | indexer | llms |
| ⑥ | publish | WP |
| ⑦ | fixer | Incidents |
| ⑦b | content-learner | Metrika |

## Канон порядка

```text
Scout? → Research → Title → Writer → Sol → Description
→ Cover-text || Schema → Cover → Cover-QA → Indexer → Publish
→ Fixer → Content-learner
```

После **Sol**: shell `pipeline_canon --stamp` + opening_meta / html_linter.

Пока setup не complete — только Setup (+ setup-voice/visual).

## Полный список имён (18)

1. `excalibur-blog-setup`
2. `excalibur-blog-setup-voice`
3. `excalibur-blog-setup-visual`
4. `excalibur-blog-director`
5. `excalibur-blog-scout`
6. `excalibur-blog-research`
7. `excalibur-blog-title`
8. `excalibur-blog-writer`
9. `excalibur-blog-sol`
10. `excalibur-blog-description`
11. `excalibur-blog-cover-text`
12. `excalibur-blog-schema`
13. `excalibur-blog-cover`
14. `excalibur-blog-cover-qa`
15. `excalibur-blog-indexer`
16. `excalibur-blog-publish`
17. `excalibur-blog-fixer`
18. `excalibur-blog-content-learner`
