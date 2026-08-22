# Excalibur BLOG — pipeline fix queue

## INC-20260822-1320-publish-b03-idn-link-verify
status: open
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
symptom: link-verify FAIL on cyrillic IDN hrefs (добрыйдом-72.рф) — urllib latin-1 codec error
fix_applied: replaced booking/site hrefs with {{SITE_BASE}}/booking/ and {{SITE_BASE}}/ in article.html before publish
follow_up: teach link_verify classify_link to treat unicode host == punycode PUBLIC_SITE_URL as internal_absolute

## INC-20260822-1315-publish-schema-wp-head
status: open
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
symptom: live gate jsonld=0 — excalibur schema meta set but not echoed in wp_head
fix_applied: patched wp-content/themes/theme/functions.php to use get_queried_object_id() + is_singular('post') instead of get_the_ID() in wp_head
follow_up: add same fix to theme_contract_deploy default patch; document `theme` slug for Добрый дом (not kov4eg-mcp-theme)

## INC-20260822-1325-publish-schema-blog-permalink
status: open
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
symptom: BlogPosting JSON-LD URL mismatch — committed schema uses /{slug}/ but WP permalink is /blog/{slug}/
fix_applied: rewrite_schema_urls_for_blog_permalink() in excalibur_blog_wp_publish.load_article at runtime
follow_up: optional tenant-config blog_path_prefix for non-/blog tenants

## INC-20260822-1324-publish-llms-transport-import
status: open
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
symptom: publish crashed after live PASS — ImportError resolve_publish_transport from excalibur_blog_remote_transport
fix_applied: added resolve_publish_transport + upload_text_file to remote_transport.py; ran llms deploy manually
follow_up: none
