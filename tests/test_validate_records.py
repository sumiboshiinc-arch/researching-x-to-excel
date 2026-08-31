import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_records.py"
FIXTURES = ROOT / "tests" / "fixtures"


class ValidateRecordsTest(unittest.TestCase):
    def run_validator(self, name: str):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / name)],
            text=True, capture_output=True, check=False,
        )

    def test_valid_records_pass(self):
        result = self.run_validator("valid_records.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"ok": True, "errors": []})

    def test_invalid_records_report_required_failures(self):
        result = self.run_validator("invalid_records.json")
        self.assertEqual(result.returncode, 1)
        codes = {item["code"] for item in json.loads(result.stdout)["errors"]}
        required = {"duplicate_post_id", "view_threshold", "invalid_post_url", "missing_creator_url", "sort_order"}
        self.assertTrue(required.issubset(codes))


if __name__ == "__main__":
    unittest.main()
