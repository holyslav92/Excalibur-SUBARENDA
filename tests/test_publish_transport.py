"""Tests for FTP/SFTP publish transport selection."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_remote_transport import (  # noqa: E402
    effective_publish_transport,
    is_cursor_cloud_agent,
    remote_path,
    resolve_publish_transport,
    upload_text_file,
)
from excalibur_blog_wp_publish import publish_env_check_report  # noqa: E402


class PublishTransportTest(unittest.TestCase):
    def test_resolve_ftp_by_port(self) -> None:
        env = {"FTP_PORT": "21"}
        self.assertEqual(resolve_publish_transport(env), "ftp")

    def test_resolve_sftp_default(self) -> None:
        env = {"FTP_PORT": "22"}
        self.assertEqual(resolve_publish_transport(env), "sftp")

    def test_resolve_ftp_explicit(self) -> None:
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "22"}
        self.assertEqual(resolve_publish_transport(env), "ftp")

    def test_remote_path_with_root(self) -> None:
        env = {"FTP_ROOT": "[REDACTED]"}
        self.assertEqual(
            remote_path(env, "excalibur-blog-publish-once.php"),
            "[REDACTED]/excalibur-blog-publish-once.php",
        )

    def test_env_check_report_ftp_mode(self) -> None:
        env = {
            "FTP_HOST": "188.225.40.162",
            "FTP_USER": "ca21576_svyat",
            "FTP_PASS": "secret",
            "FTP_PORT": "21",
            "FTP_TRANSPORT": "ftp",
            "FTP_ROOT": "[REDACTED]",
            "PUBLIC_SITE_URL": "https://example.com",
            "EXCALIBUR_BLOG_ALLOW_PUBLISH": "no",
        }
        with patch.dict("os.environ", {"CURSOR_AGENT": ""}, clear=False):
            report = publish_env_check_report(env)
        transport = report["transport"]
        assert isinstance(transport, dict)
        self.assertEqual(transport["configured_mode"], "ftp")
        self.assertEqual(transport["mode"], "ftp")
        self.assertFalse(report["allow_publish"])
        self.assertEqual(transport["port"], "21")
        self.assertEqual(transport["pasv_rewrite_ip"], "188.225.40.162")

    def test_effective_transport_cloud_agent_overrides_ftp(self) -> None:
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "21"}
        with patch.dict("os.environ", {"CURSOR_AGENT": "1"}, clear=False):
            self.assertEqual(resolve_publish_transport(env), "ftp")
            self.assertEqual(effective_publish_transport(env), "sftp")
            self.assertTrue(is_cursor_cloud_agent())

    @patch("excalibur_blog_remote_transport._upload_text_ftp")
    def test_upload_dispatches_ftp(self, mock_ftp: MagicMock) -> None:
        mock_ftp.return_value = "[REDACTED]/test.php"
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "21"}
        with patch.dict("os.environ", {"CURSOR_AGENT": ""}, clear=False):
            path = upload_text_file(env, "test.php", b"<?php")
        self.assertEqual(path, "[REDACTED]/test.php")
        mock_ftp.assert_called_once()

    @patch("excalibur_blog_wp_publish.upload_bootstrap_sftp")
    @patch("excalibur_blog_remote_transport._upload_text_ftp")
    def test_upload_llms_uses_sftp_on_cloud_agent(
        self, mock_ftp: MagicMock, mock_sftp: MagicMock
    ) -> None:
        mock_sftp.return_value = "[REDACTED]/llms.txt"
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "21"}
        with patch.dict("os.environ", {"CURSOR_AGENT": "1"}, clear=False):
            path = upload_text_file(env, "llms.txt", b"# llms")
        self.assertEqual(path, "[REDACTED]/llms.txt")
        mock_ftp.assert_not_called()
        mock_sftp.assert_called_once()


if __name__ == "__main__":
    unittest.main()
