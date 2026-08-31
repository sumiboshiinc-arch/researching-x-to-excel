import json
import re
import sys
from datetime import datetime
from pathlib import Path

POST_URL = re.compile(r"^https://x\.com/[A-Za-z0-9_]{1,15}/status/(\d+)$")


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_payload(payload: dict) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    threshold = payload.get("brief", {}).get("view_threshold", {})
    operator = threshold.get("operator")
    limit = threshold.get("value")
    if operator not in {"gt", "gte"} or isinstance(limit, bool) or not isinstance(limit, (int, float)):
        errors.append({"code": "invalid_threshold", "message": "view_threshold requires operator gt/gte and a numeric value"})
        return errors

    seen: set[str] = set()
    previous: datetime | None = None
    for index, row in enumerate(payload.get("records", [])):
        post_id = str(row.get("post_id", ""))
        if post_id in seen:
            errors.append({"code": "duplicate_post_id", "message": f"row {index}: duplicate {post_id}"})
        seen.add(post_id)

        match = POST_URL.match(str(row.get("post_url", "")))
        if not match or match.group(1) != post_id:
            errors.append({"code": "invalid_post_url", "message": f"row {index}: post URL does not match post ID"})
        if not str(row.get("creator_url", "")).startswith("https://x.com/"):
            errors.append({"code": "missing_creator_url", "message": f"row {index}: valid creator URL required"})

        if row.get("verification_state") != "verified":
            errors.append({"code": "unverified_views", "message": f"row {index}: verification_state must be verified"})

        views = row.get("views")
        if isinstance(views, bool) or not isinstance(views, (int, float)):
            errors.append({"code": "invalid_views", "message": f"row {index}: views must be numeric"})
            qualifies = False
        else:
            qualifies = views > limit if operator == "gt" else views >= limit
        if not qualifies:
            errors.append({"code": "view_threshold", "message": f"row {index}: views do not satisfy {operator} {limit}"})

        try:
            published = datetime.fromisoformat(str(row.get("published_at", "")).replace("Z", "+00:00"))
        except ValueError:
            errors.append({"code": "invalid_timestamp", "message": f"row {index}: invalid published_at"})
            continue
        if previous is not None and published > previous:
            errors.append({"code": "sort_order", "message": f"row {index}: records are not newest first"})
        previous = published
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(json.dumps({"ok": False, "errors": [{"code": "usage", "message": "provide one JSON path"}]}))
        return 2
    errors = validate_payload(load_payload(Path(argv[1])))
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
