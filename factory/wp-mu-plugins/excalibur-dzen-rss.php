<?php
/**
 * Excalibur BLOG — правки RSS /feed/zen/ для Яндекс Дзен.
 *
 * Плагин «RSS for Yandex Zen» по умолчанию:
 * - ставит native-no (картинка без текста в Студии);
 * - добавляет enclosure для каждого <img> в content:encoded.
 *
 * MU-plugin:
 * - одна enclosure (обложка, full size);
 * - category format-article;
 * - убирает native-no;
 * - full URL обложки через yzen_thumb_imgurl.
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Не выпускать native-no в RSS (глобально через фильтр плагина).
 */
add_filter('yzen_type_platform', static function ($value) {
    if ($value === 'native-no') {
        return 'native-yes';
    }
    return $value;
});

/**
 * Обложка в content:encoded и enclosure — full/largest, не -1024x576.
 */
add_filter('yzen_thumb_imgurl', static function ($url) {
    if (!is_string($url) || $url === '') {
        return $url;
    }
    $path = wp_parse_url($url, PHP_URL_PATH);
    if (!is_string($path) || $path === '') {
        return $url;
    }
    $full_path = preg_replace('/-\d+x\d+\.(png|jpe?g|webp)$/i', '.$1', $path);
    if ($full_path === $path) {
        return $url;
    }
    $upload = wp_upload_dir();
    $basedir = rtrim((string) ($upload['basedir'] ?? ''), '/');
    $baseurl = rtrim((string) ($upload['baseurl'] ?? ''), '/');
    if ($basedir !== '' && $baseurl !== '' && is_file($basedir . $full_path)) {
        return $baseurl . $full_path;
    }
    return $url;
});

add_action('template_redirect', static function () {
    if (!is_feed('zen')) {
        return;
    }
    ob_start('excalibur_dzen_sanitize_feed_xml');
}, 0);

/**
 * @param string $xml
 */
function excalibur_dzen_sanitize_feed_xml($xml)
{
    if (!is_string($xml) || stripos($xml, '<rss') === false) {
        return $xml;
    }

    return (string) preg_replace_callback(
        '/<item>(.*?)<\/item>/si',
        static function (array $match) {
            return excalibur_dzen_sanitize_feed_item($match[1]);
        },
        $xml
    );
}

/**
 * @param string $item_inner
 */
function excalibur_dzen_sanitize_feed_item($item_inner)
{
    $item = (string) $item_inner;

    $item = (string) preg_replace('/\s*<category>native-no<\/category>\s*/i', '', $item);

    if (!preg_match('/<category>format-article<\/category>/i', $item)) {
        if (preg_match('/<author>.*?<\/author>/si', $item)) {
            $item = (string) preg_replace(
                '/(<author>.*?<\/author>)/si',
                '$1' . "\n        <category>format-article</category>",
                $item,
                1
            );
        } else {
            $item = "\n        <category>format-article</category>" . $item;
        }
    }

    $parts = preg_split('/(<enclosure\s[^>]*\/?>)/i', $item, -1, PREG_SPLIT_DELIM_CAPTURE);
    if (!is_array($parts)) {
        return '<item>' . $item . '</item>';
    }

    $out = '';
    $enclosure_kept = false;
    foreach ($parts as $part) {
        if (preg_match('/^<enclosure/i', $part)) {
            if (!$enclosure_kept) {
                $part = (string) preg_replace(
                    '/(<enclosure\s+url="[^"]*)-\d+x\d+(\.(png|jpe?g|webp))"/i',
                    '$1$2"',
                    $part,
                    1
                );
                $out .= $part;
                $enclosure_kept = true;
            }
            continue;
        }
        $out .= $part;
    }

    return '<item>' . $out . '</item>';
}
