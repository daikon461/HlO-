# Hardcore Loot Overhaul v0.2 検証版

v0.1の250件のGlobal Loot Modifierを維持しつつ、難易度別の追加報酬プールを付加します。既存戦利品を上書きしません。

- low: 13%で追加抽選
- mid: 21%で追加抽選
- high: 29%で追加抽選
- highのみ0.8%で大当たり抽選

設定値は `loot_balance.json` を変更してビルド時に反映されます（ゲーム内configではありません）。分類はテーブル名に基づく暫定ルールです。

## GitHub

ZIPを解凍して中身をリポジトリ直下へアップロード。`.github/workflows/build.yml` を更新すること。Actionsでビルド後、ArtifactsからJARを取得します。

## 注意

現段階の追加報酬はバニラアイテムのみです。MODアイテムの登録ID・依存MOD不在時の挙動を確実に検証してから拡張します。Minecraftでの起動と報酬生成はv0.2として未検証です。既存のv0.1 JARは外してから導入してください。
