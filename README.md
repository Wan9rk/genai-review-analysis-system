# 生成式 AI 应用用户体验评价与痛点分析系统

这是一个面向“大数据技术与应用”期末汇报的可运行系统。系统基于 Kaggle 公开用户评论数据，分析 ChatGPT、Claude、Gemini、Copilot、Perplexity 等生成式 AI 应用的用户口碑、情感倾向、痛点主题、关键词和时间趋势。

# 1. 题目

**基于多源评论数据的生成式 AI 应用体验评价与痛点分析系统**

# 2. 数据来源

以下两个 Kaggle 数据集的 CSV 文件：

1. `ChatGPT reviews [DAILY UPDATED]`
   - 用途：分析 ChatGPT 单产品的评论数量、评分、差评率和痛点随时间变化。
2. `The Generative AI Ecosystem: 50K User Reviews 2026`
   - 用途：横向比较 ChatGPT、Claude、Gemini、Copilot、Perplexity 等生成式 AI 应用的用户体验差异。

> 注意：CSV 文件不要放入公开仓库。如果课堂展示，在本地 `data/` 目录放置即可。

# 3. 系统功能

- 多 CSV 数据导入：支持页面上传，也支持读取 `data/` 目录。
- 字段自动识别：兼容 `content/score/at/thumbsUpCount` 和 `Review_Text/Star_Rating/Review_Date/Sentiment_Polarity/Review_Theme` 等常见字段。
- 数据清洗：去重、缺失值处理、时间格式统一、评分标准化、文本清洗。
- 口碑分析：平均评分、好评率、差评率、评论量。
- 情感分析：优先使用数据集自带情感字段；缺失时自动用 VADER 计算。
- 痛点识别：基于关键词规则识别回答质量、性能稳定、登录账号、订阅付费、使用限制、功能体验、学习工作等主题。
- 关键词分析：高频关键词、低分评论关键词、各产品 TF-IDF 差异关键词。
- 时间趋势：月度评论数、平均评分、差评率变化。
- 典型评论：按主题和情感筛选代表性评论。

# 4. 安装与运行

## 4.1 创建虚拟环境

```bash
python -m venv .venv
```

Windows：

```bash
.venv\Scripts\activate
```

macOS / Linux：

```bash
source .venv/bin/activate
```

## 4.2 安装依赖

```bash
pip install -r requirements.txt
```

## 4.3 准备数据

方式一：把 Kaggle 下载的 CSV 文件放入项目的 `data/` 目录。

方式二：运行系统后，在页面左侧上传 CSV 文件。

## 4.4 启动系统

```bash
streamlit run app.py
```

浏览器会自动打开本地页面。若未自动打开，终端会显示类似地址：

```text
http://localhost:8501
```

# 5. 标准字段说明

| 字段 | 含义 | 系统用途 |
|---|---|---|
| App | 应用名称 | 区分 ChatGPT、Claude、Gemini、Copilot、Perplexity 等产品 |
| Review_Date | 评论时间 | 用于时间趋势分析 |
| Star_Rating | 用户评分 | 计算平均评分、好评率、差评率 |
| Review_Text | 评论正文 | 情感分析、关键词提取、主题识别 |
| Word_Count | 评论词数 | 辅助判断评论长度 |
| Review_Length_Chars | 评论字符数 | 辅助选择典型评论 |
| Thumbs_Up_Count | 点赞数 | 衡量评论代表性 |
| App_Version | 应用版本 | 可用于版本维度分析 |
| Sentiment_Polarity | 情感极性分数 | 判断评论文本正负倾向 |
| Sentiment_Label | 情感标签 | 正面/中性/负面 |
| Review_Theme | 评论主题 | 识别用户痛点和关注点 |
| Source | 数据来源 | 标记 CSV 来源 |


核心表达：

> 本项目不是简单判断评论正负，而是结合评分、评论文本、应用名称和时间信息，构建生成式 AI 应用的用户口碑画像，分析不同产品的体验优势和主要痛点。

1. 第二个数据集已有情感和主题字段，说明需要做字段统一、清洗、交叉统计、可视化和典型评论分析。
2. 主题识别当前采用可解释的关键词规则，适合课程展示；如果想增强，可以后续替换为机器学习分类模型或 BERTopic。
