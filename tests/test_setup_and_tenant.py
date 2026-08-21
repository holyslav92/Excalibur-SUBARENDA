"""Excalibur-SUBARENDA setup/tenant contracts (Добрый дом)."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NON_WRITER_TEXT_ROLES = (
    "scout",
    "title",
    "sol",
    "research",
    "description",
    "cover-text",
    "schema",
    "cover-scene",
)


class SetupTenantTests(unittest.TestCase):
    def test_setup_status_complete_after_tenant_fill(self) -> None:
        status = json.loads((ROOT / "memory/setup/status.json").read_text(encoding="utf-8"))
        self.assertTrue(status.get("complete"))
        for phase in ("cloud", "site", "author", "voice", "scout"):
            self.assertEqual(status.get("phases", {}).get(phase), "done", phase)
        # visual/cta may be need_replace/todo after fork from Excalibur-2-Cloud
        visual = status.get("phases", {}).get("visual")
        self.assertIn(visual, ("done", "need_replace"), visual)

    def test_tenant_config_dobry_dom(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        self.assertTrue(tenant.get("setup_complete"))
        self.assertEqual(tenant.get("brand_name"), "Добрый дом")
        self.assertEqual(tenant.get("author_id"), "dobry-dom")
        self.assertEqual(tenant.get("topic_focus_profile"), "short_term_rental")
        self.assertIn(tenant.get("cover_mode"), {"brand_logo_paste", "logo_lockup"})
        hints = tenant.get("publish_transport_hints") or {}
        self.assertEqual(hints.get("transport"), "ftp")
        self.assertEqual(hints.get("ftp_root"), "sublease/public_html")
        schedule = tenant.get("publish_schedule") or {}
        self.assertEqual(schedule.get("slots_local"), ["10:00", "13:00", "17:00"])
        self.assertEqual(schedule.get("runs_per_day"), 3)
        self.assertEqual(schedule.get("timezone"), "Asia/Yekaterinburg")
        self.assertTrue(tenant.get("cta_required"))
        links = tenant.get("cta_links") or []
        self.assertTrue(any("blog" in x for x in links))
        self.assertFalse(any("tymenrieltor" in x for x in links))
        self.assertFalse(any("Tyumen_Rieltor" in x for x in links))
        self.assertTrue(tenant.get("interlink_old_articles"))
        self.assertTrue(tenant.get("wp_categories_required"))
        writing = tenant.get("writing_model") or {}
        powerful = writing.get("powerful") or {}
        utility = writing.get("utility") or {}
        self.assertEqual(powerful.get("model"), "claude-opus-5")
        self.assertEqual(utility.get("model"), "gpt-5.6-terra")
        self.assertEqual(set(powerful.get("roles") or []), {"writer"})
        self.assertTrue(set(NON_WRITER_TEXT_ROLES).issubset(set(utility.get("roles") or [])))
        self.assertEqual(writing.get("canon_note"), "Opus 5 = Writer only; everything else Terra")
        self.assertTrue(writing.get("fail_loud_if_unavailable"))

    def test_setup_agents_present(self) -> None:
        for rel in (
            "agents/excalibur-blog-setup.md",
            "agents/excalibur-blog-setup-voice.md",
            "agents/excalibur-blog-setup-visual.md",
            "skills/setup-excalibur-blog/SKILL.md",
            ".cursor/agents/excalibur-blog-setup.md",
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_automation_config_present(self) -> None:
        automation = ROOT / ".cursor/automations/dobry-dom-3x.yml"
        self.assertTrue(automation.is_file(), str(automation))
        text = automation.read_text(encoding="utf-8")
        self.assertIn("Добрый дом 3 статьи", text)
        self.assertIn("holyslav92/Excalibur-SUBARENDA", text)
        self.assertIn("0 10,13,17 * * 1-5", text)
        self.assertIn("memories: false", text)
        self.assertIn("wordpress_*", text)
        self.assertNotIn("FTP_PASS:", text.replace("# FTP_PASS", ""))  # no committed password value

    def test_tenant_files_filled_no_setup_required(self) -> None:
        for rel in (
            "shared/SOUL.md",
            "shared/article-style.md",
            "memory/brief/site-brief.md",
            "memory/cover/blog-hero.json",
            "shared/authors-registry.json",
        ):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("SETUP_REQUIRED", text, rel)

    def test_cta_gate_requires_tenant_links(self) -> None:
        import shutil
        import subprocess
        import tempfile

        article_dir = ROOT / "memory/blog/articles/_cta_gate_fixture"
        if article_dir.exists():
            shutil.rmtree(article_dir)
        article_dir.mkdir(parents=True, exist_ok=True)
        try:
            (article_dir / "article.html").write_text(
                '<p>Читайте <a href="https://xn---72-9cdob8azaodt6k.xn--p1ai/blog/">блог</a> и '
                '<a href="https://xn---72-9cdob8azaodt6k.xn--p1ai/">сайт Добрый дом</a>.</p>\n',
                encoding="utf-8",
            )
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_community_cta_gate.py"),
                    "--article-dir",
                    str(article_dir.relative_to(ROOT)),
                    "--root",
                    str(ROOT),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((article_dir / "community-cta-gate.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "PASS")
        finally:
            shutil.rmtree(article_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
