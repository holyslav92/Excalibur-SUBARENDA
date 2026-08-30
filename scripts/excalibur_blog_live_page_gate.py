#!/usr/bin/env python3
"""Verify that the live theme does not bury or duplicate Excalibur article content."""
from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from excalibur_blog_html_linter import (
    extract_faq_answer_after_h3,
    extract_thematic_faq_bodies,
    is_faq_section_heading,
)
from excalibur_blog_link_verify import encode_idna_url

FORBIDDEN = {
    "engagement_quiz": r"engagement-quiz|КВЕСТ\s+[«\"]?КОНТЕНТ-ЗАВОД",
    "side_stickers": r"article-side-stickers|side-sticker--",
    "generic_signal_cards": r"article-signal-cards|signal-card--important",
    "generic_theme_faq": r"Часто задаваемые вопросы по теме\s*\(FAQ\)",
}

# Theme share row after thematic FAQ — not part of FAQ answer text.
_SHARE_CHROME_SPLIT = (
    r"(?:<!--\s*Share\s+buttons\s*-->|"
    r"<div\b[^>]*\bclass=[\"'][^\"']*\barticle-share\b|"
    r"<aside\b[^>]*\bclass=[\"'][^\"']*\barticle-share\b|"
    r"<section\b[^>]*\bclass=[\"'][^\"']*\barticle-share\b)"
)


def _canonical_article_path(url: str) -> str:
    """Normalize article paths for permalink vs schema JSON-LD (WP /blog/{slug}/ vs /{slug}/)."""
    raw = (url or "").strip()
    if not raw:
        return ""
    path = urlparse(raw).path if "://" in raw else raw
    path = "/" + path.strip("/")
    # Strip optional /blog prefix so schema {{SITE_BASE}}/<slug>/ matches WP permalink.
    if path.startswith("/blog/"):
        path = path[5:]
    return path.rstrip("/") + "/"


def _normalize_live_url(url: str) -> str:
    """Normalize absolute URLs for parity checks (IDNA host + trailing slash)."""
    raw = (url or "").strip()
    if not raw:
        return ""
    if "://" in raw:
        return encode_idna_url(raw.rstrip("/") + "/")
    return raw.rstrip("/") + "/"


def _normalize_faq_plain(text: str) -> str:
    """Match schema_gate FAQ plain-text rules (post-anchor space vs punctuation).

    Also collapse dash variants: WP wptexturize turns ASCII ``--`` in post
    content into an em dash while FAQPage JSON-LD keeps ``--`` (B71).
    """
    plain = html_lib.unescape(re.sub(r"<[^>]+>", " ", str(text)))
    plain = re.sub(r"\s+", " ", plain).strip()
    plain = re.sub(r"\s+([,.;:!?…»\)\]])", r"\1", plain)
    plain = re.sub(r"([«\(\[])\s+", r"\1", plain)
    # Em/en dash and doubled ASCII hyphens → single hyphen for FAQ parity.
    plain = plain.replace("\u2014", "-").replace("\u2013", "-")
    plain = re.sub(r"-{2,}", "-", plain)
    return plain


def _jsonld_types(value: object) -> list[str]:
    types: list[str] = []
    if isinstance(value, dict):
        raw = value.get("@type")
        if isinstance(raw, str):
            types.append(raw)
        elif isinstance(raw, list):
            types.extend(str(item) for item in raw)
        for child in value.values():
            types.extend(_jsonld_types(child))
    elif isinstance(value, list):
        for child in value:
            types.extend(_jsonld_types(child))
    return types


