#!/usr/bin/env python3
"""Validate normalized X records and emit only stable JSON results."""
from __future__ import annotations
import argparse, json, math, re, sys
from datetime import datetime
from pathlib import Path
from typing import Any

POST_URL = re.compile(r"^https://x\.com/[A-Za-z0-9_]{1,15}/status/(\d+)$")
CREATOR_URL = re.compile(r"^https://x\.com/[A-Za-z0-9_]{1,15}/?$")

def err(code: str, message: str) -> dict[str, str]: return {"code": code, "message": message}
def finite(value: Any) -> bool:
    if isinstance(value, bool): return False
    if isinstance(value, int): return True
    return isinstance(value, float) and math.isfinite(value)
def aware(value: Any) -> datetime | None:
    if not isinstance(value, str): return None
    try: parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, OverflowError): return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None

def validate_payload(payload: Any, override: dict[str, Any] | None = None) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    envelope = isinstance(payload, dict)
    if isinstance(payload, list): records, brief = payload, override or {}
    elif isinstance(payload, dict):
        records, brief = payload.get("records"), payload.get("brief")
        if not isinstance(brief, dict): errors.append(err("invalid_brief", "brief must be an object")); brief = {}
    else: return [err("invalid_payload", "payload must be an object or a records array")]
    if not isinstance(records, list): return errors + [err("invalid_records", "records must be an array")]
    if "qualification_operator" in brief or "qualification_value" in brief:
        operator, limit = brief.get("qualification_operator"), brief.get("qualification_value")
    else:
        threshold = brief.get("view_threshold", {})
        if not isinstance(threshold, dict): return errors + [err("invalid_threshold", "legacy view_threshold must be an object")]
        operator, limit = threshold.get("operator"), threshold.get("value")
    if operator not in {"gt", "gte"} or not finite(limit): return errors + [err("invalid_threshold", "qualification_operator must be gt/gte and qualification_value must be finite numeric")]
    start = aware(brief.get("date_start")) if "date_start" in brief else None
    end = aware(brief.get("date_end")) if "date_end" in brief else None
    if (envelope or "date_start" in brief) and start is None: errors.append(err("invalid_date_window", "date_start is required and must be timezone-aware ISO 8601"))
    if (envelope or "date_end" in brief) and end is None: errors.append(err("invalid_date_window", "date_end is required and must be timezone-aware ISO 8601"))
    if start and end and start > end: errors.append(err("invalid_date_window", "date_start must not be after date_end"))
    seen: set[str] = set(); previous: tuple[datetime, int] | None = None
    for index, row in enumerate(records):
        if not isinstance(row, dict): errors.append(err("invalid_record", f"row {index}: record must be an object")); continue
        post_id = row.get("post_id")
        if not isinstance(post_id, str) or not post_id.isdigit(): errors.append(err("invalid_post_id", f"row {index}: post_id must be a digit string")); post_id = ""
        if post_id in seen: errors.append(err("duplicate_post_id", f"row {index}: duplicate {post_id}"))
        seen.add(post_id)
        match = POST_URL.fullmatch(str(row.get("post_url", "")))
        if not match or match.group(1) != post_id: errors.append(err("invalid_post_url", f"row {index}: post URL does not match post ID"))
        if not CREATOR_URL.fullmatch(str(row.get("creator_url", ""))): errors.append(err("missing_creator_url", f"row {index}: strict X creator profile URL required"))
        if row.get("verification_state") != "verified": errors.append(err("unverified_views", f"row {index}: verification_state must be verified"))
        views = row.get("views")
        if not finite(views): errors.append(err("invalid_views", f"row {index}: views must be finite numeric"))
        elif not (views > limit if operator == "gt" else views >= limit): errors.append(err("view_threshold", f"row {index}: views do not satisfy {operator} {limit}"))
        for field in ("likes", "reposts", "replies", "quotes", "bookmarks"):
            if field in row and row[field] is not None and not finite(row[field]): errors.append(err("invalid_metric", f"row {index}: {field} must be finite numeric or null"))
        published = aware(row.get("published_at"))
        if published is None: errors.append(err("invalid_timestamp", f"row {index}: published_at must be timezone-aware ISO 8601")); continue
        if (start is not None and published < start) or (end is not None and published > end): errors.append(err("date_window", f"row {index}: published_at is outside the inclusive date window"))
        current = (published, int(post_id)) if post_id else None
        if previous is not None and current is not None and current > previous: errors.append(err("sort_order", f"row {index}: records must sort by published_at then post_id descending"))
        if current is not None: previous = current
    return errors

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(add_help=False); parser.add_argument("path"); parser.add_argument("--operator", choices=("gt", "gte")); parser.add_argument("--value", type=float); parser.add_argument("--date-start"); parser.add_argument("--date-end")
    try:
        args = parser.parse_args(argv[1:]); payload = json.loads(Path(args.path).read_text(encoding="utf-8")); override = None
        if isinstance(payload, list):
            if args.operator is None or args.value is None: raise ValueError("records-array input requires --operator and --value")
            override = {"qualification_operator": args.operator, "qualification_value": args.value}
            if args.date_start is not None: override["date_start"] = args.date_start
            if args.date_end is not None: override["date_end"] = args.date_end
        errors = validate_payload(payload, override); print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, allow_nan=False)); return 1 if errors else 0
    except SystemExit:
        print(json.dumps({"ok": False, "errors": [err("usage", "provide a JSON path; arrays also require --operator and --value")]})); return 2
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"ok": False, "errors": [err("invalid_input", str(exc))]}, ensure_ascii=False)); return 2

if __name__ == "__main__": raise SystemExit(main(sys.argv))
