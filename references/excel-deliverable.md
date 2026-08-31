# Excel deliverable

Use these seven sections/sheets one-to-one unless an existing workbook has compatible localized names:

1. **Dashboard / ダッシュボード** — linked KPIs, time trend, category/relevance distribution, a linked top-post view, interactive filters or slicers, and navigation to Posts.
2. **Summary / サマリー** — brief, observation window/timezone, coverage, accepted/rejected counts, findings, and limitations.
3. **Posts / 投稿一覧** — one qualifying post per row, all `PostRecord` fields, rank, normalization, tags, and quality note.
4. **Source & Quote Analysis / 引用元分析** — quote, reply, parent/source relationships and both URLs.
5. **Research Angles & Candidate Log / 調査角度・候補ログ** — lanes, terms, accounts, substantive rounds, candidate counts, yield, decisions, and reasons.
6. **Additional Candidates / 追加調査候補** — near-threshold, unverified, inaccessible, context-only, and other excluded candidates with reasons.
7. **Methodology & Verification / 調査方法・検証結果** — definitions, timestamps, sources, limits, stopping evidence, validation results, and QA outcomes.

Do not collapse or substitute these required sections; Japanese equivalents may be combined labels but must preserve each role. Make Posts and all detail/log ranges Excel Tables with filters and frozen headers. Keep clickable post/creator URLs and typed dates/numbers. Link Dashboard KPIs, charts, top posts, and controls to the Posts table through formulas, pivots, Power Query, or slicer-capable Tables/Pivots—never copied totals. Include linked trend and distribution charts. Filters/slicers must materially filter the linked view.

For incremental work, preserve compatible order, tables, calculated columns, filters/slicers, formulas, styles, validations, named ranges, hyperlinks, charts, and sort order. Insert through established tables. Before delivery, inspect formula errors, table/filter/slicer behavior, links, top-post ordering, chart ranges, and dashboard totals; render/open every sheet for clipping, overlap, and readability QA.
