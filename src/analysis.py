from __future__ import annotations

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from .text_utils import STOPWORDS, top_keywords


def metric_summary(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "total_reviews": 0,
            "app_count": 0,
            "avg_rating": 0,
            "negative_rate": 0,
            "date_min": None,
            "date_max": None,
        }
    return {
        "total_reviews": int(len(df)),
        "app_count": int(df["App"].nunique()),
        "avg_rating": round(float(df["Star_Rating"].mean()), 2),
        "negative_rate": round(float((df["Star_Rating"] <= 2).mean() * 100), 2),
        "date_min": df["Review_Date"].min() if "Review_Date" in df.columns else None,
        "date_max": df["Review_Date"].max() if "Review_Date" in df.columns else None,
    }


def app_profile(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    g = df.groupby("App", dropna=False).agg(
        评论数=("Review_Text", "count"),
        平均评分=("Star_Rating", "mean"),
        好评率=("Star_Rating", lambda s: (s >= 4).mean() * 100),
        差评率=("Star_Rating", lambda s: (s <= 2).mean() * 100),
        平均情感分=("Sentiment_Polarity", "mean"),
        平均点赞数=("Thumbs_Up_Count", "mean"),
    ).reset_index()
    for col in ["平均评分", "好评率", "差评率", "平均情感分", "平均点赞数"]:
        g[col] = g[col].round(2)
    return g.sort_values(["评论数", "平均评分"], ascending=[False, False])


def rating_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    res = df.groupby(["App", "Star_Rating"]).size().reset_index(name="评论数")
    return res


def sentiment_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    res = df.groupby(["App", "Sentiment_Label"]).size().reset_index(name="评论数")
    total = res.groupby("App")["评论数"].transform("sum")
    res["占比"] = (res["评论数"] / total * 100).round(2)
    return res


def theme_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    res = df.groupby(["App", "Review_Theme"]).size().reset_index(name="评论数")
    total = res.groupby("App")["评论数"].transform("sum")
    res["占比"] = (res["评论数"] / total * 100).round(2)
    return res.sort_values("评论数", ascending=False)


def monthly_trend(df: pd.DataFrame, app: str | None = None) -> pd.DataFrame:
    if df.empty or "Review_Date" not in df.columns:
        return pd.DataFrame()
    d = df.dropna(subset=["Review_Date"]).copy()
    if app and app != "全部":
        d = d[d["App"] == app]
    if d.empty:
        return pd.DataFrame()
    d["月份"] = d["Review_Date"].dt.to_period("M").dt.to_timestamp()
    res = d.groupby("月份").agg(
        评论数=("Review_Text", "count"),
        平均评分=("Star_Rating", "mean"),
        差评率=("Star_Rating", lambda s: (s <= 2).mean() * 100),
        平均情感分=("Sentiment_Polarity", "mean"),
    ).reset_index()
    for col in ["平均评分", "差评率", "平均情感分"]:
        res[col] = res[col].round(3)
    return res


def keyword_table(df: pd.DataFrame, top_n: int = 30, only_negative: bool = False) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["关键词", "频次"])
    d = df[df["Star_Rating"] <= 2] if only_negative else df
    words = top_keywords(d["Review_Text"].dropna().astype(str).tolist(), top_n=top_n)
    return pd.DataFrame(words, columns=["关键词", "频次"])


def tfidf_by_app(df: pd.DataFrame, top_n: int = 12) -> pd.DataFrame:
    if df.empty or df["App"].nunique() < 1:
        return pd.DataFrame(columns=["App", "关键词", "TF-IDF"])
    docs = df.groupby("App")["Review_Text"].apply(lambda s: " ".join(s.astype(str))).reset_index()
    if docs.empty:
        return pd.DataFrame(columns=["App", "关键词", "TF-IDF"])
    vectorizer = TfidfVectorizer(
        stop_words=list(STOPWORDS),
        lowercase=True,
        max_features=1000,
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z']{2,}\b",
    )
    X = vectorizer.fit_transform(docs["Review_Text"])
    terms = vectorizer.get_feature_names_out()
    rows = []
    for i, app in enumerate(docs["App"]):
        row = X.getrow(i).toarray().ravel()
        top_idx = row.argsort()[::-1][:top_n]
        for idx in top_idx:
            if row[idx] > 0:
                rows.append({"App": app, "关键词": terms[idx], "TF-IDF": round(float(row[idx]), 4)})
    return pd.DataFrame(rows)


def representative_reviews(df: pd.DataFrame, theme: str | None = None, sentiment: str | None = None, top_n: int = 10) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    d = df.copy()
    if theme and theme != "全部":
        d = d[d["Review_Theme"] == theme]
    if sentiment and sentiment != "全部":
        d = d[d["Sentiment_Label"] == sentiment]
    if d.empty:
        return pd.DataFrame()
    d["代表性得分"] = d["Thumbs_Up_Count"].fillna(0) + d["Review_Length_Chars"].fillna(0) / 100
    cols = ["App", "Review_Date", "Star_Rating", "Sentiment_Label", "Review_Theme", "Thumbs_Up_Count", "Review_Text"]
    return d.sort_values("代表性得分", ascending=False)[cols].head(top_n)
