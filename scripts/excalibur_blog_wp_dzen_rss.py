#!/usr/bin/env python3
"""Dzen RSS helpers: yzen_options, post meta, MU-plugin deploy."""

from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MU_PLUGIN_REL = "wp-content/mu-plugins/excalibur-dzen-rss.php"
MU_PLUGIN_SRC = ROOT / "factory/wp-mu-plugins/excalibur-dzen-rss.php"

# Post meta keys used by «RSS for Yandex Zen».
YZEN_META_PLATFORM = "yztypeplatform_meta_value"
YZEN_META_ARTICLE = "yztypearticle_meta_value"
YZEN_META_INDEX = "yzindex_meta_value"

# Canon: never native-no; materials → evergreen via yztypearticle=false.
DZEN_PLATFORM_NATIVE_YES = "native-yes"
DZEN_ARTICLE_MATERIAL = "false"
DZEN_INDEX = "index"
DZEN_FORBIDDEN_PLATFORM = "native-no"
DZEN_FORMAT_CATEGORY = "format-article"
DZEN_AUTHOR_DEFAULT = "Добрый дом"
DZEN_THUMB_SIZE = "full"


def mu_plugin_bytes() -> bytes:
    if not MU_PLUGIN_SRC.is_file():
        raise FileNotFoundError(f"MU-plugin missing: {MU_PLUGIN_SRC}")
    return MU_PLUGIN_SRC.read_bytes()


def default_yzen_options(public_site_url: str, author: str = DZEN_AUTHOR_DEFAULT) -> dict[str, str]:
    """Global yzen_options patch for RSS for Yandex Zen."""
    site = public_site_url.rstrip("/")
    return {
        "yzlink": site,
        "yzauthor": author,
        "yztypeplatform": DZEN_PLATFORM_NATIVE_YES,
        "yztypearticle": DZEN_ARTICLE_MATERIAL,
        "yzindex": DZEN_INDEX,
        "yzthumbnail": "enabled",
        "yzselectthumb": DZEN_THUMB_SIZE,
    }


def post_dzen_meta_values() -> dict[str, str]:
    return {
        YZEN_META_PLATFORM: DZEN_PLATFORM_NATIVE_YES,
        YZEN_META_ARTICLE: DZEN_ARTICLE_MATERIAL,
        YZEN_META_INDEX: DZEN_INDEX,
    }


