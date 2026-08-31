# Baseline Results

Controls were run in fresh contexts with only the corresponding fixed scenario and a request for an execution plan and output contract. The raw responses below are reproduced verbatim.

## Scenario 1: Generic consumer product — raw response

# Execution plan

1. Define the collection window as the six calendar months immediately preceding the run date, and record the exact start/end timestamps and timezone in the workbook's README sheet.
2. Establish the metric definition: include only public X posts whose displayed or retrievable view count is strictly greater than 10,000. Do not substitute likes, impressions, reposts, or follower count for views.
3. Build a broad query matrix, then search it systematically. The matrix should cover:
   - Direct terms: compact countertop dishwasher, portable dishwasher, mini dishwasher, table-top/tabletop dishwasher, small dishwasher.
   - Brand/model terms identified during research, including product names and common misspellings.
   - Comparison and purchase language: versus/vs, alternative, worth it, review, setup, install, apartment, RV, dorm, rental, sink hookup, water tank.
   - Problem language: leak, noisy, broken, smell, drying, cleaning, support, return, refund, complaint.
   - Conversation expansion: quoted posts, replies from brands or support accounts, official product announcements/replies, and posts from creators repeatedly appearing in relevant results.
4. Search public posts newest first within the time window. Capture candidates in a staging table, retaining the search query/source route used to find each one.
5. For each candidate, verify that it is publicly accessible, is within the time window, is substantively about a compact countertop dishwasher, and has a verified view count over 10,000. Deduplicate by canonical post URL/ID; treat reposts, quotes, and replies as separate posts only when their own content is relevant and they independently meet the view threshold.
6. Rank the verified set by post timestamp descending and keep at most 80 posts. If fewer than 80 qualify, deliver all qualifying posts and explicitly state the shortfall; do not pad the workbook with unverified or below-threshold posts.
7. Capture only metrics visibly available from the public post or reliable exported source at collection time. Leave unavailable values blank (with an availability flag or note), never estimate them.
8. Perform quality checks: confirm date/time parsing, canonical links, no duplicate post IDs, strict view threshold, relevance evidence for every row, and dashboard formulas/pivots that match the underlying filtered table.
9. Export the workbook and validate that filters, hyperlinks, formulas, charts, and dashboard navigation work in Excel.

# Output contract

Deliver one filterable Excel workbook (`.xlsx`) with these sheets:

## 1. README / Methodology

- Run date and exact six-month collection window.
- Inclusion criteria: public X post, compact-countertop-dishwasher relevance, and views >10,000.
- Ordering rule: newest first.
- Coverage/search taxonomy and any access limitations.
- Data provenance, metric definitions, and a clear statement that blanks mean unavailable/not observed rather than zero.
- Total eligible post count, total delivered count (maximum 80), and exclusions summary.

## 2. Posts

An Excel Table with enabled filters and frozen header row. One row per verified post, sorted newest first, with at least:

| Field | Requirement |
|---|---|
| Rank | Sequential rank after newest-first sorting. |
| Post date/time | Original published timestamp and timezone/normalized timezone. |
| Creator display name | As displayed publicly. |
| Creator handle | Public handle. |
| Creator link | Hyperlink to creator profile. |
| Post link | Canonical hyperlink to the post. |
| Post type | Original post, quote post, reply, official reply, or repost where relevant. |
| Brand / model | Normalized brand/model when identifiable; otherwise blank or `Not specified`. |
| Topic tags | Controlled multi-value tags such as review, comparison, complaint, setup, official response. |
| Relevance evidence | Short, factual snippet or concise description showing why the post concerns a compact countertop dishwasher. |
| Views | Verified numeric view count; only rows >10,000 are included. |
| Likes | Numeric when available; blank when unavailable. |
| Replies | Numeric when available; blank when unavailable. |
| Reposts | Numeric when available; blank when unavailable. |
| Bookmarks | Numeric when publicly available; blank when unavailable. |
| Quotes | Numeric when publicly available; blank when unavailable. |
| Collection source / checked at | Where the data was observed and collection timestamp. |
| Data-quality note | Access issues, unavailable metrics, ambiguity, or other material caveat. |

