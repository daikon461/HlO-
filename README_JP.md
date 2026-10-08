# Hardcore Loot Overhaul v0.1.0（検証用ソース）
Minecraft 1.21.1 / NeoForge 21.1.x / Java 21。

- 既存戦利品を置き換えず、NeoForge標準の `neoforge:add_table` で追加。
- 実在を確認できたMODのチェストテーブルIDとバニラIDのみを対象とする。
- 追加アイテムは現時点ではバニラのみ。MOD独自アイテムIDの検証後に拡張。
- 出現率は暫定値。設定ファイルからの変更は未実装。
- ビルドとゲーム内起動は未検証。GitHub ActionsのBuildワークフローで確認。
- 対象テーブル数: 250（序盤 50、中盤 175、高難度 25）

GitHubリポジトリのルートにこのZIPの中身を配置し、Actions > Build Hardcore Loot Overhaul > Run workflow。
※ Gradle依存解決とコンパイルの成功は未確認です。失敗したらActionsログを共有してください。
