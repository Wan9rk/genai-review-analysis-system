from __future__ import annotations

import re
from collections import Counter
from typing import Iterable

try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
except Exception:  # pragma: no cover
    SentimentIntensityAnalyzer = None

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "than", "so", "to", "of", "in", "on", "for", "with",
    "at", "by", "from", "as", "is", "are", "was", "were", "be", "been", "being", "it", "this", "that", "these",
    "those", "i", "me", "my", "we", "our", "you", "your", "he", "she", "they", "them", "their", "not", "no",
    "do", "does", "did", "can", "could", "would", "should", "will", "just", "very", "really", "app", "chatgpt",
    "chat", "gpt", "ai", "use", "using", "used", "get", "got", "one", "also", "please", "like", "good", "great",
    "best", "nice", "love", "amazing", "help", "helpful", "thanks", "thank", "much", "many", "make", "made"
}

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "awesome", "perfect", "love", "helpful", "useful", "easy", "fast",
    "smooth", "wonderful", "best", "nice", "satisfied", "smart", "brilliant", "productive", "accurate"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "worst", "slow", "crash", "bug", "bugs", "wrong", "false", "inaccurate", "limit", "limited",
    "pay", "paid", "subscription", "refund", "login", "error", "problem", "issue", "issues", "freeze", "stuck",
    "annoying", "useless", "poor", "broken", "fail", "failed", "cannot", "can't"
}

THEME_KEYWORDS = {
    "Accuracy/Logic Issues": [
        "wrong", "false", "inaccurate", "hallucination", "hallucinate", "incorrect", "accuracy", "logic", "fact", "answer",
        "response", "trust", "not true", "fake", "misleading", "outdated"
    ],
    "Bugs/Performance": [
        "slow", "lag", "crash", "freeze", "loading", "bug", "bugs", "error", "stuck", "broken", "performance",
        "not working", "doesn't work", "cannot open", "network", "server", "down"
    ],
    "Pricing/Subscription": [
        "pay", "paid", "plus", "premium", "subscription", "subscribe", "billing", "refund", "price", "expensive",
        "free", "upgrade", "money", "trial", "purchase"
    ],
    "Usage Limits": [
        "limit", "quota", "cap", "message cap", "wait", "hours", "creation limit", "image limit", "upload limit",
        "restricted", "unavailable", "too many", "rate limit"
    ],
    "Login/Account": [
        "login", "log in", "sign in", "account", "verify", "verification", "otp", "password", "email", "phone",
        "blocked", "ban", "banned"
    ],
    "Feature Experience": [
        "voice", "image", "photo", "picture", "file", "upload", "search", "camera", "audio", "speaker", "video",
        "generate", "drawing", "code", "coding"
    ],
    "Learning/Work Value": [
        "study", "school", "homework", "exam", "teacher", "learn", "learning", "project", "work", "job", "writing",
        "summary", "summarize", "productivity", "coding", "explain"
    ],
}


def clean_text(text: object) -> str:
    """Normalize review text for analysis while keeping original content elsewhere."""
    if text is None:
        return ""
    s = str(text)
    s = re.sub(r"https?://\S+|www\.\S+", " ", s)
    s = re.sub(r"<.*?>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def tokenize(text: str) -> list[str]:
    text = clean_text(text).lower()
    tokens = re.findall(r"[a-zA-Z][a-zA-Z']{1,}", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 2]


def top_keywords(texts: Iterable[str], top_n: int = 30) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for text in texts:
        counter.update(tokenize(text))
    return counter.most_common(top_n)


def sentiment_score(text: str) -> float:
    """Return VADER compound score if available; otherwise a small lexicon fallback."""
    text = clean_text(text)
    if not text:
        return 0.0
    if SentimentIntensityAnalyzer is not None:
        analyzer = SentimentIntensityAnalyzer()
        return float(analyzer.polarity_scores(text)["compound"])

    tokens = tokenize(text)
    if not tokens:
        return 0.0
    pos = sum(t in POSITIVE_WORDS for t in tokens)
    neg = sum(t in NEGATIVE_WORDS for t in tokens)
    return max(-1.0, min(1.0, (pos - neg) / max(1, pos + neg)))


def sentiment_label(score: float) -> str:
    try:
        score = float(score)
    except Exception:
        score = 0.0
    if score >= 0.05:
        return "正面"
    if score <= -0.05:
        return "负面"
    return "中性"


def infer_theme(text: str) -> str:
    s = clean_text(text).lower()
    scores = {}
    for theme, words in THEME_KEYWORDS.items():
        scores[theme] = sum(1 for w in words if w in s)
    if not scores or max(scores.values()) == 0:
        return "General"
    return max(scores, key=scores.get)
