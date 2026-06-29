from __future__ import annotations

import pandas as pd


def make_sample_data() -> pd.DataFrame:
    rows = [
        ["ChatGPT", "2026-03-31 11:56:27", 1, "consistently gives false information and will argue it is true even when it is verified to be false", 184, "1.2026.076", -0.3187, "Accuracy/Logic Issues"],
        ["ChatGPT", "2026-03-31 11:33:15", 1, "having a convo and then they want us to pay for plus or start new chat", 0, "Unknown", -0.5423, "Pricing/Subscription"],
        ["ChatGPT", "2026-03-31 10:53:21", 2, "the free version is slow performance and paid is good performance", 0, "1.2026.076", 0.25, "Bugs/Performance"],
        ["ChatGPT", "2026-03-31 10:52:23", 4, "very smart in headings and explaining but some factual data are not updated", 0, "1.2026.076", 0.68, "Accuracy/Logic Issues"],
        ["Claude", "2026-03-20 08:10:00", 5, "excellent writing assistant and the long text conversation is very smooth", 35, "2.1.0", 0.91, "Learning/Work Value"],
        ["Claude", "2026-03-21 08:10:00", 3, "good answer quality but file upload limit is annoying", 6, "2.1.0", 0.13, "Usage Limits"],
        ["Gemini", "2026-03-19 12:15:00", 2, "login verification keeps failing and the app gets stuck", 11, "3.0.1", -0.61, "Login/Account"],
        ["Gemini", "2026-03-22 12:15:00", 4, "image and search features are useful for school study", 18, "3.0.1", 0.72, "Feature Experience"],
        ["Copilot", "2026-03-15 09:20:00", 4, "works well for office writing and productivity", 9, "1.5.2", 0.71, "Learning/Work Value"],
        ["Copilot", "2026-03-16 09:20:00", 2, "account sign in is complicated and sometimes does not work", 4, "1.5.2", -0.34, "Login/Account"],
        ["Perplexity", "2026-03-25 20:00:00", 5, "great for search and citations, answers are clear", 27, "4.0.0", 0.84, "Learning/Work Value"],
        ["Perplexity", "2026-03-26 20:00:00", 3, "sometimes outdated sources and the response is too short", 3, "4.0.0", -0.02, "Accuracy/Logic Issues"],
    ]
    df = pd.DataFrame(rows, columns=[
        "App", "Review_Date", "Star_Rating", "Review_Text", "Thumbs_Up_Count", "App_Version",
        "Sentiment_Polarity", "Review_Theme"
    ])
    df["Review_Date"] = pd.to_datetime(df["Review_Date"])
    df["Word_Count"] = df["Review_Text"].str.split().str.len()
    df["Review_Length_Chars"] = df["Review_Text"].str.len()
    df["Sentiment_Label"] = df["Sentiment_Polarity"].map(lambda x: "正面" if x >= 0.05 else ("负面" if x <= -0.05 else "中性"))
    df["Rating_Group"] = pd.cut(df["Star_Rating"], bins=[0, 2, 3, 5], labels=["差评(1-2星)", "中评(3星)", "好评(4-5星)"], include_lowest=True)
    df["Source"] = "sample"
    return df
