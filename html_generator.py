class HTMLGenerator:
    @staticmethod
    def generate_base_style():
        """基本的なCSSスタイルを生成"""
        return """
        <style>
            /* 完全リセット */
            *, *::before, *::after {
                box-sizing: border-box !important;
                max-width: 100% !important;
            }
            
            html {
                overflow-x: hidden !important;
                width: 100vw !important;
                max-width: 100vw !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            body {
                overflow-x: hidden !important;
                width: 100vw !important;
                max-width: 100vw !important;
                margin: 0 !important;
                padding: 0 !important;
                position: relative !important;
            }
            
            .zukai-container {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                max-width: min(1200px, 100vw) !important;
                width: 100% !important;
                margin: 0 auto !important;
                padding: 20px !important;
                background-color: #ffffff;
                overflow-x: hidden !important;
                position: relative !important;
            }
            
            .zukai-header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px !important;
                border-radius: 15px;
                text-align: center;
                margin: 0 0 30px 0 !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                width: 100% !important;
                max-width: 100% !important;
                overflow: hidden !important;
                word-wrap: break-word !important;
                position: relative !important;
            }
            
            .zukai-header h1 {
                margin: 0;
                font-size: 2.5em;
                font-weight: 700;
            }
            
            .zukai-section {
                background: #f8f9fa;
                border-radius: 10px;
                padding: 30px !important;
                margin: 0 0 20px 0 !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                width: 100% !important;
                max-width: 100% !important;
                overflow-x: hidden !important;
                word-wrap: break-word !important;
                position: relative !important;
            }
            
            .zukai-section h2 {
                color: #2c3e50;
                font-size: 1.8em;
                margin-bottom: 20px;
                border-bottom: 3px solid #667eea;
                padding-bottom: 10px;
            }
            
            .zukai-section h3 {
                color: #34495e;
                font-size: 1.4em;
                margin-top: 25px;
                margin-bottom: 15px;
            }
            
            .highlight-box {
                background: #e8f4ff;
                border-left: 5px solid #3498db;
                padding: 15px 20px;
                margin: 20px 0;
                border-radius: 5px;
            }
            
            .important-point {
                background: #fff3cd;
                border: 2px solid #ffc107;
                border-radius: 8px;
                padding: 15px;
                margin: 20px 0;
                position: relative;
            }
            
            .important-point::before {
                content: "⚡ ポイント";
                position: absolute;
                top: -12px;
                left: 20px;
                background: #ffc107;
                color: #000;
                padding: 2px 10px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 0.9em;
            }
            
            .data-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .data-table th {
                background: #667eea;
                color: white;
                padding: 12px;
                text-align: left;
                font-weight: 600;
            }
            
            .data-table td {
                padding: 12px;
                border-bottom: 1px solid #e0e0e0;
            }
            
            .data-table tr:nth-child(even) {
                background: #f5f5f5;
            }
            
            .bullet-list {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }
            
            .bullet-list li {
                margin-bottom: 12px;
                line-height: 1.6;
                color: #2c3e50;
            }
            
            .quote-box {
                background: #f0f0f0;
                border-left: 4px solid #667eea;
                padding: 20px;
                margin: 20px 0;
                font-style: italic;
                border-radius: 0 8px 8px 0;
            }
            
            .source-link {
                color: #3498db;
                text-decoration: none;
                font-size: 0.9em;
                display: inline-block;
                margin-top: 10px;
            }
            
            .source-link:hover {
                text-decoration: underline;
            }
            
            /* 通常の見出しは黒文字 */
            h1, h2, h3, h4, h5, h6 {
                color: #2c3e50 !important;
                font-weight: bold !important;
            }
            
            /* 色付き背景・グラデーション背景の見出しは白抜きに */
            div[style*="background"] h1,
            div[style*="background"] h2,
            div[style*="background"] h3,
            div[style*="background"] h4,
            div[style*="background"] h5,
            div[style*="background"] h6,
            section[style*="background"] h1,
            section[style*="background"] h2,
            section[style*="background"] h3,
            section[style*="background"] h4,
            section[style*="background"] h5,
            section[style*="background"] h6,
            header[style*="background"] h1,
            header[style*="background"] h2,
            header[style*="background"] h3,
            header[style*="background"] h4,
            header[style*="background"] h5,
            header[style*="background"] h6,
            .hero h1, .hero h2, .hero h3, .hero h4, .hero h5, .hero h6,
            .banner h1, .banner h2, .banner h3, .banner h4, .banner h5, .banner h6,
            .card-header h1, .card-header h2, .card-header h3, .card-header h4, .card-header h5, .card-header h6 {
                color: white !important;
            }
            
            /* より具体的に青・紫系の背景を検出 */
            [style*="linear-gradient"] h1,
            [style*="linear-gradient"] h2,
            [style*="linear-gradient"] h3,
            [style*="blue"] h1,
            [style*="blue"] h2,
            [style*="blue"] h3,
            [style*="purple"] h1,
            [style*="purple"] h2,
            [style*="purple"] h3 {
                color: white !important;
            }
            
            /* .zukai-headerのテキストも確実に見やすくする */
            .zukai-header h1,
            .zukai-header p {
                color: white !important;
            }
            
            /* すべての要素を完全制御 */
            .zukai-container, .zukai-container * {
                max-width: 100% !important;
                overflow-x: hidden !important;
                word-wrap: break-word !important;
                overflow-wrap: break-word !important;
            }
            
            @media (max-width: 768px) {
                html, body {
                    overflow-x: hidden !important;
                    width: 100vw !important;
                    max-width: 100vw !important;
                }
                
                .zukai-container {
                    padding: 10px !important;
                    margin: 0 !important;
                    width: calc(100vw - 20px) !important;
                    max-width: calc(100vw - 20px) !important;
                    overflow-x: hidden !important;
                }
                
                .zukai-container * {
                    max-width: 100% !important;
                    overflow-x: hidden !important;
                    word-wrap: break-word !important;
                    overflow-wrap: break-word !important;
                }
                
                .zukai-header {
                    padding: 20px 15px !important;
                    margin: 0 0 20px 0 !important;
                    width: 100% !important;
                    max-width: 100% !important;
                    overflow: hidden !important;
                }
                
                .zukai-header h1 {
                    font-size: 1.8em !important;
                    word-wrap: break-word !important;
                    overflow-wrap: break-word !important;
                    hyphens: auto !important;
                }
                
                .zukai-section {
                    padding: 20px 15px !important;
                    margin: 0 0 15px 0 !important;
                    width: 100% !important;
                    max-width: 100% !important;
                    overflow-x: hidden !important;
                }
                
                .data-table {
                    width: 100%;
                    display: block;
                    overflow-x: auto;
                    white-space: nowrap;
                    box-sizing: border-box;
                }
                
                .data-table thead, .data-table tbody, .data-table th, .data-table td, .data-table tr {
                    display: block;
                }
                
                .data-table thead tr {
                    position: absolute;
                    top: -9999px;
                    left: -9999px;
                }
                
                .data-table tr {
                    border: 1px solid #ccc;
                    margin-bottom: 10px;
                    background: white;
                    border-radius: 5px;
                    padding: 10px;
                }
                
                .data-table td {
                    border: none;
                    border-bottom: 1px solid #eee;
                    position: relative;
                    padding-left: 50% !important;
                    white-space: normal;
                    text-align: left;
                }
                
                .data-table td:before {
                    content: attr(data-label) ": ";
                    position: absolute;
                    left: 6px;
                    width: 45%;
                    padding-right: 10px;
                    white-space: nowrap;
                    font-weight: bold;
                    color: #667eea;
                }
                
                .highlight-box, .important-point, .quote-box {
                    margin: 15px 0;
                    padding: 15px;
                    box-sizing: border-box;
                }
                
                .bullet-list {
                    padding: 15px;
                    box-sizing: border-box;
                }
                
                * {
                    max-width: 100% !important;
                    box-sizing: border-box !important;
                    overflow-wrap: break-word !important;
                    word-wrap: break-word !important;
                }
                
                img, video, iframe, table, pre, code {
                    max-width: 100% !important;
                    height: auto !important;
                    overflow-x: auto !important;
                }
                
                /* 長いテキストも確実に折り返し */
                p, div, span, td, th, li {
                    word-wrap: break-word !important;
                    overflow-wrap: break-word !important;
                    hyphens: auto !important;
                    max-width: 100% !important;
                }
            }
        </style>
        """
    
    @staticmethod
    def wrap_content(content: str, keyword: str) -> str:
        """コンテンツを基本的なHTMLテンプレートでラップ"""
        base_style = HTMLGenerator.generate_base_style()
        
        return f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <title>{keyword} の図解</title>
        </head>
        <body>
        {base_style}
        <div class="zukai-container">
            <div class="zukai-header">
                <h1>🔍 {keyword} の図解</h1>
                <p>スーパー図解くんが分かりやすく解説します！</p>
            </div>
            {content}
        </div>
        </body>
        </html>
        """