The workbook must preserve raw numeric metrics as numbers, not formatted text. Hyperlinks must be active and point to the public creator/post URLs.

## 3. Dashboard

Linked to the Posts table through formulas, PivotTables, or Power Query and refreshed/validated before delivery. It should show:

- Total qualifying posts and total recorded views.
- Posts by week or month (newest period visible).
- Top brands/models by post count and recorded views where identifiable.
- Topic mix (reviews, comparisons, complaints, setup, official replies, etc.).
- Top creators by qualifying-post count and recorded views.
- A linked navigation control back to the Posts table and a visible note that all metrics are only those publicly available at collection time.

Dashboard filters/slicers should, where supported, allow at least date/month, brand/model, topic tag, and post type filtering. Visual totals must update consistently with the selected filters.

# Acceptance criteria

- No more than 80 rows; all are public, in-window, relevant, deduplicated, and have verified views strictly above 10,000.
- Rows are newest first.
- Every row includes working creator and post links plus relevance evidence.
- Unavailable metrics are blank/noted, never fabricated or inferred.
- The Posts sheet is filterable, and the dashboard is linked to it and internally consistent.

### Score

| Requirement | Pass/Fail | Evidence |
|---|---|---|
| Multi-lane term expansion | Pass | It specifies direct, brand/model, comparison/purchase, problem, and conversation query lanes in steps 3–4. |
| Quote/reply/source traversal | Pass | Step 3 requires quoted posts, replies from brands/support, official announcements/replies, and keeps each candidate's search query/source route. |
| Related-account recursion | Fail | It mentions creators repeatedly appearing in results, but has no explicit related-account discovery/traversal rule or recursion boundary. |
| Strict view/date qualification | Pass | Steps 1–2 and 5 set the six-month window and require a verified view count strictly greater than 10,000. |
| Post-ID deduplication | Pass | Step 5 requires deduplication by canonical post URL/ID. |
| No invented metrics | Pass | Step 7 requires only visibly available/reliably exported metrics and blanks unavailable values. |
| Linked Excel dashboard | Pass | The Dashboard contract requires formulas, PivotTables, or Power Query linked to Posts and refreshed/validated. |
| Formula/filter/link/visual QA | Pass | Steps 8–9 require formula/pivot, filter, hyperlink, chart, and navigation checks. |
| Natural Japanese; verbatim originals | Fail | The response is an English workbook plan and contains no Japanese UI or immutable-original-text requirement because this control is the English scenario. |
| Monitoring authorization boundary | Fail | The response does not state that no schedule/automation will be created or require explicit authorization. |

## Scenario 2: Japanese beauty — raw response

# 実行計画

## 目的と範囲

日本語で公開されている X の投稿を対象に、実行日から過去 1 年間の「眉毛の色を明るくする商品・方法」に関する投稿を収集・分析する。表示回数が 5,000 超の投稿のみを対象とし、最新順で最大 200 件を納品対象とする。投稿本文は原文をそのまま保存し、口語表現、誤字、表記揺れ、絵文字、ハッシュタグ、URL を改変・正規化しない。

対象は公開投稿に限定する。非公開アカウント、閲覧権限のない投稿、削除済み投稿、取得時点で本文・表示回数・日時のいずれかを確認できない投稿は除外し、除外理由を記録する。

## 収集設計

1. 実行日を `調査基準日` として固定し、開始日をその 365 日前（または暦上の 1 年前。採用した定義を概要シートに明記）に設定する。
2. 次のような語群を組み合わせて検索し、重複を許容して候補を収集する。
   - 課題・行為: `眉毛 明るく`, `眉色 明るく`, `眉毛 脱色`, `眉毛 ブリーチ`, `眉毛 染める`, `眉マスカラ`, `眉カラー`, `眉カラーリング`
   - 商品・剤形: `眉毛脱色剤`, `脱色クリーム`, `ブリーチ剤`, `アイブロウマスカラ`, `眉ティント`, `眉コンシーラー`
   - 購買・販促: `Qoo10`, `メガ割`, `メガポ`, `セール`, `クーポン`, `提供`, `PR`, `広告`, `gifted`
   - 代表的な表記揺れ・候補語: 全角/半角、ひらがな/カタカナ、英字大文字小文字、スペース有無、誤記・略称を含める。
