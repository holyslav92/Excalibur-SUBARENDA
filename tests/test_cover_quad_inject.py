#!/usr/bin/env python3
"""Regression tests for inline figure inject (INC B16 phantom h2_anchor)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_cover_quad_split import (  # noqa: E402
    _positional_h2_anchor,
    inject_figures,
)


B16_H2S = [
    "Не отмена рейса, а пустое обещание",
    "Один вопрос до перевода",
    "Когда четвёртый день уже наступил",
    "Мой вывод как практика",
]

B16_ARTICLE_SNIPPET = """\
<p>Lead.</p>
<h2>Не отмена рейса, а пустое обещание</h2>
<p>First paragraph in section one.</p>
<p>Second paragraph in section one.</p>
<h2>Один вопрос до перевода</h2>
<p>Section two opener.</p>
"""


class CoverQuadInjectTests(unittest.TestCase):
    def test_positional_h2_anchor_maps_inline_2_to_first_section(self) -> None:
        anchor = _positional_h2_anchor("inline_2", B16_H2S)
        self.assertIsNotNone(anchor)
        h2, para_offset = anchor
        self.assertEqual(h2, B16_H2S[0])
        self.assertEqual(para_offset, 1)

    def test_inject_figures_uses_positional_fallback_for_phantom_anchor(self) -> None:
        article_path = Path(self._testMethodName) / "article.html"
        article_path.parent.mkdir(parents=True, exist_ok=True)
        article_path.write_text(B16_ARTICLE_SNIPPET, encoding="utf-8")
        outputs = {
            "inline_2": {
                "file": "cover/inline-02.png",
                "alt": "Переписка с обещанием вернуть деньги за три дня.",
                "h2_anchor": "Вежливый ответ без даты",
            }
        }
        log = inject_figures(article_path, outputs, ("inline_2",), dry_run=False)
        html = article_path.read_text(encoding="utf-8")
        self.assertIn('data-slot="inline_2"', html)
        self.assertTrue(any("positional after H2" in line for line in log))
        self.assertIn("cover/inline-02.png", html)
        article_path.unlink()
        article_path.parent.rmdir()


if __name__ == "__main__":
    unittest.main()
