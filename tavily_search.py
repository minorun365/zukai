import os
from typing import List, Dict, Any
from tavily import TavilyClient
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class TavilySearch:
    def __init__(self):
        # Streamlit secretsを優先、なければ環境変数を使用
        api_key = st.secrets.get('TAVILY_API_KEY', os.getenv('TAVILY_API_KEY'))
        if not api_key:
            raise ValueError("TAVILY_API_KEYが設定されていません")
        self.client = TavilyClient(api_key=api_key)
    
    def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Tavilyを使用してWeb検索を実行（精度向上設定）"""
        try:
            response = self.client.search(
                query=query,
                topic="general",  # generalトピックで幅広い情報を取得
                search_depth="advanced",  # 詳細な検索（2クレジット使用）
                max_results=max_results,  # デフォルトを10に増加
                include_answer=True,  # AI生成の回答を含める
                include_raw_content=True,  # 完全なWebページコンテンツを取得
                include_images=False,  # 画像は不要（テキスト重視）
                chunks_per_source=3,  # ソースあたり3チャンクを取得（最大）
                time_range=None,  # 時間制限なし（最新＋過去の情報）
                include_domains=[],  # 特定ドメイン指定なし
                exclude_domains=[
                    "pinterest.com",  # 画像サイトを除外
                    "instagram.com",
                    "tiktok.com",
                    "youtube.com"  # 動画サイトを除外（テキスト情報重視）
                ]
            )
            
            results = []
            
            # 検索結果を整形（詳細情報を含む）
            for result in response.get('results', []):
                # より詳細なコンテンツを取得
                content = result.get('content', '')
                raw_content = result.get('raw_content', '')
                
                # raw_contentがある場合はより詳細な情報を使用
                if raw_content and len(raw_content) > len(content):
                    content = raw_content[:2000]  # 2000文字まで
                
                results.append({
                    'title': result.get('title', ''),
                    'content': content,
                    'url': result.get('url', ''),
                    'score': result.get('score', 0),
                    'published_date': result.get('published_date', ''),  # 公開日を追加
                    'domain': result.get('url', '').split('/')[2] if result.get('url') else ''  # ドメイン情報
                })
            
            # スコアでソート（関連性の高い順）
            results.sort(key=lambda x: x['score'], reverse=True)
            
            # AI生成サマリーを先頭に追加
            if response.get('answer'):
                results.insert(0, {
                    'title': '🤖 AI生成サマリー',
                    'content': response['answer'],
                    'url': '',
                    'score': 1.0,
                    'published_date': '',
                    'domain': 'AI Generated'
                })
            
            return results
            
        except Exception as e:
            print(f"検索エラー: {str(e)}")
            return [{
                'title': 'エラー',
                'content': f'検索中にエラーが発生しました: {str(e)}',
                'url': '',
                'score': 0
            }]
    
    def format_results_for_display(self, results: List[Dict[str, Any]]) -> str:
        """検索結果を表示用にフォーマット"""
        formatted = []
        for i, result in enumerate(results):
            if result['url']:
                formatted.append(f"### {i+1}. {result['title']}\n{result['content'][:200]}...\n[詳細]({result['url']})")
            else:
                formatted.append(f"### {result['title']}\n{result['content']}")
        
        return "\n\n".join(formatted)