3. 検索結果だけに依存せず、候補投稿の返信、引用、会話スレッド、リンク先の公式投稿、投稿者プロフィール内の関連投稿をたどり、対象範囲に合う投稿を追加する。
4. 各候補について投稿 ID を主キーとして保存し、同一投稿が複数検索で見つかった場合は 1 件に統合する。リポスト表示や重複表示は別投稿として数えない。
5. 投稿日時が対象期間内、本文が日本語中心または日本市場向け、かつ取得時点の表示回数が `5,001` 以上であることを機械判定後、人手確認する。
6. 適格投稿を投稿日時の降順で並べ、上位 200 件を採用する。201 件目以降も条件適合なら除外ログへ残す。

## 深掘り・分析手順

各採用投稿について、原文は変更せず、別列に次を構造化して付与する。

- 商品・ブランド: 本文、画像説明、リンク先で明示されたブランド名・商品名。曖昧な推定は「推定」とし、根拠を記載する。
- 表記揺れ: 原文表記を保持した上で、分析用の統一ブランド名・統一商品名・別名・略称を対応表に登録する。統一不能なものは空欄にせず `要確認` とする。
- 分類: `脱色/ブリーチ`、`眉マスカラ等のメイク`、`染毛・カラー剤`、`サロン・施術`、`DIY/代替手段`、`比較・レビュー`、`その他`。複数該当は複数タグで保持する。
- 競合・代替: 投稿中で直接言及された比較対象、乗り換え先、代用案、購入候補を抽出し、明示言及と分析上の競合候補を分ける。後者は投稿が根拠ではないため根拠ソースを必須にする。
- 関係性: 返信先投稿、引用元投稿、公式アカウントへの返信、公式投稿からの返信、投稿内メンション、関連投稿者を ID と URL で記録する。返信・引用元が取得できない場合はその状態を記録し、推測で補わない。
- 商流・表示: Qoo10、メガ割、その他モール、公式通販、店頭などの購入・販促言及を抽出する。`PR表記あり`、`提供表記あり`、`広告表記あり`、`表記なし`、`判定不能` を区別し、判断根拠となる原文の該当箇所を別列に保存する。

投稿画像・動画にのみ記載された商品情報は、読めた文字と確認方法を「画像由来」と明記する。画像から断定できないブランド名や商品名は補完しない。

## 品質管理

1. 投稿 ID、URL、投稿日時、表示回数、原文、取得日時を必須項目として検査する。
2. 表示回数は取得日時を伴うスナップショット値であり、後日変動し得ることを明示する。
3. サンプルの全件について、URL 遷移、日付範囲、表示回数閾値、重複、原文一致を再確認する。
4. ブランド・商品名の正規化は原文列を一切上書きしない。正規化辞書の変更履歴と判断根拠を残す。
5. 公式性の判定は、アカウントの自己表記・認証・公式サイトからのリンクなど確認可能な根拠に限定し、未確認なら `公式性未確認` とする。
6. 集計数は「候補数」「重複除外数」「期間外除外数」「表示回数不足除外数」「情報不足除外数」「採用数」「上限超過除外数」を照合可能にする。

# 納品物（自然な日本語 UI の Excel）

ファイル名例: `X_眉毛を明るくする商品・方法_公開投稿調査_YYYYMMDD.xlsx`

Excel は日本語の見出し、固定ヘッダー、オートフィルター、先頭行固定、テーブル書式、日付・数値の適切な表示形式、入力規則、条件付き書式を備える。閲覧者がまず開く `調査概要` シートを先頭に置き、セル結合は最小限にする。

## シート構成と列定義

### 1. 調査概要

