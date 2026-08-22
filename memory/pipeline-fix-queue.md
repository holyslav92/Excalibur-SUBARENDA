# Pipeline fix queue

## INC-20260822-0700 — live-page gate vs Добрый дом theme

- **symptom:** `excalibur_blog_live_page_gate.py` BLOCK after successful WP publish (post 3835 B03); same errors on B01/B02.
- **cause:** Gate expects `kov4eg-mcp-theme` markers (`#article-content`, `.post-thumbnail`, `_excalibur_blog_schema_jsonld` in `wp_head`). Timeweb theme uses `entry-content` / `wp-post-image`; Yoast `@graph` Article only. `excalibur_blog_theme_contract_deploy.py` uses SFTP:22 and cannot find theme path (tenant uses FTP:21).
- **workaround:** WP publish + media upload succeed; verify `wp-content` img src manually; ledger updated post-publish.
- **fix:** (1) theme contract deploy over FTP via `excalibur_blog_remote_transport`; (2) live gate fallbacks for `entry-content` / `wp-post-image`; (3) optional tenant flag to skip schema parity when theme outputs Yoast graph only.
