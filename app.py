from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.analysis import (  # noqa: E402
    app_profile,
    keyword_table,
    metric_summary,
    monthly_trend,
    rating_distribution,
    representative_reviews,
    sentiment_distribution,
    tfidf_by_app,
    theme_distribution,
)
from src.data_loader import load_many  # noqa: E402
from src.sample_data import make_sample_data  # noqa: E402

st.set_page_config(
    page_title="生成式 AI 应用评论分析系统",
    page_icon="📊",
    layout="wide",
)

st.title("📊 生成式 AI 应用用户体验评价与痛点分析系统")
st.caption("基于 Kaggle 公开评论数据，分析 ChatGPT、Claude、Gemini、Copilot、Perplexity 等生成式 AI 应用的用户口碑、情感倾向、痛点主题和时间趋势。")


@st.cache_data(show_spinner=False)
def load_cached(uploaded_files, use_data_dir: bool, use_sample: bool) -> pd.DataFrame:
    if use_sample:
        return make_sample_data()
    data_dir = ROOT / "data" if use_data_dir else None
    return load_many(uploaded_files, data_dir=data_dir)


with st.sidebar:
    st.header("数据输入")
    uploaded = st.file_uploader(
        "上传 Kaggle CSV 文件，可多选",
        type=["csv"],
        accept_multiple_files=True,
        help="可上传 ChatGPT reviews daily updated 与 Generative AI Ecosystem 50K reviews 的 CSV。",
    )
    use_local_data = st.checkbox("同时读取 data/ 目录下的 CSV", value=True)
    use_sample = st.checkbox("没有数据时使用示例数据", value=False)
    st.divider()
    st.markdown("**推荐流程**：下载 Kaggle CSV → 放入 `data/` 或直接上传 → 系统自动识别字段并分析。")

try:
    df = load_cached(uploaded, use_local_data, use_sample)
except Exception as e:
    st.error(str(e))
    st.stop()

if df.empty:
    st.warning("还没有读到数据。请上传 CSV，或把 CSV 放入项目的 data/ 目录。也可以勾选“使用示例数据”先查看系统效果。")
    st.stop()

