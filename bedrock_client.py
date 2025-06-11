import os
import json
import boto3
from typing import Dict, Any, List
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class BedrockClient:
    def __init__(self):
        # Streamlit secretsから認証情報を取得
        aws_region = st.secrets['AWS_REGION']
        aws_access_key_id = st.secrets['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = st.secrets['AWS_SECRET_ACCESS_KEY']
        
        # boto3設定でタイムアウトを延長
        from botocore.config import Config
        
        config = Config(
            read_timeout=120,  # 2分
            connect_timeout=60,  # 1分
            retries={
                'max_attempts': 3,
                'mode': 'adaptive'
            }
        )
        
        self.client = boto3.client(
            service_name='bedrock-runtime',
            region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            config=config
        )
        
        # モデル選択: Claude 4 (USクロスリージョン) または Claude 3.5 v2
        use_claude_4 = st.secrets.get('USE_CLAUDE_4', False)
        
        if use_claude_4:
            self.model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0"  # USクロスリージョン推論
        else:
            self.model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"  # Claude 3.5 v2
    
    def generate_content(self, query: str, search_results: List[Dict[str, Any]]) -> str:
        """検索結果を基に図解コンテンツを生成（Converse API使用）"""
        
        system_prompt = """あなたは「スーパー図解くん」です。
ユーザーが調べたいキーワードについて、Web検索結果を基に、
雑誌のような見やすいHTMLレイアウトで分かりやすく解説します。

以下のルールに従ってください：
1. 検索結果の情報を整理して、視覚的に分かりやすく構成する
2. 重要なポイントは強調表示する
3. セクションごとに適切な見出しをつける
4. 箇条書きや表を効果的に使う
5. 専門用語は初心者にも分かるように説明する
6. HTMLとCSSを使って雑誌風のレイアウトを作成する
7. レスポンシブデザインを意識する
8. HTMLコードのみを出力し、説明文やコメントは一切含めない"""

        search_context = "\n\n".join([
            f"【検索結果 {i+1}】\nタイトル: {result.get('title', '')}\n内容: {result.get('content', '')}\nURL: {result.get('url', '')}"
            for i, result in enumerate(search_results)
        ])

        user_message = f"""キーワード「{query}」について、以下の検索結果を基に分かりやすく解説してください。

{search_context}

HTMLとCSSを使って、雑誌のような見やすいレイアウトで解説を作成してください。
回答はHTMLコードのみで、説明や前置きは不要です。"""

        try:
            # Converse APIを使用
            response = self.client.converse(
                modelId=self.model_id,
                system=[{"text": system_prompt}],
                messages=[
                    {
                        "role": "user",
                        "content": [{"text": user_message}]
                    }
                ],
                inferenceConfig={
                    "maxTokens": 4000,
                    "temperature": 0.7
                }
            )
            
            # レスポンスから内容を取得
            return response['output']['message']['content'][0]['text']
            
        except Exception as e:
            error_msg = f"Bedrock Converse APIエラー: {type(e).__name__}: {str(e)}"
            print(error_msg)  # デバッグ用
            raise Exception(error_msg)