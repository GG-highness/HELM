# HELM — Holistic Effect & Level Meter

HELMは、カードの効果と強さを総合的に計測するアプリです。
新しいカードの強さを評価し環境のバランスを保ちながら長期的にサービスをグロースすることを支援するツールです。
ワンピースカードゲームの舵取りをしていくことをイメージし「舵」を意味する英単語をアプリケーション名に選択しました。

カードゲームの開発現場では、新しいカードの強さを評価する客観的な尺度がなく、バランス調整が属人的な判断に依存しているという仮説からこのアプリケーションを作成することに決めました。
HELMは、カードの効果テキストをルールベースで分解・数値化し、既存カードとの比較や環境全体への影響をシミュレーションすることで、発売前のカードのバランス予測を支援します。

## 機能一覧

### 1. カード企画入力 + 偏差値スコア
企画中のカードのパラメータ（コスト、パワー、効果テキストなど）を入力すると、効果テキストをルールベースで原子効果に分解し、同コスト帯の既存カードと比較した偏差値を算出します。偏差値が高すぎる場合は警告と調整提案を表示します。

### 2. 対戦記録 + 戦績集計
開発チームが実カードで対戦した結果を記録し、デッキ別・マッチアップ別の勝率を自動集計します。企画カードを含むデッキの実戦データを蓄積できます。

### 3. 環境影響予測
企画カードを環境に投入した場合のTier表変動を予測します。既存デッキとの相性マトリクスを算出し、環境の偏りを数値化します。パラメータ変更時の影響もシミュレーションできます。

### 4. 分析レポート
対戦記録と環境影響予測のデータを統合し、予測精度を検証します。予測と実データの乖離を可視化し、スコアリングパラメータの改善に活用します。

## 使用技術

| レイヤー | 技術 |
|---------|------|
| フロントエンド | Next.js (App Router) + React + TypeScript |
| CSS | Tailwind CSS |
| 状態管理 | Zustand |
| バックエンド | Python + FastAPI |
| ORM | SQLAlchemy |
| DB | MySQL |
| スコアリング | ルールベース（正規表現 + キーワードマッチング + ポイント加算） |
| API方式 | REST API |
| テスト | pytest（バックエンド）/ Vitest + React Testing Library（フロントエンド） |

## 環境構築

### 前提条件
- Docker Desktop または Rancher Desktop がインストールされていること
- VS Code + [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) がインストールされていること

### Dev Containers を使った起動（推奨）

**1. リポジトリをクローン**
```bash
git clone https://github.com/GG-highness/HELM.git
cd HELM
```

**2. VS Code で開く**
```bash
code .
```

**3. Dev Container で開き直す**

`Ctrl+Shift+P` → `Dev Containers: Reopen in Container`

VS Code が自動的に Docker コンテナをビルドし、backend コンテナに接続します。

**4. マイグレーション実行**
```bash
cd /app && alembic upgrade head
```

### Dev Containers の構成について

`.devcontainer/devcontainer.json` の設定：

- **接続先コンテナ**: backend（`docker-compose.yml` の `backend` サービス）
- **workspaceFolder**: `/workspace`（モノレポルート）
- **理由**: `docker-compose.yml` に `.:/workspace` のボリュームマウントがあるため、Dev Containers がモノレポルートを `/workspace` として認識する。`workspaceFolder` を `/app`（backendのみ）に設定しても `/workspace` が優先されるため、`/workspace` に統一している
- **効果**: VS Code のエクスプローラーから `frontend/` と `backend/` の両方を編集できる

### Docker Compose のみで起動する場合

```bash
docker compose up --build
```

### 動作確認
- フロントエンド: http://localhost:3000
- バックエンド Swagger UI: http://localhost:8000/docs
- ヘルスチェック: http://localhost:8000/api/health