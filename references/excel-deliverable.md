# Excel deliverable

Use seven default sheets unless an existing workbook requires its established structure:

1. **Research Summary** — brief, window/timezone, criteria, source limits, counts, and exclusions.
2. **Posts** — all `PostRecord` fields plus rank, normalized brand/product, topic tags, and data-quality note.
3. **Search & Candidate Log** — candidate ID/URL, query, discovery lane, checked time, decision, and exclusion reason.
4. **Relationship Map** — root post ID, relation type, related post/account ID and URL, evidence, traversal depth, and status.
5. **Normalization Dictionary** — original term, normalized term, type, evidence post ID, decision, and note.
6. **Dashboard** — formula-linked KPIs, trend, distribution, and navigation link to Posts.
7. **Exclusions & Verification Log** — ID/URL, status/reason, required-field outcome, source, observer, and timestamp.

Make Posts and every log table an Excel Table with filters and frozen headers. Use required columns above; maintain active clickable post and creator URLs. Keep timestamps and metrics typed as dates/numbers. Link Dashboard KPIs to the Posts table through formulas, pivots, or Power Query—never manually copied totals. Include a trend chart by week/month and a distribution chart (for example topic, brand, post type, or stance); charts must reference the linked data.

For incremental work, preserve existing sheet order, tables, calculated columns, filters, formulas, styles, validations, named ranges, hyperlinks, charts, and sort order. Insert rows through the established table/range; do not overwrite formulas or manual values. Before delivery, inspect formula errors (`#REF!`, `#VALUE!`, `#DIV/0!`, and similar), validate links and filters, and render/open the workbook for visual QA of clipping, headers, charts, and dashboard readability.
