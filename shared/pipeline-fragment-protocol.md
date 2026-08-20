# Parallel fragment protocol

Parallel subagents do not write the shared handoff. Each owns one file:

```text
.cursor/excalibur-blog-fragments/<role>.md
```

## Required frontmatter

Every fragment **must** start with YAML frontmatter. Body-only marker blocks
(`=== EXCALIBUR BLOG COVER ===` without `---`) fail
`scripts/excalibur_blog_handoff_merge.py` with `frontmatter missing`
(B65 / INC-20260720-1556).

```yaml
---
role: excalibur-blog-cover
topic_id: Bxx
article_dir: memory/blog/articles/Bxx-slug
status: PASS # PASS | BLOCKER  (not ✅/❌)
completed_at: 2026-07-20T15:00:00Z
incident_report: none
artifacts:
  - cover/cover.png
---
```

Required keys for merge: `role`, `status`, `completed_at`, `incident_report`.
`status` must be exactly `PASS` for a successful merge (or merge blocks on
`BLOCKER`).

The body starts with the role marker, e.g.
`=== EXCALIBUR BLOG COVER ===`.

### Cover example

```markdown
---
role: excalibur-blog-cover
topic_id: B65
article_dir: memory/blog/articles/B65-slug
status: PASS
completed_at: 2026-07-20T15:56:00Z
incident_report: none
artifacts:
  - cover/cover.png
---

=== EXCALIBUR BLOG COVER ===
topic_id: B65
status: PASS
...
```

### Schema example

```markdown
---
role: excalibur-blog-schema
topic_id: B65
article_dir: memory/blog/articles/B65-slug
status: PASS
completed_at: 2026-07-20T15:56:00Z
incident_report: none
artifacts:
  - schema.jsonld
---

=== EXCALIBUR BLOG SCHEMA ===
topic_id: B65
verdict: PASS
...
```

## Director merge

After every parallel wave:

```bash
python3 scripts/excalibur_blog_handoff_merge.py \
  --handoff .cursor/excalibur-blog-handoff.md \
  --fragments-dir .cursor/excalibur-blog-fragments \
  --wave cover,schema
```

The merge is atomic and idempotent. It blocks on missing fragments, malformed
frontmatter or `status: BLOCKER`. Only Director writes the final handoff.

## Current fragment waves

- `cover,schema` (Writer пишет один `drafts/variant-a.html`, без status fragments)

Indexer ждёт cover + schema fragments (+ freshness). Visual QA удалён.
