# Hardcore Loot Overhaul v0.8 — 構造物戦利品の追加拡張

- v0.7の250対象に、解析済みMODの戦利品テーブル40件を追加（`extra_targets_v08.csv`）。
- 追加分は既存テーブルを置換しない `neoforge:add_table` を使用。
- 追加分はバニラ報酬と0.1%の奇跡抽選。MODアイテム報酬は既存250件の設定を維持。
- `expansion_v08.json` で追加40件の抽選率をビルド前に変更可能。
- Simply Swords / Simply More のユニーク武器は独自挿入しない。公式の抽選・覚醒・pityシステムを維持。
- 40件はJAR内に実在する戦利品テーブルIDを抽出したものだが、構造物で実際に使用されるかはゲーム内検証が必要。

## ビルド
GitHubへZIPの中身をアップロードし、Actionsの `Build Hardcore Loot Overhaul` を実行。
ビルド前に `generate_loot_data.py` → `upgrade_v04.py` → `upgrade_v05.py` → `validate_v06.py` → `expand_v08.py` を実行する。
旧版JARと同時に導入しないこと。

## 動作確認
Minecraft 1.21.1 NeoForgeの新規テストワールドで、追加対象のテーブルIDを `extra_targets_v08.csv` から選び、`/loot give @s loot <ID>` を繰り返して検証。
Simply Swordsの対象テーブル確認には `/simplyswords loot_test <ID> 1000` を利用可能なら使用。

注意: GitHub Actionsビルド・実ゲーム起動は未検証。