- 調査テーマ
- 調査基準日
- 対象期間（開始・終了）
- 対象媒体・公開範囲
- 採用条件（日本語、表示回数 5,000 超、最大 200 件、最新順）
- 取得日時・タイムゾーン
- 採用件数と除外内訳
- 留意事項（表示回数の変動、公開投稿に限ること、原文非改変、取得不能項目の扱い）
- 主要な示唆（事実と解釈を区別し、投稿母数・根拠シートへのリンクを付ける）

### 2. 投稿一覧（主データ）

必須列:

`順位`、`投稿日時`、`投稿 URL`、`投稿 ID`、`投稿者表示名`、`投稿者 ID`、`投稿本文（原文）`、`表示回数`、`表示回数取得日時`、`いいね数`、`リポスト数`、`返信数`、`ブックマーク数（取得可能な場合）`、`投稿種別`、`返信先投稿 URL`、`引用元投稿 URL`、`公式アカウントとの関係`、`ブランド名（原文）`、`ブランド名（統一）`、`商品名（原文）`、`商品名（統一）`、`商品カテゴリ`、`競合・比較対象（原文）`、`代替案（原文）`、`関連投稿者`、`購入先・販促言及`、`Qoo10言及`、`メガ割言及`、`PR/広告/提供区分`、`PR等の根拠原文`、`投稿の要点（原文を改変しない要約ではなく分析メモ）`、`画像・動画由来情報`、`取得日時`、`確認状態`、`備考`。

原文列は改行・誤字・口語・記号を含めてそのまま格納する。URL はクリック可能なハイパーリンクとする。

### 3. 商品・ブランド表記辞書

`統一ブランド名`、`統一商品名`、`原文表記`、`表記種別（正式名/略称/誤記/旧名等）`、`カテゴリ`、`根拠投稿 ID`、`公式確認 URL`、`判断状態`、`注記`。

### 4. 競合・代替マップ

`起点ブランド/商品`、`比較先ブランド/商品`、`関係（競合/代替/併用/比較のみ）`、`言及種別（投稿で明示/分析候補）`、`根拠投稿 ID`、`根拠原文`、`根拠 URL`、`確度`、`注記`。

### 5. 会話・関係投稿

`起点投稿 ID`、`関係種別（返信/引用/メンション/公式返信/関連投稿者）`、`関連投稿 ID`、`関連アカウント ID`、`関連投稿 URL`、`関連投稿日時`、`関連本文（原文）`、`公式性判定`、`確認状態`、`注記`。

### 6. 集計

ブランド別・商品別・カテゴリ別・PR区分別・Qoo10/メガ割言及別・投稿月別の件数と、表示回数合計・中央値・最大値を示す。集計対象が最大 200 件の採用投稿であることを明記し、ピボットテーブルまたは数式集計で再計算可能にする。

### 7. 除外・確認ログ

`候補投稿 ID`、`候補 URL`、`検出クエリ/経路`、`除外または保留理由`、`確認日時`、`担当/確認者`、`再確認要否`、`注記`。理由は少なくとも `重複`、`期間外`、`表示回数 5,000 以下`、`日本語対象外`、`情報不足`、`上限超過`、`削除・閲覧不能`、`判定保留` を使用する。

## 出力順と採番ルール

- `投稿一覧` は投稿日時の降順、同日時は投稿 ID の降順で並べる。
- 順位は採用投稿に対する連番 1〜200。欠番を作らない。
- 表示回数がちょうど 5,000 の投稿は含めない（条件は「5,000超」）。
- 200件未満の場合は取得できた適格件数のみを納品し、不足理由を `調査概要` と `除外・確認ログ` に明記する。
- 200件を超える場合は最新順の 200 件のみを `投稿一覧` に載せ、それ以外の適格候補を `上限超過` としてログに残す。

## 完了判定

次をすべて満たしたとき完了とする。

