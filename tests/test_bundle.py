import json
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "scripts"))
from validate_bundle import validate_bundle


RECORD = {
    "record_id": "nt-example",
    "canonical_url": "https://developer.ninjatrader.com/docs/desktop/example",
    "title": "Example",
    "focused_track": "indicator-coding",
    "reference_version": "NinjaTrader 8.1.8.2",
    "classification": "ambiguous",
}


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.package = Path(self.temp.name)
        (self.package / "references").mkdir()
        (self.package / "SKILL.md").write_text(
            "---\nname: example\ndescription: A valid package\n---\n\n[Reference](references/example.md)\n",
            encoding="utf-8",
        )
        (self.package / "references/example.md").write_text("# Reference\n", encoding="utf-8")
        (self.package / "references/source-index.jsonl").write_text(
            json.dumps(RECORD) + "\n", encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def assertInvalid(self, text, expected):
        if text:
            (self.package / "references/negative.md").write_text(text, encoding="utf-8")
        self.assertTrue(any(expected in error for error in validate_bundle(self.package)), expected)

    def test_clean_package(self):
        self.assertEqual(validate_bundle(self.package), [])

    def test_rejects_absolute_path(self):
        self.assertInvalid("/home/user/file", "/home/")

    def test_rejects_email(self):
        self.assertInvalid("owner@example.com", "email address")

    def test_rejects_credential_like_value(self):
        self.assertInvalid("token: abc123", "credential-like value")

    def test_rejects_private_url(self):
        self.assertInvalid("https://localhost:8000/private", "private URL")

    def test_rejects_stale_typo(self):
        self.assertInvalid("ninjascipt", "ninjascipt")

    def test_rejects_malformed_jsonl(self):
        (self.package / "references/source-index.jsonl").write_text("{not json}\n", encoding="utf-8")
        self.assertInvalid("{not json}", "malformed JSONL")

    def test_rejects_missing_file(self):
        (self.package / "SKILL.md").unlink()
        self.assertInvalid("", "missing required public file")

    def test_rejects_escaping_link(self):
        (self.package / "SKILL.md").write_text(
            "---\nname: example\ndescription: valid\n---\n\n[escape](../../../secret.md)\n",
            encoding="utf-8",
        )
        self.assertInvalid("", "escapes package")


if __name__ == "__main__":
    unittest.main()
