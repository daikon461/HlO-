# Hardcore Loot Overhaul v0.6 — Simply Swords / Simply More 互換性監査版

対象：Simply Swords 1.70.2 (NeoForge 1.21.1)、Simply More 1.3.0 alpha5 (NeoForge 1.21.1)。両JARを読み取り、モデル候補一覧を同梱しました。**モデル名は登録アイテムIDの証明ではありません**。

- v0.5の250対象テーブル、MOD報酬、奇跡報酬は維持。
- `validate_v06.py` で250個の生成テーブルを検証し、未検証のSimply Swords/Simply Moreアイテムの直接挿入を拒否。
- 両MODのユニーク武器専用ロジック（覚醒・救済抽選等）の動作を解析・検証するまでは、追加抽選は無効のまま。
- これは**ユニーク武器追加完成版ではありません**。既存の両MODが自前で生成するユニーク武器の処理を変更しません。
- GitHub Actionsでビルド可能な構成。実際のMinecraft起動確認は未実施。

次の段階：専用レジストリ・抽選コードの逆解析と、MOD本来の生成方法を利用した安全な連携実装。