# ---------- filters ----------
with st.sidebar:
    st.header("筛选条件")
    apps = sorted(df["App"].dropna().astype(str).unique().tolist())
    selected_apps = st.multiselect("应用", apps, default=apps)
    rating_range = st.slider("评分范围", 1, 5, (1, 5))

    date_df = df.dropna(subset=["Review_Date"])
    if not date_df.empty:
        min_date = date_df["Review_Date"].min().date()
        max_date = date_df["Review_Date"].max().date()
        selected_dates = st.date_input("评论日期范围", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    else:
        selected_dates = None

filtered = df[df["App"].astype(str).isin(selected_apps)].copy()
filtered = filtered[filtered["Star_Rating"].between(rating_range[0], rating_range[1])]
if selected_dates and isinstance(selected_dates, tuple) and len(selected_dates) == 2 and not filtered["Review_Date"].isna().all():
    start, end = pd.to_datetime(selected_dates[0]), pd.to_datetime(selected_dates[1]) + pd.Timedelta(days=1)
    filtered = filtered[(filtered["Review_Date"].isna()) | ((filtered["Review_Date"] >= start) & (filtered["Review_Date"] < end))]

pages = [
    "1. 项目说明与字段说明",
    "2. 总览看板",
    "3. 产品口碑对比",
    "4. 情感分析",
    "5. 痛点主题分析",
    "6. 时间趋势分析",
    "7. 关键词与典型评论",
    "8. 系统设计说明",
]
page = st.sidebar.radio("页面", pages)

# ---------- page 1 ----------
if page == "1. 项目说明与字段说明":
    st.header("一、项目定位")
    st.markdown(
        """
本系统面向“大数据技术与应用”课程期末项目，核心目标不是判断哪个大模型能力最强，而是基于真实用户评论数据，分析生成式 AI 应用在**用户体验层面**的口碑差异与主要痛点。

**系统要回答的问题：**
- 不同生成式 AI 应用的评分和评论情感有什么差异？
- 用户对生成式 AI 应用主要满意/不满在哪里？
- 低分评论更集中在模型回答质量、登录账号、订阅付费、性能稳定，还是使用限制？
- ChatGPT 的评论数量、评分和负面反馈是否随时间变化？
        """
    )

    st.header("二、统一后的数据字段")
    field_desc = pd.DataFrame(
        [
            ["App", "应用名称", "区分 ChatGPT、Claude、Gemini、Copilot、Perplexity 等产品"],
            ["Review_Date", "评论时间", "用于月度/日度趋势分析"],
            ["Star_Rating", "用户评分", "计算平均评分、好评率、差评率"],
            ["Review_Text", "评论正文", "用于情感分析、关键词提取、痛点主题识别"],
            ["Word_Count", "评论词数", "衡量评论长度，辅助过滤异常短文本"],
            ["Review_Length_Chars", "评论字符数", "衡量评论长度，辅助选择典型评论"],
            ["Thumbs_Up_Count", "评论点赞数", "衡量评论代表性"],
            ["App_Version", "应用版本", "分析不同版本评论差异，可选"],
            ["Sentiment_Polarity", "情感极性分数", "判断文本正负倾向，来自数据集或系统自动计算"],
            ["Sentiment_Label", "情感标签", "正面/中性/负面"],
            ["Review_Theme", "评论主题/痛点类别", "分析用户关注点和产品问题"],
            ["Source", "数据来源", "标记来自哪个 CSV/数据集"],
        ],
        columns=["字段", "含义", "系统用途"],
    )
    st.dataframe(field_desc, use_container_width=True, hide_index=True)

    st.header("三、当前数据预览")
    st.write(f"当前筛选后共有 **{len(filtered):,}** 条评论；原始合并数据共有 **{len(df):,}** 条评论。")
    st.dataframe(filtered.head(50), use_container_width=True)

# ---------- page 2 ----------
elif page == "2. 总览看板":
    st.header("总览看板")
    m = metric_summary(filtered)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("评论总数", f"{m['total_reviews']:,}")
    c2.metric("应用数量", f"{m['app_count']}")
    c3.metric("平均评分", f"{m['avg_rating']:.2f}")
    c4.metric("差评率", f"{m['negative_rate']:.2f}%")

    profile = app_profile(filtered)
    st.subheader("各产品核心指标")
    st.dataframe(profile, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(profile, x="App", y="评论数", title="各应用评论数量")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(profile, x="App", y="平均评分", title="各应用平均评分", range_y=[0, 5])
        st.plotly_chart(fig, use_container_width=True)

# ---------- page 3 ----------
elif page == "3. 产品口碑对比":
    st.header("产品口碑对比")
    profile = app_profile(filtered)
    st.dataframe(profile, use_container_width=True, hide_index=True)

    dist = rating_distribution(filtered)
    fig = px.bar(dist, x="Star_Rating", y="评论数", color="App", barmode="group", title="不同应用的评分分布")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
        profile,
        x="差评率",
        y="好评率",
        size="评论数",
        hover_name="App",
        title="好评率-差评率产品画像",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("汇报时可以强调：这里比较的是用户评论中的体验口碑，不等同于模型客观能力排名。")

# ---------- page 4 ----------
elif page == "4. 情感分析":
    st.header("情感分析")
    sent = sentiment_distribution(filtered)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(sent, x="App", y="占比", color="Sentiment_Label", title="不同应用情感占比")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.box(filtered, x="App", y="Sentiment_Polarity", title="不同应用情感分数分布")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("评分与情感交叉分析")
    cross = pd.crosstab(filtered["Rating_Group"], filtered["Sentiment_Label"], normalize="index") * 100
    st.dataframe(cross.round(2), use_container_width=True)
    st.markdown("这一部分可用于说明：单看星级评分不够，文本情感可以补充解释用户为什么满意或不满意。")

# ---------- page 5 ----------
elif page == "5. 痛点主题分析":
    st.header("痛点主题分析")
    themes = theme_distribution(filtered)
    st.dataframe(themes, use_container_width=True, hide_index=True)

    fig = px.bar(themes, x="Review_Theme", y="评论数", color="App", barmode="group", title="不同应用的痛点/主题分布")
    st.plotly_chart(fig, use_container_width=True)

    negative = filtered[filtered["Star_Rating"] <= 2]
    if not negative.empty:
        neg_themes = theme_distribution(negative)
        fig = px.bar(neg_themes, x="Review_Theme", y="占比", color="App", barmode="group", title="低分评论中的主题占比")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("重点汇报这张图：它能说明用户差评主要来自哪些产品体验问题。")
    else:
        st.info("当前筛选条件下没有 1-2 星评论。")

# ---------- page 6 ----------
elif page == "6. 时间趋势分析":
    st.header("时间趋势分析")
    app_options = ["全部"] + sorted(filtered["App"].dropna().astype(str).unique().tolist())
    app_choice = st.selectbox("选择应用", app_options, index=0 if "ChatGPT" not in app_options else app_options.index("ChatGPT"))
    trend = monthly_trend(filtered, app=app_choice)
    if trend.empty:
        st.warning("当前数据没有可用的时间字段，无法绘制趋势。")
    else:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.line(trend, x="月份", y="评论数", markers=True, title="月度评论数量变化")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.line(trend, x="月份", y="平均评分", markers=True, title="月度平均评分变化", range_y=[0, 5])
            st.plotly_chart(fig, use_container_width=True)
        fig = px.line(trend, x="月份", y="差评率", markers=True, title="月度差评率变化")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(trend, use_container_width=True, hide_index=True)

# ---------- page 7 ----------
elif page == "7. 关键词与典型评论":
    st.header("关键词与典型评论")
    only_negative = st.checkbox("只分析低分评论关键词", value=True)
    kw = keyword_table(filtered, top_n=30, only_negative=only_negative)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("高频关键词")
        st.dataframe(kw, use_container_width=True, hide_index=True)
    with col2:
        if not kw.empty:
            fig = px.bar(kw.head(20), x="频次", y="关键词", orientation="h", title="关键词频次 Top 20")
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("各应用差异化关键词 TF-IDF")
    tfidf = tfidf_by_app(filtered, top_n=8)
    st.dataframe(tfidf, use_container_width=True, hide_index=True)

    st.subheader("典型评论")
    themes = ["全部"] + sorted(filtered["Review_Theme"].dropna().astype(str).unique().tolist())
    labels = ["全部"] + sorted(filtered["Sentiment_Label"].dropna().astype(str).unique().tolist())
    theme_choice = st.selectbox("主题", themes)
    label_choice = st.selectbox("情感", labels)
    reps = representative_reviews(filtered, theme=theme_choice, sentiment=label_choice, top_n=12)
    st.dataframe(reps, use_container_width=True, hide_index=True)

# ---------- page 8 ----------
elif page == "8. 系统设计说明":
    st.header("系统分析与设计")
    st.subheader("1. 需求分析")
    st.markdown(
        """
**用户需求**：学生、普通用户和产品分析人员希望了解不同生成式 AI 应用的真实用户体验，尤其是用户为什么给好评或差评。

**功能需求**：
1. 支持导入 Kaggle 评论 CSV 数据；
2. 支持字段自动识别、去重、缺失值处理、文本清洗；
3. 支持评分分布、好评率、差评率、平均评分统计；
4. 支持评论情感分析；
5. 支持用户痛点主题识别；
6. 支持多产品横向对比与 ChatGPT 时间趋势分析；
7. 支持典型评论展示，且不展示用户头像、用户名等身份字段。

**非功能需求**：数据来源真实公开；分析结果可解释；系统可直接运行；页面适合课堂十五分钟汇报展示。
        """
    )

    st.subheader("2. 系统架构")
    st.code(
        """
Kaggle 公开评论数据集
        ↓
数据接入层：CSV 上传 / data 目录读取
        ↓
数据预处理层：字段统一、去重、缺失值处理、评分标准化、时间格式转换、文本清洗
        ↓
文本分析层：情感分析、主题/痛点识别、关键词提取、TF-IDF 差异词分析
        ↓
统计分析层：评分分布、产品口碑对比、差评率、情感占比、时间趋势
        ↓
可视化展示层：Streamlit + Plotly 交互式看板
        """,
        language="text",
    )

    st.subheader("3. 数据流程")
    st.markdown(
        """
系统会把不同数据集的字段统一成标准结构。比如第一个数据集中的 `content / score / at / thumbsUpCount`，以及第二个数据集中的 `Review_Text / Star_Rating / Review_Date / Sentiment_Polarity / Review_Theme`，会被统一映射为系统内部字段。

如果数据集中没有情感分数或主题字段，系统会自动用 VADER 情感分析和关键词规则补充；如果数据集中已经提供这些字段，系统会优先使用原字段，并对缺失值补算。
        """
    )

    st.subheader("4. 项目边界")
    st.warning("本系统分析的是应用商店评论中的用户体验口碑，不能直接推出哪个大模型能力最强；汇报时应避免夸大结论。")