1. `投稿一覧` の全行が対象期間内で、表示回数が 5,001 以上である。
2. 採用件数が 200 件以下で、並び順と順位が最新順になっている。
3. 全投稿に投稿 ID、URL、原文、投稿日時、表示回数、表示回数取得日時がある（取得不能なら採用しない）。
4. 原文列が非改変であり、正規化・分析内容は別列・別シートに分離されている。
5. ブランド表記、商品、競合、代替、公式関係、引用・返信、関連投稿者、Qoo10・メガ割・PR表記について、該当なし・未確認・判定不能を含め一貫した状態値が入っている。
6. 概要数値と主データ・除外ログの件数が一致し、数式・フィルター・リンクが正常に機能する。

### Score

| Requirement | Pass/Fail | Evidence |
|---|---|---|
| Multi-lane term expansion | Pass | The collection design gives task/action, product/form, purchase/promotion, and spelling-variation query families. |
| Quote/reply/source traversal | Pass | Collection step 3 explicitly traverses replies, quotes, conversation threads, linked official posts, and profile-related posts. |
| Related-account recursion | Fail | Collection step 3 follows related posts from the poster profile and the relationship sheet records related accounts, but it defines neither related-account discovery nor recursive traversal. |
| Strict view/date qualification | Pass | Collection steps 1 and 5 require the one-year window and views of 5,001 or greater; completion checks repeat it. |
| Post-ID deduplication | Pass | Collection step 4 uses post ID as the primary key and merges repeat findings. |
| No invented metrics | Pass | It excludes posts with unverifiable text/views/date and says unavailable relationship information must be recorded rather than guessed. |
| Linked Excel dashboard | Fail | It requires recalculable aggregation but does not require a linked dashboard, dashboard navigation, or dashboard filters/slicers. |
| Formula/filter/link/visual QA | Pass | Quality control requires URL, date, threshold, duplicate, and original-text checks; completion requires formulas, filters, and links to work. |
| Natural Japanese; verbatim originals | Pass | It specifies Japanese labels/UI and repeatedly requires the original text to remain unmodified in a separate original-text column. |
| Monitoring authorization boundary | Fail | No statement prohibits scheduling/automation or requires explicit authorization. |

## Scenario 3: Incremental weekly update — raw response

# Weekly X Research Workbook Update: Execution Plan and Output Contract

## Scope and operating assumptions

- This run updates an existing workbook; it does not redesign it or create a new reporting process.
- No scheduling or recurring automation is created. A future weekly run requires explicit authorization.
- The prior observation timestamp is read from the workbook's designated metadata field (or, if absent, the latest successfully recorded observation date). The research window is exclusive of that timestamp and inclusive of the current run cutoff.
- A qualifying item must satisfy the workbook's existing inclusion criteria. If those criteria are not explicit, the run stops for clarification rather than inventing a new standard.

## Execution plan

1. Create a recoverable working copy of the existing workbook and inspect its structure without changing values: sheets, tables/ranges, headers, metadata fields, formulas, filters, sort settings, charts, styles, hyperlinks, and validation rules.
2. Determine and record the prior observation timestamp, current cutoff timestamp, timezone, and resulting date window. Confirm the target research tab/table and the canonical post-ID column.
3. Derive search angles from the workbook's established research scope and prior entries. Use multiple complementary angles as applicable: key people/accounts, product/company/topic names, event or announcement terms, relevant hashtags/phrases, and language/region variants already represented in the workbook.
4. Search only content posted within the determined date window. Collect candidate posts with, at minimum, post ID, URL, author, published time, text/snippet, search angle, and preliminary relevance decision.
5. Recheck the required metrics for each candidate using the same definitions and units used by the workbook. Capture the observation time, source values, and any unavailable metric explicitly; do not substitute estimates.
6. Deduplicate candidates by canonical post ID before insertion. Compare against both the current candidate set and all existing workbook post IDs. Retain one canonical record per ID and merge only non-conflicting supplemental metadata.
7. Apply the workbook's qualifying criteria to the deduplicated, metric-rechecked candidate set. Keep an auditable checked-candidate log, including exclusions and their reason.
8. Insert only new qualifying records into the existing target table/range. Copy the established row structure so formulas, number formats, styles, hyperlinks, data validation, and any calculated columns remain intact. Do not overwrite existing formulas or manual values.
9. Restore and verify newest-first ordering by the workbook's existing date/time field. Preserve existing filters and filter criteria, table definitions, charts, named ranges, links, formulas, styles, freeze panes, and worksheet layout.
10. Update the observation metadata and run report. Save as the agreed deliverable path, then reopen/validate the workbook for formula integrity, links, row counts, duplicate IDs, sorting, filters, and chart references.

