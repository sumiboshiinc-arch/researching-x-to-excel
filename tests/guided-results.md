# Guided Results

## Raw guided outputs (verbatim)

### Scenario 1

<pre>
# Guided scenario 1 — public X research to Excel plan

## Scope and assumptions

| Brief field | Value |
| --- | --- |
| Topic | Compact countertop dishwashers |
| Scope | Public X posts only |
| Date window | The six calendar months ending at execution time; use an explicit `date_start` and `date_end` at run start |
| Timezone | Capture and report the execution timezone; normalize every source timestamp with its offset |
| Qualification | `views gt 10000` — strictly more than 10,000 observed views |
| Cap | Up to 80 verified qualifying posts |
| Ordering | `published_at` descending, then `post_id` descending |
| Output | New, filterable Excel workbook with a linked dashboard |
| Language/locale | Not stated; retain each original post verbatim and use English workbook labels unless the requester specifies otherwise |
| Monitoring | Not authorized |

Do not treat 10,000 views as qualifying. A post without an observed public view count is not a verified result, even if other engagement is high.

## Execution plan

1. Initialize a `ResearchBrief` with the fixed scope above and freeze the exact run timestamps, timezone, and six-month boundary before collection.
2. Create a candidate log and conduct independent search lanes. Record every query, lane, checked time, candidate URL/ID, and disposition.
   - Direct: `countertop dishwasher`, `compact dishwasher`, `portable dishwasher`, `mini dishwasher`, `tabletop dishwasher`, spelling and hashtag variants.
   - Brands/products: current and historical compact units (for example, COMFEE', Farberware, Hermitlux, BLACK+DECKER, Novete, HAVA, Danby, RCA, Midea) and explicit model names discovered during research.
   - Intent/experience: apartment, dorm, RV, small kitchen, no hookup, installation, cleaning, drying, leak, noise, capacity, detergent, energy/water use, repair, return, deal, sale, and purchase terms.
   - Comparisons/alternatives: handwashing, full-size and built-in dishwashers, portable/rolling models, dish-drying and countertop appliances.
   - Community/creator: appliance reviewers, small-space/RV/dorm accounts, kitchen creators, deal accounts, consumer advocates, and creators explicitly connected by a verified post.
   - Official/conversation: official brand accounts, launch/support announcements, replies, quote posts, source posts, quoted posts, and threads.
3. For each candidate, open the public source and verify the canonical post ID/URL, original text, creator and creator URL, publication timestamp/offset, view count, and every engagement metric actually displayed. Determine post type and capture source-post linkage for replies/quotes.
4. Apply the strict qualification gate: in-window, public and accessible, genuinely about compact countertop dishwashers, and observed `views > 10000`. Keep excluded, restricted, deleted, and missing-view candidates in logs rather than estimating metrics.
5. From each qualifying seed, discover accounts/posts only through explicit mentions, reply/quote participants, profile links, and official-network links. Record relationship evidence and traverse one hop; do not recurse further without authorization.
6. Deduplicate on `post_id`. When observations conflict, retain the newest verified observation by `observed_at`; preserve older values only where the newest observation lacks that field. Never overwrite verified facts with candidate data.
7. Continue productive lanes and traversal until 80 verified posts are collected, all relevant lanes are exhausted, or three consecutive substantive zero-yield rounds occur. A zero-yield round must exhaust new relevant queries plus required traversal and add no new verified qualifying record.
8. Sort verified posts newest first, build the workbook, validate its links/formulas/tables/charts visually, and document source limitations, timestamps, and exclusions.

## Normalized record contract

Use `post_id` as the identity key. Keep the following `PostRecord` fields for every formal record; metrics are numeric, unavailable displayed metrics are blank/null, and `original_text` is immutable verbatim source text.

| Field | Rule |
| --- | --- |
| `post_id`, `post_url` | Canonical X status identity and clickable source URL |
| `published_at`, `timezone` | Source timestamp with offset and execution/reporting timezone |
| `views` | Required qualification metric; observed numeric count only; must be `> 10000` to be verified |
| `likes`, `reposts`, `replies`, `quotes`, `bookmarks` | Observed numeric values only; blank/null when unavailable, never inferred or set to zero |
| `original_text` | Exact post text; no translation or normalization in this field |
| `creator_name`, `handle`, `creator_url` | Observed creator identity and clickable public profile link |
| `post_type` | `original`, `reply`, `quote`, or other observed type |
| `relevance_tier`, `stance`, `disclosure`, `summary` | Separate analytical fields; evidence-based and distinct from source text |
| `relevance_evidence` | Brief factual evidence tying the post to a compact countertop dishwasher (brand/model, use case, comparison, complaint, or official reply) |
| `source_post_id`, `source_post_url` | Source/conversation post linkage for a reply or quote; blank/null if none |
| `discovery_lane` | Named lane/query family that discovered the record |
| `verification_state`, `observed_at` | Explicit state and time source facts were observed |

Add these workbook-specific fields to the Posts table: `rank`, `normalized_brand`, `normalized_product`, `topic_tags`, and `data_quality_note`.

Verification states include `candidate`, `verified`, `missing_required_view`, `restricted`, and `deleted`. A candidate is promoted only when all required source facts, especially views, are observed. Candidates and exclusions are never mixed into the verified Posts table.

## Workbook contract

Create a new workbook with these seven sheets, using Excel Tables with filters and frozen header rows on Posts and every log sheet. Store timestamps as date/time values and metrics as numbers. Keep active hyperlinks for post and creator URLs.

| Sheet | Required content |
| --- | --- |
| Research Summary | Frozen brief, exact six-month window/timezone, strict `views gt 10000` rule, run timestamp, source/access limitations, verified count, and exclusion counts |
| Posts | All `PostRecord` fields plus rank, normalized brand/product, tags, and data-quality note; sorted newest first |
| Search & Candidate Log | Candidate ID/URL, exact query, discovery lane, checked time, decision, and exclusion reason |
| Relationship Map | Root post ID, relation type, related post/account ID and URL, relationship evidence, traversal depth, and status |
| Normalization Dictionary | Original term, normalized term, type, evidence post ID, decision, and note |
| Dashboard | Formula/pivot/Power-Query-linked KPIs, a weekly or monthly posting trend, a distribution chart, and a navigation hyperlink to Posts |
| Exclusions & Verification Log | ID/URL, status/reason, required-field outcome, source, observer, and timestamp |

Dashboard KPIs must calculate from the Posts table—not copied values—and should include verified-post count, total/median views where available, share by stance/post type, and newest post date. Use a trend chart by week or month and a distribution chart by normalized brand, post type, topic tag, or stance. Both charts must reference linked data.

## Stopping rule

Stop collection at the first applicable condition:

1. 80 verified qualifying records are collected;
2. relevant independent lanes and the allowed one-hop traversals are exhausted; or
3. three consecutive substantive zero-yield rounds occur.

Do not relax the date window, public-only rule, relevance requirement, strict `> 10,000` view threshold, or cap to reach 80. Do not stop a productive lane merely because an earlier phase ended.

## Validation checklist

- [ ] Exact run date, date window, timezone, strict operator, cap, and public-only scope are recorded.
- [ ] Every verified post has a canonical `post_id`, working post and creator links, observed publication time, verbatim text, and numeric observed views strictly greater than 10,000.
- [ ] All unavailable engagement metrics are blank/null; none are fabricated, estimated, or substituted with zero.
- [ ] Relevance evidence demonstrates an actual compact countertop-dishwasher connection; generic dishwasher posts are excluded or logged.
- [ ] Quotes, replies, official replies, and source-post links have correct relationship metadata; related-account exploration does not exceed one hop.
- [ ] Candidates, verified records, and exclusions are separated; restricted/deleted/missing-view records are retained only in appropriate logs.
- [ ] Duplicate IDs are merged according to newest verified `observed_at`; records are sorted by `published_at` then `post_id`, both descending.
- [ ] Posts and logs are Excel Tables with filters and frozen headers; all dates and metrics use correct cell types.
- [ ] Dashboard formulas/pivots/charts point to the Posts table; no formula errors (`#REF!`, `#VALUE!`, `#DIV/0!`, etc.) remain.
- [ ] Dashboard navigation link, every creator/post hyperlink, chart source range, filters, and workbook rendering have been checked visually.
- [ ] Research Summary plainly states verification time, access limitations, source limitations, stopping condition, and counts by exclusion status.

## Supporting references read

- `SKILL.md` — required workflow, independent-lane research, verification, traversal, stopping, and delivery rules.
- `references/data-contract.md` — `ResearchBrief` and `PostRecord` schema, strict metric semantics, identity/deduplication rules.
- `references/excel-deliverable.md` — required workbook sheets, Excel tables, dashboard linkage, and QA requirements.
</pre>

### Scenario 2

<pre>
# 日本のX公開投稿調査：眉毛の色を明るくする商品・方法

## 前提（ResearchBrief）

| 項目 | 定義 |
|---|---|
| topic | 日本のX公開投稿における「眉毛の色を明るくする商品・方法」 |
| locale / languages | 日本 / 日本語を主対象（日本向けの英語・ローマ字・混在表記も検索対象） |
| public_only | true。ログイン必須、非公開、削除、閲覧制限付きの投稿は正式結果にしない。 |
| date_start | 実査開始時点から遡る直近1年間（Asia/Tokyo）。開始・終了の確定ISO日時を調査概要に記録する。 |
| date_end | 実査終了時点（Asia/Tokyo） |
| qualification_metric | views |
| qualification_operator / value | `gt` / `5000`。**5,000ちょうどは不採用**、5,001以上のみ正式結果にする。 |
| cap | 最大200件。到達前でも基準を緩和しない。 |
| output_language | 日本語の自然なExcel UI。投稿本文（原文）は改変しない。 |
| workbook_mode | new |
| monitoring_authorized | false。定期監視や自動化は作成しない。 |

この文書は実行設計であり、Xの投稿データを生成・推測しない。実査には公開X投稿を確認できるアクセス、又はその裏付けとなるXエクスポートが必要である。

## 実行計画

1. **調査範囲を固定する。** 実査日を `date_end`、その1年前の同時刻を `date_start` とし、JSTで記録する。検索画面で見える候補と、検証済み・除外を初めから別管理する。

2. **独立した検索レーンを作る。** 各候補にレーン名と実際の検索式を残す。使う語群は、`眉マスカラ`、`眉毛 脱色`、`眉毛 ブリーチ`、`眉毛 明るく`、`眉カラー`、`アイブロウカラー`、`眉染め`、`眉ティント`、`コンシーラー 眉`、`眉毛 剃る`、`眉カット`、`眉毛 サロン`、`眉毛 アート` と、それぞれの漢字・ひらがな・カナ・英字・全半角・スペース有無である。検索語には、直接商品/方法、効果・使用感、悩み/失敗/不満、比較/競合、代替、購入/セール、公式、クリエイター/コミュニティ、会話追跡を分けて割り当てる。

3. **ブランド・商品・販促・開示を深掘りする。** 候補本文、メンション、プロフィール、リンク先、返信/引用から発見した正式名称と表記揺れを辞書化する。ブランド名、商品名、競合品、代替方法を横断し、`Qoo10`、`メガ割`、`楽天`、`Amazon`、`PLAZA`、`LOFT`、`@cosme`、公式通販、クーポン、セールも独立レーンで検索する。`PR`、`AD`、`提供`、`gifted`、`モニター` は検出語・原文・確認状態を保存するだけで、検出語のみからPR又は公式性を断定しない。

4. **会話と関連投稿者を1ホップだけたどる。** 各適格シードについて、親投稿、引用元、返信先/返信者、引用投稿、明示メンション、プロフィールリンク、公式ネットワークを確認する。関係タイプ、根拠、深さ、結果を関係マップに記録し、関連アカウントはシードから1ホップまで探索する。明示的な追加許可なしに2ホップへ再帰しない。

5. **候補を一次記録してから原典で検証する。** 公開投稿ビューで canonical post ID、URL、JST公開日時、原文、表示回数を確認する。表示回数が確認できない候補は正式結果から除外し、`missing_required_view` としてログに残す。制限・削除・非公開は利用可能なURL/IDを残して `restricted` / `deleted` 等で管理する。

6. **正規化・重複処理・並べ替えを行う。** identity は表示URLではなく `post_id`。同一IDの観測値が矛盾する時は `observed_at` が最も新しい検証済み観測を優先し、新しい観測に欠ける値だけ旧検証済み値を保持する。候補値で検証済み値を上書きしない。採用レコードは `published_at` 降順、同時刻は `post_id` 降順で並べる。

7. **Excelを作成し検証する。** 以下の7シートとExcelテーブル、フィルター、固定ヘッダー、型付き日時/数値、クリック可能なURL、数式連動ダッシュボードを作る。投稿本文（原文）は一文字も正規化・校正・翻訳しない。集計値は手入力で複写せず投稿テーブルから数式又はピボットで作る。

## 正規化済みレコード契約

### 必須 `PostRecord` フィールド

| フィールド | 型・規則 |
|---|---|
| `post_id` | 文字列。主キー、Xのcanonical ID。 |
| `post_url` | 文字列URL。公開投稿のcanonical URL。 |
| `published_at` | JSTオフセット付きISO 8601日時。Excelでは型付き日時も保持する。 |
| `timezone` | `Asia/Tokyo`。 |
| `views` | 数値。必須の適格指標。未観測時は空欄であり0にしない。 |
| `likes`, `reposts`, `replies`, `quotes`, `bookmarks` | 数値又はnull。観測済み値だけ入れ、未観測を0にしない。 |
| `original_text` | 文字列。表示された投稿原文を**そのまま**保存。口語、誤字、絵文字、改行、URLを変更しない。 |
| `creator_name`, `handle`, `creator_url` | 文字列又はnull。観測できた公開プロフィール情報。 |
| `post_type` | `original` / `reply` / `quote` / `repost` 等、原典で確認した投稿形態。 |
| `relevance_tier` | `high` / `medium` / `low`。商品・方法との明示性に基づく分析値。 |
| `stance` | `positive` / `negative` / `neutral` / `mixed` / `unclear`。原文と文脈に基づく分析値。 |
| `disclosure` | `none_observed` / `PR_detected` / `AD_detected` / `provided_detected` / `gifted_detected` / `monitor_detected` / `unclear`。検出と確認を混同しない。 |
| `summary` | 改変不可の原文とは別の日本語要約。推測はしない。 |
| `relevance_evidence` | その投稿が対象に関係する明示根拠（商品・方法・比較・購入等）。 |
| `source_post_id`, `source_post_url` | 引用元、返信先、又は発見元の投稿ID/URL。なければnull。 |
| `discovery_lane` | 検索マトリクスのレーン名。 |
| `verification_state` | `candidate` / `verified` / `missing_required_view` / `restricted` / `deleted` 等。正式結果は `verified` のみ。 |
| `observed_at` | 検証者が原典を観測したJSTオフセット付きISO 8601日時。 |

### 追加の正規化・関係フィールド

- `rank`：`verified` だけに付与する最新順の連番。
- `normalized_brand` / `normalized_product`：原文から分離した正規化値。原文へ書き戻さない。
- `brand_alias_observed` / `product_alias_observed`：本文・プロフィール・リンクに出た表記そのもの。
- `topic_tags`：例：`眉マスカラ`、`脱色`、`眉毛サロン`、`比較`、`代替`、`Qoo10`、`メガ割`。複数可。
- `marketplace_promotion_signals`：Qoo10・メガ割等の検出語と文脈。
- `official_relationship_status`：`official_account` / `reply_to_official` / `quote_of_official` / `official_network_linked` / `not_confirmed`。証拠を必ず併記する。
- `data_quality_note`：欠損、URL解決、重複競合、文脈不足などの注記。

### 関係エッジ契約

`root_post_id`, `relation_type`, `related_post_id_or_account_id`, `related_url`, `evidence`, `traversal_depth`, `status`, `checked_at` を1行1エッジで保存する。`relation_type` は `reply_to`、`replied_by`、`quotes`、`quoted_by`、`source_post`、`mentions`、`profile_link`、`official_network` 等を用いる。深さは0（シード）又は1のみ。

## ブック契約（自然な日本語UI）

| シート名 | 役割・必須内容 |
|---|---|
| `調査概要` | 調査テーマ、対象期間/JST、公開限定、`表示回数 > 5,000`、上限200、実査日時、取得制約、採用/候補/除外件数、未確認事項。 |
| `投稿一覧` | 全必須PostRecord列、順位、正規化ブランド/商品、表記揺れ、トピックタグ、販促シグナル、公式関係、品質メモ。投稿URL・投稿者URLはクリック可能。Excelテーブル、フィルター、先頭行固定、最新順。 |
| `検索・候補ログ` | 候補ID/URL、検索式、検索レーン、確認日時、判定、除外理由、再確認要否。採否と根拠を監査可能にする。 |
| `関係マップ` | 上記関係エッジ契約。引用元・返信・公式返信・関連投稿者を1ホップまで可視化できるテーブル。 |
| `表記ゆれ辞書` | 原表記、正規化表記、種別（ブランド/商品/方法/販促/開示）、証拠投稿ID、判断、注記。 |
| `集計` | `投稿一覧`テーブルに数式/ピボットで連動するKPI（採用件数、ブランド/商品/方法別件数、PR検出数、Qoo10・メガ割言及数、投稿形態別件数）。週又は月の件数推移グラフと、ブランド・方法・投稿形態・スタンスのいずれかの分布グラフを置く。グラフ元データも数式連動にする。 |
| `除外・確認ログ` | ID/URL、状態・理由、表示回数の確認結果、原典、確認者、確認日時。`missing_required_view`、`restricted`、`deleted`、期間外、重複、関連性不足を明示する。 |

全てのログ/一覧はExcelテーブルにし、固定ヘッダーとフィルターを設定する。見出しは明確に区別し、数値は `#,##0`、日付は `yyyy-mm-dd`、日時は `yyyy-mm-dd hh:mm` の型付き表示とする。タイトル/要約・カードには控えめな色と余白を使い、未使用領域を過度に装飾しない。集計は元表参照の数式・ピボットのみとし、手入力のKPIや静的コピーのグラフデータは作らない。作成時は投稿本文列を読みやすく広めにし、折返し・行高を確認する。

## 停止ルール

次のいずれかで停止する。

1. 検証済みかつ期間内・公開・関連・`views > 5000` の投稿が200件に達した時点。
2. 依頼された実査対象数（最大200件の範囲で別途合意された目標）が到達した時点。
3. 新たな検証済み適格投稿を得られない**実質的なゼロ収穫ラウンドが3回連続**した時点。各ラウンドでは、未試行の関連検索語と、返信・引用・引用元・関連アカウント（最大1ホップ）の追跡を使い切る必要がある。

5,000ちょうどを採用する、期間を広げる、非公開/制限投稿を正式化する、表示回数を他エンゲージメントから推定する、といった基準緩和は停止回避のためにも行わない。アクセス不足の場合は、直ちに取得不能を明示し、候補/ログ用テンプレートと必要なアクセス又はXエクスポートの引き継ぎ手順を渡して停止する。

## 検証チェックリスト

- [ ] `date_start` / `date_end`、JST、公開限定、`views gt 5000`、最大200件を調査概要に明記した。
- [ ] 正式レコードは全件 `verification_state=verified`、期間内、公開、関連あり、`views` が数値の5,001以上である。
- [ ] 投稿ID、canonical URL、公開日時、原文、表示回数を公開原典で確認し、`observed_at` を記録した。
- [ ] 投稿本文（原文）には校正・表記統一・翻訳・要約の上書きがない。
- [ ] 候補、検証済み、除外を混在させず、表示回数不明は `missing_required_view` として除外ログにある。
- [ ] 重複を `post_id` で解消し、競合観測は最新の検証済み `observed_at` を優先した。
- [ ] 最新順（`published_at` 降順、同時刻は `post_id` 降順）かつ最大200件である。
- [ ] ブランド/商品表記揺れ、競合・代替、Qoo10・メガ割等、PR等の検出語は原文根拠と別分析列に保存した。検出語だけでPR・公式性を断定していない。
- [ ] 公式への返信、引用元、引用投稿、関連投稿者は根拠付きの関係エッジとして記録され、探索深度は1を超えない。
- [ ] `投稿一覧` と各ログはExcelテーブル、固定ヘッダー、フィルター、型付き数値/日時、動作する投稿者/投稿ハイパーリンクを備える。
- [ ] `集計` のKPI・週/月推移・分布グラフは投稿テーブルの数式/ピボットに連動しており、静的転記ではない。
- [ ] 数式エラー（`#REF!`、`#VALUE!`、`#DIV/0!`、`#NAME?`、`#N/A`）を確認し、テーブル範囲、フィルター、リンク、数値セル、グラフ元範囲を点検した。
- [ ] 全シートをレンダリングして、見出し・原文・数値・グラフに切れ、重なり、空白グラフ、読めない配色がないことを確認した。

## 読了した参照

- `SKILL.md`（Researching X to Excel）
- `references/data-contract.md`
- `references/excel-deliverable.md`
- `references/japanese-beauty-preset.md`
- `spreadsheets/SKILL.md`（必須サブスキル）
- `spreadsheets/style_guidelines.md`
- `spreadsheets/artifact_tool_docs/API_QUICK_START.md`
- `spreadsheets/features/charts.md`
</pre>

### Scenario 3

<pre>
# Guided scenario 3 — weekly incremental X-research update

## Scope decision

Treat this as an **incremental workbook update**, not authorization to create a
recurring monitor or scheduler. “Weekly” describes the requested update
cadence; `monitoring_authorized` remains `false` unless the user explicitly
authorizes automation and provides all of: cadence, scope, destination, and
notification preference.

Before execution, obtain or read from the existing workbook: topic, locale and
languages, public-only scope, workbook timezone, the exact threshold metric,
operator (`gt`/`gte`), value, cap, output language, target table/sheets, and
the prior observation timestamp. If any required criterion or the prior
observation boundary is absent or ambiguous, stop and ask; do not invent it.

## Execution plan

1. Make a safe working copy if the source workbook is malformed, protected, or
   formula-damaged; preserve the original and report the defect. Otherwise use
   the agreed incremental working copy.
2. Inspect the workbook before insertion: sheet order, target Posts table and
   whole `post_id` column, formulas/calculated columns, filters, sort order,
   styles, validations, named ranges, hyperlinks, chart references, dashboard
   links, and the prior-observation metadata. Render/open it to establish the
   visual baseline.
3. Set the observation window to `(prior_observed_at, current_observed_at]` in
   the configured timezone. Record both endpoints and the timezone in the
   update log/summary. Search public X only for posts published in that window;
   “weekly” must not replace this boundary with an assumed calendar week.
4. Build and record independent search angles: direct topic/spelling variants;
   brands/products; benefits, complaints, comparisons, alternatives, and
   purchase/sale terms; official accounts/announcements; creators/communities;
   and quote/reply/source-post/thread traversal. Discover related accounts via
   explicit relationship evidence and traverse one hop from each qualifying
   seed only.
5. Create a candidate for every discovered post. At the public source, recheck
   canonical ID, URL, publication timestamp/timezone, immutable original text,
   and current view count; capture other visible metrics when observed. Do not
   substitute engagement for missing views.
6. Apply the configured threshold literally (`gt N` excludes `N`; `gte N`
   includes it). Put missing-view, restricted, deleted, unavailable,
   irrelevant, out-of-window, and below-threshold candidates in the appropriate
   log/exclusion state rather than in verified records.
7. Deduplicate candidates and accepted records by `post_id`, including the
   entire existing workbook ID column. For an ID with conflicting observations,
   keep the newest verified observation by `observed_at`; do not overwrite a
   verified field with a candidate field or silently blend conflicts.
8. Insert only genuinely new qualifying records through the established table
   or range. Preserve calculated columns and all existing layout; keep formal
   records ordered `published_at` descending, then `post_id` descending, using
   the established table sort mechanism where available.
9. Update the existing summary/log structures with observation window, search
   angles, candidate count, new qualifying count, exclusions, source limits,
   and verification times. Report those fields even when the new qualifying
   count is zero.
10. Validate workbook integrity and visual output, then deliver the updated
    working copy. Do not create any scheduler or automation.

## Proposed record contract

### ResearchBrief / run metadata

`topic, locale, languages, public_only, date_start, date_end, timezone,
qualification_metric, qualification_operator, qualification_value, cap,
output_language, workbook_mode="incremental", monitoring_authorized=false,
prior_observed_at, current_observed_at, observation_window_start,
observation_window_end, search_angles, candidate_count, new_qualifying_count`

`date_start` is the exclusive prior-observation boundary and `date_end` is the
inclusive current-observation boundary. Store timestamps as timezone-aware
values; retain the exact search angles/queries in the Search & Candidate Log.

### PostRecord

Required fields:

`post_id, post_url, published_at, timezone, views, likes, reposts, replies,
quotes, bookmarks, original_text, creator_name, handle, creator_url,
post_type, relevance_tier, stance, disclosure, summary, relevance_evidence,
source_post_id, source_post_url, discovery_lane, verification_state,
observed_at`

Rules:

- `post_id` is the identity key; URLs are not the deduplication key.
- Metrics are numeric when observed; unavailable values are blank/null, never
  zero or estimates.
- `original_text` is verbatim and immutable; normalization, translation, and
  analysis stay in separate columns.
- A formal inserted record must be `verification_state=verified`, have a
  verified required view count, fall in the observation window, be relevant,
  meet the configured threshold, and be new relative to the whole existing ID
  column.
- Keep candidates, verified records, and exclusions separate. Use explicit
  states such as `candidate`, `verified`, `missing_required_view`,
  `restricted`, and `deleted`.

## Workbook update contract

- Preserve the source workbook’s sheet order, existing tables, formulas,
  calculated columns, filters, styles, validations, named ranges, hyperlinks,
  dashboard links, chart references, and established newest-first sort order.
- Add rows through the target Excel Table/range only; never overwrite formulas
  or user-entered values. Extend table-dependent calculations, conditional
  formatting, and dynamic chart sources as required by the established design.
- Keep clickable post and creator hyperlinks active; store timestamps as dates
  and metrics as numbers.
- Do not recreate default sheets when an existing workbook has an established
  structure. If its structure uses the seven standard areas, update their
  corresponding existing tables: Research Summary, Posts, Search & Candidate
  Log, Relationship Map, Normalization Dictionary, Dashboard, and Exclusions &
  Verification Log.
- The summary/run log must state: prior and current observation timestamps,
  timezone, exact observation window, search angles, candidate count, new
  qualifying count, threshold/operator, exclusion counts/reasons, source
  limitations, and verification timestamp—also for a zero-result update.
- If workbook damage, protection, or malformed formulas prevent safe mutation,
  stop in-place editing, use a safe working copy only when feasible, and report
  the defect.

## Stopping rule

Continue successive, distinct search-and-traversal rounds until the first of:

1. the user-defined cap is reached;
2. the requested target count of qualified records is reached; or
3. three consecutive **substantive** zero-yield rounds occur.

A substantive zero-yield round exhausts untried relevant queries and required
one-hop traversal without finding a new verified qualifying record. Never stop
a productive lane merely because an earlier phase ends, and never relax the
public-only, date-window, relevance, cap, or threshold rules to fill a target.
For an incremental run, existing records and duplicate IDs do not count as new
qualified yield.

## Validation checklist

- [ ] Existing workbook was inspected and visually baselined before editing.
- [ ] Prior observation boundary, current boundary, and configured timezone are
      explicit; every searched post is within `(prior, current]`.
- [ ] Each search angle/query and relationship traversal is retained in a log.
- [ ] Candidate count and new qualifying count are reported, including zero.
- [ ] Each inserted record has a canonical `post_id`, source URL, verified
      publication time, immutable original text, `observed_at`, and an observed
      numeric view count.
- [ ] Threshold operator and value were applied exactly; missing views were
      excluded/logged rather than inferred.
- [ ] Deduplication covered the whole existing ID column and all new candidates;
      conflicting observations honor newest verified `observed_at`.
- [ ] Posts are newest first by `published_at`, then `post_id`; ties and sort
      behavior are checked after insertion.
- [ ] Formulas/calculated columns, filters, styles, validations, named ranges,
      hyperlinks, dashboard links, and charts are still intact and correctly
      extended where needed.
- [ ] No formula errors such as `#REF!`, `#VALUE!`, or `#DIV/0!`; numeric cells
      and link targets were checked.
- [ ] Rendered visual QA confirms readable headers, no clipping, and working
      chart/dashboard presentation.
- [ ] No monitoring automation or scheduler was created.

## Exact references read

1. `/Users/SMBS05/.codex/skill-repos/researching-x-to-excel/SKILL.md`
2. `/Users/SMBS05/.codex/skill-repos/researching-x-to-excel/references/data-contract.md`
3. `/Users/SMBS05/.codex/skill-repos/researching-x-to-excel/references/excel-deliverable.md`
4. `/Users/SMBS05/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.826.12353/skills/spreadsheets/SKILL.md`
</pre>

### Scenario 1 rerun

<pre>
# Guided scenario 1 — compact countertop dishwashers

## Execution plan

### 1. Lock the research brief before collection

Use this `ResearchBrief` at execution start. The six-month window is interpreted as the six complete calendar months ending on the execution date, in `Asia/Tokyo`; for an execution on 2026-08-31, this is 2026-03-01T00:00:00+09:00 through 2026-08-31T23:59:59+09:00. Record the actual run-start time separately as `observed_at`.

| Field | Locked value |
| --- | --- |
| `topic` | Compact countertop dishwashers (portable/mini/desktop dishwashers intended for countertop or small-space use) |
| `locale` | Global public X; do not apply an unstated country restriction |
| `languages` | Any language; retain original text exactly and write English analysis fields unless the delivery brief changes it |
| `public_only` | `true` |
| `date_start` / `date_end` | Locked rolling six-month window above |
| `timezone` | `Asia/Tokyo` |
| `qualification_metric` | `views` |
| `qualification_operator` | `gt` |
| `qualification_value` | `10000` |
| `cap` | `80` verified posts maximum |
| `output_language` | English |
| `workbook_mode` | `new` |
| `monitoring_authorized` | `false` — no scheduler, refresh, or recurring monitor |

`gt 10000` is strict: a post at exactly 10,000 views does **not** qualify. A missing view count is unavailable, never zero or inferred from engagement, and therefore cannot become a verified record.

### 2. Set up candidate, evidence, and conflict handling

Create separate collections/tables for candidates, verified records, and exclusions. Capture the canonical post URL and ID, public source observation, published time, original text, and view count before formal acceptance. Keep an evidence URL and the verification timestamp for every observation. Verify `post_id`, source timestamp/timezone, original text, and views at the public source; do not substitute search snippets or engagement estimates.

Deduplicate only on `post_id`. When observations conflict, prefer the newest verified observation by `observed_at`; retain an older field only if the newer verified observation does not contain it. Never overwrite a verified fact with a candidate fact or silently blend discrepancies. Sort accepted records by `published_at` descending and then `post_id` descending.

### 3. Research in independent, recorded rounds

For every candidate and query, record the search lane, query, timestamp, and decision. Use distinct, relevant queries across these lanes before repeating any lane:

| Lane | Examples of coverage |
| --- | --- |
| Direct topic and spelling variants | countertop dishwasher, compact dishwasher, portable dishwasher, mini dishwasher, desktop dishwasher, table-top dishwasher, “dishwasher for apartment” |
| Brands and products | named compact dishwasher brands/models discovered in results, official product names, and spelling variants |
| Benefits and complaints | installation/no plumbing, water tank, noise, cleaning performance, drying, capacity, leaks, reliability, small kitchen or dorm use |
| Comparisons and alternatives | countertop vs built-in, hand-washing, models/brands compared, apartment or RV alternatives |
| Purchase and sale terms | bought, sale, deal, recommendation, review, unboxing, setup, affiliate/sponsored disclosure |
| Official accounts and announcements | manufacturer, retailer, and product-account releases, demonstrations, promotions, and linked product pages |
| Creators and communities | reviewers, small-space/apartment/RV/home-organization communities, and relevant creator posts |
| Conversation traversal | source posts, quotes, replies, and threads connected to qualifying seeds |

Relationship discovery must be explicit: capture mentions, reply/quote participants, profile links, and official-network links in the Relationship Map. From each qualifying seed, make one bounded hop to its related accounts/posts, logging the relationship edge and traversal depth. Do not extend beyond one hop unless the brief is expanded. Keep searching productive lanes after a phase or lane has been reviewed; an earlier phase ending does not end other lanes.

### 4. Qualify, classify, and cap records

Accept a record only when it is public, within the locked window, materially about a compact countertop dishwasher, has a canonical post identity/source, and has an observed numeric `views > 10000`. Classify post type, relevance tier, stance, disclosure, normalized brand/product, topic tags, and data-quality notes separately from immutable `original_text`.

Posts that are deleted, restricted, unavailable, out of window, irrelevant, duplicate, or missing the required view count go to the appropriate log with the available URL/ID and reason. They must not be counted as verified. Stop accepting new verified records immediately once 80 verified records have been reached; do not relax any criterion to approach the cap.

### 5. Build and verify the new Excel workbook

Use the standalone spreadsheet authoring workflow and create the following seven-sheet `.xlsx` workbook. Create the Posts and every log as Excel Tables with filters and frozen headers. Store timestamps as dates/times, metrics as numbers, and URLs as active hyperlinks. Use formula-, Pivot-, or Power Query-linked dashboard outputs; never paste dashboard totals manually.

Perform compact value/formula inspection, formula-error scanning, link and filter validation, sort verification, and a rendered visual pass over every sheet before export. If public-X access, an export, or credentials needed to obtain public source facts are unavailable, do not fabricate data: deliver the workbook shell/log template, identify the missing access, and document the handoff steps.

## Normalized record contract

Every `PostRecord` contains the required fields below. `null`/blank for an optional metric means unavailable; it never means zero. `original_text` is verbatim and immutable. Analysis/normalization belongs in separate fields.

| Field | Type / rule |
| --- | --- |
| `post_id` | Text identity key; required; canonical X post ID |
| `post_url` | Canonical public post URL; required |
| `published_at` | Typed datetime; required; normalized to the locked timezone while preserving the source instant |
| `timezone` | IANA timezone string; `Asia/Tokyo` for normalized reporting |
| `views` | Numeric observed source value; required for `verified`; must be `> 10000` |
| `likes`, `reposts`, `replies`, `quotes`, `bookmarks` | Numeric when observed; blank/null when unavailable |
| `original_text` | Exact source text; no rewriting, translation, or cleanup |
| `creator_name`, `handle`, `creator_url` | Source identity fields; `creator_url` is a clickable public URL when available |
| `post_type` | Controlled classification, e.g. original, reply, quote, repost |
| `relevance_tier` | Controlled classification, e.g. high/medium/low, justified by evidence |
| `stance` | Controlled analysis label, e.g. positive/negative/mixed/neutral/unclear |
| `disclosure` | Observed disclosure classification, e.g. none_observed/affiliate/sponsored/unclear |
| `summary` | Concise English analytical summary; separate from original text |
| `relevance_evidence` | Why the post is materially in scope |
| `source_post_id`, `source_post_url` | Parent/source-post identity for reply, quote, or thread traversal; blank for an original with none |
| `discovery_lane` | One recorded lane from the research matrix |
| `verification_state` | Explicit state: `candidate`, `verified`, `missing_required_view`, `restricted`, `deleted`, or another logged exclusion state |
| `observed_at` | Typed verification datetime; required for every observation |

The Posts table additionally contains `rank`, `normalized_brand`, `normalized_product`, `topic_tags`, and `data_quality_note`. Keep the post ID as text to avoid Excel precision loss. Maintain a separate candidate/exclusion entry rather than turning a non-verified post into a partial formal record.

## Workbook contract

| Sheet | Required content and linked behavior |
| --- | --- |
| Research Summary | Locked brief, execution window/timezone, strict `views > 10000` criterion, source limitations, verified/candidate/exclusion counts, and a clear no-monitoring statement |
| Posts | All `PostRecord` fields plus rank and normalized-analysis fields; Excel Table, filters, frozen header, active post/creator links, newest-first sort |
| Search & Candidate Log | Candidate ID/URL, query, lane, checked time, decision, and exclusion reason; Excel Table, filters, frozen header |
| Relationship Map | Root post ID, relation type, related post/account ID and URL, evidence, traversal depth, status; Excel Table, filters, frozen header; depth must not exceed one for qualifying seeds |
| Normalization Dictionary | Original term, normalized term, type, evidence post ID, decision, note; Excel Table, filters, frozen header |
| Dashboard | Formula/pivot/query-linked KPIs, trend by week or month, a distribution chart (topic, brand, post type, or stance), and a navigation link to Posts; no manually copied totals |
| Exclusions & Verification Log | ID/URL, status/reason, required-field outcome, public source, observer, timestamp; Excel Table, filters, frozen header |

Dashboard KPIs must reconcile to the Posts table under its data contract. Charts must reference linked data, remain readable in a rendered view, and not display blank/broken ranges. The dashboard link to Posts and every stored post/creator URL must be tested.

## Authorized stopping rule

The research may stop **only** when one of these conditions is true:

1. The user-imposed limit is reached: 80 verified qualifying posts have been accepted.
2. A separately requested target count of verified qualifying records has been reached. This scenario specifies a cap, not a lower target, so this condition does not currently apply.
3. Three consecutive **substantive zero-yield rounds** have occurred. Each such round must use untried, relevant queries and required source/conversation traversal across the research matrix and must yield no new verified qualifying record. Log the queries/traversal and zero result for each of the three rounds.

An exhausted lane, an exhausted set of lanes, lack of a convenient next query, or the end of an arbitrary research phase is **not** an independent stopping condition. It may contribute evidence within a substantive zero-yield round, but cannot replace one. Do not skip still-productive lanes merely because another lane was exhausted. Do not stop after one or two zero-yield rounds, and do not label a round substantive if it only repeats already exhausted work without untried relevant queries/traversal. No threshold, public-access, date, relevance, or cap rule may be relaxed to fill the workbook.

## Validation checklist

- [ ] Brief records global/public-only scope, locked six-month window, `Asia/Tokyo`, `views gt 10000`, cap 80, English output, new workbook, and monitoring disabled.
- [ ] Every verified row has a canonical `post_id` and public URL, an in-window published timestamp, immutable original text, observed timestamp, and numeric views strictly greater than 10,000.
- [ ] Exactly-10,000-view posts and posts without observed views are excluded from verified results and logged with the correct reason.
- [ ] Candidate, verified, and exclusion populations are distinct; duplicates are resolved by `post_id` and conflicts use newest verified `observed_at` without silent blending.
- [ ] Accepted records are sorted by `published_at` descending, then `post_id` descending; no more than 80 are accepted.
- [ ] Queries, discovery lanes, source evidence, candidate decisions, and one-hop relationship traversal are recorded; no traversal exceeds depth one without revised authorization.
- [ ] If stopped before the cap, the log proves three consecutive substantive zero-yield rounds with untried relevant queries and traversal; lane exhaustion alone was not used as a stop reason.
- [ ] Posts and all log sheets are Excel Tables with filters and frozen headers; IDs remain text, timestamps typed, metrics numeric, and post/creator links clickable.
- [ ] Dashboard KPIs, trend, and distribution chart are formula/pivot/query-linked to Posts and reconcile to the table; no manual totals are used.
- [ ] Formula error scan finds no `#REF!`, `#VALUE!`, `#DIV/0!`, `#NAME?`, or unintended `#N/A` errors.
- [ ] Links, table filters, chart source ranges, sort order, and rendered readability of every sheet pass inspection.
- [ ] Any unavailable access/source limitation, restricted/deleted record, uncertainty, or repair need is stated plainly; no data is fabricated and no monitoring/scheduler is created.
</pre>

### Scenario 1 rerun 2

<pre>
# Guided Scenario 1 — Fresh Rerun 2

## Locked research brief

| Field | Value |
| --- | --- |
| Topic | Compact countertop dishwashers |
| Scope | Public X posts only; do not use private, logged-in-only, restricted, or inferred content |
| Locale / languages | Global; search English plus relevant product/model, brand, and locally used-language variants discovered from verified public posts |
| Observation timestamp (`date_end` / as-of) | `2026-08-31T14:34:33+09:00` (`Asia/Tokyo`), captured at execution time |
| Window | The six calendar months ending at the exact observation timestamp: `2026-02-28T14:34:33+09:00` through `2026-08-31T14:34:33+09:00` |
| Inclusion timestamp test | `published_at >= 2026-02-28T14:34:33+09:00` and `published_at <= 2026-08-31T14:34:33+09:00`; convert each source timestamp to `Asia/Tokyo` before comparison |
| Qualification | Observed public `views` must be strictly greater than `10,000` (`gt 10000`); `10,000` exactly does **not** qualify |
| Target / cap | Collect up to 80 verified, deduplicated posts. Fewer is valid only under the stopping rule below. |
| Deliverable | New filterable Excel workbook with a formula-/pivot-/Power Query-linked dashboard |
| Monitoring | Not authorized. Do not create a scheduler, automation, or recurring research task. |

`date_end` is deliberately an observed timestamp, not an end-of-day or forward-rounded value. Because February 2026 has 28 days, six-calendar-month subtraction from August 31 resolves `date_start` to February 28 at the same time and offset.

## Execution plan

1. Create a `ResearchBrief` with the locked fields above and a new-workbook mode. Maintain three separate queues/tables from the outset: candidates, verified records, and exclusions.
2. Run independent discovery lanes in rounds; log every query, its lane, observed time, and result decision. Use direct topic/spelling variants first, then do not retire a productive lane merely because another phase has finished.

   | Lane | Required coverage |
   | --- | --- |
   | Direct topic | `countertop dishwasher`, `compact dishwasher`, `portable dishwasher`, `mini dishwasher`, `tabletop dishwasher`, `small apartment dishwasher`, and hashtag/spelling variants |
   | Brand / product | Publicly surfaced compact models and their manufacturers, model numbers, and retailer/product-name variants; use only evidence-supported additions |
   | Benefits | Space saving, renter/apartment use, installation/no-plumbing, water/energy use, baby-bottle or small-load use, drying, cleaning performance |
   | Complaints | Noise, leaks, capacity, reliability, detergent residue, installation, shipping/returns, customer support |
   | Comparisons / alternatives | Hand-washing, full-size or slimline units, other countertop models, RV/camper use, and purchase alternatives |
   | Purchase / sale | Buying intent, deals, reviews, recommendations, restocks, affiliate/disclosure signals |
   | Official network | Manufacturer and product-account announcements, replies, quotes, linked official profiles, and launches |
   | Creators / communities | Reviewers, appliance/home/renter/RV communities, and accounts explicitly connected by public mention, profile link, reply, or quote |
   | Thread traversal | For qualified seeds, inspect source posts, quote posts, replies, and conversation participants where publicly visible |

3. For every candidate, capture the canonical status URL and ID, the original post text, published timestamp, public view count, engagement metrics when shown, and the source location. Verify those facts on the public source; a search snippet alone is never verification.
4. Apply the inclusion tests in this order: public availability; canonical ID; timestamp inside the locked window; direct topical relevance; observed view count; then strict threshold (`views > 10000`). A missing view count is not zero: mark it `missing_required_view` and exclude it from formal results.
5. For each verified seed, record relationship edges and recurse exactly one hop through explicitly evidenced mentions, replies, quotes, profile links, and official-network links. Search the resulting related account/post only within the same window and qualification rules; do not expand to a second hop.
6. Deduplicate exclusively by `post_id`. Where observations conflict, retain the newest verified observation by `observed_at`; retain an older field only if the newer verified observation lacks it, and expose any conflict in the quality note/log. Never let candidate values overwrite verified values.
7. Continue successive, distinct rounds and traversal. Sort verified records by `published_at` descending and then `post_id` descending. Once complete, construct the workbook, validate it, and clearly disclose access limitations and excluded/unverifiable candidates.

## Normalized record contract

Create the following `ResearchBrief` before collection:

```text
topic: compact countertop dishwashers
locale: global
languages: English plus evidence-supported relevant variants
public_only: true
date_start: 2026-02-28T14:34:33+09:00
date_end: 2026-08-31T14:34:33+09:00
timezone: Asia/Tokyo
qualification_metric: views
qualification_operator: gt
qualification_value: 10000
cap: 80
output_language: English
workbook_mode: new
monitoring_authorized: false
```

Every candidate and verified item uses these required `PostRecord` fields. Numeric engagement fields are numbers when observed and blank/null when unavailable; they are never estimates.

```text
post_id, post_url, published_at, timezone, views, likes, reposts,
replies, quotes, bookmarks, original_text, creator_name, handle,
creator_url, post_type, relevance_tier, stance, disclosure, summary,
relevance_evidence, source_post_id, source_post_url, discovery_lane,
verification_state, observed_at
```

Operational meanings:

- `post_id` is the immutable identity key and is stored as text so Excel cannot round it.
- `post_url` and `creator_url` are canonical, active clickable URLs when available.
- `published_at` is an offset-aware source timestamp retained as a typed date/time where supported; `timezone` records the source/normalized timezone used for the window test.
- `original_text` is verbatim and immutable. Translation, normalization, brand/model extraction, tags, summary, stance, and relevance assessment must be separate fields.
- `post_type` records original, reply, quote, repost, or other source-supported form. `source_post_id` / `source_post_url` preserve the source relationship where applicable.
- `relevance_tier` and `relevance_evidence` state why the post is substantively about a compact countertop dishwasher rather than merely a generic appliance mention.
- `disclosure` records observed sponsorship, affiliate, gifted-product, or other material disclosure; use `none_observed` only when no disclosure is visible, not as proof of independence.
- `verification_state` is one of at least `candidate`, `verified`, `missing_required_view`, `restricted`, or `deleted`. Only `verified` rows can appear in the accepted Posts table.
- `observed_at` is the exact verification time. For conflicts, preserve the newest verified observation and document the discrepancy instead of silently blending values.

The Posts table additionally has `rank`, `normalized_brand`, `normalized_product`, `topic_tags`, and `data_quality_note`. Formal accepted records are sorted newest first by `published_at`, then `post_id` descending.

## Workbook contract

Build a new `.xlsx` with seven sheets, each using an Excel Table where it holds rows. Freeze headers and enable table filters on Posts and every log table. Store post IDs as text, timestamps as typed dates/times, metrics as numeric values, and URLs as live hyperlinks.

| Sheet | Required content and linkage |
| --- | --- |
| Research Summary | Locked brief, exact as-of timestamp/window/timezone, strict threshold, verified count, candidate/exclusion counts, source/access limits, and methodology. Counts link to the tables rather than being manually typed. |
| Posts | Verified `PostRecord` fields plus rank, normalized brand/product, tags, and quality note; table filters, frozen header, canonical URLs, and mandated sort order. |
| Search & Candidate Log | Candidate ID/URL, query, lane, checked time, decision, and exclusion reason; includes candidates not promoted to verified. |
| Relationship Map | Root post ID, relation type, related post/account ID and URL, relationship evidence, traversal depth (0 or 1), and status. |
| Normalization Dictionary | Original term, normalized term, type, evidence post ID, decision, and note. |
| Dashboard | Formula-/pivot-/Power Query-linked KPI cards (verified count, total/median views, and at least one auditable segment measure), a weekly or monthly trend chart, a distribution chart by topic/brand/post type/stance, and a navigation hyperlink to Posts. No manually copied dashboard totals. |
| Exclusions & Verification Log | ID/URL, status/reason, required-field outcome, source, observer, timestamp, plus conflicts/reverification notes. |

Dashboard checks must reconcile to Posts: filtered verified count equals the Dashboard count; its aggregate views and segment totals recalculate from the Posts table; both charts reference linked data; and the Posts navigation link opens the table. Add a visibly stated `Views > 10,000` rule and exact as-of window to Research Summary and Dashboard so downstream users do not mistake the dataset for a live monitor.

## Stopping rule

Stop collection only at the first applicable condition:

1. 80 verified, unique, qualifying posts have been collected; or
2. Three consecutive **substantive zero-yield rounds** have occurred.

A round is substantive only when it exhausts untried relevant queries and required one-hop traversal for its lanes without producing a new verified qualifying record. A round that finds at least one new verified record resets the consecutive zero-yield count to zero. Repeated, duplicate, non-substantive, or untried-lane checks do not count toward the three rounds. Exhausted lanes are inputs to a substantive round, not an independent completion condition: continue every productive, relevant lane and do not stop just because an earlier phase or lane is exhausted. Never relax public-only access, date window, topical relevance, cap, or the strict view threshold to reach 80.

## Validation checklist

- [ ] Reconfirm the actual `date_end` shown in the workbook is `2026-08-31T14:34:33+09:00`, not a future/end-of-day rounding; derive and display the matching `date_start`.
- [ ] Confirm every accepted row is public, canonically identified, within the timestamp window, relevant, and has an observed numeric `views` value greater than 10,000.
- [ ] Confirm exactly-10,000-view and missing-view posts are excluded from accepted Posts and logged with the correct reason/state.
- [ ] Confirm accepted count is at most 80; deduplicate against the whole Posts `post_id` column and resolve observation conflicts by newest verified `observed_at`.
- [ ] Confirm original text was retained verbatim and that analytical/normalized fields are separate.
- [ ] Confirm every required PostRecord field is present; identifiers are text, metrics are numeric, timestamps are typed, and public URLs work.
- [ ] Confirm candidate, verified, restricted/deleted, and missing-view records are distinct and auditable in the logs.
- [ ] Confirm all relationship entries have evidence and depth no greater than one hop.
- [ ] Inspect Excel Table filters, frozen headers, table ranges, formulas/pivots/query links, hyperlinks, number/date formats, sort order, and chart source ranges.
- [ ] Scan for formula errors including `#REF!`, `#VALUE!`, `#DIV/0!`, `#NAME?`, and `#N/A`; reconcile Dashboard KPIs and charts to Posts.
- [ ] Render/open every sheet for visual QA: no clipped headers, unreadable charts, blank default sheets, broken navigation, or dashboard elements outside the usable area.
- [ ] State any unavailable public-source facts or access limitations plainly; do not fabricate rows, metrics, views, or completion claims.
- [ ] Confirm no monitoring, scheduling, automation, credentials, cookies, browser profiles, or research data were written to this repository.

</pre>

The five raw guided outputs are preserved verbatim in these complete
fresh-context scenario fixtures:

1. [Scenario 1 raw output](../.superpowers/sdd/2026-08-31-researching-x-to-excel/guided-scenario-1.md)
2. [Scenario 2 raw output](../.superpowers/sdd/2026-08-31-researching-x-to-excel/guided-scenario-2.md)
3. [Scenario 3 raw output](../.superpowers/sdd/2026-08-31-researching-x-to-excel/guided-scenario-3.md)
4. [Scenario 1 rerun raw output](../.superpowers/sdd/2026-08-31-researching-x-to-excel/guided-scenario-1-rerun.md)
5. [Scenario 1 rerun 2 raw output](../.superpowers/sdd/2026-08-31-researching-x-to-excel/guided-scenario-1-rerun2.md)

No portion of these outputs was normalized, translated, or otherwise altered
for scoring here.

## Scenario 1 — generic consumer product

| Requirement | Pass/Fail | Evidence |
| --- | --- | --- |
| Multi-lane term expansion | Pass | Execution plan step 2 separates direct, brand/product, intent/experience, comparison/alternative, community/creator, and official/conversation lanes. |
| Quote/reply/source traversal | Pass | Steps 2–3 require replies, quote posts, source posts, quoted posts, threads, post type, and source-post linkage. |
| Related-account recursion | Pass | Step 5 restricts explicit-relationship discovery to one hop from a qualifying seed and requires relationship evidence. |
| Strict view/date qualification | Pass | Scope states views gt 10000; steps 1, 3, and 4 require an explicit window and observed views strictly above 10,000. |
| Post-ID deduplication | Pass | Step 6 uses post_id, resolves conflicts by newest verified observed_at, and forbids candidate-over-verified overwrite. |
| No invented metrics | Pass | Steps 3–4 and the record contract permit only observed numeric metrics; missing views are logged, not estimated. |
| Linked Excel dashboard | Pass | The workbook contract requires formula/pivot/Power-Query-linked KPIs and two linked charts. |
| Formula/filter/link/visual QA | Pass | Step 8 and the checklist cover formulas, tables/filters, hyperlinks, charts, source ranges, and rendered visual QA. |
| Natural Japanese; verbatim originals | Pass | Japanese UI is not applicable because the brief does not request Japanese; the scope and record contract explicitly preserve each original post verbatim and select English labels by default. |
| Monitoring authorization boundary | Pass | Scope marks monitoring “Not authorized”; no schedule is proposed. |

### Scenario 1 stopping assessment — Historical failure (resolved by first rerun)

The preserved raw output incorrectly treats “all relevant lanes are exhausted”
as an independent stopping condition (execution-plan step 7 and stopping-rule
item 2). Under `SKILL.md`, exhaustion instead contributes to a substantive
zero-yield round only when no new verified qualifying record is found; it does
not itself complete the research. The raw output remains verbatim; the first
rerun corrects this stopping behavior, so this is a historical failure rather
than an unresolved stopping assessment.

### Scenario 1 first-rerun verdict — Historical failure (resolved by second rerun)

| Requirement | Pass/Fail | Rerun evidence |
| --- | --- | --- |
| Stopping behavior | Pass | “Authorized stopping rule” permits only the 80-record limit, an applicable requested target, or three consecutive substantive zero-yield rounds. It explicitly rejects exhausted lanes/phases as independent conditions and requires untried relevant queries and traversal in each zero-yield round. |
| Multi-lane term expansion | Pass | “Research in independent, recorded rounds” lists direct, brand/product, benefit/complaint, comparison/alternative, purchase/sale, official, creator/community, and conversation lanes. |
| Quote/reply/source traversal | Pass | The conversation lane covers source posts, quotes, replies, and threads; the relationship rule requires logging qualifying-seed traversal. |
| Related-account recursion | Pass | Explicit mentions, reply/quote participants, profile links, and official-network links are logged; qualifying seeds receive one bounded hop only. |
| Strict view/date qualification | Fail | The rerun sets `date_end` to `2026-08-31T23:59:59+09:00` for an execution date, which rounds the window forward rather than using the actual observation/execution timestamp; `date_start` therefore is not derived from that exact timestamp. |
| Post-ID deduplication | Pass | The rerun uses `post_id` only, prefers the newest verified `observed_at`, avoids candidate overwrite, and defines newest-first sorting. |
| No invented metrics | Pass | Missing views stay unavailable and cannot be verified; source facts, not snippets or engagement estimates, are required. |
| Linked Excel dashboard | Pass | The Dashboard is formula/pivot/query-linked to Posts, includes linked KPI/trend/distribution outputs, and forbids copied totals. |
| Formula/filter/link/visual QA | Pass | The workbook contract and checklist require tables, filters, frozen headers, formula-error scans, links, sort checks, and rendered visual inspection. |
| Natural Japanese; verbatim originals | Pass | Japanese UI is not applicable to this English Scenario 1 brief; the rerun explicitly retains original text exactly and puts analysis/normalization in separate fields. |
| Monitoring authorization boundary | Pass | `monitoring_authorized` is false and the rerun prohibits a scheduler, refresh, or recurring monitor. |

The first rerun resolves the demonstrated stopping defect, but fails the exact
date-window requirement. The second rerun resolves that date-window failure;
this first-rerun verdict remains historical evidence and does not alter either
raw output.

### Scenario 1 second-rerun verdict — Pass

| Requirement | Pass/Fail | Second-rerun evidence |
| --- | --- | --- |
| Exact date window | Pass | `date_end`/as-of is the execution-time `2026-08-31T14:34:33+09:00`; `date_start` is the matching six-calendar-month timestamp `2026-02-28T14:34:33+09:00`, and the inclusion test compares against both exact endpoints. |
| Stopping behavior | Pass | Stop conditions are only the 80-record cap or three consecutive substantive zero-yield rounds; exhausted lanes are inputs to a substantive round, never independent completion conditions. |
| Multi-lane term expansion | Pass | The independent-round matrix covers direct, brand/product, benefits, complaints, comparisons/alternatives, purchase/sale, official network, creators/communities, and thread traversal. |
| Quote/reply/source traversal | Pass | Qualified-seed traversal explicitly inspects source posts, quote posts, replies, and conversation participants. |
| Related-account recursion | Pass | Explicitly evidenced mentions, replies, quotes, profile links, and official-network links receive exactly one hop; second-hop expansion is prohibited. |
| Strict view qualification | Pass | Qualification requires an observed public numeric `views > 10000`; exactly 10,000 and missing views are excluded. |
| Post-ID deduplication | Pass | `post_id` is the exclusive identity, with conflicts resolved by the newest verified `observed_at` and no candidate overwrite. |
| No invented metrics | Pass | Search snippets cannot verify a record; unavailable views are `missing_required_view`, engagement is recorded only when observed, and no data is fabricated. |
| Linked Excel dashboard | Pass | The Dashboard uses formula/pivot/Power Query-linked KPIs and charts reconciled to Posts, with no manually copied totals. |
| Formula/filter/link/visual QA | Pass | The workbook contract and checklist require table filters, frozen headers, typed values, live links, formula-error scans, chart/source checks, and rendered visual QA. |
| Natural Japanese; verbatim originals | Pass | Japanese UI is not applicable to this English Scenario 1 brief; original text is explicitly verbatim and analytical/normalized fields remain separate. |
| Monitoring authorization boundary | Pass | Monitoring is not authorized and the checklist prohibits a scheduler, automation, or recurring research task. |

The second rerun passes the exact date-window rule, the stopping rule, and all
Scenario 1 contract items. It resolves the first rerun's historical strict-date
failure without altering either earlier raw output.

Scenario-specific evidence: the output excludes exactly 10,000 views, keeps
unobserved views out of formal records, preserves original-text and analysis
fields separately, limits relationship traversal to one hop, sorts by
published_at then post_id descending. Its stopping assessment is a historical
failure resolved by the first rerun, and the first rerun's strict-date failure
is historical evidence resolved by the second rerun.

## Scenario 2 — Japanese beauty

| Requirement | Pass/Fail | Evidence |
| --- | --- | --- |
| Multi-lane term expansion | Pass | Execution plan steps 2–3 separate direct products/methods, benefits, complaints, comparisons, alternatives, purchase/sale, official, creator/community, and conversation lanes. |
| Quote/reply/source traversal | Pass | Step 4 requires parent posts, quote sources, replies, quoted posts, explicit mentions, profile links, and official-network links. |
| Related-account recursion | Pass | Step 4 records relationship type/evidence/depth and limits related-account exploration to one hop. |
| Strict view/date qualification | Pass | The brief fixes gt 5000; step 5 and the checklist require observed numeric views of 5,001 or more within the JST one-year window. |
| Post-ID deduplication | Pass | Step 6 makes post_id the identity and selects the newest verified observed_at without candidate overwrite. |
| No invented metrics | Pass | Step 5 logs missing view counts as missing_required_view; unavailable/restricted/deleted posts remain outside formal results. |
| Linked Excel dashboard | Pass | Step 7 and the 集計 sheet contract require a Posts-table-linked formula/pivot dashboard with linked trend and distribution charts. |
| Formula/filter/link/visual QA | Pass | The checklist checks formula errors, table ranges, filters, links, numeric cells, chart sources, and rendered sheets. |
| Natural Japanese; verbatim originals | Pass | The brief requires a natural Japanese Excel UI and repeatedly states that original text remains unchanged, with Japanese summaries/analysis in separate fields. |
| Monitoring authorization boundary | Pass | monitoring_authorized is false and the brief explicitly states that no recurring monitoring or automation will be created. |

Scenario-specific evidence: the Japanese classifications (relevance_tier, stance,
and disclosure states) are natural Japanese-explained analytical fields; they
do not alter immutable original text. The plan traverses quote/reply/source
relationships, uses the exact strict threshold, records each relation edge, and
gives the zero-yield stopping rule.

## Scenario 3 — incremental weekly update

| Requirement | Pass/Fail | Evidence |
| --- | --- | --- |
| Multi-lane term expansion | Pass | Step 4 requires direct/spelling, brand/product, benefit/complaint/comparison/alternative/purchase, official, creator/community, and conversation lanes. |
| Quote/reply/source traversal | Pass | Step 4 expressly includes quote, reply, source-post, and thread traversal. |
| Related-account recursion | Pass | Step 4 requires explicit relationship evidence and one-hop traversal from each qualifying seed only. |
| Strict view/date qualification | Pass | Step 3 uses the exact (prior_observed_at, current_observed_at] window; step 6 applies gt/gte literally. |
| Post-ID deduplication | Pass | Step 7 deduplicates candidates and accepted records against the entire existing ID column and resolves conflicts by newest verified observed_at. |
| No invented metrics | Pass | Step 5 uses source-observed metrics only; step 6 logs missing views and never substitutes engagement. |
| Linked Excel dashboard | Pass | Steps 2 and 10 inspect and validate existing dashboard links and chart references; the update contract preserves and extends table-dependent dashboard calculations and chart sources. |
| Formula/filter/link/visual QA | Pass | Steps 1–2 and 8–10 preserve formulas, filters, styles, validations, hyperlinks, dashboard links, charts, and rendered appearance. |
| Natural Japanese; verbatim originals | Pass | Output language is preserved from the existing workbook; the record contract keeps original_text verbatim and separates normalization, translation, and analysis. If that workbook is Japanese, the Japanese beauty preset governs its UI. |
| Monitoring authorization boundary | Pass | The scope says weekly does not authorize a scheduler and requires explicit cadence, scope, destination, and notification preference. |

Scenario-specific evidence: this is an incremental update, not a new workbook
or monitor. It preserves all existing formulas, filters, charts, styles,
hyperlinks, and dashboard structures; reports candidate/new-qualifying counts
even when zero; and inserts only genuinely new verified records in newest-first
order.

## Baseline-gap-to-contract mapping

| Baseline gap | Exact corrective passage | Guided evidence |
| --- | --- | --- |
| Scenario 1 first rerun: exact observation window | [SKILL.md line 14](../SKILL.md#start-with-the-brief): “Set `date_end`/as-of to the actual observation/execution timestamp; never round it forward into future time. Derive `date_start` from that exact timestamp and the requested window.” | The first rerun's `2026-08-31T23:59:59+09:00` end is a historical strict-date failure; the second rerun uses the exact `2026-08-31T14:34:33+09:00` observation timestamp and matching derived start. |
| Scenario 1: related-account recursion | [SKILL.md line 21](../SKILL.md#research-matrix-and-qualification): “Discover related accounts through explicit mentions, reply/quote participants, profile links, and official-network links; recurse one hop from each qualifying seed, then stop unless the brief authorizes a wider depth.” | Scenario 1 step 5 follows that rule. |
| Scenario 1: natural Japanese/verbatim originals | [SKILL.md line 27](../SKILL.md#research-matrix-and-qualification): “Keep verbatim original text immutable: store normalizations, translations, summaries, stance, and analysis in separate fields.” [Japanese beauty preset line 3](../references/japanese-beauty-preset.md): “日本語の自然な見出しを使う（例: `調査概要`、`投稿一覧`、`集計`、`除外・確認ログ`）。原文は `投稿本文（原文）` にそのまま残し、正規化・翻訳・分析メモを別列に置く。” | Scenario 1 keeps the original text verbatim and uses English labels because its brief does not request Japanese; the cited preset supplies the natural-Japanese UI rule when that locale is requested. |
| Scenario 1: monitoring authorization | [SKILL.md line 35](../SKILL.md#delivery-and-updates): “Do not create a recurring monitor, schedule, or automation ... Create one only after explicit authorization that states cadence, scope, destination, and notification preference.” [SKILL.md line 52](../SKILL.md#common-mistakes) reinforces that weekly wording is not authorization. | Scenario 1 declares monitoring unauthorized. |
| Scenario 2: linked dashboard | [Excel deliverable line 10](../references/excel-deliverable.md#excel-deliverable) requires a Dashboard; [line 13](../references/excel-deliverable.md#excel-deliverable) requires Posts-linked KPIs and linked trend/distribution charts. [SKILL.md line 50](../SKILL.md#common-mistakes) rejects an unlinked summary. | Scenario 2 step 7 and its 集計 contract use Posts-linked formulas/pivots and charts. |
| Scenario 2: related-account recursion | [SKILL.md line 21](../SKILL.md#research-matrix-and-qualification): “Discover related accounts through explicit mentions, reply/quote participants, profile links, and official-network links; recurse one hop from each qualifying seed, then stop unless the brief authorizes a wider depth.” | Scenario 2 step 4 records relationship type, evidence, and depth; it explores only one hop from each qualifying seed. |
| Scenario 2: monitoring authorization | [SKILL.md line 35](../SKILL.md#delivery-and-updates) and [data contract line 11](../references/data-contract.md#data-contract) require explicit authorization and otherwise set monitoring_authorized false. | Scenario 2 sets it false and prohibits automation. |
| Scenario 3: quote/reply/source traversal | [SKILL.md line 21](../SKILL.md#research-matrix-and-qualification) requires quote, reply, source-post, and thread traversal. | Scenario 3 step 4 lists all four. |
| Scenario 3: related-account recursion | [SKILL.md line 21](../SKILL.md#research-matrix-and-qualification) sets evidence-based, bounded one-hop related-account traversal; [line 49](../SKILL.md#common-mistakes) requires a relationship edge. | Scenario 3 step 4 uses explicit evidence and one hop. |
| Scenario 3: linked dashboard | [Excel deliverable line 13](../references/excel-deliverable.md#excel-deliverable) requires linked KPI/chart data; [SKILL.md line 33](../SKILL.md#delivery-and-updates) requires dashboard-link and chart inspection before delivery. | Scenario 3 steps 2 and 10 inspect/validate dashboard links and charts; its update contract preserves and extends linked structures. |
| Scenario 3: Japanese/verbatim-original safeguards | [SKILL.md line 27](../SKILL.md#research-matrix-and-qualification) makes original text immutable and separates analysis; [line 44](../SKILL.md#quick-reference) requires natural Japanese labels for Japanese beauty work; [data contract line 27](../references/data-contract.md#data-contract) preserves original_text exactly. | Scenario 3 preserves existing output language and declares immutable original_text; Japanese beauty updates additionally use the preset. |

## Refactor decision

The original Scenario 1 raw output remains a historical stopping-rule failure:
it treats exhausted lanes as a standalone completion condition. The first
rerun resolves that failure, but its `2026-08-31T23:59:59+09:00` end remains a
historical strict-date failure. The second rerun uses the exact
`2026-08-31T14:34:33+09:00` observation timestamp and matching derived start,
passing both the observation-window and stopping rules with all Scenario 1
contract items. All three raw outputs remain verbatim evidence.
