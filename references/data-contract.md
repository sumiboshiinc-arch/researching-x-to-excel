# Data contract

Use `ResearchBrief` before collecting:

```text
topic, purpose, seed_terms, seed_accounts, exclusions, locale, languages,
public_only, date_start, date_end, timezone, qualification_metric,
qualification_operator, qualification_value, target_count, cap, sort_rule,
accepted_post_types, required_evidence, required_metrics, output_language,
preset, workbook_mode, existing_workbook_path, monitoring_authorized
```

`workbook_mode` is `new` or `incremental`. `monitoring_authorized` is false unless explicit authorization supplies cadence, scope, destination, and notifications.

Authorized monitoring also records `prior_observation_at` or `initial_lookback`, workbook path, unchanged qualification rule, sheets to update, `dedupe_key=post_id`, formula/filter/link/chart/dashboard QA, and a zero-new-results report. It never silently broadens scope or thresholds.

The validator prefers the `{ "brief": ..., "records": [...] }` envelope. Envelopes use flat `qualification_operator` and `qualification_value` and require timezone-aware `date_start` and `date_end`. A nested `view_threshold: {operator, value}` is accepted only as a legacy envelope alias. For legacy root arrays, pass `--operator` and `--value` plus optional date bounds; implicit qualification defaults are forbidden.

Each `PostRecord` has these required fields:

```text
post_id, post_url, published_at, timezone, views, likes, reposts,
replies, quotes, bookmarks, original_text, creator_name, handle,
creator_url, post_type, relevance_tier, stance, disclosure, summary,
relevance_evidence, source_post_id, source_post_url, discovery_lane,
verification_state, observed_at
```

Keep candidates, verified records, and exclusions distinct. A candidate becomes formal only after its required source facts are verified. `verification_state` should make the distinction explicit, for example `candidate`, `verified`, `missing_required_view`, `restricted`, or `deleted`.

Use `post_id` as the identity key. When observations for one ID disagree, prefer the newest *verified* observation by `observed_at`; retain an older value only when the newer observation lacks that field. Never merge a candidate value over a verified value or conceal a conflict. Sort formal records by `published_at` descending, then `post_id` descending.

Interpret comparison operators literally: `gt` is strictly greater than the value; `gte` includes the value. Store finite metrics as numbers, not display strings. Timestamps are timezone-aware ISO 8601 and date-window bounds are inclusive. Creator URLs are strict profile URLs, not the X root. Sort equal timestamps by numeric `post_id` descending. Preserve `original_text` exactly; normalized names and analysis belong elsewhere.

```json
{
  "post_id": "1890000000000000001",
  "post_url": "https://x.com/sample/status/1890000000000000001",
  "published_at": "2026-08-12T09:15:00+09:00",
  "timezone": "Asia/Tokyo",
  "views": 5001,
  "likes": 124,
  "reposts": 12,
  "replies": 8,
  "quotes": 3,
  "bookmarks": null,
  "original_text": "サンプルを使ってみた。",
  "creator_name": "山田 花",
  "handle": "sample_user",
  "creator_url": "https://x.com/sample_user",
  "post_type": "original",
  "relevance_tier": "high",
  "stance": "positive",
  "disclosure": "none_observed",
  "summary": "使用感の投稿",
  "relevance_evidence": "商品名と使用感を明示",
  "source_post_id": null,
  "source_post_url": null,
  "discovery_lane": "benefit",
  "verification_state": "verified",
  "observed_at": "2026-08-31T10:00:00+09:00"
}
```
