from __future__ import annotations

import io
from pathlib import Path
from typing import Iterable

import pandas as pd

from .text_utils import clean_text, infer_theme, sentiment_label, sentiment_score

COLUMN_ALIASES = {
    "App": ["App", "app", "app_name", "App_Name", "application", "product", "Product"],
    "Review_Date": ["Review_Date", "review_date", "date", "Date", "at", "posted_at", "time", "created_at"],
    "Star_Rating": ["Star_Rating", "star_rating", "score", "Score", "rating", "Rating", "stars", "Stars"],
    "Review_Text": ["Review_Text", "review_text", "content", "Content", "review", "Review", "text", "Text", "comment", "Comment"],
    "Word_Count": ["Word_Count", "word_count", "words"],
    "Review_Length_Chars": ["Review_Length_Chars", "review_length_chars", "length", "content_length"],
    "Thumbs_Up_Count": ["Thumbs_Up_Count", "thumbsUpCount", "thumbs_up_count", "likes", "helpful_count", "helpful"],
    "App_Version": ["App_Version", "app_version", "reviewCreatedVersion", "appVersion", "version", "Version"],
    "Sentiment_Polarity": ["Sentiment_Polarity", "sentiment_polarity", "sentiment_score", "compound", "polarity"],
    "Review_Theme": ["Review_Theme", "review_theme", "theme", "topic", "Topic", "category", "Category"],
    "Review_ID": ["Review_ID", "reviewId", "review_id", "id", "ID"],
    "Source": ["Source", "source", "dataset"],
}

IDENTITY_COLUMNS = {
    "userName", "user_name", "UserName", "userImage", "user_image", "UserImage",
    "replyContent", "repliedAt", "developer_reply"
}


def _find_column(df: pd.DataFrame, aliases: list[str]) -> str | None:
    lower_map = {str(c).strip().lower(): c for c in df.columns}
    for alias in aliases:
        if alias in df.columns:
            return alias
        c = lower_map.get(alias.strip().lower())
        if c is not None:
            return c
    return None


def read_csv_any(file_obj, source_name: str | None = None) -> pd.DataFrame:
    """Read uploaded or local CSV with common encodings."""
    if isinstance(file_obj, (str, Path)):
        raw = Path(file_obj).read_bytes()
        source_name = source_name or Path(file_obj).name
    else:
        raw = file_obj.getvalue() if hasattr(file_obj, "getvalue") else file_obj.read()
        source_name = source_name or getattr(file_obj, "name", "uploaded_csv")
    last_err = None
    for enc in ["utf-8", "utf-8-sig", "latin1", "gb18030"]:
        try:
            return pd.read_csv(io.BytesIO(raw), encoding=enc).assign(_file_source=source_name)
        except Exception as e:
            last_err = e
    raise ValueError(f"CSV 读取失败：{source_name}; last error={last_err}")


def standardize_dataframe(df: pd.DataFrame, default_app: str | None = None) -> pd.DataFrame:
    """Map dataset-specific columns to a unified schema and derive missing analysis fields."""
    df = df.copy()

    # Remove user identity columns if present. The system analyzes product feedback, not individual users.
    drop_cols = [c for c in df.columns if str(c) in IDENTITY_COLUMNS]
    if drop_cols:
        df = df.drop(columns=drop_cols)

    out = pd.DataFrame(index=df.index)
    for std_col, aliases in COLUMN_ALIASES.items():
        col = _find_column(df, aliases)
        if col is not None:
            out[std_col] = df[col]

    if "Source" not in out.columns:
        out["Source"] = df.get("_file_source", "unknown")

    if "App" not in out.columns:
        source_text = " ".join(map(str, out.get("Source", pd.Series([""])).head(1).tolist())).lower()
        if default_app:
            out["App"] = default_app
        elif "chatgpt" in source_text or "chat-gpt" in source_text or "openai" in source_text:
            out["App"] = "ChatGPT"
        else:
            out["App"] = "Unknown"

    if "Review_Text" not in out.columns:
        raise ValueError("没有识别到评论文本字段。请确认 CSV 中有 content / Review_Text / review / text 等字段。")
    if "Star_Rating" not in out.columns:
        raise ValueError("没有识别到评分字段。请确认 CSV 中有 score / rating / Star_Rating 等字段。")

    out["Review_Text"] = out["Review_Text"].map(clean_text)
    out = out[out["Review_Text"].str.len() > 0].copy()

    out["Star_Rating"] = pd.to_numeric(out["Star_Rating"], errors="coerce")
    out = out[out["Star_Rating"].between(1, 5, inclusive="both")].copy()

    if "Review_Date" in out.columns:
        out["Review_Date"] = pd.to_datetime(out["Review_Date"], errors="coerce")
    else:
        out["Review_Date"] = pd.NaT

    if "Thumbs_Up_Count" in out.columns:
        out["Thumbs_Up_Count"] = pd.to_numeric(out["Thumbs_Up_Count"], errors="coerce").fillna(0).astype(int)
    else:
        out["Thumbs_Up_Count"] = 0

    if "App_Version" not in out.columns:
        out["App_Version"] = "Unknown"
    out["App_Version"] = out["App_Version"].fillna("Unknown").astype(str)

    if "Word_Count" not in out.columns:
        out["Word_Count"] = out["Review_Text"].str.split().str.len()
    else:
        out["Word_Count"] = pd.to_numeric(out["Word_Count"], errors="coerce").fillna(0).astype(int)

    if "Review_Length_Chars" not in out.columns:
        out["Review_Length_Chars"] = out["Review_Text"].str.len()
    else:
        out["Review_Length_Chars"] = pd.to_numeric(out["Review_Length_Chars"], errors="coerce").fillna(0).astype(int)

    if "Sentiment_Polarity" in out.columns:
        out["Sentiment_Polarity"] = pd.to_numeric(out["Sentiment_Polarity"], errors="coerce")
        missing = out["Sentiment_Polarity"].isna()
        if missing.any():
            out.loc[missing, "Sentiment_Polarity"] = out.loc[missing, "Review_Text"].map(sentiment_score)
    else:
        out["Sentiment_Polarity"] = out["Review_Text"].map(sentiment_score)

    out["Sentiment_Label"] = out["Sentiment_Polarity"].map(sentiment_label)

    if "Review_Theme" in out.columns:
        out["Review_Theme"] = out["Review_Theme"].fillna("General").astype(str)
        blank = out["Review_Theme"].str.strip().eq("")
        out.loc[blank, "Review_Theme"] = out.loc[blank, "Review_Text"].map(infer_theme)
    else:
        out["Review_Theme"] = out["Review_Text"].map(infer_theme)

    out["Rating_Group"] = pd.cut(
        out["Star_Rating"],
        bins=[0, 2, 3, 5],
        labels=["差评(1-2星)", "中评(3星)", "好评(4-5星)"],
        include_lowest=True,
    )

    # Avoid duplicated rows when the same review appears in both datasets.
    subset = ["App", "Review_Date", "Star_Rating", "Review_Text"]
    out = out.drop_duplicates(subset=[c for c in subset if c in out.columns]).reset_index(drop=True)
    return out


def load_many(files: Iterable, data_dir: str | Path | None = None) -> pd.DataFrame:
    frames = []
    for f in files or []:
        raw = read_csv_any(f)
        frames.append(standardize_dataframe(raw))

    if data_dir:
        for path in sorted(Path(data_dir).glob("*.csv")):
            raw = read_csv_any(path)
            frames.append(standardize_dataframe(raw))

    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)
