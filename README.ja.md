# Whoogle Search MCP

[![Docker Hub](https://img.shields.io/badge/Docker-hdh0926%2Fwhoogle--search--mcp-blue)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp)
[![Docker Version](https://img.shields.io/docker/v/hdh0926/whoogle-search-mcp?sort=semver)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp/tags)
[![Docker Pulls](https://img.shields.io/docker/pulls/hdh0926/whoogle-search-mcp)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp)
[![Image Size (latest)](https://img.shields.io/docker/image-size/hdh0926/whoogle-search-mcp/latest)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp/tags)
[![Build and Push (Release Only)](https://github.com/Fhwang0926/whoogle-search-mcp/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Fhwang0926/whoogle-search-mcp/actions/workflows/docker-build.yml)

Open WebUI統合のために特別に設計されたWhoogle検索エンジンと連携するFastAPIベースの検索プロキシサーバーです。

## 概要

このプロジェクトは、Open WebUIおよびその他のAIチャットアプリケーションで検索機能が必要な場合のために設計されたWhoogle検索エンジンのREST APIラッパーです。検索結果を一貫した形式で正規化し、Open WebUIの検索機能とシームレスに統合されるクリーンなAPIインターフェースを提供します。

### Open WebUI統合

このサービスはOpen WebUIのための**検索プロキシ**として機能し、ユーザーが以下を可能にします：
- Whoogle（プライバシー重視のGoogle検索代替）を通じたウェブ検索の実行
- AI会話でリアルタイム検索結果の受信
- ウェブ情報にアクセスしながらプライバシーを維持
- Googleに個人データを露出することなく検索機能を使用

## 主な機能

- 🔍 **Open WebUI統合**: Open WebUIで検索ツールとしてシームレスに統合
- 🚀 **FastAPIバックエンド**: 高性能非同期ウェブフレームワーク
- 📊 **正規化された結果**: AIチャットインターフェースと互換性のある一貫したJSONレスポンス形式
- 🔒 **プライバシー重視**: Whoogle（プライバシー重視のGoogle検索代替）を使用
- 🐳 **Dockerサポート**: DockerおよびDocker Composeによる簡単なデプロイ
- ⚙️ **設定可能**: 柔軟なデプロイのための環境ベース設定
- 🌐 **リアルタイム検索**: AI会話でライブウェブ検索結果を提供

## APIエンドポイント

### GET /search

Whoogleを通じて検索クエリを実行し、正規化された結果を返します。

**パラメータ:**
- `q` または `query`: 検索クエリ文字列（必須）

**レスポンス形式:**
```json
{
  "query": "検索語",
  "number_of_results": 10,
  "results": [
    {
      "url": "https://example.com",
      "title": "例のタイトル",
      "content": "例の説明",
      "img_src": "https://example.com/image.jpg",
      "engine": "whoogle",
      "category": "general"
    }
  ],
  "answers": [],
  "infoboxes": []
}
```

## インストール

### 事前ビルドされたDockerイメージを使用（推奨）

最新のDockerイメージはすべてのリリースで自動的にビルドされ、Docker Hubにプッシュされます：

```bash
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 your-username/whoogle-search-mcp:latest
```

### ソースからビルド

1. リポジトリをクローン：
```bash
git clone https://github.com/your-username/whoogle-search-mcp.git
cd whoogle-search-mcp
```

2. Dockerでビルドおよび実行：
```bash
docker build -t whoogle-search-mcp .
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 whoogle-search-mcp
```

### ローカル開発

1. 依存関係をインストール：
```bash
pip install -r requirements.txt
```

2. 環境変数を設定：
```bash
export WHOOGLE_BASE_URL=http://localhost:5000
```

3. アプリケーションを実行：
```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Open WebUI設定

### Open WebUIで検索プロキシを設定

1. **このサービスをDockerまたはローカルでデプロイ**
2. **Open WebUIをこのサービスを検索プロキシとして使用するように設定**：
   - Open WebUI設定に移動
   - 「ツール」または「検索」セクションに移動
   - 以下の構成で新しい検索ツールを追加：
     - **名前**: Whoogle検索
     - **URL**: `http://your-server:8080/search`
     - **方法**: GET
     - **パラメータ**: `q`（クエリパラメータ）

### 環境変数

- `WHOOGLE_BASE_URL`: WhoogleインスタンスのURL（デフォルト: `http://whoogle:5000`）

### 設定ファイル

`env.sample`を`.env`にコピーし、必要に応じて値を変更してください：

```bash
cp env.sample .env
```

`env.sample`ファイルの内容：
```bash
# Whoogle Search MCP Server Configuration

# Whoogle server url
# デフォルト: http://whoogle:5000
WHOOGLE_BASE_URL=http://whoogle:5000

# 例:
# WHOOGLE_BASE_URL=http://localhost:5000
# WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### 設定例

```bash
# ローカル開発用
WHOOGLE_BASE_URL=http://localhost:5000

# プロダクション用
WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### Docker Compose例（Open WebUIと一緒に）

```yaml
version: '3.8'
services:
  whoogle-search-mcp:
    image: your-username/whoogle-search-mcp:latest
    ports:
      - "8080:8080"
    environment:
      - WHOOGLE_BASE_URL=http://whoogle:5000
    depends_on:
      - whoogle

  whoogle:
    image: benbusby/whoogle-search:latest
    ports:
      - "5000:5000"

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OPENAI_API_BASE_URL=http://your-llm-server:8000/v1
```

## 使用例

### 基本的な検索
```bash
curl "http://localhost:8080/search?q=Pythonプログラミング"
```

### クエリパラメータを使用
```bash
curl "http://localhost:8080/search?query=機械学習"
```

## 開発

### プロジェクト構造
```
whoogle-search-mcp/
├── app.py                    # メインFastAPIアプリケーション
├── requirements.txt          # Python依存関係
├── Dockerfile               # Docker構成
├── env.sample               # 環境変数テンプレート
├── README.md                # 英語ドキュメント
├── README.ko.md             # 韓国語ドキュメント
├── README.ja.md             # 日本語ドキュメント
├── README.zh.md             # 中国語ドキュメント
├── LICENSE                  # MITライセンス
└── .github/
    └── workflows/
        └── docker-build.yml # Docker Hub用GitHub Actions
```

### 依存関係
- **FastAPI**: API構築のためのウェブフレームワーク
- **httpx**: Whoogleにリクエストを送信するための非同期HTTPクライアント
- **uvicorn**: アプリケーション実行のためのASGIサーバー

### CI/CDパイプライン
- **GitHub Actions**: Docker Hubへの自動Dockerイメージビルドおよびプッシュ
- **マルチプラットフォームサポート**: linux/amd64およびlinux/arm64アーキテクチャ用ビルド
- **自動タグ付け**: ブランチ、バージョン、および最新リリース用タグ生成

## ライセンス

このプロジェクトはMITライセンスの下にあります。詳細については[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

1. リポジトリをフォーク
2. 機能ブランチを作成
3. 変更を適用
4. プルリクエストを提出

## 要件

- Python 3.11+
- 実行中のWhoogleインスタンスへのアクセス
- Docker（オプション、コンテナ化されたデプロイ用）