## Quality gates

- Every searched candidate is within the stated date window.
- No inserted post ID already exists in the workbook or appears more than once in the new batch.
- Every inserted record passes the pre-existing qualifying criteria and has rechecked metrics.
- Existing formulas and chart source ranges are intact; no formulas have been replaced by static values.
- Existing filters, styling, hyperlinks, validations, and newest-first sort order are preserved.
- A zero-result run still updates the run report/metadata only as appropriate and states that no qualifying records were added; it does not fabricate rows.

## Output contract

The completed update returns the workbook plus a concise run report containing:

| Field | Required content |
| --- | --- |
| Workbook | Absolute path/name of the updated workbook and the target sheet/table updated. |
| Date window | Previous observation timestamp (exclusive), current cutoff (inclusive), and timezone. |
| Search angles | Each query/angle category used, including account/topic/event/language variants where applicable. |
| Checked candidates | Count of unique candidates evaluated; optional attached/logged list with post ID, URL, time, angle, decision, and exclusion reason. |
| New qualifying count | Number of deduplicated qualifying posts inserted; explicitly report `0` when none qualify. |
| Deduplication | Number removed as intra-run duplicates and number already present in the workbook. |
| Metric recheck | Metric definitions/observation time and any unavailable values. |
| Preservation checks | Result for formulas, filters, charts, styles, hyperlinks, validations, and newest-first ordering. |
| Exceptions | Any ambiguity, unavailable source data, or validation failure requiring follow-up. |
| Scheduling | State that no automation or schedule was created unless separately and explicitly authorized. |

### Minimum completion statement

`Updated [workbook] for [previous observation, current cutoff] ([timezone]). Used [search angles]; checked [N] unique candidates; added [M] new qualifying posts ([D1] intra-run duplicates and [D2] existing IDs excluded). Formula/filter/chart/style/link/order preservation: [pass/fail]. No schedule was created.`

### Score

| Requirement | Pass/Fail | Evidence |
|---|---|---|
| Multi-lane term expansion | Pass | Step 3 derives multiple search angles: accounts, product/company/topic names, events, hashtags/phrases, and language/region variants. |
| Quote/reply/source traversal | Fail | It collects candidates but never requires quote, reply, source-post, or conversation-thread traversal. |
| Related-account recursion | Fail | It lists key accounts as a search angle but does not require discovery and recursive review of related accounts. |
| Strict view/date qualification | Pass | Steps 2 and 4 define the exclusive/inclusive window and search only within it; step 7 applies the existing qualifying criteria. |
| Post-ID deduplication | Pass | Step 6 deduplicates by canonical post ID across both the new set and existing workbook records. |
| No invented metrics | Pass | Step 5 requires rechecked source metrics, explicit unavailable values, and no estimates. |
| Linked Excel dashboard | Fail | It preserves existing charts but does not require that a dashboard be linked to the Posts data or validate dashboard consistency. |
| Formula/filter/link/visual QA | Pass | Steps 8–10 and quality gates require preserving and validating formulas, filters, charts, styles, hyperlinks, validations, and order. |
| Natural Japanese; verbatim originals | Fail | It contains no Japanese UI requirement or preservation rule for verbatim original post text. |
| Monitoring authorization boundary | Pass | Scope explicitly says no recurring automation is created and future runs need explicit authorization; the output repeats that boundary. |

## Demonstrated baseline gaps

At least one gap is demonstrated: the generic-control response lacks related-account recursion and the monitoring-authorization boundary; the Japanese-control response omits a linked dashboard and the monitoring boundary; and the incremental-control response omits quote/reply/source traversal, related-account recursion, a linked dashboard, and Japanese/verbatim-original safeguards. A reusable Skill is therefore justified.
