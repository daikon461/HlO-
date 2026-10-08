# Hardcore Loot Overhaul v0.3 — MOD報酬追加版

GitHub Actionsで `generate_loot_data.py` → `upgrade_v02.py` → `upgrade_v03.py` を実行してJARを生成します。

Create、Iron’s Spells、Ars Nouveau、CataclysmのJAR内loot tableに登場したアイテムID（Createのみアイテムモデル由来の候補）を報酬に追加します。実際のレジストリ登録はゲーム内で要確認です。

**重要：** `mod_rewards.json` の `enabled: true` は4つのMODがすべて入ったMODパック向けです。いずれかを外す場合は `enabled: false` に変更してからビルドしてください。存在しないアイテム参照の動作は保証できません。

追加報酬の確率は low=4.5%、mid=9.5%、high=14%。v0.2のバニラ追加抽選とは独立しています。既存戦利品の上書きは行いません。

**注意：** このZIPはGitHub Actionsビルド未検証。v0.2のJARと同時に導入しないでください。
