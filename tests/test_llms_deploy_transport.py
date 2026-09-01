"""llms deploy must respect FTP_TRANSPORT (SFTP on Cloud Agent)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_llms_deploy import deploy_llms_files  # noqa: E402


class LlmsDeployTransportTest(unittest.TestCase):
    def setUp(self) -> None:
        self.llms = ROOT / "memory" / "blog" / "llms.txt"
        self.full = ROOT / "memory" / "blog" / "llms-full.txt"
        if not self.llms.is_file() or not self.full.is_file():
            self.skipTest("llms files missing")

    @patch("excalibur_blog_llms_deploy.upload_text_file")
    def test_deploy_uses_upload_text_file_not_raw_ftp(self, mock_upload: MagicMock) -> None:
        mock_upload.return_value = "llms.txt"
        env = {
            "FTP_HOST": "example.com",
            "FTP_USER": "user",
            "FTP_PASS": "pass",
            "FTP_TRANSPORT": "sftp",
            "FTP_PORT": "22",
            "FTP_ROOT": ".",
            "PUBLIC_SITE_URL": "https://example.com",
        }
        report = deploy_llms_files(ROOT, env, "https://example.com")
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["transport"], "sftp")
        self.assertEqual(mock_upload.call_count, 2)
        names = [call.args[1] for call in mock_upload.call_args_list]
        self.assertEqual(names, ["llms.txt", "llms-full.txt"])


if __name__ == "__main__":
    unittest.main()