def inspect(
    html: str,
    *,
    expected_slug: str = "",
    expected_title: str = "",
    body_probe: str = "",
    verify_media: bool = False,
    expected_permalink: str = "",
) -> list[str]:
    errors = [
        f"{name} present on live article"
        for name, pattern in FORBIDDEN.items()
        if re.search(pattern, html, flags=re.I)
    ]
    # Align with html_linter.is_faq_section_heading (accepts bare FAQ /
    # «Частые вопросы» / openers). Old regex omitted bare FAQ → live BLOCK
    # after schema/linter PASS (INC-20260722-1248).
    faq_h2_texts = [
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw)).strip()
        for raw in re.findall(
            r"<h2\b[^>]*>\s*(.*?)\s*</h2>",
            html,
            flags=re.IGNORECASE | re.DOTALL,
        )
    ]
    visible_faqs = sum(1 for text in faq_h2_texts if is_faq_section_heading(text))
    if visible_faqs > 1:
        errors.append(f"expected at most one visible FAQ section, found {visible_faqs}")
    jsonld_payloads: list[object] = []
    for raw in re.findall(
        r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
        html,
        flags=re.I | re.S,
    ):
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        jsonld_payloads.append(payload)
    faq_jsonld = sum(_jsonld_types(payload).count("FAQPage") for payload in jsonld_payloads)
    if faq_jsonld != visible_faqs:
        errors.append(
            "FAQPage JSON-LD count must match visible FAQ sections "
            f"(jsonld={faq_jsonld}, visible={visible_faqs})"
        )
    if expected_slug:
        canonical = re.search(
            r"<link\b[^>]*rel=[\"']canonical[\"'][^>]*href=[\"']([^\"']+)",
            html,
            flags=re.I,
        )
        canonical_url = canonical.group(1).rstrip("/") + "/" if canonical else ""
        expected_url = expected_permalink.rstrip("/") + "/" if expected_permalink else ""
        if expected_url and _normalize_live_url(canonical_url) != _normalize_live_url(expected_url):
            errors.append("canonical URL does not exactly match published permalink")
        elif not expected_url and (
            not canonical_url or not canonical_url.rstrip("/").endswith("/" + expected_slug)
        ):
            errors.append("canonical URL does not match published slug")
        posting_urls: list[str] = []
        for payload in jsonld_payloads:
            stack = [payload]
            while stack:
                value = stack.pop()
                if isinstance(value, dict):
                    if value.get("@type") == "BlogPosting":
                        for key in ("url", "@id", "mainEntityOfPage"):
                            field = value.get(key)
                            if isinstance(field, str):
                                posting_urls.append(field)
                            elif isinstance(field, dict):
                                posting_urls.extend(
                                    str(field.get(k) or "") for k in ("@id", "url")
                                )
                    stack.extend(value.values())
                elif isinstance(value, list):
                    stack.extend(value)
        if expected_url:
            norm_expected = _canonical_article_path(_normalize_live_url(expected_url))
            norm_posting = {
                _canonical_article_path(_normalize_live_url(u)) for u in posting_urls if u
            }
            norm_posting_raw = {_normalize_live_url(u) for u in posting_urls if u}
            if (
                norm_expected not in norm_posting
                and _normalize_live_url(expected_url) not in norm_posting_raw
            ):
                errors.append("live BlogPosting JSON-LD URL does not exactly match permalink")
        elif not expected_url and not any(
            url.rstrip("/").endswith("/" + expected_slug) for url in posting_urls
        ):
            errors.append("live BlogPosting JSON-LD URL does not match published slug")
    if expected_title:
        title = re.search(r"<title\b[^>]*>(.*?)</title>", html, flags=re.I | re.S)
        title_text = html_lib.unescape(title.group(1)) if title else ""
        if expected_title not in title_text:
            errors.append("live <title> does not contain expected article title")
    if body_probe:
        plain = html_lib.unescape(re.sub(r"<[^>]+>", " ", html))
        plain = re.sub(r"\s+", " ", plain)
        probe = re.sub(r"\s+", " ", body_probe).strip()
        if probe and probe not in plain:
            errors.append("expected article body probe not found on live page")
    entry = re.search(
        r"<div\b[^>]*id=[\"']article-content[\"'][^>]*>(.*?)</div>",
        html,
        flags=re.I | re.S,
    )
    if not entry:
        errors.append("article-content container missing")
    else:
        article_image_tags = re.findall(r"<img\b[^>]*>", entry.group(1), flags=re.I)
        for tag in article_image_tags:
            alt = re.search(r"\balt=[\"']([^\"']*)", tag, flags=re.I)
            if not alt or not alt.group(1).strip():
                errors.append("article image has empty/missing alt")
                break
            src = re.search(r"\bsrc=[\"']([^\"']+)", tag, flags=re.I)
            if src:
                src_val = src.group(1).strip()
                if src_val.startswith("cover/") or src_val.startswith("./cover/"):
                    errors.append(f"relative cover image src on live page: {src_val}")
                elif verify_media and src_val.startswith(("http://", "https://")):
                    try:
                        request = urllib.request.Request(
                            encode_idna_url(src_val),
                            headers={"User-Agent": "ExcaliburBlogLiveGate/1.0"},
                            method="HEAD",
                        )
                        with urllib.request.urlopen(request, timeout=15) as response:
                            if int(response.status) >= 400:
                                errors.append(f"article image unavailable: {src_val}")
                    except Exception:
                        errors.append(f"article image unavailable: {src_val}")

    featured = re.search(
        r"<div\b[^>]*class=[\"'][^\"']*post-thumbnail[^\"']*[\"'][^>]*>(.*?)</div>",
        html,
        flags=re.I | re.S,
    )
    if not featured:
        errors.append("featured image container missing")
    else:
        image = re.search(r"<img\b[^>]*>", featured.group(1), flags=re.I)
        alt = re.search(r"\balt=[\"']([^\"']*)", image.group(0), flags=re.I) if image else None
        src = re.search(r"\bsrc=[\"']([^\"']+)", image.group(0), flags=re.I) if image else None
        if not image or not alt or not alt.group(1).strip():
            errors.append("featured image has empty/missing alt")
        if verify_media and src and src.group(1).startswith(("http://", "https://")):
            try:
                request = urllib.request.Request(
                    encode_idna_url(src.group(1)),
                    headers={"User-Agent": "ExcaliburBlogLiveGate/1.0"},
                    method="HEAD",
                )
                with urllib.request.urlopen(request, timeout=15) as response:
                    if int(response.status) >= 400:
                        errors.append("featured image unavailable")
            except Exception:
                errors.append("featured image unavailable")

    visible_pairs: list[tuple[str, str]] = []
    faq_bodies = extract_thematic_faq_bodies(html)
    if faq_bodies:
        # Theme chrome (share row) often sits after the last FAQ answer but
        # before the next H2 / </article>; do not treat it as FAQ answer text.
        faq_body = re.split(
            _SHARE_CHROME_SPLIT,
            faq_bodies[0],
            maxsplit=1,
            flags=re.I,
        )[0]
        for chunk in re.split(r"(?=<h3\b)", faq_body, flags=re.I):
            question = re.search(r"<h3\b[^>]*>(.*?)</h3>", chunk, flags=re.I | re.S)
            if question:
                # First <p> only — ignore trailing CTA/interlink siblings
                # (INC-20260726-1615).
                answer_html = extract_faq_answer_after_h3(chunk[question.end() :])
                visible_pairs.append(
                    (
                        _normalize_faq_plain(question.group(1)),
                        _normalize_faq_plain(answer_html),
                    )
                )
    schema_pairs: list[tuple[str, str]] = []
    for payload in jsonld_payloads:
        stack = [payload]
        while stack:
            value = stack.pop()
            if isinstance(value, dict):
                if value.get("@type") == "FAQPage":
                    for question in value.get("mainEntity") or []:
                        if isinstance(question, dict):
                            answer = question.get("acceptedAnswer")
                            answer_text = (
                                answer.get("text") if isinstance(answer, dict) else ""
                            )
                            schema_pairs.append(
                                (
                                    _normalize_faq_plain(str(question.get("name") or "")),
                                    _normalize_faq_plain(str(answer_text or "")),
                                )
                            )
                stack.extend(value.values())
            elif isinstance(value, list):
                stack.extend(value)
    if schema_pairs != visible_pairs:
        errors.append("live FAQPage question/answer pairs differ from visible thematic FAQ")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--permalink", required=True)
    parser.add_argument("--expected-slug", default="")
    parser.add_argument("--expected-title", default="")
    parser.add_argument("--body-probe", default="")
    parser.add_argument("-o", "--output", default="")
    parser.add_argument("--html-file", default="", help="Offline fixture instead of HTTP")
    args = parser.parse_args()
    if args.html_file:
        html = Path(args.html_file).read_text(encoding="utf-8")
    else:
        request = urllib.request.Request(
            encode_idna_url(args.permalink),
            headers={"User-Agent": "ExcaliburBlogLiveGate/1.0"},
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            html = response.read().decode("utf-8", errors="replace")
    errors = inspect(
        html,
        expected_slug=args.expected_slug,
        expected_title=args.expected_title,
        body_probe=args.body_probe,
        verify_media=not bool(args.html_file),
        expected_permalink=args.permalink,
    )
    report = {
        "gate": "live-page",
        "status": "PASS" if not errors else "BLOCK",
        "permalink": args.permalink,
        "errors": errors,
    }
    if args.output:
        Path(args.output).write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
