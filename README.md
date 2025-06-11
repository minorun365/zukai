# 🔍 スーパー図解くん

キーワードを入力すると、Web検索して雑誌のように見やすく解説するStreamlitアプリです！

## 🌟 特徴

- **AWS Bedrock**: Claude 3.5 Sonnet v2 / Claude Sonnet 4を使用
- **Tavily Search**: 高精度なWeb検索機能
- **雑誌風レイアウト**: 美しいHTML生成で見やすい図解
- **レスポンシブデザイン**: モバイル対応
- **Streamlit Cloud**: 簡単デプロイ

## 🚀 クイックスタート

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourusername/zukai.git
cd zukai
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. 認証情報の設定

`.streamlit/secrets.toml`ファイルを作成して、以下の情報を設定してください：

```toml
[default]
AWS_ACCESS_KEY_ID = "your_aws_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_aws_secret_access_key"
AWS_DEFAULT_REGION = "us-east-1"
TAVILY_API_KEY = "your_tavily_api_key"
USE_CLAUDE_4 = false
```

### 4. アプリの実行

```bash
streamlit run app.py
```

## 🔧 設定

### AWS Bedrock

1. AWS CLIでの認証設定、または
2. `.streamlit/secrets.toml`でのクレデンシャル設定

**必要な権限:**
- `bedrock:InvokeModel`
- `bedrock:Converse`

### Tavily Search API

[Tavily](https://tavily.com/)でAPIキーを取得してください。

### Claude 4使用時の注意

Claude Sonnet 4を使用する場合は：
- `USE_CLAUDE_4 = true`に設定
- US Cross-Region Inference Profileが必要
- より高精度な図解生成が可能

## 📁 プロジェクト構造

```
zukai/
├── app.py                  # メインのStreamlitアプリ
├── bedrock_client.py       # AWS Bedrock接続
├── tavily_search.py        # Web検索機能
├── html_generator.py       # HTML生成・スタイリング
├── requirements.txt        # Python依存関係
├── .streamlit/
│   ├── config.toml        # Streamlit設定
│   └── secrets.toml       # 認証情報（gitignore対象）
└── .gitignore
```

## 🎨 使い方

1. アプリを起動
2. 調べたいキーワードを入力
3. 「図解」ボタンをクリック
4. 美しい図解レイアウトで結果を確認

## 🌐 Streamlit Cloudでのデプロイ

1. GitHubリポジトリをStreamlit Cloudに接続
2. Secretsページで認証情報を設定：
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`
   - `TAVILY_API_KEY`
   - `USE_CLAUDE_4`

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します！

## 📄 ライセンス

MIT License

## 🙏 謝辞

- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [Tavily Search](https://tavily.com/)
- [Streamlit](https://streamlit.io/)