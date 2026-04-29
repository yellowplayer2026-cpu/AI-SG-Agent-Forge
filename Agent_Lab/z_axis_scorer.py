import json

def calculate_z_score(project_metrics):
    """
    AI-SG Z-Axis Scoring Logic
    Metrics: Breadth (廣), Height (高), Depth (深), Strength (強), Reliability (信)
    """
    # 這裡未來會接 LLM API 進行語義分析，目前先用邏輯權重模擬
    weights = {
        "breadth": 0.2,
        "height": 0.2,
        "depth": 0.2,
        "strength": 0.2,
        "reliability": 0.2
    }
    
    score = sum(project_metrics[k] * weights[k] for k in weights)
    return round(score, 2)

if __name__ == "__main__":
    # 範例：一個 ESG 自動化報告專案
    sample_metrics = {
        "breadth": 85,  # 覆蓋全公司 5 個部門
        "height": 90,   # 提升至決策層級指標
        "depth": 70,    # 涉及 ISO 14064 專業細節
        "strength": 95, # 節省 80% 人力工時
        "reliability": 80 # 數據經由系統自動校驗
    }
    
    final_score = calculate_z_score(sample_metrics)
    print(f"--- AI-SG Z-Axis Value Report ---")
    print(f"Project Value Score: {final_score} / 100")
