from pathlib import Path
import pandas as pd
import numpy as np

INPUT_FILE = Path("data/chatgpt_reviews_sample_50000.csv")
OUTPUT_FILE = Path("data/chatgpt_reviews_fast_50000.csv")

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"找不到输入文件：{INPUT_FILE}")

print("开始读取 GPT 抽样评论数据...")
df = pd.read_csv(INPUT_FILE, low_memory=False)

print("原始规模:", df.shape)
print("原始字段:", list(df.columns))

# 统一字段
out = pd.DataFrame()
out["App"] = "ChatGPT"
out["Review_ID"] = df.get("reviewId", "")
out["Review_Text"] = df["content"].fillna("").astype(str).str.strip()
out["Star_Rating"] = pd.to_numeric(df["score"], errors="coerce")
out["Thumbs_Up_Count"] = pd.to_numeric(df.get("thumbsUpCount", 0), errors="coerce").fillna(0).astype(int)
out["Review_Date"] = pd.to_datetime(df["at"], errors="coerce")
out["App_Version"] = df.get("appVersion", df.get("reviewCreatedVersion", "Unknown")).fillna("Unknown").astype(str)
out["Source"] = "ChatGPT reviews daily updated sample"

# 基础清洗
out = out[out["Review_Text"].str.len() > 0].copy()
out = out[out["Star_Rating"].between(1, 5)].copy()

# 用评分快速生成情感分数，避免 Streamlit 逐条跑 VADER
score_to_sentiment = {
    1: -0.8,
    2: -0.4,
    3: 0.0,
    4: 0.4,
    5: 0.8,
}
out["Sentiment_Polarity"] = out["Star_Rating"].round().map(score_to_sentiment).fillna(0.0)

# 用向量化关键词规则生成主题，避免 Streamlit 实时逐条主题识别
text = out["Review_Text"].str.lower()

theme_rules = {
    "Accuracy/Logic Issues": r"wrong|false|inaccurate|hallucination|incorrect|accuracy|logic|fact|answer|response|fake|misleading|outdated",
    "Bugs/Performance": r"slow|lag|crash|freeze|loading|bug|bugs|error|stuck|broken|not working|doesn't work|cannot open|network|server|down",
    "Pricing/Subscription": r"pay|paid|plus|premium|subscription|subscribe|billing|refund|price|expensive|free|upgrade|money|trial|purchase",
    "Usage Limits": r"limit|quota|cap|message cap|wait|hours|image limit|upload limit|restricted|unavailable|too many|rate limit",
    "Login/Account": r"login|log in|sign in|account|verify|verification|otp|password|email|phone|blocked|ban|banned",
    "Feature Experience": r"voice|image|photo|picture|file|upload|search|camera|audio|speaker|video|generate|drawing|code|coding",
    "Learning/Work Value": r"study|school|homework|exam|teacher|learn|learning|project|work|job|writing|summary|summarize|productivity|coding|explain",
}

out["Review_Theme"] = "General"
for theme, pattern in theme_rules.items():
    mask = text.str.contains(pattern, regex=True, na=False)
    out.loc[mask & out["Review_Theme"].eq("General"), "Review_Theme"] = theme

# 补充长度字段
out["Word_Count"] = out["Review_Text"].str.split().str.len()
out["Review_Length_Chars"] = out["Review_Text"].str.len()

# 去重
out = out.drop_duplicates(subset=["App", "Review_Date", "Star_Rating", "Review_Text"]).reset_index(drop=True)

out.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print("处理完成！")
print("输出文件:", OUTPUT_FILE)
print("输出规模:", out.shape)
print("输出字段:", list(out.columns))
print(out.head(3).to_string())
