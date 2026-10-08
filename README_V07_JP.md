# Hardcore Loot Overhaul v0.7 — Simply Swords / Simply More 安全連携版

## 確認できたこと
Simply More 1.3.0 alpha5 の `LootRegistry.register()` は、複数のユニーク武器を Simply Swords の `SimplySwordsAPI.registerUniqueLoot(item, 1)` に登録しています。JARのバイトコードで確認しました。武器名の一覧は `SIMPLY_MORE_VERIFIED_REGISTRATIONS.txt` に収録。

## 安全な連携方針
- Simply Swords / Simply Moreのユニーク武器をHLOから直接追加しません。元MODの抽選・覚醒・救済システムを使用します。
- `miracle_v05.json` の `unique_weapons.enabled` は引き続き `false` とします（ここを `true` にするだけでは連携できません）。
- 既存のv0.6の通常戦利品、MOD報酬、奇跡の戦利品は維持。
- Simply Swordsの `config/simplyswords/loot.toml` をゲーム起動後に確認し、ユニーク抽選対象チェストや確率を調整してください。ファイル名・項目名は環境の実物を優先してください。
- 元MOD側で抽選対象外の構造物を追加したい場合、Simply Swords側の設定・APIの仕様を先に確認します。

## テスト
Simply Swords 1.70.2 のコマンドが利用可能なら、`/simplyswords loot_test minecraft:chests/ancient_city 1000` と `/simplyswords pity status` を試してください。コマンドが存在しない場合はゲーム内の候補を確認してください。

## 制限
これは既存のSimply Swords抽選を活用する互換性改善版で、HLO独自のユニーク武器抽選を新規有効化する版ではありません。ビルド・ゲーム内起動は未検証です。
