# Hardcore Loot Overhaul v1.0 RC1（完成候補・検証版）

Minecraft 1.21.1 / NeoForge 21.1.209 / Java 21

## この版について
v0.8の290件の戦利品拡張を保持し、生成後のJSON、GLM参照、重複対象をGitHub Actionsで自動検査します。
**完成版の動作保証ではありません。** GitHubでのビルド、Minecraftクライアント・専用サーバーでの実機テストが必要です。

## GitHubへの導入
ZIPを展開し、`.github` を含めてリポジトリのルートにアップロード。既存の古いファイルは残さず置き換えてください。
Actionsの Build Hardcore Loot Overhaul を実行。ArtifactsからJARを入手してください。
古いHLOのJARを削除し、新しいJARを一つだけmodsに入れてください。

## 現時点の仕様と制約
- 既存の戦利品テーブルを直接置換せず、NeoForge Global Loot Modifierで追加します。
- 既存のSimply Swords / Simply Moreの独自ユニーク武器抽選は変更しません。
- HLO独自のユニーク武器追加抽選は未実装です。元MODの覚醒・救済処理を保証できないためです。
- 確率は同梱JSONと生成スクリプトで設定し、変更には再ビルドが必要です。ゲーム起動中の設定ファイルによる調整は未実装です。
- 290対象テーブルの全てをゲーム内で検証したわけではありません。

## 実機テスト
1. Mods一覧にHLOが一つだけあるか確認。
2. `/loot give @s loot minecraft:chests/abandoned_mineshaft` などを20回程度試す。
3. MOD追加ダンジョンの未開封チェストで追加報酬・既存報酬を確認。
4. Simply Swords / Moreの通常ユニーク抽選に異常がないか確認。
5. 専用サーバーで起動・戦利品生成・ログを確認。

## 今後の正式版に必要な条件
設定ファイル対応、ユニーク武器の安全な連携方法の確認、専用サーバー検証、複数MOD構成での競合検証。
