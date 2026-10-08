# Hardcore Loot Overhaul v1.0.0 正式版ソース

Minecraft 1.21.1 / NeoForge 21.1.209 / Java 21 / Apotheosis 8.8.0 以降

## 主な機能
- 既存のチェスト戦利品を維持した追加報酬システム
- 6段階の報酬バランス、豪華報酬、奇跡の戦利品
- 高レベルエンチャント装備、秘宝、プレミアム装備
- Apotheosisの既存 `apotheosis:affix_loot` と `apotheosis:gems` の形式による追加抽選
- Simply Swords / Simply More の独自ユニーク武器抽選には介入しない

## GitHubでビルド
1. ZIPを展開し、全ファイルと `.github` フォルダをリポジトリにアップロード。
2. Actions → Build Hardcore Loot Overhaul を実行。
3. 成功したら Artifacts からJARをダウンロード。
4. 旧バージョンのHLO JARを取り除き、Apotheosis 8.8.0とその依存MODが入ったテスト環境で確認。

## 検証範囲
ソース生成・JSON検証・Apotheosis 8.8.0内蔵JSONとの構造照合を実施。
**GitHub上のJARビルド成功・Minecraft起動・専用サーバーでの動作は未検証。**
実機テスト完了まで、配布前の正式版候補として扱ってください。

## 注意
- Apotheosis標準の戦利品抽選に加えて独立した追加抽選を行うため、同じチェストに複数の装備や宝石が出る可能性があります。
- 確率はソース内の設定JSONで変更後、再ビルドが必要です。ゲーム内設定画面はありません。
- このZIPには第三者のMOD JARを含みません。
