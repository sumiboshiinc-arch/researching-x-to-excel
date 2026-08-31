---
name: researching-x-to-excel
description: Use when investigating public posts on X for a topic, brand, product, creator network, campaign, or recurring monitor and the result must be delivered or maintained as a verified Excel workbook.
---

# Researching X to Excel

Turn a research brief into evidence-backed public-X records and a linked, filterable Excel workbook. Depth means independent search lanes and relationship edges, not repeated queries.

## Start with the brief

Record the topic, locale/languages, public-only scope, date window and timezone, qualification rule (including whether a metric is `gt` or `gte`), cap, required output language, and update versus new-workbook intent. Preserve an existing workbook's stated criteria; if a required criterion is absent or ambiguous, ask rather than invent one.

Set `date_end`/as-of to the actual observation/execution timestamp; never round it forward into future time. Derive `date_start` from that exact timestamp and the requested window.

- Read `references/data-contract.md` before normalizing or merging records.
- Read `references/excel-deliverable.md` before creating or editing a workbook.
- Read `references/japanese-beauty-preset.md` only for Japanese beauty-related research.
- **REQUIRED SUB-SKILL:** Use spreadsheets:Spreadsheets for standalone Excel creation or editing.

## Research matrix and qualification

Build independent lanes before searching: direct topic and spelling variants; brands/products; benefits, complaints, comparisons, alternatives, purchase/sale terms; official accounts and announcements; creators/communities; and quote, reply, source-post, and conversation-thread traversal. Record each lane and query on the candidate. Discover related accounts through explicit mentions, reply/quote participants, profile links, and official-network links; recurse one hop from each qualifying seed, then stop unless the brief authorizes a wider depth.

Work in successive rounds with distinct queries and required traversal. Stop only when a user limit is reached, the requested target count of qualified records is reached, or three consecutive substantive zero-yield rounds occur. A substantive zero-yield round exhausts untried relevant queries and traversal without finding a new verified qualifying record. Exhaustion is not a standalone completion condition: it contributes to a substantive zero-yield round; productive work cannot be skipped. Do not stop productive lanes merely because an earlier phase ends. Never relax a date, public-access, relevance, cap, or metric threshold to fill a target count.

Create a candidate record first. Verify the public post view, canonical post ID, published timestamp/timezone, original text, and required metric at the source. Include a metric only when observed; blank is unavailable, never zero or an estimate. Exclude a candidate with a missing required view count; log it rather than inferring from likes or engagement. Mark restricted, deleted, or unavailable posts with their status and retain the available URL/ID without treating them as verified.

Keep verbatim original text immutable: store normalizations, translations, summaries, stance, and analysis in separate fields. Deduplicate by `post_id`, not display URL. On conflicts, retain the newest verified observation and its `observed_at`; do not silently blend contradictory values. Separate formal verified records from candidates and exclusions. Sort accepted records newest first by `published_at` (then `post_id` for ties).

## Delivery and updates

Create or update only a safe working copy when a workbook is malformed, protected, or formula-damaged; preserve the original and report the defect. For incremental updates, inspect the existing tables, formulas, filters, chart references, styles, validations, sort order, and metadata before adding rows. Deduplicate against the whole existing ID column, preserve calculated columns and layout, and update only the agreed target structures.

Before delivery, inspect formula errors, table filters, link targets, numeric cells, sort order, dashboard links, charts, and rendered workbook appearance. State uncertainty, source limitations, exclusions, and verification timestamps plainly. If required search access, an X export, or credentials are unavailable, provide the exact missing access, candidate/log template, and handoff steps; do not fabricate a dataset.

Keep credentials, cookies, workbooks, browser profiles, and research data outside this repository; never commit or copy them into it. Do not create a recurring monitor, schedule, or automation from a research/update request. Create one only after explicit authorization that states cadence, scope, destination, and notification preference.

## Quick reference

| Need | Rule |
| --- | --- |
| Threshold wording | `gt 5000` excludes 5,000; `gte 5000` includes it. |
| Missing view count | Exclude from verified results; log as unavailable. |
| Repeated discovery | Merge by post ID; preserve newest verified observation. |
| Japanese beauty work | Use natural Japanese sheet labels and the preset; never alter original text. |
| Existing workbook | Preserve its structures and use a safe copy if damaged. |

## Common mistakes

- Treating a creator search as related-account recursion: record the relationship edge and do the bounded one-hop review.
- Calling a summary sheet a dashboard: KPIs and charts must be linked to the posts table and checked against it.
- Replacing malformed formulas in place: work from a copy and disclose the repair need.
- Scheduling “weekly” research by implication: wait for explicit monitoring authorization.
