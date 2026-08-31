import json
import subprocess
import sys
import unittest
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_records.py"
FIXTURES = ROOT / "tests" / "fixtures"


class ValidateRecordsTest(unittest.TestCase):
    @staticmethod
    def brief(operator="gt", value=0):
        return {"qualification_operator": operator, "qualification_value": value, "date_start": "2026-08-01T00:00:00Z", "date_end": "2026-08-31T23:59:59Z"}

    def run_validator(self, name: str):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / name)],
            text=True, capture_output=True, check=False,
        )

    def run_payload(self, payload, *args):
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as stream:
            json.dump(payload, stream, allow_nan=True); stream.flush()
            return subprocess.run([sys.executable, str(SCRIPT), stream.name, *args], text=True, capture_output=True, check=False)

    def test_valid_records_pass(self):
        result = self.run_validator("valid_records.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"ok": True, "errors": []})

    def test_complete_flat_research_brief_passes(self):
        result = self.run_validator("valid_records.json")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_invalid_records_report_required_failures(self):
        result = self.run_validator("invalid_records.json")
        self.assertEqual(result.returncode, 1)
        codes = {item["code"] for item in json.loads(result.stdout)["errors"]}
        required = {"duplicate_post_id", "view_threshold", "invalid_post_url", "missing_creator_url", "sort_order", "unverified_views"}
        self.assertTrue(required.issubset(codes))

    def test_unverified_views_fail_validation(self):
        result = self.run_validator("invalid_records.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("unverified_views", {item["code"] for item in json.loads(result.stdout)["errors"]})

    def test_boolean_threshold_is_rejected(self):
        result = self.run_validator("boolean_threshold.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid_threshold", {item["code"] for item in json.loads(result.stdout)["errors"]})

    def test_boolean_views_are_rejected(self):
        result = self.run_validator("boolean_views.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid_views", {item["code"] for item in json.loads(result.stdout)["errors"]})

    def test_gt_rejects_views_exactly_at_threshold(self):
        result = self.run_validator("exact_gt_threshold.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("view_threshold", {item["code"] for item in json.loads(result.stdout)["errors"]})

    def test_gte_accepts_views_exactly_at_threshold(self):
        result = self.run_validator("exact_gte_threshold.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"ok": True, "errors": []})

    def test_adversarial_shapes_nonfinite_urls_and_timestamps(self):
        for payload, code in (("bad", "invalid_payload"), ({"brief": {}, "records": {}}, "invalid_records"), ({"brief": [], "records": []}, "invalid_brief")):
            result = self.run_payload(payload)
            self.assertIn(code, {e["code"] for e in json.loads(result.stdout)["errors"]})
        payload = {"brief": self.brief(), "records": [{"post_id": "2", "post_url": "https://x.com/a/status/2", "creator_url": "https://x.com/", "published_at": "2026-08-01T00:00:00", "views": float("inf"), "likes": float("nan"), "verification_state": "verified"}]}
        codes = {e["code"] for e in json.loads(self.run_payload(payload).stdout)["errors"]}
        self.assertTrue({"missing_creator_url", "invalid_timestamp", "invalid_views", "invalid_metric"}.issubset(codes))

    def test_exact_window_and_equal_time_id_order(self):
        brief = self.brief("gte", 1)
        brief["date_end"] = "2026-08-02T00:00:00+00:00"
        def row(pid, stamp): return {"post_id": pid, "post_url": f"https://x.com/a/status/{pid}", "creator_url": "https://x.com/a", "published_at": stamp, "views": 1, "verification_state": "verified"}
        self.assertEqual(self.run_payload({"brief": brief, "records": [row("3", brief["date_end"]), row("2", brief["date_start"])]}).returncode, 0)
        bad = {"brief": brief, "records": [row("2", "2026-08-01T12:00:00Z"), row("3", "2026-08-01T12:00:00Z"), row("1", "2026-07-31T23:59:59Z")]}
        codes = {e["code"] for e in json.loads(self.run_payload(bad).stdout)["errors"]}
        self.assertTrue({"sort_order", "date_window"}.issubset(codes))

    def test_list_input_uses_explicit_cli_brief(self):
        row = {"post_id": "1", "post_url": "https://x.com/a/status/1", "creator_url": "https://x.com/a", "published_at": "2026-08-01T00:00:00Z", "views": 2, "verification_state": "verified"}
        self.assertEqual(self.run_payload([row], "--operator", "gt", "--value", "1").returncode, 0)

    def test_object_envelope_requires_both_date_bounds(self):
        for missing in ("date_start", "date_end"):
            brief = self.brief(); del brief[missing]
            result = self.run_payload({"brief": brief, "records": []})
            self.assertIn("invalid_date_window", {e["code"] for e in json.loads(result.stdout)["errors"]})

    def test_huge_json_integer_never_crashes(self):
        huge = 10 ** 400
        row = {"post_id": "1", "post_url": "https://x.com/a/status/1", "creator_url": "https://x.com/a", "published_at": "2026-08-01T00:00:00Z", "views": huge, "likes": huge, "verification_state": "verified"}
        result = self.run_payload({"brief": self.brief("gt", huge - 1), "records": [row]})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"ok": True, "errors": []})

    def test_nested_threshold_remains_documented_legacy_alias(self):
        brief = {"view_threshold": {"operator": "gt", "value": 0}, "date_start": "2026-08-01T00:00:00Z", "date_end": "2026-08-31T23:59:59Z"}
        self.assertEqual(self.run_payload({"brief": brief, "records": []}).returncode, 0)

    def test_malformed_json_is_stable_json_error(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json") as stream:
            stream.write("{"); stream.flush(); result = subprocess.run([sys.executable, str(SCRIPT), stream.name], text=True, capture_output=True, check=False)
        self.assertEqual(json.loads(result.stdout)["errors"][0]["code"], "invalid_input")


if __name__ == "__main__":
    unittest.main()
