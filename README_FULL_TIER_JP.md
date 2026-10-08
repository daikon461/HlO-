# Hardcore Loot Overhaul v1.1 Beta 2 — 全報酬ワールドティア連動

Minecraft 1.21.1 / NeoForge 21.1.209 / Apotheosis 8.8.0以上。

## 変更点
- 構造物別の6段階難易度を維持。
- HLO独自の報酬プールすべてにApotheosisワールドティア条件を設定。
- 報酬プール内のランダム抽選確率を Haven 0.55倍 / Frontier 0.8倍 / Ascent 1.0倍 / Summit 1.3倍 / Pinnacle 1.65倍で補正（最大95%）。
- HLOが `minecraft:set_enchantments` で直接指定するエンチャントレベルを Haven 0.75倍 / Frontier 0.9倍 / Ascent 1.0倍 / Summit 1.2倍 / Pinnacle 1.4倍で補正（整数に丸め、1〜255）。
- アフィックス装備と宝石の追加抽選は前版のワールドティア連動を継承。

## 注意
- **試験版**。GitHub Actionsでのビルド、実機でのApotheosis条件評価は未確認。
- Apotheosisのワールドティア条件が利用できないコンテキスト（例: /loot コマンドの一部）ではHLOの追加報酬が出ない可能性があります。
- 全プールを5分岐に展開するため、生成リソースとJARが大きくなります。
- アイテム数量、固定装備の種類、Apotheosisが独自生成するアフィックス性能そのものはHLO側で変更しません。
- 既存のチェストには遡及適用されません。新しく生成されるチェストで検証してください。