def build_yzen_options_bootstrap(public_site_url: str) -> str:
    opts = default_yzen_options(public_site_url)
    encoded = base64.b64encode(json.dumps(opts, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p)) {{
    echo 'ERR dzen_rss: bad payload' . PHP_EOL;
    exit(1);
}}
$opts = get_option('yzen_options');
if (!is_array($opts)) {{
    $opts = [];
}}
foreach ($p as $key => $value) {{
    $opts[$key] = $value;
}}
update_option('yzen_options', $opts);
echo 'OK yzen_options=' . base64_encode(json_encode($opts, JSON_UNESCAPED_UNICODE)) . PHP_EOL;
echo 'OK dzen_yzen_options_done' . PHP_EOL;
"""


def build_post_dzen_meta_bootstrap(
    post_id: int,
    *,
    bump_modified: bool = True,
    repoint_featured_full: bool = True,
) -> str:
    meta = post_dzen_meta_values()
    payload: dict[str, Any] = {
        "post_id": int(post_id),
        "meta": meta,
        "bump_modified": bool(bump_modified),
        "repoint_featured_full": bool(repoint_featured_full),
        "forbidden_platform": DZEN_FORBIDDEN_PLATFORM,
    }
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['post_id'])) {{
    echo 'ERR dzen_rss: bad post payload' . PHP_EOL;
    exit(1);
}}
$post_id = (int) $p['post_id'];
$post = get_post($post_id);
if (!$post || $post->post_type !== 'post') {{
    echo 'ERR dzen_rss: post not found id=' . $post_id . PHP_EOL;
    exit(1);
}}
$meta = is_array($p['meta'] ?? null) ? $p['meta'] : [];
foreach ($meta as $key => $value) {{
    update_post_meta($post_id, $key, $value);
}}
$forbidden = (string) ($p['forbidden_platform'] ?? 'native-no');
$stored = get_post_meta($post_id, 'yztypeplatform_meta_value', true);
if ($stored === $forbidden) {{
    update_post_meta($post_id, 'yztypeplatform_meta_value', 'native-yes');
}}
if (!empty($p['repoint_featured_full']) && has_post_thumbnail($post_id)) {{
    $thumb_id = (int) get_post_thumbnail_id($post_id);
    if ($thumb_id > 0) {{
        $full = wp_get_attachment_image_src($thumb_id, 'full');
        if (is_array($full) && !empty($full[0])) {{
            echo 'OK featured_full_url=' . $full[0] . PHP_EOL;
        }}
        $meta_data = wp_get_attachment_metadata($thumb_id);
        if (is_array($meta_data) && !empty($meta_data['file'])) {{
            echo 'OK featured_file=' . $meta_data['file'] . PHP_EOL;
        }}
    }}
}}
if (!empty($p['bump_modified'])) {{
    wp_update_post([
        'ID' => $post_id,
        'post_modified' => current_time('mysql'),
        'post_modified_gmt' => current_time('mysql', 1),
    ]);
    echo 'OK post_modified_bump=1' . PHP_EOL;
}}
echo 'OK dzen_post_meta=' . base64_encode(json_encode([
    'post_id' => $post_id,
    'yztypeplatform' => get_post_meta($post_id, 'yztypeplatform_meta_value', true),
    'yztypearticle' => get_post_meta($post_id, 'yztypearticle_meta_value', true),
    'yzindex' => get_post_meta($post_id, 'yzindex_meta_value', true),
    'modified_gmt' => get_post_field('post_modified_gmt', $post_id),
], JSON_UNESCAPED_UNICODE)) . PHP_EOL;
echo 'OK dzen_post_meta_done' . PHP_EOL;
"""


def build_mu_plugin_deploy_bootstrap(plugin_php: str) -> str:
    encoded = base64.b64encode(plugin_php.encode("utf-8")).decode("ascii")
    rel = MU_PLUGIN_REL.replace("\\", "/")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$rel = '{rel}';
$dir = dirname($rel);
$base = dirname(__FILE__);
$target_dir = $base . '/' . $dir;
$target = $base . '/' . $rel;
if (!is_dir($target_dir)) {{
    if (!wp_mkdir_p($target_dir)) {{
        echo 'ERR dzen_rss: mkdir failed ' . $target_dir . PHP_EOL;
        exit(1);
    }}
}}
$php = base64_decode('{encoded}');
if ($php === false || $php === '') {{
    echo 'ERR dzen_rss: empty mu-plugin payload' . PHP_EOL;
    exit(1);
}}
$written = file_put_contents($target, $php);
if ($written === false) {{
    echo 'ERR dzen_rss: write failed ' . $target . PHP_EOL;
    exit(1);
}}
echo 'OK mu_plugin_bytes=' . (int) $written . PHP_EOL;
echo 'OK mu_plugin_path=' . $rel . PHP_EOL;
echo 'OK dzen_mu_plugin_done' . PHP_EOL;
"""


def dzen_meta_php_snippet() -> str:
    """Inline PHP for publish bootstrap — set yzen post meta after categories."""
    meta = post_dzen_meta_values()
    lines = [
        "// Dzen RSS directives (RSS for Yandex Zen plugin).",
        f"update_post_meta($post_id, '{YZEN_META_PLATFORM}', '{meta[YZEN_META_PLATFORM]}');",
        f"update_post_meta($post_id, '{YZEN_META_ARTICLE}', '{meta[YZEN_META_ARTICLE]}');",
        f"update_post_meta($post_id, '{YZEN_META_INDEX}', '{meta[YZEN_META_INDEX]}');",
        "echo 'OK dzen_yzen_meta=1' . PHP_EOL;",
    ]
    return "\n".join(lines)
