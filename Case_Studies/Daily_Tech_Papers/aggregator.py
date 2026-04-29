import json
import datetime
import requests # 如果需要抓取網頁內容
from bs4 import BeautifulSoup # 如果需要解析網頁內容

def fetch_and_summarize_papers():
    """
    這個函數將負責：
    1. 從 arXiv 或其他科技論文來源抓取最新論文資訊。
    2. 對每篇論文生成一個簡短摘要（目前先用模擬的）。
    3. 將結果格式化為 JSON。
    """
    papers_data = []
    today_date = datetime.date.today().strftime("%Y年%m月%d日")

    # --- 模擬抓取和摘要過程 ---
    # 實際應用中，這裡會是複雜的網頁爬蟲或 API 調用
    # 並會使用 LLM 進行摘要和分類

    # 範例論文 1
    papers_data.append({
        "title": "AI Agent Orchestration: A Secretary-General's Perspective",
        "authors": "Roger Lo et al.",
        "summary": "本論文深入探討了 AI Agent 如何在 Roger 老師的 AI-SG 框架下，扮演數位秘書長的角色，通過 X-Y-Z 軸的治理模型與 AEDDI 工作流，實現人機協作的最大化價值產出，為個人與企業帶來可持續發展的第二曲線。",
        "link": "https://github.com/yellowplayer2026-cpu/AI-SG-Agent-Forge"
    })

    # 範例論文 2
    papers_data.append({
        "title": "Enhancing Knowledge Management with LLM-Powered Aggregation",
        "authors": "AI Hermes",
        "summary": "本研究介紹了一種利用大型語言模型（LLM）自動彙整、摘要科技論文的方法。透過高效的資訊提取與語義理解，該系統能大幅提升個人及組織獲取最新知識的效率，實現知識管理的智能化與自動化。",
        "link": "https://arxiv.org/abs/2301.xxxx" # 假設的 arXiv 連結
    })
    
    # 範例論文 3 (從 arXiv 模擬獲取)
    try:
        # 這裡示範如何從 arXiv API 獲取數據，但我們不會真的執行這個請求，
        # 因為需要安裝 'arxiv' 庫，且可能超出單次 terminal 調用的複雜度。
        # 這裡僅作示意，實際將替換為真實的抓取邏輯。
        # from arxiv import Client, Search, SortCriterion
        # client = Client()
        # search = Search(
        #     query="LLM agent knowledge management",
        #     max_results=1,
        #     sort_by=SortCriterion.SubmittedDate
        # )
        # results = client.results(search)
        # first_paper = next(results)
        # papers_data.append({
        #     "title": first_paper.title,
        #     "authors": ", ".join([a.name for a in first_paper.authors]),
        #     "summary": "（由 LLM 生成的摘要，此處為示意）" + first_paper.summary[:200] + "...",
        #     "link": first_paper.entry_id
        # })
        pass
    except Exception as e:
        # print(f"Error fetching from arXiv: {e}")
        papers_data.append({
            "title": "（模擬）arXiv 論文：AI 發展的最新趨勢",
            "authors": "AI Researcher",
            "summary": "本論文分析了人工智慧領域的最新發展，特別是大型語言模型在多模態應用、Agent 行為設計和倫理挑戰方面的進展，並提出了未來研究方向的展望。旨在為廣大 AI 從業者提供前瞻性視角。",
            "link": "https://arxiv.org/abs/2404.xxxx"
        })

    return {
        "update_date": today_date,
        "papers": papers_data
    }

def generate_html_from_papers(data):
    """
    根據 JSON 數據生成 HTML 內容。
    """
    html_template_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    papers_html = []
    for paper in data["papers"]:
        papers_html.append(f"""
            <li class="paper-item">
                <h2>{paper["title"]}</h2>
                <p class="authors">作者：{paper["authors"]}</p>
                <p class="summary">{paper["summary"]}</p>
                <a href="{paper["link"]}" target="_blank" class="read-more">閱讀更多</a>
            </li>
        """)
    
    # 替換 HTML 中的內容
    html_content = html_content.replace('<span id="update-date">2026年4月29日</span>', f'<span id="update-date">{data["update_date"]}</span>')
    # 這裡的替換方式需要更精確，確保不會替換掉範例論文，未來可使用模板引擎
    # 為了簡化，目前直接替換整個容器的內容 (這會移除範例論文)
    # 或者，我們可以在 JavaScript 中動態插入，讓 Python 只負責生成 JSON
    
    # 為了實現動態內容，我們先讓 Python 生成一個包含數據的 JSON 文件
    # 而 HTML 的 JavaScript 會去讀取這個 JSON
    
    # 更正：為簡化 GitHub Pages 部署，讓 Python 直接生成完整的 HTML 內容會更直接
    # 因此，我們需要一個新的 HTML 模板，不包含預設範例，並讓 Python 填充
    
    # 暫時簡化邏輯：直接替換掉原 HTML 裡面的預設內容
    # 在實際部署中，會將動態生成的內容寫入到一個預留的 div 中
    start_marker = "<!-- 論文條目將由 AI Agent 動態生成 -->"
    end_marker = "<!-- 更多論文將在此處加入 -->"
    
    if start_marker in html_content and end_marker in html_content:
        pre_content = html_content.split(start_marker)[0]
        post_content = html_content.split(end_marker)[1]
        
        final_html = pre_content + start_marker + "\\n" + "\\n".join(papers_html) + "\\n" + end_marker + post_content
    else:
        # 如果標記不存在，簡單地在 body 結束前插入
        final_html = html_content.replace('</ul>', "\\n".join(papers_html) + "\\n        </ul>")

    return final_html


if __name__ == "__main__":
    papers_data = fetch_and_summarize_papers()
    
    # 重新生成包含最新數據的 index.html
    final_html_output = generate_html_from_papers(papers_data)
    
    output_html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(final_html_output)
    
    print(f"Generated Daily Tech Papers HTML for {papers_data['update_date']}")
    # 為了讓 GitHub Action 看到輸出，這裡可以打印一些關鍵信息
    for paper in papers_data['papers']:
        print(f"  - {paper['title']}")

