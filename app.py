import streamlit as st
import streamlit.components.v1 as components
from tavily_search import TavilySearch
from bedrock_client import BedrockClient
from html_generator import HTMLGenerator
import time

# ページ設定
st.set_page_config(
    page_title="スーパー図解くん",
    page_icon="🪄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# セッション状態の初期化
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# タイトルとヘッダー
st.markdown("""
<style>
    .title-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem 2.5rem;
        margin: -1rem -100vw 3rem;
        padding-left: 100vw;
        padding-right: 100vw;
        text-align: center;
        color: white;
    }
    
    .title-text {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    
    /* スピナーメッセージを中央揃え - 最終版 */
    [data-testid="stSpinner"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    [data-testid="stSpinner"] > div {
        text-align: center !important;
        width: 100% !important;
    }
    
    .stSpinner {
        text-align: center !important;
        width: 100% !important;
    }
    
    .stSpinner > div {
        text-align: center !important;
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    @media (max-width: 768px) {
        .title-text {
            font-size: 2rem;
        }
        .subtitle-text {
            font-size: 1rem;
        }
        .search-card {
            padding: 25px;
        }
    }
</style>

<div class="title-container">
    <h1 class="title-text">🪄 スーパー図解くん</h1>
    <p class="subtitle-text">キーワードを入力すると、Web検索して雑誌のように見やすく解説します！<br>
    Amazon BedrockのClaude Sonnet 4を利用しています。</p>
</div>
""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([2, 6, 2])
    
    with col2:
        col_input, col_button = st.columns([5, 1])
        
        with col_input:
            keyword = st.text_input(
                "キーワードを入力",
                placeholder="調べたいキーワードを入力してね",
                help="知りたいトピックやキーワードを入力してください",
                label_visibility="collapsed"
            )
        
        with col_button:
            search_button = st.button(
                "図解",
                use_container_width=True,
                type="primary"
            )

# 検索処理
if search_button and keyword:
    with st.container():
        col1, col2, col3 = st.columns([1, 8, 1])
        
        with col2:
            # 検索フェーズ
            search_results = None
            with st.spinner("検索中..."):
                try:
                    # Tavily検索を実行
                    search_client = TavilySearch()
                    search_results = search_client.search(keyword, max_results=10)
                    
                    if not search_results:
                        st.error("検索結果が見つかりませんでした。別のキーワードをお試しください。")
                    else:
                        # 検索結果をサイドバーに表示
                        with st.sidebar:
                            st.subheader("📋 検索ソース")
                            for i, result in enumerate(search_results):
                                if result['url']:
                                    st.markdown(f"**{i+1}. [{result['title']}]({result['url']})**")
                                else:
                                    st.markdown(f"**{i+1}. {result['title']}**")
                except Exception as e:
                    st.error(f"検索エラーが発生しました: {str(e)}")
                    st.stop()
            
            # 検索が成功した場合のみ進行
            if search_results:
                # 検索完了メッセージ
                st.markdown("<div style='text-align: center;'>✅ 検索完了！</div>", unsafe_allow_html=True)
            
                # 図解生成フェーズ
                final_html = None
                with st.spinner("図解を生成中...（1分ぐらいかかります）"):
                    try:
                        bedrock_client = BedrockClient()
                        html_content = bedrock_client.generate_content(keyword, search_results)
                        
                        # HTMLジェネレーターでラップ
                        final_html = HTMLGenerator.wrap_content(html_content, keyword)
                        
                        # 検索履歴に追加
                        st.session_state.search_history.append({
                            'keyword': keyword,
                            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                            'html': final_html
                        })
                        
                    except Exception as bedrock_error:
                        st.error(f"Claude生成でエラーが発生しました: {str(bedrock_error)}")
                        st.info("AWS認証情報やBedrockの設定を確認してください。")
                        st.stop()
                
                # 図解生成が成功した場合のみ表示
                if final_html:
                    # 図解生成完了メッセージ
                    st.markdown("<div style='text-align: center;'>✅ 図解生成完了！</div>", unsafe_allow_html=True)
                    
                    # 結果を表示
                    st.markdown("---")
                    st.markdown("### 📖 図解結果")
                    
                    # HTMLコンポーネントとして表示
                    components.html(final_html, height=800, scrolling=True)


# エラーハンドリング用の情報
if not keyword and search_button:
    with st.container():
        col1, col2, col3 = st.columns([1, 8, 1])
        
        with col2:
            st.warning("キーワードを入力してください。")